---
id: SRT-GRG-R1-NEUROSCIENCE-TRANSFER-PILOT-RESULT-20260920
type: experimental_result
status: active
date: 2026-09-20
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Proposals/SRT_GRG_R1_NEUROSCIENCE_TRANSFER_PILOT_CHARTER_2026-09-20.md
  - Experiments/grg_r1_neuro_transfer_pilot/PREREGISTRATION_v0_1.md
  - Operations/Audits/SRT_GRG_DISTRIBUTED_NEIGHBOR_EXTRACTION_PASS1_2026-09-20.md
tags: [GRG, GRGR1, TransferPilot, Neuroscience, RNN, NullResult, Withdrawal, Preregistered]
---

# GRG-R1 bounded neuroscience transfer pilot — result

## 0. Verdict

~~~text
PRIMARY VERDICT = PILOT-NULL

PILOT-PASS = NO
PILOT-INVALID = NO
PILOT-SEMANTIC-FAIL = NO
~~~

All 24 preregistered networks completed and passed the three admission requirements used in the primary merge:

~~~text
eligible Structured S = 12 / 12
eligible Direct D     = 12 / 12
eligible total        = 24 / 24
~~~

The null is therefore not an eligibility or execution failure.

## 1. Frozen hypothesis and pass rule

The preregistered operationalization defined an independently decoded context-routing subspace O from base-task activity, then compared:

~~~text
I-O = targeted projection removal of O
I-R = rank-matched random-subspace removal
I-N = hidden-state displacement-magnitude-matched isotropic noise
~~~

Primary contrasts:

~~~text
C_R = Delta_O - Delta_R
C_N = Delta_O - Delta_N
~~~

PILOT-PASS required all of:

~~~text
eligible S >= 8
eligible D >= 8
median C_R >= 0.03
median C_N >= 0.03
bootstrap 95% CI of mean C_R entirely > 0
bootstrap 95% CI of mean C_N entirely > 0
no semantic drift
~~~

No threshold, held-out context, intervention interval, random-control count, target schedule, O-extraction rule or bootstrap rule was changed after target execution began.

## 2. Primary result

| Quantity | Result |
|---|---:|
| eligible S | 12 |
| eligible D | 12 |
| median C_R | 0.000719 |
| median C_N | -0.152512 |
| mean C_R | 0.032623 |
| mean C_N | -0.151262 |
| bootstrap 95% CI mean C_R | [0.001675, 0.065597] |
| bootstrap 95% CI mean C_N | [-0.193555, -0.108447] |
| mean Delta_O | 0.026385 |
| mean Delta_R | -0.006238 |
| mean Delta_N | 0.177647 |
| mean intact transfer AUC | 0.785090 |
| mean targeted-O transfer AUC | 0.758705 |
| mean random-control transfer AUC | 0.791329 |
| mean noise-control transfer AUC | 0.607443 |

Two facts must be kept together.

First, targeted O removal had a positive mean contrast against random subspace removal:

~~~text
mean C_R = +0.0326
bootstrap CI of mean C_R > 0
~~~

but this did not satisfy the preregistered distributional burden:

~~~text
median C_R = 0.000719 < 0.03
~~~

Only 9 / 24 networks had C_R >= 0.03.

Second, and more decisively, targeted O removal was much less disruptive than the magnitude-matched noise control:

~~~text
median C_N = -0.1525
mean C_N   = -0.1513
95% CI of mean C_N is wholly below zero
~~~

Only 1 / 24 networks had C_N >= 0.03.

Therefore the complete preregistered conjunction fails.

## 3. What the null means

The pilot tested one specific operationalization:

A low-dimensional base-task context-decodable subspace is a candidate retained organization O whose later re-entry is specifically necessary for transfer accessibility.

That operationalization is not supported by the preregistered withdrawal test.

The result does not warrant:

~~~text
decodable context subspace
= causal retained organization
= GRG-R1 O
~~~

A representation can be highly decodable and still fail the stronger organization-specific causal burden.

This is exactly the kind of distinction the GRG programme requires if it is to avoid retrospective relabeling.

## 4. What the null does not mean

Do not infer:

~~~text
GRG-R1 is universally false;
retained organization never re-enters later generation;
history has no effect;
recurrent organization is epiphenomenal;
Simondon / synergetics-style recurrence is refuted;
SRT ontology is refuted or confirmed.
~~~

The result is local to:

~~~text
synthetic tanh RNN
+ this compositional task
+ final-state linear context-decoder-defined O
+ this projection-withdrawal intervention
+ this transfer criterion.
~~~

The correct update is to reject or narrow this O-identification strategy, not to change GRG-R1 after the fact.

## 5. Secondary history observations — non-rescue only

Both histories reached perfect mean base competence and all networks admitted an O.

Structured S:

~~~text
mean intact transfer AUC = 0.79056
mean targeted-O Delta_O = 0.01822
median C_R = -0.00322
median C_N = -0.21556
k*: 8 networks at k=3, 4 at k=2
mean admitted context-decoding score = 0.96956
~~~

Direct D:

~~~text
mean intact transfer AUC = 0.77962
mean targeted-O Delta_O = 0.03455
median C_R = 0.00820
median C_N = -0.09560
k*: 9 networks at k=2, 3 at k=3
mean admitted context-decoding score = 0.99206
~~~

These exploratory differences do not alter the primary verdict and are not used to create a history-specific positive claim.

## 6. Important negative-control lesson

The strongest constructive outcome is methodological:

~~~text
decodability != organization-specific causal re-entry
~~~

More specifically:

~~~text
high held-out decoding of a formed representational subspace
does not license treating that subspace as the retained organization
whose withdrawal uniquely changes later accessibility.
~~~

The magnitude-matched noise result is also a guard against over-reading generic perturbation:

~~~text
generic hidden-state disruption can impair transfer much more strongly
than targeted removal of the decoded subspace.
~~~

Thus a future O must be identified by a stronger mediator / dynamical / intervention criterion, not merely by what information a linear decoder can read.

## 7. GRG programme scorecard

### Compression

PARTIAL / RETAIN.

GRG-R1 still provides a compact common problem connecting operation -> retained organization -> later condition across Simondon, synergetics and recurrent neural dynamics.

The pilot does not validate universality.

### Constraint

PASS.

The frozen relation rejected a tempting mapping:

~~~text
context-decodable subspace -> GRG-R1 O
~~~

rather than absorbing the null by semantic drift.

This is positive evidence that the programme can constrain its own mappings.

### Transfer

PARTIAL / NEGATIVE RESULT.

GRG-R1 generated a domain-native design constraint beyond a history coefficient:

~~~text
independent O identification
+ targeted withdrawal
+ rank-matched random control
+ magnitude-matched generic-damage control.
~~~

However the chosen O failed the preregistered causal test, so no positive realization was earned.

### Revision

PASS.

The grammar programme must now record:

~~~text
information-bearing / decodable organization
!= causal retained organization by default.

future GRG-R1 pilots need a stronger pre-target O admission rule
based on mediator/dynamical/causal organization,
not target-blind decodability alone.
~~~

This is a revision to research method, not a canonical ontology edit.

## 8. Preregistration fidelity / execution note

Frozen implementation preregistration commit:

~~~text
dfe642ab07868fabd93e1b38406ff4aac28d90e8
~~~

Initial runner commit:

~~~text
5a93f94a2cc2512e095c8faacd1ced025ceb532c
~~~

A later implementation-only optimization vectorized batch construction and execution was changed to restart-safe per-network scheduling because the execution environment repeatedly timed out under monolithic / parallel runs.

No preregistered scientific field was changed:

~~~text
target context: unchanged
network size: unchanged
histories: unchanged
seed set: unchanged
O extraction: unchanged
O admission: unchanged
intervention definition/timing: unchanged
random controls: unchanged
noise-matching rule: unchanged
fine-tuning schedule: unchanged
primary metric: unchanged
PASS thresholds: unchanged
bootstrap rule: unchanged
~~~

Final merge used exactly 24 unique network rows, one for each S/D x seed 0..11.

## 9. Disposition

~~~text
GRG-R1 abstract relation: RETAIN AS RESEARCH CANDIDATE
current decoder-defined O operationalization: REJECT / NOT SUPPORTED
PILOT-PASS: NO
canonical edit: NO
new Level 1: NO
Level 2: HOLD
scientific distinctiveness: NOT ESTABLISHED
winner-style strongest-neighbor audit: DO NOT REOPEN
~~~

## 10. Next bounded step

Do not tune this v0.1 pilot into a success.

Next work should be a productive-adequacy / revision pass asking:

1. what source-native property should qualify O before transfer if decodability is insufficient?
2. can Bowler-style recurrent eigenspectrum / dynamical scaffold, synergetic order-parameter logic, or Simondonian operation-structure recurrence supply a stronger pre-target O criterion?
3. can that criterion be frozen using only base-task dynamics and intervention structure?
4. what control distinguishes organization-specific withdrawal from generic task damage without using the target outcome to choose O?

Any v0.2 pilot must be a new visible charter and preregistration. v0.1 remains permanently NULL.
