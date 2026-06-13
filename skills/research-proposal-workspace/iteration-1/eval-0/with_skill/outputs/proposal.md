# Curriculum Tactile Randomization for Sample-Efficient Sim-to-Real In-Hand Manipulation

*PhD research proposal — University of Edinburgh, Informatics. Prepared for Dr. Maria O'Keefe's dexterous-manipulation group.*

## Motivation & problem

Dexterous in-hand manipulation — re-orienting an object within the fingers rather than
regrasping it — is one of the clearest places where simulation-trained policies still fail to
transfer to real hardware. Vision and geometry can be randomized in simulation fairly
faithfully, but the *contact* signals that actually drive in-hand control (force magnitudes,
slip onset, contact location and timing across a tactile array) are exactly where simulators
are least trustworthy. As a result, two coupled gaps remain open: (1) we do not yet know how
to randomize *tactile* signals effectively, as opposed to merely adding noise, so that a policy
trained in sim is robust to the very different statistics of a real sensor; and (2) even a
well-randomized policy still needs some real-world adaptation, and dexterous fine-tuning on
hardware is sample-expensive and risky for the robot and object.

Both gaps are central to Dr. O'Keefe's stated agenda — pushing toward generalist in-hand
manipulation that transfers across object shapes, with tactile randomization and
sample-efficient real-world fine-tuning called out as the key open problems. This proposal
attacks them jointly: I argue that *how* tactile randomization is scheduled over training
directly determines how little real-world data is needed afterward, and I propose to make that
link explicit and exploitable.

## Background & related work

Domain randomization is the standard route to sim-to-real transfer: train across a distribution
of simulator parameters so the real world looks like one more sample. Most of this work, and my
own to date, randomizes vision and geometry. Dr. O'Keefe's group has pushed the frontier into
the contact channel: "Tactile-Guided Sim-to-Real for In-Hand Manipulation" (2025) uses
*simulated tactile randomization* to close the sim-to-real gap on re-orientation, building on
"Learning Dexterous Policies with Sparse Tactile Feedback" (2024). These establish that tactile
randomization helps — but treat the randomization distribution as fixed, leaving open *which*
tactile factors matter most and *how* the randomization should change over the course of
training.

Separately, my MSc thesis work shows that the *schedule* of randomization, not just its range,
governs transfer. In "Curriculum Domain Randomization for Sim-to-Real Manipulation" (CoRL
workshop, 2025) I found that ramping geometry/visual randomization on a curriculum rather than
sampling it uniformly from the start improved real pick-and-place transfer on a UR5
[reference my reported numbers from the thesis here]. That curriculum insight has, to my
knowledge, not been brought to the *tactile* channel — which is precisely where the
distribution is hardest to specify and where a naive "randomize everything immediately"
strategy is most likely to drown the learning signal. That gap is the opening for this PhD.

## Proposed research

**Core idea.** Treat tactile randomization as a *curriculum* — a schedule over which tactile
factors are perturbed, and how widely, as training proceeds — and design that curriculum
explicitly to minimize the real-world data later needed to close the residual gap. Three aims:

- **Aim 1 — A factored tactile randomization model.** Decompose the tactile signal into
  interpretable factors (per-taxel force scale and bias, contact-location jitter, slip/stick
  thresholds, temporal latency and dropout, sensor noise) and measure each factor's individual
  contribution to sim-to-real transfer on an in-hand re-orientation task. *Hypothesis:* a small
  subset of factors (likely force scaling and slip thresholds) dominates, and identifying them
  lets us randomize hard where it matters and lightly elsewhere. *Success:* a ranked sensitivity
  map that predicts real transfer better than uniform randomization at matched training cost.

- **Aim 2 — Curriculum tactile randomization.** Schedule the factors from Aim 1 — e.g. start
  with reliable contact, widen force/slip randomization as the policy stabilizes — and compare
  against fixed-distribution randomization (the current lab approach) and anti-curriculum
  controls. *Hypothesis:* curricula matched to factor sensitivity yield policies that transfer
  zero-shot at least as well *and* are markedly cheaper to fine-tune. *Success:* equal or better
  zero-shot real success with measurably fewer real episodes to reach a target.

- **Aim 3 (extension) — Sample-efficient real fine-tuning informed by the curriculum.** Use the
  sensitivity map to direct the small real-world adaptation budget at the factors the simulator
  got most wrong (e.g. calibrate residual force/slip dynamics first). *Hypothesis:* curriculum
  pre-training plus targeted fine-tuning reaches a target real success rate with substantially
  fewer real trials than fine-tuning a fixed-randomization policy. *Success:* a clear
  data-efficiency gain, and evidence the curriculum and the fine-tuning strategy are
  complementary rather than redundant.

A natural further extension is whether a curriculum tuned on one object shape generalizes across
shapes, connecting directly to the lab's generalist-manipulation goal.

## Methods & feasibility

I would build the simulation and policy stack in MuJoCo / Isaac Gym with PPO/SAC — the exact
tools from my MSc pipeline — extended with a simulated tactile array over a multi-fingered hand.
The factored randomization parameters of Aim 1 plug directly into the curriculum-scheduling
machinery I already implemented for geometry/visual randomization, so Aim 2 reuses
infrastructure rather than starting from scratch. Real-robot evaluation and fine-tuning (Aim 3)
follow the sim-to-real evaluation discipline I used to reach [my reported pick-and-place success
rate] on a UR5, adapted to the lab's dexterous hand and tactile hardware.

Feasibility rests on a tight progression: Aim 1's sensitivity study is a self-contained,
publishable first-year result that de-risks everything after it; Aim 2 is an engineering-plus-
analysis extension of existing curriculum code; Aim 3 is where real-hardware cost concentrates,
deferred to years 2–3 once the simulation findings have narrowed what to test. This sequencing
keeps real-robot time — the scarcest resource — small and well-targeted.

## Risks & alternatives

- **Sim tactile is too inaccurate to randomize usefully.** If even the best simulated tactile
  signal is too far from the real sensor, curricula over it may not transfer. *Fallback:*
  treat Aim 1's sensitivity analysis as guidance for a real-data-driven randomization
  distribution (fit factor ranges to a small calibration set), shifting weight toward Aim 3.
- **No curriculum beats a well-tuned fixed distribution.** A null result is still informative —
  reframe the contribution as the factor-sensitivity map (Aim 1) and the targeted fine-tuning
  recipe (Aim 3), which stand on their own.
- **Hardware constraints (sensor availability, hand reliability).** Keep the core scientific
  claims demonstrable in simulation with a contained real-robot confirmation, so progress does
  not stall on a single piece of hardware.

## Fit with the lab

This project lives exactly where Dr. O'Keefe's group is heading and where my background gives me
a credible running start. The lab has the tactile sim-to-real platform, the dexterous hand, and
the two papers (2024, 2025) that make tactile randomization tractable at all; it is one of the
few places this work can be done. I bring the complementary half: demonstrated curriculum
domain-randomization and real-robot sim-to-real experience (UR5 pick-and-place, MuJoCo/Isaac
Gym, PPO/SAC). The honest gap — my randomization work has been visual/geometric, not tactile —
is precisely the bridge this proposal builds, and addressing it directly answers the lab's two
named open problems: how to randomize tactile signals effectively, and how to fine-tune
dexterous policies sample-efficiently on real hardware. The named, fully-funded
dexterous-manipulation project Dr. O'Keefe is recruiting for is the right home for it.

## References

1. O'Keefe, M., et al. "Tactile-Guided Sim-to-Real for In-Hand Manipulation." 2025.
2. O'Keefe, M., et al. "Learning Dexterous Policies with Sparse Tactile Feedback." 2024.
3. [Test Applicant]. "Curriculum Domain Randomization for Sim-to-Real Manipulation." CoRL
   Robot Learning Workshop, 2025.

*Note: bracketed items above are placeholders only I can fill with specifics from my MSc
thesis (reported success rates and curriculum results) and my own name/citation formatting.*
