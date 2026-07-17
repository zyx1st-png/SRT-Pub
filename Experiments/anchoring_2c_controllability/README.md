---
id: SRT-EXP-ANCHORING-2C-CONTROLLABILITY-README
type: experiment_readme
status: phase2c_locked_holdout_go
layer: lab
epistemic_layer: p4
claim_mode: experiment
canonical: false
created: 2026-07-16
---

# Phase 2c — action-attributable controllability write-back (result: GO)

Reverses the Phase 2b NO-GO. The write-back signal is no longer accumulated
prediction error (which any passive observer of the same stream forms), but
**how much the agent's own chosen action adds to outcome prediction** — a
selection-specific controllability signal that is ~0 for a yoked agent by
construction of the data (not of the estimator).

## Architecture (corrections applied)

- **Separate variables** — `Q` (fast policy, drives the action) / `q` (outcome model,
  drives the score, updated AFTER scoring, separate from `Q`) / `z` (slow controllability,
  gates consolidation STRENGTH only, never the current action) / `m` (path memory, the
  consolidated CONTENT; the future reachable set is a function of `m`).
- **Score** (correction 1): reference-measure pointwise log-likelihood ratio, computed
  with the pre-update `q` against a FIXED reachable-action reference measure `mu` (uniform):
  `r_t = log q(o_t|a_t) - log sum_a mu(a) q(o_t|a)`. Not the average of logs; not called
  the acting-policy conditional MI. Also reported: structural index
  `C_mu = sum_a mu(a) KL(Bern(q[a]) || Bern(qbar_mu))`.
- **Negative baseline**: `z_pe` = leaky integral of `|o - Q[a]|`, which should again give
  active ~ yoked (reproduce 2b).
- **Consolidation** (correction 2): `m += alpha_m * relu(z_gate) * (greedy(Q) - m)`; `z`
  gates strength, `m` holds content. Future reachable set = commitment (narrowness of the
  m-biased policy), a **content-neutral** readout so a strongly-consolidating baseline
  commits just as much — only a selection-specific `z` leaves the yoked memory diffuse.

## Anti-circularity (how active>yoked is NOT written into z)

The estimator is identical for every agent and never sees the group label. `z_ctrl` is
high only where the agent's own action carries outcome information (A->O edge exists).
The manipulation check confirms the yoke breaks that edge: ctrl-corr(chose-good, reward)
= -0.000 for yoked vs +0.27 for active. So active>yoked emerges from each agent's data,
not from the definition.

## 2x2 design

External volatility (**outcome noise**, fixed good arm; low = 0.85/0.15, high = 0.65/0.35)
x action-consequence coupling (active / master-yoked). Volatility is operationalized as
noise, not reversals, so the active agent always has stable content to consolidate (a
reversal destabilizes the active content too and collapses the contrast). `sham-action`
is deferred to v2 (needs the self/external dual-attribution model; omitted here rather
than duplicating a hidden yoked).

## Locked holdout result: **GO** (frozen params, 40 fresh seeds 30000-30039)

| check | result | pass |
|---|---|---|
| P2 primary: paired active-yoked commitment (ctrl) > Delta_min=0.20, CI_lo>0 | 0.570, 90% CI [0.559, 0.581] | ✓ |
| N1 negative baseline: `|PE|` paired diff within ±0.15 equivalence | 0.087, CI [0.082, 0.091] | ✓ |
| P1 z-formation coupling effect sign-stable (ctrl) | per-vol +0.26 / +0.93; z^PE ≈ −0.07 | ✓ |
| manipulation: yoked I(A;O) proxy ≈ 0 (independent action RNG) | ctrl-corr = −0.000 | ✓ |
| causal null-z collapses active commitment | 0.997 → 0.000 | ✓ |
| causal swap-m follows memory | active-with-yoked-m = 0.427 = yoked | ✓ |

Structural `C_mu`: active 0.121 > yoked 0.022.

## Evidence weighting (post-audit, 2026-07-17)

Per repo-root `AUDIT.md`: the **load-bearing evidence** here is the **selection-specificity**
of the write-back — active ≫ yoked on controllability-z (data-driven: yoked ctrl-corr ≈ 0),
with the |PE| baseline within the equivalence bound (not selection-specific). The
**null-z / swap-m checks are PIPELINE VALIDATION only**: because the future readout is a
deterministic function of m, swap-m following the memory donor is largely mechanical, and
null-z collapsing commitment confirms the z→m plumbing rather than providing independent
causal isolation. Do not cite null-z/swap-m as independent causal proof.

## Scope and caveats

1. **Bandit-level feasibility, not confirmatory.** The future reachable set is a
   content-neutral commitment proxy; the full reachable-set semantics (behavior under a
   battery of new tasks in a state/action space) is for the tiny-MDP confirmatory.
2. **Design decisions were fixed during CALIBRATION (seeds 1-5) before freezing**: the
   commitment metric, noise-based volatility, the z/m split, and the pre-registered
   thresholds (Delta_min, eps, CI). The holdout on fresh seeds tests generalization of the
   frozen design; it passed.
3. **The |PE| baseline residual (0.087) is small but not exactly 0** — active has stable
   content, yoked noisy — hence judged by an equivalence bound, not equality.
4. **Yoked residual commitment (0.427)** comes from near-zero-gate noise; the effect is
   measured as active−yoked (0.57), which is conservative.
5. `sham-action` (self vs external attribution) deferred to v2.

Per protocol, tiny-MDP does NOT start on this result alone — it awaits confirmation.

## Files
`model2c.py`, `calibrate.py`, `config2c_frozen.json`, `holdout2c.py` ->
`results_2c_holdout.json`, `tests/test_2c.py`, `freeze_manifest.json`. numpy only.
Run: `python3 tests/test_2c.py && python3 holdout2c.py`.
