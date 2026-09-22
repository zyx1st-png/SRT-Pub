---
id: SRT-NEURO-OBJECTIFICATION-SCALE-EXTERNAL-HAMBURG-SLEEP-STATE-RECOVERY-ADDENDUM-20260923
type: experiment_audit
status: frozen
version: v0_1
record_stage: phase3a_sleep_state_recovery_evidence_addendum
date: 2026-09-23
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_SLEEP_STATE_RECOVERY_2026-09-22.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_AVAILABILITY_AUDIT_2026-09-22.md
tags: [Neuroscience, ExternalReplication, HamburgCA1, SleepStateRecovery, ResultBlind, ProtocolGate]
---

# Phase 3A — Hamburg sleep-state recovery evidence addendum

## Scope

This addendum records a further result-blind inspection of the locally materialized
metadata and source-tree inventory. It does not define a new classifier and does not
calculate calcium-network modularity, `Q`, or `DeltaQ`.

## Local file evidence

The processed Sleep metadata contains 54 calcium-recording rows for animals 8235,
8237, and 8238. The rows provide recording length and a corresponding pupillometry
filename. The public processed tree separately exposes the following calcium-side
objects for these recordings:

```text
calcium pupillometry videos: 54
DLC_csv_2PM files: 54
Matlab_2PM pupil-feature files: 54
ready discrete calcium Wake/NREM/REM vectors: not present
```

The locally materialized `Sleep/sleep_scoring` objects are:

```text
M1R1.mat, M1R2.mat, M2R1.mat, M2R2.mat,
M3R1.mat, M4R1.mat, M4R2.mat
```

Each file contains one `SleepScoring` object with three fields:

```text
Wake, NREM, REM
```

Their vector lengths are 1461, 1421, 1763, 799, 1173, 1047, and 1469,
respectively. These are electrophysiology-side scoring vectors for seven ephys
sessions. They are not keyed to the 54 calcium recordings by a same-session
calcium epoch-label object.

## Gate consequence

The additional inventory strengthens, but does not change, the prior gate decision:

```text
published ephys scoring code: recoverable
calcium pupil/DLC features: available
original pupil/eyelid-to-calcium classifier: not recoverable
frozen calcium epoch labels: not recoverable
new classifier or threshold: not created
Sleep Q/DeltaQ: not calculated
```

The Sleep external replication therefore remains stopped at the protocol gate. A
future Sleep calculation requires either the original classifier and its frozen
model/threshold state, or a separately authorized result-blind protocol amendment
that defines and validates a replacement classifier before any network analysis.

## Provenance

Local evidence was inspected under `.local/phase3a_hamburg/metadata/` and
`.local/phase3a_hamburg/tree/`. The primary processed dataset is the Hamburg CA1
dataset at DOI `10.12751/g-node.lkx6kk`. No external network outcome was read or
computed during this addendum.
