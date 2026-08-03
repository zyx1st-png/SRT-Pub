---
id: HOOK-NEURO-NEURAL19-PREATTENTIVE-GIST-BINDING-REPORT-INTERFACE
patch_id: PATCH-NEURO-NEURAL19-PREATTENTIVE-GIST-BINDING-REPORT-INTERFACE
type: integration_hook
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
domain: philosophy_of_cognitive_science_visual_attention
status: active
integration_status: pending
landing_ledger:
  - target: "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
    state: pending
    blocked_by: "This PR records the bounded bridge only; compact-core insertion requires a separate synthesis pass that checks overlap with existing attention, working-memory, and predictive-processing sections."
  - target: "Neuroscience/SRT_Neuro_Predictions_Table.md"
    state: pending
    blocked_by: "Prediction-table insertion requires experiment-row normalization and comparison against existing attention, reportability, and conscious-access hypotheses."
  - target: "Neuroscience/SRT_Neuroscience_Hardening_N1_N12_v0_2.md"
    state: pending
    target_status: planned
    blocked_by: "The N1-N12 synthesis is already named in the neuroscience hardening index but has not been created; final placement belongs to that future synthesis."
---

# NEURAL19 Integration Hook: Pre-Attentive Gist, Binding, and Report Interface

## 1. Target documents

Primary:

```text
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
```

Experimental:

```text
Neuroscience/SRT_Neuro_Predictions_Table.md
```

Future synthesis:

```text
Neuroscience/SRT_Neuroscience_Hardening_N1_N12_v0_2.md
```

## 2. Insert after

For the compact core, insert after the section that introduces `G_hat_theta` as embodied neural selection and before any treatment that equates conscious access, report, or working memory with initial perception.

For the prediction table, place near attention / conscious-access / reportability dissociation rows.

For the future N1-N12 synthesis, place in the selection-architecture section before consciousness claims and alongside the NEURAL18 decodability–anchoring guardrail.

## 3. Suggested paragraph

> **Pre-attentive is not pre-selection.** Visual processing can form a wide-field, coarse scene anchor before focused object confirmation. Rapid gist therefore supports a global multi-feature selection stage, but not a complete inner photograph. Illusory conjunctions must be localized across perception, short-term retention, and report reconstruction before they are used to infer the format of initial `L_1`. Picture-like, map-like, and object-bound structures may be task- and resolution-conditioned formats of one selection architecture rather than mutually exclusive ontologies.

## 4. Suggested table

| Measured phenomenon | Safest stage claim | SRT bridge | Do not infer directly |
|---|---|---|---|
| rapid gist categorization | coarse global scene structure is usable before focal inspection | wide-field low-resolution `L_1` anchoring candidate | complete inner photograph; full local binding; consciousness |
| single-feature pop-out | a feature difference rapidly guides spatial selection | salience / spatial-index routing candidate | `d-value`; full `G_hat_theta`; subjecthood |
| conjunction-search slope | heterogeneous grouping, switching, ownership uncertainty, or confirmation adds cost | candidate typed-friction decomposition | `Psi_f` identity; proof of separate feature maps |
| illusory-conjunction report | binding information is wrong at some point before response | perception–VSTM–report localization problem | initial `L_1` format from report alone |
| post-cue detail recovery | some initially unreported information remained accessible | graded occlusion / reversibility candidate | universal preservation of all unattended detail |

## 5. Suggested prediction row

```text
Phenomenon: accurate rapid gist with noisy local conjunction reports
SRT addition: coarse scene anchoring -> focal object reselection -> VSTM -> report gate
Predictions: online action exceeds delayed report binding; gist/local binding dissociate by scale;
concern changes fine-resolution persistence; valid post-cues recover some occluded detail
Failure: standard perception, memory, salience, and search models fully explain all dissociations
```

## 6. Do not include

- The source proves SRT or selection realism.
- Pre-attentive vision occurs before every form of selection.
- Focused visual attention is identical to the whole `G_hat_theta`.
- Gist is a pixel-complete or phenomenally conscious inner picture.
- Feature maps are `L_0`, or iconic format is `L_1` by definition.
- A delayed report error uniquely localizes an error to early perception.
- VSTM is full `L_2` by default.
- Reaction time, set-size slope, memory load, masking cost, or confidence directly measure `Psi_f`.
- Salience or task relevance directly measures `d-value`.
- The supplied penultimate manuscript should replace the eventual published citation.

## 7. Future synthesis target

The future synthesis should compress this hook into:

1. one terminology guardrail: `pre-attentive != pre-selection`;
2. one staged model: coarse scene anchoring -> focal object binding -> VSTM -> report;
3. one scale guardrail: reliable gist can coexist with noisy local ownership;
4. one format guardrail: iconic, map-like, and object-bound structures may be task-conditioned;
5. two experimental rows: online-versus-delayed binding and reversible-detail cueing.

The patch remains the full source-facing analysis:

```text
Neuroscience/patches/SRT_Neuro_NEURAL19_Preattentive_Gist_Binding_Report_Interface_v0_1.md
```
