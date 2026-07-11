---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-PREREGISTERED-ANALYSIS-20260710
type: preregistered_analysis_plan
status: draft_v0_1
layer: paper_working
epistemic_layer: bridge
claim_mode: preregistration_plan
claim_level: P4
canonical: false
created: 2026-07-10
depends_on:
  - PAPER-SELECTIVE-RESYNCHRONIZATION-CONSTRUCT-HARDENING-20260710
  - PAPER-SELECTIVE-RESYNCHRONIZATION-TWO-SHIFT-PROTOCOL-20260710
---

# Preregistered Analysis Plan

## 0. Status and scope

This document is a **Stage-1-style / registered-report-style analysis plan** for a proposed study. It is not a formal journal Registered Report and contains no results.

The primary scientific target is construct validity. Fisher-geometric burden is a secondary candidate predictor. All thresholds, windows, model formulas, seed counts, and smallest effects of interest must be frozen after calibration and before confirmatory outcomes are inspected.

## 1. Experimental unit, indexing, and analysis populations

### 1.1 Experimental unit

The experimental unit is one complete seeded `A -> B -> C` training trajectory under a fixed dataset, architecture, optimizer, and adaptation condition. Checkpoints and mini-batches are repeated measurements, not independent replicates.

### 1.2 Seed pairing

The same confirmatory seed identifiers are reused across compatible conditions for initialization, data order, and shift generation. Analyses include seed as a random intercept or use paired seed-level contrasts. Epochs/checkpoints are never treated as independent samples for the main outcome.

### 1.3 Analysis populations

| Population | Definition | Use |
|---|---|---|
| calibration | disjoint pilot seeds used to set windows, thresholds, matching bands, and estimator settings | no confirmatory p-values |
| full confirmatory cohort | every launched confirmatory seed-condition run, including scientific failures | state frequencies, failure rates, intention-to-measure sensitivities |
| matched-`B` cohort | confirmatory runs entering the frozen common-support band | primary retained-adaptability analysis |
| valid-measure cohort | runs with complete preregistered pre-`C` metric block | metric model comparison; missingness reported |

The matched cohort is not silently generalized to regimes outside common support.

## 2. Primary outcome

The primary outcome is early adaptation of the four changed classes under `C`, measured after matching current `B` performance:

\[
Q_C^{\mathrm{AULC}}
=
\frac{1}{K_C}
\sum_{k=1}^{K_C}
\left[
\operatorname{BA}_{C,\mathrm{changed}}(k)
-
\operatorname{BA}_{C,\mathrm{changed}}(0)
\right].
\]

Definitions:

- `BA_C,changed(k)`: balanced accuracy on the four remapped classes after `k` prespecified `C` checkpoints;
- `BA_C,changed(0)`: balanced accuracy immediately before any `C` update;
- `K_C`: fixed early-adaptation horizon selected before confirmatory runs.

Subtracting the initial `C` score measures learning gain rather than rewarding a favorable zero-shot mapping. Absolute curves are also reported.

## 3. Secondary outcomes

1. all-class `Q_C^AULC`;
2. unchanged-class performance change during `C`;
3. updates/samples to a frozen `C` performance threshold;
4. final `C` balanced accuracy and NLL at fixed budget;
5. `A` and `B` forgetting after `C`;
6. held-out `B` robustness after adaptation;
7. calibration error / Brier score;
8. optional return-to-`B` relearning speed;
9. state-classification frequencies;
10. BOCPD/CUSUM detection delay and false-alarm rate;
11. wall-clock, examples, and FLOPs estimates as realized-cost descriptors.

No secondary outcome replaces the primary outcome after data inspection.

## 4. Confirmatory hypotheses

### H-P: primary construct-validity hypothesis

At matched current `B` performance, the prespecified pre-`C` selective-resynchronization feature block (`SR_preC`) improves prediction of `Q_C^AULC` beyond endpoint performance, training history, and standard optimization/representation controls.

The `SR_preC` block contains only pre-`C` variables:

- early gradient-disagreement peak and decay;
- early representation displacement;
- early-to-stable change-subspace overlap `S_B`;
- late-`B` representation velocity / stability;
- held-out `B` robustness.

The block is frozen before `C` outcomes and is tested jointly. No outcome-trained composite is used.

Prespecified directions are: greater `S_B` and held-out `B` robustness predict higher `Q_C`; lower late-`B` representation velocity predicts higher `Q_C`; and greater open-to-stable disagreement decay predicts higher `Q_C` after conditioning on the opening peak. The raw opening peak has no monotonic directional prediction and is tested jointly with decay (and, secondarily, a frozen quadratic term), because both insufficient opening and uncontrolled opening are plausible failures.

**Support rule:** the block must pass both the inferential and held-out predictive criteria in §10. A favorable state-label plot alone is insufficient.

### H-S1: current performance and future adaptability dissociate

After matching/adjusting `B` balanced accuracy and NLL, condition-level and run-level variation remains in `Q_C^AULC` and is not explained solely by updates-to-match, compute, or optimizer state.

This hypothesis fails if residual `Q_C` variation is negligible or ordinary current-performance/training controls account for it.

### H-S2: temporal organization

Successful trajectories more often show the preregistered ordering:

\[
A\text{-stability}
\rightarrow
D\text{-opening}
\rightarrow
\text{selective incorporation}
\rightarrow
B\text{-restabilization}
\rightarrow
Q_C>q_0,
\]

than rigidity, matched-noise, rollback, or collapse controls. A Fisher peak is tested as an optional intermediate event, not a required element.

### H-S3: intermediate-burden regime

The relationship between cumulative Fisher burden during `B` and `Q_C` may be non-monotonic. The confirmatory version fits standardized linear and quadratic terms and predicts a negative quadratic coefficient with the estimated maximum inside the central `80%` of observed burden support.

The same test is repeated for update norm and output KL. A Fisher-specific interpretation is permitted only if Fisher provides better held-out prediction and the pattern survives these controls.

### H-S4: limited incremental value of Fisher

Fisher summaries may add prediction beyond standard controls, but Fisher alone is not expected to determine success. The decisive comparisons are `M_F` versus `M_0` and `M_FD` versus `M_D`.

Fisher can win, tie, lose, or remain inconclusive under the frozen rules in §11.

## 5. Exploratory questions

The following are exploratory unless promoted before confirmatory data collection:

- which layer carries the strongest predictive representation signal;
- empirical-Fisher versus model-sampled-Fisher differences beyond the primary sensitivity subset;
- optimizer-reset versus optimizer-state-preserving mediation;
- reverse shift order;
- alternative `C` class-prior shift;
- learned composite state score;
- natural-gradient/Fisher-preconditioned and SAM extensions;
- nonlinear interactions among Fisher burden, disagreement, and architecture;
- change-point localization on individual layers;
- mediation from `D` through restabilization to `Q_C`.

Exploratory findings are labeled as hypothesis-generating and are not used to declare the construct retained.

## 6. Prespecified feature construction

### 6.1 Temporal summaries

For each metric `X_t` in `W_B^open` and `W_B^stable`, compute only the frozen summaries relevant to its role:

- baseline-normalized peak;
- trapezoidal area above `W_A` baseline;
- time-to-peak;
- stable-window mean;
- decay ratio from open peak to stable window.

Normalization constants come from calibration/no-shift runs. If the baseline standard deviation is nearly zero, use a frozen robust scale (median absolute deviation with a prespecified floor) and record the substitution.

### 6.2 Compact baseline feature set

To avoid unregistered feature fishing, `M_0` uses one prespecified summary per mandatory baseline family:

1. `A` balanced accuracy;
2. matched `B` balanced accuracy;
3. matched `B` NLL;
4. updates-to-match;
5. `B` loss-change area;
6. gradient-norm area;
7. parameter distance from the `A` checkpoint;
8. output-KL area on the fixed probe;
9. predictive-entropy change area;
10. representation-drift area;
11. Hessian-trace or sharpness summary, with one designated primary curvature baseline.

Dataset, architecture, optimizer, adaptation condition, and shift version enter as design factors where applicable. Continuous predictors are standardized using calibration means/scales or training-fold statistics within cross-validation, never the held-out fold.

### 6.3 Fisher feature block

The primary Fisher block contains:

- open-window `G_t` area;
- peak `G_t`;
- open-to-stable `G_t` decay ratio.

Accumulated path burden and model-sampled-Fisher analogues are sensitivity features, not extra degrees of freedom in the primary test.

### 6.4 Desynchronization/process block

The primary `D/process` block contains:

- gradient-disagreement peak;
- gradient-disagreement decay ratio;
- representation-displacement peak;
- selective-incorporation overlap `S_B`;
- late-`B` representation velocity;
- held-out `B` robustness.

Raw representation-drift area remains in `M_0`; the added block tests temporal organization and selective retention beyond drift magnitude.

## 7. Nested model families

Let `Y = Q_C^AULC` for the changed classes. The core linear mixed-model form is:

\[
Y_{i}
=
X_i\beta
+
u_{\mathrm{seed}(i)}
+
\epsilon_i,
\]

where `u_seed` is a random intercept for paired seed identifiers. If the random-effect fit is singular, the preregistered fallback is a fixed-effect model with seed-clustered robust standard errors and paired-seed bootstrap for predictive intervals.

### 7.1 Core models

| Model | Predictors | Question |
|---|---|---|
| `M_0` | compact baseline set + design factors | how well do ordinary controls predict `Q_C`? |
| `M_F` | `M_0` + Fisher block | does Fisher add information beyond ordinary controls? |
| `M_D` | `M_0` + desynchronization/process block | does the proposed pre-`C` process add information? |
| `M_FD` | `M_0` + Fisher block + desynchronization/process block | do Fisher and process information add complementary value? |
| `M_T` | `M_FD` + frozen temporal-order features | does explicit event ordering improve prediction beyond aggregate summaries? |

`M_D` versus `M_0` is the primary construct comparison. `M_F` versus `M_0` and `M_FD` versus `M_D` are the primary Fisher comparisons. `M_T` is secondary because timing features are more estimator-sensitive.

### 7.2 Temporal-order features for `M_T`

- lag from perturbation to `D` peak;
- lag from `D` peak to the start of stable `B` window;
- Fisher-peak lag, if a Fisher peak crosses the frozen detection rule;
- whether BOCPD/CUSUM detected change before restabilization;
- duration of the open state.

Absent events are coded by a prespecified censored/indicator scheme, not assigned favorable arbitrary times.

### 7.3 Non-monotonic model

For H-S3, fit:

\[
Y_i
=
M_{0,i}
+
\beta_1\widetilde{\mathcal G}_{B,i}
+
\beta_2\widetilde{\mathcal G}_{B,i}^{2}
+
u_{\mathrm{seed}(i)}
+
\epsilon_i.
\]

Required evidence for an intermediate regime:

1. `beta_2 < 0` with corrected `p < .05` and a 95% confidence interval excluding zero;
2. the implied maximum lies inside the central `80%` of support;
3. leave-one-seed-out prediction improves by the frozen smallest effect of interest;
4. no single adaptation condition or seed drives the curve;
5. comparable quadratic models for update norm and KL do not fully account for it.

Otherwise the result is null, monotonic, or inconclusive—not a productive window.

## 8. Cross-validation and generalization checks

### 8.1 Primary predictive evaluation

Use leave-one-seed-identifier-out cross-validation. All paired runs carrying the held-out seed ID are excluded together. Feature standardization, imputation permitted by §13, and any regularization are fit inside the training fold.

Report:

- cross-validated `R^2`;
- root-mean-square error normalized by the training-fold outcome standard deviation (`NRMSE`);
- mean absolute error;
- seed-bootstrap 95% confidence intervals for differences between nested models.

### 8.2 Generalization sensitivities

- leave-one-adaptation-condition-out;
- leave-one-architecture-out in the CIFAR study;
- leave-one-optimizer-out in the CIFAR study;
- shift-order sensitivity, reported separately if only a subset is available;
- Fashion-to-CIFAR sign and rank consistency without pooling incompatible scales.

These analyses distinguish interpolation across seeds from broader transfer across mechanisms.

## 9. Smallest effects of interest and power

### 9.1 Predictive smallest effect of interest

The initial proposed smallest effect of interest is:

- at least a `5%` relative reduction in held-out NRMSE, and
- at least `Delta R^2_CV = 0.05`.

The final thresholds must be assessed by simulation using calibration-run variance and frozen before confirmatory outcomes. Any change is versioned as a preregistration amendment made without access to confirmatory results.

### 9.2 Inferential smallest effect

For individual standardized coefficients, report effects in outcome standard-deviation units. The smallest practically meaningful coefficient is initially `|beta_std| = 0.10`; the calibration-based power simulation may revise it before registration.

### 9.3 Seed counts

- Fashion-MNIST MVP: `10` confirmatory paired seeds per condition;
- CIFAR-10 main study: `12` confirmatory paired seeds per factorial cell;
- calibration: `3` disjoint seeds per condition;
- no-shift controls: at least `5` seeds per required regime.

The MVP is a construct gate and may be underpowered for small effects. The main-study seed count must be justified by simulation. If planned power is inadequate, increase seeds before confirmatory results are inspected or downgrade the hypothesis; do not collect until significance.

## 10. Decision rule for the primary construct hypothesis

`H-P` is supported only when all of the following hold for `M_D` versus `M_0`:

1. the joint block likelihood-ratio or prespecified Wald test has `p < .05`;
2. the seed-bootstrap 95% confidence interval for `Delta R^2_CV` excludes zero;
3. held-out NRMSE improves by at least the frozen smallest effect of interest;
4. selective-incorporation and restabilization features have directions compatible with the preregistered interpretation;
5. the result survives the primary estimator/probe robustness checks;
6. no common-support or missingness failure invalidates the matched analysis.

If only some criteria hold, the result is **inconclusive**, not supportive. If `M_D` adds no material prediction and ordinary controls suffice, the construct meets a kill condition.

## 11. Fisher win, tie, lose, and inconclusive rules

Fisher status is assessed primarily by `M_FD` versus `M_D`, and secondarily by `M_F` versus `M_0`.

### Fisher win

Declare a Fisher win only if:

1. the Fisher block passes the Holm-adjusted inferential test;
2. seed-bootstrap 95% confidence intervals for `Delta R^2_CV` and NRMSE improvement exclude zero;
3. improvement reaches the frozen smallest effect of interest;
4. the sign/rank conclusion is stable across empirical and model-sampled Fisher sensitivity estimates;
5. Fisher is not rendered redundant by output KL, update norm, Hessian/sharpness, or representation features.

Interpretation: Fisher burden has incremental predictive value in this domain and protocol. It does not define the construct or `Psi_f`.

### Fisher tie

Declare a practical tie only if the confidence interval lies entirely inside a frozen equivalence band, initially:

- absolute `Delta R^2_CV < 0.01`, and
- relative NRMSE difference within `plus/minus 2%`.

Interpretation: Fisher provides no practically special advantage over the comparator at the available resolution.

### Fisher lose

Declare a Fisher loss if:

- the upper confidence bound for predictive improvement is below zero, or
- the comparator improves NRMSE by at least the smallest effect of interest while Fisher does not, or
- Fisher conclusions reverse under required estimator/probe checks and simpler measures remain stable.

Interpretation: weaken or reject the Fisher bridge for this regime. The result does not refute the operational framework if `M_D` succeeds.

### Inconclusive

Use “inconclusive” when intervals span both meaningful benefit and meaningful harm, common support is inadequate, or metric reliability is insufficient. Absence of significance alone is not equivalence.

## 12. Multiple comparisons

- one primary hypothesis (`H-P`): two-sided `alpha = .05`, no multiplicity adjustment;
- Fisher family: Holm correction across the two primary nested comparisons and designated Fisher outcomes;
- temporal/non-monotonic family: Holm correction within H-S2/H-S3 tests;
- secondary outcome family: Holm correction across the prespecified outcome contrasts;
- exploratory analyses: Benjamini-Hochberg false-discovery-rate control where a family is coherent, otherwise exact p-values labeled exploratory.

All tested models and family membership are reported, including null results.

## 13. Missing data, failed runs, and exclusions

### 13.1 Technical failures

Examples: filesystem failure, preemption without checkpoint, corrupted download, logging bug, or verified hardware error.

- rerun the same seed and exact configuration once;
- if the same technical issue recurs, repair the pipeline before resuming the cell;
- use the next prespecified reserve seed only when the original seed cannot be recovered, and retain the audit trail;
- technical failures are excluded from scientific state counts.

### 13.2 Scientific failures

Examples: divergence, NaNs produced by the preregistered hyperparameters, failure to adapt, or inability to reach the `B` matching band for a substantive reason.

- do not rerun with friendlier hyperparameters;
- retain in the full-cohort failure/state analysis;
- do not include in the matched cohort if the frozen matching rule is not met;
- for a post-match numerical failure during `C`, impute chance-level balanced accuracy for missing future checkpoints in the primary conservative sensitivity analysis and report complete-case and last-valid-observation analyses separately.

### 13.3 Missing metric values

- no outcome-informed imputation;
- if one metric checkpoint is missing between valid neighbors, preregistered linear interpolation may be used only for temporal area summaries, with a missingness flag;
- if more than `10%` of required checkpoints for a feature are missing, that feature is missing for the run;
- models use complete cases for the required block plus a multiple-imputation sensitivity only when missing-at-random is plausible.

### 13.4 Cell-level validity rule

If more than `10%` of a confirmatory cell is lost to technical failure, pause analysis and rerun the entire affected cell after a versioned correction. If more than `30%` fails scientifically or common support falls below `70%`, the matched primary claim for that cell is not identified and is downgraded rather than rescued post hoc.

### 13.5 Prohibited exclusions

Do not exclude runs because they:

- weaken the preferred hypothesis;
- show low or high Fisher burden;
- fall outside a visually appealing state trajectory;
- are statistical outliers without a preregistered technical/data-integrity reason;
- make a model residual non-normal when robust inference remains possible.

## 14. Thresholds and state classification

Primary inference uses continuous variables. Secondary state labels use only frozen rules:

- opening: `95th` percentile of matched no-shift calibration distribution;
- sensitivity opening thresholds: `90th` and `97.5th` percentiles;
- stability: calibration-based maximum slope/variance sustained for a fixed window;
- selective incorporation: temporal-permutation/no-shift threshold;
- `B` adequacy and matching: calibration-defined common-support band;
- `Q_C` adequacy: frozen non-inferiority or reference floor.

No threshold is estimated from confirmatory `Q_C`, state counts, Fisher rankings, or desired effect significance. State-label conclusions must be consistent across the prespecified sensitivity thresholds or be labeled threshold-dependent.

## 15. Effect sizes and uncertainty

Report, as applicable:

- standardized coefficients with 95% confidence intervals;
- joint-block partial `R^2`;
- `Delta R^2_CV`, `Delta NRMSE`, and `Delta MAE` with paired seed-bootstrap 95% intervals;
- mean or median paired differences in `Q_C`;
- time-to-threshold ratio with bootstrap interval;
- risk difference / odds ratio for state or failure classification;
- rank correlation between metric summaries and outcomes;
- reliability estimates for probe resampling and seed stability.

Do not report p-values without effect sizes and uncertainty. Do not treat a large sample or many checkpoints as extra independent evidence.

## 16. Robustness and sensitivity analyses

Required:

1. empirical versus model-sampled Fisher subset;
2. probe sizes `128/256/512` where feasible;
3. gradient and representation `D` measures separately;
4. layerwise representation sensitivity;
5. output KL, update norm, Hessian/sharpness as direct Fisher competitors;
6. optimizer state preserved versus reset at `C`;
7. fixed-budget versus matched-performance analysis;
8. alternative matching caliper fixed before outcomes;
9. no-shift, matched-noise, rollback, and state-anchor conditions;
10. leave-one-seed, condition, architecture, and optimizer checks as applicable;
11. state thresholds at prespecified alternative percentiles;
12. scientific-failure treatment sensitivity.

Optional sensitivity analyses are clearly separated from required ones.

## 17. Null-result interpretations

| Result pattern | Required interpretation |
|---|---|
| `M_D` beats `M_0`; Fisher wins | operational construct gains support; Fisher is incrementally useful in this regime only |
| `M_D` beats `M_0`; Fisher ties/loses | retain construct provisionally; weaken or reject Fisher bridge |
| `M_D` ties `M_0`; Fisher wins | Fisher predicts later adaptation, but “selective resynchronization” has not gained construct validity |
| neither block improves prediction | current framework adds no predictive value; retain two-shift dataset/protocol only if independently useful |
| current `B` performance fully explains `Q_C` | current/future dissociation fails; construct kill condition |
| `Q_C` varies but standard retained-plasticity metrics explain it | study contributes a retained-plasticity result; drop or narrow the new term |
| state labels unstable but continuous effects exist | remove categorical taxonomy claims; report continuous dynamics only |
| Fisher collapses to KL/update norm | report projection redundancy; no special Fisher interpretation |
| one dataset/shift supports, another fails | claim task/shift specificity; no general process claim |
| all intervals are wide | inconclusive; do not convert uncertainty into a negative or positive claim |

## 18. Stopping rules

1. Use fixed preregistered seed counts; no significance-based early stopping.
2. Stop a run only for prespecified safety/numerical criteria such as non-finite loss, memory failure, or fixed maximum budget.
3. Pause the experiment for a verified systemic software/data bug; version the correction and rerun every affected cell.
4. Stop scale-up to CIFAR if the MVP meets a construct kill criterion, lacks matching common support, or yields unreliable core measures.
5. Stop Fisher expansion if metric overhead prevents the prespecified seed count or estimator reliability is inadequate.
6. Do not stop because Fisher loses; that is an allowed outcome.

## 19. Preregistration deviation log

Every deviation must record:

- timestamp and code commit;
- rule changed;
- reason;
- whether confirmatory outcomes had been inspected;
- affected runs/cells;
- whether the analysis is still confirmatory, downgraded to exploratory, or rerun from scratch.

Outcome-aware changes automatically become exploratory unless an independent untouched confirmatory dataset is collected.

## 20. Analysis gate

The analysis plan supports a **CONDITIONAL GO** only. Before confirmatory execution it still requires:

- calibration-based final constants for windows, thresholds, and common-support matching;
- simulation-based power verification;
- validated implementations of every primary metric;
- a frozen statistical script tested on synthetic/null data;
- a public or immutable preregistration snapshot.

No empirical claim is authorized until those items and the experiments are complete.
