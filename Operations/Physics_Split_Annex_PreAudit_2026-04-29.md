---
id: SRT-OPS-PHYSICS-SPLIT-ANNEX-PREAUDIT-2026-04-29
type: audit_record
tags: [Operations, Physics, Audit, Claim-Status, Annex, Split, Guardrail]
status: active_audit_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Operations/AI_Annex_Round1_Closure_Report.md
  - Physics/README.md
  - Physics/SRT_Physics_Claim_Status.md
  - Physics/PHYSICS_COMPACT_REGISTRY.md
  - Physics/_SRT_Phys_Bridge.md
machine_summary: >
  Read-only pre-audit for Physics split/annex and claim-status work. Adds navigation and claim-status guardrails,
  but does not create Physics_Annex, move source text, change formulas, or promote physics hypotheses.
---

# Physics Split / Annex Pre-Audit Record

**Date**: 2026-04-29  
**Scope**: Physics directory entry, claim-status inventory, and future annex readiness  
**Mode**: read-only / navigation hardening  
**No Physics source text moved. No formulas changed. No Physics annex created.**

---

## 1. Why this record exists

After AI Annex Round 1 closure, the next structural-hardening candidate is Physics.

Physics is high-value but higher-risk than AI because it contains claims that may be read as:

1. solving the quantum measurement problem;
2. refuting or absorbing MWI / Everett;
3. deriving discrete time;
4. deriving gravity or Einstein equations from `Psi_f`;
5. explaining physical constants;
6. treating QBox / hyperdecoherence / post-quantum materials as evidence for SRT.

This pre-audit creates a guardrail layer before any extraction or annex creation.

---

## 2. Files added in this safety pass

| File | Role | Risk |
|---|---|---|
| `Physics/README.md` | Physics directory entry and read order | Low |
| `Physics/SRT_Physics_Claim_Status.md` | Claim-status audit for Physics-domain claims | Low |
| `Operations/Physics_Split_Annex_PreAudit_2026-04-29.md` | This pre-audit record | Low |

---

## 3. Existing Physics surfaces identified

| Surface | Current role | Needed check |
|---|---|---|
| `Physics/_SRT_Phys_Bridge.md` | Main physics bridge / foundational axioms | Claim-level and interpretation-label audit |
| `Physics/PHYSICS_COMPACT_REGISTRY.md` | Compact registry and reading path | Add guardrail pointer later if needed |
| `Physics/SRT_Quant_00_Intro_CompactCore.md` | Quantum compact entry | Check claim level and collapse/MWI wording |
| `Physics/SRT_Quant_01_Selection_CompactCore.md` | Quantum selection compact entry | Check measurement-as-selection status |
| `Physics/SRT_Quant_02_Cosmology_CompactCore.md` | Quantum cosmology compact entry | Check cosmology / multiverse claims |
| `Physics/SRT_Physics_Cosmology_CompactCore.md` | Physics cosmology compact entry | Check cosmology and physical-constant wording |
| `Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md` | Formalism compact entry | Check formula status and derivation language |
| `Physics/SRT_Phys_10_Integration_CompactCore.md` | Integration compact entry | Check synthesis overclaims |
| `Physics/SRT_Phys_07_Complex_Systems_CompactCore.md` | Complexity compact entry | Check complexity / ontology bridge status |
| `Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md` | Ontology extension compact entry | Check ontology vs physics proof boundary |
| Longform counterparts | Complete argument / interface accumulation | Do not move until section-level adjudication |

---

## 4. Safe next steps

### PR-P0 — Physics inventory and frontmatter audit

Allowed:

1. Inventory all files in `Physics/`.
2. Record line counts and frontmatter fields.
3. Record whether each file points to `Physics/SRT_Physics_Claim_Status.md` and `Physics/README.md`.
4. Identify candidate high-risk sections by label only.
5. Update readme / registry pointers if missing.

Forbidden:

- Do not move sections.
- Do not delete content.
- Do not create `Physics_Annex/` yet.
- Do not change formulas.
- Do not modify Core / Core_Law / AI / Neuroscience / Philosophy / Public / Papers.
- Do not promote any physics hypothesis.

### PR-P1 — Physics interface extraction adjudication

Only after PR-P0. Read-only adjudication for specific extraction candidates.

Potential candidates for adjudication:

- external theory comparison tables;
- MWI / collapse compatibility notes;
- empirical pressure-point tables;
- QBox / hyperdecoherence interface material;
- public-facing analogies.

Blocked without separate adjudication:

- tensor / gravity derivations;
- discrete-time formulas;
- physical constants tables;
- candidate empirical predictions;
- any claim sounding like established physics.

---

## 5. Current stop rule

This pass stops after adding Physics navigation and claim-status guardrails.

Do not extract Physics content until a future PR-P0 inventory and PR-P1 adjudication are complete.

---

## 6. Codex handoff prompt for PR-P0

```text
You are working in the SRT-Pub repository. Perform a low-risk Physics inventory and frontmatter audit only.

Scope:
- Physics/
- Physics/README.md
- Physics/SRT_Physics_Claim_Status.md
- Physics/PHYSICS_COMPACT_REGISTRY.md
- Physics/_SRT_Phys_Bridge.md
- Operations/Physics_Split_Annex_PreAudit_2026-04-29.md

Allowed actions:
1. Inventory all files in Physics/.
2. Record line counts, frontmatter status, claim_mode, epistemic_layer, canonical flag, and whether each file points to Physics/SRT_Physics_Claim_Status.md and Physics/README.md.
3. Add or update README / registry guardrail pointers only if missing.
4. Identify high-risk candidate sections by label only.
5. Add an Operations audit record documenting what was inspected.

Forbidden actions:
- Do not move sections between files.
- Do not delete content.
- Do not create Physics_Annex/.
- Do not rewrite theory body text.
- Do not change formulas.
- Do not edit Core/, Core_Law/, AI/, Neuroscience/, Philosophy/, Public/, Papers/, or graphify-out/.
- Do not alter collapse, MWI, gravity, discrete-time, constants, QBox, or cosmology claims except by adding navigation/guardrail pointers.

Required safety checks:
- Confirm no formulas changed.
- Confirm no source body sections moved.
- Confirm no Physics_Annex/ directory created.
- Confirm high-risk labels are only inventoried, not extracted.

Commit message:
"Audit Physics inventory and claim-status guardrails"
Create a PR for review. Do not merge automatically.
```
