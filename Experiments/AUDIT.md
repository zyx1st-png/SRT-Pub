---
id: SRT-EXP-ANCHORING-CHAIN-AUDIT-2026-07-17
type: audit_report
status: final_audit_v1
layer: lab
epistemic_layer: p4
claim_mode: audit
canonical: false
created: 2026-07-17
---

# Selective-anchoring computational chain — independent audit

**Date:** 2026-07-17. **Scope:** the five frozen experiment directories under
`Experiments/anchoring_*`. This audit adds documentation only; it does **not** modify any
frozen code, parameters, or results JSON, and does not amend any existing commit.

## Chain and commits

| Phase | Dir | Gate | Commit |
|---|---|---|---|
| Phase 1 double-well toy | `anchoring_double_well` | GO | `7d6fd039` |
| Phase 2 bandit feasibility | `anchoring_bandit_feasibility` | GO (feasibility) | `8d703838` |
| Phase 2b locked holdout | `anchoring_bandit_holdout` | **NO-GO** | `6d5f80d4` |
| Phase 2c controllability holdout | `anchoring_2c_controllability` | GO | `c653b170` |
| tiny-MDP confirmatory | `anchoring_tiny_mdp_confirmatory` | GO | `104baf9b` |

## Findings

### Clean (verified)
- **Reproducibility:** re-running the tiny-MDP holdout reproduced the committed
  `results_mdp_holdout.json` **bit-identically** (deterministic seeds).
- **No seed leakage:** every holdout seed set is disjoint from its own calibration set and
  from the other holdouts. Phase 2c and tiny-MDP share calibration seeds 1–5 (different
  models — acceptable). Holdout seeds: 2b 20000–20039, 2c 30000–30039, tiny-MDP 40000–40049.
- **Only `m` read at test (tiny-MDP):** `future_task(m, target, blocked, seed, c)` receives
  only `m` from formation; it references no `z`, outcome model `q`, counters, or eligibility
  traces; call sites pass only `act["m"]`/`yok["m"]`. Confirmed by code inspection and by
  `same-m/different-z = 0`.

### Issues
1. **Nothing was pushed (at audit time).** The entire branch
   `claude/selective-anchoring-paper-53f36f`, including all five experiment commits, was
   local-only; `origin/claude/selective-anchoring-paper-53f36f` did not exist. Resolved by
   the audit-repair push to a dedicated remote audit branch (see below).
2. **Manifest drift — `anchoring_bandit_feasibility/README.md`.** That README was
   intentionally edited (overclaim fix) in commit `6d5f80d4`, but its
   `freeze_manifest.json` was not regenerated, so the manifest's README hash is stale.
   Code and results JSON hashes still match. A `freeze_manifest_v2.json` is added here that
   supersedes the old manifest (README updated; code/results unchanged).
3. **memory-swap is mechanical / vacuous (tiny-MDP).** As implemented it compares
   `battery(yoked_m)` with `battery(yoked_m)` — the same memory to itself — giving 0 by
   construction. The alternative framing (active vs active-with-yoked-m) equals the main
   effect (0.374). Because the future is a deterministic function of `m`, memory-swap
   carries **no independent causal information**.
4. **memory-null is weak / architecture-bound (tiny-MDP).** 0.044 is the residual between a
   *uniform*-m future and a *near-zero*-m (yoked) future (yoked m ≈ [0.076, 0.066, 0.065]).
   It confirms that active's advantage needs its specific peaked m, but it lives inside the
   "future = f(m)" world and is not independent causal proof. `same-m/different-z = 0` is
   tautological (the future takes no z argument) but validly confirms the plumbing.
5. **Phase 2c bootstrap unit is seed × volatility, not pure seed.** `holdout2c.py` pools
   `d_ctrl` over `rows["high"] + rows["low"]` → 80 values (2 per seed). The tiny-MDP holdout
   bootstrap unit is the seed (50 values). **Retained as a known audit limitation; 2c is
   NOT re-run.**
6. **CI interpretation.** The very tight CIs (e.g., tiny-MDP macro-TV [0.3736, 0.3752])
   reflect **reproducibility of the frozen model across seeds**, because each per-seed
   statistic already averages over N = 400 agents. They are **not** construct-level
   confidence intervals and must not be read as such.

## Evidence weighting (applied to phase READMEs)
- **LOAD-BEARING:** (a) selection-specificity of the write-back — active ≫ yoked on
  controllability-z, data-driven (yoked ctrl-corr ≈ 0; |PE| baseline within equivalence);
  (b) the directional behavioral prediction in the tiny-MDP battery — aligned advantage
  vs blocked/novel stickiness (primary macro-TV + three direction gates).
- **PIPELINE VALIDATION ONLY (downgraded):** memory-null, memory-swap, same-m/different-z.
  They verify the identification plumbing (only m is read; m carries the future) and must
  not be cited as independent causal isolation.

## Final credibility judgment
Within the level of a **constructive, designed-model feasibility/confirmatory**, the chain
is **credible, reproducible, seed-clean, and only-m-read verified**. Its strongest claims —
data-driven **selection-specificity** and the **directional** behavioral reachable-set
signature — stand. The tiny-MDP causal battery (null/swap) is **downgraded to pipeline
validation**. None of this is empirical evidence about any natural system.
