---
id: SRT-DEEP-NAV-AUDIT-2026-04-24
type: audit_report
tags: [Navigation, Audit, Context Router, Deep Theory Map, Retrieval]
status: completed_initial_audit
layer: operations
epistemic_layer: meta
claim_mode: navigation
dependency: [_SRT_CONTEXT_ROUTER, _SRT_DEEP_THEORY_MAP, Operations/_SRT_DEEP_NAV_TODO]
---

# SRT Deep Navigation Audit — 2026-04-24

> **Scope**: Initial audit of `_SRT_CONTEXT_ROUTER.md` and `_SRT_DEEP_THEORY_MAP.md` for path validity and missing deep-content routes.

> **Result**: The main deep-theory skeleton is valid and usable, but the map is not yet full-coverage. Two path corrections and several route enrichments are recommended.

---

## 1. Check A — Route Path Validity

### 1.1 General result

Most primary routes in `_SRT_CONTEXT_ROUTER.md` and `_SRT_DEEP_THEORY_MAP.md` point to existing high-value files. The following route groups are structurally valid:

- `Ψ_f / Fisher / Information Geometry`
- `d-value / Stake`
- Ghost Operator / `Ĝθ`
- `L0 / L1 / L2`
- Adjacent Theories
- FEP / Active Inference
- IIT / PCI / GNW
- Quantum Measurement / Decoherence
- Language / Social Reality
- AI Consciousness
- Political Philosophy
- Spirituality / Subject-Position
- Open Tensions

### 1.2 Confirmed high-value route files

The audit confirmed that the following referenced files exist and are appropriate as route anchors or support files:

- `_SRT_PSI_F_CANONICAL.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_SYMBOL_TABLE.md`
- `SRT_Fisher_FEP_Landscape_Interface.md`
- `Core/SRT_Core_22_Equations.md`
- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`
- `Core/SRT_Core_12b_Ontology_L2.md`
- `Core_Law/SRT_L0_Metaphysics.md`
- `Core_Law/SRT_Constitution_Seven_Theses.md`
- `AI/SRT_AI_01_Ontology_CompactCore.md`
- `AI/SRT_AI_03_Consciousness_Framework.md`
- `SRT_TOPIC_ARTICLE_INDEX.md`
- `SRT_EXP_TEMPLATE.md`
- `Operations/_SRT_PAPER_PIPELINE.md`
- `Operations/_SRT_MEDIA_PIPELINE.md`
- `papers/working_notes/PAPER_INTERNAL_REVIEW_ACTIONS_2026-03-02.md`
- `graphify-out/wiki/Ontology_Split_Index.md`
- `graphify-out/wiki/SRT_Consciousness_Conditions.md`
- `graphify-out/wiki/SRT_Hard_Problem_Epistemology.md`
- `Philosophy/SRT_SocTheory_06_L2_Dynamics.md`

### 1.3 Path corrections needed

#### Correction 1 — Consciousness Conditions

Current route references:

```text
Philosophy/SRT_Consciousness_Conditions.md
```

Observed file:

```text
graphify-out/wiki/SRT_Consciousness_Conditions.md
```

Recommended action:

- Replace `Philosophy/SRT_Consciousness_Conditions.md` with `graphify-out/wiki/SRT_Consciousness_Conditions.md` in:
  - `_SRT_CONTEXT_ROUTER.md`
  - `_SRT_DEEP_THEORY_MAP.md`

Boundary:

- Since this is a graphify output, keep it as support file, not primary canonical anchor.

#### Correction 2 — Ontology Split Index

Current route references:

```text
Ontology_Split_Index.md if available in current navigation context
```

Observed file:

```text
graphify-out/wiki/Ontology_Split_Index.md
```

Recommended action:

- Replace vague context-dependent wording with explicit support path:

```text
graphify-out/wiki/Ontology_Split_Index.md
```

Boundary:

- Treat as graphify support / navigation artifact, not canonical ontology source.

---

## 2. Check B — Missing Deep-Content Routes

### 2.1 L2 Dynamics enrichment

Observed file:

```text
Philosophy/SRT_SocTheory_06_L2_Dynamics.md
```

Recommended route additions:

- `_SRT_CONTEXT_ROUTER.md Route 4: L0 / L1 / L2`
- `_SRT_CONTEXT_ROUTER.md Route 10: Language / Social Reality / Institutions`
- `_SRT_DEEP_THEORY_MAP.md Node 4: L2 Sedimentation / Constraint Domain`
- `_SRT_DEEP_THEORY_MAP.md Node 12: Social Reality / Language / Institution`

Reason:

- This file is likely a deep bridge between social theory and L2 dynamics. It should not be omitted from L2/social routes.

---

### 2.2 Hard Problem / Consciousness Epistemology enrichment

Observed file:

```text
graphify-out/wiki/SRT_Hard_Problem_Epistemology.md
```

Recommended route additions:

- `_SRT_CONTEXT_ROUTER.md Route 7: IIT / PCI / GNW / Consciousness Mechanisms`
- `_SRT_DEEP_THEORY_MAP.md Node 10: Consciousness Node`

Boundary:

- Graphify output; use as support only. Do not let it override canonical d-value, Ψ_f, or AI consciousness files.

---

### 2.3 Writing / Article Route missing

Observed file:

```text
SRT_TOPIC_ARTICLE_INDEX.md
```

Recommended route addition:

Create a new route in `_SRT_CONTEXT_ROUTER.md`:

```markdown
## Route: Writing / Article Framing / Public Communication
```

Primary:

- `SRT_TOPIC_ARTICLE_INDEX.md`
- `Operations/_SRT_MEDIA_PIPELINE.md`

Secondary:

- `SRT_Navigation_Map.md`
- `SRT_Quick_Start.md`
- relevant theory route depending on topic

Boundary:

- Writing index is not a theory source. It routes deep theory into article topics.

---

### 2.4 Experiment / Lab Route missing

Observed file:

```text
SRT_EXP_TEMPLATE.md
```

Recommended route addition:

Create a new route in `_SRT_CONTEXT_ROUTER.md`:

```markdown
## Route: Experiment / Lab Hypotheses / Falsification
```

Primary:

- `SRT_EXP_TEMPLATE.md`
- `Governance/SRT_LAB_HYPOTHESES.md`
- `SRT_EXP_MEASURE_MAP.md` if present

Secondary:

- `Core/SRT_OPEN_TENSIONS.md`
- relevant canonical file depending on hypothesis

Boundary:

- Lab files are experimental / falsification interfaces, not new canonical theory definitions.

---

### 2.5 Paper / Publication Route missing

Observed files:

- `Operations/_SRT_PAPER_PIPELINE.md`
- `papers/working_notes/PAPER_INTERNAL_REVIEW_ACTIONS_2026-03-02.md`
- `papers/ontological_friction/paper_ontological_friction.md`
- `papers/SRT_MetaOS_JCS_v1.md`
- `papers/SRT_MetaOS_JCS_v2.md`
- `papers/SRT_MetaOS_JCS_reframe.md`
- `papers/ALIFE2026_SelectiveRealityConstruction_v14_anonymous_submission.html`

Recommended route addition:

Create a new route in `_SRT_CONTEXT_ROUTER.md`:

```markdown
## Route: Publication / Paper Preparation / Review Risk
```

Primary:

- `Operations/_SRT_PAPER_PIPELINE.md`
- `papers/working_notes/PAPER_INTERNAL_REVIEW_ACTIONS_2026-03-02.md`
- `Core/SRT_OPEN_TENSIONS.md`

Secondary:

- relevant paper file
- relevant canonical file
- relevant bridge file

Boundary:

- Paper drafts should not outrank canonical files unless explicitly promoted through the registry.

---

## 3. Coverage Assessment

### Current coverage estimate

| Area | Coverage | Status |
|---|---:|---|
| Core ontology / L0-L1-L2 | High | Minor path correction needed |
| Ψ_f / Fisher / payability | High | Good |
| d-value / stake | High | Add graphify consciousness condition support |
| Ghost Operator | High | Good |
| FEP / adjacent theories | High | Good |
| IIT/GNW / consciousness | Medium-high | Add Hard Problem / Consciousness Conditions support |
| Quantum measurement | High | Good |
| L2 / social reality | Medium-high | Add `SRT_SocTheory_06_L2_Dynamics.md` |
| AI consciousness | High | Good |
| Political philosophy | Medium | Future enrichment recommended |
| Spirituality | Medium | Future enrichment recommended |
| Writing/public communication | Low | New route recommended |
| Experiment / lab | Low | New route recommended |
| Publication / review | Low | New route recommended |

### Overall result

The current navigation layer covers the major deep-theory spine, but does not yet fully cover:

- writing transformation routes;
- lab / falsification routes;
- publication / review routes;
- some graphify support pages;
- detailed L2 social dynamics;
- hard-problem epistemology support.

---

## 4. Recommended Patch Batch

### Batch 1 — Minimal path fixes

Files:

- `_SRT_CONTEXT_ROUTER.md`
- `_SRT_DEEP_THEORY_MAP.md`

Actions:

- Replace `Philosophy/SRT_Consciousness_Conditions.md` with `graphify-out/wiki/SRT_Consciousness_Conditions.md`.
- Replace `Ontology_Split_Index.md if available...` with `graphify-out/wiki/Ontology_Split_Index.md` and mark as support.

### Batch 2 — Missing deep-content additions

Files:

- `_SRT_CONTEXT_ROUTER.md`
- `_SRT_DEEP_THEORY_MAP.md`

Actions:

- Add `Philosophy/SRT_SocTheory_06_L2_Dynamics.md` to L2 / social routes.
- Add `graphify-out/wiki/SRT_Hard_Problem_Epistemology.md` to consciousness support.
- Add `graphify-out/wiki/SRT_Consciousness_Conditions.md` to d-value / consciousness support.

### Batch 3 — New operational routes

Files:

- `_SRT_CONTEXT_ROUTER.md`
- `_SRT_DEEP_THEORY_MAP.md`
- `Operations/_SRT_DEEP_NAV_TODO.md`

Actions:

- Add Writing / Article Framing route.
- Add Experiment / Lab / Falsification route.
- Add Publication / Paper Preparation route.

---

## 5. Audit Status

- [x] Checked primary route structure.
- [x] Identified path corrections.
- [x] Identified missing deep-content additions.
- [x] Identified missing operational routes.
- [ ] Apply minimal path fixes.
- [ ] Apply missing deep-content additions.
- [ ] Apply new operational routes.
- [ ] Re-run route verification after patch.

