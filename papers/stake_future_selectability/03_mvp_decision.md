Decision: UNINTERPRETABLE PROTOCOL

# Stake–Future Selectability MVP Decision

## Scope

This is the frozen decision for the independent P4 Stake–Future Selectability MVP. It does not revise canonical `d`, `Ψ_f`, the Core axioms, or any consciousness/subjecthood claim. It does not revive or reinterpret the earlier selective-resynchronization NO-GO.

The full formal cohort completed: 12 master seeds, six paired branches per seed, and 72 A→B→C trajectories. The decision is `UNINTERPRETABLE PROTOCOL` because the preregistered environment-level T/S Reach20 validity gate failed in 8 of 48 coupled cells. The locked predictive results are also unfavorable, but they cannot be promoted to a clean scientific NO-GO because the structural manipulation did not pass its own frozen gate.

## Preregistered criteria

| Criterion | Frozen rule | Observed | Result |
|---|---|---|---|
| Structural manipulation | all validity checks pass | X 24/24 exact uncoupling; T/S Reach20 40/48 pass; T reset, S persistence, identity all pass | **FAIL** |
| S proxy separation | paired S−X `dV_CF_pre` mean > 0 and clustered 95% interval > 0 | mean 0.0004248; 95% interval [0.0001054, 0.0007443] | PASS |
| Positive predictive coefficient | M4 standardized β > 0 and seed-cluster 95% interval > 0 | β 0.0300; interval [−0.2610, 0.1924] | **FAIL** |
| Incremental grouped prediction | Δ leave-one-seed CV R² ≥ 0.03 | −1.0275 | **FAIL** |
| NRMSE improvement | relative reduction ≥ 3% | −13.04% (worsened) | **FAIL** |
| Not one-seed dependent | all leave-one-seed M4 `dV` coefficients positive | 3/12 were non-positive | **FAIL** |
| Severity robustness | both positive, or one positive and the other > −0.10 | low −0.1108; high 0.0797 | **FAIL** |
| Leakage/protocol integrity | no pre-C hash/schema/phase failure | 72/72 hashes verified; zero leakage errors | PASS |

Because the first gate failed, the correct top-level decision is not GO, NARROW, or a clean NO-GO. The frozen analysis nevertheless shows that even if the failed reachability gate were set aside, the primary bridge would meet multiple locked NO-GO conditions.

## Manipulation and bearer audit

- Low/high B-end median integrity was 0.85/0.65 in every X/T/S cell.
- X `Reach20(i=1)-Reach20(i=.7)` was exactly 0 in all 24 X cells.
- T/S Reach20 delta had a minimum of −0.0017854. Eight cells failed: all T/S×low/high branches for master seeds 4101 (0.0005412) and 4105 (−0.0017854).
- The corresponding Emp5 delta remained positive in every T/S cell; minimum 0.0923263. This cannot replace the frozen Reach20 gate.
- T performed 24/24 explicit B→C resets and began C at integrity 1.0.
- S performed 0/24 resets and preserved B-earned integrity exactly into C.
- All 72 branches preserved `agent_id` and `branch_id`; replacement count was zero.

The validity failure is therefore specific: the locked scalar Reach20 summary did not monotonically register the intended capability reduction for two master-seed layouts. It is not an identity, reset, leakage, or stored-integrity failure.

## Primary model comparison

| Model | Added block | LOSO CV R² | NRMSE |
|---|---|---:|---:|
| M0 | current performance/reward/state | −0.7895 | 1.3377 |
| M1 | homeostatic energy deviation | −1.1678 | 1.4724 |
| M2 | Reach20 + Emp5 controllability | −1.9193 | 1.7086 |
| M3 | generic PPO adaptation dynamics | −2.6984 | 1.9231 |
| M4 | `dV_CF_pre` | −3.7259 | 2.1739 |

Every added block worsened leave-one-master-seed prediction. M4 versus M3 changed CV R² by −1.0275 and NRMSE by +0.2508, a 13.04% relative worsening. Standard reward/current-state, homeostasis, and controllability baselines did not themselves predict well; more importantly, there was no residual predictive gain for the SRT-motivated proxy after those controls.

The full-cohort standardized `dV_CF_pre` coefficient was 0.0300. Its HC3 95% interval was [−0.0890, 0.1490], and its 2,000-resample master-seed-cluster bootstrap interval was [−0.2610, 0.1924]. The coefficient was negative after leaving out seeds 4105, 4107, or 4109. OLS condition number was 43.13, below the frozen `1e8` ridge trigger, so the preregistered ridge sensitivity was not invoked.

## Outcomes and secondary diagnostics

Mean `Q_C` was 0.15365 overall (SD 0.22904; range −0.0625 to 0.70625). Cell means ranged from 0.13698 (S-low) to 0.16823 (X-low). Paired clustered contrasts were small and interval-crossing:

- S−X `Q_C`: −0.00990, 95% interval [−0.09507, 0.07424];
- S−T `Q_C`: −0.00495, 95% interval [−0.08776, 0.07032];
- T−X `Q_C`: −0.00495, 95% interval [−0.07241, 0.04766].

The positive S−X `dV_CF_pre` separation therefore did not correspond to better future adaptation. `dV_CF_pre` was strongly associated with generic parameter-path length in a descriptive secondary analysis (Spearman ρ=0.675) but not with hazard contacts, preserved integrity, post-C Reach20, or stable incremental `Q_C` prediction. `dPi_CF_pre` agreed only modestly with `dV_CF_pre` (ρ=0.335).

The optional Fisher comparator was not implemented. It was preregistered as non-privileged and optional; its absence cannot be used to rescue or redefine the primary analysis.

## Negative and unexpected findings

1. The A/B-only pilot passed the Reach20 gate on all three pilot seeds, but two of twelve formal layouts failed it. The controlled slip/dropout intervention can sometimes increase the composite Reach20 scalar through stochastic exploration/entropy even while effective integrity is lower.
2. The pilot had no favorable S-over-X `dV_CF_pre` pattern, whereas the formal cohort produced a small positive separation. This demonstrates why the proxy difference alone is insufficient: it was not a stable predictor of the primary C outcome.
3. M0–M4 all had negative out-of-sample R², and each additional block worsened prediction. The experiment did not isolate a useful future-selectability signal at this sample/model granularity.
4. Persistent same-bearer damage did not improve C adaptation relative to X or T. The paired condition intervals all crossed zero.

## Protocol execution and deviations

- Initial smoke exposed a pre-lock probe bug: lowering integrity also capped probe energy. The probe was corrected so only the integrity input changes; the obsolete smoke tree was moved intact to `/tmp/stake_future_selectability_smoke_pre_probe_fix_20260808`, and smoke was rerun before pilot/formal.
- A pre-lock training-summary bug that reported `reward_sum=0` was corrected to sum real rollout rewards and covered by a regression test.
- The A/B-only pilot used seeds 1201–1203, constructed no C environment, and caused no change to candidate hazards, damage, budgets, proxy, direction, model blocks, thresholds, or formal seeds.
- Formal execution used two disjoint six-seed CPU shards. Sharding was implemented and manifest-hashed before formal execution; scientific budgets and grouping were unchanged.
- No code or scientific parameter changed after the formal lock. No formal cell was deleted, replaced, or selectively rerun.
- There were no post-lock scientific protocol deviations. The failed Reach20 validity gate is an observed protocol/manipulation failure, not an undocumented deviation.

## Reproducibility record

- Scientific lock commit: `686fdec44d02d3901b8d9f2c8c92e1e7979cdea7`.
- Manifest commit: `a7c467d5`.
- Formal manifest SHA-256: `d75e2d16781264fe712f2ea2d3ca9b2a9020b916f1c0a8bae2b5b2ca64cc1d3b`.
- Code-tree SHA-256: `286a5629bbc10fdc874c0e16116eb828a159d276c1784ed31bdcb24dee8d69a5`.
- Runtime: Python 3.12.11, Torch 2.7.1, Gymnasium 1.1.1, NumPy 2.2.6, pandas 2.3.0, SciPy 1.15.3, scikit-learn 1.7.0, statsmodels 0.14.4, PyArrow 20.0.0, macOS 15.7.4 arm64, Apple M1-class machine, 8 logical CPUs, deterministic CPU execution; MPS was available but unused.
- Formal A/B completion window: 2026-08-07 17:19:50–17:56:52 UTC.
- Formal C completion window: 2026-08-07 17:59:12–18:35:18 UTC.
- Local formal artifact tree: `Experiments/stake_future_selectability_mvp/outputs/formal/` (227 MB at decision time).
- Tracked compact artifacts: `outputs/formal/processed/`.

## Exact claim boundary

This result licenses only the following statement:

> In this PPO/grid architecture, the locked Reach20 manipulation gate was not stable across formal seeds, so the surrogate-stake → counterfactual-sensitivity → future-selectability bridge is not scientifically interpretable under the preregistered protocol. Independently, the observed `dV_CF_pre` did not add robust grouped prediction beyond standard RL baselines and satisfied multiple frozen NO-GO diagnostics.

It does not establish or refute canonical `d`, subjecthood, consciousness, suffering, or SRT as a whole. Nothing in the result overturns the separation `reward != homeostatic deviation != controllability != same-bearer stake`. What remains SRT-specific is only the unvalidated bridge question—whether a better structural manipulation and non-monotonicity-safe proxy for same-bearer consequence return could predict future selectability beyond standard controls. That question remains open; this MVP does not support it.
