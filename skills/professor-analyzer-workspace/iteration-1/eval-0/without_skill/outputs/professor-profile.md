# Professor Sergey Levine — PhD Fit Analysis

**Prepared for:** A master's student in CS researching reinforcement learning for robotics (sim-to-real transfer; one workshop paper on domain randomization), applying for PhDs starting Fall 2027.
**Target professor:** Sergey Levine, Associate Professor, EECS, UC Berkeley
**Date:** June 2026

---

## 1. Who he is

Sergey Levine is an Associate Professor in EECS at UC Berkeley (joined 2016; BS/MS Stanford 2009, PhD Stanford 2014). He directs the **Robotic AI & Learning Lab (RAIL)** and is one of the most prolific and highly cited researchers in deep RL and robot learning. He is also a co-founder / lead researcher at **Physical Intelligence (Pi)**, the startup building general-purpose robotic foundation models — so a meaningful part of his recent output is tied to that effort.

His stated research mission: general-purpose algorithms that let *any* autonomous system learn *any* task, with robotics as the primary proving ground.

## 2. What he's actually working on right now (grounded in recent work)

His 2024–2026 output clusters around a few themes that are directly relevant to your background:

- **Robotic foundation models / Vision-Language-Action (VLA) models.** With Physical Intelligence: **π0** (pi-zero, late 2024) and **π0.5** ("a Vision-Language-Action Model with Open-World Generalization," arXiv 2504.16054, April 2025). These are generalist policies that fold laundry, bus tables, clean, assemble boxes, etc., and emphasize open-world generalization from large-scale real robot data.

- **Real-world reinforcement learning (not sim).** **HiL-SERL** — "Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning" (arXiv 2410.21845), published in **Science Robotics, August 2025**. A sample-efficient, vision-based RL system that learns dexterous skills (Jenga block whipping, timing-belt assembly, motherboard/IKEA assembly) directly in the real world using human corrections via a 3D mouse. Reports ~2x success-rate and ~1.8x speed gains over imitation/prior RL.

- **Offline / value-based RL to improve generalist policies.** E.g., **"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance" (V-GPS, CoRL 2024)** — using offline-RL value functions to re-rank a generalist policy's actions at deployment. Follow-on lines on scalable offline RL value learning continue into 2025–2026.

- **Self-improving embodied foundation models** (arXiv 2509.15155, 2025) — combining imitation pretraining with RL-based self-improvement.

**Important stance for you to know:** Levine is famous for the line *"simulation is doomed to succeed"* (Generally Intelligent / imbue podcast, 2023). His view: sim-to-real *works*, but the gains come from a human designer pre-specifying the variations the robot should be robust to (i.e., domain randomization), not from simulators truly modeling reality. He argues real-world data is "indispensable" for genuinely general robotic foundation models. His current center of gravity has clearly shifted toward **learning from large-scale real-world robot data and real-world RL**, somewhat *away* from pure sim-to-real.

## 3. Fit assessment for you

**Topical overlap: Strong but with a caveat.**
- Your core area — RL for robotics — is dead-center in his lab. This is one of the best possible labs in the world for RL + robot manipulation.
- Your specific sub-focus — **sim-to-real and domain randomization** — is something he knows deeply and has used, but it is *not* where his frontier is anymore. His recent work pointedly de-emphasizes simulation in favor of real-world data and real-world RL. So you'd likely be entering a group that views your current specialty as a known tool rather than the open frontier.

**What this means practically:**
- A pure "I want to keep doing sim-to-real domain randomization" pitch would be a *weak* fit signal — it reads as one generation behind his current direction.
- A reframed pitch — "I've worked on closing the sim-to-real / distribution gap, and I want to push toward real-world RL and generalist policies that don't depend on hand-specified simulation" — is a *strong* fit signal and shows you've read his recent trajectory.

**Overall verdict: Good fit, conditional on reframing.** His lab is an excellent match for your *skills* (RL, robotics, transfer/generalization), but you should position your interest toward his current themes (real-world RL, VLA foundation models, offline/value-based RL for generalist policies) rather than sim-to-real as an end in itself.

## 4. Practical realities you must know before emailing

**He explicitly does NOT want admissions emails.** His faculty page states plainly: *"please do not contact me directly in regard to undergraduate, MS, or PhD admissions, as I will not be able to reply... I encourage you to submit your application to the UC Berkeley EECS PhD program."* Cold-emailing him about admission is likely to be ignored and could read as not having done your homework.

**Implications:**
- The primary path is the **UC Berkeley EECS PhD application**, where you list him as a faculty of interest. Admissions at Berkeley EECS are committee-based, not solely advisor-pick.
- The lab is large, extremely competitive, and his attention is split with Physical Intelligence. Funding and bandwidth are real considerations; this is a high-bar, high-reward target.
- A legitimate non-admissions way to get on his radar: RAIL periodically hires **research engineers / interns** (BS/MS welcome) via the lab's "Getting Involved" page (rail.eecs.berkeley.edu/contact.html). Doing a stint there, or co-authoring with a current RAIL student/postdoc, is a far more effective route than a cold email.

## 5. If you do reach out (or write your statement) — what to mention

Given that he discourages admissions emails, treat the points below as material for (a) your **statement of purpose**, (b) outreach to his **students/postdocs** rather than him directly, or (c) a substantive research email only if you have a genuine technical contribution/question — not an admissions ask.

Things to mention, grounded in his real work:

1. **Engage his current frontier, not just sim-to-real.** Reference HiL-SERL (real-world RL, Science Robotics 2025) or π0.5 (open-world generalization) and connect your transfer/generalization experience to those problems. E.g., "My domain-randomization work targeted the same robustness-to-distribution-shift problem your real-world RL tackles without a simulator."

2. **Show you understand his thesis on data.** Acknowledge his "simulation is doomed to succeed" / real-world-data-is-indispensable view. Signal that you're interested in *reducing* reliance on hand-specified sim, e.g., real-world RL or learning robustness from data rather than randomization priors.

3. **Pitch a concrete direction at the intersection.** Strong candidate directions that fit his lab: using offline/value-based RL to fine-tune or "steer" generalist VLA policies (cf. V-GPS); sample-efficient real-world RL with human-in-the-loop feedback; or bridging your sim-to-real expertise into real-world adaptation/closing distribution gaps for foundation-model policies.

4. **Be specific and brief.** He values good research-problem selection (a recurring theme in his talks/podcasts). One crisp, well-posed problem beats a broad "I admire your work" message.

5. **Demonstrate technical readiness.** His CS 285 (Deep RL) course is the de facto standard; mentioning you've worked through it and can build on offline RL (CQL/IQL) or VLA pipelines signals you can contribute quickly.

**What to avoid:** a generic admissions ask; pitching sim-to-real domain randomization as your end goal; vague praise without a concrete research idea; emailing him for an admission decision (he won't reply).

## 6. Bottom line

- **Fit: Yes — strong on skills, conditional on reframing your focus** from sim-to-real/domain randomization toward his current real-world-RL and robotic-foundation-model agenda.
- **Process: Apply through Berkeley EECS PhD; do not cold-email him about admissions** (he says so explicitly). Consider the RAIL research-engineer/intern route or contact current lab members instead.
- **If you make contact:** lead with his recent work (HiL-SERL, π0.5, V-GPS), tie your transfer/generalization background to real-world RL, and propose one concrete, well-scoped problem.

---

### Key sources
- Faculty page: https://people.eecs.berkeley.edu/~svlevine/ (admissions-email policy; bio; talks)
- RAIL lab: http://rail.eecs.berkeley.edu (people, publications, getting involved)
- π0.5 paper: https://arxiv.org/abs/2504.16054 ; blog: https://www.physicalintelligence.company/blog/pi05
- HiL-SERL: https://arxiv.org/abs/2410.21845 ; project: https://hil-serl.github.io/ ; Science Robotics: https://www.science.org/doi/10.1126/scirobotics.ads5033
- V-GPS "Steering Your Generalists": https://arxiv.org/abs/2410.13816
- Self-Improving Embodied Foundation Models: https://arxiv.org/abs/2509.15155
- "Simulation is doomed to succeed" interview: https://imbue.com/podcast/2023-03-01-podcast-episode-28-sergey-levine/
- Berkeley News on HiL-SERL: https://news.berkeley.edu/2025/01/28/using-ai-these-robots-learn-complicated-skills-with-startling-accuracy/
- Google Scholar: https://scholar.google.com/citations?user=8R35rCwAAAAJ
