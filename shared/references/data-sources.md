# Data sources reference

Shared across skills. The applicant's `profile/profile.md` `sources:` list narrows these
to what's relevant for their field and region. When a source needs a connector that isn't
installed, surface it to the user rather than failing silently.

## Publications & researcher profiles
- **arXiv** — preprints (CS, physics, math, quant-bio). Free API/search.
- **Semantic Scholar / OpenAlex** — cross-field metadata, citations, author profiles. Free APIs.
- **Google Scholar** — broad coverage incl. h-index; often needs the browser (rendered page).
- **OpenReview** — ML/AI conference submissions + reviews; reveals active research threads.
- **PubMed / Europe PMC** — life sciences & medicine.
- **CrossRef** — DOIs and citation metadata across publishers.

## Open positions
- **FindAPhD** — advertised, mostly UK/EU funded projects.
- **EURAXESS** — EU-wide research positions and funding.
- **jobs.ac.uk** — UK academic jobs incl. PhD studentships.
- **University department / lab pages** — "join us", "open positions", "prospective students".
- **Field mailing lists & X/Twitter / Mastodon** — many openings are announced informally.

## Funding
- National schemes (configured per region), program pages, fellowship databases.

## Tools the skills use
- **WebSearch** for discovery; **web_fetch** for static pages; **browser tools** for
  JS-rendered pages (Scholar, some lab sites).
- **Email / calendar connectors** (optional) for outreach tracking and deadlines.
- **docx / pdf** skills for submission-grade documents.

## Etiquette
Respect robots and rate limits; prefer official APIs over scraping. Outreach should be
targeted, not bulk — see `ethics.md`.
