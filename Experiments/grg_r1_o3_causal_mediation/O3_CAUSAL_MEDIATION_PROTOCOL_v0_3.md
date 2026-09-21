---
id: SRT-GRG-R1-O3-CAUSAL-MEDIATION-PROTOCOL-V0-3-20260921
type: experimental_protocol
status: frozen
date: 2026-09-21
layer: experiments
epistemic_layer: experimental
claim_mode: prediction
canonical: false
ai_do_not_use_for_definition: true
supersedes:
  - Experiments/grg_r1_o3_causal_mediation/O3_CAUSAL_MEDIATION_PROTOCOL_v0_2.md
dependency:
  - Operations/Audits/SRT_GRG_R1_O3_V0_2_INVALID_RESULT_2026-09-21.md
  - Operations/Audits/SRT_GRG_R1_PRODUCTIVE_ADEQUACY_O_CRITERION_REVISION_PASS1_2026-09-20.md
  - Operations/Audits/SRT_GRG_R1_O_FEASIBILITY_SPECTRAL_FORMATION_RESULT_2026-09-20.md
  - Materials/2026/SRC_2026_09_08_Neuro_Bowler_Structured_Experience_Strategy_Dynamics.md
tags: [GRG, GRGR1, O3, CausalMediation, SingularSpectrum, HistoryDirectionControl, TargetBlind]
---

# GRG-R1 O3 target-blind causal-mediation protocol v0.3

## 0. Scope lock

v0.3 supersedes v0.2 because v0.2's matched random control was geometrically infeasible before any post-intervention learning outcome.

This protocol tests O3 only.

No new transfer target may be generated, selected or inspected.

## 1. Question

Does an S-history recurrent singular-spectrum direction causally improve later learning on the same source-domain base task relative to:

- an intact naive learner; and
- a D-history spectral-direction control with the same intervention magnitude?

Target chain:

~~~text
history
-> retained operator spectral direction
-> target-blind operator intervention
-> later source-domain learning gain
~~~

## 2. Donor formation and exact-feature admission

Reuse the frozen fresh donor set:

~~~text
donor seeds = 200..211
histories = S and D
~~~

Training and competence gates are unchanged from v0.2.

Feature:

~~~text
top-four singular values of recurrent W_h
~~~

Admission:

~~~text
12/12 S competent
12/12 D competent
paired-seed leave-one-pair-out CV >= 0.75
1000 within-pair label swaps
permutation p <= 0.05
~~~

The already executed v0.2 donor admission may be reused because it was generated before any recipient learning outcome and is exactly the same feature/gate.

Frozen donor result:

~~~text
paired CV = 1.00
permutation p = 0.001998001998001998
mu_S = [6.236416, 5.433141, 4.753791, 3.941183]
mu_D = [4.691599, 3.538975, 2.846765, 2.503406]
~~~

## 3. Fresh recipients

Use a new recipient set not touched by v0.2:

~~~text
recipient seeds = 400..411
~~~

Each seed creates three copies of the identical naive initialization:

~~~text
I = intact
S = S-history spectral scaffold
D = D-history spectral-direction magnitude control
~~~

All arms receive identical online base-task batches.

## 4. Reset schedule

Fixed reset points:

~~~text
before update 1
after updates 50, 100, 150, 200, 250, 300
~~~

At a reset, interventions occur before any checkpoint evaluation at that same update.

After update 300 there are no further resets.

## 5. S intervention

For current S-arm recurrent singular values s_S:

~~~text
d_S = mu_S - s_S
L = ||d_S||_2
target_S = mu_S
~~~

Replace only the first four singular values with target_S while retaining current singular vectors and all remaining singular values.

## 6. D-history direction magnitude control

For current D-arm top-four singular values s_D:

~~~text
raw_D = mu_D - s_D
q_D = raw_D / ||raw_D||_2
d_D = L * q_D
target_D = s_D + d_D
~~~

Thus:

~~~text
||d_D||_2 = ||d_S||_2 = L
~~~

but the intervention follows the independently formed D-history spectral direction rather than S-history direction.

If raw_D norm is zero, use no D displacement only if L is also zero; otherwise the triplet is invalid.

If any target_D singular value is <= 0, the triplet is invalid.

This control is source-native and parameter-distance matched; it is not called a random control.

## 7. Source-domain training and evaluation

Training:

~~~text
five-context base task only
Adam lr = 0.01
batch size = 128
updates = 1200
identical per-seed batches across I/S/D
~~~

Balanced held-out evaluation set:

~~~text
500 trials per base context
2500 total
fixed RNG seed = 710000 + recipient_seed
reused across I/S/D
~~~

Evaluation checkpoints:

~~~text
post-initial-intervention update 0,
10, 25, 50, 100, 150, 200, 300, 400, 600, 800, 1200
~~~

For I, update 0 is the intact naive state.

For S and D, update 0 is measured after the initial reset.

## 8. Primary learning-gain metric

To prevent immediate post-intervention competence differences from automatically counting as learning benefit, define per arm:

~~~text
gain(t) = accuracy(t) - accuracy(0)
~~~

Primary:

~~~text
GAIN_AUC_0_400
= trapezoidal area under gain(t) through update 400
  normalized by 400
~~~

Higher means more learning improvement relative to that arm's own post-intervention starting point.

Per recipient:

~~~text
C_SD = GAIN_AUC_S - GAIN_AUC_D
C_SI = GAIN_AUC_S - GAIN_AUC_I
~~~

Inferential unit = recipient seed.

## 9. Primary PASS rule

Bootstrap:

~~~text
10000 seed-level resamples
C_SD seed = 20260923
C_SI seed = 20260924
~~~

O3-CAUSAL-PASS requires all:

~~~text
donor exact-feature admission PASS
12/12 recipient triplets valid
median C_SD >= 0.02
median C_SI >= 0.02
95% bootstrap CI mean C_SD entirely > 0
95% bootstrap CI mean C_SI entirely > 0
~~~

Otherwise, with valid execution:

~~~text
O3-CAUSAL-NULL
~~~

Fewer than 10 valid triplets:

~~~text
O3-INVALID
~~~

## 10. Secondary readouts — non-rescue

Report:

- post-intervention update-0 accuracy for I/S/D;
- raw accuracy AUC_0_400;
- gain AUC_0_1200;
- final accuracy;
- updates to >=0.95;
- per-reset S and D singular-value displacement norms;
- per-reset recurrent Frobenius distance;
- spectral trajectories.

Secondary readouts cannot rescue the primary verdict.

## 11. Interpretation ceiling

PASS means only:

> In this toy source domain, an independently history-formed recurrent spectral direction causally changes later learning gain beyond intact learning and an equal-magnitude D-history spectral-direction perturbation.

PASS pays O3 for this bounded operator family.

It does not establish O4, transfer, biological implementation, strict synergetic order-parameter status, SRT distinctiveness, canonical ontology or a new Level.

NULL means do not open O4 for this spectral family.

## 12. Immutable-after-execution fields

After any post-intervention recipient learning outcome is generated, do not change:

- recipient seeds;
- S and D control definitions;
- reset schedule;
- gain metric;
- checkpoints;
- thresholds;
- bootstrap seeds.

Any changed design requires a new version.
