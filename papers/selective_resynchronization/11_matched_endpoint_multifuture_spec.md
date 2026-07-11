---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-MATCHED-ENDPOINT-MULTIFUTURE-SPEC-20260711
type: preregistration_lock
status: locked_before_new_future_results_v1
layer: paper_working
epistemic_layer: bridge
claim_mode: preregistration
claim_level: P4
canonical: false
created: 2026-07-11
locked_before_new_future_results: true
new_future_results_seen_at_lock: false
v1_decision_changed: false
depends_on:
  - PAPER-SELECTIVE-RESYNCHRONIZATION-V1-FAILURE-DIAGNOSTIC-20260711
  - PAPER-SELECTIVE-RESYNCHRONIZATION-MVP-DECISION-20260711
---

# Matched-Endpoint, Multi-Future Diagnostic Specification

## 0. Lock declaration

This file is locked before any Stage-4 future-task outcome is generated. Stage-4 does not rescue, revise, or supersede the v1 NO-GO. It tests a new and narrower identification question:

> **When models reach closely matched performance states at the end of phase B through different adaptation paths, do those paths predict retained adaptability across multiple mechanistically distinct future shifts?**

The target is a P4 machine-learning path-dependence hypothesis. No result tests SRT ontology, consciousness, subjecthood, or `Psi_f`. No new `SR_preC` score is defined.

## 1. Diagnostic motivation

The v1 post-failure audit established four facts:

1. B-end accuracy/loss alone reproduced M0's leave-seed-out prediction (`R2=0.9323`);
2. condition labels added little after B performance was known;
3. no valid endpoint-matched pair existed;
4. each B condition's optimizer was reused during C, so path history and future adaptation algorithm were confounded.

Stage-4 therefore changes the identification design, not the v1 construct. It requires within-seed matched endpoint groups and one identical future optimizer for every B path.

## 2. Data, model, and shared A checkpoint

### 2.1 Data partitions

Use the exact v1 Fashion-MNIST split and IDs:

- 50,000 training examples;
- 8,000 validation examples;
- 2,000 probe examples;
- 10,000 official test examples;
- fixed 256-example metric probe and fixed 20-example Fisher subset.

The v1 split and probe manifests are copied into the new experiment manifest and hash-verified. Training, validation, probe, and official test roles remain separated. The official test set cannot select a B checkpoint or a matching rule.

### 2.2 Model

Use only the v1 light CNN:

```text
Conv(1,32,3,pad=1) -> ReLU
Conv(32,32,3,pad=1) -> ReLU -> MaxPool(2)
Conv(32,64,3,pad=1) -> ReLU -> MaxPool(2)
GlobalAveragePool -> Linear(64,10)
```

No ViT, recurrent model, state-space model, or alternative architecture is permitted.

### 2.3 A training

- A environment: clean Fashion-MNIST with original labels;
- 15 epochs, batch size 128;
- SGD, learning rate `0.02`, momentum `0.9`, weight decay `0.0001`;
- one A checkpoint per seed;
- the checkpoint file hash and state-dict tensor hash are recorded;
- all four B paths for a seed must load the exact same A tensor hash.

Feasibility seeds are `3001` through `3005`. Locked diagnostic seeds are `4001` through `4010`. Feasibility seeds cannot enter the confirmatory matched-group analysis.

## 3. B environment and path interventions

The B environment is the v1 deterministic background-texture shift: amplitude `0.35`, threshold `0.20`, `7 x 7` low-frequency field, unchanged labels, and the same partition-specific seeds and shift hash.

Four path names describe interventions only. They are not state labels.

| Path | Trainable parameters | B optimizer | Additional intervention |
|---|---|---|---|
| `standard_full` | all | SGD lr `0.02`, momentum `0.9`, wd `0.0001` | none |
| `head_only` | classifier head only | SGD lr `0.02`, momentum `0.9`, wd `0.0001` | convolutional trunk frozen throughout B |
| `replay_full` | all | SGD lr `0.02`, momentum `0.9`, wd `0.0001` | clean-A replay fraction `0.10` |
| `head_reset_full` | all | SGD lr `0.02`, momentum `0.9`, wd `0.0001` | classifier head reset once at B start using deterministic seed `seed + 700000` |

`head_reset_full` is the single locked plasticity-restoring intervention. It cannot be supplemented with neuron resets, noise, schedulers, or an unfreezing curriculum after seeing results.

Each path receives at most 20 B epochs. B data order is fixed by seed and identical across paths except for the replay examples inherent to `replay_full`. Checkpoints and B validation/probe metrics are saved at B0 and every epoch.

## 4. B endpoint measures

Checkpoint selection can read only:

- B validation balanced accuracy;
- B validation mean cross-entropy/NLL;
- B validation expected calibration error with 15 equal-width confidence bins;
- checkpoint epoch and update count;
- the immediately preceding B checkpoint's three endpoint measures, solely for the stability rule.

It cannot read probe representations, gradients, Fisher, A retention, any future-task definition, or any future outcome.

The following are recorded but not used for matching:

- predictive entropy;
- representation drift from A (linear CKA);
- effective representation rank, defined as entropy effective rank of the centered probe covariance spectrum;
- gradient norm and four-batch gradient disagreement;
- parameter update norm and distance from A;
- inactive-unit ratio, defined as the fraction of penultimate units with mean absolute activation below `10^-4` on the fixed probe;
- feature reuse (CKA with A-end features);
- A validation retention;
- diagonal empirical-Fisher transition burden at the selected checkpoint, exploratory only;
- B adaptation epoch and update budget.

These are process measurements and explanatory proxies. They do not define path effect or a new selective-resynchronization construct.

## 5. Stable candidate checkpoints

A B checkpoint at epoch `e` is eligible only when `2 <= e <= 20` and both `e-1` and `e` satisfy the broad adequacy region:

- balanced accuracy at least `0.75`;
- NLL at most `0.80`;
- ECE at most `0.15`.

The consecutive-checkpoint stability rule also requires:

- absolute accuracy change no greater than `0.020`;
- absolute NLL change no greater than `0.080`;
- absolute ECE change no greater than `0.030`.

This prevents selection on one accidental evaluation crossing. Epoch 1 can never be selected.

## 6. Within-seed four-path endpoint matching

For each seed, enumerate one stable candidate from each of the four paths. A tuple is a valid matched group only if its selected endpoints satisfy all three range constraints:

\[
\max_p \mathrm{BA}_{B,p}-\min_p \mathrm{BA}_{B,p}\le 0.015,
\]

\[
\max_p \mathrm{NLL}_{B,p}-\min_p \mathrm{NLL}_{B,p}\le 0.060,
\]

\[
\max_p \mathrm{ECE}_{B,p}-\min_p \mathrm{ECE}_{B,p}\le 0.030.
\]

If several tuples qualify, choose deterministically by the following lexicographic key:

1. smallest maximum selected epoch across paths;
2. smallest normalized endpoint range

\[
d_{group}=\frac{range(BA)}{0.015}+\frac{range(NLL)}{0.060}+\frac{range(ECE)}{0.030};
\]

3. smallest sum of selected epochs;
4. lexicographically smallest epoch tuple in path order `standard_full`, `head_only`, `replay_full`, `head_reset_full`.

No three-path fallback is permitted. A seed either forms a complete four-path group or is unmatched.

## 7. Matching feasibility gate

Stage 1 runs A/B only for seeds `3001`–`3005`. No future-task dataset or loader may be constructed.

Feasibility passes only if:

1. at least 3 of 5 seeds form complete four-path groups under the locked windows;
2. every selected checkpoint hash verifies and precedes any future-branch artifact;
3. observed endpoint ranges respect all three tolerances;
4. at least 60% of matched groups retain a nontrivial path-history contrast, defined prospectively as either a selected-epoch range of at least 2 epochs or a representation-drift range of at least `0.05`.

If any condition fails, the result is:

> **matched-endpoint design infeasible under current interventions**.

The matching window cannot be widened and no future task can be run.

After a feasibility pass, the same frozen rules are applied to the ten locked seeds. At least 8 of 10 complete four-path groups are required before future branching. Unmatched seeds are retained in trajectory/failure reporting but excluded from the primary path analysis. If fewer than eight groups match, stop with `DESIGN INFEASIBLE` and do not run future tasks.

## 8. Freeze and leakage boundary

Before any future task is constructed:

1. write `matched_B_checkpoints.parquet` using an A/B-only schema;
2. write `endpoint_balance.csv`;
3. freeze each selected checkpoint and record file SHA-256 plus state-dict tensor SHA-256;
4. hash the matching specification, configuration, code tree, data manifests, and matched-checkpoint table;
5. make the matched table, balance table, configuration snapshot, and lock manifest read-only;
6. assert that no file or schema used for matching contains `future`, `C`, `Q`, or outcome fields;
7. only then permit construction of future-task loaders.

Future results cannot replace a checkpoint, change a window, remove a path, or alter a task.

## 9. Future environments

Every selected B checkpoint is copied into four branches. All branches use the B-textured input as their base and one additional mechanism:

### F1: `rotation20`

- deterministic `+20 degree` image rotation after the B texture;
- original ten-class label rule;
- measures adaptation to a geometric covariate/style shift.

Primary task utility: all-class balanced accuracy.

### F2: `class_imbalance_4to1`

- original B images and labels;
- training prior gives classes 0–4 four times the probability of classes 5–9;
- a deterministic 50,000-draw training index sequence is generated for each seed and shared across paths;
- held-out NLL is weighted to the same fixed target prior on the full official test set.

Primary task utility: negative target-prior-weighted NLL, so improvement is a reduction in weighted NLL. Weighted accuracy and calibration are secondary.

### F3: `partial_label_permutation`

- B images;
- fixed label permutation `0 <-> 6`, `2 <-> 4`;
- measures partial rule relearning, with changed and unchanged classes reported separately.

Primary task utility: balanced accuracy over changed classes `{0,2,4,6}`.

### F4: `parity_regrouping`

- B images;
- original even-numbered classes map to label 0 and odd-numbered classes map to label 1;
- the unchanged ten-output head is used, with labels restricted to 0/1;
- measures adaptation to a new class-combination decision boundary.

Primary task utility: balanced binary accuracy.

These tasks are fixed before outcomes. Rotation is not a stronger B texture; imbalance changes the data prior; partial permutation changes part of the rule; regrouping compresses the rule into a new binary task.

## 10. Identical future adaptation rule

For every path and future task:

- load the exact selected B state dict;
- create a fresh optimizer; never inherit B optimizer state;
- unfreeze the full network;
- SGD lr `0.02`, momentum `0.9`, weight decay `0.0001`;
- batch size 128;
- six epochs and the same number of optimizer updates per task;
- no replay, scheduler, gradient clipping, reset, or path-specific adaptation;
- task/seed-specific training order shared identically across all four paths;
- zero-update task baseline recorded before the first optimizer step.

The branch manifest must prove that four future branches for a path share the selected B tensor hash and that all four paths within a seed use identical future-task data-order hashes and budgets.

## 11. Outcomes

For future task `k`, let `u_{k,e}` be its locked higher-is-better utility at epoch `e`. The raw adaptation-efficiency outcome is

\[
q_{k,i,p}=\frac{1}{6}\sum_{e=1}^{6}[u_{k,i,p,e}-u_{k,i,p,0}].
\]

This uses the entire fixed-budget learning curve. C0/future-start utility is also reported separately.

Within each task, standardize over all complete matched seed-path observations:

\[
z(q_k)=\frac{q_k-\overline q_k}{\max(s_k,0.02)},
\]

where `s_k` is the sample standard deviation. The `0.02` floor prevents a nearly invariant task from receiving arbitrarily high weight. No winsorization or outcome-dependent task deletion is allowed.

The unique primary outcome is

\[
\boxed{Q_{future,i,p}=\frac{1}{4}\sum_{k=1}^{4}z(q_{k,i,p})}.
\]

Secondary outcomes:

- each raw and standardized `q_k`;
- future-start utility;
- final utility;
- fixed thresholds: F1 balanced accuracy `0.80`, F2 weighted NLL `0.40`, F3 changed-class accuracy `0.60`, F4 binary balanced accuracy `0.85`;
- epochs to threshold, censored after epoch 6;
- A and B retention after each future task;
- task loss variance and non-finite failure;
- head/trunk parameter distance from the selected B checkpoint.

Both baseline-adjusted `q_k` and unadjusted utility curves are mandatory. A path effect cannot be attributed solely to different future-start headroom without explicit reporting.

## 12. Primary hypotheses

- **H1, independent path effect:** matched B paths differ in `Q_future`.
- **H2, endpoint insufficiency:** path indicators retain explanatory value after controlling residual within-window B accuracy, NLL, and ECE differences.
- **H3, cross-future stability:** a path contrast is not generated by only one future task.
- **H4, process interpretation only:** B process metrics may explain a path contrast but cannot be combined post hoc into a new construct.

The null or a practically negligible path effect is an allowed and decision-relevant result.

## 13. Statistical analysis

### 13.1 Primary matched-group model

Fit OLS with seed/A-checkpoint fixed effects, path indicators, and within-seed-centered endpoint residuals:

\[
Q_{future,i,p}=\alpha_i+\beta_p+
\gamma_1\widetilde{BA}_{i,p}+
\gamma_2\widetilde{NLL}_{i,p}+
\gamma_3\widetilde{ECE}_{i,p}+\epsilon_{i,p}.
\]

Report adjusted path means, all six pairwise path contrasts, HC3 intervals, partial eta-squared for the path block, and a seed-blocked permutation test with 5,000 permutations. Report a no-endpoint-covariate matched model as a sensitivity analysis.

### 13.2 Multi-task model

On task-standardized `q_k`, fit seed fixed effects, path, task, path-by-task interaction, and centered endpoint residuals. Report path main effect, interaction effect, task-specific contrasts, and cluster-by-seed uncertainty.

### 13.3 Robustness

- leave one seed out;
- leave one future task out while retaining the locked task scaling constants;
- paired seed bootstrap with 5,000 resamples;
- matched-group within-seed path rankings;
- models with and without residual endpoint controls;
- C0/future-start utility added as a sensitivity control;
- complete-case group analysis: if any path or future branch is missing, the entire seed group is excluded from the primary model and retained in failure reporting.

### 13.4 Exploratory inverted-U tests

For representation drift, effective-rank change, update norm, and gradient disagreement, compare:

1. linear;
2. linear plus quadratic;
3. restricted cubic spline with three fixed degrees of freedom.

Use nested CV and report prediction error. These are new v2 exploratory hypotheses. They cannot change the v1 decision, define selective resynchronization, or determine the primary path-effect decision.

## 14. Decision rules

All decisions first require a valid matched design and at least eight complete formal groups.

### 14.1 PATH EFFECT SUPPORTED

All are required:

1. path-block partial eta-squared at least `0.06` and seed-blocked permutation `p < 0.05`;
2. at least one of the six prespecified pairwise adjusted contrasts has absolute effect at least `0.30` task-standardized units, a paired seed-bootstrap 95% interval excluding zero, and Holm-adjusted `p < 0.05`;
3. that contrast retains its sign in at least three of four leave-one-future-task-out analyses and in at least 80% of leave-one-seed-out analyses;
4. at least three of four task-specific contrasts have the same sign, or every leave-one-task-out average has the same sign;
5. adding residual B endpoint controls changes its magnitude by no more than 25% and does not reverse its sign;
6. the result is not solely a C0/future-start headroom effect.

### 14.2 CONDITIONAL SUPPORT

Use this decision only when no NOT-SUPPORTED rule applies and a practically meaningful indication remains, for example:

- partial eta-squared lies between `0.03` and `0.06`;
- a contrast is at least `0.20` but uncertainty includes zero;
- direction is stable across seeds but heterogeneous across future tasks;
- eight or nine groups complete, producing wide uncertainty;
- only a coherent subset of the prespecified paths differs.

The unresolved limitation must be named. Conditional support does not authorize a new composite score.

### 14.3 PATH EFFECT NOT SUPPORTED

Trigger this result if any major condition holds:

1. path-block partial eta-squared is below `0.03` and every adjusted pairwise contrast is smaller than `0.20` in absolute value;
2. any apparent average contrast is eliminated or reversed by the residual endpoint controls;
3. all practically meaningful effect is attributable to one future task;
4. the strongest contrast changes sign in more than half of leave-one-seed analyses or more than two leave-one-task analyses;
5. future-start utility explains the apparent contrast and the path effect disappears;
6. process metrics fail to generalize across future tasks and no categorical path effect remains.

### 14.4 DESIGN INFEASIBLE

Use this result if the Stage-1 gate fails, fewer than eight locked four-path groups can be formed, or the locked windows would need post hoc widening.

## 15. Missingness and stopping

- software failure: fix only the software defect, version the correction, and rerun the same cell once;
- scientific path failure: retain and report; do not tune the intervention;
- future-branch failure: retain the failure, exclude the complete seed group from the primary complete-group model, and report sensitivity where possible;
- fewer than eight complete formal groups: no supported/not-supported inference; report inconclusive execution;
- fixed stopping: five feasibility seeds, then ten locked seeds if feasible; no significance-based stopping.

After `15_path_effect_decision.md`, stop. Do not run CIFAR-10, add architectures, create `SR_preC v2`, draft a full paper, change v1 NO-GO, or edit SRT canonical/Core/ChoiceMap files.

## 16. Claim boundary

Allowed conclusion:

- a matched endpoint path intervention did, did not, or may have affected multi-future adaptation under this Fashion-MNIST protocol.

Not allowed:

- path dependence proves selective resynchronization;
- any process metric is selective resynchronization;
- Fisher estimates `Psi_f`;
- neural-network path effects establish an ontological, conscious, or subject-level mechanism.
