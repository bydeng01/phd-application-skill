# Knowledge-base schemas

Every skill reads and writes the knowledge base, so the files need a shared shape.
Each schema below is the YAML front-matter + section layout for one entity type. Skills
should treat these as the contract: write all the fields, leave a field blank (not absent)
when unknown, and keep the Markdown section headings stable so other skills can find them.

Slugs are lowercase-kebab (`jane-smith-mit`). Dates are ISO (`2026-06-12`).

---

## professor (`knowledge-base/professors/<slug>.md`)

```yaml
---
slug: jane-smith-mit
name: Jane Smith
title: Associate Professor
institution: MIT
department: EECS
lab: Smith Lab
homepage:
scholar:
email:
field: machine learning
last_analyzed: 2026-06-12
fit_score:        # 0–100, set by professor-analyzer
funding_signal:   # strong | mixed | weak | unknown
accepting_students: # yes | no | unknown
---
```

Body sections (stable headings):
`## Research focus` · `## Recent publications` (last ~3 yrs, with takeaways) ·
`## Research agenda & open problems` · `## Funding & grants` · `## Fit with my profile`
(specific overlaps + gaps) · `## Outreach hooks` (concrete things to reference in an email) ·
`## Sources` (links).

---

## opening (`knowledge-base/openings/<slug>.md`)

```yaml
---
slug: smith-lab-rl-2026
professor: jane-smith-mit
institution: MIT
title: PhD in reinforcement learning for robotics
source_url:
discovered: 2026-06-12
deadline:
funding: # fully funded | partial | unknown
status: # new | shortlisted | applied | rejected | offer | declined
---
```

Body: `## Description` · `## Requirements` · `## Why it fits` · `## Notes`.

---

## institution (`knowledge-base/institutions/<slug>.md`)

```yaml
---
slug: mit
name: Massachusetts Institute of Technology
country: USA
admission_model: # direct-to-advisor | program-committee | rotation
gre_required:
english_test:
application_deadline:
funding_model:
---
```

Body: `## Program requirements` · `## Funding` · `## Notes`.

---

## application (`knowledge-base/applications/<id>/status.md`)

`<id>` is `<professor-slug>` or `<institution>-<program>`.

```yaml
---
id: jane-smith-mit
opening: smith-lab-rl-2026
professor: jane-smith-mit
institution: mit
stage: # researching | contacted | replied | applying | submitted | interview | decision
deadline:
priority: # high | medium | low
---
```

Body: `## Checklist` (documents needed + done/pending) · `## Timeline` · `## Notes`.
Companion files in the same folder: `proposal.md`, `sop.md`, `cv.md`, `interview.md`.

---

## interaction log (`knowledge-base/interactions/<professor-slug>.md`)

A reverse-chronological log. Each entry:

```markdown
### 2026-06-12 — sent: cold email
Subject: ...
Summary: ...
Follow-up due: 2026-06-26
Status: awaiting reply
```

---

## profile (`knowledge-base/profile/profile.md`)

```yaml
---
name: Boyuan
field:
subfields: []
degree_seeking: PhD
target_regions: []
target_start: 2027
sources: []        # which boards/databases to search
constraints: []    # funding needs, location, visa, etc.
---
```

Body: `## Research interests` · `## Background` · `## Goals` · `## Dealbreakers`.
