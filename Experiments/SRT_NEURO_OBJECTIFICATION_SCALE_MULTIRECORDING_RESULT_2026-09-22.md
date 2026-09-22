---
id: SRT-NEURO-OBJECTIFICATION-SCALE-MULTIRECORDING-RESULT-20260922
type: experiment_result
status: frozen
version: v0_1
record_stage: multirecording_primary_complete
date: 2026-09-22
layer: operations
epistemic_layer: experimental
claim_mode: result_report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, MultiRecording, Replication, Objectification, Scale, GrainInstability]
---

# Multi-recording grain replication — primary result

## 1. Scope and execution gate

This result reports the frozen multi-recording primary replication specified in `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_MULTIRECORDING_PREREGISTRATION_2026-09-21.md`. The availability audit was completed and committed before any recording-level `DeltaQ` was calculated: `bca6ecfa86871e0a1faed590971a8803d536de2e`.

The analysis used every technically eligible recording, with no result-dependent exclusion. It used only S3 (`spike_smoothed`), C1, G1/G2/G3, the frozen connected graph rule with target mean degree 16, and 200 fixed-seed Python Louvain repeats per window.

## 2. Completion and validation

- Eligible recordings: `10/10`.
- Recording-level outputs complete: `10/10`.
- Source windows processed: `216`.
- Q trials validated: `43,200` (`216 × 200`).
- Every window has finite 200-trial Q values and a stored max-Q.
- Every graph has exact edge count `M=round(N×16/2)`, one connected component, largest-component fraction 1.0, and zero isolates.
- Biological unit: animal; sessions are nested within animal. The two mouse04 sleep sessions are retained as separate sessions and averaged only in the animal-level summary.
- No result-based early stopping or recording exclusion occurred.

## 3. Recording-level DeltaQ

`DeltaQ_g = mean(Q_max,target windows) − mean(Q_max,Wake windows)`. The classification threshold is the frozen `±0.01 Q` rule.

| recording | condition | animal | DeltaQ G1 | DeltaQ G2 | DeltaQ G3 | G3−G1 | classification |
|---|---|---|---:|---:|---:|---:|---|
| mouse01_sleep | Sleep | mouse01 | 0.051566 | 0.014278 | -0.039700 | -0.091265 | R-GRAIN-REVERSED |
| mouse02_sleep | Sleep | mouse02 | 0.030518 | 0.025625 | -0.002174 | -0.032693 | R-ATTENUATED |
| mouse03_sleep | Sleep | mouse03 | 0.097086 | 0.062438 | 0.097567 | 0.000481 | R-STABLE-POSITIVE |
| mouse04_day1_sleep | Sleep | mouse04 | 0.154801 | 0.080644 | -0.034761 | -0.189562 | R-GRAIN-REVERSED |
| mouse04_day2_sleep | Sleep | mouse04 | 0.066988 | 0.092620 | 0.082976 | 0.015988 | R-STABLE-POSITIVE |
| mouse05_sleep | Sleep | mouse05 | 0.108831 | 0.034341 | -0.061396 | -0.170227 | R-GRAIN-REVERSED |
| mouse03_ane | Anesthesia | mouse03 | -0.020865 | 0.115074 | 0.027144 | 0.048009 | R-GRAIN-REVERSED |
| mouse05_ane | Anesthesia | mouse05 | 0.000681 | 0.051741 | -0.068572 | -0.069253 | R-GRAIN-REVERSED |
| mouse06_ane | Anesthesia | mouse06 | 0.131523 | -0.034559 | -0.166371 | -0.297895 | R-GRAIN-REVERSED |
| mouse07_ane | Anesthesia | mouse07 | 0.124052 | 0.062147 | 0.108333 | -0.015718 | R-STABLE-POSITIVE |

## 4. Animal-level summaries

Animal summaries average sessions within animal before the cross-animal summary. Sleep has five animals and six sessions; Anesthesia has four animals and four sessions.

| condition | animals | recordings | median grain_shift | mean grain_shift | negative grain_shift |
|---|---:|---:|---:|---:|---:|
| Sleep | 5 | 6 | -0.086787 | -0.076098 | 4/5 (0.80) |
| Anesthesia | 4 | 4 | -0.042486 | -0.083714 | 3/4 (0.75) |

Animal-level bootstrap summaries (10,000 resamples; percentile interval):

| condition | metric | mean | median | 95% interval |
|---|---|---:|---:|---:|
| Sleep | DeltaQ G1 | 0.079779 | 0.097086 | [0.050390, 0.107307] |
| Sleep | DeltaQ G2 | 0.044663 | 0.034341 | [0.022829, 0.069592] |
| Sleep | DeltaQ G3 | 0.003681 | -0.002174 | [-0.040873, 0.053491] |
| Sleep | paired G3−G1 | -0.076098 | -0.086787 | [-0.126928, -0.030242] |
| Anesthesia | DeltaQ G1 | 0.058848 | 0.062366 | [-0.010092, 0.127788] |
| Anesthesia | DeltaQ G2 | 0.048601 | 0.056944 | [-0.010383, 0.099241] |
| Anesthesia | DeltaQ G3 | -0.024867 | -0.020714 | [-0.117993, 0.067739] |
| Anesthesia | paired G3−G1 | -0.083714 | -0.042486 | [-0.227351, 0.018694] |

## 5. Replication outcome

The preregistered labels are descriptive. For transparent reporting, `MR-C` here means that at least two independent animals contain a recording classified `R-GRAIN-REVERSED`, with a negative animal-level median `G3−G1` shift. This operationalization is applied only after the complete eligible dataset and is not a parameter-selection rule.

- Sleep: `MR-C` — three independent animals have at least one reversed recording; four of five animal-level grain shifts are negative and the median shift is `-0.086787`.
- Anesthesia: `MR-C` — three independent animals have reversed recordings; three of four animal-level grain shifts are negative and the median shift is `-0.042486`.

The bounded empirical statement is that grain-dependent state-contrast instability recurs across multiple independent recordings and animals under the frozen connected, mean-degree-matched graph construction. It does not establish SRT, objectification as an ontology, Bearer, One, Selection, consciousness, or a consciousness mechanism.

## 6. Runtime outputs

The complete machine-readable outputs remain in `.local/phase2_multirecording/` and are not tracked:

- `primary_results/<recording_id>.json` — all windows, all 200 Q trials, max-Q and graph diagnostics;
- `summary/recording_window_results.csv`;
- `summary/recording_graph_diagnostics.csv`;
- `summary/recording_deltaq.csv`;
- `summary/animal_summary.csv`;
- `summary/animal_bootstrap_summary.csv`;
- `summary/summary.json`;
- `summary/plots/recording_deltaq_by_grain.png`;
- `summary/plots/recording_g1_vs_g3.png`;
- `summary/plots/animal_paired_g1_g3.png`.

Raw CBS `.mat` files, correlation caches and runtime scripts were not added to Git. No Phase 1 preregistration was amended, and no new graph family, signal family, matched-component analysis, NEURAL34 analysis or theory promotion was started.
