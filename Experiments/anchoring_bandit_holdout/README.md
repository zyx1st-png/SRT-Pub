---
id: SRT-EXP-ANCHORING-BANDIT-HOLDOUT-README
type: experiment_readme
status: phase2b_locked_holdout_no_go
layer: lab
epistemic_layer: p4
claim_mode: experiment
canonical: false
created: 2026-07-16
---

# Phase 2b locked holdout — result: NO-GO (selection-specificity fails)

Locked replication of the Phase-2 bandit gate with **all parameters frozen** from the
committed feasibility run (`feasibility.py @ 8d703838`; zc=3.17073, kk=3.88219,
washout=200, recov_window=40). **No recalibration, no tuning.** 40 fresh holdout seeds
(20000–20039). Adds washout-length curves, an active-vs-yoked control, and a
cross-individual permutation control.

## Result: **NO-GO**

| test | result | verdict |
|---|---|---|
| Holdout: durable z (frozen params, new seeds) | 67% retained (min 67%) | PASS |
| Holdout: future early-adaptation diff | 0.241 ± 0.010, 100% of seeds positive | PASS |
| Holdout: null abolishes | mean \|diff\| = 0.010 | PASS |
| Holdout: swap reverses | 100% of seeds diff<0 | PASS |
| Permutation: effect follows z, not label | recovery~z = 0.76, recovery~label = 0.007 | PASS |
| **Active vs yoked: selection-specificity** | future 0.239 vs 0.238 (d=0.05); z-gap ratio 1.20 | **FAIL** |

**The gate fails on selection-specificity.** A yoked-observation group that receives the
same reward stream but has **no choice→consequence coupling** reproduces the entire
future effect (0.238 vs the active 0.239). So the slow variable `z`, as currently
mechanized (a leaky |prediction-error| integrator), is **dominantly a reward-stream
volatility tracker, not a selection-specific write-back.** There is a small genuine
selection signature — active-history stable-`z` (2.66) is lower than yoked stable-`z`
(2.90), because choice-contingency lets the active agent learn and reduce surprise — but
it is ~8% and does **not** translate into a differential future consequence.

Note: `gap_cohen_d_active_vs_yoked = 17.8` in the JSON is a **variance artifact** (each
gap is a mean over N=200 agents, so the standard error is tiny); it is deliberately NOT
used as a pass criterion. The load-bearing quantity is the future effect (d=0.05).

## Washout-length curves

| washout steps | 0 | 50 | 100 | 200 | 400 | 800 |
|---|---|---|---|---|---|---|
| z gap retained | 1.00 | 0.90 | 0.82 | 0.67 | 0.45 | 0.20 |
| future diff | 0.312 | 0.447 | 0.486 | 0.239 | 0.009 | 0.002 |

The inscription is durable over moderate unexpressive horizons and erodes for very long
ones (leaky slow variable).

## What this means for the program

- Durable inscription that **generalizes** (holdout) and is **causally carried by `z`**
  (permutation) is established.
- **Selective anchoring is NOT established**: the write-back is not selection-specific.
  For the SRT claim, selection-specificity is essential, so this is a real failure of the
  essential property — not a tuning issue.
- **Implication (redesign before tiny-MDP):** `z` must be formed from a signal that
  *requires* choice→consequence coupling — e.g., a **controllability / PE-reducibility**
  estimate (how much the agent's own choices reduce prediction error), which is low for a
  yoked agent by construction, rather than raw |prediction-error| magnitude which any
  passive observer of the same stream also accumulates.
- Per protocol, **the confirmatory tiny-MDP does NOT start** until a redesigned mechanism
  passes this holdout (including active > yoked).

## Files
`phase2b.py` -> `results_phase2b.json`; `tests/test_phase2b.py`; `freeze_manifest.json`.
Imports the frozen model from `../anchoring_bandit_feasibility/feasibility.py`. numpy only.
