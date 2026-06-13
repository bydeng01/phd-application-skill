# PhD Research Proposal

## Tactile Domain Randomization and Sample-Efficient Real-World Fine-Tuning for Dexterous In-Hand Manipulation

**Proposed supervisor:** Dr. Maria O'Keefe, School of Informatics, University of Edinburgh
**Applicant:** MSc Computer Science (graduating 2026)

---

## 1. Motivation and Problem Statement

Dexterous in-hand manipulation remains one of the hardest open problems in robot learning. Policies trained in simulation routinely fail when transferred to physical hardware because the contact-rich dynamics and, crucially, the *tactile* signals that drive in-hand control are poorly modeled by simulators. Domain randomization (DR) has become the dominant tool for closing the sim-to-real gap, but the community's understanding of DR is overwhelmingly skewed toward **visual and geometric** randomization — lighting, textures, object shape, mass, and friction. Far less is understood about how to randomize **tactile** signals, which are noisier, higher-dimensional, and more tightly coupled to contact geometry than any camera image.

Dr. O'Keefe's recent work directly defines this frontier. *Tactile-Guided Sim-to-Real for In-Hand Manipulation* (2025) demonstrated that randomizing simulated tactile readings can narrow the sim-to-real gap, and *Learning Dexterous Policies with Sparse Tactile Feedback* (2024) showed that even impoverished touch signals carry exploitable information for dexterous control. These results surface two open problems that this PhD proposes to attack head-on:

1. **How should tactile signals be randomized effectively** — as opposed to naively perturbing them the way we perturb pixels — so that policies transfer robustly across real sensors with different noise, drift, and contact response?
2. **How can dexterous policies be fine-tuned on real hardware sample-efficiently**, given that real-world in-hand manipulation data is expensive and risky to collect?

My MSc background gives me a concrete and honest starting point: I have worked deeply on **sim-to-real domain randomization, but on the vision/geometry side**, not tactile. My thesis studies domain-randomization *schedules* for pick-and-place, and my CoRL 2025 workshop paper, *Curriculum Domain Randomization for Sim-to-Real Manipulation*, develops curricula that order randomization difficulty over training. This proposal argues that the curriculum and scheduling machinery I have built for visual/geometric DR is exactly the transferable foundation needed to make **tactile** randomization principled — and that this is a natural, non-trivial extension into Dr. O'Keefe's research program rather than a repackaging of prior work.

---

## 2. Research Questions

- **RQ1.** What is a useful taxonomy and generative model of tactile-signal corruptions (sensor noise, gain/offset drift, spatial miscalibration, latency, dead taxels, contact-geometry mismatch), and which of these actually matter for sim-to-real transfer of in-hand policies?
- **RQ2.** Do *curriculum* and *scheduled* tactile randomization strategies — ordering tactile perturbations from easy to hard during training — improve transfer and stability over uniform tactile DR, as they do for visual/geometric DR?
- **RQ3.** Can a policy pre-trained with structured tactile randomization be fine-tuned on real hardware with an order of magnitude fewer real interactions than training from scratch or naive fine-tuning, and what makes fine-tuning sample-efficient (which parameters to adapt, what to keep frozen, how to use tactile residuals)?
- **RQ4.** Is there a measurable relationship between *how* tactile signals are randomized in sim and *how much* real-world fine-tuning is subsequently required — i.e., can good randomization buy down real-data cost?

---

## 3. Proposed Research Programme

### Year 1 — Tactile randomization, grounded in a working pipeline

I will first build a contact-rich in-hand manipulation testbed in simulation (Isaac Gym / MuJoCo, both of which I use) instrumented with simulated tactile sensing, reusing the MuJoCo→real pipeline experience from my MSc (where I achieved 88% success on a 6-object UR5 pick-and-place setup). The first scientific contribution is **a structured model of tactile randomization**: rather than adding Gaussian noise to tactile arrays, I will parameterize physically-motivated corruption modes (RQ1) and measure each mode's individual contribution to transfer via ablation. This produces an empirical "which tactile randomizations matter" study — the tactile analogue of well-known visual-DR sensitivity analyses, which to my knowledge does not yet exist.

### Year 2 — Curriculum and scheduled tactile randomization

I will transfer my curriculum-DR methodology from the visual/geometric domain to the tactile domain (RQ2). Concretely: define difficulty metrics over tactile corruption modes, schedule them over training (e.g., progressive noise, progressive taxel dropout, progressive contact-geometry mismatch), and compare against uniform and no-randomization baselines on transfer. Because my prior work is on *schedules* specifically, the novel question here is whether tactile signals — being lower-bandwidth and more contact-coupled than images — demand *different* curriculum structure than vision. I expect the answer is yes, and characterizing that difference is a publishable result.

### Year 3 — Sample-efficient real-world fine-tuning

The final thrust targets RQ3/RQ4: real-hardware fine-tuning of dexterous policies under a tight real-interaction budget. I will investigate (a) which policy components to adapt vs. freeze, (b) residual/offset learning that corrects sim tactile predictions toward real readings, and (c) using the Year-1 randomization model to predict and minimize the real-data needed for a target success rate. The unifying hypothesis is that **better-structured tactile randomization in sim reduces the real-world sample complexity of fine-tuning** — directly serving Dr. O'Keefe's two stated open problems and linking them causally rather than treating them separately.

### Cross-cutting and methods

Policies will be trained with PPO/SAC (both in my toolkit) in PyTorch under ROS-based real control. Throughout, I will hold myself to honest, reproducible sim-to-real reporting: pre-registered evaluation objects, fixed real-trial budgets, and reporting of failure modes, consistent with the rigor of Dr. O'Keefe's transfer studies.

---

## 4. Fit with the Lab and Honest Statement of Background

I want to be transparent about my starting point. My demonstrated results are in **vision- and geometry-based** sim-to-real DR for pick-and-place, not in tactile sensing or in-hand manipulation. I am proposing this PhD precisely because the *methodological* tools I have already built — curriculum design, randomization scheduling, and a tested MuJoCo→real workflow — are the right scaffolding for the tactile and fine-tuning problems Dr. O'Keefe has identified, and because moving from vision-DR to tactile-DR is a substantive research step I am eager to make under her supervision. The lab's 2024–2025 papers are not just context for this proposal; they are its foundation, and each of my three research thrusts is anchored to a specific open question those papers raised.

---

## 5. Expected Contributions

1. A physically-grounded taxonomy and generative model of tactile randomization, with an ablation showing which modes drive transfer.
2. The first study of *curriculum/scheduled* tactile randomization for in-hand manipulation, and how it differs from visual-DR curricula.
3. A sample-efficient real-world fine-tuning method for dexterous policies, with an empirical link between sim randomization quality and real-data cost.
4. Open-source tooling and reproducible benchmarks for tactile sim-to-real.

---

## 6. Indicative Timeline

| Phase | Focus | Output |
|-------|-------|--------|
| Y1 | Tactile testbed + randomization taxonomy/ablation (RQ1) | Workshop/conference paper |
| Y2 | Curriculum/scheduled tactile DR (RQ2) | Main conference paper |
| Y3 | Sample-efficient real fine-tuning + randomization↔data-cost link (RQ3/RQ4) | Main conference paper, thesis |
| Y3.5 | Thesis writing, open-source release | PhD thesis |

---

## 7. References (supervisor's work this proposal builds on)

- O'Keefe, M. (2025). *Tactile-Guided Sim-to-Real for In-Hand Manipulation.*
- O'Keefe, M. (2024). *Learning Dexterous Policies with Sparse Tactile Feedback.*
- [Applicant] (2025). *Curriculum Domain Randomization for Sim-to-Real Manipulation.* CoRL Workshop.
