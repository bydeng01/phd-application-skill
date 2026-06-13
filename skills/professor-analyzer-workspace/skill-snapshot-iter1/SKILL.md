---
name: professor-analyzer
description: >-
  Deep-dive a professor or research lab to assess PhD fit. Use this whenever the user
  wants to research, analyze, profile, or "look into" a potential PhD supervisor, advisor,
  faculty member, or lab — including questions like "is Prof X a good fit for me?", "what
  is this lab working on?", "analyze Professor Smith's recent work", "should I email this
  professor?", or when they paste a faculty page, Google Scholar link, or lab URL and want
  it understood. Gathers recent publications, grants, lab agenda, and open problems, then
  scores fit against the applicant's profile and surfaces concrete outreach hooks. Writes a
  structured profile to knowledge-base/professors/. Trigger even if the user doesn't say
  the word "analyze" — any intent to evaluate a specific researcher for PhD applications
  should use this skill.
---

# Professor / lab analyzer

This is the load-bearing skill of the PhD copilot: outreach emails, proposals, and ranking
all consume the profile it produces. The goal is a profile so specific that a cold email
built from it could only have been written to *this* professor — the opposite of generic.

## What you produce

A single file at `knowledge-base/professors/<slug>.md` following the **professor schema**
in `shared/schemas/README.md` (read it for the exact front-matter fields and section
headings). Match that shape exactly so downstream skills can parse it.

## Step 1 — Load context

Read `knowledge-base/profile/profile.md` (and `profile/cv-master.md` if fit detail is
needed). You cannot assess "fit" without knowing the applicant's interests, background, and
dealbreakers. If the profile is empty, ask the user for their research interests before
proceeding — fit scoring is meaningless otherwise.

Identify the professor from the user's request: a name + institution, a homepage, a Scholar
profile, or a lab URL.

## Step 2 — Gather evidence

Use `shared/references/data-sources.md` for where to look. Prioritize *recency* — a PhD
starts in 1–2 years, so what matters is where the lab is heading, not its decade-old
greatest hits. Aim to ground every later claim in a real source.

Gather, roughly in priority order:

- **Recent publications (last ~3 years).** Titles, venues, and — crucially — the *takeaway*
  of each: what problem, what approach, what's new. Use publication search (arXiv, Semantic
  Scholar/OpenAlex, Scholar, PubMed as fits the field). Static pages → web fetch; rendered
  pages like Google Scholar → browser tools.
- **Lab website / "join us" page.** Current projects, stated open problems, whether they're
  recruiting, funding mentions.
- **Grants / funding signals.** Active grants suggest funded positions. Note explicitly
  when funding is unclear — don't guess.
- **Research trajectory.** Read across the recent papers for the *direction*: what thread
  is the lab pulling on, what will the next few papers likely be about?

If a source can't be fetched, note the gap rather than fabricating around it.

## Step 3 — Assess fit

This is the part that makes the profile useful. Compare the professor's trajectory against
the applicant's profile and be honest and specific:

- **Overlaps** — concrete intersections between their open problems and the applicant's
  interests/skills. Name the paper and the matching part of the applicant's background.
- **Gaps** — where the applicant lacks relevant background, or the lab's direction diverges
  from their goals. Real assessment includes the misses.
- **fit_score (0–100)** — your overall judgment, justified by the overlaps/gaps above, not
  a vibe. Reserve 80+ for strong, well-evidenced matches.
- **Funding & "accepting students"** signals, set honestly to `unknown` when unclear.

## Step 4 — Outreach hooks

The payoff section. List 2–4 *specific* things the applicant could reference in a first
email: a particular recent paper and a genuine, substantive reaction or question; a
connection between one of their projects and the applicant's work; an open problem the
applicant is positioned to contribute to. These must be real and specific — they are what
separates an authentic email from spam. No flattery, no invented enthusiasm.

## Step 5 — Write the file

Write `knowledge-base/professors/<slug>.md` with all schema fields and a `## Sources`
section linking everything you used. Then give the user a short summary: the fit verdict,
the single strongest hook, and any gap they should be aware of. If you found a clear
opening, suggest the natural next step (e.g. drafting outreach).

## Guardrails

Follow `shared/references/ethics.md`. The cardinal rule: never invent a publication,
finding, grant, or shared interest. If you're unsure whether something is real, mark it
uncertain and cite what you actually found. A profile that honestly says "weak fit" is more
valuable than a flattering one that wastes the applicant's outreach on a bad match.
