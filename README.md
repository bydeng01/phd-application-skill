# PhD Application Copilot

An AI skill suite that automates the slow, repetitive parts of applying for a PhD —
finding openings, analyzing professors, drafting outreach, tailoring materials, and
tracking deadlines — while keeping everything you send personal and authentic.

It is **field-agnostic**: your research area, target regions, and preferred sources are
configured once in `knowledge-base/profile/profile.md`, and the same skills work whether
you're applying in machine learning, molecular biology, or medieval history.

## How it works

The system is a set of focused **skills** that share a **knowledge base** of Markdown
files. Skills don't call each other; they read and write the same files (a "blackboard").
That makes every step inspectable and hand-editable, and the whole thing version-controlled.

```
skills/            the suite — each dir is one skill with a SKILL.md
knowledge-base/    your data: profile, professors, openings, applications, interactions
shared/schemas/    the agreed-upon shape of each knowledge-base file
ARCHITECTURE.md    full design: skills, collaboration, data sources, roadmap
```

## Quickstart

1. Fill in `knowledge-base/profile/profile.md` (who you are, what you want, where to look)
   and `profile/cv-master.md` (your full CV).
2. Ask Claude to analyze a professor — e.g. *"Do a deep dive on Prof. Jane Smith at MIT
   for fit with my background."* The **professor-analyzer** skill writes a profile to
   `knowledge-base/professors/`.
3. From there, draft outreach, rank opportunities, or tailor materials — each skill picks
   up the files the previous one wrote.

## Build status

| Skill | Status |
|---|---|
| professor-analyzer | 🔨 first to build (Phase 1) |
| position-discovery | 📋 planned (Phase 2) |
| opportunity-ranker | 📋 planned (Phase 2) |
| outreach-email | 📋 planned (Phase 3) |
| application-tracker | 📋 planned (Phase 3) |
| research-proposal | 📋 planned (Phase 4) |
| application-materials | 📋 planned (Phase 4) |
| phd-copilot | 📋 planned (Phase 5) |
| interview-prep | 📋 planned (Phase 5) |

See `ARCHITECTURE.md` for the full design and rationale.
