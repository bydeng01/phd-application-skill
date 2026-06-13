---
name: interview-prep
description: >-
  Prepare the applicant for a PhD interview with a professor or admissions committee. Use this
  whenever the user has an interview coming up or wants to rehearse — e.g. "I have an
  interview with Prof X next week, help me prepare", "what will they ask me?", "prep me for my
  PhD interview", "can we do a mock interview?", or "what questions should I expect from the
  admissions committee?". Generates likely questions grounded in the professor's real work and
  the applicant's own materials, with model answers in the applicant's voice and coaching
  notes, and can run an interactive mock. Trigger whenever the intent is to get ready for a
  PhD interview, even if the user doesn't say "interview prep".
---

# Interview prep

A PhD interview is a two-way fit conversation: the professor is checking whether the
applicant thinks well, knows their own work, and would be good to mentor; the applicant is
checking whether the lab is right for them. Good preparation isn't memorizing answers — it's
anticipating the real questions this specific professor would ask and having thought through
genuine, specific responses. The aim is for the applicant to walk in able to speak
confidently about their work, the lab's work, and the connection between them.

## Step 1 — Load the context

Read the professor's profile at `knowledge-base/professors/<slug>.md` (agenda, recent
papers, open problems), the application materials at `knowledge-base/applications/<id>/`
(the SOP and proposal — they'll be asked about), and the applicant's `profile/` (background
and the work they'll be expected to discuss). The more the questions are tied to *this*
professor's actual research, the more useful the prep.

If no professor profile exists, run **professor-analyzer** first — generic interview
questions are far less useful than ones grounded in the specific lab.

## Step 2 — Generate questions across the real categories

Cover the categories a PhD interview actually spans. For each question, write a *model
answer* drawn from the applicant's real material plus a short coaching note on what the
interviewer is really probing and how to handle it well.

- **Motivation & fit** — why a PhD, why this lab, why now. (Probing: genuine, specific
  interest vs. scattershot applying.)
- **The applicant's own work** — deep questions about their MS thesis / projects / papers:
  why this approach, what they'd do differently, what they learned. (Probing: do they own
  their work and think critically about it.)
- **The proposed research / the lab's work** — questions about their proposal and the
  professor's recent papers. (Probing: can they engage with the lab's actual problems.)
- **Technical depth** — field-appropriate fundamentals the professor would expect.
  (Probing: foundations and how they reason through a problem.)
- **Behavioral / working style** — collaboration, handling failure, independence.
- **Questions the applicant should ask back** — thoughtful questions about the lab
  (funding, mentorship style, current projects, where students go after). Asking good
  questions is itself evaluated, and helps the applicant choose well.

Prioritize questions this specific professor is *likely* to ask given their work, not a
generic bank. Where a strong answer needs a specific only the applicant has, mark it with
`[brackets]` and coach them on how to fill it.

## Step 3 — Save and offer a mock

Write the prep to `knowledge-base/applications/<id>/interview.md`: questions grouped by
category, each with a model answer and a coaching note, plus the applicant's questions-to-ask
and a short list of likely-discussed papers to review beforehand.

Then offer an **interactive mock interview**: you play the professor, ask questions one at a
time, let the applicant answer, and give specific feedback. This rehearsal is where prep
turns into confidence — many applicants want it once they see the question list.

## Guardrails

Per `shared/references/ethics.md`, model answers must be grounded in the applicant's real
experience — coach them to articulate what's true, not to memorize impressive-sounding
fabrications they can't back up under follow-up questioning (interviews are designed to
expose exactly that). Keep the tone encouraging and constructive; the goal is a prepared,
confident applicant who can have a genuine conversation, not a scripted one.
