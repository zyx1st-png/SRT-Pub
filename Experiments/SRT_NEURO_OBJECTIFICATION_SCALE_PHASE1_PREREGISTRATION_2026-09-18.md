---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PHASE1-PREREGISTRATION-20260918
type: experiment_preregistration
status: frozen
version: v0_1
record_stage: phase1a_preregistration_frozen_before_execution
date: 2026-09-18
layer: operations
epistemic_layer: experimental
claim_mode: hypothesis
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_REPLICATION_v0_1.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_MANIFEST_2026-09-17.json
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_AVAILABILITY_AUDIT_2026-09-18.md
tags: [Neuroscience, Phase1, Preregistration, Objectification, Stability, Exploratory]
---

# Phase 1 minimal objectification matrix — preregistration

## 1. Status and scope

This preregistration is frozen before any new Phase 1 state-effect calculation or inspection. It defines an exploratory benchmark only. It does not repair or upgrade the Phase 0 `R0-PARTIAL` status and cannot establish SRT, consciousness, Bearer, One, Selection, or a neural mechanism.

The benchmark-local question is:

```text
For the same source-selected recording, does the state contrast in network modularity
remain directionally and practically similar across predeclared signal and grain objects?
```

The primary contrasts are `Wake vs NREM` and `Wake vs Isoflurane`, analyzed separately. `NREM vs Isoflurane` is not primary.

## 2. Data lock

```text
source archive: mouse_data.zip
Zenodo DOI: 10.5281/zenodo.17667863
archive bytes: 1865754335
archive SHA-256: dd29cf6adda2e04745834525a94122076152c31f5136acbc39b57d4a9013638c
source code commit: 90e1c7dc5823f9d413b1bddf5c649ec87d6598a3
data root: existing Phase 0 materialization under .local/phase0_replication/source_repo/mouse_data/
```

No RIKEN CBS v3.0 data, new data download, or alternate archive is permitted for this matrix.

## 3. Frozen objectification matrix

### Signal

```text
S1 = dFF
S2 = spike
S3 = smoothed_spike
```

All three are direct released variables. No branch may be dropped because of an unobserved or later result.

### Cell inclusion

```text
C1 = all source-preserved released ROI rows
C2 = deferred; unavailable as an independent QC/activity-threshold branch
```

Sleep has 6920 released ROI rows; anesthesia has 3210. No invented activity threshold, variance filter, or state-dependent exclusion is allowed in the primary matrix.

### Grain

```text
G1 = single cells
G2 = source get_close_clustering with N_neighbors = 10
G3 = source get_close_clustering with N_neighbors = 40
```

For G2/G3, use the pinned `get_close_clustering.m` and `spatial_coarse_graining.m` logic. Aggregated signal and coordinates are arithmetic means of source cluster members. The selection of 10 and 40 is frozen from the source-defined neighbor sequence before Phase 1 results; it is not based on the known paper pattern.

### Graph

Primary graph construction is identical across all branches and states:

```text
association: pairwise Pearson correlation across time points
NaN correlation: set to 0
diagonal: set to 0
ranking: absolute correlation values on the upper triangle
network: undirected binary
density: K = 0.05
```

The density implementation follows the pinned source convention: sort upper-triangle values descending, choose the source-equivalent `floor(K * N*(N-1)/2)` order statistic, and retain all edges at or above that threshold. Ties may produce a density at or above the nominal K; this tie behavior is fixed and must be logged. No weighted graph, gamma tuning, or alternate graph implementation is allowed in the primary pass.

### Windows and state epochs

```text
sleep: source frame.used_frame cells; 1500 frames; cell 1 Awake, cell 2 NREM
anesthesia: source frame.used_frame cells; 2900 frames; cell 1 Awake, cell 2 Isoflurane
windowing: non-overlapping complete windows from each source frame cell
```

No window length, overlap, state relabeling, or state reclassification is permitted in the primary pass.

## 4. Modularity implementation and randomization

The Phase 1 primary implementation is Python, with the same implementation used for every matrix cell:

```text
Python: 3.14.0
networkx: 3.6.1
python-louvain: 0.16
function: community.community_louvain.best_partition
Q function: community.community_louvain.modularity
resolution: 1.0
optimization repeats: 200 per window
```

Each repeat receives a deterministic seed derived from the fixed root `12345`, condition, source recording, signal ID, inclusion ID, grain ID, window index and repeat index using a stable hash/seed derivation implemented in the runtime. Wall-clock time, process order and global mutable RNG state must not determine a seed.

For each window, retain all 200 Q values, the maximum Q, the first maximum index, node count, edge count, achieved density, connected-component summary and optimization spread. Only the maximum Q is used for the primary state contrast.

Octave is a later cross-check for the source-faithful S3/C1/G1 or closest available baseline branch. It is not mixed into the Python primary results and does not replace the frozen Python implementation.

## 5. Effect extraction and statistical unit

For each objectification cell and condition:

```text
Q_window = maximum of 200 optimization Q values
Q_state = mean(Q_window over complete windows in that source state cell)
DeltaQ = Q_unconscious - Q_wake
```

The biological unit is the source recording/session. The available raw signal files provide one recording per condition; therefore `n_recordings = 1` for Sleep and `n_recordings = 1` for Anesthesia in this first pass. Windows, neurons, edges, and optimization repeats are not independent biological replicates. No p-value, animal-level CI, or cross-animal consistency claim will be reported for this single-recording matrix.

The result tables must retain every window-level Q and the session-level `DeltaQ`.

## 6. Predeclared interpretation rules

These rules are benchmark-local and are not significance tests:

```text
practical null band: |DeltaQ| <= 0.01 Q units
material magnitude difference between branches: > 0.02 Q units
```

For each contrast, classify only after all primary cells are executed:

```text
DIRECTION-STABLE:
  all usable primary cells fall on the same side of the practical null band;

MAGNITUDE-SENSITIVE:
  all usable primary cells retain the same direction, but the branch range
  exceeds 0.02 Q units;

CONCLUSION-UNSTABLE:
  at least one usable cell is in the practical null band while another is
  outside it, without a declared directional reversal;

DIRECTION-REVERSED:
  at least one usable cell has DeltaQ > +0.01 and another has DeltaQ < -0.01;

INSUFFICIENT:
  data, graph or implementation diagnostics make a cell non-comparable.
```

The first applicable class in the order `DIRECTION-REVERSED`, `CONCLUSION-UNSTABLE`, `MAGNITUDE-SENSITIVE`, `DIRECTION-STABLE`, `INSUFFICIENT` is used, with exact cell scope reported. Crossing a p-value threshold is not a classification rule.

Because `n=1` per condition, all classifications are descriptive stability labels for this recording-level matrix, not population claims.

## 7. Diagnostics and fail-safe rules

Every cell must log:

```text
node count
edge count / achieved density
connected components
degree summary
NaN/constant/pathological signal checks
all window IDs
all 200 Q values or a lossless equivalent
```

Stop before continuing the matrix if the closest source-faithful baseline branch has an implementation-level direction contradiction, missing source frames, non-finite Q, or non-comparable graph construction. Save stdout/stderr, exit code and checkpoint state before diagnosis.

No branch may be removed because it is inconvenient or produces an unfavorable result. Any pathological branch remains recorded and is classified as `INSUFFICIENT` only under the predeclared diagnostics rule.

## 8. Deferred analyses

The following are not part of the primary freeze:

```text
K sensitivity at 0.02 and 0.10
C2 inclusion branch
window sensitivity
NREM vs anesthesia
matched-component analysis
full source seven-level grain sweep
```

They require a separately recorded extension or amendment before execution. After the primary matrix, stop and report the next gate rather than automatically expanding the search.

## 9. Reproducibility and checkpoint contract

Runtime files are kept under the ignored directory:

```text
.local/phase1_objectification/
```

At minimum, `phase1_state.json`, `commands.log`, `execution.log`, `preregistered_matrix.json`, per-cell results, diagnostics and the stability matrix are updated incrementally. A completed cell is flushed and checkpointed before the next cell starts. No raw MAT, ZIP, large NumPy array or runtime log enters Git.

This preregistration is the Phase 1A freeze. Results must be committed separately and must not amend this file after state effects are inspected, except for a purely mechanical typo correction explicitly recorded.
