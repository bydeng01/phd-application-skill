---
name: research-proposal
description: >-
  Draft a PhD research proposal or research plan aligned to a specific lab's current and
  future agenda. Use this whenever the user needs a research proposal, project proposal,
  research statement, or research plan for a PhD application or a particular professor —
  e.g. "write a research proposal for the Smith lab", "I need a 2-page research plan for my
  Cambridge application", "draft a PhD proposal on diffusion models for this professor", or
  "help me turn my interests into a proposal that fits her work". Builds a concrete,
  feasible project at the intersection of the lab's open problems and the applicant's
  strengths, grounded in real prior work, as a draft the applicant authors and refines.
  Trigger whenever the intent is to produce a research proposal tied to a PhD opportunity.
---

# Research proposal

A PhD research proposal does two jobs at once: it shows the applicant can think like a
researcher (frame a real problem, propose a credible approach, see the obstacles), and it
demonstrates *specific* fit with the target lab. A proposal that could be sent to any lab in
the field fails the second job. The aim here is a proposal that sits precisely at the
intersection of where the lab is heading and what the applicant can credibly do — concrete
enough to be evaluated, modest enough to be feasible in a PhD, and clearly the applicant's
own thinking.

## Step 1 — Load the lab and the applicant

Read the professor's profile at `knowledge-base/professors/<slug>.md`, focusing on
**Research agenda & open problems** and recent publications — the proposal must connect to
the lab's *trajectory*, not its past. Read the applicant's `profile/profile.md`,
`profile/research-statement.md` (if present), and `profile/cv-master.md` for the methods and
results they can credibly build on.

If no professor profile exists, run **professor-analyzer** first; a proposal not anchored in
the lab's real open problems is just a generic essay. Note any program constraints the user
gives (page/word limit, required structure) and follow them.

## Step 2 — Find the intersection

The core intellectual work: identify a problem that is (a) genuinely open in the lab's
agenda, (b) something the applicant's background gives them a credible angle on, and (c)
scoped to a PhD. Avoid both extremes — a problem the lab has already solved, or a moonshot
no student could make progress on. Prefer a specific, well-motivated question over a broad
theme. It's fine to propose one main thrust with one or two extensions rather than a sprawl.

## Step 3 — Draft the proposal

Use this structure unless the program specifies otherwise. Keep it tight; most PhD proposals
are 1–3 pages.

```markdown
# <Working title>

## Motivation & problem
The specific problem, why it matters, and the gap in current work (cite real papers —
the lab's and the field's). 1–2 paragraphs.

## Background & related work
What's been done, including the lab's relevant work, and what's still open. Show you've
read the literature, including the professor's. Cite specific real papers.

## Proposed research
The core idea and approach. Concrete enough to picture the first experiments. Break into
1–3 aims/phases. State hypotheses and what success would look like.

## Methods & feasibility
How you'd actually do it, what you'd build on (your own skills/results + the lab's
resources), and why it's achievable in a PhD timeframe.

## Risks & alternatives
The main ways it could go wrong and your fallback directions. Including this signals
research maturity — proposals that pretend nothing can fail read as naive.

## Fit with the lab
Why *this* lab: the specific resources, datasets, methods, or expertise that make the
project viable here and not just anywhere. Tie to the professor's open problems by name.

## References
Real citations only.
```

## Step 4 — Keep it honest and the applicant's own

Cite only real papers, and never claim preliminary results the applicant doesn't have —
"preliminary experiments show X" is a fabrication unless X actually happened. Where the
proposal would benefit from a specific the applicant must supply (a dataset they have, a
result from their MS thesis, a concrete prior finding), mark it with `[brackets]` rather
than inventing it. The proposal should read as the applicant's thinking sharpened, not as
generic AI prose — match the voice in their research statement.

## Step 5 — Save and hand off

Write the proposal to `knowledge-base/applications/<id>/proposal.md`. Summarize for the user
the core idea, why it fits this lab, and which `[brackets]` they need to fill. For a
submission-grade document (PDF/Word with formatting), hand off to the `pdf` or `docx` skill.
If the proposal surfaces a strong angle, suggest it can seed the **outreach-email** hook or
the **application-materials** SOP so the application tells one coherent story.

## Guardrails

Follow `shared/references/ethics.md`. The proposal represents the applicant's research
judgment to people deciding whether to mentor them for years — fabricated results or a
misrepresented grasp of the literature are both dishonest and easily caught in interview.
Aim for a strong, real, feasible draft the applicant can stand behind and defend.
