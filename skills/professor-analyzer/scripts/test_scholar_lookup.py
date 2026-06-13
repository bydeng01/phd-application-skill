#!/usr/bin/env python3
"""
Offline validation for scholar_lookup.py.

This environment can't reach the live scholarly APIs (sandbox allowlist / web_fetch limits),
so we validate the part that actually matters — that the parser correctly consumes the REAL
response shapes of OpenAlex and arXiv — by mocking the network layer with realistic fixtures
captured from the documented API schemas. Run: `python3 test_scholar_lookup.py`

For a true live check in an environment with network access, see the command printed at the end.
"""
import json
import scholar_lookup as s

# --- Realistic OpenAlex fixtures (current schema: last_known_institutions is a LIST) ---
OPENALEX_AUTHORS = {
    "results": [
        {
            "id": "https://openalex.org/A5023888391",
            "display_name": "Sergey Levine",
            "works_count": 600,
            "last_known_institutions": [
                {"id": "https://openalex.org/I95457486", "display_name": "University of California, Berkeley"}
            ],
        },
        {
            "id": "https://openalex.org/A9999999999",
            "display_name": "Sergey Levine",
            "works_count": 12,
            "last_known_institutions": [
                {"display_name": "Some Other University"}
            ],
        },
    ]
}

OPENALEX_WORKS = {
    "results": [
        {
            "title": "Sample-Efficient Real-World Reinforcement Learning",
            "publication_year": 2025,
            "doi": "https://doi.org/10.1234/abcd",
            "cited_by_count": 42,
            "primary_location": {"source": {"display_name": "Science Robotics"}},
            "abstract_inverted_index": {"We": [0], "present": [1], "a": [2], "method": [3]},
        },
        {
            "title": "Generalist Robot Policies",
            "publication_year": 2024,
            "doi": None,
            "cited_by_count": 10,
            "primary_location": {"source": None},
            "abstract_inverted_index": None,
        },
    ]
}

# --- Realistic arXiv Atom fixture ---
ARXIV_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2501.00001v1</id>
    <published>2025-01-02T00:00:00Z</published>
    <title>Tactile Sim-to-Real Transfer</title>
    <summary>We study tactile randomization for in-hand manipulation.</summary>
  </entry>
</feed>"""


def test_openalex():
    calls = {"n": 0}

    def fake_get(url):
        calls["n"] += 1
        if "/authors" in url:
            assert "search=" in url, "author search URL malformed"
            return json.dumps(OPENALEX_AUTHORS).encode()
        if "/works" in url:
            assert "author.id:A5023888391" in url, "should query the institution-matched author id"
            assert "from_publication_date:2023-01-01" in url, "should apply recency filter"
            return json.dumps(OPENALEX_WORKS).encode()
        raise AssertionError("unexpected URL: " + url)

    s._get = fake_get
    out = s.openalex("Sergey Levine", "Berkeley", 2023, 25)
    assert out["author"] == "Sergey Levine"
    assert out["openalex_id"] == "A5023888391", "institution disambiguation failed"
    assert out["institution"] == "University of California, Berkeley"
    assert len(out["works"]) == 2
    w0 = out["works"][0]
    assert w0["title"].startswith("Sample-Efficient")
    assert w0["year"] == 2025
    assert w0["venue"] == "Science Robotics"
    assert w0["citations"] == 42
    assert w0["abstract"] == "We present a method", "abstract reconstruction failed"
    # work with null source/abstract must not crash
    assert out["works"][1]["venue"] is None
    assert out["works"][1]["abstract"] == ""
    print("PASS  openalex parsing + institution disambiguation + abstract reconstruction")


def test_openalex_singular_institution_backcompat():
    # Older payloads used singular last_known_institution (object) — must still work.
    author = {"id": "https://openalex.org/A1", "display_name": "X",
              "last_known_institution": {"display_name": "Old Field University"}}
    assert s._institution_name(author) == "Old Field University"
    print("PASS  backward-compat with deprecated singular last_known_institution")


def test_arxiv():
    s._get = lambda url: ARXIV_XML
    out = s.arxiv("Jane Smith", 20)
    assert out["source"] == "arxiv"
    assert len(out["works"]) == 1
    assert out["works"][0]["title"] == "Tactile Sim-to-Real Transfer"
    assert out["works"][0]["year"] == "2025"
    assert "tactile" in out["works"][0]["abstract"].lower()
    print("PASS  arxiv Atom parsing")


def test_fallback_on_empty_openalex():
    # OpenAlex returns no authors -> openalex() returns None -> main() should fall back to arXiv
    def fake_get(url):
        if "/authors" in url:
            return json.dumps({"results": []}).encode()
        return ARXIV_XML
    s._get = fake_get
    out = s.openalex("Nobody", "", 2023, 25)
    assert out is None, "empty author search should return None to trigger fallback"
    print("PASS  empty-result handling triggers fallback path")


if __name__ == "__main__":
    test_openalex()
    test_openalex_singular_institution_backcompat()
    test_arxiv()
    test_fallback_on_empty_openalex()
    print("\nAll parsing-contract tests passed.")
    print("Live check (run where the API hosts are reachable):")
    print('  python3 scholar_lookup.py "Sergey Levine" --institution "UC Berkeley" --since 2023 --max 5')
