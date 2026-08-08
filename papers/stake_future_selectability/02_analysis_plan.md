---
id: PAPER-STAKE-FUTURE-SELECTABILITY-ANALYSIS-PLAN-20260808
type: analysis_plan
status: locked_before_formal
layer: paper_working
epistemic_layer: lab
claim_mode: preregistration
claim_level: P4
canonical: false
created: 2026-08-08
locked_utc: 2026-08-07T17:13:59Z
formal_results_seen_at_lock: false
---

# Stake–Future Selectability MVP Analysis Plan

## Unit and leakage boundary

The observational rows are 72 paired branches, but the independent grouping unit is the 12-level `master_seed`. Random row CV/bootstrap is forbidden. All pre-C predictors are computed and frozen before C construction.

## Predictor blocks

- M0 current-state baseline: B-end success, B-end return, B-end integrity, hazard contacts, cumulative B reward, severity, and condition indicators.
- M1 homeostasis: M0 + B energy-deviation area.
- M2 controllability: M1 + Reach20 summary and Emp5.
- M3 generic adaptation: M2 + representation-drift area, policy-KL area, cumulative update norm, and parameter path length.
- M4 bridge test: M3 + `dV_CF_pre`.

Continuous predictors are standardized inside each training fold. Categorical encodings are fit inside each fold with fixed reference cells. The primary full-cohort coefficient report uses full-cohort standardized continuous variables and OLS HC3.

## Prediction metrics

- leave-one-master-seed-out CV R²: `1 - SSE/SST`, with SST computed around the full observed outcome mean;
- NRMSE: pooled held-out RMSE divided by the full observed SD of `Q_C`;
- primary increments: `CV_R2(M4)-CV_R2(M3)` and `(NRMSE_M3-NRMSE_M4)/NRMSE_M3`.

## Inference and robustness

- standardized M4 `dV_CF_pre` coefficient with HC3 interval;
- 2,000-resample master-seed-cluster bootstrap interval;
- leave-one-master-seed coefficient signs;
- separate low/high severity coefficients;
- condition contrasts S–X, S–T, and T–X as secondary analyses;
- `dPi_CF_pre`, hazard avoidance, B-end integrity, Fisher-like comparator, and post-C Reach20 are secondary only.

If an OLS design is rank-deficient or has condition number above the locked threshold, primary coefficient inference remains transparently reported as unstable. A ridge sensitivity may be added, with alpha selected solely by nested grouped CV inside each training fold; it cannot silently replace the primary coefficient.

## Structural validity gates

Before scientific interpretation:

1. X controlled `i=1.0` versus `i=0.7` has negligible Reach20 effect.
2. T/S controlled reduction measurably lowers future reachability.
3. T reset restores C-start capability near baseline.
4. S enters C with B-earned loss intact.
5. S keeps `agent_id` and branch lifetime identity with no hidden reset/replacement.

Frozen tolerances are: X maximum absolute Reach20 delta `1e-12`; every T/S Reach20 delta strictly above `0.001`; T-reset and S-persistence absolute equality tolerance `1e-12` with zero relative tolerance. Identity/replacement flags must pass exactly.

## Decision

### SRT-BRIDGE GO

All required:

1. manipulation validity passes;
2. S shows nontrivial `dV_CF_pre` relative to X, operationalized as paired S−X mean above zero with the 2,000-resample master-seed bootstrap 95% interval above zero;
3. M4 standardized coefficient is positive and clustered bootstrap 95% CI excludes zero;
4. Δ grouped-CV R² ≥ 0.03;
5. relative NRMSE reduction ≥ 3%;
6. no single seed creates the effect;
7. same direction in both severities, or one positive and the other above the frozen large-reversal boundary of `-0.10` standardized coefficient;
8. no leakage/protocol failure.

### NARROW

Use when manipulation changes behavior/dynamics but the proxy is redundant, below threshold, interval-crossing, condition-specific, or absorbed by standard RL controls. NARROW is not SRT support.

### NO-GO

Trigger when a major frozen condition holds: no X/S proxy separation; robust non-positive coefficient; ΔCV R² ≤0 without NRMSE improvement; Reach20/Emp5 absorbs the effect; one seed/cell drives it; post-hoc redefinition is needed; or protocol/leakage fails.

If fewer than 12 complete master seeds are available for resource reasons, thresholds remain unchanged and the decision is `INCONCLUSIVE / UNDERPOWERED` unless a protocol failure instead requires `UNINTERPRETABLE PROTOCOL`.

The frozen OLS-instability trigger is condition number above `1e8` or rank deficiency. The cluster bootstrap count is 2,000. The exact executable thresholds live in `configs/formal_locked.yaml` and are manifest-hashed.
