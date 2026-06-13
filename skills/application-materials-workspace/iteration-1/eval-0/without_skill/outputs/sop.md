# Statement of Purpose

**Applicant:** Test Applicant
**Program:** PhD in Informatics, University of Edinburgh
**Proposed supervisor:** Dr. Maria O'Keefe
**Project:** Sim-to-real dexterous (in-hand) manipulation
**Intended start:** 2027

## Research motivation

My research goal is to build robots that learn dexterous manipulation skills in simulation and deploy them reliably in the real world. Over the course of my MSc I have come to believe that the central obstacle is not raw policy capacity but the sim-to-real gap, and that the most promising way to close it is principled randomization of the right signals during training. I want to spend my PhD pushing this idea from pick-and-place toward genuinely dexterous, in-hand manipulation that generalizes across object shapes, which is precisely the agenda of Dr. O'Keefe's group at Edinburgh.

## What I have done

My MSc thesis, "Domain Randomization Schedules for Sim-to-Real Transfer in Pick-and-Place" (advised by Dr. R. Patel), studies how the *schedule* of domain randomization affects transfer rather than treating randomization as a static design choice. In the Patel Robot Learning Lab I built an end-to-end MuJoCo-to-real pick-and-place pipeline, designed curriculum domain-randomization schedules, and validated the resulting policies on physical hardware, achieving 88% success on a 6-object set with a UR5 arm. This work became a workshop paper, "Curriculum Domain Randomization for Sim-to-Real Manipulation," presented at the CoRL Robot Learning Workshop (2025), where I also gave a poster. Earlier, as an undergraduate research assistant, I implemented PPO baselines for a grasping benchmark, which is where my interest in manipulation began.

Through this work I have developed the concrete skills this project needs: reinforcement learning (PPO/SAC), simulation in MuJoCo and Isaac Gym, ROS, and hands-on real-robot experimentation with a UR5 arm. Crucially, I have already lived the full sim-to-real loop, designing randomization, training in simulation, and confronting the realities of deployment on hardware, rather than working only in simulation.

## Why Edinburgh and Dr. O'Keefe

My background and Dr. O'Keefe's research agenda meet at exactly the point I find most interesting. To date, my randomization work has targeted vision and geometry: I randomize object appearance and shape to make policies robust to the visual and geometric sim-to-real gap. Dr. O'Keefe's 2025 work, "Tactile-Guided Sim-to-Real for In-Hand Manipulation," reframes this problem around a different and harder signal, showing that randomizing *simulated tactile* feedback can close the sim-to-real gap for re-orientation tasks. This is a natural and exciting extension of my own thinking. The methodological question I would most like to pursue is how to randomize tactile signals effectively, given that the assumptions and noise models that work for vision and geometry do not obviously transfer to contact and touch.

This connects directly to two open problems in the group: how to randomize tactile signals (not just vision and geometry) in a principled way, and how to fine-tune dexterous policies sample-efficiently in the real world. My thesis on randomization *schedules* is relevant to both, since the question of *what* to randomize and the question of *when and how much* to randomize are deeply linked, and curriculum ideas that helped pick-and-place transfer may carry over to tactile in-hand manipulation. I see the move from "Learning Dexterous Policies with Sparse Tactile Feedback" (2024) toward generalist in-hand manipulation that transfers across object shapes as the kind of long-horizon problem I want to commit to.

## Proposed direction

For the named project I would like to start by extending curriculum-based randomization from visual and geometric parameters to tactile ones, asking which tactile randomization strategies most improve real-world transfer of in-hand re-orientation policies, and whether scheduling those strategies (as opposed to applying them statically) improves sample efficiency during real-world fine-tuning. My MuJoCo-to-real and Isaac Gym experience gives me a running start on the simulation and hardware infrastructure such a study requires. [I would welcome the chance to discuss which tactile sensing hardware and benchmark tasks the project is built around, so I can sharpen this direction.]

## Goals and fit

I am academia-leaning and want to train in a lab that is actively pushing dexterous manipulation and generalist robot policies, which is why this fully funded, named project is a strong match for both my interests and my circumstances. [I require a fully funded position, which this opening provides.] I expect to complete my MSc in 2026 and to begin a PhD in 2027, aligning with the project timeline.

I would be honored to pursue this work under Dr. O'Keefe's supervision within the Edinburgh Informatics PhD program, and I am confident that my sim-to-real manipulation background, combined with the group's leadership in tactile-informed dexterous control, would make for a productive collaboration.

[Contact details, references, and any program-specific requirements to be supplied by the applicant.]
