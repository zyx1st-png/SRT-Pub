---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-TWO-SHIFT-PROTOCOL-20260710
type: experiment_protocol
status: draft_v0_1
layer: paper_working
epistemic_layer: bridge
claim_mode: preregistration_plan
claim_level: P4
canonical: false
created: 2026-07-10
depends_on:
  - PAPER-SELECTIVE-RESYNCHRONIZATION-CONSTRUCT-HARDENING-20260710
---

# Two-Shift Protocol: `A -> B -> C`

## 0. Protocol objective

The experiment asks one question:

> Does a pre-second-shift pattern of perturbation-induced opening, selective incorporation, and restabilization predict later adaptability after current performance has been matched?

The protocol is not designed to confirm SRT or to make Fisher geometry win. Fisher-geometric burden is one candidate predictor in a comparative measurement test.

## 1. Design principles

1. **Two changes are mandatory.** `A -> B` measures current adaptation; `B -> C` measures future adaptation capacity.
2. **`B` and `C` differ mechanistically.** The primary design does not use two severities of the same corruption.
3. **Performance is matched before `C`.** Otherwise later adaptation can be explained by unequal mastery of `B`.
4. **Pre-`C` predictors never use `C` outcomes.** This prevents circular construct validation.
5. **Fisher is optional for the phenomenon.** State classification and the primary construct test do not depend on `G_t`.
6. **Continuous analyses are primary.** Four-state labels are secondary summaries governed by frozen thresholds.
7. **Pilot/calibration and confirmatory seeds are disjoint.** Calibration fixes windows, thresholds, probe sizes, and the common-support matching band.
8. **A negative result remains publishable.** The study can conclude that retained adaptability is useful while selective resynchronization is redundant, or that Fisher adds no incremental value.

## 2. Environment sequence

### 2.1 Environment `A`: stable baseline

- original balanced training distribution;
- original label rule;
- fixed official or prespecified train/validation/test split;
- fixed training budget and checkpoint cadence;
- final `K_A` checkpoints define `W_A`.

The `A` baseline is valid only if held-out loss/performance and selected internal measures satisfy the frozen stability rule. Runs failing for scientific reasons remain reported but cannot support an opening-from-stability claim.

### 2.2 Environment `B`: label-preserving covariate/background shift

Primary mechanism:

- preserve class labels;
- add a procedurally generated low-frequency texture or background field;
- apply it predominantly to low-intensity/background pixels using a frozen mask rule;
- use disjoint texture seeds for training, validation, test, and robustness probes;
- keep image identity splits unchanged.

The exact texture generator, amplitude range, spatial-frequency range, mask rule, and random seeds are versioned before confirmatory runs. Shift strength is selected on calibration seeds to cause measurable but recoverable degradation in the standard-learning condition.

This design tests adaptation to a functionally label-preserving visual change. Common-corruption benchmarks establish that corruption robustness is a distinct empirical target, but the present study uses held-out procedural instances to reduce overfitting to a named benchmark ([Hendrycks & Dietterich, 2019](https://openreview.net/forum?id=HJz6tiCqYm)).

### 2.3 Environment `C`: partial label-rule shift

Primary mechanism:

- retain the `B` input/background distribution;
- apply a fixed partial permutation to four of ten class labels;
- leave six classes unchanged;
- use the same mapping for `C` train, validation, and test sets;
- freeze the mapping before confirmatory runs.

For Fashion-MNIST, the calibration default is two pairwise swaps among visually confusable classes, such as `T-shirt/top <-> Shirt` and `Pullover <-> Coat`. The final mapping is frozen before confirmatory seeds and must not be chosen for a favorable result.

The partial mapping permits separate reporting for changed and unchanged classes. It also creates a serious head-local confound: a flexible output layer may remap labels without substantial representation reorganization. The protocol therefore includes:

- head-versus-trunk update norms;
- layerwise representation measures;
- head-only adaptation control;
- frozen-head or trunk-only sensitivity control where feasible;
- changed-class and unchanged-class outcomes.

If the effect exists only in the final layer and carries no broader transfer/robustness signal, the interpretation is narrowed to output-rule relearning.

### 2.4 Mechanistic distinction rule

The primary sequence is valid because:

- `A -> B` changes the input distribution while preserving the target rule;
- `B -> C` changes part of the target rule while preserving the `B` input mechanism.

An optional sensitivity analysis replaces the partial label-rule shift with a fixed class-prior / imbalance shift. That analysis is secondary because class-prior change can alter accuracy without requiring rich internal reorganization and must be evaluated with balanced accuracy and calibration.

## 3. Minimum viable protocol: Fashion-MNIST

### 3.1 Purpose

The MVP is a mechanism and construct-validity experiment on ordinary compute. It is not a small-scale proof and does not require a full Fisher matrix.

### 3.2 Data

- dataset: Fashion-MNIST;
- train/calibration split: stratified split of the official training set, fixed once and versioned;
- test: official held-out test set;
- fixed probe: `B_probe = 256` stratified validation examples per environment, disjoint from gradient updates;
- all `A/B/C` transforms are deterministic conditional on logged transform seeds;
- balanced and per-class outcomes are retained even when the training stream becomes imbalanced in a sensitivity condition.

Recommended split:

| Partition | Size | Use |
|---|---:|---|
| training stream | 50,000 | parameter updates in `A`, `B`, and `C` |
| calibration/validation | 10,000 | hyperparameter calibration, matching band, probes, stopping diagnostics |
| official test | 10,000 | confirmatory outcomes only |

The exact split seed is frozen and published in the run manifest.

### 3.3 Model

One light convolutional network:

```text
Conv(1, 32, 3) -> ReLU -> Conv(32, 32, 3) -> ReLU -> MaxPool
Conv(32, 64, 3) -> ReLU -> MaxPool
GlobalAveragePool -> Linear(64, 10)
```

Batch normalization is omitted in the MVP to avoid mixing representation change with running-statistic adaptation. A batch-normalized variant is exploratory.

### 3.4 Training budgets

Initial frozen defaults, subject to calibration before registration:

- batch size: `128`;
- `A`: `15` epochs;
- `B`: maximum `10` epochs, with checkpoints every `100` optimizer updates;
- `C`: fixed early-adaptation budget of `8` epochs;
- optimizer: SGD with momentum `0.9` in all MVP conditions;
- primary learning-rate schedule: fixed within each environment; schedules and resets are preregistered.

The confirmatory analysis uses the full fixed budget. It does not stop early for significance.

### 3.5 Adaptation conditions

The MVP requires enough dynamical diversity to test the state framework:

| Condition | Purpose | Status |
|---|---|---|
| standard SGD | ordinary adaptation reference | confirmatory |
| strong regularization + reduced learning rate | rigidity-enriched condition | confirmatory if it retains common `B` support; otherwise state anchor only |
| high learning rate / update-noise condition | disorganization-enriched condition | confirmatory if numerically valid; extreme failing variant is calibration anchor |
| 10% stratified replay from prior environments | continual-learning baseline | confirmatory |

Calibration anchor conditions may additionally freeze the trunk or use an intentionally excessive learning rate. They verify that the proposed metrics react to known rigidity/collapse manipulations, but they do not enter the primary efficacy comparison unless preregistered and within common support.

### 3.6 Seeds

- pilot/calibration: `3` seeds per condition; excluded from confirmatory inference;
- confirmatory: `10` paired seeds per condition;
- no-shift calibration controls: at least `5` seeds for each primary optimizer/regime needed to estimate the opening envelope;
- identical seed IDs are paired across valid conditions for initialization, data order, and procedural shifts where technically possible.

The MVP core is approximately `40` confirmatory shifted trajectories plus no-shift and calibration runs.

### 3.7 MVP Fisher computation

No full `P x P` Fisher matrix is formed. For fixed probe samples and score vectors

\[
s_i
=
\nabla_\theta\log p_\theta(y_i\mid x_i),
\]

compute

\[
G_t^{\mathrm{EF}}
=
\frac{1}{2B_{\mathrm{probe}}}
\sum_{i=1}^{B_{\mathrm{probe}}}
\left(s_i^{\top}\Delta\theta_t\right)^2.
\]

This is an empirical-Fisher quadratic estimate. It is evaluated every `100` updates and at all transition checkpoints. Per-sample score-vector products are computed without materializing the full matrix. The primary sensitivity analysis uses model-sampled labels to approximate the conditional Fisher on the same probe.

Required labels in outputs:

- `fisher_empirical_quadratic`;
- `fisher_model_sampled_quadratic` where computed;
- never `selection_cost` or `psi_f`.

## 4. Main protocol: CIFAR-10

### 4.1 Purpose

The main protocol tests whether the construct and predictor comparisons survive a harder visual task, architecture variation, and optimizer variation.

### 4.2 Core factorial design

| Factor | Levels |
|---|---|
| dataset | CIFAR-10 |
| architecture | small four-block CNN; ResNet-18 |
| optimizer | SGD with momentum; AdamW |
| adaptation control | standard; strong regularization; 10% replay |
| environment sequence | clean `A` -> held-out background/texture `B` -> partial label-rule `C` |
| confirmatory seeds | `12` paired seeds per architecture × optimizer × adaptation-control cell |

This yields `2 x 2 x 3 x 12 = 144` core trajectories. Calibration and no-shift controls are additional and are not pooled into confirmatory inference.

The choice of `12` seeds is a design commitment, not a claim of universal power. A simulation-based power analysis using calibration-run variance must be completed and frozen before the main experiment. If the prespecified smallest effect of interest requires more seeds, the registration is amended before confirmatory outcomes are inspected.

### 4.3 CIFAR-10 shifts

- `A`: clean balanced CIFAR-10 with original labels;
- `B`: label-preserving procedural texture/background shift with held-out texture families and strengths;
- `C`: the same `B` input mechanism plus a fixed four-class partial label permutation;
- robustness: held-out `B` texture realizations and one corruption family not used in training;
- shift-order sensitivity: a smaller preregistered subset evaluates label-rule first and background shift second, without pooling it into the primary estimate.

### 4.4 Additional measurement-challenge baselines

After the core protocol, optional prespecified extensions can add:

- SAM or another sharpness-aware method;
- diagonal/K-FAC Fisher-preconditioned or natural-gradient-like updates;
- continual backpropagation / unit-reset intervention;
- stronger replay or regularization variants.

These extensions are not required to decide whether the construct survives the MVP. They are useful for generating different Fisher and optimization geometries at similar endpoint performance.

## 5. Matching current `B` performance before `C`

### 5.1 Primary estimand

The primary comparison asks how quickly two systems adapt to `C` when they begin `C` with comparable held-out `B` performance.

### 5.2 Frozen matching procedure

Using calibration seeds only:

1. For each eligible condition, estimate the distribution of maximum `B` validation balanced accuracy.
2. Define a common-support target `b_star` as two percentage points below the lowest condition-level median maximum among the conditions intended for the matched analysis.
3. Freeze an accuracy band around `b_star` (initial default `plus/minus 0.5` percentage points) and a compatible validation-loss/calibration band.
4. For each confirmatory run, select the earliest saved `B` checkpoint entering the frozen band.
5. Start `C` from that checkpoint with its model and, for the primary system-level estimand, its optimizer state.
6. Include updates-to-match and cumulative examples seen as covariates; perform a secondary fixed-budget analysis.

The constants are written symbolically here because they must be calibrated before confirmatory outcomes exist. The algorithm, not a favorable observed result, determines them.

### 5.3 Common-support failure

The primary matched analysis is declared not identified for a cell if fewer than `70%` of its confirmatory runs enter the frozen band or if overlap is too narrow for stable weighting/matching. The response is not to widen the band after seeing `C` outcomes.

Prespecified fallbacks:

1. report the failure transparently;
2. run a continuous covariate-adjusted analysis of `Q_C` using `B` accuracy/loss;
3. restrict a secondary analysis to the preregistered common-support subset;
4. downgrade causal/process interpretation.

### 5.4 Optimizer-state estimands

- **Primary, system-level retained adaptability:** preserve the assigned optimizer state and schedule when entering `C`.
- **Secondary, model-state residual plasticity:** branch from the matched checkpoint, reset optimizer state, and apply a common `C` optimizer/schedule.

If the system-level result disappears under optimizer reset, the conclusion is limited to whole-training-system adaptability rather than a persistent representation/parameter property.

## 6. Measurements

### 6.1 Primary construct block, all measured before `C`

- peak and area of `D_t^grad` in `W_B^open`;
- peak and area of layerwise `D_t^repr` in `W_B^open`;
- early-to-stable change-subspace overlap `S_B`;
- decay of gradient disagreement from open to stable window;
- stable-`B` performance, slope, and variance;
- late-`B` representation velocity;
- held-out `B` robustness.

The primary construct test treats these as a prespecified feature block. It does not tune a composite against `Q_C`.

### 6.2 Primary outcome

\[
Q_C^{\mathrm{AULC}}
=
\frac{1}{K_C}
\sum_{k=1}^{K_C}
\left[
\operatorname{BA}_C(k)-\operatorname{BA}_C(0)
\right],
\]

reported for:

- all classes;
- four changed classes, designated primary for the label-rule shift;
- six unchanged classes, used as a stability/forgetting guardrail.

### 6.3 Secondary outcomes

- updates and samples to a fixed `C` balanced-accuracy threshold;
- final `C` balanced accuracy and NLL under fixed budget;
- `A` and `B` forgetting after `C`;
- expected calibration error / Brier score;
- held-out corruption/background robustness;
- optional fixed-budget return-to-`B` relearning speed;
- wall-clock time, FLOPs estimate, and examples seen as realized-cost descriptors.

### 6.4 Mandatory predictor/baseline set

At the same checkpoint cadence, record:

- loss and balanced accuracy;
- gradient norm;
- parameter update norm and distance from `A` / early `B` checkpoints;
- predictive KL divergence on the fixed probe;
- predictive entropy;
- representation drift / CKA distance;
- approximate Hessian trace by Hutchinson probes;
- one-step or small-radius sharpness approximation;
- Fisher quadratic burden `G_t` and accumulated `sum_t G_t`;
- BOCPD and CUSUM scores applied to prespecified monitored series.

BOCPD and CUSUM are evaluated as change-detection baselines, not success measures. BOCPD estimates the posterior distribution of the current run length ([Adams & MacKay, 2007](https://arxiv.org/abs/0710.3742)); CUSUM is a sequential accumulation procedure ([Page, 1954](https://academic.oup.com/biomet/article-abstract/41/1-2/100/456627)). Their false-alarm rate and detection delay are reported separately from `Q_C` prediction.

## 7. Fisher predictor comparison

### 7.1 Candidate quantities

Primary local quantity:

\[
G_t
=
\frac{1}{2}
\Delta\theta_t^{\top}F_t\Delta\theta_t.
\]

Primary path summary:

\[
\mathcal G_{B}
=
\sum_{t\in W_B^\mathrm{open}\cup W_B^\mathrm{stable}}
G_t.
\]

Additional prespecified summaries are peak, time-to-peak, open-window area, stable-window mean, and decay ratio. The path sum is an energy-style discrete accumulation, not automatically a geodesic length or realized training cost.

### 7.2 Direct competitors

Fisher summaries are compared with:

- output-space KL change;
- gradient norm and update norm;
- parameter distance;
- loss change;
- predictive entropy;
- representation drift;
- Hessian trace and sharpness;
- generic BOCPD/CUSUM transition scores.

Empirical Fisher, model-sampled Fisher, Hessian, and KL are not treated as interchangeable. Estimator, probe, layer, damping, and checkpoint cadence are logged.

### 7.3 Projection-failure checks

Fisher projection failure is recorded when one or more of the following occurs:

- rankings reverse under reasonable empirical versus model-sampled Fisher choices;
- estimates are dominated by probe composition or damping;
- functionally equivalent parameter rescalings change conclusions materially;
- `G_t` is nearly redundant with output KL or update norm;
- Fisher adds no held-out prediction beyond simpler baselines;
- computational cost prevents adequate seed-level measurement.

Projection failure weakens or rejects the Fisher bridge. It does not by itself refute the two-shift construct.

## 8. Ablations and negative controls

### 8.1 Required MVP controls

- no-shift `A -> A` control for `D` envelopes;
- transform-seed holdout for `B`;
- temporal permutation null for early-to-stable subspace overlap;
- matched random-noise perturbation with comparable immediate loss increase;
- simple rollback / return-to-`A` condition;
- head-only `C` adaptation control;
- fixed-budget analysis alongside performance matching;
- probe-size sensitivity (`128`, `256`, `512` where feasible);
- CKA layer sensitivity;
- empirical versus model-sampled Fisher on a subset.

### 8.2 Main-study ablations

- remove Fisher block;
- remove desynchronization block;
- remove selective-incorporation features;
- remove restabilization features;
- replace process block with endpoint `B` metrics only;
- reset versus retain optimizer state at `C`;
- reverse shift order on a preregistered subset;
- change partial label permutation;
- vary background texture family and severity;
- compare replay and strong-regularization conditions;
- compare whole-network versus layerwise metrics.

## 9. Compute and storage estimates

These are planning ranges, not guaranteed measurements.

### 9.1 MVP

- core trajectories: about `40` confirmatory plus calibration/no-shift controls;
- expected compute: approximately `25-75` single-GPU hours, or a longer but feasible CPU run;
- Fisher/Hessian probe overhead: expected `1.5x-3x` on metric checkpoints, controlled by sparse checkpoint cadence;
- storage: approximately `10-30 GB` if only transition/matched checkpoints are retained; substantially more if every checkpoint is saved.

### 9.2 CIFAR-10 main protocol

- core trajectories: `144` plus calibration and controls;
- expected compute: approximately `300-900` modern single-GPU hours depending on architecture, metric cadence, and branching at `C`;
- storage: approximately `0.3-1.0 TB` before checkpoint thinning;
- recommended execution: parallel jobs with deterministic manifests, checkpoint thinning outside transition windows, and a separate metrics store.

A calibration benchmark must measure actual wall time and memory before committing to the full protocol. If the Fisher/Hessian overhead threatens adequate seeds, preserve seeds and reduce metric cadence or estimator complexity; do not sacrifice replication to compute a privileged Fisher object.

## 10. Expected output files

```text
experiments/selective_resynchronization/
  configs/
    mvp_fashion_preregistered.yaml
    main_cifar_preregistered.yaml
    shift_definitions.yaml
  manifests/
    dataset_splits.json
    probe_ids.json
    seed_manifest.csv
    environment_versions.json
  raw/
    run_<run_id>/
      config_resolved.yaml
      training_log.jsonl
      metrics_long.parquet
      checkpoints/
      failure_record.json
  derived/
    matched_checkpoints.csv
    state_features.parquet
    fisher_features.parquet
    change_point_features.parquet
    outcomes_qc.parquet
  analysis/
    confirmatory_results.json
    model_comparison.csv
    effect_sizes.csv
    robustness_checks.csv
    exclusions.csv
  figures/
    temporal_profiles/
    matched_qc/
    model_comparison/
    state_examples/
  reports/
    run_completion_report.md
    preregistration_deviation_log.md
    null_and_failure_report.md
```

Every derived row must contain dataset, architecture, optimizer, condition, seed, environment, checkpoint, probe version, metric version, and code commit.

## 11. Implementation order

1. Implement deterministic `A/B/C` transforms and dataset split tests.
2. Implement the light CNN and ordinary training logs without Fisher.
3. Validate no-shift, rigidity, and disorganization anchors.
4. Implement fixed-probe gradient disagreement and CKA displacement.
5. Implement selective-incorporation and stability features.
6. Implement checkpoint matching and `C` branching.
7. Implement empirical-Fisher quadratic products; validate against a tiny explicit Fisher matrix.
8. Implement simple baselines, BOCPD, CUSUM, Hessian trace, and sharpness approximation.
9. Run disjoint calibration seeds and freeze the preregistration.
10. Run the confirmatory Fashion-MNIST MVP.
11. Apply the construct-retention / kill criteria before scaling to CIFAR-10.

## 12. Scale-up gate

Proceed from Fashion-MNIST to the CIFAR-10 main protocol only if:

- the two-shift pipeline and performance matching are technically reliable;
- `SR_preC` measures are stable enough for confirmatory use;
- at least two intended dynamical regimes are empirically distinguishable;
- common support exists for the primary matched comparison;
- the construct has not met a kill criterion;
- compute estimates preserve the planned seed count.

Fisher need not win this gate. If Fisher loses but the pre-`C` process block predicts retained adaptability, the scale-up remains scientifically justified. If the construct block fails but retained adaptability is still a useful outcome, the scale-up should be redesigned as a plasticity/continual-learning study without selective-resynchronization branding.
