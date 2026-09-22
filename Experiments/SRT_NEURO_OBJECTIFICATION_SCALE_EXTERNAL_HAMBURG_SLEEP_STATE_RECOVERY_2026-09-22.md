---
id: SRT-NEURO-OBJECTIFICATION-SCALE-EXTERNAL-HAMBURG-SLEEP-STATE-RECOVERY-20260922
type: experiment_audit
status: frozen
version: v0_1
record_stage: phase3a_sleep_state_recovery_stopped_at_protocol_gate
date: 2026-09-22
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_AVAILABILITY_AUDIT_2026-09-22.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_PREREGISTRATION_2026-09-18.md
tags: [Neuroscience, ExternalReplication, HamburgCA1, SleepStateRecovery, ResultBlind, ProtocolGate]
---

# Phase 3A — Hamburg sleep-state recovery gate

## Status

```text
status: STOPPED_PROTOCOL_GATE
network modularity calculated: NO
Q calculated: NO
DeltaQ calculated: NO
sleep network preregistration frozen: NO
```

This record reports a result-blind recovery audit only. It does not inspect or calculate any Hamburg sleep network outcome.

## 1. Published method recovery

The public author repository was inspected at:

```text
https://github.com/mchini/Yang_Chini_et_al
commit: 317a72de133b6d7f23a59481dd2a3c9323fc3b16
relevant directory: Figures_5-7_(MATLAB)
```

The available `AutomatedSleepScoring.m` recovers the electrophysiology-side scoring logic and is parameterized by a block size:

```text
scoring epoch: parameterized; shipped MainSleepScoring.m sets 10 s
overlap: 50% (15 s step)
LFP features: delta 1–4 Hz; theta 6–12 Hz; theta/delta ratio
EMG feature: 30–300 Hz power
movement: summed block movement
NREM: deltaP > 70th percentile, EMG < 50th percentile, movement < 5e6
REM: theta/delta > 75th percentile, EMG < 25th percentile, movement < 5e6
Wake: EMG > 80th percentile or movement > 1e7
```

The code uses electrophysiology and movement inputs and depends on the author's external Neuralynx/filter/multitaper functions. This is sufficient to recover the published ephys scoring rule, but it is not itself a calcium-recording label vector.

There is a source-method discrepancy that is recorded rather than silently resolved: the published method describes 30 s scoring epochs, while the shipped `MainSleepScoring.m` driver sets `block_size = 10` and therefore calls the same 50%-overlap helper with 10 s epochs. No 10-to-30 s substitution was used to create labels for the Hamburg calcium recordings.

The paper's second stage maps ephys-grounded state labels to calcium recordings using pupil/eyelid features. The inspected public `Figures_5-7_(MATLAB)` tree contains no executable pupil/eyelid-to-calcium classifier, frozen classifier object, or ready per-epoch state vector for the 54 Hamburg calcium recordings. The processed Hamburg repository likewise exposes pupil/DLC feature objects but no unambiguous calcium Wake/NREM/REM label vector.

## 2. Result-blind Hamburg sleep inventory

The availability audit found:

```text
natural-sleep calcium recordings: 54
animals: 8235, 8237, 8238
recording counts: 22, 15, 17
calcium pupil videos: 54
DLC feature CSVs: 54
Matlab_2PM feature objects: 54
ready discrete calcium epoch labels: not found
```

The separate `Sleep/sleep_scoring/*.mat` files are electrophysiology scores for four animals and seven ephys sessions. They are not a direct mapping for the 54 calcium recordings and cannot be used as if they were same-session calcium labels.

No recording was excluded using correlation, graph, modularity, `Q`, `DeltaQ`, or grain effects. No state-effect pattern was inspected.

## 3. Required epoch accounting

The required per animal/recording/epoch inventory was not fabricated. Because the calcium classifier output is unavailable, the following fields remain explicitly unresolved rather than being filled with guessed labels:

```text
epoch count: NOT RECOVERABLE FROM AVAILABLE LABEL OBJECTS
Wake count: NOT RECOVERABLE
NREM count: NOT RECOVERABLE
REM count: NOT RECOVERABLE
unclassified count: NOT RECOVERABLE
fraction classified: NOT RECOVERABLE
cross-validation/accuracy diagnostics: NOT RECOVERABLE FOR CALCIUM MAPPING
```

The published paper reports that the pupil/eyelid classifier was evaluated against the ephys-grounded labels, but a reported accuracy number is not a substitute for the per-recording classifier output required for this replication.

## 4. Gate decision

```text
ephys method: recovered at source-code level
calcium state-label recovery: not faithfully executable from the public code/data objects inspected
new classifier or threshold design: prohibited and not performed
Sleep network protocol: not frozen
Sleep Q/DeltaQ: not calculated
```

The Sleep gate therefore stops at the published state-label recovery protocol boundary. A future continuation requires one of:

1. the original calcium pupil/eyelid classifier code and its frozen model/threshold state;
2. a separately authorized, result-blind protocol amendment that defines and validates a new classifier before any Sleep network calculation.

Neither condition is silently assumed here. The Hamburg Anesthesia gate is independent and may complete under its separately frozen preregistration.

## Evidence

- Author code: <https://github.com/mchini/Yang_Chini_et_al/tree/master/Figures_5-7_%28MATLAB%29>
- `MainSleepScoring.m` and `supporting functions/AutomatedSleepScoring.m` were fetched from the pinned public repository commit above.
- Hamburg availability audit: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_AVAILABILITY_AUDIT_2026-09-22.md`.
- Hamburg processed dataset: <https://doi.gin.g-node.org/10.12751/g-node.lkx6kk/>.
