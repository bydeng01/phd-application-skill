# Interview Prep — PhD Interview with Dr. Maria O'Keefe

**Role:** Fully-funded PhD, dexterous in-hand manipulation project
**Institution:** University of Edinburgh, School of Informatics
**Timing:** July 2026 (start 2027)
**Interviewer:** Dr. Maria O'Keefe, Senior Lecturer — sim-to-real for dexterous (in-hand) manipulation, tactile-informed control

---

## 1. The big picture: what this interview is really testing

O'Keefe is recruiting for a *named, specific* project on generalist in-hand manipulation. She is not just checking competence — she is checking **fit between your background and her open problems**. Your record is a strong-but-imperfect match, and you should own that explicitly:

- **Your strength:** real sim-to-real manipulation experience — MuJoCo→real pipeline, curriculum domain randomization, real-robot eval (UR5, 88% on 6 objects), a CoRL workshop paper on exactly this theme. This is *directly* what her lab does.
- **Your gap:** all your randomization and control work is **vision/geometry-based**, on a parallel-jaw / arm setup. Her frontier is **tactile** signals and **in-hand dexterity** (multi-fingered re-orientation). You have not worked with tactile sensing or dexterous hands.

The winning narrative: *"I've built and validated the exact sim-to-real machinery your lab depends on; tactile and in-hand dexterity are the natural next axis for me, and I have concrete ideas about how my randomization experience transfers to that setting."* Treat the gap as a research direction, not a weakness.

**Before the interview, read her two papers properly:**
- 2025: *Tactile-Guided Sim-to-Real for In-Hand Manipulation* (tactile randomization to close the gap for re-orientation)
- 2024: *Learning Dexterous Policies with Sparse Tactile Feedback*

Be able to summarize each in two sentences and name one thing you'd question or extend in each.

---

## 2. Likely questions and how to answer

### A. Your own research (expect deep, probing follow-ups)

**Q: "Walk me through your sim-to-real pick-and-place work."**
- Structure: problem → pipeline (MuJoCo → UR5) → the curriculum domain-randomization idea → real-robot result (88% / 6 objects) → what you learned.
- Land the *insight*, not just the result: e.g. why a *schedule* of randomization beat fixed-range randomization, where it still failed, what the residual sim-to-real gap looked like.
- Have a number ready for "compared to what?" — what was the non-curriculum baseline?

**Q: "What were the failure modes? Where did 88% break?"**
- She *will* push on the 12% that failed. Don't hand-wave. Name concrete failures (object geometry, contact-rich grasps, perception edge cases) and say what you'd do differently. Admitting limits credibly is a strong positive signal.

**Q: "Why a curriculum / scheduled randomization rather than just wide randomization from the start?"**
- Be ready to defend the design choice on sample-efficiency and optimization-stability grounds, and to say honestly whether you ablated it.

**Q: "What would you have done with more time / a better setup?"**
- Bridge here toward tactile and dexterity — a natural segue into her work.

### B. Her work and the project (fit + genuine engagement)

**Q: "What did you think of our 2025 tactile sim-to-real paper?"**
- Summarize accurately, then engage critically and constructively. Good angle: *"In my work I randomized vision and geometry, where the sim distribution is fairly well understood. Tactile is harder because the sensor model and contact physics are noisier and less characterized — so the open question for me is how you even define the randomization distribution for tactile signals so it covers reality without being so wide it's unlearnable."* This directly names one of her stated open problems.

**Q: "How is randomizing tactile signals different from the visual/geometry randomization you've done?"**
- This is *the* fit question. Key points to make:
  - Tactile is **contact-conditioned and local** — you only get signal where the hand touches, so randomization interacts with the policy's own contact behavior (a feedback loop visual randomization doesn't have).
  - Sim tactile models (e.g. simulated taxels / force fields) are **lower-fidelity and less validated** than rendering, so the sim-to-real gap is larger and harder to characterize.
  - Naive wide randomization may destroy the very signal the policy needs. So the interesting problem is *structured* / physically-grounded tactile randomization, possibly calibrated against a small amount of real data.
- Even if you get details wrong, showing you've *thought structurally* about the difference is what she wants.

**Q: "Sample-efficient real-world fine-tuning is a problem we care about — any ideas?"**
- Her second stated open problem. Offer 2–3 concrete directions, framed as hypotheses not claims:
  - Pre-train broadly in sim with randomization, then fine-tune on real with a small budget using offline/off-policy methods (SAC, which you know) to reuse every real sample.
  - Use real tactile data to *calibrate the randomization distribution* (close the loop), rather than blindly fine-tuning the policy.
  - Residual policy learning / sim-anchored regularization to avoid catastrophic forgetting from few real samples.
- Then pivot: *"This is exactly the area I'd want my thesis to live in — which is partly why I'm applying to your lab."*

**Q: "Why this project / why my lab specifically?"**
- Be concrete: her sim-to-real + tactile + in-hand focus is the precise intersection where your existing machinery (randomization, real-robot eval) meets the frontier you want to move into. Avoid generic praise.

### C. Direction, independence, and logistics

**Q: "What do you want to work on for your PhD?"**
- Show a *direction* with flexibility, not a rigid plan: generalist in-hand manipulation that transfers across object shapes, with tactile-informed sim-to-real as the core method. Tie it to her named project but signal you can co-shape it.

**Q: "Where do you see yourself after the PhD?"**
- Honest answer fits your profile: academia-leaning. That's fine and often welcome.

**Q: "How do you handle being stuck / a long debugging slog / a failed experiment?"**
- Real-robot work is full of this. Give a concrete example from the UR5 pipeline and show resilience and systematic debugging.

**Q: "How independent are you vs. how much guidance do you want?"**
- Position yourself as able to run experiments independently (you already have) while wanting mentorship on the tactile/dexterity domain that's new to you.

**Logistics to clarify (these are legitimate to ask):**
- Funding details and what the named studentship covers (you require full funding — confirm it).
- Hardware available (which dexterous hand? what tactile sensors — e.g. GelSight-style vs. taxel arrays?).
- Whether the project scope is fixed or negotiable.
- Expected start, cohort, team size, co-supervision.

---

## 3. Questions YOU should ask her

Asking sharp questions is half the interview. Good ones:
1. "For the tactile randomization work — are you finding the bottleneck is the sim sensor model fidelity, or the randomization distribution design, or the real-world calibration?"
2. "How much real-robot time would a student realistically get? What's the hardware setup for the dexterous hand and tactile sensing?"
3. "Is the named project's scope fixed, or is there room to shape the direction — e.g. toward cross-shape generalization vs. sample-efficient fine-tuning?"
4. "What's worked and what's frustrated you most in closing the tactile sim-to-real gap so far?"
5. "What does a successful first year look like for a student on this project?"
6. "How does the lab collaborate — solo projects, or shared infrastructure / pairing?"

Avoid: questions answered on her website, salary-first questions, or anything implying you haven't read her papers.

---

## 4. Gap-management cheat sheet

| If she probes... | Your move |
|---|---|
| "You've never used tactile sensing." | Acknowledge directly, then show you understand *why* tactile randomization is hard and have ideas. Frame as the deliberate next step, not a blind spot. |
| "You've only done parallel-jaw / arm, not dexterous hands." | True — but the sim-to-real *methodology* (randomization, real eval, debugging) transfers; the hand is the new variable, and that's what excites you. |
| "Your result is a workshop paper, not a full paper." | Own the scope; emphasize what you learned and that you ran a real-robot eval end-to-end, which many workshop papers don't. |
| "How fast can you get up to speed on dexterous manipulation?" | Point to MuJoCo/Isaac Gym fluency and that you've already built a sim-to-real stack from scratch — the infrastructure learning curve is behind you. |

---

## 5. Final prep checklist

- [ ] Re-read both O'Keefe papers; write a 2-sentence summary + 1 critique each.
- [ ] Rehearse the 2-minute and 5-minute versions of your sim-to-real project story.
- [ ] Memorize your own numbers and the baseline you compared against.
- [ ] Prepare 3 concrete failure modes from your work and the fix for each.
- [ ] Prepare 2–3 concrete ideas each on (a) tactile randomization and (b) sample-efficient real fine-tuning.
- [ ] Make your SOP/proposal claims consistent with what you say live — re-read them the night before.
- [ ] Have 5–6 questions ready for her (above).
- [ ] Confirm logistics list: funding, hardware, scope, supervision.
- [ ] Test your video/audio setup if remote; have water and notes off-camera.

**One-line framing to keep in your head the whole time:**
*"I already build and validate sim-to-real manipulation systems — I'm here to push that machinery into tactile, in-hand dexterity, which is exactly your lab's frontier."*
