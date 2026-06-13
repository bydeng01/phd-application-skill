---
name: application-tracker
description: >-
  Track PhD application status, deadlines, required documents, and follow-up timing across
  many universities at once. Use this whenever the user wants to manage, check, review, or
  get a status update on their applications — e.g. "what deadlines are coming up?", "which
  professors haven't replied?", "what do I still need for the MIT application?", "where am I
  with everything?", "remind me to follow up", or "give me a status update on my PhD apps".
  Reads the application status files and interaction logs in the knowledge base, surfaces
  what's due, missing, or overdue, updates the records, and can set up recurring reminders.
  Trigger whenever the intent is to get oriented across multiple applications or stay on top
  of deadlines and follow-ups, even if the user doesn't say "tracker".
---

# Application tracker

A PhD applicant is running many parallel processes — different deadlines, document
checklists, and pending replies across a dozen labs — and the failure mode is silent: a
missed deadline or a follow-up that never happened costs an entire opportunity. This skill
is the applicant's air-traffic control. Its value is *surfacing* the few things that need
action now out of a mass of state, accurately, so nothing winnable slips.

## What you produce

An updated set of `status.md` files plus a concise **action digest** for the user: what's
overdue, what's due soon, what's missing, and what's waiting on someone else. Accuracy and
prioritization matter more than completeness — a digest that buries the one urgent deadline
under thirty lines of "no action needed" has failed.

## Step 1 — Gather state

Read every `knowledge-base/applications/*/status.md` (the `stage`, `deadline`, `priority`,
checklist, and timeline) and the `knowledge-base/interactions/*.md` logs (what was sent,
when, and any `Follow-up due` dates). Determine today's date with the shell rather than
assuming it — overdue/upcoming calculations depend on it.

## Step 2 — Compute what needs attention

Sort everything into a small number of action buckets, ordered by urgency:

- **Overdue** — a passed application deadline still marked unsubmitted, or a `Follow-up due`
  date in the past with status still "awaiting reply". These are the headline items.
- **Due soon** — deadlines or follow-ups within the next ~14 days. Show the date and the
  days remaining so urgency is legible.
- **Missing documents** — checklist items still pending for applications whose deadline is
  approaching (transcripts, letters, writing samples, test scores). Surface these early
  because documents like recommendation letters have their own lead time.
- **Waiting on others** — sent emails or submitted applications where the ball is in the
  professor's or committee's court; note when a polite follow-up becomes appropriate.
- **No action needed** — everything else, summarized in a single line, not enumerated.

For follow-up timing, respect the dates logged by **outreach-email**; a cold email typically
warrants a follow-up ~2 weeks out, and only one or two follow-ups before moving on.

## Step 3 — Update the records

Where the state has clearly changed, update the `status.md` files: advance `stage`, tick
completed checklist items, correct deadlines you've confirmed. Keep edits faithful to what
you actually know — don't mark something submitted on assumption. If you change a record,
note it so the user can see what moved.

## Step 4 — Deliver the digest

Lead with the action buckets, most urgent first. Be specific and scannable:

```markdown
## PhD application status — <date>

### ⚠ Overdue / act now
- <App>: follow-up to Prof X is 5 days overdue (emailed <date>, no reply) → send follow-up
- ...

### Due within 14 days
- <App>: application deadline <date> (in 9 days); still missing: writing sample

### Waiting on others
- <App>: submitted <date>; committee decisions typically <timeframe>

### On track
- 6 other applications, nothing due in the next two weeks.
```

End with a short recommended next-action list tied to the urgent items (e.g. "draft the
overdue follow-up to Prof X" → hand to **outreach-email**; "request the missing transcript").

## Step 5 — Offer recurring tracking

Staying on top of deadlines is inherently recurring, and the whole point is to catch things
*before* they're missed. Offer to set up a scheduled task (e.g. a Monday-morning digest)
that re-runs this check and surfaces only what needs action that week. Many applicants don't
realize this can run automatically.

## Guardrails

Never invent or guess a deadline or a status — an applicant who relies on a fabricated date
is worse off than one who knows the date is unconfirmed. When a date or requirement is
unverified, say so and flag it for the user to confirm at the source. Don't auto-send
follow-ups; surface that one is due and hand the drafting to outreach-email for the user to
review and send.
