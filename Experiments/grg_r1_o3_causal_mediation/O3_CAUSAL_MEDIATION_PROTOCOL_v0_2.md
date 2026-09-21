---
id: SRT-GRG-R1-O3-CAUSAL-MEDIATION-PROTOCOL-V0-2-20260921
type: experimental_protocol
status: frozen
date: 2026-09-21
layer: experiments
epistemic_layer: experimental
claim_mode: prediction
canonical: false
ai_do_not_use_for_definition: true
supersedes:
  - Experiments/grg_r1_o3_causal_mediation/O3_CAUSAL_MEDIATION_PROTOCOL_v0_1.md
dependency:
  - Operations/Audits/SRT_GRG_R1_O3_V0_1_PREEXECUTION_VALIDITY_AUDIT_2026-09-21.md
  - Operations/Audits/SRT_GRG_R1_PRODUCTIVE_ADEQUACY_O_CRITERION_REVISION_PASS1_2026-09-20.md
  - Operations/Audits/SRT_GRG_R1_O_FEASIBILITY_SPECTRAL_FORMATION_RESULT_2026-09-20.md
  - Materials/2026/SRC_2026_09_08_Neuro_Bowler_Structured_Experience_Strategy_Dynamics.md
tags: [GRG, GRGR1, O3, CausalMediation, SingularSpectrum, RNN, TargetBlind]
---

# GRG-R1 O3 target-blind causal-mediation protocol v0.2

## 0. Scope lock

This protocol supersedes v0.1 before any O3 outcome was generated.

It tests O3 only.

It may use the original base/source-domain task and its learning trajectory.

It must not:

- generate or inspect any new transfer target;
- reuse the old held-out transfer context as an outcome;
- choose an operator feature from recipient outcomes;
- open O4 or v0.2 transfer execution.

Question:

> Does a history-formed recurrent operator scaffold causally bias later learning on the same source-domain task beyond intact learning and a parameter-distance-matched random spectral perturbation?

## 1. Domain realization

The intervention is Bowler-inspired but not claimed as an exact replication.

Bowler's source-native pattern is:

~~~text
history
-> recurrent operator spectral organization
-> spectral scaffold intervention
-> changed later learning
~~~

For numerical real-valued stability, this toy protocol uses the leading **singular spectrum** of the recurrent operator rather than direct complex-eigenvalue replacement.

That implementation choice is frozen before results.

## 2. Fresh donor formation set

Donor initialization seeds:

~~~text
200..211
~~~

For each seed train paired histories with identical initialization:

Structured S:

~~~text
300 updates identity contexts features 1,2,3
300 updates invert contexts features 1,2
600 updates all five base contexts
total = 1200
~~~

Direct D:

~~~text
1200 updates all five base contexts
~~~

Architecture, optimizer and batch size are inherited unchanged from the merged v0.1 runner.

Donor competence:

~~~text
held-out base accuracy >= 0.95
~~~

All 12 S and 12 D donors are required for a primary O3 verdict.

## 3. Exact O3 scaffold feature

For each donor recurrent matrix W_h:

1. compute singular values;
2. sort descending;
3. retain the first four;
4. define s4 = [sigma1, sigma2, sigma3, sigma4].

Define:

~~~text
mu_S = mean s4 across 12 S donors
mu_D = mean s4 across 12 D donors
~~~

No recipient outcome enters either centroid.

## 4. Exact-feature donor admission

Because O1 Pass A used a different 12-dimensional eigenvalue feature, this O3 intervention feature must independently pay formation pressure.

Use top-four singular-value vectors only.

Classifier:

~~~text
logistic regression
training-fold z-scoring only
12-fold Leave-One-Seed-Pair-Out
test fold = S and D donors sharing one initialization seed
~~~

Permutation:

~~~text
1000 within-pair S/D label swaps
fixed RNG seed = 20260921
p = (1 + count(null_accuracy >= observed_accuracy)) / 1001
~~~

Scaffold admission requires:

~~~text
12/12 S competent
12/12 D competent
paired CV accuracy >= 0.75
permutation p <= 0.05
~~~

If not:

~~~text
O3-SCAFFOLD-NOT-ADMITTED
~~~

and recipient causal execution stops.

## 5. Fresh recipient set

Recipient initialization seeds:

~~~text
300..311
~~~

Each seed creates three arms from the identical initialized network:

~~~text
I = intact direct learning
S = structured-history spectral scaffold
R = random spectral-direction control
~~~

All arms receive the identical per-seed sequence of five-context base-task training batches.

Recipients do not receive staged curriculum.

## 6. S-scaffold intervention

Fixed reset points:

~~~text
before update 1
after updates 50, 100, 150, 200, 250, 300
~~~

At a reset:

~~~text
W = U diag(s) V^T
s[0:4] <- mu_S
W <- U diag(s) V^T
~~~

Only recurrent weights are changed.

At resets that coincide with evaluation checkpoints, reset occurs **before** checkpoint evaluation.

After update 300 no further reset occurs.

## 7. Parameter-distance-matched random control

At every S reset compute:

~~~text
d_S = mu_S - current_S_s4
L = ||d_S||_2
~~~

For the R arm at the corresponding reset:

1. compute its current top-four singular values;
2. draw deterministic random unit direction q in R^4;
3. require abs(cos(q, d_S)) <= 0.25 when d_S is nonzero;
4. set random displacement d_R = L*q;
5. require proposed singular values remain strictly positive;
6. replace R top-four singular values by current_R_s4 + d_R.

Random seed:

~~~text
20260921 + 1000 * recipient_seed + reset_index
~~~

Because singular vectors are held fixed during each reset, the Frobenius norm of the operator change equals the L2 singular-value displacement up to numerical tolerance.

Thus S and R are matched on reset magnitude but differ in spectral direction.

Failure to find a valid q in 1000 deterministic draws invalidates that recipient triplet.

## 8. Source-domain outcome

Per recipient, create one fixed balanced base evaluation set:

~~~text
500 trials per each of five base contexts
2500 trials total
RNG seed = 700000 + recipient_seed
~~~

Reuse it across I/S/R.

Training checkpoints:

~~~text
0, 10, 25, 50, 100, 150, 200, 300, 400, 600, 800, 1200
~~~

Primary metric:

~~~text
AUC_0_400
= trapezoidal area under held-out base accuracy vs update
  using checkpoints through update 400
  normalized by 400
~~~

Higher is better.

## 9. Primary contrasts

Per recipient seed:

~~~text
C_SR = AUC_S - AUC_R
C_SI = AUC_S - AUC_I
~~~

Inferential unit = recipient initialization seed.

Bootstrap:

~~~text
10000 seed-level resamples
C_SR RNG seed = 20260921
C_SI RNG seed = 20260922
~~~

## 10. O3 verdict contract

O3-CAUSAL-PASS requires all:

~~~text
exact-feature donor admission PASS
12/12 recipient triplets valid
median C_SR >= 0.02
median C_SI >= 0.02
95% bootstrap CI mean C_SR entirely > 0
95% bootstrap CI mean C_SI entirely > 0
~~~

Valid execution without the full conjunction:

~~~text
O3-CAUSAL-NULL
~~~

Donor feature fails admission:

~~~text
O3-SCAFFOLD-NOT-ADMITTED
~~~

Fewer than 10 valid recipient triplets:

~~~text
O3-INVALID
~~~

## 11. Secondary readouts — non-rescue

Report:

- AUC_0_1200;
- final accuracy at 1200;
- first checkpoint >=0.95 accuracy;
- mu_S and mu_D;
- donor exact-feature CV/permutation result;
- per-reset requested singular displacement;
- per-reset S and R Frobenius weight displacement;
- recipient singular-spectrum trajectory.

Secondary results cannot rescue the primary verdict.

## 12. Interpretation ceiling

PASS means only:

> In this toy source domain, a history-associated recurrent operator scaffold causally biases later learning beyond intact learning and a parameter-distance-matched random spectral perturbation.

PASS would pay O3 for this bounded operator family.

PASS would not establish:

- O4 prospective re-entry;
- a new transfer result;
- biological implementation;
- a strict synergetic order parameter;
- SRT scientific distinctiveness;
- canonical ontology or Level change.

NULL means:

Do not choose a new O4 target for this scaffold family. Return to O-criterion revision or another source-native realization.

## 13. Immutable-after-execution fields

After recipient outcome generation begins, do not change:

- donor seeds;
- recipient seeds;
- top-four singular-value feature;
- exact-feature donor admission;
- reset schedule;
- random-control cosine bound;
- evaluation set;
- checkpoints;
- AUC_0_400;
- PASS thresholds;
- bootstrap rules.

Any changed design requires a new protocol version; v0.2 remains preserved.
