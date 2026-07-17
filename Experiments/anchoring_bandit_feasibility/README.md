---
id: SRT-EXP-ANCHORING-BANDIT-FEASIBILITY-README
type: experiment_readme
status: phase2_feasibility_go_superseded_by_2b_2c
layer: lab
epistemic_layer: p4
claim_mode: experiment
canonical: false
created: 2026-07-16
---

# Phase 2 contextual-bandit feasibility gate (durable selective anchoring)

Tests whether a **two-timescale agent** can exhibit what the potential toy could not:
a **durable** written disposition that is not currently expressed in behavior, yet
changes the future learning distribution under identical future conditions.

## Architecture

- Fast `Q[2]` — action = softmax(Q/temp). **The policy depends on Q only.**
- Slow `z` — a leaky reinforcement-driven consolidation variable. **`z` does NOT enter
  the policy.** `z` only sets the effective learning rate of *future* updates:
  `alpha_eff = lr_lo + (lr_hi-lr_lo)*sigmoid(kk*(z-zc))`.

Phases: formation (two natural histories -> different `z`, never hand-set) -> match
(reset `Q` exactly; `z` carried) -> washout (behavior exercised, no reinforcement) ->
future (identical reversal schedule for all; `z` **frozen** so any divergence is caused
by the inscribed `z`).

## Gate result: **GO** (seed 101, N=400/regime)

| gate | result |
|---|---|
| G1 z separable by history | vol 3.74 vs stable 2.61, gap 1.13, **d=8.84** |
| G2 exact fast-state match | reset touches Q only; z bit-unchanged; action KL=0 |
| G3 **durability** | gap 1.13 -> 0.76 after unexpressive washout (**67% retained**, still d=8.84) |
| G4 **future divergence (z frozen)** | early post-reversal recovery vol=0.396 vs stable=0.215, d=1.81, **sign-stable 5/5** |
| G5 null abolishes | diff +0.008 |
| G5 swap follows z | diff -0.176 (**sign flips**) |
| G5 dose-response monotone | Spearman 0.96 |
| G5 random-slow-variable control | diff +0.006 (**no history-label effect**) |

The most critical GO condition is met: the inscription **persists while unexpressed**
(G3) and **causally shifts the future reachable/learning distribution** (G4 + G5).

## Scope and caveats (read before citing)

1. **This is a feasibility gate, not the confirmatory result.** It shows the two-timescale
   mechanism *can* produce durable, causally-effective inscription. The confirmatory run
   (tiny MDP, not started) must reproduce the future-reachable-set divergence.
2. **`zc` is calibrated post-formation** (centered between the two regimes' `z`) so the
   learning-rate gate is not saturated. This is legitimate for feasibility but is a
   readout calibration; the confirmatory run must fix `zc`/`kk` **a priori**.
   **null / swap / dose-response are MECHANISM-CHANNEL checks** (they verify `z` is the
   causal channel). **The random-slow-variable control only shows that a random `z`
   produces no history-label effect; it does NOT rule out calibration artifactuality.**
   Ruling out calibration artifactuality requires an a-priori `zc` (the confirmatory
   tiny-MDP), not this gate. See `../anchoring_bandit_holdout/` for the locked holdout
   that tests generalization and selection-specificity (result: **NO-GO** on
   selection-specificity).
3. **Washout = behavior exercised with no reinforcement contingency**, so the
   reinforcement-driven `z` receives no input and leaks slowly (both regimes by the same
   factor, so the *separation* is retained, not created). A stronger durability test
   (persistence through an active but z-irrelevant task) is deferred to the confirmatory run.
4. **`z` is frozen during the future phase** for the causal battery, to isolate the effect
   of the inscribed value from future `z` drift.

## Files

`feasibility.py` -> `results_feasibility.json`; `tests/test_bandit.py`;
`freeze_manifest.json`. numpy only. Run: `python3 tests/test_bandit.py && python3 feasibility.py`.
