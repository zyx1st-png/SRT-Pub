---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PHASE1-RESULT-20260919
type: experiment_result
status: active
version: v0_1
record_stage: phase1b_primary_matrix_complete
date: 2026-09-19
layer: operations
epistemic_layer: experimental
claim_mode: evidence
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_AVAILABILITY_AUDIT_2026-09-18.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_PREREGISTRATION_2026-09-18.md
  - Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
tags: [Neuroscience, Phase1, PrimaryMatrix, Objectification, Modularity, CoarseGraining, Reproducibility]
---

# Phase 1 primary result — objectification–scale benchmark

## 1. Scope and stopping boundary

This record reports the frozen Phase 1 primary matrix after the separately
completed result-blind compute audit. It does not amend the preregistration,
run sensitivity analyses, or make an SRT-facing theoretical claim.

The primary matrix is descriptive at the source-recording level. Sleep and
anesthesia each contribute one source recording; windows, neurons, edges and
Louvain repeats are not independent biological replicates. No p-value,
animal-level confidence interval, or cross-animal inference is reported.

The preregistered classes are benchmark-local labels only:

- `DIRECTION-REVERSED`: at least one cell has `DeltaQ > +0.01` and another has `DeltaQ < -0.01`.
- `CONCLUSION-UNSTABLE`, `MAGNITUDE-SENSITIVE`, `DIRECTION-STABLE`, and `INSUFFICIENT` were not selected because the first applicable class in the preregistered order was `DIRECTION-REVERSED` for both contrasts.

## 2. Execution identity

- Branch: `experiments/neuro-objectification-phase1-20260918`.
- Phase 1 preregistration commit: `60d5df13273080212f69e0af4a6d7e02486ed80e`.
- Pinned author source commit: `90e1c7dc5823f9d413b1bddf5c649ec87d6598a3`.
- Dataset archive: `mouse_data.zip`, SHA-256 `dd29cf6adda2e04745834525a94122076152c31f5136acbc39b57d4a9013638c`.
- Python primary runtime: Python `3.14.0`, NumPy `2.5.3`, SciPy `1.18.1`, NetworkX `3.6.1`, python-louvain `0.16`.
- Primary execution: 4-worker fork scheduler after a result-blind performance audit; fixed graph, fixed seed derivation, 200 repeats, and max-Q rule unchanged.
- MATLAB: unavailable. Octave is recorded below as a compatibility cross-check, not native MATLAB execution.

## 3. Compute audit gate

The baseline convergence audit used the saved 200 Q trials and did not rerun
the baseline. `N=25`, `50`, and `100` failed the all-window `<=1e-4` rule;
`N=200` was the smallest value passing both the `<=1e-4` and `<=1e-6`
all-window checks. Therefore no repeat-count amendment was proposed.

The one-graph serial versus 4-worker benchmark produced exact per-seed Q
equivalence and the same max-Q. Wall-clock time was `6562.757 s` serial and
`1728.476 s` parallel, a `3.796845x` speedup. The primary matrix therefore
kept 200 repeats and used the audited runtime parallelization.

## 4. Primary matrix completion

All 18 frozen cells completed. Sleep cells contain 9 windows (6 Wake, 3
NREM); anesthesia cells contain 6 windows (5 Wake, 1 Isoflurane). Every
window has 200 finite Q trials, graph diagnostics, and a persisted max-Q.

`DeltaQ = mean(Q_max,target windows) - mean(Q_max,Wake windows)`.

| Condition | Signal | Grain | Wake Q mean | Target Q mean | DeltaQ | Effective density |
|---|---|---:|---:|---:|---:|---:|
| sleep | S1 dFF | G1 | 0.352711669 | 0.357280694 | 0.004569025 | 0.050000000000 |
| sleep | S1 dFF | G2 | 0.371391818 | 0.316945843 | -0.054445975 | 0.049998745221 |
| sleep | S1 dFF | G3 | 0.499374603 | 0.404342730 | -0.095031872 | 0.049939507998 |
| sleep | S2 spike | G1 | 0.219407353 | 0.234387502 | 0.014980149 | 0.050000000000 |
| sleep | S2 spike | G2 | 0.321821788 | 0.314424526 | -0.007397262 | 0.049998745221 |
| sleep | S2 spike | G3 | 0.498000781 | 0.473618284 | -0.024382497 | 0.049939507998 |
| sleep | S3 smoothed_spike | G1 | 0.294596517 | 0.347091862 | 0.052495345 | 0.050000000000 |
| sleep | S3 smoothed_spike | G2 | 0.330269277 | 0.353335720 | 0.023066442 | 0.049998745221 |
| sleep | S3 smoothed_spike | G3 | 0.470370686 | 0.418278691 | -0.052091994 | 0.049939507998 |
| anesthesia | S1 dFF | G1 | 0.296609542 | 0.365037241 | 0.068427699 | 0.049999951461 |
| anesthesia | S1 dFF | G2 | 0.397077134 | 0.481489923 | 0.084412788 | 0.050000000000 |
| anesthesia | S1 dFF | G3 | 0.451051669 | 0.482110197 | 0.031058528 | 0.050000000000 |
| anesthesia | S2 spike | G1 | 0.254979926 | 0.195058185 | -0.059921740 | 0.049999951461 |
| anesthesia | S2 spike | G2 | 0.360223434 | 0.301221343 | -0.059002090 | 0.050000000000 |
| anesthesia | S2 spike | G3 | 0.334015394 | 0.295819997 | -0.038195397 | 0.050000000000 |
| anesthesia | S3 smoothed_spike | G1 | 0.289100998 | 0.399252713 | 0.110151716 | 0.049999951461 |
| anesthesia | S3 smoothed_spike | G2 | 0.349581295 | 0.279423133 | -0.070158162 | 0.050000000000 |
| anesthesia | S3 smoothed_spike | G3 | 0.381069959 | 0.270690444 | -0.110379515 | 0.050000000000 |

The effective-density values slightly below `0.05` for some node counts are
the exact discrete `floor(0.05 * possible_edges) / possible_edges` result;
they are not a post-hoc parameter change or graph failure.

## 5. Preregistered stability classification

| Contrast | DeltaQ range | Classification |
|---|---:|---|
| Wake vs NREM | `-0.095031872` to `+0.052495345` | `DIRECTION-REVERSED` |
| Wake vs Isoflurane | `-0.110379515` to `+0.110151716` | `DIRECTION-REVERSED` |

These labels mean that the direction of the recording-level `DeltaQ` changes
across the frozen signal/grain cells. They do not establish a population
effect, a consciousness mechanism, objectification, Bearer, One, Selection,
or any SRT proposition.

## 6. Octave compatibility cross-check

GNU Octave `11.3.0` with `statistics 1.9.3` and `datatypes 1.4.2` completed a
bounded cross-check on the first Sleep S3/C1/G3 Awake window. It used the
pinned author `get_close_clustering`, `spatial_coarse_graining`,
`densityBasedThresh`, and included BCT `community_louvain`. Because Octave
lacks MATLAB `graph`/`conncomp`, an external BFS compatibility wrapper supplied
the source preconditioner; the pinned source files were not modified.

| Quantity | Octave wrapper | Python primary |
|---|---:|---:|
| Nodes | 173 | 173 |
| Edges | 743 | 743 |
| Effective density | 0.049939507998 | 0.049939507998 |
| Connected components | 41 | 41 |
| Largest component | 130 | 130 |

Octave BCT 10-trial Q maximum was `0.396396877813`; Python primary
python-louvain 200-trial Q maximum for the same graph was `0.397945653375`.
Those Q values are not treated as exact-equivalence targets because the
algorithm implementations and randomization paths differ. The graph and
source preprocessing cross-check passed. This does not upgrade the result to
native MATLAB execution.

## 7. Deferred work and next gate

Not executed: `K` sensitivity, C2 inclusion, window sensitivity, NREM versus
anesthesia, matched-component analysis, full seven-level grain sweep, and
any SRT-facing theory interpretation. These require a separately recorded
extension or amendment under the frozen protocol.

Machine-readable outputs remain under the ignored runtime directory:

```text
.local/phase1_objectification/phase1_postprimary_summary.json
.local/phase1_objectification/compute_audit.json
.local/phase1_objectification/octave_crosscheck.mat
.local/phase1_objectification/cell_results/*.json
```
