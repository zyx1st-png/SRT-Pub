---
id: SRT-NEURO-OBJECTIFICATION-SCALE-EXTERNAL-HAMBURG-ANESTHESIA-RESULT-20260923
type: experiment_result
status: frozen
version: v0_1
record_stage: phase3a_external_anesthesia_result_complete
date: 2026-09-23
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_ANESTHESIA_PREREGISTRATION_2026-09-22.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_AVAILABILITY_AUDIT_2026-09-22.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_SLEEP_STATE_RECOVERY_2026-09-22.md
tags: [Neuroscience, ExternalReplication, HamburgCA1, Anesthesia, FrozenResult]
---

# HAMBURG EXTERNAL ANESTHESIA REPLICATION

## Gate status

```text
primary contrast: Wake ↔ Isoflurane
preregistration commit: a9ce37fb7bcb11108a40dd0efd108355ab44def7
recordings completed: 88/88
animals completed: 7/7
awake recordings: 39/39
isoflurane recordings: 49/49
network modularity calculated: yes, Anesthesia only
Sleep Q calculated: no
early stopping: no
```

This is the result of the separately frozen Hamburg Anesthesia protocol. It is an external method replication/adaptation and does not require numerical equality with Kiyooka et al.

## Data and materialization

```text
processed DOI: 10.12751/g-node.lkx6kk
GIN repository commit: 8a784cc0177eaa8d66970363b76b84ff1a7cf662
license: CC0 1.0 Public Domain Dedication
primary source cell: awake ↔ isoflurane
processed ZIP: not materialized as a full archive
raw 2.3-TiB archive: not downloaded
operational retrieval: 264 per-recording Suite2p objects (spks, iscell, stat)
materialized bytes: 1,927,376,637 bytes
```

All selected objects were validated before use. The final runtime inventory contained 39 Awake and 49 Isoflurane recordings across the seven animals. Every recording supplied one complete 9000-frame (300 s) window.

## Frozen computation

```text
signal: Suite2p spks.npy → Gaussian smoothing, support=59 frames, sigma=59/6
ROI inclusion: iscell.npy[:,0] == 1
G1: accepted cells
G2: local groups max(2, ceil(0.02*N))
G3: local groups max(4, ceil(0.04*N))
graph: connected MST backbone + strongest remaining abs-correlation edges
target mean degree: 4
edge count: M=2N
Louvain repeats: 200
seed root: 12345
window: 9000 frames at 30 Hz, one complete window per recording
window/recording is not a biological replicate
primary biological unit: animal
```

Each of the 88 recordings had 3 grains × 200 finite Q trials. The recording Q is the maximum of the 200 trials. The animal-level quantity is the mean recording Q within condition, followed by:

```text
DeltaQ_g = mean(Q_iso,g) - mean(Q_awake,g)
grain_shift = DeltaQ_G3 - DeltaQ_G1
```

## Animal-level results

| animal | awake recordings | isoflurane recordings | DeltaQ G1 | DeltaQ G2 | DeltaQ G3 | grain shift G3−G1 | classification |
|---|---:|---:|---:|---:|---:|---:|---|
| 37527 | 7 | 9 | 0.106886 | 0.029096 | 0.006314 | -0.100573 | EX-R-NEGATIVE-SHIFT |
| 37528 | 7 | 9 | -0.068495 | 0.015841 | -0.008780 | 0.059716 | EX-R-GRAIN-REVERSED |
| 37529 | 6 | 9 | 0.033076 | -0.032672 | -0.015634 | -0.048709 | EX-R-GRAIN-REVERSED |
| 37530 | 6 | 9 | -0.054012 | -0.029931 | -0.000493 | 0.053519 | EX-R-OTHER |
| 48 | 3 | 3 | 0.117979 | 0.000968 | 0.041827 | -0.076152 | EX-R-NEGATIVE-SHIFT |
| 51 | 5 | 5 | 0.001439 | -0.150164 | -0.132599 | -0.134038 | EX-R-NEGATIVE-SHIFT |
| 53 | 5 | 5 | 0.017549 | 0.008085 | 0.047173 | 0.029624 | EX-R-OTHER |

Summary:

```text
mean grain shift: -0.0309446622
median grain shift: -0.0487091562
animal bootstrap 95% percentile CI: [-0.0845573022, 0.0217828032]
substantive negative grain shifts (< -0.01): 4/7
categorical grain reversals: 2/7
per-animal classes: 3 EX-R-NEGATIVE-SHIFT, 2 EX-R-GRAIN-REVERSED, 2 EX-R-OTHER
dataset classification: EX-C
```

`EX-C` is the preregistered dataset-level label for substantial grain reversal across multiple independent animals with an overall negative grain-shift tendency. It is a description of this external result under the frozen adaptation; it is not a claim that SRT, objectification, Bearer, One, consciousness, or a universal neural law has been established.

## Graph and numerical integrity

```text
all 264 graph records: M=2N and achieved mean degree=4
components != 1: 0
isolates != 0: 0
largest-component invariant failures: 0
non-finite Q trials: 0
Q trial count errors: 0
threshold/tie excess failures: 0 observed in retained edge ranking
```

Observed node-count ranges were G1 85–652, G2 36–50, and G3 22–25. The minimum G3 graph therefore remained connected under the fixed `kbar=4` rule without post-hoc degree adjustment.

## Execution incidents and recovery

Two runtime-only incidents were preserved in the checkpoint evidence:

1. Index 024 encountered a race when an earlier experimental prefetch process and the main analyzer wrote the same `.part` path. The valid final `spks.npy` was independently checked (`shape=(607,9000)`, recorded SHA-256), the prefetcher was stopped, and index 024 was completed without rerunning indices 000–023.
2. The first analyzer process later disappeared while index 045 had a partial file and no new traceback. The partial was retained as evidence; because GIN rejected byte-range resume, the file was safely re-downloaded from the beginning. Indices 000–044 were reused from valid results.

Neither incident changed a scientific parameter, signal, inclusion rule, graph rule, seed, window, or result-selection rule.

## Sleep boundary

The separate Hamburg Sleep state-recovery record remains:

```text
STOPPED_PROTOCOL_GATE
calcium state-label vector: not faithfully executable from inspected public code/data objects
Sleep network preregistration: not frozen
Sleep Q/DeltaQ: not calculated
```

This Anesthesia result does not authorize a Hamburg Sleep network calculation. The programme stops at this Anesthesia result until a separately frozen Sleep protocol exists.

## Files and evidence

- Machine-readable result: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_ANESTHESIA_RESULT_2026-09-23.json`
- Animal-level CSV: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_ANESTHESIA_ANIMAL_RESULTS_2026-09-23.csv`
- Frozen preregistration: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_ANESTHESIA_PREREGISTRATION_2026-09-22.md`
- Availability audit: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_AVAILABILITY_AUDIT_2026-09-22.md`
- Sleep recovery gate: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_SLEEP_STATE_RECOVERY_2026-09-22.md`
- Runtime checkpoint: `.local/phase3a_hamburg/anesthesia_state.json`
- Runtime numeric summary: `.local/phase3a_hamburg/anesthesia_numeric_summary.json`

The external Anesthesia gate is complete. No new Hamburg Sleep network analysis was started.
