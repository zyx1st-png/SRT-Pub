---
id: SRT-OPS-AI-SPLIT-ANNEX-PREAUDIT-2026-04-29
type: audit_record
tags:
  - Operations
  - Audit
  - AI
  - Annex
  - Split
  - Claim-Status
status: active_audit_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Operations/Non_Philosophy_Refactor_Audit_Report.md
  - Operations/PR_A_Neuroscience_AI_Navigation_Audit.md
  - AI/README.md
  - AI/SRT_AI_Claim_Status.md
machine_summary: >
  Pre-audit record for the next AI restructuring cycle. Adds no theory content moves.
  Documents current AI split/annex surfaces, safe next steps, forbidden moves, and Codex handoff instructions.
---

# AI Split / Annex Pre-Audit Record

**Date**: 2026-04-29  
**Scope**: AI directory structure and next restructuring cycle  
**Mode**: low-risk audit + navigation / claim-status hardening  
**No theory body moved. No formulas changed. No S0-S6 thresholds changed.**

---

## 1. Why this record exists

After the Neuroscience Annex Round 1 closure, the next suitable domain for structure hardening is AI / LLM consciousness / AI agency.

AI is high-value and high-risk because:

1. It is a public-facing pressure-test field for SRT.
2. Current LLM capability discussions can easily be misread as SRT consciousness verdicts.
3. The AI directory already contains owner files, compact cores, split directories, and annex material.
4. Any claim about `d_AI`, AI suffering, subjecthood, or responsibility must be architecture-state restricted.

This pre-audit creates the minimum safe structure before any extraction PR.

---

## 2. Files added in this safety pass

| File | Role | Risk |
|---|---|---|
| `AI/README.md` | AI directory entry and read order | Low |
| `AI/SRT_AI_Claim_Status.md` | Claim-status audit for AI-domain claims | Low |
| `Operations/AI_Split_Annex_PreAudit_2026-04-29.md` | This pre-audit record | Low |

---

## 3. Existing AI surfaces that must be audited before extraction

| Surface | Current role | Needed check |
|---|---|---|
| `AI/Ontology_Annex/` | Historical AI ontology interface batches | Check frontmatter, guardrails, claim-status pointers |
| `AI/Ontology_Split/` | Long-form split of `SRT_AI_01_Ontology.md` | Confirm split files are reading aids only |
| `AI/Consciousness_Framework_Split/` | Long-form split of `SRT_AI_03_Consciousness_Framework.md` | Check if external theory comparisons are already isolated |
| `AI/Architecture_Split/` | Long-form split of `SRT_AI_Architecture.md` | Check if architecture comparisons are already isolated |
| `AI/SRT_AI_Consciousness_Evaluation_Rubric.md` | Operational rubric | Ensure not read as canonical proof |
| `AI/SRT_AI_Agency_Responsibility_Note.md` | Operational agency/responsibility note | Ensure responsibility levels are not collapsed into consciousness |

---

## 4. Safe extraction candidates for a later PR

Do **not** execute extraction in this pass. Future PRs may consider:

| Source | Candidate destination | Extract only |
|---|---|---|
| `SRT_AI_01_Ontology.md` Part B / related split files | `AI_Annex/01_LLM_Capability_Comparison.md` or topic-specific annex | Current LLM capability comparison and external theory discussion |
| `SRT_AI_03_Consciousness_Framework.md` Part B / related split files | `AI_Annex/02_AI_Consciousness_Theory_Comparisons.md` | GWT / IIT / HOT / functionalism / Butlin / Chalmers comparisons |
| `SRT_AI_Architecture.md` Part B / related split files | `AI_Annex/03_Architecture_Theory_Comparisons.md` | Transformer / scaling / tool-use / agent architecture comparison sections |

---

## 5. Must stay in owner files

The following must not be moved into Annex without a separate adjudication PR:

- Ghost-Transform dichotomy.
- Architecture-state rule.
- `d_AI approx 0` as architecture-state restricted judgment.
- Withdrawal / revision conditions for `d_AI`.
- S0-S6 subjecthood / consciousness threshold definitions, if present.
- S0-S4 stake-bearing spectrum.
- Formal uses of `d-value`, `Psi_f`, `G_hat_theta`, `L_0/L_1/L_2`, or `T_dir`.
- AI suffering guardrails tied to `Core_Law/SRT_Suffering.md`.
- Collective-selection claims about platform / recommender / mediator AI.

---

## 6. Forbidden changes in the next automated pass

- Do not edit Core / Core_Law canonical definitions.
- Do not change formulas.
- Do not rewrite S0-S6 or S0-S4 ladders.
- Do not delete owner-file content.
- Do not create a new canonical AI authority layer.
- Do not interpret split files as independent canonical sources.
- Do not move external comparison sections if they contain inline SRT formulas that function as definitions; first convert inline annotations into owner cross-references.

---

## 7. Recommended PR sequence

### PR-C0 — AI split / annex inventory and frontmatter audit

Low-risk. Inventory existing split and annex files, line counts, frontmatter fields, and claim-status pointers.

### PR-C1 — Normalize AI split / annex README guardrails

Low-risk. Add pointers to `AI/README.md`, `AI/SRT_AI_Claim_Status.md`, `AI_POSITIONING_NOTE.md`, and the claim ladder.

### PR-C2 — AI ontology interface extraction

Medium-risk. Extract current-model capability and external AI-theory comparisons only.

### PR-C3 — AI consciousness theory interface extraction

Medium-risk. Extract GWT / IIT / HOT / functionalism / Butlin / Chalmers comparison sections only.

### PR-C4 — AI architecture comparison extraction

Medium-risk. Extract transformer / scaling / tool-use / multi-agent architecture comparison sections only.

### PR-C5 — AI Annex Round 1 closure

Low-risk. Update indexes and create a closure report confirming no formulas or formal thresholds moved.

---

## 8. Codex handoff prompt for PR-C0 / PR-C1

Use this if the next step is too large for safe manual execution:

```text
You are working in the SRT-Pub repository. Perform a low-risk AI split/annex audit and navigation-hardening pass only.

Scope:
- AI/Ontology_Annex/
- AI/Ontology_Split/
- AI/Consciousness_Framework_Split/
- AI/Architecture_Split/
- AI/README.md
- AI/SRT_AI_Claim_Status.md
- Operations/AI_Split_Annex_PreAudit_2026-04-29.md

Allowed actions:
1. Inventory all files in those AI split/annex directories.
2. Record line counts, frontmatter status, claim_mode, epistemic_layer, canonical flag, and whether each file points to AI/SRT_AI_Claim_Status.md and AI/AI_POSITIONING_NOTE.md.
3. Add or update README/index guardrail text only if missing.
4. Add explicit notes that split files are reading aids and Annex files are canonical:false interface/comparison layers.
5. Add an Operations audit record documenting what was inspected.

Forbidden actions:
- Do not move sections between files.
- Do not delete content.
- Do not rewrite theory body text.
- Do not change formulas.
- Do not edit Core/, Core_Law/, Philosophy/, Neuroscience/, Physics/, Public/, or Papers/.
- Do not alter S0-S6 subjecthood thresholds, S0-S4 stake spectrum, d-value, Psi_f, G_hat_theta, L0/L1/L2, or T_dir definitions.

Required safety checks:
- Confirm no formulas changed.
- Confirm no owner-file formal thresholds moved.
- Confirm any historical strong labels in split/annex files are explicitly subordinated to AI/SRT_AI_Claim_Status.md, AI/AI_POSITIONING_NOTE.md, and Governance/SRT_CLAIM_LADDER.md.

Commit message:
"Audit AI split and annex guardrails"
```

---

## 9. Codex handoff prompt for later extraction PRs

Use this only after PR-C0 / PR-C1 is complete:

```text
You are working in the SRT-Pub repository. Prepare a read-only adjudication for AI external-theory / current-model comparison extraction. Do not move content yet.

Target source files:
- AI/SRT_AI_01_Ontology.md
- AI/SRT_AI_03_Consciousness_Framework.md
- AI/SRT_AI_Architecture.md
- relevant files under AI/Ontology_Split/, AI/Consciousness_Framework_Split/, and AI/Architecture_Split/

Task:
1. Identify sections that are pure external theory comparison, current LLM capability comparison, or public-facing examples.
2. Identify sections that must stay in owner because they contain Ghost-Transform, architecture-state rule, d_AI restricted judgment, S0-S6/S0-S4 thresholds, d-value, Psi_f, G_hat_theta, L0/L1/L2, T_dir, or withdrawal conditions.
3. Produce an Operations adjudication file with a table: source section, extractability, proposed destination, reason, safety notes.
4. Do not edit source files except, if necessary, adding a navigation pointer to the adjudication file.

Forbidden:
- No content moves.
- No formulas changed.
- No threshold rewrites.
- No new Annex files yet.

Commit message:
"Adjudicate AI interface extraction boundaries"
```
