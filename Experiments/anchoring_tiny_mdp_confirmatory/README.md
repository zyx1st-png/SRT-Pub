---
id: SRT-EXP-ANCHORING-TINY-MDP-CONFIRMATORY-README
type: experiment_readme
status: confirmatory_locked_holdout_go
layer: lab
epistemic_layer: p4
claim_mode: experiment
canonical: false
created: 2026-07-16
---

# tiny-MDP confirmatory — controllability write-back (result: GO)

Confirmatory for the Phase 2c controllability write-back. Unlike 2c (content-neutral
commitment proxy), the future reachable set is here estimated by **behavioral goal-arrival
probabilities in a unified task battery**, and consolidation can bring **both advantage
(aligned) and stickiness cost (blocked / novel)**.

## What is new vs Phase 2c (all locked corrections applied)

1. **Behavioral reachability, not an m threshold.** Future = a 2-step reach MDP (3
   corridors -> 3 goals) with a **non-arrival / timeout component**: terminal distribution
   `[P(G0), P(G1), P(G2), P(EMPTY)]`. Blocked corridor forces re-selection under a move
   budget; perseveration times out (EMPTY).
2. **Bidirectional battery** (equal-weight): aligned (goal = history corridor -> advantage),
   blocked (history corridor blocked -> stickiness / timeout), novel (non-history goal ->
   stickiness). Roles counterbalanced across seeds.
3. **Only m carried.** The future resets state and Q (matched initial action distribution)
   and reads **only m**; formation q, z, counters, traces are never read. m acts as a
   BOUNDED retention pull on the evolving policy, so the initial action distribution is
   matched and trajectories diverge over episodes by m alone. (Tests confirm the future is
   a deterministic function of m: same-m/different-z and memory-swap are exactly 0.)
4. **Primary GO = macro-TV of goal-reachability vectors**, not commitment or accuracy.
5. **Observable external-action sham** with self- vs external-attribution (mechanism gate).

## Locked holdout result: **GO** (50 fresh seeds 40000-40049, 10,000 paired bootstrap)

Thresholds locked before calibration: `Delta_min = 0.15`, `eps_TV = 0.05`, 95% CI.
Calibration (seeds 1-5) tuned only env/mechanism params to avoid saturation.

| check | result | pass |
|---|---|---|
| P1 primary: macro-TV 95% CI lower **> Delta_min=0.15** | mean 0.374, CI [0.374, 0.375] | ✓ |
| DIR aligned: active advantage (P(Gh) diff, CI lower > 0) | +0.221, CI [0.219, 0.223] | ✓ |
| DIR blocked: active stickiness (P(EMPTY) diff, CI lower > 0) | +0.582, CI [0.580, 0.583] | ✓ |
| DIR novel: active stickiness (P(Gnovel) diff, CI upper < 0) | −0.278, CI [−0.280, −0.276] | ✓ |
| NULL memory-null within ±0.05 | 0.044, CI [0.043, 0.045] | ✓ (tightest) |
| NULL same-m/different-z within ±0.05 | 0.000 | ✓ |
| SWAP memory-swap follows donor within ±0.05 | 0.000 | ✓ |
| sham mechanism gate: self ≈ 0, ext > 0 (not GO-deciding) | self −0.015, ext +0.143 | ✓ |

Manipulation check: yoked ctrl-corr = −0.001 (yoke breaks A→O).

## Evidence weighting (post-audit, 2026-07-17)

An independent audit (see repo-root `AUDIT.md`) re-classified the evidence in this GO:

- **LOAD-BEARING (genuine, non-mechanical):**
  1. **Selection-specificity is data-driven.** Active memory peaks on the history corridor
     (z_ctrl high) while yoked stays diffuse (z_ctrl ≈ 0) — and this arises from the data,
     not the definition: the yoke decouples action from outcome, giving ctrl-corr = −0.001
     (A ⊥ O verified). The |PE| baseline (Phase 2b) reproduces active ≈ yoked, so this is
     not generic volatility learning.
  2. **Directional behavioral prediction.** The m difference yields aligned **advantage**
     (+0.221) and blocked/novel **stickiness cost** (+0.582 P(∅); −0.278 P(Gnovel)) — a
     non-trivial, bidirectional behavioral signature, not merely a divergence magnitude.
     The primary macro-TV (0.374) and these three direction gates carry the result.
- **PIPELINE VALIDATION ONLY (not independent causal evidence):**
  - **memory-swap = 0 is mechanical/vacuous** — as implemented it compares `battery(yoked_m)`
    with `battery(yoked_m)` (the same m to itself); the alternative framing equals the main
    effect. Because the future is a deterministic function of m, swap carries no independent
    information.
  - **same-m/different-z = 0** is tautological (the future takes no z argument). It validly
    confirms the plumbing — *only m is read at test* — but is not a causal discovery.
  - **memory-null = 0.044** is a weak, architecture-bound confirmation (uniform-m vs
    near-zero-m futures), not independent causal proof.
  These three are retained as **pipeline validation** (they verify the identification
  plumbing) and must not be cited as independent causal isolation.

## Honest caveats

1. **Designed model, not empirical data.** This is a constructive confirmatory: it shows
   the controllability-write-back architecture *can* produce a selection-specific,
   behaviorally-measured reachable-set restructuring with the identification controls. It
   does not show any natural system does this.
2. **memory-null = 0.044 is the tightest margin** (inside the locked ±0.05). It is not ~0
   because the ablation replaces active's memory with a *uniform* m while the yoked memory
   is *near-zero* — two slightly different "diffuse" states under the bounded pull. The
   effect still collapses 0.374 → 0.044 (88%). Using yoked's own m as the null would give
   exactly 0; uniform is the more principled ablation, so the honest, stricter number is
   reported.
3. **CIs are very tight** because each seed's macro-TV averages over N=400 agents (small
   seed variance). The CI is on the across-seed mean.
4. **same-m/diff-z and memory-swap are exactly 0** — by construction, since the future is a
   deterministic function of (m, seed). This is the intended confirmation that m is the
   sole future-carrier, not an independent effect to interpret.
5. **Aligned P(Gh)=0.86** is interior but on the high side; blocked/novel are clearly
   interior. Saturation was avoided (no arm at 1.0).

## Files
`model_mdp.py`, `calibrate_mdp.py`, `config_mdp_frozen.json`, `holdout_mdp.py` ->
`results_mdp_holdout.json`, `tests/test_mdp.py`, `freeze_manifest.json`. numpy only.
Run: `python3 tests/test_mdp.py && python3 holdout_mdp.py`.
