---
slug: sergey-levine-uc-berkeley
name: Sergey Levine
title: Associate Professor
institution: UC Berkeley
department: EECS
lab: Robotic AI & Learning Lab (RAIL), BAIR
homepage: https://people.eecs.berkeley.edu/~svlevine/
scholar: https://scholar.google.com/citations?user=8R35rCwAAAAJ&hl=en
email: # see RAIL contact page; does NOT take direct admissions emails
field: machine learning / robotics
last_analyzed: 2026-06-12
fit_score: 82
funding_signal: strong
accepting_students: yes
---

## Research focus

Sergey Levine works on machine learning for decision making and control, with deep
reinforcement learning and imitation learning at the core, applied primarily to robotics.
His stated mission is general-purpose methods that let "any autonomous system learn to solve
any task." Over the last ~2 years his center of gravity has shifted decisively toward
**robotic foundation models** — large vision-language-action (VLA) models trained on diverse
real-world data — while keeping a strong thread of **real-world / sample-efficient
reinforcement learning** for fine-tuning and dexterous control. He directs the RAIL lab at
Berkeley and co-founded the robotics startup Physical Intelligence (π) in 2024, which is
where much of the frontier foundation-model work now happens.

## Recent publications (last ~3 yrs, with takeaways)

- **π0: A Vision-Language-Action Flow Model for General Robot Control** (arXiv 2410.24164,
  2024). A general-purpose robot foundation model pairing a pretrained VLM with a
  flow-matching / diffusion action expert, trained on diverse cross-embodiment real-world
  data. Takeaway: a single model can control many robot platforms and tasks; bets that
  generality is *easier* than narrow special-casing.
- **π0.5: a Vision-Language-Action Model with Open-World Generalization** (arXiv 2504.16054,
  2025). Follow-up emphasizing generalization to genuinely novel environments. Takeaway: the
  agenda is now pushing VLAs from in-distribution competence toward open-world robustness.
- **Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement
  Learning (HiL-SERL)** (arXiv 2410.21845; *Science Robotics*, Aug 2025; Luo, Xu, Wu,
  Levine et al.). A vision-based real-world RL system reaching near-100% success on dexterous
  tasks (precision assembly, dual-arm coordination, dynamic "Jenga whipping") within 1–2.5
  hours of on-robot training, by combining demonstrations, human corrections, and efficient
  RL. Takeaway: real-world RL — not just sim — can be sample-efficient enough to be practical.
- **Pushing the limits of cross-embodiment learning for manipulation and navigation**
  (RSS 2024). Cross-embodiment policy learning across robot bodies and tasks. Takeaway: data
  scale and shared representations across embodiments are central to his foundation-model bet.
- **PolaRiS / real-to-sim evaluation work** (2025). Neural reconstruction turns short real
  video scans into interactive sim environments for evaluating generalist policies, with
  better correlation to real-world performance than existing sim benchmarks. Takeaway: he is
  actively rethinking the *evaluation* side of sim-and-real for generalist policies.

Note: many recent first-author/lab papers are co-produced with Physical Intelligence; exact
author lists and venues should be confirmed against the RAIL publications page before citing
in an email.

## Research agenda & open problems

The lab is pulling hard on one thread: **building robotic foundation models that generalize
broadly**, and the supporting problems around them. Concretely, open directions visible in
the recent work:

- Scaling VLA models and the **data** that feeds them — Levine argues real robot data is
  "indispensable" for true generalization (Sporks of AGI blog).
- **Open-world generalization** of policies (the π0 → π0.5 progression).
- **Real-world RL for post-training / fine-tuning** generalist policies efficiently
  (HiL-SERL), including human-in-the-loop feedback.
- **Cross-embodiment** transfer across different robot bodies.
- **Real-to-sim / sim-for-evaluation** — using reconstruction to build faithful evaluation
  environments (PolaRiS). This is the spot where classic sim-to-real intuitions are being
  repurposed, now as much for *evaluation and world-modeling* as for training.

## Funding & grants

Strong. Levine received the **PECASE** (Presidential Early Career Award for Scientists and
Engineers) in 2025. The lab sits within BAIR, which carries substantial federal and
industry funding, and his co-founded company **Physical Intelligence** raised ~$70M seed
plus ~$400M (reported ~$2B valuation, late 2024), providing compute and real-robot data
infrastructure that lab students benefit from. New students join the RAIL lab every year.
Funding for admitted Berkeley EECS PhD students in this area is generally not a concern.
(Exact grant numbers were not individually verified; treat the company figures as
press-reported.)

## Fit with my profile

Applicant profile (from request; profile.md is a blank template): finishing an MS in CS;
research in **RL for robotics, focused on sim-to-real transfer**; one workshop paper on
**domain randomization**; targeting PhD start 2027.

**Overlaps:**
- Core method match. The applicant's RL-for-robotics background is squarely in Levine's
  central toolkit; CS 285 (his Deep RL course) is essentially the applicant's home turf.
- **HiL-SERL / real-world RL** is the most direct bridge: someone who has thought about
  sim-to-real and randomization is well positioned to contribute to making real-world RL
  sample-efficient and to closing the residual sim-to-real gap during policy fine-tuning.
- **PolaRiS real-to-sim evaluation** intersects the applicant's sim-to-real interest from a
  fresh angle (reconstruction-based sim for evaluation), where domain-randomization thinking
  about distribution shift transfers naturally.

**Gaps:**
- Levine's frontier has moved from *narrow sim-to-real transfer* toward *large VLA foundation
  models trained on real data*. The applicant's classic sim-to-real + domain-randomization
  framing is adjacent, not identical — the lab's thesis leans on real-world data scale rather
  than sim-heavy pipelines, so the applicant should frame sim-to-real as a tool within
  generalist-policy learning, not as the end goal.
- A single **workshop** paper is light for one of the most competitive robot-learning labs
  in the world; admission is via the Berkeley EECS PhD program and is extremely selective.
- Much frontier work runs through Physical Intelligence; the applicant should be comfortable
  with a foundation-model / large-scale-data research culture, not just algorithmic RL.

**fit_score: 82** — strong topical and methodological alignment, with the main caveats being
selectivity and the need to reframe sim-to-real within his current foundation-model agenda.

## Outreach hooks

Important process note: Levine's homepage explicitly asks prospective students **not to email
him about admissions** — he will not reply, and says to apply to the Berkeley EECS PhD
program (the RAIL contact page directs undergrads/postdocs separately). So a cold "please
take me" email is the wrong move. Any contact should be a genuine, narrow research exchange,
and the real action item is a strong EECS PhD application naming him. If you do reach out
(or, better, weave these into your statement of purpose), make them specific:

1. **HiL-SERL and the sim-to-real residual.** Reference the *Science Robotics* 2025
   human-in-the-loop RL result and connect it to your domain-randomization work: ask/argue
   how randomization-trained priors could reduce the human-correction budget needed for
   real-world fine-tuning — a concrete contribution you're positioned to make.
2. **PolaRiS real-to-sim evaluation.** React to the reconstruction-based evaluation idea and
   propose how domain-randomization-style distribution-shift analysis could make those
   evaluations more predictive of real-world generalization.
3. **π0.5 open-world generalization.** Tie your sim-to-real transfer interest to the open
   question of *why* VLAs still fail on novel environments, framing randomization/coverage as
   one lever for open-world robustness rather than as a standalone pipeline.
4. **Reframe, don't repeat.** Show you understand the lab's shift toward real-data foundation
   models — position sim-to-real as a component of generalist-policy training, signaling
   you've read past his greatest hits to where the lab is actually heading.

Each hook must reflect papers you have actually read; do not reference any of these unless you
can speak to the specifics.

## Sources

- Homepage: https://people.eecs.berkeley.edu/~svlevine/
- RAIL lab: https://rail.eecs.berkeley.edu/ (people, publications, contact pages)
- Google Scholar: https://scholar.google.com/citations?user=8R35rCwAAAAJ&hl=en
- Wikipedia (bio, PECASE 2025): https://en.wikipedia.org/wiki/Sergey_Levine
- UC Berkeley research profile: https://vcresearch.berkeley.edu/faculty/sergey-levine
- π0 paper: https://arxiv.org/abs/2410.24164 (html: https://arxiv.org/html/2410.24164v1)
- π0.5 paper: https://arxiv.org/abs/2504.16054
- HiL-SERL paper: https://arxiv.org/abs/2410.21845
- HiL-SERL in Science Robotics: https://www.science.org/doi/10.1126/scirobotics.ads5033
- Berkeley news coverage (HiL-SERL): https://techxplore.com/news/2025-08-human-feedback-ai-driven-robots.html
- Physical Intelligence / foundation-models talk coverage: https://www.therobotreport.com/sergey-levine-discussing-foundation-models-in-robobusiness-keynote/
- Dwarkesh interview (foundation models, real data thesis): https://www.dwarkesh.com/p/sergey-levine
