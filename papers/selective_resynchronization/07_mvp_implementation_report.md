---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-MVP-IMPLEMENTATION-20260711
type: implementation_report
status: completed_mvp_v1
canonical: false
created: 2026-07-11
---

# Fashion-MNIST MVP Implementation Report

## Scope

This report documents implementation and execution only. The experiment tests a P4 domain-level proxy prediction and does not test SRT ontology.

## Implemented structure

- deterministic Fashion-MNIST `A -> B -> C` pipeline;
- separate 50,000/8,000/2,000/10,000 train/validation/probe/test partitions;
- light CNN with a 64-dimensional penultimate representation;
- constrained, standard, high-update, and replay paths;
- A/B-only pre-C schema and read-only hash freeze before C;
- epoch-level loss, accuracy, entropy, gradient, parameter, KL, representation, coherence, and diagonal empirical-Fisher metrics;
- regression-control, matching, simple-baseline, Fisher-increment, seed/condition robustness, and secondary state analyses.

## Locked protocol

- seeds: `[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]` in every condition;
- A/B/C epochs: `{'A': 15, 'B': 10, 'C': 8}`;
- primary predictor: equal-weight five-dimensional `SR_preC` from `06_mvp_spec_lock.md`;
- primary outcome: changed-class C AULC gain over eight epochs;
- configuration SHA-256: `90c0aeb56419663f0f805abf6f92e8202409198eb4647f0a821b1b7717ab2b01`;
- specification SHA-256: `a711b690529c8bbaa1aa377776f41236c2239d98afd980a33417ea3c277f4a79`;
- code-tree SHA-256: `101ab1fbdc9bc714ae2b51f42f9b4863808949ce8f26a5f42d8b9f5447da8403`;
- Git commit at lock: `02d78d2b2cb1d0bf6ad49a224c5350effc541a27`.

## Leakage and immutability checks

All 40 completed runs passed pre-C file hash and timestamp verification before analysis. `preC_features` records carried `uses_c_data: false`; C outcomes stored and matched the frozen pre-C SHA-256.

## Deviations

The pre-formal implementation clarification in `06_mvp_spec_lock.md` made bootstrap, state-stability, and Fisher decision computations executable before the formal manifest was created. It did not change `SR_preC`, `Q_C`, windows, weights, conditions, seeds, or effect thresholds. No outcome-dependent change was permitted. Any runtime deviations or failed runs are recorded in `outputs/processed/failed_runs.csv` and the run logs.

No formal run failed and no formal run was repeated. A post-analysis output audit made two presentation-only corrections without changing data or inference: the zero-row `matched_pairs.csv` and `failed_runs.csv` received explicit headers, and `abc_full_learning_curves.png` was added because the automatically named `abc_learning_curves.png` contained only the C-stage changed-class curve. The added full-sequence figure uses the locked step table and active-environment balanced accuracy for A, B, and C.

## Software and numerical checks

- nine automated tests passed before formal locking, including C-schema rejection, frozen-artifact mutation detection, phase separation, deterministic shifts, reproducibility, metric shapes, Fisher non-negativity, and a synthetic analysis-path test;
- smoke and three-seed pilot flows completed before the formal cohort;
- pilot standardization and no-shift state calibration were produced from A/B-only artifacts before formal C execution.

## Run environment and output integrity

- device: Apple Silicon MPS on macOS 15.7.4 (`arm64`);
- Python 3.12.11, PyTorch 2.7.1, NumPy 2.2.6;
- 40 complete run-manifest rows, 1,400 epoch-level metric rows, 120 phase-summary rows, and zero failed runs;
- all empirical-Fisher burdens were finite and non-negative with a fixed sample count of 20;
- `run_manifest.csv` records the locked Git SHA, configuration SHA-256, and code-tree SHA-256 for every run.

## Known limitations

- Fashion-MNIST is a mechanism gate, not evidence of generality.
- The C shift can be solved partly in the output head.
- The empirical Fisher is diagonal and based on 20 fixed examples.
- Four-state classification is secondary and may be invalid due to sparse classes.
- Forty trajectories limit precision for multi-predictor comparisons.
