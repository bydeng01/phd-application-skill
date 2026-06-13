# Cold email draft — Prof. Sergey Levine (UC Berkeley, EECS)

## Read this first: an important caveat

Before you send anything, you should know: **Prof. Levine's faculty page explicitly says he
will NOT reply to PhD admissions emails.** He directs prospective students to apply to the
Berkeley EECS PhD program and list him as a faculty of interest. Cold "please take me on as a
student" emails are discouraged and will very likely go unanswered.

So I have **not** written a "will you take me?" pitch — that's the surest way to get ignored
here. Two honest options:

1. **(Recommended) Apply to the Berkeley EECS PhD program and name him there.** This is the
   route he actually asks for. Your outreach energy is better spent on a strong SOP that names
   him and connects your sim-to-real / domain-randomization work to his real-world-RL agenda.
   No cold email needed — and arguably it's counterproductive to send one.

2. **A short, substantive research note (not an admissions ask).** If you still want to make
   contact, the only version with a chance is a genuine, specific question or observation about
   his work that stands on its own — something a curious researcher would send regardless of
   admissions. It must NOT ask him to advise you. That's the draft below. Use it only if you
   have a real question you actually want answered; otherwise go with option 1.

Tell me which you'd prefer and I can adjust.

---

## Draft (option 2 — substantive research note, no admissions ask)

**Subject:** Sim priors to cut the human-correction budget in HiL-SERL?

Dear Prof. Levine,

I'm Test Applicant, an MS CS student (graduating 2026) working on sim-to-real RL for robotic
manipulation — my one published piece is a workshop paper on domain randomization for sim-to-real
pick-and-place.

Reading the HiL-SERL results (the ~100% success on dexterous tasks with human-in-the-loop
corrections) left me with a concrete question: how much of the human-correction budget do you
think is fundamentally irreducible, versus how much could be front-loaded into better sim priors
before the policy ever touches hardware? In my own pick-and-place pipeline [add the specific
result/number you saw, e.g. "domain randomization cut real-world correction episodes by X%"],
the corrections that remained were almost all [contact-rich / perception edge cases — name
which], which made me wonder whether a sim prior can ever cover those or whether HiL is the
right tool there by design.

No need for a detailed reply — even a one-line steer on whether that framing is naive would be
genuinely useful. Thanks for putting so much of this work out in the open.

Best,
Test Applicant
[link to your workshop paper / personal page]

---

## Brackets you must fill before sending
- `[add the specific result/number you saw …]` — a real figure from your sim-to-real pipeline.
  Do not send an empty or invented number.
- `[contact-rich / perception edge cases — name which]` — which corrections actually remained.
- `[link to your workshop paper / personal page]` — your real link.

## Why this hook
I chose HiL-SERL (from his Outreach hooks) over pi0.5 because your domain-randomization /
sim-to-real work connects to it directly and specifically: "better sim priors to reduce the
human-correction budget" is a real, two-sided research question you're credibly positioned to
ask, not flattery. I deliberately framed it as a question, not an admissions request, because
his Notes rule the latter out.

## Honest fit note
The topical fit (sim-to-real ⊂ his real-world-RL agenda) is genuinely strong — fit_score 88 in
your KB. The obstacle is purely the channel: email is the wrong channel for the admissions ask
here. Put the strong-fit case in your EECS application and SOP.

## Next step
I have **not** sent this (and won't — you always send yourself). If you go with option 1, no
send is needed at all. If you send option 2, I've logged it with a follow-up date, but for a
note like this I'd honestly not follow up — silence is a fine answer to a research question.
