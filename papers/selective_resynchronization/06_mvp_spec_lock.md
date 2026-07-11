---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-MVP-SPEC-LOCK-20260710
type: preregistration_lock
status: locked_before_confirmatory_v1_1
layer: paper_working
epistemic_layer: bridge
claim_mode: preregistration
claim_level: P4
canonical: false
created: 2026-07-10
last_updated: 2026-07-11
locked_before_confirmatory_results: true
formal_results_seen_at_lock: false
depends_on:
  - PAPER-SELECTIVE-RESYNCHRONIZATION-CONSTRUCT-HARDENING-20260710
  - PAPER-SELECTIVE-RESYNCHRONIZATION-TWO-SHIFT-PROTOCOL-20260710
  - PAPER-SELECTIVE-RESYNCHRONIZATION-PREREGISTERED-ANALYSIS-20260710
---

# Fashion-MNIST MVP Specification Lock

## 0. Lock declaration

This file fixes the confirmatory Fashion-MNIST MVP before any locked-MVP `C` outcome is generated or inspected. Smoke-test outcomes are used only to validate software. Pilot standardization constants and state thresholds may use **A/B-only** pilot or no-shift calibration artifacts under the algorithms fixed below. No pilot or confirmatory `C` outcome may alter `SR_preC`, its weights, its components, the primary `Q_C`, or the model-comparison rules.

The specification is domain-level and empirical. No metric below is a direct measure of SRT, `Psi_f`, ontology, consciousness, or subjecthood.

### 0.1 Pre-formal implementation clarification (2026-07-11)

Before creation of the formal manifest and without inspecting or comparing pilot `Q_C` values, the executable audit rules were made explicit in four places: paired seed-bootstrap intervals are stored for cross-validated model differences; leave-one-component-out directional consistency requires at least four of five alternative-score coefficients to be positive with a positive median; state-label stability uses held-out-seed agreement with the condition-modal label learned from the other seeds; and Fisher status uses the exact interval and KL sanity rules stated in Section 14. These clarifications add missing implementation detail but do not change `SR_preC`, `Q_C`, shifts, conditions, windows, weights, seeds, effect thresholds, or construct decision thresholds. This amended file is the version hashed by the formal manifest.

## 1. Conflicts and conservative resolutions

| Conflict / unresolved option | Locked resolution | Reason |
|---|---|---|
| Stage-2 files proposed a multivariable `SR_preC` feature block, while Stage 3 requires one primary predictor | lock one equal-weight composite as primary; retain the unweighted components and feature-block model as secondary | reduces researcher degrees of freedom without discarding diagnostic information |
| `03_two_shift_protocol.md` allocated 10,000 training-set examples jointly to calibration/validation and probe use; Stage 3 requires separate validation and probe sets | split official training data into 50,000 train, 8,000 validation, and 2,000 probe examples | stricter information separation |
| Stage 2 proposed performance-matched `B` checkpoints as a primary route; Stage 3 prioritizes regression control and matching as secondary | all locked runs enter `C` after fixed `B` epoch 10; primary analysis controls `B` endpoint performance; a frozen matched analysis is secondary | avoids outcome-adjacent checkpoint selection and keeps exposure budgets equal |
| Stage 2 allowed several Fisher estimators | lock a diagonal empirical-Fisher quadratic on a fixed 20-example stratified probe; model-sampled Fisher is exploratory | executable on ordinary compute and auditable; no full Fisher matrix |
| “productive desynchronization” could be interpreted retrospectively | real-time state name is `desynchronization-open`; productivity is never assigned before later evidence | prevents outcome information from entering a pre-`C` state |

No SRT canonical, Core, ChoiceMap, or theory file is modified by this lock.

## 2. Unique primary question

> **Does an A/B-only measure of selective resynchronization predict adaptation to a mechanistically distinct second shift after controlling or matching for current B-stage performance?**

The primary estimand is the incremental prediction of a continuous `SR_preC` score after regression control for current `B` performance. Matching is secondary.

## 3. Locked environment sequence

### 3.1 Data partitions

Fashion-MNIST is split once with `split_seed = 20260710`, stratified by class:

| Partition | Size | Permitted use |
|---|---:|---|
| training | 50,000 | parameter updates only |
| validation | 8,000 | `B` controls, validation time series, software/calibration diagnostics |
| probe | 2,000 | fixed internal metrics; never parameter updates |
| official test | 10,000 | confirmatory outcome reporting; never thresholds or model selection |

The fixed metric probe contains `256` examples selected from the 2,000-example probe partition. The fixed Fisher subset contains `20` examples, two per class, selected from the metric probe. IDs and hashes are saved before formal runs.

### 3.2 Environment `A`

- original Fashion-MNIST pixels in `[0,1]`;
- original labels;
- no procedural texture;
- balanced training stream.

### 3.3 Environment `B`

- labels unchanged;
- deterministic low-frequency texture generated from a `7 x 7` random field and bilinearly upsampled to `28 x 28`;
- random-field generator version `hashed_lcg_v1`, computed in deterministic vectorized batches and cached as uint8 solely for runtime efficiency;
- texture amplitude `0.35`;
- texture applied where the original pixel value is below `0.20`;
- disjoint deterministic texture seeds: train `1101`, validation `2201`, probe `3301`, test `4401`;
- image identity partitions unchanged.

`A -> B` is a label-preserving covariate/background shift.

### 3.4 Environment `C`

- retains the same input-shift mechanism and partition-specific texture seeds as `B`;
- changes the label rule by the fixed partial permutation `0 <-> 6` and `2 <-> 4`;
- changed classes: `{0, 2, 4, 6}`;
- unchanged classes: `{1, 3, 5, 7, 8, 9}`;
- stores the zero-update `C` baseline before the first `C` optimizer step.

`B -> C` is mechanistically distinct from `A -> B`: it changes the target rule, not texture severity. Changed- and unchanged-class curves are reported separately so label-rule adaptation is not collapsed into forgetting. The output-head-local nature of this shift is an explicit limitation.

## 4. Model and training lock

### 4.1 Architecture

```text
Conv(1, 32, 3, padding=1) -> ReLU
Conv(32, 32, 3, padding=1) -> ReLU -> MaxPool(2)
Conv(32, 64, 3, padding=1) -> ReLU -> MaxPool(2)
GlobalAveragePool -> Linear(64, 10)
```

- no batch normalization;
- penultimate representation is the 64-dimensional global-average-pooled vector;
- PyTorch default initialization is used after the global seed is fixed;
- the same `A` checkpoint is branched across conditions for each seed.

### 4.2 Common schedule

- batch size: `128`;
- `A`: `15` epochs;
- `B`: `10` epochs;
- `C`: `8` epochs;
- optimizer family: SGD with momentum `0.9`;
- no learning-rate scheduler;
- validation/probe metrics at phase start and every epoch;
- official test outcomes at `A` end, `B` start/end, `C` start, and every `C` epoch;
- non-finite loss or parameters constitute a scientific failure under the locked hyperparameter condition.

### 4.3 Conditions

Condition names describe interventions, not inferred dynamical states.

| Condition | `B/C` LR | weight decay | replay | purpose only |
|---|---:|---:|---:|---|
| `constrained` | `0.003` | `0.02` | none | low-update / strong-constraint path |
| `standard` | `0.02` | `0.0001` | none | ordinary adaptation path |
| `high_update` | `0.12` | `0` | none | high-update path with instability risk |
| `replay` | `0.02` | `0.0001` | `10%` | prior-environment replay path |

All conditions use `A` learning rate `0.02` and weight decay `0.0001`. Replay uses clean `A` examples during `B` and original-rule `B` examples during `C`. No condition is called rigidity, selective resynchronization, or collapse before metric classification.

### 4.4 Seed tiers

- smoke: `{9001}` with reduced data/epochs; software interpretation only;
- pilot: `{1001,1002,1003}` for full-protocol A/B metric scaling; pilot `C` is pipeline validation only and cannot alter the lock;
- no-shift calibration: `{1101,1102,1103,1104,1105}` per condition, using `A -> A` during the nominal `B` window;
- locked MVP: `{2001,2002,2003,2004,2005,2006,2007,2008,2009,2010}` for every condition;
- reserve technical-failure seeds: `{2101,2102,2103,2104}` used only under the preregistered technical-failure rule.

## 5. Locked windows

Checkpoints are epoch-end snapshots plus each phase-start snapshot.

| Window | Locked checkpoints |
|---|---|
| `W_A` | `A13`, `A14`, `A15` |
| `W_B_open` | `B1`, `B2`, `B3` |
| `W_B_stable` | `B8`, `B9`, `B10` |
| `W_C_early` | `C1` through `C8` |

No result-dependent window shifting is allowed.

## 6. Primary predictor: `SR_preC`

### 6.1 A/B-only raw measures

All representations and gradients use the fixed probe and the `B` data rule where relevant.

1. **Representation opening**

\[
d_{\mathrm{repr,peak}}
=
\max_{e\in\{1,2,3\}}
\left[1-\operatorname{CKA}(Z_{B_e},Z_{A_{15}})\right].
\]

2. **Gradient-disagreement opening**

The 256-example probe is split into four fixed 64-example batches. For their gradients `g_b`,

\[
D^{\mathrm{grad}}_t
=
1-
\frac{2}{4(4-1)}
\sum_{b<b'}
\frac{g_b^\top g_{b'}}
{\lVert g_b\rVert\lVert g_{b'}\rVert+10^{-12}},
\]

and `d_grad,peak = max(D_grad,B1:B3)`.

3. **Gradient-disagreement decay**

\[
r_{\mathrm{grad}}
=
\frac{d_{\mathrm{grad,peak}}-overline{D}^{\mathrm{grad}}_{B8:B10}}
{|d_{\mathrm{grad,peak}}|+10^{-12}}.
\]

4. **Late representation velocity**

\[
v_{\mathrm{late}}
=
\frac{1}{2}
\sum_{e\in\{9,10\}}
\left[1-\operatorname{CKA}(Z_{B_e},Z_{B_{e-1}})\right].
\]

5. **B adaptation gain**

\[
a_B
=
\operatorname{BA}_{B,\mathrm{val}}(B10)
-
\operatorname{BA}_{B,\mathrm{val}}(B0).
\]

6. **Non-rollback displacement**

\[
n_B
=
1-\operatorname{CKA}(Z_{B10},Z_{A15}).
\]

7. **Selective-incorporation proxy**

Let `U_open` and `U_stable` be the top `k=8` right-singular-vector bases of `Z_B3-Z_A15` and `Z_B10-Z_A15`:

\[
S_B
=
\frac{1}{8}
\lVert U_{\mathrm{open}}^\top U_{\mathrm{stable}}\rVert_F^2.
\]

`S_B` is an operational proxy, not a direct measure of selection.

### 6.2 A/B-only robust standardization

For raw measure `x`,

\[
z_R(x)
=
\frac{x-\operatorname{median}_{\mathrm{pilot,AB}}(x)}
{1.4826\operatorname{MAD}_{\mathrm{pilot,AB}}(x)+10^{-6}}.
\]

The median and MAD pool the twelve pilot A/B trajectories across conditions. Constants are computed without loading any pilot `C` file, written to the locked configuration, hashed, and then reused unchanged for all formal runs. A scale below `10^-6` uses the denominator floor and is flagged; the component remains in the primary score rather than being deleted after `C`.

### 6.3 Five equal-weight dimensions

\[
O
=
\frac{1}{2}
\left[z_R(\log(1+d_{\mathrm{repr,peak}}))
+z_R(\log(1+d_{\mathrm{grad,peak}}))\right],
\]

\[
T
=
\frac{1}{2}
\left[z_R(r_{\mathrm{grad}})-z_R(v_{\mathrm{late}})\right],
\]

\[
A_B=z_R(a_B),
\qquad
N_B=z_R(n_B),
\qquad
I_B=z_R(S_B).
\]

The unique primary predictor is

\[
\boxed{
SR_{\mathrm{preC}}
=
\frac{O+T+A_B+N_B+I_B}{5}
}.
\]

Every dimension has equal weight. No C data, outcome regression, optimization, or component deletion determines the weights. Positive direction means greater opening, subsequent stabilization, B adaptation, non-rollback displacement, and retained change-subspace overlap. The raw opening peak is not by itself interpreted as beneficial; high opening can be offset by poor stabilization/adaptation dimensions.

### 6.4 Secondary predictor analyses

- the five dimensions entered separately as the Stage-2 feature block;
- each raw proxy alone;
- leave-one-component-out versions of the equal-weight score;
- representation-drift-only score;
- no Fisher quantity inside `SR_preC`.

These analyses cannot replace the primary score.

## 7. Primary outcome: retained adaptability `Q_C`

For the four changed classes and official test data, store balanced accuracy immediately before `C` updates and after each of eight `C` epochs. The unique primary outcome is

\[
\boxed{
Q_C
=
\frac{1}{8}
\sum_{e=1}^{8}
\left[
\operatorname{BA}_{C,\mathrm{changed}}(C_e)
-
\operatorname{BA}_{C,\mathrm{changed}}(C_0)
\right]
}.
\]

`Q_C` uses only C-stage data and measures average early learning gain over a fixed budget. It cannot be replaced after inspection.

Secondary outcomes:

- all-class C AULC gain;
- unchanged-class C AULC change;
- final C balanced accuracy and NLL;
- epochs to a fixed changed-class threshold of `0.60` (censored at 8);
- A/B forgetting after C;
- C-stage loss variance and non-finite failure;
- head-versus-trunk parameter update norm.

## 8. B-stage performance control

### 8.1 Primary regression control

The full locked cohort is analyzed first. Continuous predictors are standardized inside each training fold for prediction and across the full cohort for reported standardized coefficients.

Base model `M0`:

\[
Q_C
\sim
\operatorname{BA}_{B,\mathrm{val}}(B10)
+\operatorname{NLL}_{B,\mathrm{val}}(B10)
+\operatorname{BA}_{A,\mathrm{val}}(A15)
+\text{condition indicators}.
\]

`B` update count is recorded. It is omitted from the design matrix if constant by construction; any run with a shorter scientific-failure budget is retained in failure reporting and cannot enter the complete primary regression.

Incremental construct model `M1`:

\[
M1=M0+SR_{\mathrm{preC}}.
\]

Inference uses OLS with HC3 standard errors, standardized coefficients, a 2,000-resample seed-cluster bootstrap confidence interval, adjusted `R^2`, leave-one-seed-identifier-out cross-validation, and leave-one-condition-out analysis. Checkpoints are not independent observations.

### 8.2 Secondary matching analysis

The matching algorithm is frozen as follows:

1. define `high SR_preC` as the top confirmatory tertile and `low SR_preC` as the bottom tertile without reading `Q_C`; discard the middle tertile for this analysis only;
2. estimate a logistic propensity score from B-end balanced accuracy, B-end NLL, A-end balanced accuracy, and condition indicators;
3. perform greedy 1:1 nearest-neighbor matching without replacement on propensity-score logit, ordered by decreasing extremeness;
4. caliper: `0.25` pooled standard deviations of the propensity-score logit;
5. unmatched runs remain in the primary regression but are excluded from the matched contrast with reasons recorded;
6. minimum valid set: `8` matched pairs;
7. balance requirement: absolute standardized mean difference `<0.10` for continuous matching variables and `<0.20` for each condition indicator;
8. report paired mean `Q_C` difference, bootstrap interval, and exact pair count.

If fewer than eight balanced pairs remain, matching is declared inconclusive; the caliper is not widened.

## 9. Simple baselines and Fisher comparison

All predictor summaries below use only A/B data.

- `M2_repr = M0 + B representation-drift area`;
- `M2_simple = M0 +` gradient-norm area, update-norm area, parameter distance, predictive-KL area, predictive-entropy change, and representation-drift area;
- `M3 = M1 + M2_simple predictors +` empirical-Fisher burden area;
- a ridge-regularized sensitivity is used for `M2_simple/M3` if ordinary least squares is rank-deficient; regularization is selected inside cross-validation only.

Primary comparator questions:

1. Does `M1` improve over `M0`?
2. Does `M1` improve over `M2_repr`?
3. Does empirical Fisher improve prediction beyond `M1 + M2_simple`?
4. Does `M1` retain value when Fisher does not?

No baseline is removed because it outperforms the construct or Fisher.

## 10. Empirical Fisher boundary

At each epoch transition, estimate a diagonal empirical Fisher on the fixed 20-example stratified Fisher probe:

\[
\widehat F_{\mathrm{diag},t}
=
\frac{1}{20}
\sum_{i=1}^{20}
\left(\nabla_\theta\log p_\theta(y_i\mid x_i)\right)^{\odot 2},
\]

\[
G_t^{\mathrm{EF,diag}}
=
\frac{1}{2}
\sum_j
\widehat F_{jj,t}(\Delta\theta_{t,j})^2.
\]

Required implementation records:

- fixed Fisher sample IDs and count;
- empirical-label estimator name;
- non-negativity assertion with tolerance `-10^-10`;
- finite-value flag;
- same sample count at every comparable checkpoint;
- adjacent predictive KL on the 256-example probe;
- any approximation failure or skipped measurement.

`G_t` is a candidate predictor only. It is not part of `SR_preC`, not `Psi_f`, and not a complete training-cost measure.

## 11. Leakage lock

The implementation must enforce:

1. `compute_preC_features` accepts an A/B-only schema with no C field;
2. A/B training completes before any C loader is passed to the phase runner;
3. per-run `preC_features.json` and `preC_features.parquet` are written and hashed before the C phase;
4. the pre-C feature file is made read-only and never overwritten;
5. `preC_features.sha256` and creation timestamp precede the first C metric timestamp;
6. analysis verifies the stored hash before merging with C outcomes;
7. pilot robust-standardization constants are produced by an A/B-only aggregation command that refuses C columns/files;
8. test-set data cannot enter training, threshold selection, standardization, or matching-rule selection;
9. automated tests cover schema rejection, hash mutation, phase ordering, and deterministic shifts.

Any violation affecting a formal run triggers protocol-error review. If the primary cohort cannot be regenerated without leakage, the MVP decision is `NO-GO: uninterpretable protocol`.

## 12. Four-state classification: secondary only

Continuous `SR_preC -> Q_C` analysis is primary. State rules are derived before formal C outcomes from no-shift A/B calibration:

- opening thresholds: condition-specific 95th percentile of no-shift `D_repr` and `D_grad` epoch distributions;
- late-stability thresholds: condition-specific 95th percentile of no-shift late representation velocity and absolute B-loss slope;
- selective-incorporation threshold: 95th percentile of a fixed temporal-permutation null generated from no-shift/pilot A/B representations;
- B adequacy: validation balanced-accuracy gain above `0.05` and B-end balanced accuracy above `0.70`;
- no C quantity enters pre-C state assignment.

State plots are generated only if every reported class contains at least five formal runs and leave-one-seed label agreement is at least `0.70`. For the latter check, the modal state for each condition is estimated from the other nine seeds and compared with the held-out seed's state in that condition; agreement is pooled over the forty held-out assignments. Otherwise state classification is declared unstable and omitted from inferential figures.

## 13. Success, conditional, and failure rules

### 13.1 Construct GO

All are required:

1. standardized `SR_preC` coefficient in `M1` is positive and its 95% seed-cluster bootstrap interval excludes zero;
2. `M1` improves leave-one-seed-out cross-validated `R^2` over `M0` by at least `0.05` and reduces NRMSE by at least `5%`;
3. `M1` is not fully replaced by `M2_repr`: it has better CV `R^2` or NRMSE by at least one frozen smallest-effect threshold;
4. leave-one-condition-out `SR_preC` coefficients are positive in at least three of four analyses and none shows a large reversal below `-0.10` standardized units;
5. at least one of matching, leave-one-component-out, or probe-split reliability analyses is directionally consistent; the implemented leave-one-component-out rule requires at least four of five alternative-score coefficients to be positive and their median to be positive;
6. no single seed changes the full-cohort coefficient sign;
7. the median Spearman correlation between the primary score and its five leave-one-component-out variants is at least `0.70`;
8. no leakage, protocol, or cell-validity failure invalidates the cohort.

### 13.2 CONDITIONAL GO

Use this outcome when no NO-GO rule applies and at least one substantive indication remains, for example:

- the full-cohort coefficient is positive but its interval includes zero;
- predictive improvement is positive but below one frozen smallest-effect threshold;
- matching yields fewer than eight valid pairs;
- only a coherent subset of preregistered dimensions predicts `Q_C`;
- continuous prediction is directionally stable but four-state classification is unstable;
- the run is underpowered because a prespecified seed count could not be completed.

The decision must name the unresolved uncertainty and cannot be presented as support.

### 13.3 NO-GO

Trigger a construct NO-GO review if any major condition holds:

1. `SR_preC` has no stable positive increment after B controls: full-cohort coefficient is non-positive and at least two leave-one-condition/seed robustness analyses are non-positive;
2. `M1` has `Delta R^2_CV <= 0` and no NRMSE improvement over `M0`;
3. `Q_C` is almost fully predicted by B current performance, operationalized as `M0` cross-validated `R^2 >= 0.90`, with `M1` adding `Delta R^2_CV < 0.01`;
4. `M2_repr` meets or exceeds `M1` on both CV `R^2` and NRMSE, while `SR_preC` adds less than `0.01` CV `R^2` to `M2_repr`;
5. score direction repeatedly flips across reasonable locked analyses or leave-one-component-out score correlations have median below `0.50`;
6. all apparent value is confined to one condition and disappears when that condition is left out;
7. information leakage, post-C tuning, or unrecoverable protocol error makes the primary result uninterpretable;
8. the primary score requires post hoc reweighting or threshold changes to appear useful.

Fisher losing does not trigger construct NO-GO. If the construct fails but `Q_C` remains scientifically useful, the recommended reframe is retained plasticity / sequential adaptation without the selective-resynchronization term.

## 14. Fisher decision

- **win:** empirical-Fisher area adds at least `0.05` CV `R^2` and `5%` NRMSE reduction beyond `M1 + M2_simple`, its seed-cluster bootstrap coefficient interval is positive, and the A/B Fisher-area versus predictive-KL-area Spearman relation is finite and non-negative;
- **tie:** the paired seed-bootstrap interval is entirely within `plus/minus 0.01` CV `R^2` and `plus/minus 2%` relative NRMSE improvement;
- **lose:** the paired seed-bootstrap upper bounds for both CV `R^2` and relative NRMSE improvement are below zero, or the simple predictor block improves over `M1` by both frozen smallest-effect thresholds while Fisher fails either threshold;
- **inconclusive:** interval spans meaningful benefit and harm, reliability fails, or compute/measurement missingness is excessive.

Only domain-level measurement wording is allowed.

## 15. Missing runs and stopping

- technical failure: rerun the same seed/configuration once after fixing the infrastructure issue; log both attempts;
- scientific failure under locked hyperparameters: do not retune or delete; record in `failed_runs.csv` and full-cohort state/failure summaries;
- more than 10% technical loss in a cell: pause and rerun the affected cell after a versioned fix;
- more than 30% scientific failure in a cell: primary complete-case inference for that cell is not identified;
- formal stopping is the fixed 10 seeds per condition, not significance;
- if fewer than 10 formal seeds per condition are completed for resource reasons, mark the decision underpowered/inconclusive and retain the stopping reason;
- after `09_mvp_decision.md`, do not run CIFAR-10 or draft the full paper without human review.

## 16. Locked artifacts and immutability

Before formal `C` execution, save:

- this specification and SHA-256;
- `configs/mvp_locked.yaml` and SHA-256;
- pilot A/B robust-standardization constants and SHA-256;
- state-calibration thresholds and SHA-256;
- data split, probe, Fisher-probe, seed, shift, code-tree, and Git hashes;
- package/environment versions;
- a manifest timestamp confirming no locked `C` result existed at lock time.

The Git commit SHA may point to a dirty worktree; therefore the manifest also records the code-tree SHA-256. Formal results are interpretable only against both identifiers.

## 17. Pre-run claim boundary

Target claim: a P4 domain-level proxy prediction.

Allowed outcomes:

- `SR_preC` adds predictive value under this protocol;
- `SR_preC` is redundant with simpler metrics;
- the result is uncertain or condition-specific;
- Fisher wins, ties, loses, or is unmeasurable;
- the construct is retained provisionally, narrowed, or withdrawn.

Not allowed:

- SRT is proved or empirically confirmed;
- Fisher measures `Psi_f`;
- Fashion-MNIST results establish a general mechanism of mind, ontology, or reality selection;
- an association is a causal mechanism.
