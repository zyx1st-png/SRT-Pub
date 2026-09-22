---
id: SRT-NEURO-OBJECTIFICATION-SCALE-EXTERNAL-HAMBURG-ANESTHESIA-PREREGISTRATION-20260922
type: experiment_preregistration
status: frozen
version: v0_1
record_stage: phase3a_external_anesthesia_preregistration_frozen_before_q
date: 2026-09-22
layer: operations
epistemic_layer: experimental
claim_mode: hypothesis
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_AVAILABILITY_AUDIT_2026-09-22.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_PREREGISTRATION_2026-09-18.md
  - Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
tags: [Neuroscience, ExternalReplication, HamburgCA1, Anesthesia, Preregistration, ResultBlind]
---

# Phase 3A — Hamburg Wake↔Isoflurane external anesthesia replication preregistration

## 1. Scope and gate

This protocol is frozen before any Hamburg correlation, graph, Louvain, modularity, `Q`, `DeltaQ`, grain-shift, or condition-effect result is inspected. It authorizes only the primary external Anesthesia contrast:

```text
Wake ↔ Isoflurane
```

It does not authorize the Hamburg Sleep network analysis. Sleep remains a separate result-blind state-recovery gate and requires a separate Sleep network preregistration before any Sleep `Q` is calculated. Keta/Xyl and MMF are future secondary contrasts and are not part of this execution.

This is an external method replication/adaptation. It does not require numerical equality with Kiyooka et al. and cannot establish SRT, objectification, Bearer, One, consciousness, or a neural mechanism.

## 2. Locked data and provenance

```text
processed source:
  Formozov A, Chini M, Dieter A, Yang W, Pöpplau JA,
  Hanganu-Opatz IL, Wiegert JS (2022)
  Calcium Imaging and Electrophysiology of hippocampal Activity
  under Anesthesia and natural Sleep in Mice

processed DOI: 10.12751/g-node.lkx6kk
GIN repository: doi/Anesthesia_CA1
license: CC0 1.0 Public Domain Dedication
primary processed archive: not materialized as a full ZIP
raw imaging archive: not downloaded
operational data: per-recording Suite2p objects fetched on demand
```

The primary cell is defined before the external outcome is viewed:

```text
animals: 7
awake recordings: 39
isoflurane recordings: 49
recording duration: approximately 5 minutes each
```

All seven animals have both conditions in the metadata. The contrast is not session-paired. No artificial one-to-one awake/isoflurane pairing will be created.

## 3. Explicit graph-degree change

The availability audit listed `k̄ = 16` only as a feasibility candidate. It is not the primary rule.

```text
primary graph:
  connected maximum-spanning-tree backbone on abs(correlation)
  + strongest remaining abs-correlation edges
  + target mean degree k̄ = 4
```

The change is frozen before any Hamburg `Q` or `DeltaQ` inspection:

> `k̄` changed from the feasibility-audit candidate 16 to primary 4 before any external Q inspection, because the minimum coarse graph `N = 22` would make `k̄ = 16` approximately 76% dense (`16/21`). `k̄ = 4` gives the same degree target at every grain and an effective density of approximately `4/(N-1)`, about 0.19 at `N = 22`. This was selected from node-count/topology feasibility only. `k̄ = 8` and `k̄ = 16` are not primary analyses.

The graph is undirected and binary for Louvain. For a graph with `N` nodes, the exact target edge count is:

```text
M = round(N × 4 / 2) = 2N
```

The MST minimizes `1 - abs(correlation)` over the complete finite candidate graph. Ties in MST edge costs are resolved by the deterministic upper-triangle row-major edge order. Remaining edges are ranked by descending `abs(correlation)`; equal-weight ties are resolved by the same upper-triangle row-major order. Exactly `M` edges are retained. The MST edges are never duplicated in the ranked-addition set.

## 4. Signal and smoothing adaptation

Primary Hamburg signal:

```text
Suite2p spks.npy
  = processed deconvolved activity estimate
  → one frozen Gaussian temporal smoothing operation
  → S3-Hamburg
```

`spks.npy` is the nearest available Hamburg analogue to Kiyooka's S3, but it is not asserted to be numerically identical to Kiyooka's released `smoothed_spike` preprocessing. The result record must call this `S3-equivalent`, not `S3-identical`.

The Kiyooka Phase 1 protocol and pinned author script expose `kernel_size = 15` as the source smoothing-kernel label, while the released Kiyooka `.mat` file exposes the already smoothed variable rather than a reconstructible filter parameter. The same-author data description reports the Kiyooka wide-field calcium sampling rate as `7.65 Hz`. Therefore the source support is converted to physical time before mapping to Hamburg:

```text
source support = 15 / 7.65 s = 1.9607843137 s
Hamburg rate = 30 Hz
Hamburg support = round(1.9607843137 × 30) = 59 frames
Gaussian support = 59 frames, centered, truncated at the support boundary
Gaussian sigma = support / 6 = 9.8333333333 frames
boundary rule = reflected signal boundary
normalization = kernel weights sum to 1
```

The `support/6` sigma convention is an explicit protocol adaptation because the public Kiyooka source does not expose the original Gaussian sigma. It is frozen before external outcome inspection and is applied identically to every Hamburg recording, state, and grain. If `spks.npy` is already sampled at 30 Hz as documented for the Hamburg CA1 processed data, no resampling is performed.

## 5. ROI inclusion

Primary inclusion is the availability-audit C1-equivalent rule:

```text
iscell.npy[:, 0] == 1
```

No activity, correlation, modularity, or grain-outcome filter is permitted. A recording may be technically excluded only for a pre-defined failure of the required object or metadata integrity:

```text
missing/corrupt spks.npy, stat.npy, or iscell.npy;
non-finite or zero-length accepted signal;
non-finite or unrecoverable accepted ROI centroid;
missing animal/condition/recording identity;
insufficient frames for the frozen 300-second window.
```

Any such exclusion must be logged with the exact file, exception, and checkpoint state. It must not be replaced by a result-based exclusion.

## 6. Spatial grain construction

Let `N` be the number of accepted Suite2p cells in one recording. The same deterministic family is applied before any state comparison:

```text
G1 = every accepted neuron as one node
G2 = local groups with group size m2 = ceil(0.02 × N)
G3 = local groups with group size m3 = ceil(0.04 × N)
```

For implementation stability, `m2` and `m3` are bounded below by 2 and 4 respectively. This is equivalent to the frozen availability-audit proposal and avoids singleton `G2`/`G3` groups at the smallest recordings.

The grouping algorithm reuses the source-faithful deterministic local-clustering family:

1. recover the centroid of every accepted ROI from `stat.npy` (`med` when available, otherwise the mean of finite `xpix`/`ypix`);
2. order accepted ROIs by `(x + y, x, y, original ROI index)` using stable ordering;
3. take the first unassigned ROI as the next anchor;
4. select the nearest currently unassigned ROIs to that anchor until the group contains at most the frozen group size, with distance ties resolved by the same deterministic ROI order;
5. continue until every accepted ROI is assigned exactly once;
6. aggregate each group's smoothed activity and centroid by arithmetic mean.

Groups are formed once from the recording's accepted ROI geometry and reused across all complete windows and both condition labels. There is no state-specific regrouping, boundary wrap, or outcome-dependent group repair. The final partial group is retained; it is not discarded or merged after looking at network results.

## 7. Windowing

The frozen Kiyooka anesthesia source rule is `2900` frames. The source rate evidence above implies approximately `379.085 s`, which cannot fit inside the Hamburg processed recordings of approximately five minutes. Copying `2900` Hamburg frames would therefore silently shorten the physical window to approximately `96.7 s` and would not be a physical-time replication.

The Hamburg primary window is consequently frozen as the dataset-compatible fixed duration:

```text
Hamburg sampling rate: 30 Hz
window length: 300.000 s = 9000 frames
overlap: 0 s
windows per recording: one complete window
remainder: not used; no incomplete window is analyzed
minimum valid frames: 9000
```

This is a declared Hamburg time-window adaptation required by the source-duration/data-duration incompatibility. It is not selected from a Hamburg network outcome. No recording is subdivided into pseudo-replicate windows. If a recording does not contain 9000 valid frames, it is a technical exclusion under §5 and the exact exclusion is reported.

## 8. Modularity and randomization

For each recording, grain, and complete 300-second window:

```text
association: Pearson correlation across node time series
NaN/non-finite correlation: set to 0
diagonal: removed
edge score: abs(correlation)
network: binary connected MST-plus-ranked-edge graph
resolution: 1.0
Louvain repeats: 200
seed root: 12345
Q used for the window: maximum of the 200 finite Q values
```

The stable seed is derived from the fixed root, condition, animal, recording ID, signal, inclusion, grain, window index, and repeat index. The exact seed list is written to the runtime checkpoint. Parallel scheduling, if used, changes only execution order and not the graph, algorithm, seed list, repeat count, or max-Q rule.

All 200 Q trial values, the maximum and first-maximum index, graph diagnostics, and finite-value checks are retained per window. A non-finite Q or graph invariant failure is an implementation failure requiring stop-and-diagnose; it is not silently dropped.

## 9. Graph diagnostics and invariants

Every graph record must contain:

```text
N
M
target degree
achieved mean degree
effective density
components
largest component fraction
isolates
MST edges
rank-added edges
degree min/median/max
last-added edge weight
tie excess
```

The primary invariants are:

```text
components = 1
isolates = 0
largest component fraction = 1.0
M = 2N
achieved mean degree = 4.0
```

Failure of any invariant stops the affected checkpoint before result aggregation. It cannot be repaired by changing `k̄`, grain size, threshold, or seed.

## 10. Biological hierarchy and effect extraction

```text
window nested in recording
recording nested in condition
condition nested in animal
primary biological unit = animal
```

For each recording and grain, calculate the mean of the one complete-window `Q` value. For each animal and grain, average recording-level `Q` separately within Awake and Isoflurane:

```text
DeltaQ_g(animal) = mean(Q_iso,g over that animal's iso recordings)
                   - mean(Q_awake,g over that animal's awake recordings)

grain_shift(animal) = DeltaQ_G3(animal) - DeltaQ_G1(animal)
```

The primary animal-level report contains all seven trajectories `DeltaQ_G1`, `DeltaQ_G2`, `DeltaQ_G3`, all seven grain shifts, mean and median shift, a deterministic 10,000-resample animal bootstrap 95% percentile interval, sign consistency, and the number of categorical reversals. Windows and recordings are not treated as independent biological replicates. Any p-value with `n = 7` is auxiliary only.

The practical sign threshold is frozen:

```text
grain shift > +0.01: substantive positive
-0.01 <= grain shift <= +0.01: null
grain shift < -0.01: substantive negative
```

## 11. Classification

Per animal:

```text
EX-R-GRAIN-REVERSED:
  at least one grain shift > +0.01 and another < -0.01

EX-R-NEGATIVE-SHIFT:
  G3-G1 < 0 but no substantive sign reversal

EX-R-STABLE:
  same substantive direction across grains

EX-R-OTHER:
  mixed or null pattern not covered above
```

Dataset-level classification:

```text
EX-A: no reproducible negative grain shift
EX-B: animal-level negative grain shift replicates but categorical reversal inconsistent
EX-C: substantial grain reversal across multiple independent animals with overall negative grain-shift tendency
EX-D: heterogeneity prevents interpretable replication
```

`EX-C` is not forced. Classification is assigned after all 7 animals, 39 awake recordings, and 49 Isoflurane recordings are accounted for.

## 12. Checkpoint and fail-safe execution

Runtime files are outside canonical source and excluded from Git:

```text
.local/phase3a_hamburg/anesthesia_state.json
.local/phase3a_hamburg/anesthesia_execution.log
.local/phase3a_hamburg/anesthesia_commands.log
.local/phase3a_hamburg/anesthesia_environment.txt
.local/phase3a_hamburg/anesthesia_recording_inventory.json
.local/phase3a_hamburg/anesthesia_results/
```

The checkpoint is updated atomically after every file download, recording, grain, and window completion. A resumed run verifies the preregistration hash, source metadata, file checksum/shape, graph diagnostics, and seed list before reusing a result. It never repeats a completed valid window. A failed command preserves stdout/stderr and exit code and resumes from the nearest valid checkpoint.

Execution order is fixed:

```text
source/object smoke test
→ one awake and one isoflurane graph/Q smoke test
→ all eligible awake recordings
→ all eligible isoflurane recordings
→ animal aggregation and bootstrap
→ result record
```

No early stopping is allowed after a favorable or unfavorable animal. The full eligible set is required.

## 13. Scientific boundary

The only permitted primary comparison is the Hamburg animal-level Wake↔Isoflurane contrast under the frozen adaptations above. The output is an external objectification/scale stability result, not a test that proves SRT, consciousness, Bearer, One, Selection, or a universal neural law. After the Anesthesia result record and checks are written, the Anesthesia gate is complete and the programme must stop before any Hamburg Sleep `Q` calculation.

## 14. Source anchors

- Kiyooka Phase 1 frozen protocol: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_PREREGISTRATION_2026-09-18.md`.
- Pinned Kiyooka source: `.local/phase0_replication/source_repo/` at commit `90e1c7dc5823f9d413b1bddf5c649ec87d6598a3`; relevant source files include `scripts/calc_modularity.m`, `functions/get_close_clustering.m`, and `functions/spatial_coarse_graining.m`.
- Hamburg availability audit: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_AVAILABILITY_AUDIT_2026-09-22.md`.
- Hamburg processed dataset DOI: <https://doi.gin.g-node.org/10.12751/g-node.lkx6kk/>.
- Hamburg Scientific Data article: <https://pmc.ncbi.nlm.nih.gov/articles/PMC8964694/>.
- Same-author Kiyooka dataset descriptor reporting 7.65 Hz: <https://www.nature.com/articles/s41597-026-08202-2>.
- Suite2p output schema: <https://suite2p.readthedocs.io/en/latest/outputs/>.

