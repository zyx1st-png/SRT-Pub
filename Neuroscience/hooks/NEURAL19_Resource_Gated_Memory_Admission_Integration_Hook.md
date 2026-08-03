---
id: HOOK-NEURO-NEURAL19-RESOURCE-GATED-MEMORY-ADMISSION
patch_id: PATCH-NEURO-NEURAL19-RESOURCE-GATED-MEMORY-ADMISSION
type: integration_hook
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
domain: theoretical_neuroscience_resource_rational_memory
status: active
integration_status: pending
landing_ledger:
  - target: "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
    state: pending
    blocked_by: "Await the next neuroscience compact-core synthesis pass; preserve the encoding/stabilization distinction and proxy boundaries."
  - target: "Neuroscience/SRT_Neuro_Predictions_Table.md"
    state: pending
    blocked_by: "Await a differential-prediction pass that can add resource-by-uncertainty and acquisition-retention tests without duplicating existing rows."
  - target: "Core/SRT_Core_14_Dynamics_Scaling.md"
    state: pending
    blocked_by: "This is an axiomatic-hybrid core file; any bridge insertion requires author-approved edit-protocol review and must not promote source parameters into canonical variables."
---

# NEURAL19 Integration Hook: Resource-Gated Memory Admission

## 1. Target documents

Primary:

```text
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
Neuroscience/SRT_Neuro_Predictions_Table.md
```

Conditional high-risk target:

```text
Core/SRT_Core_14_Dynamics_Scaling.md
```

## 2. Insert after

In the future neuroscience synthesis, insert after the section that introduces `L_2` as historically sedimented transition structure and before broad claims about learning, habit, or long-term memory.

For the prediction table, place beside existing history-dependence, plasticity, or write-back tests rather than creating a disconnected memory section.

## 3. Suggested native paragraph

> Historical constraint should not be treated as the automatic result of repeated input. A system must both encode current evidence into a history-bearing state and stabilize that state against internal noise and maintenance burden. These functions can fail separately, and the usefulness of history may peak within a bounded uncertainty regime rather than increasing monotonically with uncertainty. This is an implementation-level admission rule, not a definition of `L_2`, `Psi_f`, or `d`.

## 4. Suggested table

| Gate | Question | Candidate measures | Failure mode |
|---|---|---|---|
| encoding | Is current evidence written into a persistent state? | learning rate, trial-history weight, acquisition accuracy | evidence is observed but not stored |
| stabilization | Does the stored state resist internal noise and decay? | retention curve, perturbation recovery, maintenance burden | memory forms but cannot persist |
| behavioral use | Does the history alter later estimation or action? | delayed choice, cue weighting, policy change | memory persists without effective readout |
| reselection | Does stored history preserve revision when conditions change? | reversal cost, exploration, alternative-policy recovery | history improves performance but hardens replacement |

## 5. Do not include

- `M v_t^2 = Psi_f`;
- `Q/(MF) = d`;
- internal memory state as canonical `L_2` by identity;
- a claim that the PRL model demonstrates a neural or ontological phase transition;
- a claim that optimal estimation implies subjecthood, agency, or real choice;
- source equations in canonical sections without explicit bridge labels.

## 6. Future synthesis target

Compress the patch into:

1. one native paragraph on history admission;
2. one encoding/stabilization/use/reselection table;
3. one resource-by-uncertainty differential prediction;
4. one boundary sentence preserving `Psi_f`, `d`, and `L_2` non-identity.

Source patch:

```text
Neuroscience/patches/SRT_Neuro_NEURAL19_Resource_Gated_Memory_Admission_v0_1.md
```
