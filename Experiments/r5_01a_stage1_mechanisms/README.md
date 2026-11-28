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

## 1. Quick Reproduction & Cross-Environment Tolerance (`P2-04`)

From the repository root:

```bash
uv run python Experiments/r5_01a_stage1_mechanisms/run_all_verifications.py
```

- **Primary execution environment**: Python `3.13` (`uv`), `numpy 2.3.3`, `scipy 1.18.1` (exact bit-identical JSON regeneration verified locally; runtime ~9 seconds on CPU).
- **Independent replication environment (ChatGPT, independent re-implementation of core S2 & C2 equations; did NOT execute `run_all_verifications.py` bit-for-bit)**: Python `3.13`, `numpy 2.3.5`, `scipy 1.17.0`, including `C2` step-size convergence checks at `dt = 0.01, 0.005, 0.001`.
- **Expected cross-environment numerical tolerances**:
  - S2 fixed points, 5D eigenvalues, and augmented fold $\chi_c^{\text{dual}}$: agreement within `<= 1e-6` (Newton residual `< 1e-10`, central finite-difference Jacobian `eps = 1e-7`);
  - C2 equilibrium / post-perturbation errors across step sizes `dt ∈ {0.01, 0.005, 0.001}`: agreement within `<= 5e-4 rad` (e.g. `T3b`: `0.0882–0.0886 rad`);
  - S2 two-switch floating-point roundoff arm (`standard_float_roundoff`): saddle-escape timing depends on IEEE-754 roundoff trajectory and may vary across BLAS/hardware; therefore use `explicit_perturbation_1e-3_rad` vs `strict_antipodal_clamp` as the deterministic cross-platform benchmark (`P1-02`).
- **Determinism**: Fixed seeds (`seed=42` for utility-selective reset baseline, `seed=123` for `C2` background phase drift); all assertions inside `run_all_verifications.py` must pass and deterministically regenerate `results_calibrated.json`.

## 2. Package Inventory

| Path | Role | Notes |
|---|---|---|
| `run_all_verifications.py` | Calibrated master verification suite | Executes all calibrated modules (`divisive_normalization`, `S1`, `S2` full 5D Jacobian + augmented fold numerical certification + `A-1a/A-1b/A-2` counterexamples + **`P1-02` three-arm two-switch phase-perturbation control**, mature two-switch baselines, `C2` identical-initial-state transient-history differentiation + four-regime partner swap + **`P1-01` `T3c` extended to `T=1000` reconfiguration-delay check** + state-conditional analytical void-awakening check) with built-in assertions. |
| `results_calibrated.json` | Machine-readable calibrated output | Exact numerical outputs referenced in [SRT_R5_01A_STAGE1_MECHANISM_RESEARCH_ARCHIVE_2026-11-28.md](../../Operations/Proposals/SRT_R5_01A_STAGE1_MECHANISM_RESEARCH_ARCHIVE_2026-11-28.md). |
| `legacy_exploratory/round3_exploratory_2plus1.py` | Preserved Round-3 exploratory script | Original S1/S2 two-switch script prior to parameter reconciliation and $T=400$ extension. |
| `legacy_exploratory/round4_exploratory_paths_AB.py` | Preserved Round-4 exploratory script | Exposed the `Gamma=1.80` parameter mix-up (`a_p*m0=1.60` vs `1.445`), the ESC Form A vs Form B report typo, and the $T=400$ success-induced delayed extinction anomaly at $\chi=1.65$. |
| `legacy_exploratory/round5_exploratory_convergence.py` | Preserved Round-5 exploratory script | Original 3D restricted Jacobian + early `C2` test before Round-6 calibrations ($\lambda > 8 C_0$, full 5D phase-saddle proof, augmented fold certification, identical-initial-state transient-history test, and PR `#1173` `P1-01`/`P1-02` calibrations). |

## 3. What Independent Reviewers Should Verify First

1. **S2 scalar & 5D coupled spectra (numerical certification, `P2-03`)**: Confirm that at $\chi=1.65$ the single-aligned state ($\Phi_1=1,\Phi_2=0$) is stable in the 3D $(w_1,w_2,p)$ subspace (`max Re = -0.2739`) yet is a **5D saddle** due to positive phase eigenvalue `+0.5226`, whereas at $\chi=1.55$ the dual-aligned state is **5D locally asymptotically stable** (`max Re = -0.1190`).
2. **S2 coupled upper fold numerical certification & `P1-02` perturbation control**: Confirm `chi_c_dual = 1.58884564` via augmented `{F=0, det(J_3x3)=0}` (`lam_crit = 4.321e-11`, transversality `-0.319072`, quadratic coefficient `-2.125488`), and confirm `two_switch_phase_perturbation_control` separates `strict_antipodal_clamp` (`p=0.45161` at `T=400`) from `explicit_perturbation_1e-3_rad` (`t_dual_aligned=80.79`, `t_extinct=98.33`) and `standard_float_roundoff` (`t_dual_aligned=117.62`, `t_extinct=136.77`).
3. **A-1a vs A-1b ($\lambda > 8 C_0$)**: Confirm `A-1a` ($\lambda=2.5 < 8C_0$) has $d\Gamma/dW = +0.3317 > 0$ (level elevation only), whereas `A-1b` ($\lambda=12.0 > 8C_0, K=4.0$) sits at a 5D-stable equilibrium with $E_{C,W} = 1.0781 > 1$ and $d\Gamma/dW = -0.0481 < 0$.
4. **C2 identical-initial-state history bifurcation, `P1-01` viscosity delay (`T=1000`), and state-conditional void awakening (`P2-02`)**: Confirm `same_initial_state_H_sym_T1` vs `same_initial_state_H_asym_T1` start from identical `(0.50,0.50)` and `(0.60,0.60)`, match present output `U=0.6616` vs `0.6615` at `t=59.5`, yet diverge into symmetric vs asymmetric roles (`pA=0.6987` vs `0.0096`); confirm `T3c` recovers by `t=400/1000` (`err=0.0886, pA=0.6845`, demonstrating **reconfiguration delay**, not permanent failure); confirm `T3d` void awakening satisfies `S_max=0.00608 <= 0.012` for the current degraded interface state.
