---
id: SRT-EXP-ANCHORING-DOUBLE-WELL-README
type: experiment_readme
status: phase1_frozen
layer: lab
epistemic_layer: p4
claim_mode: experiment
canonical: false
created: 2026-07-16
---

# Anchoring double-well toy (Phase 1, frozen)

Identification-clean toy for **selective anchoring**. Fast state `x`, slow (plastic)
state `z`; `z` is written by the selection episode. This is a **constructive
existence + measurement-instrument proof** (see point 6), not an empirical discovery
that anchoring occurs in any natural system.

## What is and is not claimed (read this first)

1. **P and W_sel are bidirectionally dissociable / non-equivalent — NOT statistically
   independent.** The result is that all four `P x W_sel` cells can be occupied, so
   neither quantity implies the other. Over the parameter sweep they are in fact
   correlated; we make no independence claim.
2. **LatentInscription is a selection-episode-scale, short-term latent inscription.**
   It shows low `P` with high `W_sel` *measured at the end of the selection episode*.
   It is **not yet a durable** low-`P` / high-`W_sel` state: because `z` here tracks the
   fast state, an off-target write erodes (`z_after_int=+0.74 -> z_final=-5.53`).
   Producing a *durable* written-but-unexpressed disposition is deferred to Phase 2.
3. **RoughenWrite is a nonspecific rule-change negative control.** It has the largest
   `W_global` (kernel KL/JS/TV) but `W_sel ~ 0`: the transition rule changes a lot, but
   not in a way that specifically favors the selected macrostate.
4. **Cost conclusions are limited to the two costs actually measured here**, `J_ext`
   (external control effort) and `J_write` (slow-variable dissipation). We do not claim
   anything about "cost in general". Finding: neither `J_ext` nor `J_write` tracks
   `W_sel` (the nonspecific control has the *highest* `J_write`).
5. **"Matched present" means the fast state / observable endpoint is matched exactly**
   (`x0` identical). It does **not** mean the full system state is identical — `z`
   (the history-carrying slow state) differs by construction. That difference is the
   entire point.
6. **Phase 1 is positioned as a constructive existence + measurement-instrument proof:**
   it shows the constructs `P`, `W_global`, `W_sel` are separable and provides portable
   measurement instruments (matched-state kernel divergence; `h+`/`h-` counterfactual
   `W_sel`; exact endpoint matching). It does not establish that any natural system
   exhibits selective anchoring.

## Constructs

- **P** — persistence: does the fast state hold `M+ = {x>0}` after support withdrawal.
- **W_global** — any transition-rule change: kernel KL/JS/TV vs the condition's own
  pre-landscape, over uniform / pre-occupancy / mixture reference measures.
- **W_sel** — *selection-specific* write-back: functional difference between the
  landscape written by the actual selection history `h+` (push toward M+) and a matched
  counterfactual history `h-` (equal magnitude, opposite direction). Functionals:
  stationary occupancy of `M+`, escape barrier, committor; measured from `z_after_int`.
  Auxiliary: `M+`-basin-localized JS/TV.
- **J_ext / J_write** — see point 4.

Selective anchoring is **P > 0 AND W_sel > 0** (not W_global, not cost).

## Result summary (5 seeds, n=4000, sd<=0.005)

| condition | P_surv | W_sel(occ) | W_global KL | J_ext | J_write | cell |
|---|---|---|---|---|---|---|
| A_transient       | 0.000 |  0.000 | 0.000 | 17.3 | 0.00 | P- W_sel- |
| PreExistingWell   | 1.000 |  0.000 | 0.000 | 17.3 | 0.00 | P+ W_sel- |
| RoughenWrite      | 0.000 | -0.000 | 7.976 | 17.3 | 6.70 | nonspecific neg-control |
| LatentInscription | 0.000 | +1.000 | 0.008 | 17.3 | 2.10 | P- W_sel+ (episode-scale) |
| C_anchor          | 1.000 | +1.000 | 0.035 | 17.3 | 0.28 | P+ W_sel+ |
| B_clamp           | 1.000 held / 0.000 after withdrawal | 0.000 | 0.000 | 86.4 | 0.00 | clamp control |

Phase diagrams (`sweep.py`): each cell occupies a contiguous region (anchor 49, latent
56, null 11, pre-existing ~62 cells), not a single tuned point.

Matched-present -> different-future (`matched_future.py`): present-state gap = 0.0000
(exact fast-state match), raw future P(M+) = 1.000 (anchor) vs 0.000 (naive), reachable
sets disjoint, future KL=20.7 / JS=0.693 / TV=1.000.

## Files & run order

```bash
python3 tests/test_toy.py        # 6 identification/sanity tests
python3 run_dissociation.py      # -> results_dissociation.json  (~2 min)
python3 sweep.py                 # -> results_sweep.json         (~2 min)
python3 matched_future.py        # -> results_matched_future.json
```

`config.json` holds all params + the locked seeds (dissociation 11-15, sweep 21,
matched-future 99). `freeze_manifest.json` holds sha256 of every input+result.
Dependencies: numpy only.
