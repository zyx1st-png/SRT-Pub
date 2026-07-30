---
patch_id: PATCH-NEURO-NEURAL19-PREATTENTIVE-GIST-BINDING-REPORT-INTERFACE
source_ids:
  - SRC-2026-07-30-NEURO-WENTZELL-PREATTENTIVE-VISION-FORMAT-PQ
domain: philosophy_of_cognitive_science_visual_attention
claim_level: bridge
canonical_status: domain_bridge_patch_added
status: patch
target_documents:
  - "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
  - "Neuroscience/SRT_Neuro_Predictions_Table.md"
  - "Neuroscience/SRT_Neuroscience_Hardening_N1_N12_v0_2.md"
related_claims:
  - preattentive_selection
  - global_gist_anchoring
  - local_feature_binding
  - L0_visual_accessibility
  - L1_scene_anchoring
  - L1_object_reselection
  - VSTM_report_interface
  - G_hat_theta
  - resolution_rho
  - occlusion
  - Psi_f_proxy_guardrail
  - d_value_future_test
tags:
  - preattentive_vision
  - iconicity
  - feature_maps
  - gist_perception
  - illusory_conjunctions
  - conjunction_search
  - visual_short_term_memory
  - representational_format
  - attention
  - scale
  - reportability
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_patch
id: PATCH-NEURO-NEURAL19-PREATTENTIVE-GIST-BINDING-REPORT-INTERFACE
---

# SRT Neuroscience Patch NEURAL19: Pre-Attentive Gist, Feature Binding, and the Perception-to-Report Interface v0.1

> **Status**: high-priority philosophy-of-cognitive-science / neuroscience bridge and guardrail patch.  
> **Canonical caution**: this patch does not define `L_0`, `L_1`, `L_2`, `G_hat_theta`, `d-value`, `Psi_f`, attention, perception, or consciousness. It proposes a stage- and scale-typed interface for interpreting pre-attentive vision evidence.

## 0. Source anchor

Primary source:

- Alexander Wentzell. "What is the Format of Pre-Attentive Vision?" *The Philosophical Quarterly* (forthcoming). Penultimate manuscript; public PhilArchive record `WENWIT`.

Source card:

```text
Materials/2026/SRC_2026_07_30_Neuro_Wentzell_Preattentive_Vision_Format_Philosophical_Quarterly.md
```

## 1. Why this matters for SRT

The phrase **pre-attentive vision** creates a predictable SRT category error. In cognitive science it means processing before focused visual attention. It does not mean processing before every form of selection, gain control, relevance weighting, competition, or anchoring.

The first correction is therefore:

```text
pre-attentive
  != pre-selection
```

Pop-out, scene-gist extraction, spatial grouping, and differential feature sensitivity already imply that the visual system has transformed incoming differences into an action- or attention-guiding structure before focused object inspection begins.

The second correction concerns evidence flow. Illusory-conjunction paradigms often infer the format of early perception from delayed reports after masking, divided attention, and short-term retention. SRT needs a stage distinction before using those errors as evidence about `L_1`:

```text
initial perceptual anchoring
  != short-term retention proxy
  != reconstructed report
```

The source is therefore useful less as proof of pictorialism than as pressure for a **multi-resolution, multi-stage selection account**.

## 2. Source argument in compressed form

Wentzell compares two views.

### 2.1 Pictorial / iconic view

```text
parts of representation correspond to scene parts
+
features such as color, shape, and location are represented holistically
```

This format is proposed to explain parallel, high-capacity early vision without requiring one discrete symbol for every feature or object.

### 2.2 Cartographic / feature-map view

```text
separate spatial feature maps
  -> color at locations
  -> orientation / shape at locations
  -> later binding across maps
```

Illusory conjunctions and conjunction-search costs are used to support this account.

### 2.3 Wentzell's counter-pressure

```text
gist perception:
  fast
  high accuracy
  weak sensitivity to scene complexity
  improved in some cases by diagnostic color
  dependent on multiple feature dimensions
```

Wentzell argues that this is difficult to reconcile with an account on which cross-feature combination is intrinsically slow or resource-demanding.

He then weakens the two principal arguments for feature maps:

```text
illusory conjunctions
  may be VSTM binding-retention errors

conjunction-search cost
  may be heterogeneous grouping-and-rejection cost
```

## 3. Main SRT bridge claim

### Claim NEURAL19

Pre-attentive visual processing should be treated as **selection before focal object confirmation**, not as a pre-selection state. The admissible bridge is a staged, resolution-sensitive chain:

\[
L_{0}^{visual}
\xrightarrow{\hat G_{\theta}^{global,\rho_{coarse}}}
L_{1}^{scene/gist}
\xrightarrow{\hat G_{\theta}^{focal,\rho_{fine}}}
L_{1}^{object/binding}
\rightarrow M_{VSTM}
\rightarrow R_{report}
\]

where:

- `L0_visual` is only a local bridge label for currently accessible visual differences, not the canonical total meaning of `L_0`;
- `L1_scene/gist` is a coarse, global, task-conditioned scene anchoring;
- `L1_object/binding` is a finer-grained reselection or confirmation of local object-feature ownership;
- `M_VSTM` is a short-term retention proxy, not automatically full `L_2`;
- `R_report` is a reconstructive behavioral or linguistic output.

The chain is not a claim that the brain executes five serial boxes. It is an epistemic discipline requiring experiments and SRT interpretations to state which stage and output they measure.

## 4. Scene-level and object-level binding must be separated

The apparent conflict between reliable gist and noisy conjunctions weakens when scale is typed.

A visual system may reliably anchor:

- open versus enclosed space;
- natural versus urban texture;
- coarse horizon structure;
- upper/lower field organization;
- diagnostic color-layout relations;
- global spatial frequency and orientation distributions;

while remaining unreliable about:

- which small shape owned which color;
- which local orientation belonged to which object;
- which adjacent feature tokens were co-instantiated;
- which object was present at a precisely reportable location.

Therefore:

```text
global scene coherence
  != complete local object binding
```

and:

```text
reliable scene-level conjunctions
  can coexist with
noisy object-level feature ownership
```

This scale distinction is a direct correction to any SRT reading that treats one successful `L_1` anchoring as maximal-resolution determination of the entire field.

## 5. Pictorialism should be weakened to field-like anchoring

The source's strongest defensible pressure is not that early vision contains an internal realistic photograph. It is that multiple feature dimensions can jointly constrain an early global representation.

SRT should use the weaker bridge term:

```text
field-like holistic anchoring
```

This means:

- globally organized;
- spatially continuous or topology-preserving enough for scene structure;
- jointly constrained by several feature dimensions;
- coarse-grained;
- incomplete with respect to object individuation and reportable detail;
- task- and body-conditioned.

It does not mean:

- pixel-complete;
- phenomenally conscious by default;
- fully bound at every local scale;
- identical to a photograph;
- independent of recurrent processing;
- canonical evidence that `L_1` has one universal format.

## 6. Format pluralism as operator-conditioned geometry

The picture-versus-map dispute may be overdrawn if representational format varies with task, scale, and resolution.

A non-canonical SRT scaffold is:

\[
F_{eff}=F(\theta,\rho,\vec v,B,t)
\]

where:

- `theta` collects embodied, historical, state, and task constraints;
- `rho` is effective resolution;
- `v` is selection direction or task orientation;
- `B` is available processing / retention bandwidth;
- `t` is the relevant processing window.

Candidate regimes:

| Task regime | Effective geometry | SRT-facing reading |
|---|---|---|
| scene gist | global field / spatial envelope | wide-field coarse anchoring |
| single-feature pop-out | salience or feature-index map | rapid differential routing |
| conjunction verification | local object-feature confirmation | focal high-resolution reselection |
| delayed report | feature stores plus binding metadata | retention and reconstruction interface |
| learned naturalistic expertise | hybrid predictive / object / scene structure | history-conditioned format under `L_2` |

The bridge claim is not that these mechanisms are literally interchangeable. It is that SRT should not promote one laboratory format into the unique ontology of all early vision.

## 7. Illusory conjunctions and the `L_1 -> VSTM -> report` gate

Before illusory conjunctions are used as evidence about initial `L_1`, the experiment should declare at least four intervals:

```text
stimulus presentation
mask / interruption
retention and competing task
response generation
```

A local gate can be written:

```text
R_IC = 1
only when the claimed error origin is matched to evidence that localizes it
within perception, retention, or report reconstruction.
```

Possible error sites:

| Site | Candidate error | Useful evidence |
|---|---|---|
| early perception | features never correctly co-instantiated | online eye movement, rapid pointing, neural binding marker |
| perceptual-to-memory transfer | binding relations lost during encoding | retention-delay slope, masking manipulation |
| VSTM maintenance | features survive but ownership metadata decays | load and interference manipulation |
| report reconstruction | separately retained features guessed into one object | response-format and confidence effects |

Guardrail:

```text
final report error
  does not uniquely identify
initial perceptual format
```

## 8. Visual search cost and `Psi_f` proxy discipline

Set-size slopes and reaction times can be useful operational signals, but they are not `Psi_f` by definition.

A bridge decomposition for conjunction-search cost is:

\[
C_{search}
=
\alpha N_{groups}
+
\beta C_{switch}
+
\gamma U_{ownership}
+
\delta C_{confirmation}
+
\epsilon C_{motor/report}
\]

where:

- `N_groups` is the number of distractor groups that must be rejected;
- `C_switch` is grouping, strategy, or attentional switching cost;
- `U_ownership` is uncertainty about which features belong together;
- `C_confirmation` is local high-resolution verification cost;
- `C_motor/report` is downstream response cost.

This is not a canonical equation and does not exhaust the phenomenon.

Only after controls and intervention can one ask whether some component is a proxy for a typed SRT friction:

```text
reaction time / set-size slope / error rate
  = candidate behavioral proxy
  != Psi_f by identity
```

## 9. Relationship to occlusion

SRT's current operator language treats ordinary selection as reduced accessibility or occlusion rather than absolute deletion.

Gist provides a useful bridge hypothesis:

```text
scene-level anchoring
  enhances diagnostic global structure
  while occluding task-irrelevant local detail
```

If occlusion is graded and partly reversible, a valid post-cue should recover some detail that was not initially reportable.

This yields a testable distinction:

```text
occluded but retained / recoverable
  versus
never encoded or fully lost
```

A failure to recover any unreported detail under optimized cueing would weaken this particular occlusion interpretation, though it would not refute the whole SRT operator framework.

## 10. Relationship to `d-value`

The source uses low-stake laboratory stimuli and does not directly test concern-weighted selection.

SRT should not infer `d-value` from:

- color salience;
- target uniqueness;
- experimenter-defined task relevance;
- confidence;
- reaction speed;
- memory accuracy.

The source instead opens a future test:

```text
matched visual structure
x
neutral vs bodily relevant / threat / self-relevant / future-constraining meaning
```

A stronger SRT result would require concern manipulation to alter not only report speed but also persistence, interference resistance, autonomic response, delayed memory, reversal cost, or future visual policy.

## 11. Candidate bridge hypotheses

These are P3/P4 bridge-lab candidates, not primitive axioms.

### H-NEURAL19a: online-versus-delayed binding dissociation

If a substantial share of illusory conjunctions arises in VSTM or report reconstruction, immediate online action should preserve correct feature ownership better than delayed verbal report under matched exposure.

Prediction:

```text
binding accuracy:
immediate saccade / pointing / grasping
  > delayed verbal reconstruction
```

Failure condition:

```text
If online action and delayed report show the same error structure across delay, load,
and response format, the memorial-error bridge weakens.
```

### H-NEURAL19b: scale-typed reliability

Scene-level gist can remain accurate when fine object-feature ownership is unreliable.

Prediction:

```text
same trial:
correct scene category / global layout
+
incorrect local color-shape ownership
```

The effect should vary systematically with spatial scale and resolution rather than appearing as one undifferentiated binding capacity.

Failure condition:

```text
If gist accuracy and local-binding accuracy always covary after difficulty and confidence controls,
the proposed scale dissociation weakens.
```

### H-NEURAL19c: task-conditioned format geometry

The same stimulus should recruit different effective representational geometry when the task changes from gist classification to feature pop-out to conjunction verification.

Prediction:

- global summary sensitivity should dominate gist tasks;
- single-feature spatial indexing should dominate pop-out;
- local recurrent or focal confirmation should dominate conjunction verification;
- cross-task representational similarity should not imply one invariant format.

Failure condition:

```text
If one fixed representational model predicts all tasks and interventions without task- or scale-specific parameters,
the SRT format-pluralism increment narrows.
```

### H-NEURAL19d: concern-weighted resolution allocation

At matched physical salience, high-consequence stimuli should receive more rapid or more persistent fine-grained binding than neutral stimuli.

Candidate measures:

- eye-movement latency and landing precision;
- local binding accuracy;
- resistance to masking and distractors;
- autonomic response;
- delayed memory;
- rule-reversal cost;
- future attentional bias.

Failure condition:

```text
If reward, arousal, salience, and ordinary task relevance fully absorb the effect,
no independent d-value bridge is established.
```

### H-NEURAL19e: reversible-detail cueing

If gist selection occludes rather than absolutely deletes local differences, valid post-cues should recover above-chance detail not included in the first report, within a bounded temporal window.

Failure condition:

```text
If optimized cueing never recovers unreported detail beyond response guessing and iconic-memory baselines,
the specific occlusion-recovery bridge weakens.
```

## 12. Differential prediction card

### Phenomenon

Rapid accurate gist extraction coexists with slower conjunction search and illusory conjunctions under masking, divided attention, retention, and report.

### Nearby explanations

- classic or revised feature-integration theory;
- recurrent visual grouping and segmentation;
- object-file / index models;
- biased competition;
- predictive-processing hierarchy;
- visual working-memory feature-store models;
- search-strategy and distractor-homogeneity accounts.

### SRT added structure

- pre-attentive versus pre-selection distinction;
- global coarse anchoring versus local fine reselection;
- perception / retention / report stage typing;
- task-conditioned effective format;
- concern-weighted resolution allocation;
- graded occlusion and detail recovery;
- typed friction rather than raw latency identity.

### SRT-favoring pattern

```text
matched stimulus and basic decodability
+
selective changes in scale, concern, cueing, and stage
predict different persistence, binding, recovery, and future-selection effects
```

### Narrowing condition

If ordinary hierarchical perception, working-memory, salience, reward, arousal, and search-strategy variables explain all stage, scale, persistence, and cue-recovery effects, NEURAL19 should remain only a terminology and measurement-hygiene patch.

## 13. Boundary cautions

- Do not write that the paper proves SRT or selection realism.
- Do not write that pre-attentive vision occurs before all selection.
- Do not identify focused visual attention with the whole of `G_hat_theta`.
- Do not identify a picture-like format with `L_1` by definition.
- Do not identify feature maps with `L_0`.
- Do not write that gist is a complete or pixel-accurate inner photograph.
- Do not infer local object binding from scene-category accuracy.
- Do not infer initial perceptual error from delayed report error without stage-localizing evidence.
- Do not call VSTM full `L_2` without durable history and future-transition evidence.
- Do not equate reaction time, set-size slope, masking cost, working-memory load, or accuracy with `Psi_f`.
- Do not equate target salience or task relevance with `d-value`.
- Do not treat the iconic-versus-cartographic contrast as exhaustive of current vision science.
- Keep source status visible: forthcoming philosophy article, penultimate manuscript, no new experiment.

## 14. What would narrow or defeat this patch

This patch should be narrowed if:

1. online action measures show the same illusory-conjunction profile as delayed reports, with no delay/load dependence;
2. scene-level and object-level binding show no meaningful scale dissociation after difficulty controls;
3. a single fixed-format model explains gist, pop-out, conjunction verification, retention, and report better than task-conditioned models;
4. cueing results are fully explained by standard iconic-memory mechanisms without any added value from SRT occlusion language;
5. concern manipulations collapse into reward, arousal, salience, or learned task relevance;
6. `Psi_f` proxies add no prediction beyond reaction time, uncertainty, switching, and working-memory demand;
7. the eventual published article materially revises or withdraws the manuscript's argument.

If these conditions hold broadly, NEURAL19 remains a useful stage-typing and report-interface guardrail rather than an SRT-specific neurocognitive bridge.

## 15. Integration target text

Recommended compact-core insertion:

> **Pre-attentive is not pre-selection.** Visual processing can form a wide-field, coarse scene anchor before focused object confirmation. Rapid gist therefore supports a global multi-feature selection stage, but not a complete inner photograph. Illusory conjunctions must be localized across perception, short-term retention, and report reconstruction before they are used to infer the format of initial `L_1`. Picture-like, map-like, and object-bound structures may be task- and resolution-conditioned formats of one selection architecture rather than mutually exclusive ontologies.

Recommended prediction-table insertion:

```text
Phenomenon: accurate rapid gist with noisy local conjunction reports
SRT addition: coarse scene anchoring -> focal object reselection -> VSTM -> report gate
Predictions: online action exceeds delayed report binding; gist/local binding dissociate by scale;
concern changes fine-resolution persistence; valid post-cues recover some occluded detail
Failure: standard perception, memory, salience, and search models fully explain all dissociations
```

Recommended claim-status insertion:

```text
NEURAL19 is a bridge/guardrail claim.
Gist accuracy, iconicity, feature maps, reaction time, VSTM errors, and reportability are not
direct measures of L0, L1, L2, G_hat_theta, d-value, Psi_f, subjecthood, or consciousness.
```

## 16. Integration status

Added as a standalone high-priority visual-cognition bridge patch.

```text
SourceCard created
NEURAL19 patch created
IntegrationHook created
Neuroscience hardening index updated
Material log registered
Compact-core / prediction-table / future N1-N12 synthesis merge remains pending
```

Future synthesis should place NEURAL19 near the attention / selection-architecture section, with NEURAL18 immediately nearby as the complementary warning that neural decodability is not anchoring and pre-attentive format is not directly recoverable from a single downstream readout.
