---
id: SRT-NEURO-OBJECTIFICATION-SCALE-MULTIRECORDING-PREREGISTRATION-20260921
type: experiment_preregistration
status: frozen
version: v0_1
record_stage: multirecording_preregistration_frozen_before_deltaq
date: 2026-09-21
layer: operations
epistemic_layer: experimental
claim_mode: hypothesis
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
post_primary_replication: true
tags: [Neuroscience, MultiRecording, Replication, Objectification, Scale, ConnectedGraph, Preregistration]
---

# Multi-recording grain replication — preregistration

## 1. Scope and freeze boundary

This is a result-blind replication of the strongest current empirical observation from the Phase 1 benchmark: the S3 grain-dependent state contrast changes direction between G1 and a coarser grain in the source-selected recordings.

This record is frozen before any new recording-level `DeltaQ` is calculated or inspected. It does not amend the Phase 1 preregistration, primary result, density control, mean-degree control or connected-graph control. It does not authorize matched-component analysis, NEURAL34, new graph families, new signal families, MATLAB replication or SRT-facing theoretical promotion.

The replication question is:

> Does grain-dependent state-contrast instability recur across independent recordings and biological animals under one predeclared connected, mean-degree-matched graph construction?

The primary analysis is complete-data, not an early-stop analysis. Every eligible recording is retained regardless of the eventual state contrast.

## 2. Dataset identity and materialization lock

Primary source:

```text
RIKEN CBS Data Sharing Platform
accession DOI: 10.60178/cbs.20260708-001
collection folder: Large-scale two-photon calcium imaging dataset
collection folder id: 12a35d86-b6e1-4cc0-8e69-ab0cbb6ef010
processed release README version: v2.0 (analysis dataset), release date 2026-03
license: CC BY 4.0
```

The accession is the current RIKEN CBS collection identified at intake. The collection README calls the processed analysis release `v2.0`; this version-label discrepancy is retained rather than silently relabeled as the Zenodo v1-style subset.

The frozen processed file set is the ten recording files listed below. The CBS API does not expose file SHA-256 values; the expected byte size and immutable CBS file ID are therefore frozen here, and a local SHA-256 for every materialized file must be recorded in the pre-execution audit manifest before any `DeltaQ` computation.

| Condition | Animal | Session/recording | CBS file | CBS file ID | Expected bytes |
|---|---|---|---|---|---:|
| Sleep | mouse01 | mouse01_sleep | `mouse01_sleep.mat` | `1f786027-c4b2-4ac9-8449-24c0cfb434db` | 658474258 |
| Sleep | mouse02 | mouse02_sleep | `mouse02_sleep.mat` | `b266f5ee-cc1d-4a47-9d41-29655a7c3967` | 1093789677 |
| Sleep | mouse03 | mouse03_sleep | `mouse03_sleep.mat` | `3191b169-1d10-4807-9284-edfd96f6c44e` | 1197235306 |
| Sleep | mouse04 | mouse04_day1_sleep | `mouse04_day1_sleep.mat` | `8d84d7ac-b4c8-4208-9e5c-c3a4605d3e31` | 1625754526 |
| Sleep | mouse04 | mouse04_day2_sleep | `mouse04_day2_sleep.mat` | `105e2c10-8a9a-4cd2-9c76-411cf673ec28` | 2254368168 |
| Sleep | mouse05 | mouse05_sleep | `mouse05_sleep.mat` | `ed06e6f2-7485-493e-8d32-d01e0d13aec9` | 1263665343 |
| Anesthesia | mouse03 | mouse03_ane | `mouse03_ane.mat` | `1616a6b6-edec-4637-bea9-bca9c0a95848` | 1123058079 |
| Anesthesia | mouse05 | mouse05_ane | `mouse05_ane.mat` | `5b5f67db-2bd0-43ae-8b4f-eb50138e6057` | 1079340853 |
| Anesthesia | mouse06 | mouse06_ane | `mouse06_ane.mat` | `e1dd0560-3486-45e6-a086-e2c1bfb2bb6e` | 563929318 |
| Anesthesia | mouse07 | mouse07_ane | `mouse07_ane.mat` | `ffdc68e6-fbb4-43f5-81e2-a8271a50819a` | 363189208 |

The local audit must record actual bytes, SHA-256, download URL, download timestamp, MAT format and all eligibility fields before analysis. The earlier Zenodo `mouse_data.zip` single-recording subset remains a prior Phase 0/1 source and is not silently substituted for this expansion.

## 3. Eligibility and exclusion rules

Eligibility is frozen without reference to any state effect, modularity magnitude, direction or reversal:

1. The file is one of the ten frozen processed recording files above.
2. The recording declares a compatible condition (`sleep` or `ane`) and can be assigned to the filename-derived animal/session hierarchy.
3. S3 is directly available as the release's smoothed deconvolved signal (`spike_smoothed`; a source-compatible alias may be accepted only if documented in the audit).
4. ROI centroid coordinates are present, finite, two-dimensional, and row-aligned with S3.
5. The released state annotation and/or `frame.used_frame` contains the required Wake and target state epochs. `frame.used_frame` is authoritative for the primary windows; no state relabeling is allowed.
6. Both required states have at least one complete source-sized window: 1500 frames for Sleep Wake/NREM and 2900 frames for Anesthesia Wake/Isoflurane.
7. Essential MAT metadata are readable and the required arrays are not corrupt, have compatible dimensions, and contain finite usable values under the declared signal checks.

All files satisfying these criteria enter the primary analysis. A file failing a criterion is retained in the inventory as `R-INSUFFICIENT`/technical exclusion with the exact non-result-based reason. No recording may be excluded because its `DeltaQ`, sign, magnitude, reversal status or agreement with the motivating finding is unfavorable.

## 4. Data hierarchy and objectification

```text
biological unit: animal
session unit: recording/session nested within animal
```

Sleep has six candidate sessions from five animals (`mouse04` has two sessions). Anesthesia has four candidate sessions from four animals. Sleep and Anesthesia remain separate cohorts and are not pooled into one contrast. If the same animal appears in both condition packages, condition-specific summaries remain separate; cross-condition pairing is not a primary analysis.

Signal and cell inclusion are fixed:

```text
signal: S3 = spike_smoothed / released smoothed deconvolved estimate
cell inclusion: C1 = all released ROI rows supplied in the processed file
```

The optional release `nonzero_ROI` activity flag is not used as a new result-dependent exclusion. It may be inventoried, but it is window-specific and cannot silently replace C1.

Grains are fixed:

```text
G1 = single cells
G2 = source-compatible spatial coarse-graining, N_neighbors=10
G3 = source-compatible spatial coarse-graining, N_neighbors=40
```

For G2/G3, use the pinned author's `get_close_clustering` and `spatial_coarse_graining` logic, adapted only by an external v2.0 field-name/path wrapper if needed. Aggregated signal and coordinates are arithmetic means of source cluster members. No parcel, cluster or ROI selection may use state contrasts.

## 5. State epochs and windows

```text
Sleep: Wake -> NREM; non-overlapping complete windows of 1500 frames
Anesthesia: Wake -> Isoflurane; non-overlapping complete windows of 2900 frames
```

Use the released `frame.used_frame` state-specific frame vectors when present. They define the source-compatible state epochs and are not recomputed from observed signal values. State labels are used only for audit and reporting; no reclassification, overlap change or window-length tuning is permitted.

## 6. Primary graph construction

One primary graph rule is frozen before any new recording-level result:

```text
association: Pearson correlation across time points on each window
NaN/Inf correlation: 0
diagonal: removed
edge ranking: absolute correlation, unique undirected upper-triangle edges
graph: binary and unweighted
target mean degree: k_bar = 16
target edge count: M = round(N * 16 / 2)
connectivity: maximum-spanning-tree backbone from absolute-correlation weights
additional edges: strongest remaining non-MST edges until exactly M
repair: none beyond the MST backbone
```

The MST is built from `1 - abs(correlation)` and must contain `N-1` edges. The additional-edge ordering uses a deterministic stable upper-triangle tie rule. Every primary graph must satisfy:

```text
components = 1
largest component fraction = 1.0
isolates = 0
edge count = M
achieved mean degree = 2M/N
```

If a recording cannot satisfy these graph diagnostics under the frozen rule, it is a technical implementation failure and is not repaired with another graph family. `k_bar=8` is a deferred secondary robustness branch, not part of this primary freeze.

## 7. Louvain implementation and reproducibility

```text
Python 3.14.0
NetworkX 3.6.1
python-louvain 0.16
best_partition + modularity, resolution=1.0
200 repeats per window
max-Q is the window statistic
4 workers with deterministic fixed seeds
```

The fixed seed root is `12345`. The seed is derived by the existing stable BLAKE2b policy, with a unique recording ID added to the cell identity:

```text
stable_seed(12345, recording_id, condition, S3, C1, grain_id,
            state_index*1000 + window_index, repeat_index)
```

Process order, wall-clock time and global mutable RNG state must not determine seeds. Save all 200 Q trials, maximum Q, first-max index, graph diagnostics and window identifiers for every usable window. Windows, graphs, neurons and Louvain repeats are not biological replicates.

## 8. Primary contrasts and recording-level classification

For each eligible recording separately:

```text
DeltaQ_g = mean(Q_max,target windows at grain g)
           - mean(Q_max,Wake windows at grain g)
```

Sleep target is NREM; Anesthesia target is Isoflurane. No Sleep/Anesthesia pooling is primary.

The frozen practical threshold is `±0.01 Q units`. Classification is applied only after all three grain values for a recording are complete, with technical insufficiency first and then the following deterministic order:

```text
R-GRAIN-REVERSED:
  at least one grain > +0.01 and another grain < -0.01

R-STABLE-POSITIVE:
  all three grains > +0.01

R-STABLE-NEGATIVE:
  all three grains < -0.01

R-ATTENUATED:
  no substantive reversal and all usable grain contrasts share one direction,
  but at least one grain lies inside the ±0.01 band

R-UNSTABLE:
  mixed/near-null pattern not meeting the reversal rule

R-INSUFFICIENT:
  missing/corrupt data, inadequate source windows, non-finite Q, or graph/
  implementation failure under the frozen diagnostics
```

The classification is descriptive and does not replace continuous analysis.

## 9. Continuous and animal-level summaries

For every recording retain:

```text
DeltaQ_G1, DeltaQ_G2, DeltaQ_G3
grain_shift = DeltaQ_G3 - DeltaQ_G1
```

For every animal, summarize its sessions without treating sessions as independent animals. Report, separately for Sleep and Anesthesia:

```text
number of animals, sessions and recordings
recording-level classification counts and fractions
animal-level summaries
median and mean grain_shift
paired G1/G3 differences
sign consistency for grain_shift < 0
animal-level bootstrap confidence intervals where identifiable
```

The analysis does not treat windows, neuron pairs, graph instances or optimization repeats as biological replicates. With small animal counts, scatterplots, paired differences, medians and bootstrap intervals take priority over a single p-value. Any inferential model must respect sessions nested within animals.

## 10. Replication outcome labels

Sleep and Anesthesia are classified independently:

```text
MR-A:
  grain reversal / negative grain shift does not replicate

MR-B:
  directional grain shift replicates, but categorical reversal is inconsistent

MR-C:
  substantial grain reversal replicates across multiple independent animals/
  recordings

MR-D:
  dataset heterogeneity or implementation prevents clean replication
```

The label is assigned from the complete eligible dataset and technical audit, never from an early subset.

## 11. Fail-safe and stopping rules

The runtime must checkpoint after each recording, cache preprocessing/correlation intermediates, flush all Q trials and graph diagnostics, and resume without recomputing completed recordings. One failed recording must not block independent recordings; failure details are saved and the remaining eligible files continue where safe.

There is no result-based early stop. The primary replication stops only after every eligible recording has been processed or after a documented technical impossibility/data corruption/resource failure that prevents completion. No new graph family, signal family, matched-component analysis, dataset or theoretical interpretation starts automatically after this replication.

## 12. Reporting boundary

Even an `MR-C` result may only support the bounded methodological statement that reproducible grain-dependent inferential instability is observed across independent neural recordings under a controlled graph construction. It does not prove SRT ontology, Selection, Bearer, One, consciousness or a consciousness mechanism. Network modularity and state labels remain downstream measurement objects.
