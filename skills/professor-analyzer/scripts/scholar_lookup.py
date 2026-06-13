#!/usr/bin/env python3
"""
scholar_lookup.py — fetch a researcher's RECENT publications from free scholarly APIs.

Primary source: OpenAlex (author resolution + recent works, with abstracts).
Fallback source: arXiv (preprints), used if --source arxiv or if OpenAlex returns nothing.

The professor-analyzer skill uses this to ground its profile in real, recent work instead of
relying on the model's memory. It degrades gracefully: on any network failure it prints a
clear NOTICE and exits non-zero so the skill knows to fall back to WebSearch — it never
invents data.

Usage:
    python scholar_lookup.py "Sergey Levine" --institution "UC Berkeley" --since 2023 --max 25
    python scholar_lookup.py "Jane Smith" --source arxiv --max 20
    python scholar_lookup.py "Sergey Levine" --dry-run      # print the API URLs, fetch nothing

Output: JSON to stdout — {author, source, works:[{title, year, venue, doi, citations, abstract}]}
Designed to be read by the model, not chained into other code, so the shape is forgiving.
"""
import argparse, json, sys, urllib.parse, urllib.request
from datetime import date

OPENALEX = "https://api.openalex.org"
ARXIV = "http://export.arxiv.org/api/query"
UA = {"User-Agent": "phd-application-copilot/1.0 (mailto:example@example.com)"}
TIMEOUT = 25


def _get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read()


def _institution_name(author):
    """OpenAlex moved from `last_known_institution` (object) to `last_known_institutions`
    (list). Support both so the lookup works across API versions."""
    insts = author.get("last_known_institutions")
    if isinstance(insts, list) and insts:
        return insts[0].get("display_name", "") or ""
    single = author.get("last_known_institution") or {}
    return single.get("display_name", "") or ""


def _reconstruct_abstract(inv):
    """OpenAlex stores abstracts as an inverted index {word: [positions]}; rebuild the text."""
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))[:1200]


def openalex_urls(name, institution, since):
    author_url = f"{OPENALEX}/authors?search={urllib.parse.quote(name)}&per_page=5&mailto=example@example.com"
    # works URL is templated once we know the author id; show the shape in dry-run
    works_tmpl = (f"{OPENALEX}/works?filter=author.id:<AUTHOR_ID>,"
                  f"from_publication_date:{since}-01-01&sort=publication_date:desc&per_page=25&mailto=example@example.com")
    return author_url, works_tmpl


def openalex(name, institution, since, max_n):
    author_url, _ = openalex_urls(name, institution, since)
    data = json.loads(_get(author_url))
    results = data.get("results", [])
    if not results:
        return None
    # pick best match, preferring institution substring if given
    chosen = results[0]
    if institution:
        inst_l = institution.lower()
        for a in results:
            if inst_l in _institution_name(a).lower():
                chosen = a
                break
    aid = chosen["id"].rsplit("/", 1)[-1]
    works_url = (f"{OPENALEX}/works?filter=author.id:{aid},"
                 f"from_publication_date:{since}-01-01&sort=publication_date:desc&per_page={max_n}&mailto=example@example.com")
    wdata = json.loads(_get(works_url))
    works = []
    for w in wdata.get("results", []):
        loc = (w.get("primary_location") or {}).get("source") or {}
        works.append({
            "title": w.get("title"),
            "year": w.get("publication_year"),
            "venue": loc.get("display_name"),
            "doi": w.get("doi"),
            "citations": w.get("cited_by_count"),
            "abstract": _reconstruct_abstract(w.get("abstract_inverted_index")),
        })
    return {
        "author": chosen.get("display_name"),
        "openalex_id": aid,
        "institution": _institution_name(chosen),
        "source": "openalex",
        "works": works,
    }


def arxiv_url(name, max_n):
    last_first = "_".join(reversed(name.split()[:2])) if len(name.split()) >= 2 else name
    q = urllib.parse.quote(f"au:{last_first}")
    return f"{ARXIV}?search_query={q}&sortBy=submittedDate&sortOrder=descending&max_results={max_n}"


def arxiv(name, max_n):
    import xml.etree.ElementTree as ET
    raw = _get(arxiv_url(name, max_n))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(raw)
    works = []
    for e in root.findall("a:entry", ns):
        works.append({
            "title": (e.findtext("a:title", default="", namespaces=ns) or "").strip(),
            "year": (e.findtext("a:published", default="", namespaces=ns) or "")[:4],
            "venue": "arXiv preprint",
            "doi": e.findtext("a:id", default="", namespaces=ns),
            "citations": None,
            "abstract": (e.findtext("a:summary", default="", namespaces=ns) or "").strip()[:1200],
        })
    return {"author": name, "source": "arxiv", "works": works}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("name")
    ap.add_argument("--institution", default="")
    ap.add_argument("--since", type=int, default=date.today().year - 3)
    ap.add_argument("--max", type=int, default=25)
    ap.add_argument("--source", choices=["openalex", "arxiv"], default="openalex")
    ap.add_argument("--dry-run", action="store_true", help="print the API URLs and exit; fetch nothing")
    args = ap.parse_args()

    if args.dry_run:
        a_url, w_tmpl = openalex_urls(args.name, args.institution, args.since)
        print(json.dumps({
            "dry_run": True,
            "openalex_author_search": a_url,
            "openalex_works_template": w_tmpl,
            "arxiv_query": arxiv_url(args.name, args.max),
        }, indent=2))
        return 0

    try:
        if args.source == "arxiv":
            out = arxiv(args.name, args.max)
        else:
            out = openalex(args.name, args.institution, args.since, args.max)
            if not out or not out.get("works"):
                sys.stderr.write("NOTICE: OpenAlex returned no works; trying arXiv fallback.\n")
                out = arxiv(args.name, args.max)
        if not out or not out.get("works"):
            sys.stderr.write("NOTICE: no works found via APIs. Fall back to WebSearch; do not fabricate.\n")
            print(json.dumps({"author": args.name, "source": "none", "works": []}))
            return 2
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0
    except Exception as e:  # network error, timeout, parse error
        sys.stderr.write(f"NOTICE: scholarly API unavailable ({type(e).__name__}: {e}). "
                         f"Fall back to WebSearch; do not fabricate publications.\n")
        print(json.dumps({"author": args.name, "source": "error", "works": []}))
        return 3


if __name__ == "__main__":
    sys.exit(main())
