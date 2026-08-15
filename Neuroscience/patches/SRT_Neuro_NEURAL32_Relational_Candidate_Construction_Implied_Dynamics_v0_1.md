---
id: SRT-NEURO-NEURAL32-RELATIONAL-CANDIDATE-CONSTRUCTION-IMPLIED-DYNAMICS
patch_id: PATCH-NEURO-NEURAL32-RELATIONAL-CANDIDATE-CONSTRUCTION-IMPLIED-DYNAMICS
type: bridge_patch
status: active
version: v0_1
canonical: false
claim_level: P3-P4
claim_mode: evidence
layer: operations
epistemic_layer: os
domain: Neuroscience
source_ids: [SRC-2026-08-12-NEURO-YASHIRO-BODY-SEMANTICS-IMPLIED-MOTION]
created: 2026-08-12
target_future_doc:
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  - Neuroscience/SRT_Neuro_Predictions_Table.md
  - Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
  - 01_Source_Intuition/BOOK/Drafts_26Q/Q02_对象化.md
related_claims: [structured_candidate_construction, high_level_visual_representation, objectification, action_relevance, representation_stabilization, L1, NEURAL18, NEURAL28, NEURAL30, G_hat_theta_implementation_bridge]
tags: [EBA, FBA, implied-motion, relational-representation, structured-candidate, action-dynamics, category-conditioned-dynamics, representation-stabilization, objectification]
---

# NEURAL32 — Relational candidate construction and category-conditioned implied dynamics

> **Boundary**: bounded P3 neuroscience / representation bridge with P4 discriminating experiments. This patch does not define canonical `L0`, `L1`, `L2`, `G_hat_theta`, `d`, `Psi_f`, objecthood, affordance, consciousness, subjecthood, or bearer formation. Its core use is narrower: high-level perceptual candidates should not be assumed to be isolated object labels, and the phrase “selection before representation” must not be read as denying precursor feature encoding or provisional representation.

## 1. Source anchor

Primary source:

- Yashiro R, Sawayama M, Yamashita A, Amano K. *Probing the content of semantic representations in body-selective regions*. *Imaging Neuroscience*, Volume 4 (2026). DOI `10.1162/IMAG.a.1309`.
- User-supplied published full PDF close-read.
- Human Natural Scenes Dataset 7T fMRI + caption-based encoding + object co-occurrence NMF + behavioral implied-motion ratings + vertex-wise correlations + variance partitioning.

Load-bearing source anchors are preserved in:

```text
Materials/2026/SRC_2026_08_12_Neuro_Yashiro_Body_Semantics_Implied_Motion.md
```

Most important source-level results:

1. `person x sports` co-occurrence is associated with the highest predicted EBA-response component, while `person x accessory` / `person x vehicle` are moderate-response patterns;
2. actual EBA/FBA responses correlate most strongly with implied human motion, number of people, and body size among six tested features;
3. implied motion uniquely explains the largest fraction of EBA vertices for 7/8 participants and FBA vertices for 5/8 participants;
4. implied-motion representation is substantially stronger for person images than animal or vehicle images (`p = 0.007`);
5. the authors explicitly treat the three identified features as incomplete and speculate that EBA integrates lower-/mid-level information into action-recognition-relevant intermediate representations.

---

## 2. Why this matters for SRT

Current SRT neuroscience often compresses the implementation picture into:

```text
accessible candidates
-> competition / gain / gating / stabilization
-> L1
```

That picture leaves one question under-specified:

> **What kind of thing is a perceptual candidate before stabilization?**

If candidates are tacitly modeled as labels such as:

```text
person
car
dog
chair
```

then the Yashiro results create pressure. Body-selective visual responses depend not only on the presence of a body but on scene relations and latent action-related features inferred from a static image.

The source therefore supports a bounded implementation correction:

> **A high-level perceptual candidate may already be a structured relational hypothesis rather than a bare category token.**

This does not replace the selection architecture. It specifies the possible **content geometry** over which selection and stabilization may later operate.

---

## 3. Main SRT bridge claim

### NEURAL32 core claim

> **Perceptual candidate construction can precede stabilized `L1` commitment. Candidate content may bind entities, relations, category-conditioned latent dynamics, and action-relevant properties before the system resolves which structured state becomes behaviorally or consciously dominant.**

Short form:

> **Selection-before-stabilized-representation is compatible with representation-before-selection at precursor and candidate-construction levels.**

This is a P3 bridge statement, not a canonical processing theorem.

---

## 4. Mapping table

| Source result | SRT-safe bridge use | Do not infer |
|---|---|---|
| `person x sports` produces strongest predicted EBA-response component | scene relation changes high-level representational content beyond category identity | sports context = `d`; object co-occurrence = selection |
| implied motion is reproducibly judged from static images | candidate content can include latent dynamics not physically unfolding in the current stimulus | implied motion = future selectability / affordance |
| implied motion / people count / body size correlate with actual EBA/FBA | high-level representation can be multidimensional and partly decomposable | EBA/FBA = `L1` |
| implied motion has largest unique vertex fraction for most subjects | latent dynamics contribute independently beyond size / people-count covariance | implied motion is the unique neural mechanism of action perception |
| person implied motion >> animal / vehicle implied motion | dynamic features may be category-conditioned rather than context-free scalar features | human-specific motion code = subjecthood or stake |
| authors propose low-/mid-level features feed EBA feature construction | precursor representation exists before higher-level body semantics | paper proves `G_hat_theta` or selection architecture |

---

## 5. Formal bridge — structured candidate content

Introduce only local bridge notation:

\[
c_i(t)=\langle E_i,R_i,D_i,A_i,K_i\rangle_t
\]

where:

- `E_i` = discriminated entities / body candidates;
- `R_i` = current scene relations;
- `D_i` = latent or implied dynamics;
- `A_i` = action / interaction relevance descriptor;
- `K_i` = category-conditioned constraints on how other features are interpreted.

The point is not that every candidate literally has five fields. The point is negative:

\[
c_i \neq \text{bare object label by default}.
\]

A neural implementation bridge can then be decomposed as:

\[
Enc_{precursor}
\rightarrow
Construct(\{c_i\})
\rightarrow
Select/Stabilize
\rightarrow
L_1.
\]

Only the existence of precursor feature information and structured high-level representation is pressured by the Yashiro source. `Select/Stabilize -> L1` is SRT architecture and is not directly tested by the paper.

---

## 6. New claim cluster

### NEURAL32-A — category identity is insufficient for candidate content

Within the source paradigm:

```text
person present
!= fixed high-level body representation
```

because co-occurring scene categories and inferred action dynamics systematically alter EBA/FBA response structure.

SRT use:

> Candidate identity should remain open to relational and contextual specification before stabilization.

### NEURAL32-B — latent dynamics can be represented without current physical motion

A static frame contains no unfolding velocity trajectory, yet participants reliably rate implied motion and body-selective cortex tracks that inferred property.

Bounded bridge:

```text
currently instantiated sensory property
!= full represented content
```

This is an inferential / representational claim, not an ontological claim that the brain creates external reality.

### NEURAL32-C — feature meaning can be category-conditioned

The person-versus-animal/vehicle contrast shows that the neural relevance of “implied motion” depends strongly on what kind of entity carries that motion.

Bounded bridge:

\[
D_{implied}\mid Category=person
\neq
D_{implied}\mid Category=vehicle
\]

at the level of body-selective cortical representation.

This creates pressure against an overly atomic additive model in which `object identity + generic speed scalar` fully specifies the represented state.

### NEURAL32-D — `L1` should be treated as a structured stabilized state, not a winner label

The source does not study canonical `L1`, but it constrains a neuroscience-facing interpretation. If multiple partially separable body features are distributed across EBA/FBA, then a plausible stabilized perceptual state may bind several dimensions rather than consist of one victorious category token.

SRT-side notation only:

\[
L_1^{percept}
\sim
Bind(c_*, context, task, body, history)
\]

not:

\[
L_1^{percept}=\operatorname{argmax}\{person,car,dog,...\}
\]

No new canonical equation is proposed.

### NEURAL32-E — selection-before-representation wording guard

The current neuroscience slogan:

```text
neural selection before representation
```

must be read as:

```text
selection before stabilized / committed L1 representation
```

not:

```text
selection before every sensory encoding,
feature representation,
or provisional candidate representation
```

The Yashiro Discussion explicitly assumes lower-/mid-level orientation and shape information can be integrated into higher-level body-related features. Therefore a literal “no representation before selection” sequence would be an unnecessary overclaim.

---

## 7. Interface with existing neuroscience patches

### NEURAL18 — selection-ready geometry

NEURAL18 separates decodability from causal access, behavior, conscious anchoring, and write-back.

NEURAL32 adds a content-side complement:

```text
NEURAL18:
representational geometry can be rich before anchoring

NEURAL32:
the candidate units within that geometry need not be bare labels;
they may already be relational/action-structured
```

Together:

```text
rich candidate geometry
!= current reality commitment
```

### NEURAL28 — re-identifiable object identity

NEURAL28 asks how an already individuated / identified object can be re-entered across changes in presentation and relation.

NEURAL32 is upstream:

```text
NEURAL32:
construct structured current candidate

-> stabilization / objectification

NEURAL28:
re-identify / re-enter the object across later changes
```

This is an explanatory relation, not a fixed anatomical pipeline.

### NEURAL30 — temporal integration / object formation

NEURAL30 shows that a temporally structured event history can be integrated into one current percept.

NEURAL32 adds a complementary scene-content route:

```text
temporal structure can shape object formation
+
relational / action structure can shape object formation
```

A future synthesis should therefore avoid treating objectification as either pure temporal closure or pure category selection.

---

## 8. P4 experimental / operational consequences

### H-NEURAL32a — relational model versus additive feature model

Construct matched natural-scene stimulus sets in which object identities are preserved while relations change.

Compare held-out neural prediction among:

```text
M1: object-category bag
M2: object categories + independent scalar features
M3: structured relation graph + category-conditioned dynamics
```

Prediction:

> If NEURAL32 captures real high-level organization, `M3` should add reproducible predictive variance beyond `M1/M2` in EBA/FBA or other category-selective regions after controlling low-level image statistics.

Failure condition:

If relational structure adds no held-out prediction after category counts, pose, size, retinal position, and generic motion priors are controlled, keep the source result local and reject the broader structured-candidate inference.

### H-NEURAL32b — same body / different action relation

Use the same or tightly matched human body pose while changing surrounding objects and relation structure so that implied action differs.

Examples:

```text
same body geometry
+ racket / ball relation
vs
same body geometry
+ umbrella / waiting relation
```

Measure whether EBA/FBA representation changes with inferred action after matching body size, center distance, face area, posture and low-level image statistics.

### H-NEURAL32c — generic implied motion versus category-conditioned implied motion

Build matched person / animal / vehicle stimuli with equivalent behavioral implied-speed ratings and comparable retinal size / spatial frequency.

Test whether category x implied-motion interaction remains after these controls.

A robust interaction would support category-conditioned dynamics rather than a generic speed code.

### H-NEURAL32d — precursor encoding versus stabilized perceptual commitment

Use MEG/EEG with an ambiguous relational scene paradigm plus fMRI-localized EBA/FBA or multivariate source priors.

Test for a temporal separation among:

```text
low-/mid-level feature encoding
-> structured candidate decoding
-> task/report-dependent stabilization
```

The discriminating target is not simply “later activity is stronger,” but whether structured candidate information is decodable before the final perceptual/report commitment and whether task/history manipulations selectively affect the later commitment stage.

This would directly test the wording guard:

```text
precursor representation exists
while stabilized commitment remains unresolved
```

---

## 9. Failure conditions

Weaken or reject the broad NEURAL32 bridge if:

1. the implied-motion effect disappears under tightly matched body pose, size, retinal position, action category and scene statistics;
2. relational graph models fail to add held-out neural prediction beyond additive object/feature models;
3. person-specific implied-motion effects are fully explained by generic biological-motion priors or motion-area spillover after individualized MT/MST localization;
4. future causal perturbation shows EBA/FBA response correlations are epiphenomenal and not used by downstream action recognition;
5. precursor feature and candidate representations cannot be temporally dissociated from the purported stabilization stage;
6. the bridge is expanded so loosely that any context sensitivity is relabeled “structured candidate construction” without a specified relational variable and negative control;
7. `structured candidate` becomes a substitute name for every representation, eliminating the distinction it was introduced to sharpen.

---

## 10. Boundary cautions

Do not write:

- `EBA = L1`;
- `EBA/FBA = G_hat_theta`;
- implied motion = affordance;
- implied motion = future selectability;
- implied motion = action policy;
- body size = proximity stake;
- number of people = social `d`;
- category-specific representation = subjecthood;
- category-specific representation = consciousness;
- co-occurrence matrix = neural relation graph;
- caption embedding = the brain's semantic code;
- “static-image motion representation proves reality is constructed”;
- “all representation precedes selection”;
- “all selection precedes every representation”;
- the three source features exhaust body semantics.

---

## 11. Integration hook

Primary hook:

```text
Neuroscience/hooks/NEURAL32_Relational_Candidate_Construction_Implied_Dynamics_Integration_Hook.md
```

Main future owner insertion:

```text
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
```

Preferred future synthesis sentence:

> **Neural selection should not be pictured as operating on a menu of already finished object labels. High-level visual candidates can already bind entity identity, relational context and latent action dynamics, while remaining distinct from the later process that stabilizes one structured state into current perceptual commitment. Thus “selection before representation” is best read as selection before stabilized `L1` representation, not before every precursor code or provisional candidate representation.**

---

## 12. One-paragraph abstract

Yashiro et al. show that body-selective visual cortex is sensitive to interpretable scene features extending beyond body-category identity. Model-guided analysis of 73,000 natural-scene captions identified `person x sports` as the highest predicted EBA-response relation, and direct fMRI analyses showed that implied human motion, number of people and body size independently contribute to EBA/FBA responses, with implied motion explaining the largest unique cortical fraction for most participants. Crucially, the implied-motion effect is substantially stronger for human bodies than for animals or vehicles, indicating category-conditioned rather than generic motion sensitivity. NEURAL32 uses this as a bounded P3 pressure on SRT neuroscience: perceptual candidates may be structured relational/action-relevant states rather than bare object labels, and precursor representations can exist before the later selection/stabilization that yields current `L1` commitment. No SRT primitive is identified with EBA, FBA, implied motion, caption embeddings or co-occurrence structure.
