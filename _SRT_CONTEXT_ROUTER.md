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
- `Neuroscience/SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md`（only for the bounded P4 neural-normalization → task-choice workline）
- `Physics/SRT_Quant_01_Selection.md`
- `SRT_Fisher_FEP_Landscape_Interface.md`

### Boundary

- Divisive normalization is an implementation proxy, not the full Ghost Operator.
- A normalized neural response is not yet a behavioral choice: use `Core_14 P3-Scale-NB1` and require a frozen readout, event／execution gate, held-out error, rival comparison, and intervention tracking.
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

**Use when the query asks**: Is SRT just FEP? IIT? GNW? Quantum collapse? Social constructionism? Multilevel selection? Enactivism? Process philosophy? Buddhist metaphysics?

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
- `Philosophy/SRT_Philosophy_Foundations.md`
- `Spirituality/SRT_Spirituality_Selection_Pathology_and_Return.md`

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

## 8a. Route: Object Individuation / Identification / Subjecthood Negative Control

**Use when the query mentions**: object individuation, object identification, object tracking, object index, infant object representation, `still this one`, minimal subject, bearer individuation, subjecthood negative control.

### Primary

- `Philosophy/_SRT_Philosophy_Hardening_Index.md`（§ PH-IND01 object / subject individuation bridge）

### Secondary

- `Philosophy/patches/SRT_Philosophy_PH_IND01_Object_Subject_Individuation_Before_Identification_v0_1.md`
- `Philosophy/SRT_Subjecthood_Threshold_Interface.md`
- `Core_Law/SRT_Individuation.md`

### Boundary

- Object individuation can precede rich identification; this is a cognition-level distinction.
- Object-tracking continuity is not consequence-bearing continuity.
- An object index is not a minimal subject and does not establish consciousness.
- Use PH-IND01 as a subjecthood negative control, not as evidence transfer from infant object cognition to SRT bearer formation.

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

## 12a. Route: LLM Context / Selection Coherence / Human Understanding

**Use when the query mentions**: context window, long context, LLM intelligence, selection coherence, shared context, understanding, semantic continuity, conversational memory, role consistency.

### Primary

- `Bridge/SRT_Context_Coherence_Intelligence_Interface.md`
- `AI/SRT_AI_Architecture_CompactCore.md`
- `AI/SRT_AI_01_Ontology_CompactCore.md`
- `Philosophy/SRT_SocTheory_05_Language_Eco.md`

### Secondary

- `AI/SRT_AI_Claim_Status.md`
- `AI/AI_POSITIONING_NOTE.md`
- `Philosophy/SRT_Social_Cognition.md`
- `Bridge/SRT_Adjacent_Theory_Interface_Index.md`

### Boundary

- Context coherence is not `d-value`.
- Shared context is not subjecthood.
- LLM selection consistency is not ontological anchoring.
- Do not upgrade functional intelligence into consciousness or stake.

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
- `Neuroscience/SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md`（local P4 execution card; not a global Lab hard bet）

### Boundary

- Experimental proxies do not replace canonical definitions.
- Lab-layer canonical templates do not automatically promote a variable to core theorem status.
- Proxy conclusions must state operational scope and cannot be back-projected as ontology.
- `NB1-MOFC-Lottery-v0` remains yellow until formal lock, preregistration, execution, and within-workline intervention/rival gates are complete; cross-study evidence may not be assembled into a pass.

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
- Gate B / Shoshin layering is closed by B-A; Gate C / global-optimum scope is closed by C-A. Route to `Core_Law/SRT_L0_Metaphysics.md` 初心词条, `_SRT_D_VALUE_CANONICAL.md §5b`, and the two author records `Operations/SRT_SHOSHIN_LAYER_AUTHOR_DECISION_PACKET_2026-08-12.md` / `Operations/SRT_GLOBAL_OPTIMUM_AUTHOR_DECISION_PACKET_2026-08-12.md`. The separate CΨ `Ψ_f→0` valence question remains open in `Core/SRT_OPEN_TENSIONS.md §18`.

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
- `01_Source_Intuition/BOOK/BOOK_ARCHITECTURE_MAP_2026-06-03.md`
- `01_Source_Intuition/BOOK/BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_2026-06-03.md`
- `01_Source_Intuition/BOOK/BOOK_PROBLEM_CHAIN_REWRITE_2026-05-21.md`
- `01_Source_Intuition/BOOK/BOOK_CHAPTER_CARDS_2026-05-22.md`
- `90_Backstage/Restructure_2026/BOOK_PROJECT/repository_material_inclusion_matrix.md`

### Secondary

- `90_Backstage/Restructure_2026/BOOK_PROJECT/book_writing_style_guide.md`
- `90_Backstage/Restructure_2026/BOOK_PROJECT/philosophical_style_rules.md`
- `90_Backstage/Restructure_2026/BOOK_PROJECT/part01_consistency_closure_2026-05-10.md`
- `90_Backstage/Restructure_2026/BOOK_PROJECT/part01_consistency_precision_pass_2026-05-10.md`
- relevant current chapter files under `01_Source_Intuition/BOOK/Drafts_26Q/`
- relevant formal anchors only as accuracy guardrails

### Boundary

- Book files are high retrieval value but not canonical definition sources.
- Use formal anchors to keep terms accurate, but do not write the book in registry style.
- Backstage notes preserve continuity and editorial decisions; they do not create new theory authority.
- Root-level `Outline_Parts/` belonged to the old 52-chapter route and now lives under `01_Source_Intuition/BOOK/Archive_52Chapter/`; do not use it as the current construction path.

---

## 21. Route: Core 24 — Floor Replacement / Dynamic Normativity / Non-Reductive Verification

> Merged from `_SRT_CONTEXT_ROUTER_CORE24_EXTENSION.md` (2026-07-20).

**Use when the query mentions**: explanatory power, object-first ontology, wrong floor, floor replacement, selection-first ontology, purpose, value, morality, framework, normativity, moral constraint, non-reductive verification, indirect measurement, structural validation, core concepts hard to measure, SRT as 万能解释, SRT as 玄学, reviewer-risk guardrails.

### Primary

- `Core/SRT_Core_24_Index.md`
- `Core/SRT_Core_24_Floor_Normativity_Verification.md`
- `Core/SRT_Core_24_Canonical_Merge_Draft.md`
- `Core/SRT_Core_21_Minimal_Axioms.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`

### Secondary

- `Core/SRT_Core_12b_Ontology_L2.md`
- `Core/SRT_OPEN_TENSIONS.md`
- `SRT_EXP_MEASURE_MAP.md`
- `Governance/SRT_CLAIM_LADDER.md`
- `Philosophy/SRT_SocTheory_06_L2_Dynamics.md`
- `Philosophy/SRT_Political_Philosophy.md`

### Boundary

- Core 24 is a partially integrated bridge-hardening and canonical-framing layer, not a completed P0/P1 theorem package.
- Do not frame SRT as "explaining everything"; frame it as replacing object-first ontology with selection-first ontology.
- Do not treat "not directly measurable" as "beyond verification."
- Do not treat "morality as L2 constraint" as automatic moral endorsement.
- Do not treat value as reward / preference / salience; use concern-weighted non-substitutability under consequence return.
- Do not treat `Ψ_f` as task difficulty, pain, effort, energy, Fisher metric, prediction error, or stress marker.
- Any further canonical promotion must go through the claim ladder.

---

## 22. Route: Core 25 / Core 26 — Thermodynamic Signatures & MISA Attractor

> Merged from `_SRT_CONTEXT_ROUTER_CORE25_CORE26_EXTENSION.md` (2026-07-20).

**Route A — Thermodynamic Signatures / Irreversibility / Arrow of Time.** Use when the query mentions: Thermodynamics of Mind, irreversibility, arrow of time, entropy production, broken detailed balance, neural hierarchy, turbulence, hierarchy flattening, thermodynamic signatures of consciousness, empirical proxies for `Ψ_f` / `d-value` / `Ĝθ`.

- **Primary**: `Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md`, `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`, `_SRT_PSI_F_CANONICAL.md`, `_SRT_D_VALUE_CANONICAL.md`, `SRT_EXP_MEASURE_MAP.md`
- **Secondary**: `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md`, `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md`, `Core/SRT_Core_22_Equations.md`, `SRT_Fisher_FEP_Landscape_Interface.md`
- **Boundary**: irreversibility is a selection signature, not consciousness itself; entropy production is a domain proxy, not literal identity with `Ψ_f`; turbulence is a candidate implementation mechanism, not the Ghost Operator; consciousness-relevant use must include `d-value`, payability, anchoring, and global availability / loop closure.

**Route B — MISA Attractor / Mutual Inhibition / Self Activation / L2 Hardening.** Use when the query mentions: MISA, mutual inhibition, self activation, attractor basin, bistability, tristability, hybrid attractor, cell fate, Evo-Devo, neural category formation, habit hardening, identity attractor, social institutional lock-in, AI role attractor.

- **Primary**: `Core/SRT_Core_26_MISA_Attractor_Interface.md`, `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`, `Core_Law/SRT_Reference_Dynamics.md`, `_SRT_PSI_F_CANONICAL.md`, `_SRT_D_VALUE_CANONICAL.md`
- **Secondary**: `Core/SRT_Core_12b_Ontology_L2.md`, `Philosophy/SRT_SocTheory_06_L2_Dynamics.md`, `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md`, `AI/SRT_AI_Claim_Status.md`, `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md`
- **Boundary**: MISA is an implementation-level bridge, not a new SRT axiom; attractor stability does not imply high `d-value`; AI role attractors do not imply moral patienthood or subjecthood; hybrid attractors are possible stable basins, not automatic normative improvements; use `Ψ_f` and payability to distinguish adaptive hardening from brittle or pathological hardening.

---

## 23. Route: Reselectability / Objecthood / Reward–Reselectability Dissociation

> Merged from `_SRT_CONTEXT_ROUTER_RESELECTABILITY_ADDENDUM.md` (2026-07-20). Primary sources are now parked under `90_Backstage/Incubation/`; see `_SRT_PARKED_INDEX.md`.

**Use when the query mentions**: reselectability, re-sampling capacity, option-diversity, objecthood, object-health, reward-health / re-sampling-death, reward–reselectability dissociation, future reopening, foreclosure, ChoiceMap, AI governance audit, performance purchased by hidden loss of future choice, system health beyond performance.

### Primary

- `90_Backstage/Incubation/_SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md`
- `90_Backstage/Incubation/_SRT_DIRECTION2_WEDGE1_SIM_RESULTS.md`
- `90_Backstage/Incubation/_SRT_DIRECTION2_MORAL_GENEALOGY_SEED.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_T_DIR_CANONICAL.md`
- `Core/SRT_OPEN_TENSIONS.md`

### Secondary

- `Product/ChoiceMap/CHOICEMAP_RESELECTABILITY_PRODUCT_EXPLANATION_2026-07-01.md`
- `Governance/AI_RESELECTABILITY_AUDIT_FRAME_2026-07-01.md`
- `Public_Content/SRT_RESELECTABILITY_PUBLIC_SHORT_2026-07-01.md`

### Boundary

- Do **not** reduce reselectability to current reward, long-term reward, entropy, option count, or generic robustness.
- Do **not** identify toy `pre_div` with canonical d-value, or re-sampling capacity with canonical T_dir.
- Do **not** claim the toy wedge validates SRT ontology or morality, or infer equal moral status for all objects.
- Do **not** use this route to derive or override AM-A's P0-04 primitive boundary, nor to solve closure-boundary or externalization/X.
- Keep three layers separate: ontology (objecthood as maintained consequence-bearing reselectable closure), dynamics (reward/performance can diverge from future reselectability), morality/governance (moral pressure opens when one position's selection compresses another's reselectability, but X/externalization remains under-defined).

---

## 23a. Route: Choice Generation Conditions / Real Selection Event / Pseudo-Choice

**Use when the query mentions**: 这算不算真的选择, real choice vs script, 伪选择 / pseudo-choice, 惩罚性选择, "the AI chose", 输出不同是否等于选择, 建议是否等于决策, 后果落到谁身上, consequence-bearing position, 有记忆是否等于历史写回, 选择生成条件, 选择事件判据, CG-0..CG-4, DMF / NER / PEF / CBP / HEF, 统一选择事件审计, 耗散结构是不是选择.

### Primary

- `03_Bridges/SRT_Selection_Event_CompactCore.md` — 快速判别层（五门、五把梯子、三门槛、四类实践判读）；**先读这一份**
- `Core/SRT_Core_21b_Constitutive_Theorems.md` — P1-T05 Real Choice Moment（canonical 承载点）
- `03_Bridges/SRT_Choice_Generation_Conditions_2026-08-04.md` — T-D 条件矩阵全文（P2-P3）
- `Core/SRT_OPEN_TENSIONS.md §14` — 门槛与判别增益尚未闭合

### Secondary

- `Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md` — 分级门定义、边界冻结要求、六种拼接陷阱
- `03_Bridges/SRT_Entropy_Disturbance_Selective_Reorganization_Bridge_2026-08-04.md` — T-B 过程层
- `03_Bridges/SRT_Dissipative_Structures_and_Selection_Structures_Bridge_2026-08-04.md` — T-E 耗散／选择分层
- `03_Bridges/SRT_Selection_Dynamics_MSD_Bridge.md` — 排除／定形／写入／锚定／回流串联
- `Operations/SRT_CHOICE_TRACE_AUTHOR_DECISIONS_2026-08-04.md` — G1 可再选择性、G2 耗散分层的作者裁决
- `Operations/Audits/SRT_CHOICE_EVENT_BEHAVIOR_REGRESSION_TESTS_2026-08-06.md` — 12 道行为回归题

### Boundary

- 本路由全部内容为 **P2-P3**；`CG-0..CG-4`、五把梯子与最低门槛 **不是** canonical 判据，不得用于裁定 `d` / `Ψ_f` / `T_dir` / `Ĝ_θ` / `L_0-L_2` 的定义。
- 五门达标只允许说“**有界选择事件候选**”，**不**等于主体性、意识、自由意志、伦理责任、`L_2` 或生成健康。
- 不可补偿：任一门未达最低等级，不得由其他门的高等级补偿；不同事件、边界或时间尺度的证据不得拼接。
- **不要**把输出差异（`PEF-0`）、建议接口（`PEF-1`）、一般耗能（`CBP-1`）或短期状态携带（`HEF-1`）读成对应条件已成立。
- **不要**把惩罚性选择说成“没有选择”——这遮蔽真实承担与结构责任；也不要把“选项少”当作伪选择的判据。
- **不要**把可再选择性写成选择发生的必要条件（作者裁决 G1 为限定性确认）。
- **不要**把耗散结构写成选择的普遍必要前身（作者裁决 G2 为分层）。
- 生成条件、事件判据、脚手架、生成健康四者分工固定，不得互相替代。

---

## 24. Maintenance Rule

Whenever a new deep file is created:

1. Add it to `_SRT_INDEX.md` only if it is an entry surface or domain hub.
2. Add it to `_SRT_CONTEXT_ROUTER.md` if it should be retrieved for a recurring question type.
3. Add it to `_SRT_DEEP_THEORY_MAP.md` if it represents a major theory node.
4. Add a task to `Operations/_SRT_DEEP_NAV_TODO.md` if its route, boundary, or cross-references are incomplete.

When a Core-NN extension route matures, fold it directly into this router (as done for the Core 24 / 25 / 26 / reselectability routes on 2026-07-20) rather than creating a new standalone `_SRT_CONTEXT_ROUTER_*_EXTENSION.md` file. New router routes must not spawn new sidecar files.
