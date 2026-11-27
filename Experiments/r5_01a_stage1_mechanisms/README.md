---
id: SRT-EXP-R5-01A-STAGE1-README
type: experiment_readme
status: draft
canonical: false
layer: experiments
epistemic_layer: experimental
claim_mode: evidence
ai_do_not_use_for_definition: true
created: 2026-11-28
updated: 2026-11-28
baseline_commit: 246c24756
dependency:
  - Operations/Proposals/SRT_R5_01A_STAGE1_MECHANISM_RESEARCH_ARCHIVE_2026-11-28.md
  - Operations/Proposals/SRT_R5_RESEARCH_PROGRAM_PROPOSAL_2026-11-27.md
tags: [R5-01A, Reproducibility, S1, S2, C2, Bifurcation, RoleReallocation, NonCanonical]
---

# R5-01A Stage-1 Reproducible Mechanism Package

> **Scope & Hard Guard**: Non-canonical Stage-1 computational archive for `R5-01A` (based on `main@246c24756`). This package does **not** complete `R5-01A`, does **not** modify any canonical owner or `STATUS.md`, does **not** open `R5-02`, and leaves all `HOLD`s, 25 sealed `validation_holdout` records, and frozen paper science packages untouched.

## 1. Quick Reproduction

From the repository root:

```bash
uv run python Experiments/r5_01a_stage1_mechanisms/run_all_verifications.py
```

- **Environment verified**: Python 3.13 (`uv`), `numpy 2.3.3`, `scipy 1.18.1`.
- **Runtime**: ~7 seconds on CPU.
- **Determinism**: Fixed seeds (`seed=42` for utility-selective reset baseline, `seed=123` for `C2` background phase drift); all assertions inside `run_all_verifications.py` must pass and deterministically regenerate `results_calibrated.json`.

## 2. Package Inventory

| Path | Role | Notes |
|---|---|---|
| `run_all_verifications.py` | Calibrated master verification suite | Executes all five calibrated modules (`divisive_normalization`, `S1`, `S2` full 5D Jacobian + fold non-degeneracy + `A-1a/A-1b/A-2` counterexamples, mature two-switch baselines, `C2` identical-initial-state transient-history differentiation + four-regime partner swap + analytical void-awakening check) with built-in assertions. |
| `results_calibrated.json` | Machine-readable calibrated output | Exact numerical outputs referenced in [SRT_R5_01A_STAGE1_MECHANISM_RESEARCH_ARCHIVE_2026-11-28.md](../../Operations/Proposals/SRT_R5_01A_STAGE1_MECHANISM_RESEARCH_ARCHIVE_2026-11-28.md). |
| `legacy_exploratory/round3_exploratory_2plus1.py` | Preserved Round-3 exploratory script | Original S1/S2 two-switch script prior to parameter reconciliation and $T=400$ extension. |
| `legacy_exploratory/round4_exploratory_paths_AB.py` | Preserved Round-4 exploratory script | Exposed the `Gamma=1.80` parameter mix-up (`a_p*m0=1.60` vs `1.445`), the ESC Form A vs Form B report typo, and the $T=400$ success-induced delayed extinction anomaly at $\chi=1.65$. |
| `legacy_exploratory/round5_exploratory_convergence.py` | Preserved Round-5 exploratory script | Original 3D restricted Jacobian + early `C2` test before Round-6 calibrations ($\lambda > 8 C_0$, full 5D phase-saddle proof, augmented fold non-degeneracy, and identical-initial-state transient-history test). |

## 3. What Independent Reviewers Should Verify First

1. **S2 scalar & 5D coupled spectra**: Confirm that at $\chi=1.65$ the single-aligned state ($\Phi_1=1,\Phi_2=0$) is stable in the 3D $(w_1,w_2,p)$ subspace (`max Re = -0.2739`) yet is a **5D saddle** due to positive phase eigenvalue `+0.5226`, whereas at $\chi=1.55$ the dual-aligned state is **strictly 5D asymptotically stable** (`max Re = -0.1190`).
2. **S2 coupled upper fold non-degeneracy**: Confirm `chi_c_dual = 1.58884564` via augmented `{F=0, det(J_3x3)=0}`, with simple zero eigenvalue `4.321e-11`, transversality `-0.319072`, and quadratic coefficient `-2.125488`.
3. **A-1a vs A-1b ($\lambda > 8 C_0$)**: Confirm `A-1a` ($\lambda=2.5 < 8C_0$) has $d\Gamma/dW = +0.3317 > 0$ (level elevation only), whereas `A-1b` ($\lambda=12.0 > 8C_0, K=4.0$) sits at a 5D-stable equilibrium with $E_{C,W} = 1.0781 > 1$ and $d\Gamma/dW = -0.0481 < 0$.
4. **C2 identical-initial-state history bifurcation & void awakening**: Confirm `same_initial_state_H_sym_T1` vs `same_initial_state_H_asym_T1` start from identical `(0.50,0.50)` and `(0.60,0.60)`, match present output `U=0.6616` vs `0.6615` at `t=59.5`, yet diverge into symmetric vs asymmetric roles (`pA=0.6987` vs `0.0096`), and reproduce `T3a` lock-in, `T3b` dedifferentiation rescue (`err=0.0882`), and `T3d` void awakening (`pA=1.8140`, `S_max=0.00608 <= 0.012`).
