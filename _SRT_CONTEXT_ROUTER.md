---
id: SRT-CONTEXT-ROUTER
type: retrieval_index
tags: [Context Router, Retrieval, Navigation, Deep Theory, AI Context]
status: draft_v1
layer: meta
epistemic_layer: meta
claim_mode: navigation
dependency: [_SRT_INDEX, SRT-AGENT-RETRIEVAL-PROFILE, CANONICAL_REGISTRY, SRT-ADJACENT-THEORY-INTERFACE-INDEX]
---

# SRT Context Router

> **Purpose**: This file helps AI agents and human editors retrieve the right context for deep SRT questions. It does not define theory. It routes questions to the files that should be read together.

> **Core rule**: Do not answer a deep SRT question from a single file if the route below lists multiple primary files. SRT concepts are often distributed across canonical anchors, bridge files, equations, and domain implementations.

---

## 0. Retrieval Protocol

When answering or editing a non-simple SRT question:

0. If the task is theory advancement, book writing, domain deep-dive, material fusion, public release, or repository governance, first classify it with `_SRT_AGENT_RETRIEVAL_PROFILE.md`.
1. Identify the nearest route below.
2. Read all **Primary** files first.
3. Add **Secondary** files when the question needs domain depth, writing context, evidence pressure, or adjacent-theory comparison.
4. Check the **Boundary** note before forming the answer.
5. If the question crosses domains, combine the relevant routes rather than inventing a new definition.
6. If a route points to a long owner file, check `LONGFORM_SPLITS.md` and use the split README for connector-safe reading.

`canonical: false` files may appear in Primary or Secondary context. That status prevents them from defining SRT; it does not remove their retrieval value.

---

## 1. Route: `Ψ_f` / Fisher / Information Geometry / Payability

**Use when the query mentions**: `Ψ_f`, Fisher metric, Fisher-Rao, information geometry, ontological friction, payability, selection cost, `Ψ_f ≡ g`, local cost.

### Primary

- `_SRT_PSI_F_CANONICAL.md`
- `_SRT_SYMBOL_TABLE.md`
- `SRT_Fisher_FEP_Landscape_Interface.md`
- `Core/SRT_Core_22_Equations.md`

### Secondary

- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`
- `_SRT_VERTICAL_INTEGRATION.md`
- `papers/ontological_friction/paper_ontological_friction.md`
- `SRT_EXP_MEASURE_MAP.md`（for experimental proxies）

### Boundary

- Do not read `Ψ_f ≡ g_F` as literal identity.
- Fisher geometry is a local projection / proxy, not `Ψ_f` itself.
- `Ψ_f` is primarily payability burden; geometry and metabolism are conditional projections.

---

## 2. Route: d-value / Stake / Concern Bandwidth / Consciousness Depth

**Use when the query mentions**: d-value, stake, concern, care, existential risk, effective dimension, Fisher spectrum, `D_eff`, consciousness depth.

### Primary

- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_SYMBOL_TABLE.md`
- `Core/SRT_Core_22_Equations.md`

### Secondary

- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`
- `Neuroscience/SRT_Clin_00_IIT_PCI.md`
- `AI/SRT_AI_03_Consciousness_Framework.md`
- `graphify-out/wiki/SRT_Consciousness_Conditions.md`
- `SRT_EXP_MEASURE_MAP.md`（for lab proxy mapping）

### Boundary

- Do not reduce `d-value` to Fisher effective dimension.
- Do not reduce `d-value` to IIT `Φ`, GNW access, preference strength, or pain.
- `D_eff`, Fisher rank, and bandwidth are capacity proxies unless stake-coupling and payability are satisfied.
- Graphify consciousness condition files are support-only and do not override `_SRT_D_VALUE_CANONICAL.md`.

---

## 3. Route: T_dir / Direction Transparency / Reorientation

**Use when the query mentions**: `T_dir`, direction transparency, current selection direction, readability, reorientation, direction access, orientation clarity.

### Primary

- `_SRT_T_DIR_CANONICAL.md`
- `_SRT_SYMBOL_TABLE.md`

### Secondary

- `Spirituality/SRT_Spirituality_Selection_Pathology_and_Return.md`
- `Spirituality/SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`
- `Spirituality/SRT_Spirit_09_Praxis_CompactCore.md`
- `_SRT_CROSS_DOMAIN_MATRIX.md`

### Boundary

- `T_dir` is a v0 operational proxy for directional readability / reorientation.
- It is not semantic valence, reward, confidence, or a completed ontology of will.
- Spirituality uses of `T_dir` must route back to `_SRT_T_DIR_CANONICAL.md`.

---

## 4. Route: Ghost Operator / Selection Operator / `Ĝθ`

**Use when the query mentions**: Ghost Operator, `Ĝ`, selection operator, collapse, anchoring, normalization, lateral inhibition, `L0 -> L1`.

### Primary

- `Core/SRT_Core_21_Formal_Axioms.md`
- `Core/SRT_Core_21_Minimal_Axioms.md`
- `Core/SRT_Core_21b_Constitutive_Theorems.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`

### Secondary

- `Core/SRT_Core_13a_Operator_Basics.md`
- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`
- `Neuroscience/SRT_Neural_Mechanisms.md`
- `Physics/SRT_Quant_01_Selection.md`
- `SRT_Fisher_FEP_Landscape_Interface.md`

### Boundary

- Divisive normalization is an implementation proxy, not the full Ghost Operator.
- Quantum measurement is a physical bridge instance, not the whole `Ĝθ`.
- GNW ignition is neural stabilization / availability, not the entire selection origin.

---

## 5. Route: `L0 / L1 / L2` Ontology and Domain Split

**Use when the query mentions**: `L0`, `L1`, `L2`, latent domain, manifest domain, convergence domain, ontology split, reality domains.

### Primary

- `Core_Law/SRT_L0_Metaphysics.md`
- `Core/SRT_Core_12a_Ontology_L0L1.md`
- `Core/SRT_Core_12b_Ontology_L2.md`

### Secondary

- `graphify-out/wiki/Ontology_Split_Index.md`（support-only generated index）
- `_SRT_VERTICAL_INTEGRATION.md`
- `SRT_Fisher_FEP_Landscape_Interface.md`
- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`
- `Philosophy/SRT_SocTheory_06_L2_Dynamics.md`

### Boundary

- `L0` is not nothingness.
- `L1` is not merely physical matter; it is actualized slice / event / manifest state.
- `L2` is not identical to any single landscape; landscapes are effective projections of stable constraint domains.
- `graphify-out/wiki/Ontology_Split_Index.md` is support-only; it is not a canonical source.

---

## 6. Route: Adjacent Theories / SRT Is Not Just X

**Use when the query asks**: Is SRT just FEP? IIT? GNW? Quantum collapse? Social constructionism? Multilevel selection?

### Primary

- `Bridge/SRT_Adjacent_Theory_Interface_Index.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- `SRT_Fisher_FEP_Landscape_Interface.md`

### Secondary

- `Philosophy/SRT_FEP_Comparison.md`
- `Neuroscience/SRT_Clin_00_IIT_PCI.md`
- `Neuroscience/SRT_Consciousness_Mechanisms.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Philosophy/SRT_Social_Cognition.md`
- `Philosophy/SRT_Social_Economics.md`

### Boundary

- Adjacent theories are interfaces, not replacements.
- Always state the SRT loop segment each theory addresses.

---

## 7. Route: FEP / Active Inference / Predictive Processing

**Use when the query mentions**: FEP, Active Inference, predictive processing, variational free energy, Markov blanket, generative model.

### Primary

- `Philosophy/SRT_FEP_Comparison.md`
- `SRT_Fisher_FEP_Landscape_Interface.md`
- `Neuroscience/SRT_Clin_02_FEP.md`

### Secondary

- `Core/SRT_Core_14_Dynamics_Scaling.md`
- `Bridge/SRT_Adjacent_Theory_Interface_Index.md`

### Boundary

- FEP belongs primarily to local self-maintenance under existing organization (`L2 -> L1`).
- FEP does not replace SRT's selection ontology.

---

## 8. Route: IIT / PCI / GNW / Consciousness Mechanisms

**Use when the query mentions**: IIT, `Φ`, PCI, GNW, global workspace, access consciousness, consciousness mechanisms, ignition, hard problem, explanatory gap.

### Primary

- `Neuroscience/SRT_Clin_00_IIT_PCI.md`
- `Neuroscience/SRT_Consciousness_Mechanisms.md`
- `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md`

### Secondary

- `Neuroscience/SRT_Neuro_09_Integ_Eq.md`
- `AI/SRT_AI_03_Consciousness_Framework.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`
- `SRT_EXP_MEASURE_MAP.md`
- `graphify-out/wiki/SRT_Consciousness_Conditions.md`
- `graphify-out/wiki/SRT_Hard_Problem_Epistemology.md`

### Boundary

- IIT / PCI are integration or complexity readouts.
- GNW is global availability / broadcast.
- Neither defines `d-value` or `Ψ_f`.
- Graphify consciousness pages are support-only and should not outrank canonical consciousness / d-value / Ψ_f sources.

---

## 9. Route: Quantum Measurement / Decoherence / Quantum Darwinism

**Use when the query mentions**: quantum measurement, collapse, decoherence, pointer states, Quantum Darwinism, measurement as selection.

### Primary

- `Physics/SRT_Quant_00_Intro.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Physics/SRT_Quant_01_Selection_CompactCore.md`

### Secondary

- `graphify-out/wiki/Measurement_as_Selection.md`
- `graphify-out/wiki/Objective_Measurement_Theorem.md`
- `graphify-out/wiki/Quantum_Darwinism_Equivalence.md`
- `graphify-out/wiki/Theorem_of_Decoherence_Insufficiency.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`

### Boundary

- Quantum measurement is a physical `L0 -> L1` bridge instance.
- SRT is not reducible to quantum collapse theory.

---

## 10. Route: Multilevel Selection / Evolution / Niche Construction

**Use when the query mentions**: multilevel selection, evolutionary selection, niche construction, ecological inheritance, evolutionary feedback, selection levels.

### Primary

- `papers/ontological_friction/paper_ontological_friction.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`

### Secondary

- `Philosophy/SRT_SocTheory_05_Language_Eco.md`
- `Philosophy/SRT_SocTheory_06_L2_Dynamics.md`
- `Core/SRT_Core_12b_Ontology_L2.md`
- `Core/SRT_Core_14_Dynamics_Scaling.md`

### Boundary

- Always specify the selection level.
- Always specify where consequences return.
- Do not use “selection” as an undifferentiated keyword.

---

## 11. Route: Language / Social Reality / Institutions / L2 Social Layer

**Use when the query mentions**: language, social reality, institutions, norms, money, law, roles, social construction, social cognition, social `L2`, L2 dynamics.

### Primary

- `Philosophy/SRT_Social_Cognition.md`
- `Philosophy/SRT_Social_Economics.md`
- `Philosophy/SRT_Social_Economics_CompactCore.md`
- `Philosophy/SRT_Social_MacroDynamics.md`
- `Philosophy/SRT_SocTheory_05_Language_Eco.md`
- `Philosophy/SRT_SocTheory_06_L2_Dynamics.md`

### Secondary

- `graphify-out/wiki/Social_Reality_Construction.md`
- `graphify-out/wiki/Language_Topology.md`
- `graphify-out/wiki/Normative_Closure.md`
- `Core/SRT_Core_12b_Ontology_L2.md`

### Boundary

- Social construction is a human-social `L2` case, not the full SRT ontology.
- Language stabilizes and authorizes selection paths; it does not replace selection itself.

---

## 12. Route: AI Consciousness / AI Ontology / Synthetic Operators

**Use when the query mentions**: AI consciousness, synthetic subject, model consciousness, artificial `d`, artificial `Ψ_f`, OpenClaw / agent relevance to SRT.

### Primary

- `AI/SRT_AI_01_Ontology_CompactCore.md`
- `AI/SRT_AI_03_Consciousness_Framework.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`

### Secondary

- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`
- `Neuroscience/SRT_Consciousness_Mechanisms.md`
- `Bridge/SRT_Adjacent_Theory_Interface_Index.md`
- `SRT_EXP_TEMPLATE.md`
- `graphify-out/wiki/SRT_Consciousness_Conditions.md`

### Boundary

- Simulated loss or optimization is not automatically stake.
- Non-binding friction is not the same as existentially paid `Ψ_f`.
- AI discussions must separate functional access, integration, payability, and stake.

---

## 13. Route: Experimental Proxies / Measurement / Falsification

**Use when the query mentions**: experiment, measurement, proxy, falsification, lab, operationalization, variables, protocol, empirical test, `HRV`, `SCR`, PCI proxy, Fisher proxy, ROS proxy, task switching, measure map.

### Primary

- `SRT_EXP_MEASURE_MAP.md`
- `SRT_EXP_TEMPLATE.md`
- `Governance/SRT_LAB_HYPOTHESES.md`
- `_SRT_EQ_HYP_MAP.md`

### Secondary

- `Neuroscience/SRT_Neuro_Experiments.md`
- `_SRT_PSI_F_CANONICAL.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `Core/SRT_Core_22_Equations.md`
- `papers/ontological_friction/paper_ontological_friction.md`
- `Operations/_SRT_DEEP_NAV_AUDIT_2026-04-24.md`

### Boundary

- Experimental proxies do not replace canonical definitions.
- Lab-layer canonical templates do not automatically promote a variable to core theorem status.
- Proxy conclusions must state operational scope and cannot be back-projected as ontology.

---

## 14. Route: Political Philosophy / Ethics / Normativity

**Use when the query mentions**: political philosophy, ethics, rights, normativity, justice, governance, social order, collective `d`.

### Primary

- `Philosophy/SRT_Political_Philosophy.md`
- `Philosophy/SRT_Political_Philosophy_CompactCore.md`
- `Philosophy/SRT_Political_Rights.md`
- `Core/SRT_Core_12b_Ontology_L2.md`

### Secondary

- `Philosophy/SRT_Social_MacroDynamics.md`
- `Philosophy/SRT_Social_Economics.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`

### Boundary

- Political claims are application-level or philosophy-domain claims unless explicitly promoted through the claim ladder.
- Do not confuse descriptive `L2` stabilization with normative endorsement.

---

## 15. Route: Spirituality / Subject-Position / Return Path

**Use when the query mentions**: spirituality, subject-position, loss of self, return path, sangha, community, practice, existential orientation.

### Primary

- `Spirituality/SRT_Spirituality_Selection_Pathology_and_Return.md`
- `Spirituality/SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`
- `Spirituality/SRT_Spirituality_Community_and_Sangha.md`
- `Spirituality/SRT_Spirit_09_Praxis_CompactCore.md`

### Secondary

- `_SRT_T_DIR_CANONICAL.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`

### Boundary

- Spirituality files are praxis / existential interpretation layers.
- They should not override core definitions of `d`, `Ψ_f`, `T_dir`, or `L0-L1-L2`.

---

## 16. Route: Open Tensions / Unresolved Problems

**Use when the query mentions**: unresolved, open tension, contradiction, critique, vulnerability, review risk.

### Primary

- `Core/SRT_OPEN_TENSIONS.md`
- `Governance/SRT_CLAIM_LADDER.md`
- `Governance/SRT_CLAIM_MODE_AUDIT.md`

### Secondary

- Relevant canonical anchor depending on the topic.
- `Operations/_SRT_DEEP_NAV_TODO.md`
- `Operations/_SRT_DEEP_NAV_AUDIT_2026-04-24.md`

### Boundary

- Do not patch a tension by silently upgrading a bridge claim.
- Record whether the issue is conceptual, mathematical, empirical, or editorial.

---

## 17. Route: Writing / Article Framing / Public Communication

**Use when the query mentions**: article topic, writing, media, public communication, Medium, Substack, video script, social post, topic planning.

### Primary

- `SRT_TOPIC_ARTICLE_INDEX.md`
- `Operations/_SRT_MEDIA_PIPELINE.md`

### Secondary

- `SRT_Navigation_Map.md`
- `SRT_Quick_Start.md`
- Relevant theory route depending on selected topic

### Boundary

- Writing indexes route theory into article topics; they do not define theory.
- Always return to canonical anchors before making strong claims in public-facing writing.

---

## 18. Route: Publication / Paper Preparation / Review Risk

**Use when the query mentions**: paper, publication, manuscript, submission, journal fit, reviewer risk, Entropy, JCS, ALIFE, internal review.

### Primary

- `Operations/_SRT_PAPER_PIPELINE.md`
- `papers/working_notes/PAPER_INTERNAL_REVIEW_ACTIONS_2026-03-02.md`
- `Core/SRT_OPEN_TENSIONS.md`

### Secondary

- `papers/ontological_friction/paper_ontological_friction.md`
- `papers/SRT_MetaOS_JCS_v1.md`
- `papers/SRT_MetaOS_JCS_v2.md`
- `papers/SRT_MetaOS_JCS_reframe.md`
- `papers/ALIFE2026_SelectiveRealityConstruction_v14_anonymous_submission.html`
- Relevant canonical file and bridge file for the paper topic

### Boundary

- Paper drafts should not outrank canonical files unless explicitly promoted through the registry.
- Review-risk edits must not silently upgrade bridge claims into core claims.

---

## 19. Route: Book Writing / Manuscript Continuity

**Use when the query mentions**: book, chapter, manuscript, volume, 卷, 章节, 书稿, polish, third-tier writing, source intuition, continuity, inclusion matrix, consistency pass.

### Primary

- `_SRT_AGENT_RETRIEVAL_PROFILE.md`（Book Writing profile）
- `01_Source_Intuition/README.md`
- `01_Source_Intuition/INDEX.md`
- `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`
- `01_Source_Intuition/BOOK/Outline_Parts/README.md`
- `90_Backstage/Restructure_2026/BOOK_PROJECT/repository_material_inclusion_matrix.md`

### Secondary

- `90_Backstage/Restructure_2026/BOOK_PROJECT/book_writing_style_guide.md`
- `90_Backstage/Restructure_2026/BOOK_PROJECT/philosophical_style_rules.md`
- `90_Backstage/Restructure_2026/BOOK_PROJECT/part01_consistency_closure_2026-05-10.md`
- `90_Backstage/Restructure_2026/BOOK_PROJECT/part01_consistency_precision_pass_2026-05-10.md`
- relevant current chapter files under `01_Source_Intuition/BOOK/`
- relevant formal anchors only as accuracy guardrails

### Boundary

- Book files are high retrieval value but not canonical definition sources.
- Use formal anchors to keep terms accurate, but do not write the book in registry style.
- Backstage notes preserve continuity and editorial decisions; they do not create new theory authority.

---

## 20. Maintenance Rule

Whenever a new deep file is created:

1. Add it to `_SRT_INDEX.md` only if it is an entry surface or domain hub.
2. Add it to `_SRT_CONTEXT_ROUTER.md` if it should be retrieved for a recurring question type.
3. Add it to `_SRT_DEEP_THEORY_MAP.md` if it represents a major theory node.
4. Add a task to `Operations/_SRT_DEEP_NAV_TODO.md` if its route, boundary, or cross-references are incomplete.
