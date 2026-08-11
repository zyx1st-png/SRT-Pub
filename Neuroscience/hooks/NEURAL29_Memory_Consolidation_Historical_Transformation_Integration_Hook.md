---
id: HOOK-NEURO-NEURAL29-MEMORY-CONSOLIDATION-HISTORICAL-TRANSFORMATION
patch_id: PATCH-NEURO-NEURAL29-MEMORY-CONSOLIDATION-HISTORICAL-TRANSFORMATION
type: integration_hook
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
domain: neuroscience_memory_consolidation
status: active
integration_status: pending
landing_ledger:
  - target: "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
    state: pending
    blocked_by: "Neuroscience layer is currently frozen for local material-triggered owner rewrites. Integrate only in the next memory/neural synthesis and preserve retention/transformation/accessibility/authority separation."
  - target: "Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md"
    state: pending
    blocked_by: "Do not mutate the active NEURAL25 protocol in this material pass. Reopen only if the experiment workline adds a matched-retention/different-transformation arm with preregistered false-memory and transfer controls."
  - target: "Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md"
    state: pending
    target_status: planned
    blocked_by: "Planned neuroscience synthesis target referenced consistently by the memory hardening sequence but not yet created. Landing remains deferred until the neuroscience synthesis owner/workline creates the file and adjudicates the NEURAL28/29/25/27 ordering."
---

# NEURAL29 Integration Hook — Memory consolidation as historical transformation

## 1. Target documents

Existing machine-actionable targets:

```text
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md
```

Planned future synthesis target, formally registered in the landing ledger with `target_status: planned` because the file does not yet exist:

```text
Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
```

## 2. Insert after

### Neural mechanisms CompactCore

When the memory/history synthesis reopens, place NEURAL29 between re-identification and candidate-control decomposition:

```text
NEURAL28: Identification / Re-identification / Relational re-entry
-> NEURAL29: Retention / Transformation / Decontextualization / Integration
-> NEURAL25: Accessibility / Authority / Expression / Write-back
-> NEURAL27: Prospective history-use / Path-bias readout
```

These are explanatory decompositions, not mandatory serial anatomical stages.

### NEURAL25 experiment protocol

Only after the current protocol's calibration / formal-lock workline reopens, consider adding a distinct experimental arm asking whether two conditions matched on explicit item retention differ in:

- transfer/generalization;
- non-immediate relational inference;
- context intrusion;
- false-memory rate;
- correction after feedback.

Do not rewrite the existing flagship matched-current-state / different-history hypothesis into a sleep study.

---

## 3. Suggested native neuroscience paragraph

> Memory can change before it is recalled. Offline consolidation does not merely protect an encoded trace from decay; in some paradigms it changes which contextual bindings remain dominant, which regularities become easy to use, and which previously separated contents can be integrated. This adds a transformation stage between retention and later control. Two systems can therefore retain similar item-level content yet differ in what they can later generalize, infer, misremember or bring into effective competition.

---

## 4. Suggested stage table

| Stage | Question | Negative control |
|---|---|---|
| Retention | did any task-relevant history survive? | retention != transformation |
| Transformation | were context weights / cross-item organization altered? | transformation != explicit rule-object |
| Accessibility | can a transformed content enter current processing? | accessibility != authority |
| Authority | can it change the current path? | authority != expression on every trial |
| Write-back | does the realized path alter later structure? | one output != durable history rewrite |

---

## 5. Do not include

- `memory = L2`;
- `sleep = L2 consolidation`;
- `hippocampus = L2`;
- `schema = L2`;
- `A`, `B`, `C` as pre-objective primitives with relations as the only generated objects;
- `pattern = truth`;
- `learning = Psi_f reduction`;
- new generalization/inference capacity as automatic `d` increase;
- non-conscious processing as proof of subjecthood or phenomenality;
- false memory as evidence that truth does not matter.

---

## 6. Future experiment hook

If the NEURAL25 experimental line reopens, the cleanest NEURAL29 extension is:

```text
match explicit item retention
+ vary consolidation / transformation history
-> jointly measure transfer benefit, false-positive cost, switching/revision after corrective feedback
```

A useful result requires a **dissociation beyond ordinary retention strength**. If no such dissociation survives fatigue, circadian, practice and familiarity controls, NEURAL29 should remain a descriptive consolidation bridge rather than an SRT-specific experimental discriminator.

---

## 7. Future synthesis target

Compress NEURAL29 into four pieces when synthesis reopens:

1. one distinction: retention != transformation;
2. one mechanism bridge: selective weakening / abstraction / integration can occur before explicit recall;
3. one negative control: generativity != factivity;
4. one downstream link: transformation changes the conditions under which NEURAL25/27 accessibility, authority and prospective history-use are expressed.

Source patch:

```text
Neuroscience/patches/SRT_Neuro_NEURAL29_Memory_Consolidation_Historical_Transformation_v0_1.md
```