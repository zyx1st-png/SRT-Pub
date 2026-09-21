---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PHASE1-DENSITY-SENSITIVITY-20260921
type: experiment_result
status: active
version: v0_1
record_stage: phase1_density_sensitivity_complete
date: 2026-09-21
post_primary_exploratory: true
layer: operations
epistemic_layer: experimental
claim_mode: evidence
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, Phase1, DensitySensitivity, Exploratory, Objectification, Modularity]
---

# Phase 1 density sensitivity — post-primary exploratory control

## 1. Scope and authority

This record is `POST-PRIMARY EXPLORATORY DENSITY CONTROL`. The preregistration froze deferred densities `K=0.02` and `K=0.10`, but did not freeze representative cells. The cell rule was declared before execution: S3 at G1/G2/G3 plus S1/S2/S3 at G1, for both Sleep and Anesthesia. K=0.05 is reused from the completed primary result and was not recomputed.

This record does not amend the Phase 1 preregistration or primary result. It does not run matched-component, multi-animal, connectivity-matched, or secondary analyses.

## 2. Execution and integrity

- Selected cells: 10; density records: 20; new graphs: 150; new Q trials: 30,000.
- Every new window has 200 finite Q values and an exact max-Q extraction.
- Same Python-louvain implementation, resolution, seed root and seed derivation as primary; K is omitted from the seed so K shares the seed list.
- Four-worker deterministic equivalence was already audited: exact per-seed Q equality and max-Q equality; speedup `3.796845x`.
- All `tie_excess_edges` values are zero.

## 3. Exact ΔQ

`ΔQ = mean(Q_max,target) − mean(Q_max,wake)`.

| Condition | Signal | Grain | K=0.02 | K=0.05 reused | K=0.10 |
|---|---|---:|---:|---:|---:|
| Sleep | S1 | G1 | +0.015726046 | +0.004569025 | +0.008206723 |
| Sleep | S2 | G1 | +0.039706243 | +0.014980149 | -0.004423700 |
| Sleep | S3 | G1 | +0.104262466 | +0.052495345 | +0.025732280 |
| Sleep | S3 | G2 | +0.047062783 | +0.023066442 | +0.003266627 |
| Sleep | S3 | G3 | -0.037173078 | -0.052091994 | -0.076028562 |
| Anesthesia | S1 | G1 | +0.065937274 | +0.068427699 | +0.070089904 |
| Anesthesia | S2 | G1 | +0.024494288 | -0.059921740 | -0.024575428 |
| Anesthesia | S3 | G1 | +0.143487375 | +0.110151716 | +0.066454864 |
| Anesthesia | S3 | G2 | -0.081431818 | -0.070158162 | -0.038414885 |
| Anesthesia | S3 | G3 | -0.073388672 | -0.110379515 | -0.147793781 |

## 4. Reversal across K

### Sleep

- Condition-level reversal persists at all three K values through the selected S3 grain axis: G1 remains positive while G3 remains negative.
- S3/G2 attenuates from `+0.047063` at K=0.02 to `+0.003267` at K=0.10.
- Classification: `DS-C` for the selected condition-level/grain reversal, with `DS-B`-like attenuation at G2.

### Anesthesia

- Condition-level reversal persists at all three K values: S3/G1 is positive while S3/G2 and S3/G3 are negative.
- S2/G1 changes from `+0.024494` at K=0.02 to `−0.059922` at K=0.05 and `−0.024575` at K=0.10.
- Classification: `DS-C` for selected condition-level/grain reversal; `DS-B` for the signal axis.

## 5. Signal sensitivity

| Condition | K | S1 G1 | S2 G1 | S3 G1 |
|---|---:|---:|---:|---:|
| Sleep | 0.02 | +0.015726046 | +0.039706243 | +0.104262466 |
| Sleep | 0.05 | +0.004569025 | +0.014980149 | +0.052495345 |
| Sleep | 0.10 | +0.008206723 | -0.004423700 | +0.025732280 |
| Anesthesia | 0.02 | +0.065937274 | +0.024494288 | +0.143487375 |
| Anesthesia | 0.05 | +0.068427699 | -0.059921740 | +0.110151716 |
| Anesthesia | 0.10 | +0.070089904 | -0.024575428 | +0.066454864 |

- Sleep G1 has no substantial positive-to-negative signal reversal across K; the original Sleep G2 signal reversal was outside this minimal density-control scope and remains unresolved.
- Anesthesia S1 remains positive at all K and S2 is negative at K=0.05/0.10 but positive at K=0.02; signal sensitivity is therefore not fully K-invariant.
- The zero-inflation caveat remains: S2 is approximately 98.7% zero in Sleep and 99.25% zero in Anesthesia globally, with higher target-window sparsity.

## 6. Grain sensitivity

| Condition | K | S3 G1 | S3 G2 | S3 G3 |
|---|---:|---:|---:|---:|
| Sleep | 0.02 | +0.104262466 | +0.047062783 | -0.037173078 |
| Sleep | 0.05 | +0.052495345 | +0.023066442 | -0.052091994 |
| Sleep | 0.10 | +0.025732280 | +0.003266627 | -0.076028562 |
| Anesthesia | 0.02 | +0.143487375 | -0.081431818 | -0.073388672 |
| Anesthesia | 0.05 | +0.110151716 | -0.070158162 | -0.110379515 |
| Anesthesia | 0.10 | +0.066454864 | -0.038414885 | -0.147793781 |

- Sleep: G1 positive and G3 negative at all K; the grain reversal persists. G2 becomes near-zero at K=0.10.
- Anesthesia: G1 positive and G2/G3 negative at all K; the grain reversal persists despite density changes.

## 7. Connectivity and graph-regime diagnostics

| Condition | Grain | K | N | Edges | Mean degree | Target components mean range | Target largest-component fraction range | Target isolated nodes mean range | Ties |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Sleep | G1 | 0.02 | 6920 | 478794 | 138.380 | 1.0–74.0 | 0.989–1.000 | 0.0–70.7 | 0 |
| Sleep | G1 | 0.05 | 6920 | 1196987 | 345.950 | 1.0–2.0 | 1.000–1.000 | n/a | 0 |
| Sleep | G1 | 0.10 | 6920 | 2393974 | 691.900 | 1.0–1.0 | 1.000–1.000 | 0.0–0.0 | 0 |
| Sleep | G2 | 0.02 | 692 | 4781 | 13.818 | 43.7–43.7 | 0.935–0.935 | 40.7–40.7 | 0 |
| Sleep | G2 | 0.05 | 692 | 11954 | 34.549 | 5.0–5.0 | 0.994–0.994 | n/a | 0 |
| Sleep | G2 | 0.10 | 692 | 23908 | 69.098 | 1.0–1.0 | 1.000–1.000 | 0.0–0.0 | 0 |
| Sleep | G3 | 0.02 | 173 | 297 | 3.434 | 52.0–52.0 | 0.692–0.692 | 49.3–49.3 | 0 |
| Sleep | G3 | 0.05 | 173 | 743 | 8.590 | 23.0–23.0 | 0.865–0.865 | n/a | 0 |
| Sleep | G3 | 0.10 | 173 | 1487 | 17.191 | 6.0–6.0 | 0.969–0.969 | 4.7–4.7 | 0 |
| Anesthesia | G1 | 0.02 | 3210 | 103008 | 64.179 | 3.0–21.0 | 0.994–0.999 | 2.0–20.0 | 0 |
| Anesthesia | G1 | 0.05 | 3210 | 257522 | 160.450 | 1.0–6.0 | 0.998–1.000 | n/a | 0 |
| Anesthesia | G1 | 0.10 | 3210 | 515044 | 320.900 | 1.0–6.0 | 0.998–1.000 | 0.0–5.0 | 0 |
| Anesthesia | G2 | 0.02 | 321 | 1027 | 6.399 | 182.0–182.0 | 0.414–0.414 | 176.0–176.0 | 0 |
| Anesthesia | G2 | 0.05 | 321 | 2568 | 16.000 | 76.0–76.0 | 0.751–0.751 | n/a | 0 |
| Anesthesia | G2 | 0.10 | 321 | 5136 | 32.000 | 16.0–16.0 | 0.953–0.953 | 15.0–15.0 | 0 |
| Anesthesia | G3 | 0.02 | 81 | 64 | 1.580 | 59.0–59.0 | 0.284–0.284 | 58.0–58.0 | 0 |
| Anesthesia | G3 | 0.05 | 81 | 162 | 4.000 | 49.0–49.0 | 0.407–0.407 | n/a | 0 |
| Anesthesia | G3 | 0.10 | 81 | 324 | 8.000 | 34.0–34.0 | 0.593–0.593 | 33.0–33.0 | 0 |

- Increasing K raises mean degree exactly as expected and generally reduces fragmentation, especially for G1/G2.
- K=0.02 is a distinct sparse regime: Sleep G2 target has about 43.7 mean components and Sleep G3 about 52; Anesthesia G2 target has 182 and G3 has 59.
- K=0.10 restores G1/G2 connectivity in many branches, but G3 remains fragmented, especially in Anesthesia.
- The density result weakens a simple “K=0.05 alone” explanation, but does not eliminate node-count/mean-degree or disconnected-graph implementation explanations.

## 8. Overall density result

`mixed DS-C / DS-B`.

The selected condition-level and S3 grain reversals persist across K, so the primary reversal is not specific to the K=0.05 threshold alone. However, signal behavior is less stable: Anesthesia S2 changes sign at K=0.02, and Sleep S3/G2 attenuates to near-zero at K=0.10. The result therefore supports robustness against a simple K-only explanation, not a clean isolation of objectification sensitivity.

## 9. What this rules out

- K=0.05 as the sole explanation for the selected S3 G1-versus-coarse reversal.
- Hidden threshold ties as the explanation; all new graphs have zero tie excess.
- A claim that the result is uniformly stable across signal representations.

## 10. What remains unresolved

- Fixed density still changes mean degree with N; this is not a matched-degree test.
- G2/G3 fragmentation and isolated nodes remain substantial, especially at K=0.02.
- S2 zero inflation and signal-processing effects remain plausible alternatives.
- Python primary Q has not been shown equivalent to native MATLAB/BCT Q for every density and reversal cell.
- The selected cells are exploratory and each condition still has one recording.

## 11. Next highest-information control

A predeclared connectivity-/mean-degree-matched graph control is the most direct next test of the remaining artifact explanation. If restricted to the original three routes, broader multi-animal/full-dataset replication is next. No such follow-up was started here.

## 12. Files and boundary

- Machine-readable record: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_DENSITY_SENSITIVITY_2026-09-21.json`.
- Runtime checkpoints remain under `.local/phase1_objectification/density_sensitivity/`.
- Primary result and preregistration were not modified.
- No raw data or large runtime files were added to Git.
