---
slug: sergey-levine-uc-berkeley
name: Sergey Levine
title: Associate Professor
institution: UC Berkeley
department: EECS
lab: Robotic AI & Learning Lab (RAIL), part of BAIR
homepage: https://people.eecs.berkeley.edu/~svlevine/
scholar: https://scholar.google.com/citations?user=8R35rCwAAAAJ&hl=en
email: (does not accept direct admissions inquiries — see Outreach hooks)
field: machine learning / robot learning / reinforcement learning
last_analyzed: 2026-06-12
fit_score: 82
funding_signal: strong
accepting_students: yes
---

# Sergey Levine — UC Berkeley (RAIL)

## Research focus

Levine works on algorithms that let autonomous agents acquire complex behaviors
through learning, with an emphasis on deep reinforcement learning, imitation
learning, and scalable robot learning. He directs the Robotic AI & Learning Lab
(RAIL) within BAIR. His recent center of gravity has shifted strongly toward
**robot foundation models / vision-language-action (VLA) models** trained on
large, heterogeneous robot data, while keeping a parallel thread of work on
**real-world reinforcement learning** for efficient, autonomous policy
improvement on physical robots. He received the PECASE award in 2025.

Important context for the applicant: Levine is also a co-founder of **Physical
Intelligence (π)**, the startup behind the π0 / π0.5 models, so a large fraction
of his recent flagship work happens at the academia–industry boundary.

## Recent publications (last ~3 yrs, with takeaways)

- **π0.5: a Vision-Language-Action Model with Open-World Generalization** (CoRL
  2025; arXiv 2504.16054, Apr 2025). Co-training on heterogeneous data (multiple
  robots, web data, high-level semantic subtask prediction, object detections,
  low-level actions) so a single VLA can do long-horizon, dexterous tasks —
  e.g. cleaning a kitchen — in *entirely new homes* it never saw in training.
  Takeaway: the lab's headline bet is broad generalization of manipulation
  policies via massive multimodal co-training.
- **OpenVLA: An Open-Source Vision-Language-Action Model** (CoRL 2025; Kim,
  Pertsch, …, Levine). A 7B open-source VLA pretrained on ~970k episodes from the
  Open X-Embodiment dataset; later extended with an Optimized Fine-Tuning (OFT)
  recipe giving 25–50x faster inference. Takeaway: the lab open-sources strong
  generalist policies and cares about efficient fine-tuning/deployment.
- **FAST: Efficient Action Tokenization for Vision-Language-Action Models**
  (2025; Pertsch, Finn, Levine). A better way to tokenize continuous robot
  actions for autoregressive VLA training. Takeaway: representation/tokenization
  is treated as a first-class lever for VLA quality.
- **DSRL: Steering Your Diffusion Policy with Latent Space Reinforcement
  Learning** (2025; Wagenmaker, Nakamoto, …, Levine). Runs RL in the latent-noise
  space of a pretrained diffusion policy instead of fine-tuning its weights —
  highly sample-efficient real-world improvement of a pretrained policy.
  Takeaway: the RL thread is now about *cheaply adapting big pretrained policies
  in the real world*, not training from scratch.
- **HiL-SERL / Sample-Efficient Real-World Robotic RL** (2025, widely covered;
  e.g. "Jenga whipping" demos with reported ~100% success). Human-in-the-loop,
  sample-efficient RL that learns dexterous contact-rich skills directly on a
  real robot from demonstrations + human/real-world feedback. Takeaway: a
  practical, reproducible real-world RL stack is a live lab priority.

## Research agenda & open problems

Reading across the recent work, the lab's trajectory is converging on a single
question: **how to build generalist robot policies that both generalize broadly
(via foundation-model-scale pretraining) and keep improving autonomously after
deployment (via efficient real-world RL).** Concrete open threads the applicant
could plausibly contribute to:

- Closing the loop between *pretrained generalist VLAs* and *real-world RL
  fine-tuning* (DSRL is an early step; how to make on-robot adaptation reliable
  and safe is open).
- Evaluation of generalist policies — note the lab's interest in **real-to-sim /
  scalable evaluation** (e.g. PolaRiS-style scalable real-to-sim evals appearing
  in the surrounding literature). This is directly adjacent to sim-to-real.
- Action representation/tokenization for VLAs (FAST line).
- Sample efficiency and human-in-the-loop learning for contact-rich dexterous
  manipulation (SERL line).

Note: classic *sim-to-real transfer via domain randomization* — the applicant's
specialty — is no longer the lab's headline framing. The current emphasis is
real-world data + real-world RL, with simulation reframed mostly as a tool for
*evaluation* (real-to-sim) rather than as the primary training source. This is a
fit nuance, not a dealbreaker (see below).

## Funding & grants

funding_signal: **strong**, inferred (not from a specific grant document). New
students join the lab every year (stated on his homepage); the lab actively
recruits research engineers; and Levine holds major recognition (PECASE 2025)
plus deep industry ties via Physical Intelligence. Specific active federal grant
numbers were not verified in this pass — treat the underlying grant detail as
*unconfirmed*, but the position-availability signal is clearly positive.

## Fit with my profile

Applicant: finishing an MS in CS; research on **RL for robotics, mostly
sim-to-real transfer**; one workshop paper on **domain randomization**; applying
for PhD starts in **2027**.

**Overlaps (strong):**
- The applicant's core field — **RL for robotics** — is exactly Levine's core
  field. This is a topical bullseye at the area level.
- The applicant's **sim-to-real** background maps cleanly onto the lab's growing
  **real-to-sim evaluation** thread and onto the general problem of getting
  policies that work on real hardware — the lab's central obsession.
- **RL fine-tuning of pretrained policies** (DSRL, SERL) is a natural landing
  spot: an applicant who understands the sim-to-real gap and domain
  randomization is well-positioned to work on why pretrained generalist policies
  fail on real robots and how RL can fix them.

**Gaps (be honest):**
- The lab has largely *moved past* domain-randomization-style sim-to-real as a
  headline. The applicant's signature technique is now a supporting tool, not the
  frontier here. They should frame their experience as *understanding the
  real-world deployment gap*, not as "I do domain randomization."
- The flagship work is increasingly **VLA / foundation-model** scale, which
  leans on large-scale data engineering, vision-language pretraining, and
  significant compute. If the applicant's experience is mostly small-scale
  sim-to-real RL, there's a ramp-up to VLA-scale work.
- **Admissions reality:** Berkeley EECS is committee-admit and extremely
  competitive, and Levine explicitly will not respond to direct admissions
  emails. "Fit" here does not translate into an easy contact path (see hooks).

**fit_score: 82/100** — strong topical fit (same field, complementary skills,
multiple concrete landing projects), discounted from higher because (a) the
applicant's specific niche has shifted from center to periphery in the lab, (b)
the VLA-scale direction is a real ramp-up, and (c) the admissions path is hard
and not advisor-emailable.

## Outreach hooks

**Critical caveat first:** Levine's homepage states he will **not** reply to
direct emails about PhD/MS/undergrad admissions and asks prospective students to
apply through the UC Berkeley EECS PhD program instead. So a cold "please advise
me" email is explicitly discouraged and likely ignored.

What this means practically:
- **Do not** send a generic "I'd like to do a PhD with you" email — it will not
  be answered and may signal you didn't read his page.
- The productive paths are: (1) apply through Berkeley EECS and name RAIL/Levine
  and specific projects in your statement of purpose; (2) build a genuine,
  *technical* contact via a concrete research interaction rather than an
  admissions ask.

If/when a substantive technical message is warranted (e.g. you have a real
result or question), these are honest, specific hooks grounded in his work:

1. **DSRL ↔ your sim-to-real experience.** "DSRL steers a pretrained diffusion
   policy by RL in its latent-noise space. In my MS work on sim-to-real transfer,
   the failure mode was the policy degrading on real dynamics — I'm curious
   whether latent-space RL like DSRL implicitly absorbs sim-to-real gap, and
   whether domain-randomized pretraining changes how steerable that latent space
   is." This connects your actual background to a real 2025 paper.
2. **Real-to-sim evaluation of generalist policies.** Your domain-randomization
   background is directly relevant to building/evaluating real-to-sim test
   environments for VLAs — a genuine open problem adjacent to your skills.
3. **π0.5 generalization to new environments.** A substantive question about *why*
   co-training yields open-world generalization where domain randomization
   plateaus — i.e., is large heterogeneous real data just "domain randomization
   over the real world"? This is a real conceptual question linking your prior
   framing to his flagship result.

Each hook references a specific, verified recent paper and ties to the
applicant's actual experience — no flattery, no invented overlap.

## Sources

- Homepage / admissions policy: https://people.eecs.berkeley.edu/~svlevine/
- RAIL lab people page: https://rail.eecs.berkeley.edu/people.html
- Berkeley faculty profile: https://vcresearch.berkeley.edu/faculty/sergey-levine
- Wikipedia (bio, PECASE 2025): https://en.wikipedia.org/wiki/Sergey_Levine
- Google Scholar: https://scholar.google.com/citations?user=8R35rCwAAAAJ&hl=en
- π0.5 (arXiv 2504.16054): https://arxiv.org/abs/2504.16054
- π0.5 (CoRL 2025 proceedings): https://proceedings.mlr.press/v305/black25a.html
- OpenVLA (CoRL 2025): https://proceedings.mlr.press/v270/kim25c.html
- DSRL project page: https://diffusion-steering.github.io/
- HiL-SERL coverage: https://techxplore.com/news/2025-08-human-feedback-ai-driven-robots.html
- Fast/precise robot teaching coverage: https://techxplore.com/news/2025-01-ai-fast-precise-robots-complicated.html
