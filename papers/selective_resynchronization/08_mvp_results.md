---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-MVP-RESULTS-20260711
type: empirical_results
status: completed_mvp_v1
canonical: false
created: 2026-07-11
---

# Fashion-MNIST MVP Results

## Primary result

The locked cohort contained **40 runs across 10 paired seeds**.

- standardized `SR_preC` coefficient: `-0.2521`;
- HC3 95% interval: `[-0.6796280325871102, 0.1754983333041515]`;
- seed-cluster bootstrap 95% interval: `[-0.5667215774876391, 0.11556116583323445]`;
- HC3 p-value: `0.2386`;
- incremental leave-one-seed-out CV R-squared over B-performance controls: `0.0004`;
- relative NRMSE improvement: `0.0026`;
- paired seed-bootstrap CV intervals: `{'valid_resamples': 2000, 'delta_cv_r2_interval': [-0.002132953088582715, 0.0026818177770863744], 'relative_nrmse_improvement_interval': [-0.014861202404332634, 0.027258887867684763]}`.

These quantities are reported as effect size, uncertainty, and predictive increment. Statistical significance alone does not determine the decision.

## Simple-baseline comparison

- `SR_preC` minus representation-only CV R-squared: `0.0013`;
- relative NRMSE improvement over representation-only: `0.0090`;
- incremental CV R-squared when `SR_preC` is added to representation drift: `-0.0012`.

## Cross-condition and score robustness

- leave-one-condition coefficients: `{'constrained': -0.08468459565546504, 'high_update': -0.11251209200604517, 'replay': -0.3218515150306537, 'standard': -0.37861925307013466}`;
- leave-one-component-out median Spearman stability: `0.9559`;
- secondary matching: `{'pairs': 0, 'minimum_pairs': 8, 'caliper': 2.677457512199618, 'balance_absolute_smd': {}, 'balance_valid': False, 'analysis_valid': False, 'mean_Q_C_difference': None, 'paired_bootstrap_interval': None}`.

## Fisher result

- status: **lose**;
- standardized coefficient: `0.0151`;
- coefficient interval: `[-1.538568023587909, 1.5686718268971276]`;
- incremental CV R-squared beyond construct and simple baselines: `-0.0366`;
- relative NRMSE improvement: `-0.1333`;
- seed-bootstrap coefficient interval: `[-1.859735207167648, 3.669013306039037]`;
- paired CV intervals: `{'valid_resamples': 2000, 'delta_cv_r2_interval': [-0.08562785513936796, -0.009922747419253575], 'relative_nrmse_improvement_interval': [-0.32636072308624403, -0.039035063285926215]}`;
- Fisher-area/predictive-KL-area Spearman sanity relation: `0.2486`.

This is a result about one diagonal empirical-Fisher predictor. It is separate from the construct result and is not an estimate of `Psi_f`.

## Four-state analysis

`{'counts': {'disorganization_or_unresolved_opening': 26, 'candidate_selective_resynchronization': 14}, 'leave_one_seed_label_agreement': 0.625, 'figure_valid': False, 'reason': 'leave-one-seed modal-label agreement below 0.70'}`

State results are reported visually only if both the locked class-count and leave-one-seed agreement criteria are met. The agreement criterion failed here, so no state figure was generated.

## Nulls, failures, and uncertainty

- GO checks: `{'positive_beta_bootstrap_excludes_zero': False, 'cv_increment_meets_threshold': False, 'beats_representation_baseline': False, 'leave_condition_stable': False, 'one_robustness_consistent': False, 'no_seed_sign_flip': False, 'score_robustness': True, 'leakage_valid': True}`;
- the automated output listed three NO-GO triggers: `['non_positive_increment_and_condition_instability', 'B_performance_nearly_fully_predicts_Q_C', 'leave_one_component_direction_flips']`;
- manual protocol audit upheld the first two triggers but rejected the third label: all five leave-one-component-out coefficients were negative, so they did not *flip* direction relative to the negative full-score coefficient; their median score correlation was `0.9559`. This correction does not alter the NO-GO decision;
- failed-run table: `experiments/selective_resynchronization_mvp/outputs/processed/failed_runs.csv`.

The second upheld trigger refers precisely to the locked base model `M0`, which contains B-end accuracy, B-end loss, A-end accuracy, and condition indicators. Its leave-one-seed-out CV R-squared was `0.9311`; the result should not be paraphrased as evidence that B accuracy alone explains `Q_C`.

No Fashion-MNIST result is generalized to consciousness, ontology, or SRT as a whole.
