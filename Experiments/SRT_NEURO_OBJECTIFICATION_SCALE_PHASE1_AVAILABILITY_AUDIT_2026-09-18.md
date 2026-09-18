---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PHASE1-AVAILABILITY-AUDIT-20260918
type: experiment_audit
status: active
version: v0_1
record_stage: phase1a_availability_audit_complete
date: 2026-09-18
layer: operations
epistemic_layer: experimental
claim_mode: evidence
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_MANIFEST_2026-09-17.json
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_R0B_RESULT_2026-09-17.md
tags: [Neuroscience, Phase1A, AvailabilityAudit, Objectification, Reproducibility]
---

# Phase 1A availability audit — 2026-09-18

## Scope and stopping boundary

This record covers availability and implementation audit only. It was completed before the Phase 1 preregistration freeze and before any new state-effect inspection.

No new `Q`, `Wake - NREM`, `Wake - Anesthesia`, effect-size, p-value, branch-ranking or SRT-support result was calculated or inspected.

Phase 1 remains exploratory because Phase 0 is `R0-PARTIAL`.

## Dataset and integrity

The official Phase 0 archive was reused from the existing local materialization; it was not redownloaded.

```text
archive: mouse_data.zip
DOI: 10.5281/zenodo.17667863
bytes: 1,865,754,335
SHA-256: dd29cf6adda2e04745834525a94122076152c31f5136acbc39b57d4a9013638c
integrity: matches Phase 0 record; ZIP CRC previously PASS
root: .local/phase0_replication/source_repo/mouse_data/
```

The root contains `sleep_data.mat`, `ane_data.mat`, 33 released result MAT files, and an empty `modularity_res/` directory. The RIKEN CBS v3.0 dataset was not used.

## Signal availability

All three planned signal representations are directly released in both MAT files; no signal reconstruction is required for availability:

| Branch | Sleep | Anesthesia | Status |
|---|---:|---:|---|
| `S1 = dFF` | `6920 x 19000`, double | `3210 x 19562`, double | directly released |
| `S2 = spike` | `6920 x 19000`, double | `3210 x 19562`, double | directly released deconvolved activity estimate |
| `S3 = smoothed_spike` | `6920 x 19000`, double | `3210 x 19562`, double | directly released Gaussian-smoothed estimate; source correlation input |

The provenance labels follow the pinned author's `load_data_demo.m` and source data-flow comments. Signal branches are retained because they are available, not because any state result has been inspected.

## Cell inclusion availability

The released `ROIs` struct contains `atlasID` and `Centroid` only. The raw MAT files and pinned source snapshot do not expose an independent QC mask, activity-threshold mask, or an executable published inclusion rule.

The preregistered first pass therefore uses:

```text
C1 = source-preserved released ROI population
    sleep: 6920 rows
    anesthesia: 3210 rows

C2 = unavailable as an independently reconstructible branch; deferred
```

`C1` is an inherited release population, not an independently verified QC label. No artificial activity threshold or post-hoc exclusion is introduced to manufacture a second branch. Any future C2 sensitivity branch requires a separate pre-results amendment.

## Geometry and grain availability

Coordinates are available as `ROIs.Centroid` (`N x 2`, double) and atlas identifiers as `ROIs.atlasID` (`N x 1`). The pinned source provides deterministic `get_close_clustering.m` and `spatial_coarse_graining.m`, with source neighbor levels:

```text
[2, 5, 10, 20, 40, 80, 160]
```

The preregistered minimal grain matrix uses `G1 = single cells`, `G2 = N_neighbors=10`, and `G3 = N_neighbors=40`. The source aggregation is the arithmetic mean of member signals and coordinates.

## State and window availability

The source `frame.used_frame` cells are available and will be used without reclassification. The source `load_data_demo.m` documents cell 1 as Awake and cell 2 as NREM or Anesthesia.

```text
sleep:    used_frame lengths 9146 / 5660; source window 1500 frames; 6 / 3 complete windows
ane:      used_frame lengths 15528 / 2933; source window 2900 frames; 5 / 1 complete windows
```

The sleep `state.state` vector contains the documented labels `0`, `0.5`, `1`, and `2`, plus five small transition values at state boundaries. These values will not be used to redefine epochs; the released `used_frame` cells remain authoritative for the primary pass. Anesthesia contains the documented `0` / `1` state coding.

## Biological-unit limitation

The two raw signal files are source-selected recordings rather than a multi-animal raw-signal panel. The raw files do not contain a dedicated animal/session ID field; the source context and matching `basic_info` entries identify the selected population as mouse label 5 for both condition packages. Thus the primary matrix can be executed as a single-recording exploratory comparison per condition, but it cannot support cross-animal consistency, animal-level confidence intervals, or biological generalization across animals for all signal branches.

This limitation is frozen into the preregistration and will not be repaired by treating windows, neurons, edges, or Louvain repeats as independent animals.

## Runtime audit

```text
primary: Python 3.14.0 isolated environment
packages: numpy 2.5.3; scipy 1.18.1; h5py 3.16.0; networkx 3.6.1;
          python-louvain 0.16; pandas 3.0.6; statsmodels 0.15.0;
          matplotlib 3.11.2
cross-check: GNU Octave 11.3.0; statistics 1.9.3; datatypes 1.4.2
MATLAB: unavailable
```

Python is the Phase 1 primary implementation. Octave is reserved for a later key baseline cross-check. Wolfram Engine is not used as a MATLAB substitute.

## Audit outputs

Machine-readable audit and resumable runtime state are retained under the ignored local directory:

```text
.local/phase1_objectification/availability_audit.json
.local/phase1_objectification/phase1_state.json
.local/phase1_objectification/data_inventory.txt
.local/phase1_objectification/environment.txt
```

The next authorized step is the separately frozen preregistration. Execution remains blocked until that freeze is committed.
