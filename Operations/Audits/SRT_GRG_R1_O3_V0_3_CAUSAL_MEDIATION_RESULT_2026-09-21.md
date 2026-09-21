---
id: SRT-GRG-R1-O3-V0-3-CAUSAL-MEDIATION-RESULT-20260921
type: experimental_result
status: active
date: 2026-09-21
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/grg_r1_o3_causal_mediation/O3_CAUSAL_MEDIATION_PROTOCOL_v0_3.md
  - Operations/Audits/SRT_GRG_R1_O3_V0_2_INVALID_RESULT_2026-09-21.md
  - Operations/Audits/SRT_GRG_R1_PRODUCTIVE_ADEQUACY_O_CRITERION_REVISION_PASS1_2026-09-20.md
tags: [GRG, GRGR1, O3, CausalMediation, NullResult, SingularSpectrum, TargetBlind]
---

# GRG-R1 O3 v0.3 target-blind causal-mediation result

## 0. Verdict

~~~text
PRIMARY VERDICT = O3-CAUSAL-NULL

recipient triplets valid = 12 / 12
donor exact-feature admission = PASS
transfer target data used = NO
O4 authorization for this RNN spectral family = NO
canonical edit = NO
~~~

This is a valid causal-mediation null, not an implementation invalidity.

## 1. Frozen design

Fresh recipients:

~~~text
seeds = 400..411
~~~

Arms from identical initialization:

~~~text
I = intact
S = S-history singular-spectrum scaffold
D = equal-magnitude D-history spectral-direction control
~~~

All arms received identical five-context source/base-task batches.

No transfer target was generated or evaluated.

Primary metric:

~~~text
gain(t) = accuracy(t) - post-initial-intervention accuracy(0)

GAIN_AUC_0_400
= normalized area under gain(t) through update 400
~~~

Primary contrasts:

~~~text
C_SD = GAIN_AUC_S - GAIN_AUC_D
C_SI = GAIN_AUC_S - GAIN_AUC_I
~~~

PASS required both medians >= 0.02 and both seed-level bootstrap 95% CIs of the means entirely above zero.

## 2. Primary result

| Quantity | Result |
|---|---:|
| valid recipients | 12 / 12 |
| median C_SD | -0.002745 |
| median C_SI | 0.010806 |
| mean C_SD | -0.006542 |
| mean C_SI | 0.014748 |
| bootstrap 95% CI mean C_SD | [-0.038720, 0.016612] |
| bootstrap 95% CI mean C_SI | [-0.017672, 0.051086] |
| mean GAIN_AUC S | 0.457654 |
| mean GAIN_AUC D | 0.464196 |
| mean GAIN_AUC I | 0.442907 |

The full preregistered conjunction fails.

The decisive comparison is S versus the equal-magnitude D-history spectral-direction control:

~~~text
median C_SD < 0
mean C_SD < 0
bootstrap CI crosses 0
~~~

Therefore the S-history spectral direction did not show stable organization-specific causal mediation beyond a source-native alternative history direction.

## 3. Control validity

The v0.3 repair succeeded technically.

Across all reset events:

~~~text
maximum mismatch in requested S vs D singular-value displacement norm
= 1.78e-15

mean mismatch
= 2.09e-16

maximum mismatch in recurrent Frobenius operator displacement
= 9.54e-7

mean Frobenius mismatch
= 2.79e-7
~~~

Thus the null cannot be attributed to a material failure of the frozen parameter-distance matching.

## 4. Immediate competence guard

Mean post-initial-intervention update-0 accuracy:

~~~text
I = 0.51620
S = 0.51453
D = 0.50920
~~~

The primary metric was baseline-centered within each arm, so these small immediate competence differences did not automatically count as learning benefit.

## 5. Secondary observations — no rescue

All three arms eventually reached perfect mean final accuracy:

~~~text
mean final accuracy I = 1.0
mean final accuracy S = 1.0
mean final accuracy D = 1.0
~~~

Median first checkpoint reaching >= 0.95:

~~~text
I = 100 updates
S = 50 updates
D = 50 updates
~~~

This says spectral intervention can alter early source-domain learning relative to intact networks.

It does not support an S-specific causal mediator because D-history direction performed at least as well under the primary matched comparison.

Seed counts:

~~~text
C_SD > 0      in 5 / 12
C_SD >= 0.02 in 3 / 12
C_SI >= 0.02 in 4 / 12
~~~

No secondary pattern changes the primary NULL verdict.

## 6. Meaning for GRG-R1

The result preserves three distinct statements:

~~~text
O1:
history leaves a reproducible operator spectral imprint
= SUPPORTED

generic operator intervention:
spectral scaffold manipulation can alter early learning
= SUPPORTED AS SECONDARY SOURCE-DOMAIN EFFECT

O3:
the S-history operator direction specifically mediates later learning
beyond an equal-magnitude D-history direction
= NOT SUPPORTED
~~~

Therefore:

~~~text
history-discriminative operator structure
!= history-specific causal retained organization by default
~~~

This is a stronger constraint than the earlier decoder-null:

~~~text
decodability != causal O
and now
history-classifiable operator spectrum != causal O
unless intervention direction itself has specific causal consequence.
~~~

## 7. O3 disposition

For this toy RNN singular-spectrum family:

~~~text
O1 formation = PASS
O2 retained operator structure = PAID AS DESCRIPTIVE / STRUCTURAL CANDIDATE
O3 target-blind causal mediation = NULL
O4 prospective re-entry = BLOCKED
new transfer target = DO NOT OPEN
v0.4 tuning = DO NOT START by default
~~~

Do not tune:

- number of singular values;
- scaffold centroids;
- reset frequency;
- recipient task;
- thresholds

to seek a positive result inside this family.

Any renewed RNN O3 attempt would require a materially different source-native mechanism and a new rationale, not parameter search.

## 8. Cross-workstream consequence

Current live main also contains the independent non-RNN HKB GRG-R1c route.

The RNN O3 null strengthens the reason to keep that route independent:

~~~text
RNN spectral history imprint
did not earn O3 causal mediation;

HKB relative-phase perturbation / relaxation
remains a separate source-native causal candidate
subject to its own measurement and data-access gates.
~~~

Do not use the RNN null as evidence for HKB success.

Do not use HKB feasibility to rescue the RNN null.

## 9. Programme scorecard

### Constraint

PASS.

The programme rejects a second attractive mapping rather than widening GRG-R1 to absorb it.

### Transfer

PARTIAL.

GRG generated a stricter source-domain causal comparison, including an equal-parameter-distance history-direction control.

The candidate failed that comparison.

### Revision

PASS.

Future retained-organization candidates need not merely be:

~~~text
history-formed
+ structurally persistent
+ manipulable
~~~

They must show **organization-specific causal directionality** relative to credible alternative organization controls.

### Canonical consequence

~~~text
NONE
~~~

No Level change, no scientific-distinctiveness promotion and no canonical owner edit are licensed.
