# Interview prep — Maria O'Keefe, University of Edinburgh (Informatics)

**Interview:** July (date TBC) · **Application:** edinburgh-dexterous · **Stage:** positive reply, proposal + interview invited

## How to read this
A PhD interview with Dr. O'Keefe is a two-way fit conversation. She's checking whether you
think well, own your own work, and would be good to mentor for 3–4 years on her dexterous
manipulation project. You're checking whether the lab is right for you. The goal is not to
memorize these answers — it's to walk in having genuinely thought through each of these, so
you can have a real conversation. Where an answer needs a specific only you can supply, it's
in `[brackets]` — fill those in before the interview.

**The one gap to get ahead of:** your sim-to-real and domain-randomization work is on
**vision/geometry** randomization, and her current frontier is **tactile** randomization for
in-hand manipulation. She knows this (it's the noted fit gap). Don't hide it — show you've
read her tactile work and have concrete thoughts on how your skills transfer to it. That
single move turns the gap into your strongest fit signal.

---

## 1. Motivation & fit

**Q: Why a PhD, and why my lab specifically?**
- *Model answer:* "I want to do research in academia, and my MS work convinced me that
  sim-to-real for manipulation is the problem I want to push on for the next several years —
  I keep running into the gap between simulated success and real-robot robustness. Your lab
  is one of the few working directly on the next layer of that problem: generalist *in-hand*
  manipulation that transfers across object shapes. My background is curriculum domain
  randomization for pick-and-place on a real UR5; your 2025 tactile sim-to-real paper is
  exactly where I'd want to take that next — from randomizing vision and geometry to
  randomizing tactile signals."
- *Coaching:* She's probing genuine, specific interest vs. scattershot applying. The tell is
  naming her actual papers and the actual open problem (tactile randomization), not "your lab
  is excellent." Be ready to say honestly why *Edinburgh / her project* over other
  manipulation labs — `[name 1 concrete reason: the named fully-funded dexterous project, her
  specific sim-to-real angle, etc.]`.

**Q: Why now / why this start?**
- *Model answer:* "I finish my MS in 2026 and I've taken the sim-to-real pick-and-place work
  as far as I can at the MS level — I have a real-robot pipeline and a workshop paper, and I
  want to go deeper on the harder dexterous version under proper supervision rather than
  repeat the same difficulty level."
- *Coaching:* Short and confident. Shows momentum, not restlessness.

---

## 2. Your own work (expect the deepest probing here)

She will go deep on your MS thesis and workshop paper — this is where she learns whether you
*own* your work and think critically about it.

**Q: Walk me through your domain-randomization schedules. Why a curriculum rather than fixed
randomization?**
- *Model answer:* "Fixed wide randomization makes the early policy try to be robust to
  everything at once, which slows learning and can hurt final real-world performance. I
  schedule the randomization — start narrow so the policy learns the core skill, then widen
  the distribution over training so it becomes robust without destabilizing early learning. On
  the UR5 6-object pick-and-place set that got me to 88% real-robot success."
- *Coaching:* This is your home turf — be specific and own the design decision. She'll respect
  a clear rationale far more than a buzzword. Have the numbers ready: `[what was the baseline
  / fixed-randomization success rate you compared against? state the delta]`.

**Q: What broke in sim-to-real, and what would you do differently?**
- *Model answer:* "The biggest residual gap was `[name the dominant failure mode — e.g.
  contact dynamics / friction mismatch / perception under novel lighting]`. If I redid it I'd
  `[e.g. add system identification on the real friction, or randomize the contact model, or
  collect a small real fine-tuning set]`. That's actually part of why your sample-efficient
  real-world fine-tuning direction interests me."
- *Coaching:* This is the single most important question. She's testing intellectual honesty
  and self-critique — a candidate who says "nothing, it worked great" fails it. Name a *real*
  limitation and a *concrete* fix. Do NOT invent a sophisticated-sounding failure you can't
  defend under follow-up; pick the true one. Bridging your fix to her fine-tuning agenda is
  the bonus.

**Q: Your 88% — where did the other 12% fail, and is 88% actually good?**
- *Model answer:* "Failures clustered on `[which objects/conditions — e.g. low-friction or
  small objects, cluttered poses]`. Whether 88% is good depends on the baseline and the task
  difficulty; against `[baseline]` it was a `[X]`-point improvement, but for deployment it's
  not yet enough, which is the direction I'd want to push."
- *Coaching:* She's checking whether you interrogate your own headline number. Don't be
  defensive; show you know exactly where it breaks.

**Q: Tell me about the PPO baselines / your RL stack.**
- *Model answer:* "I've implemented PPO baselines for a grasping benchmark and used PPO/SAC in
  the thesis work, in MuJoCo and Isaac Gym with a ROS bridge to the real UR5."
- *Coaching:* Foundations check. Be ready for "why SAC vs PPO here?" — `[have a one-line
  answer: e.g. SAC's sample efficiency / off-policy reuse for the real-robot setting]`.

---

## 3. The lab's work & the proposed research

She invited a research proposal alongside the interview, so expect her to test how you'd
engage with *her* actual problems.

**Q: I work on tactile randomization for in-hand manipulation. How does that differ from your
visual/geometry domain randomization, and how would you approach it?**
- *Model answer:* "With vision/geometry I'm randomizing what the policy *sees* and the object
  shapes/poses — the observation and the kinematics. Tactile randomization is harder because
  the signal is generated by contact: you're randomizing the *physics of contact* and the
  sensor model — friction, contact stiffness, sensor noise and dropout, calibration drift —
  and these feed a control loop rather than just a perception stage. I'd start by treating the
  tactile sensor model the way I treated the camera: identify which contact parameters the
  real sensor is most sensitive to, randomize those in sim, and use a schedule so the policy
  learns the core in-hand skill before being asked to be robust to the full tactile
  distribution. Then a small real-world fine-tuning set to close the residual gap."
- *Coaching:* **This is the make-or-break question.** It directly tests whether you can carry
  your skills onto her frontier. The structure above — name the difference (contact physics
  vs. perception), then propose a concrete transfer of your curriculum/schedule idea — is
  exactly the reasoning she'd want from a student. Read the 2025 paper closely enough to use
  its framing. Don't overclaim tactile expertise you don't have; frame it as "here's how my
  approach transfers," which is true and impressive.

**Q: In the 2025 paper we randomize tactile signals to close the sim-to-real gap. What did you
take from it, and what would you push on next?**
- *Model answer:* "What I took is that the sim-to-real gap for dexterous tasks lives in the
  contact/tactile channel, not just vision, so the randomization has to move there. What I'd
  push on is generalization across object *shapes* — does a tactile policy trained on one
  shape distribution transfer to genuinely novel geometries, or does it need per-shape
  fine-tuning? And how sample-efficient can that real-world fine-tuning be?"
- *Coaching:* This names her two stated open problems (effective tactile randomization;
  sample-efficient real fine-tuning) and the generalist-across-shapes goal. Showing you've
  located the open edge of her work is the strongest possible signal of fit.

**Q: What would you want to work on in your first year here?**
- *Model answer:* "Concretely: reproduce a tactile sim-to-real re-orientation result to get
  fluent with the tactile pipeline, then run a focused study on `[e.g. shape generalization or
  a tactile randomization schedule]`. I'd want the first year to produce one solid result and
  teach me the lab's stack, not boil the ocean."
- *Coaching:* She's assessing whether you scope realistically and would be good to mentor.
  Modest, concrete, buildable beats grand and vague. Align this with your proposal.

---

## 4. Technical depth

**Q: Why does naive wide domain randomization sometimes hurt final performance?**
- *Model answer:* "It widens the task distribution faster than the policy can absorb — you pay
  an optimization cost being robust to regions you rarely face, and can converge to a
  conservative policy that underperforms in the real operating regime. A schedule or an
  automatically-tuned randomization range mitigates this."
- *Coaching:* Foundations she'll expect from anyone in this subfield. You know this cold.

**Q: How do you decide *what* to randomize?**
- *Model answer:* "Identify the parameters the real system is most sensitive to and least
  certain about — measure or system-identify where you can, randomize where you can't. For
  tactile that'd be contact friction/stiffness and sensor noise rather than randomizing
  everything uniformly."
- *Coaching:* Tests reasoning, not recall. The "measure where you can, randomize where you
  can't" principle is the mature answer.

**Q: Sim-to-real vs. just collecting real data — when is each right?**
- *Model answer:* "Real data is gold but expensive and risky for dexterous contact-rich tasks;
  sim gives scale and safety but has a reality gap. The pragmatic answer is sim for the bulk of
  learning plus a small, sample-efficient real fine-tuning pass — which is exactly the
  efficiency question your lab works on."
- *Coaching:* Ties a fundamentals question back to her agenda; do that whenever it's honest.

---

## 5. Behavioral / working style

**Q: Tell me about a time an experiment failed or a result didn't replicate.**
- *Model answer:* `[Pick one real instance from the thesis — e.g. a randomization range that
  worked in sim but tanked on the real UR5. Describe: what happened, how you diagnosed it,
  what you changed, what you learned.]`
- *Coaching:* She's looking for resilience and a debugging methodology, not a flawless record.
  Have one concrete, true story ready — STAR-ish: situation, what you tried, what you learned.

**Q: How do you like to be supervised — independent or hands-on?**
- *Model answer:* "I work best with regular direction early to learn the lab's standards, then
  more independence as I find my footing — and I like to bring problems early rather than sit
  stuck." `[Adjust to what's actually true for you.]`
- *Coaching:* No wrong answer, but be honest — mismatch here causes real friction over 4 years.
  This is also you evaluating *her* mentorship style.

**Q: How do you handle collaboration / sharing a robot and codebase?**
- *Model answer:* "In the Patel lab I shared the UR5 and pipeline — I'm used to scheduling
  hardware time, keeping the codebase reproducible, and documenting so others can run my
  experiments."
- *Coaching:* Dexterous labs share scarce hardware; signal you're a good lab citizen.

---

## 6. Questions you should ask her (asking well is itself evaluated)

- "Is this the named fully-funded dexterous-manipulation project, and what's the planned arc
  of it over a PhD?" *(You know it's funded — confirm scope and that the funding covers the
  full PhD.)*
- "What does the tactile hardware setup look like day-to-day — which sensors, and how much of
  a student's time goes to hardware vs. learning?"
- "How do you balance sim and real in the group right now — is most work in sim with periodic
  real validation, or continuous real-robot work?"
- "What's your mentorship style, and how often do students meet with you?"
- "Where have your recent PhD students gone — academia, industry research labs?"
- "What would make a first-year student in this project a success in your eyes?"
- "Is there room to shape the project toward shape-generalization, or is the direction fairly
  set by the funding?"

*Coaching:* These show you've read her work, care about fit, and are thinking like a colleague.
Pick 3–4 that matter most to you — don't rattle off all seven.

---

## Before the interview: review these

1. **O'Keefe 2025 — "Tactile-Guided Sim-to-Real for In-Hand Manipulation"** (her flagship;
   know the tactile randomization method and re-orientation results cold).
2. **O'Keefe 2024 — "Learning Dexterous Policies with Sparse Tactile Feedback"** (the
   precursor — how she handles sparse tactile signals).
3. **Your own MS thesis** — be ready to defend the curriculum schedule design, the 88% number
   and its failures, and your one honest "what I'd do differently."
4. **Your CoRL workshop paper** — one-paragraph summary you can give from memory.

## Fill-in checklist (do these before July)
- [ ] Baseline/fixed-randomization success rate to contrast with your 88%
- [ ] The dominant real-world failure mode in your thesis + your concrete fix
- [ ] Which objects/conditions the 12% failures clustered on
- [ ] Your one real "experiment that failed" story
- [ ] Your honest answer on supervision style
- [ ] One concrete extra reason it's *her project* over other manipulation labs
- [ ] Read the 2025 paper closely enough to discuss its tactile randomization specifics
