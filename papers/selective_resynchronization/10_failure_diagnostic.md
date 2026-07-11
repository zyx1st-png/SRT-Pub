---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-V1-FAILURE-DIAGNOSTIC-20260711
type: post_failure_diagnostic
status: completed_v1_diagnostic
layer: paper_working
epistemic_layer: bridge
claim_mode: empirical_diagnostic
claim_level: P4
canonical: false
created: 2026-07-11
depends_on:
  - PAPER-SELECTIVE-RESYNCHRONIZATION-MVP-DECISION-20260711
---

# Failure Diagnostic for the Fashion-MNIST MVP

## 0. Scope and non-reversal declaration

This diagnostic asks why the locked v1 experiment failed. It does not redefine `SR_preC v1`, change its weights, revise its primary outcome, or reopen the decision. The following conclusions remain fixed:

- `SR_preC v1`: **NO-GO**;
- diagonal empirical Fisher: **lose**;
- four-state classification: **unstable**;
- the v1 Fashion-MNIST experiment did not support its proposed operationalization.

All analyses below are exploratory post-failure analyses of the complete 40-run locked cohort. Their role is to design a better identification test, not to rescue v1.

## 1. Data and diagnostic method

The diagnostic merged the frozen v1 files `preC_features.parquet`, `C_outcomes.parquet`, and the B rows of `phase_summary.csv`. The target remained the locked

\[
Q_C=\frac{1}{8}\sum_{e=1}^{8}
\left[\operatorname{BA}_{C,\mathrm{changed}}(C_e)
-\operatorname{BA}_{C,\mathrm{changed}}(C_0)\right].
\]

Model comparisons used the same 10 seed identifiers and four condition labels as v1. Reported prediction scores include fixed five-fold row-level CV, leave-one-condition-out CV, leave-one-seed-out CV, and separate leave-one-seed-out fits inside each condition. The latter are diagnostic only; with 10 rows per condition, negative CV scores are expected when the within-condition signal is weak.

Reproducible tables and the merged diagnostic frame are stored under `Experiments/selective_resynchronization_matched_paths/outputs/diagnostic/`.

## 2. Where did the high M0 prediction come from?

The decomposed models were:

1. `condition_only`: condition indicators;
2. `B_accuracy_loss_only`: B-end validation balanced accuracy and loss;
3. `B_internal_state_only`: B-end predictive entropy, representation coherence, gradient disagreement, probe-gradient norm, parameter distance, and representation drift;
4. `condition_plus_B_accuracy_loss`;
5. `condition_plus_complete_B_state`;
6. `complete_locked_M0`: condition, B accuracy/loss, and A-end validation accuracy.

| Model | Ordinary CV R2 | Leave-condition-out R2 | Leave-seed-out R2 | Within-condition pooled R2* |
|---|---:|---:|---:|---:|
| condition only | 0.4279 | -0.3634 | 0.4933 | 0.4933 |
| B accuracy/loss only | 0.9304 | 0.3585 | **0.9323** | 0.9310 |
| B internal state only | 0.9082 | -12.6730 | 0.9128 | -1658.1560 |
| condition + B accuracy/loss | 0.9370 | 0.5725 | 0.9352 | 0.9310 |
| condition + complete B state | 0.5164 | -0.0279 | 0.8996 | unstable |
| complete locked M0 | 0.9317 | 0.5870 | **0.9311** | 0.9057 |

`*` The pooled value combines four separately fitted within-condition models and therefore retains condition-specific intercept information. It is not evidence of a common within-condition law. Per-condition results below are the relevant check.

### 2.1 Main attribution

The high M0 score came primarily from B-end accuracy and loss, not from the condition label:

- B accuracy/loss alone reproduced the M0 leave-seed-out score (`0.9323` versus `0.9311`);
- adding condition to B accuracy/loss increased leave-seed-out R2 by only `0.0029`;
- adding A-end accuracy did not improve prediction;
- condition alone predicted materially less (`0.4933`) and failed to generalize to an unseen condition (`-0.3634`).

Removing condition therefore did not remove the main v1 prediction. The correct statement is not “condition labels explain M0.” It is: **the v1 outcome was almost completely ordered by unmatched B endpoint performance, with condition labels adding little once B accuracy and loss were known.**

### 2.2 Generalization and instability

B accuracy/loss retained moderate leave-condition-out prediction (`0.3585`), so the relation was not exclusively a lookup table over the four labels. However, within-condition prediction was inconsistent:

| Condition | B accuracy/loss within-condition CV R2 | Complete M0 within-condition CV R2 |
|---|---:|---:|
| constrained | -0.8274 | -0.7075 |
| standard | -0.7240 | -1.0472 |
| high update | 0.8597 | 0.7967 |
| replay | 0.0899 | -0.0340 |

Most apparent within-condition predictive power came from the unstable high-update cell. The other three conditions supplied little or negative out-of-sample prediction. B internal-state variables had a high leave-seed-out score but catastrophic leave-condition and within-condition performance, indicating condition signatures, collinearity, and extrapolation failure rather than a stable endpoint law.

## 3. Mathematical and procedural coupling

### 3.1 Outcome formula

`Q_C` did not contain B accuracy or B loss as explicit terms. It did explicitly subtract C-start performance:

\[
Q_C=\overline{\operatorname{BA}}_{C1:C8}-\operatorname{BA}_{C0}.
\]

Because `C0` was the B checkpoint evaluated after a fixed partial label permutation, it was mechanically related to the B model's predictions. This created a headroom component:

- Pearson correlation `C0 changed-class accuracy` with `Q_C`: `-0.3781`;
- Pearson correlation `1-C0` with `Q_C`: `0.3781`;
- Spearman headroom correlation: `0.5535`.

This coupling was real but not sufficient to explain M0's `0.9311`: the mean post-update C accuracy, reconstructed as `Q_C + C0`, correlated `0.9706` with `Q_C`.

### 3.2 Inherited C intervention

The larger identification problem was procedural. v1 reused each B condition's optimizer settings during C:

- constrained models entered C with low learning rate and strong weight decay;
- high-update models retained the high learning rate;
- replay models continued replay during C;
- standard models used the standard C optimizer.

Thus `condition` encoded both the B learning history and the future adaptation algorithm. A condition effect on `Q_C` could not be attributed to path history alone.

### 3.3 Budgets

All B cells had the same nominal `3,910` update batches, so varying B epoch count was not the source of M0 prediction. Replay nevertheless changed the effective example composition within those batches. C had a common epoch count but not a common optimizer or effective replay composition.

### 3.4 Consequence for Stage 4

The next experiment must use one identical future optimizer, data order, and budget for every B path. It must also report both baseline-adjusted adaptation gain and the unadjusted future learning curve so that C0 headroom cannot silently carry the conclusion.

## 4. Within- and between-condition variance

| Variable | Between-condition SS fraction | Between/within SS | Variance-of-means / mean-within-variance |
|---|---:|---:|---:|
| `SR_preC` | 0.6202 | 1.6327 | 1.9592 |
| `Q_C` | 0.5895 | 1.4363 | 1.7236 |
| B accuracy | 0.5600 | 1.2727 | 1.5272 |
| B loss | 0.5642 | 1.2944 | 1.5533 |

Most of the variation in the score, outcome, and B performance lay between conditions rather than inside the stable conditions. The high-update cell dominated the remaining within-condition variance:

| Condition | Var(`SR_preC`) | Var(`Q_C`) | Var(B accuracy) | Var(B loss) | Corr(`SR_preC`,`Q_C`) |
|---|---:|---:|---:|---:|---:|
| constrained | 0.0935 | 0.00128 | 0.000184 | 0.000713 | -0.1305 |
| standard | 0.1115 | 0.000365 | 0.000143 | 0.000812 | -0.2628 |
| high update | 13.9303 | 0.10305 | 0.129601 | 0.811725 | 0.9357 |
| replay | 0.0416 | 0.000223 | 0.000146 | 0.001072 | -0.2012 |

The v1 comparison was therefore mostly

\[
\text{different condition}
\rightarrow
\text{different B endpoint}
\rightarrow
\text{different C adaptation},
\]

not a test of equal endpoints reached through different histories. The failure of the v1 propensity matching to produce even one pair is consistent with this lack of common support.

## 5. Source of the negative v1 coefficient

The exploratory component audit found strong raw condition-structured correlations:

| Candidate | Raw Pearson with `Q_C` | Within-condition-centered Pearson | Incremental beta after locked M0 | HC3 interval |
|---|---:|---:|---:|---|
| opening dimension | -0.9415 | -0.9186 | -0.0367 | [-0.3340, 0.2606] |
| stabilization dimension | 0.8199 | 0.9360 | -0.1907 | [-1.0015, 0.6201] |
| adaptation dimension | 0.9262 | 0.9308 | -0.4248 | [-1.4255, 0.5759] |
| non-rollback dimension | -0.9693 | -0.9358 | -0.0359 | [-0.4796, 0.4078] |
| incorporation dimension | -0.7143 | -0.6641 | -0.0453 | [-0.1416, 0.0509] |
| representation-drift area | -0.9567 | -0.9369 | -0.0094 | [-0.4621, 0.4433] |
| gradient-disagreement peak | -0.8509 | -0.8251 | -0.0295 | [-0.1598, 0.1008] |
| late representation velocity | -0.8256 | -0.9377 | 0.1434 | [-0.5938, 0.8805] |
| late B-loss slope | -0.1954 | 0.0044 | 0.0037 | [-0.0355, 0.0429] |
| Fisher burden area | 0.1477 | 0.7823 | -0.0226 | [-0.4002, 0.3550] |

None of the component or process measures had an incremental HC3 interval excluding zero after the locked M0 controls. The negative v1 coefficient therefore cannot be assigned to one stable mechanism.

Two condition signatures were especially influential:

- constrained adaptation produced a high mean score (`2.30`) largely because its standardized non-rollback term was extreme (`10.89`), while mean `Q_C` was only `0.30`;
- high-update adaptation produced a very negative mean score (`-4.05`) because its stabilization term was extreme (`-39.75`), with highly variable and low mean `Q_C` (`0.18`).

Standard and replay paths had similar B endpoints and high `Q_C`, but their `SR_preC` means were near zero. This mixture made the equal-weight score sensitive to condition-specific scaling and to endpoint failure. Fisher did not explain the residual result; its incremental coefficient was near zero and highly uncertain.

This is negative evidence about the v1 score. It is not a basis for selecting new weights or constructing `SR_preC v2`.

## 6. Failure diagnosis and next-test implication

The v1 failure was not mainly caused by condition labels statistically replacing a real path signal. Its high base-model prediction came from unmatched B accuracy/loss, and the future optimizer remained condition-specific. The design therefore lacked the counterfactual contrast required to estimate a history effect.

The justified Stage-4 question is narrower:

> If B accuracy, loss, and calibration are brought into common support, and every future branch uses the same optimizer and data order, does B path identity still predict adaptation across several future tasks?

Possible outcomes remain symmetric:

- a stable matched-group effect would show that v1's design was inadequate for identifying path dependence, without rehabilitating `SR_preC v1`;
- a near-zero or task-specific effect would further weaken the independent-path hypothesis;
- failure to form matched groups would establish that the chosen interventions do not support the desired counterfactual comparison.

## 7. Proxy boundary

Path labels are interventions, not dynamical states. Representation drift, effective rank, dead-unit ratio, gradient measures, and Fisher burden are operational proxies or weak correlates. None defines retained adaptability, selective resynchronization, `Psi_f`, or an ontological selection process. This diagnostic is a domain-level machine-learning identification analysis only.
