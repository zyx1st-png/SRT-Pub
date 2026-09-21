---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PHASE1-CONNECTED-GRAPH-CONTROL-20260921
type: experiment_result
status: active
version: v0_1
record_stage: phase1_connected_graph_control_complete
date: 2026-09-21
post_primary_exploratory: true
layer: operations
epistemic_layer: experimental
claim_mode: evidence
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, Phase1, ConnectedGraphControl, Objectification, Modularity, CoarseGraining, BCT, Reproducibility]
---

# Phase 1 connected-graph control

## SCOPE

Post-primary exploratory diagnostic. It does not amend the Phase-1 preregistration or promote an SRT-facing claim. Only the six mechanically selected S3 grain cells were run.

- Target mean degrees: `k̄=8` and `k̄=16`, frozen before Q inspection.
- Graph: maximum-spanning-tree backbone from absolute correlation weights, then strongest remaining non-MST edges until `M=round(N×k̄/2)`.
- Louvain graph is binary/unweighted; 200 Python repeats; fixed Phase-1 seed policy; 4 workers.
- Completed: 6 cells, 90 graph/windows, 18,000 Q trials.

No persisted hashable correlation matrices were available; the existing loader, coarse-graining and windows were rerun deterministically. The MST+ranked-edge rule is a connectivity-controlled diagnostic objectification rule, not the true network.

## SLEEP

`ΔQ = mean(Q_max,NREM) − mean(Q_max,Wake)`.

### k̄=8

| Grain | ΔQ |
|---|---:|
| G1 | +0.070298854 |
| G2 | +0.063259338 |
| G3 | -0.045847568 |

### k̄=16

| Grain | ΔQ |
|---|---:|
| G1 | +0.115485395 |
| G2 | +0.047953907 |
| G3 | -0.074769446 |

Classification: `CG-C` — substantive G1↔G3 reversal persists in connected graphs at both degree regimes.

## ANESTHESIA

`ΔQ = mean(Q_max,Isoflurane) − mean(Q_max,Wake)`.

### k̄=8

| Grain | ΔQ |
|---|---:|
| G1 | +0.184378322 |
| G2 | -0.032056172 |
| G3 | -0.096371552 |

### k̄=16

| Grain | ΔQ |
|---|---:|
| G1 | +0.156765778 |
| G2 | -0.048721307 |
| G3 | -0.118024834 |

Classification: `CG-C` — substantive G1↔G3 reversal persists in connected graphs at both degree regimes.

## GRAPH CHECK

- All 90 graphs connected: `PASS`.
- Isolates: `0` in every graph.
- Largest-component fraction: `1.0` in every graph.
- Edge count: exact `M=round(N×k̄/2)` in every graph.
- MST edge count: `N−1` in every graph.
- Tie excess: `0` in every graph.

Representative edge counts:

| Nodes | k̄=8 M | k̄=16 M |
|---:|---:|---:|
| 6920 | 27680 | 55360 |
| 692 | 2768 | 5536 |
| 173 | 692 | 1384 |
| 3210 | 12840 | 25680 |
| 321 | 1284 | 2568 |
| 81 | 324 | 648 |

Full per-cell/per-window diagnostics, including median/min/max degree and last-added weight, are in the JSON record.

## BCT CROSS-CHECK

Mechanically selected graphs: Sleep/Anesthesia S3 G1/G3, k̄=16, first Wake and first target window: 8 graphs total. Same saved adjacency was passed to Python and Octave/BCT; Octave performed no thresholding.

| Graph | Python mean Q | BCT mean Q | Python max Q | BCT max Q |
|---|---:|---:|---:|---:|
| `sleep_S3_G1_wake` | 0.735208663 | 0.734270138 | 0.737612052 | 0.737283509 |
| `sleep_S3_G1_target` | 0.842717639 | 0.842814403 | 0.843398893 | 0.843345867 |
| `sleep_S3_G3_wake` | 0.402962113 | 0.403290976 | 0.406173517 | 0.406173517 |
| `sleep_S3_G3_target` | 0.319156617 | 0.321645044 | 0.329803713 | 0.329803713 |
| `ane_S3_G1_wake` | 0.504589097 | 0.504261135 | 0.507951548 | 0.506574176 |
| `ane_S3_G1_target` | 0.702022599 | 0.702095011 | 0.705076625 | 0.705105390 |
| `ane_S3_G3_wake` | 0.197213804 | 0.197524244 | 0.207693901 | 0.206798459 |
| `ane_S3_G3_target` | 0.165481199 | 0.165078518 | 0.169182718 | 0.169182718 |

- Python state directions on the selected first windows: Sleep G1 positive / G3 negative; Anesthesia G1 positive / G3 negative.
- BCT state directions: same for both conditions.
- G1/G3 reversal agreement: `PASS`.
- BCT classification: `BCT-PASS`.
- Because 50 repeats per graph was used after a one-repeat timing smoke (200 projected clearly slow), this remains an implementation diagnostic only.
- A separate Python reload check found the same adjacency edge sets but non-identical fixed-seed Q vectors after MAT reload, attributable to NetworkX edge insertion order. This is recorded as Q-order sensitivity; it does not indicate adjacency mismatch.

## OVERALL

`CG-C`; BCT diagnostic `BCT-PASS`.

The S3 grain reversal persists after controlling both mean degree and disconnectedness, and the selected connected-graph qualitative inference is reproduced by the independent BCT implementation. The result still does not establish a causal role for grain or any SRT proposition.

### WHAT THIS WEAKENS

- A simple disconnected-graph/isolate explanation of the grain reversal.
- The combined fixed-density → mean-degree → fragmentation explanation as a sufficient account.

### WHAT REMAINS

- Network-size and finite-size modularity effects (`N_G1 >> N_G3`).
- Signal sparsity/correlation suitability.
- Single-recording and no cross-animal inference.
- Exact Q differences from Python graph-order sensitivity and Python-vs-BCT implementation differences.
- Native MATLAB execution remains unavailable.

### PAPER IMPLICATION

Stronger empirical increment candidate, but still post-primary exploratory and methodological; no theoretical promotion.

### NEXT HIGHEST-INFORMATION GATE

Multi-recording or multi-animal replication, if separately authorized. No additional graph rule was run here.

## FILES AND CHECKS

- Runtime state: `.local/phase1_objectification/connected_graph_control/connected_graph_control_state.json`.
- BCT adjacency files: `.local/phase1_objectification/connected_graph_control/bct_adjacencies/*.mat`.
- BCT output: `.local/phase1_objectification/connected_graph_control/bct_crosscheck.mat`.
- Integrity: 6/6 cells; 90/90 graph/windows; 18,000/18,000 finite Python Q values; all graphs connected; isolates zero; exact edge counts; 8 BCT graphs; 50 repeats/graph.
- Author source commit: `90e1c7dc5823f9d413b1bddf5c649ec87d6598a3`.
- Dataset SHA-256: `dd29cf6adda2e04745834525a94122076152c31f5136acbc39b57d4a9013638c`.
