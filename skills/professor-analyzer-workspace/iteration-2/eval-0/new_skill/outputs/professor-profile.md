---
slug: sergey-levine-uc-berkeley
name: Sergey Levine
title: Associate Professor
institution: UC Berkeley
department: EECS
lab: Robotic AI & Learning Lab (RAIL), part of BAIR
homepage: https://people.eecs.berkeley.edu/~svlevine/
scholar: https://scholar.google.com/citations?user=8R35rCwAAAAJ&hl=en
email: (intentionally omitted — see Notes; he asks prospective students NOT to email about admissions)
field: machine learning / robotics
last_analyzed: 2026-06-12
fit_score: 82
funding_signal: strong
accepting_students: yes
---

# Sergey Levine — UC Berkeley (RAIL / BAIR)

> Note on evidence: the bundled `scholar_lookup.py` helper could not reach OpenAlex/arXiv in this
> environment (network blocked — `URLError: Tunnel connection failed: 403 Forbidden`). Per the
> skill's fallback rule, all publications and facts below were gathered via WebSearch and
> first-party pages (EECS faculty page, lab/BAIR pages, arXiv abstract pages). Structured-index
> enrichment (exact citation counts, full publication list) was therefore unavailable, so some
> per-paper metadata is marked accordingly. No publications were invented.

## Research focus

Machine learning for decision-making and control, with an emphasis on deep and reinforcement
learning. Historically: end-to-end training of deep neural-network policies combining perception
and control, deep RL algorithms, and inverse RL. His current center of gravity has shifted toward
**robotic foundation models** and **vision-language-action (VLA) models** for general-purpose
robot control — he co-founded Physical Intelligence (Pi) in 2024 and now teaches a graduate
course, CS 294-318 "Vision-Language-Action Models and General-Purpose Robotic Learning." Real-robot
learning, sample-efficient real-world RL, and sim-to-real / real-world adaptation remain active
threads feeding into that agenda.

## Recent publications (last ~3 yrs, with takeaways)

(Authorship and venues verified via WebSearch / arXiv abstract pages; exact citation counts
unavailable because the structured index was unreachable.)

- **SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning** (arXiv 2401.16013,
  2024; co-authored by Levine with Luo, Finn, Gupta et al.). Takeaway: a practical, open-source
  stack for *real-world* robotic RL, arguing implementation details matter as much as the
  algorithm. Directly relevant to anyone wanting RL policies that actually run on hardware rather
  than only in sim.
- **Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance**
  (arXiv 2410.13816, 2024; Levine group). Takeaway: use a learned value function to steer/improve a
  pretrained generalist (VLA) policy at deployment — a bridge between his older RL/value-function
  work and the new foundation-model agenda.
- **π0 (Pi-0): a vision-language-action flow model for general robot control** (2024–25, via
  Physical Intelligence, Levine co-founder). Takeaway: a single flow-based VLA policy aimed at
  controlling many robots/tasks from language + vision — the flagship of the "robot foundation
  model" direction.
- Direction signal: recent talks (RoboBusiness/Actuate 2025 keynotes; Dwarkesh interview) frame a
  **"data flywheel"** — VLA policies deployed in the real world to autonomously gather more
  training data and self-improve. This is where the lab is heading.

> Caution / not his: papers like "Rapidly Adapting Policies to the Real World via Simulation-Guided
> Fine-Tuning (SGFT)" (arXiv 2502.02705) and "Provable Sim-to-real Transfer…" surface in searches
> on his topics but are from *other* groups (e.g. Abhishek Gupta's lab at UW). They are NOT
> attributed to Levine here. Confirm authorship before citing any of these to him.

## Research agenda & open problems

The lab is pulling hard on one thread: **general-purpose robotic foundation models** trained
across many robots/tasks, then improved with RL and real-world interaction. Open problems he
himself frames:
- What *data* to train robot foundation models on, and how to scale collection (the data-flywheel /
  autonomous-data-gathering question).
- What the right *training objective* is for generalist policies.
- *Post-training / alignment* of robot policies — how to fine-tune and steer a pretrained generalist
  (the "value guidance" line) so it adapts efficiently and safely to new tasks and the real world.
- Sample-efficient *real-world* RL on physical robots (the SERL line), including bridging the
  sim-to-real gap as part of making real-robot learning practical.

## Funding & grants

`funding_signal: strong`. Signals: PECASE (2024), prior NSF CAREER, ONR Young Investigator, Sloan,
Okawa grant; large, continuously-recruiting lab (RAIL) inside BAIR; industry ties via Physical
Intelligence and Berkeley Deep Drive. Exact active-grant titles/numbers: `unknown` (not verified
from a grants database in this run). Funded PhD positions are very likely but specific slots are not
individually advertised.

## Fit with my profile

Applicant (from request): finishing an MSc in CS; research in **reinforcement learning for
robotics**, focused on **sim-to-real transfer**; one **workshop paper on domain randomization**;
applying for PhD start **2027**.

**Overlaps (strong, specific):**
- Core-topic match. The applicant's RL-for-robotics + sim-to-real focus sits inside Levine's
  long-standing real-robot-RL program. SERL (real-world sample-efficient robotic RL) is almost
  exactly the kind of work the applicant is trained for.
- Sim-to-real / domain randomization is directly relevant to the lab's current need to make
  pretrained generalist policies *adapt to the real world* — the applicant's exact skill set feeds
  the "post-training / real-world adaptation" open problem (cf. Steering Your Generalists).
- The applicant's hands-on RL-on-hardware orientation fits the lab's empirical, real-robot culture
  rather than pure theory.

**Gaps (honest):**
- The lab's frontier has moved toward **VLA / foundation models** (π0, language-conditioned
  generalist policies). The applicant's profile shows classical RL + domain randomization but no
  stated experience with large vision-language models, imitation/BC at scale, or
  flow/diffusion policies. To be maximally competitive they should show awareness of (or a bridge
  toward) the foundation-model direction, not only standalone sim-to-real RL.
- Track record is one *workshop* paper. RAIL is extremely competitive; a single workshop paper is a
  modest signal against a very strong applicant pool. Strengthening the portfolio (a stronger
  paper, strong letters, relevant systems/robot experience) matters.
- Sim-to-real as a *standalone* topic is somewhat less central now than "real-world adaptation of
  foundation models" — framing the interest as the latter improves fit.

**fit_score: 82 / 100** — strong, well-evidenced topical match with a clear path to contribute to a
current open problem; held below the 90s by the competitiveness of the lab and the shift of its
frontier slightly past the applicant's current exact specialization.

## Outreach hooks

(These are real and specific. See Notes — Levine asks prospective students NOT to cold-email him
about admissions, so these are best used in the **EECS PhD statement of purpose** naming him as a
target advisor, not in a "please take me" email. A narrow, substantive research question would be
the only justifiable direct contact, and even that is discouraged.)

1. **SERL → sim-to-real bridge.** Connect the applicant's sim-to-real/domain-randomization work to
   SERL's thesis that real-world robotic RL is bottlenecked by sample efficiency and engineering;
   pose how domain randomization or sim priors could cut the real-world sample cost in the SERL
   setting. Specific and substantive.
2. **Steering Your Generalists / value guidance.** Frame the applicant's interest as the
   *real-world adaptation* of pretrained generalist policies — e.g., whether sim-to-real techniques
   (domain randomization, simulator-guided exploration) can serve as the "post-training" step that
   adapts a VLA policy to a new robot/task. This maps the applicant directly onto a stated open
   problem.
3. **Data-flywheel angle.** React to his data-flywheel framing (autonomous real-world data
   collection): the applicant's domain-randomization experience is relevant to making early
   self-collected real-world rollouts safe/robust enough to bootstrap the flywheel.
4. **Course signal.** Mentioning genuine engagement with CS 294-318 themes (VLA models / general
   robotic learning) shows the applicant is tracking the lab's current direction, not its
   decade-old greatest hits.

No flattery; each hook references a specific, verified piece of his recent work and a real part of
the applicant's background.

## Notes

**Contact / application rules (downstream skills depend on this):**
- **Do NOT cold-email him about admissions.** His pages state explicitly that prospective
  undergrad/MS/PhD students should *not* contact him directly about admissions — he will not be
  able to reply. Routing applicants to the program is the intended path.
- **Admission model: program-committee, not direct-to-advisor.** Apply to the **UC Berkeley EECS
  PhD program** and **name Sergey Levine (and RAIL/BAIR) as a target advisor** in the statement of
  purpose. He notes new students join the lab every year.
- No special subject-line convention was found (because direct email is discouraged in the first
  place).
- `accepting_students: yes` — he states new students join RAIL annually; this is a recurring,
  program-mediated process rather than a per-year advertised opening. Treat as the standard EECS
  Dec deadline cycle for a 2027 start (verify exact EECS deadline before applying).

**Implication for outreach:** the right move is a strong EECS application + SOP that uses the hooks
above, *not* a cold email. If the applicant wants any direct contact, restrict it to a single,
narrow, genuinely substantive research question — and accept that a non-reply is expected and not a
rejection signal.

## Sources

- EECS faculty page (bio, title, courses incl. CS 294-318, research support contact, awards):
  https://www2.eecs.berkeley.edu/Faculty/Homepages/svlevine.html
- Personal homepage (admissions / "do not email" guidance, RAIL director):
  https://people.eecs.berkeley.edu/~svlevine/
- Google Scholar profile: https://scholar.google.com/citations?user=8R35rCwAAAAJ&hl=en
- UC Berkeley VC Research profile: https://vcresearch.berkeley.edu/faculty/sergey-levine
- SERL (arXiv 2401.16013): https://arxiv.org/abs/2401.16013
- Steering Your Generalists / value guidance (arXiv 2410.13816): https://arxiv.org/abs/2410.13816
- π0 / robotic foundation models & data-flywheel framing (talks/interviews):
  https://www.therobotreport.com/sergey-levine-discussing-foundation-models-in-robobusiness-keynote/ ,
  https://www.dwarkesh.com/p/sergey-levine
- BAIR students/admissions page: https://bair.berkeley.edu/students.html
- RAIL lab people page: https://rail.eecs.berkeley.edu/people.html
- Wikipedia (Physical Intelligence co-founder, 2024): https://en.wikipedia.org/wiki/Sergey_Levine

_Helper-script status: `scholar_lookup.py` FAILED (network blocked, 403 on tunnel) — fell back to
WebSearch as the skill directs. No publications fabricated; uncertain metadata marked._
