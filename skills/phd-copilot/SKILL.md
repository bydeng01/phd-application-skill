---
name: phd-copilot
description: >-
  Orchestrate the end-to-end PhD application process and route to the right sub-skill. Use
  this as the front door whenever the user expresses a broad PhD-application intent without
  naming a specific step — e.g. "help me apply for PhDs", "be my PhD application copilot",
  "where am I with my applications and what should I do next?", "I want to start applying to
  PhD programs", or "what's the next thing I should work on?". Surveys the knowledge base to
  see what stage each opportunity is at, recommends the highest-value next action, and kicks
  off the matching skill. Trigger for orientation, planning, or whole-pipeline requests;
  defer to the specific skill when the user already names a concrete task (e.g. "write a cold
  email to Prof X" → outreach-email).
---

# PhD copilot (orchestrator)

This is the front door for someone who knows they want help with PhD applications but not
which of the nine steps they need right now. Its value is orientation and momentum: look at
where things actually stand, name the single most useful next move, and hand off to the skill
that does it. It coordinates; it doesn't duplicate the specialized skills' work.

## The pipeline it coordinates

```
position-discovery → professor-analyzer → opportunity-ranker → outreach-email
        → research-proposal / application-materials → application-tracker → interview-prep
```

Each step reads and writes the shared knowledge base, so progress is visible as files. The
copilot's job is to read that state and figure out what's missing or what's next.

## Step 1 — Survey the state

Read across the knowledge base to build a picture:

- `profile/profile.md` and `profile/cv-master.md` — is the applicant's own profile filled in
  enough to drive everything else? If it's empty, that's almost always the first action.
- `openings/` — are there discovered opportunities? `openings/_ranking.md` — has anything
  been prioritized?
- `professors/` — which targets have been analyzed?
- `applications/*/status.md` — what stage is each application at?
- `interactions/` — any outreach sent, any follow-ups due?

## Step 2 — Diagnose the next best action

Map the state to the pipeline and pick the highest-leverage next step. Heuristics:

- **Empty profile** → set up `profile/profile.md` and `cv-master.md` first; everything
  downstream depends on it.
- **Profile but no openings/targets** → run **position-discovery** (or analyze a professor
  the user already has in mind with **professor-analyzer**).
- **Several analyzed targets, nothing prioritized** → run **opportunity-ranker**.
- **A ranked shortlist, no outreach** → draft outreach for the top targets with
  **outreach-email**.
- **Outreach sent / deadlines approaching** → run **application-tracker** to surface what's
  due, missing, or overdue.
- **An active application needing documents** → **application-materials** / **research-proposal**.
- **An interview scheduled** → **interview-prep**.

When the user's request implies a specific step ("write a cold email", "rank these"), don't
re-survey everything — just route to that skill. The copilot is for ambiguity and planning,
not a tollgate on every action.

## Step 3 — Recommend and hand off

Give the user a brief, honest status overview and a clear recommended next action (usually
one, at most a few in priority order), then invoke the matching skill — keeping the applicant
in control of anything that gets sent or submitted. If several things are genuinely parallel
(e.g. analyze three professors), say so and offer to proceed.

For a recurring rhythm — a weekly "here's where you are and what's due" check — offer to set
up a scheduled task that runs the survey and surfaces the week's actions. This turns the
copilot into an ongoing assistant rather than a one-off.

## Guardrails

Respect `shared/references/ethics.md` across everything it coordinates: draft-never-send,
ground in real material, favor focused effort over mass applications. The copilot should make
the process feel manageable and honest — surfacing real next steps and real status, never
manufacturing false progress or urgency. When the knowledge base is too empty to advise well,
the right move is to help the applicant set up their profile, not to guess.
