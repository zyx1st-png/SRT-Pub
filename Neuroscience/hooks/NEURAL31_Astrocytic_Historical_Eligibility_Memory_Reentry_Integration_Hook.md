---
id: HOOK-NEURO-NEURAL31-ASTROCYTIC-HISTORICAL-ELIGIBILITY-MEMORY-REENTRY
patch_id: PATCH-NEURO-NEURAL31-ASTROCYTIC-HISTORICAL-ELIGIBILITY-MEMORY-REENTRY
type: integration_hook
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
domain: neuroscience_memory_astrocytes
status: active
integration_status: pending
landing_ledger:
  - target: "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
    state: pending
    blocked_by: "Neuroscience owner synthesis is not reopened in this material pass. Integrate NEURAL31 only with the NEURAL28/29/25/27 memory sequence and preserve the content/retrievability/eligibility distinction."
  - target: "Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md"
    state: pending
    blocked_by: "Do not mutate the active protocol from a single material pass. Reopen only if adding a matched-retention / astrocytic-eligibility arm with cue-specific versus arousal controls."
  - target: "Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md"
    state: pending
    target_status: planned
    blocked_by: "Planned neuroscience synthesis target. Land only after the owner workline adjudicates NEURAL31 against NEURAL29 and the existing astrocytic associative-memory capacity line."
---

# NEURAL31 Integration Hook — Astrocytic historical eligibility and memory re-entry

## 1. Target placement

When the memory/neuroscience synthesis reopens, use the following functional sequence:

```text
NEURAL28
Identification / re-identification / relational re-entry indexing

-> NEURAL29
Retention / transformation / decontextualization / integration

-> NEURAL31
Historical eligibility / retrievability / selective re-entry conditions

-> NEURAL25
Accessibility / authority / expression / write-back

-> NEURAL27
Prospective history-use / future path-bias readout
```

This ordering is explanatory, not a mandatory anatomical pipeline.

---

## 2. Suggested native neuroscience paragraph

> Memory persistence should not be identified only with preserved content. Learning can also leave astrocytic ensemble states that alter how later cues, neuromodulatory signals and neuronal ensemble activity are admitted into recall and restabilization. Current evidence supports a causal role for astrocytes in retrievability, stabilization and precision, but does not yet show that an astrocytic ensemble can independently carry cue-specific memory content when the corresponding neuronal engram is silenced.

---

## 3. Required distinction table

| Function | Local question | Negative control |
|---|---|---|
| Content constraint | what supports pattern-specific reconstruction? | content != accessibility |
| Historical eligibility | what past-induced state changes later responsiveness? | eligibility != content storage |
| Retrievability | can the old trajectory re-enter now? | non-recall != erasure |
| State modulation | did arousal/fear/global gain change? | state shift != cue-specific recall |
| Restabilization | does re-entry alter later trace precision/stability? | recall effect != durable write-back |

---

## 4. Insert after NEURAL29, not inside it

NEURAL29 owns:

```text
retained history
-> consolidation transformation
-> altered later use
```

NEURAL31 owns:

```text
historical state
-> re-entry eligibility / retrievability
-> recall-linked stabilization / precision
```

Do not merge the two into a generic `memory changes over time` paragraph; the distinction is the useful increment.

---

## 5. Existing astrocyte-memory line

The owner neuroscience file already contains a theoretical astrocytic associative-memory capacity window.

Keep:

```text
higher-order astrocytic coupling / attractor geometry
```

separate from:

```text
astrocytic historical eligibility / memory re-entry
```

The current experimental literature does not validate the specific higher-order coupling model.

---

## 6. Do not include

- `astrocytes store memory` as a settled conclusion;
- `astrocyte = L2`;
- `memory = L2`;
- freezing as automatic proof of cue-specific recall;
- general fear/arousal modulation as evidence for an astroengram;
- astrocytic Ca2+ as a direct SRT variable;
- reconsolidation as alteration of the irreversible past;
- the phrase `necessary and sufficient for memory` without specifying the behavioral paradigm and the neuronal/state confounds.

---

## 7. Future experiment hook

A strong NEURAL31 experiment requires at least two discriminations:

```text
memory-specific recall
vs
fear/arousal/state change
```

and:

```text
astrocytic eligibility effect
vs
ordinary neuronal-engram strength
```

Preferred design family:

```text
label learning-linked neuronal + astrocytic ensembles
+ manipulate astrocytes in separate temporal windows
+ independently suppress / measure neuronal engram state
+ measure cue-specific recall, general arousal/fear, precision/generalization and post-recall stability
```

The strongest astroengram hypothesis is supported only if cue-specific recall survives verified suppression of the corresponding neuronal engram.

The weaker NEURAL31 eligibility bridge can survive failure of that test if astrocytes still show specific causal effects on retrievability, stabilization or precision.

---

## 8. SRT bridge sentence for later synthesis

Use only as P3 bridge language:

> **Memory is one mechanism by which irreversible history becomes causally effective in future selection; its persistence can reside partly in preserved conditions for selective re-entry rather than preserved content alone.**

Cross-reference, do not rewrite:

```text
Core/SRT_Core_21b_Constitutive_Theorems.md — P1-T02 / P1-T03
Core/SRT_Core_12b_Ontology_L2.md — T-L2-Scaffold
Neuroscience/patches/SRT_Neuro_NEURAL29_Memory_Consolidation_Historical_Transformation_v0_1.md
```

---

## 9. Source patch

```text
Neuroscience/patches/SRT_Neuro_NEURAL31_Astrocytic_Historical_Eligibility_Memory_Reentry_v0_1.md
```
