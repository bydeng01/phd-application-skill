# Connectors & data-source integration

This is the retrieval layer for the copilot. Skills that gather evidence about professors,
publications, and openings (professor-analyzer, position-discovery) should use the tools and
sources here in a defined priority order, with graceful fallback, so they degrade rather than
fail when a source is unavailable.

## Tool priority (use the best available, fall back cleanly)

1. **Dedicated MCP connector** for the source, *if installed* (e.g. an arXiv or Scholar
   connector). Check first — none are guaranteed. If a relevant connector exists but isn't
   connected, surface it to the user (the registry can suggest connectors) rather than
   silently skipping richer data.
2. **Free scholarly APIs via `web_fetch`** — OpenAlex, arXiv, Crossref, Semantic Scholar,
   Europe PMC. These return structured JSON/XML and are the highest-signal source for a
   professor's *recent* publication record. Use the query recipes below. The bundled helper
   `scripts/scholar_lookup.py` builds the right URLs and parses the responses.
3. **WebSearch** — always available and reliable. The dependable grounded fallback for
   anything the APIs don't cover: lab "join us" pages, grant news, faculty bios, position
   boards. Prefer this over guessing; it is the floor that should always be hit.
4. **Chrome browser tools** — for JavaScript-rendered pages that `web_fetch` returns empty
   (Google Scholar profiles, some lab sites, some job boards). Navigate then read page text.

**Important:** if `web_fetch` times out or returns nothing for an API (it can be flaky
depending on environment), do not retry endlessly — fall back to WebSearch and note in the
output that structured-API enrichment was unavailable. Never fabricate to fill the gap.

## Scholarly API recipes

These are stable public APIs (no key required for basic use; OpenAlex appreciates a
`mailto=` param for the polite pool). The helper script wraps them; the recipes are here so
the reasoning is transparent.

### OpenAlex (best for a professor's recent works) — `https://api.openalex.org`
- Find the author: `/authors?search=<name>` → take the best match, optionally disambiguating
  by `last_known_institution`. Capture the author id (e.g. `A5023888391`).
- Their recent works: `/works?filter=author.id:<id>,from_publication_date:<YYYY-MM-DD>&sort=publication_date:desc&per_page=25`
- Per work, read: `title`, `publication_year`, `primary_location.source.display_name`
  (venue), `doi`, `cited_by_count`, and `abstract_inverted_index` (reconstruct for a summary).
- Recency is the point: filter to the last ~3 years and sort descending.

### arXiv (preprints; CS/physics/math/quant-bio) — `http://export.arxiv.org/api/query`
- `?search_query=au:<Last_First>&sortBy=submittedDate&sortOrder=descending&max_results=20`
- Returns Atom XML; read `entry/title`, `entry/published`, `entry/summary`, `entry/id`.

### Crossref (DOIs, venues across publishers) — `https://api.crossref.org`
- `/works?query.author=<name>&sort=published&order=desc&rows=20`

### Semantic Scholar — `https://api.semanticscholar.org/graph/v1`
- Author search: `/author/search?query=<name>` → `/author/<id>/papers?fields=title,year,venue,abstract,citationCount&limit=25`

### Europe PMC (life sciences / medicine) — `https://www.ebi.ac.uk/europepmc/webservices/rest/search`
- `?query=AUTH:"<Last F>"&format=json&sort=P_PDATE_D desc&pageSize=25`

## Position-board sources (for position-discovery)

No dedicated connectors are registered for these; use WebSearch (and Chrome for rendered
listings), targeting:
- **FindAPhD** (`findaphd.com`), **EURAXESS** (`euraxess.ec.europa.eu`), **jobs.ac.uk** —
  advertised funded projects, mostly UK/EU.
- **University department / lab pages** — "join us", "prospective students", "open positions".
- **Field mailing lists / social** — many openings are announced informally.
Always verify currency on the primary page before recording an opening (see ethics.md).

## Validating the API path in your environment

Reachability of the scholarly APIs depends on the host environment's network allowlist. To
check whether they're reachable where the copilot runs, and that the parser still matches the
live response shape:

```
# 1. See the exact URLs the lookup will call (no network):
python3 skills/professor-analyzer/scripts/scholar_lookup.py "Sergey Levine" --dry-run

# 2. Validate the parser against realistic OpenAlex/arXiv payloads (no network):
python3 skills/professor-analyzer/scripts/test_scholar_lookup.py

# 3. Live check — run where api.openalex.org / export.arxiv.org are reachable:
python3 skills/professor-analyzer/scripts/scholar_lookup.py "Sergey Levine" --institution "UC Berkeley" --since 2023 --max 5
```

If step 3 prints a `NOTICE` (403, timeout, etc.), the APIs aren't reachable there — the skill
falls back to WebSearch automatically, which is fine. The parser contract is covered by the
offline tests, so when the hosts *are* reachable the lookup will parse them correctly. (Note:
OpenAlex uses `last_known_institutions` as a list in its current schema; the lookup supports
both that and the deprecated singular form.)

## Plugging in a dedicated connector later

When an academic or job-board MCP connector becomes available and is installed, prefer it at
priority 1: it will be faster and more reliable than scraping. The skills are written against
*capabilities* ("find this author's recent works"), not specific tools, so adding a connector
is a matter of using it in place of the API/WebSearch step — no skill rewrite needed.
