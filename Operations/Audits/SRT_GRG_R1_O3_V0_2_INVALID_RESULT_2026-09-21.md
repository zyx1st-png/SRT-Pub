---
id: SRT-GRG-R1-O3-V0-2-INVALID-RESULT-20260921
type: experimental_result
status: active
date: 2026-09-21
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/grg_r1_o3_causal_mediation/O3_CAUSAL_MEDIATION_PROTOCOL_v0_2.md
  - Operations/Audits/SRT_GRG_R1_O3_V0_1_PREEXECUTION_VALIDITY_AUDIT_2026-09-21.md
tags: [GRG, GRGR1, O3, Invalid, ControlGeometry, TargetBlind]
---

# GRG-R1 O3 v0.2 result — INVALID before causal outcome

## Verdict

~~~text
O3-INVALID
reason = parameter-distance-matched random spectral control infeasible
post-intervention recipient learning outcomes = NONE
transfer target data used = NO
~~~

## 1. Donor exact-feature admission passed

Fresh donor seeds 200..211:

~~~text
S competent = 12/12
D competent = 12/12
paired-seed CV accuracy on top-four singular values = 1.00
1000 within-pair permutations
p = 0.001998001998001998
null mean = 0.502458
null 95% = [0.041667, 0.833333]
~~~

Frozen centroids:

~~~text
mu_S = [6.236416, 5.433141, 4.753791, 3.941183]
mu_D = [4.691599, 3.538975, 2.846765, 2.503406]
~~~

Thus the exact feature intended for O3 independently paid the donor formation gate.

## 2. Recipient control construction failed before learning outcomes

For fresh recipients 300..311, orthogonal initialization gives current leading singular values approximately:

~~~text
[0.8, 0.8, 0.8, 0.8]
~~~

The first S-scaffold displacement is therefore approximately:

~~~text
d_S = [5.4364, 4.6331, 3.9538, 3.1412]
||d_S||_2 = 8.7476
~~~

v0.2 required the random control simultaneously to:

- have the same displacement norm;
- have abs cosine <= 0.25 to d_S;
- keep every proposed singular value strictly positive.

No valid direction was found in 1000 deterministic draws for any of the 12 recipients.

All 12 triplets stopped at the first reset.

## 3. Why this is INVALID rather than NULL

The causal comparison never existed.

No arm completed post-intervention source-domain learning.

Therefore:

~~~text
O3-CAUSAL-NULL = NOT LICENSED
O3-CAUSAL-PASS = NOT LICENSED
O3-INVALID = REQUIRED
~~~

Initial pre-intervention accuracy may have been computed by the runner, but it is common to the copied arms and is not a causal outcome.

## 4. Design lesson

Matching an extremely large S-scaffold displacement with a near-orthogonal random direction while preserving positive singular values is not a generally feasible control geometry near the naive operator.

This is a control-design failure, not evidence against the scaffold.

A revised protocol may be created because no causal outcome was generated.

The next control should remain parameter-distance matched but use a feasible source-native spectral direction fixed before outcomes.

## 5. Allowed revision

The strongest available control direction is the independently formed D-history centroid.

A v0.3 design may compare:

~~~text
S-direction intervention
vs
D-history-direction intervention scaled to the same top-four singular displacement norm
vs
intact
~~~

This preserves:

- equal intervention magnitude by construction;
- a history-derived alternative spectral direction;
- source-domain-only evaluation;
- target blindness.

Any v0.3 must be frozen before post-intervention recipient outcomes.
