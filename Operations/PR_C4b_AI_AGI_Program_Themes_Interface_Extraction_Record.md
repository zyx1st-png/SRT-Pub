---
id: SRT-OPS-PR-C4B-AI-AGI-PROGRAM-THEMES-INTERFACE-EXTRACTION-2026-04-29
type: extraction_record
tags: [Operations, AI, Architecture, Annex, Extraction, AGI, Taxonomy]
status: active_record_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Operations/PR_C2_AI_Interface_Extraction_Adjudication.md
  - Operations/PR_C4a_AI_Architecture_Engineering_Interface_Extraction_Record.md
  - AI/SRT_AI_Architecture.md
  - AI/Architecture_Split/05_Interface_Additions.md
  - AI/Architecture_Annex/README.md
  - AI/Architecture_Annex/02_AGI_Program_Themes_Interface.md
machine_summary: >
  Extraction record for the AGI program-themes architecture taxonomy. Moves one taxonomy
  block into AI/Architecture_Annex while leaving formalization, mechanism explanation,
  falsification conditions, ACT alignment formulas, attention-selection formulas, and d_k / SRT
  d-value disambiguation in the split/owner layer.
---

# PR-C4b AI AGI Program Themes Interface Extraction Record

## 0. Scope

This PR extracts one low-risk taxonomy/interface block from `AI/Architecture_Split/05_Interface_Additions.md`:

- `Taxonomy Mapping: Human-like AGI Program Themes -> SRT`

Created:

- `AI/Architecture_Annex/02_AGI_Program_Themes_Interface.md`

Updated:

- `AI/Architecture_Split/05_Interface_Additions.md` with an owner summary and annex pointer
- `AI/Architecture_Annex/README.md` with the new annex entry

## 1. Safety Record

- No formulas changed.
- No S0-S6 thresholds changed.
- No S0-S4 stake spectrum changed.
- No attention-selection formalization moved.
- No `d_k` / SRT `d-value` disambiguation moved.
- `Formalization Summary` remains in `AI/Architecture_Split/05_Interface_Additions.md`.
- `Mechanism Explanation` remains in `AI/Architecture_Split/05_Interface_Additions.md`.
- `Falsification Conditions` remain in `AI/Architecture_Split/05_Interface_Additions.md`.
- `ACT 对齐判据与熔断` formulas remain in `AI/Architecture_Split/05_Interface_Additions.md`.
- No Core / Core_Law / Philosophy / Neuroscience / Physics / Public / Papers / graphify-out files touched.

## 2. Boundary Rationale

The extracted AGI program-themes block is a taxonomy / interface mapping. It is not a formal SRT architecture axiom and does not define subjecthood, consciousness, `d-value`, `Psi_f`, or `G_hat_theta`.

## 3. Owner Replacement Pattern

The split source now keeps a summary and link:

- `Taxonomy Mapping: Human-like AGI Program Themes -> SRT` -> `AI/Architecture_Annex/02_AGI_Program_Themes_Interface.md#taxonomy-mapping-human-like-agi-program-themes--srt`

## 4. Guardrails Added in Annex

The new annex states:

- The taxonomy is a translation aid, not an AGI architecture proof.
- Higher engineering sophistication does not imply SRT subjecthood.
- `d-value` intervals are proxy labels only.
- `Psi_f` states are bridge usage only.
- A system may satisfy external AGI program themes while remaining below SRT subjecthood / consciousness thresholds.

## 5. Next Recommendation

Pause architecture extraction after this PR unless a separate adjudication is prepared for ACT alignment formulas. The remaining architecture interface material is more formula-bound and should not be moved opportunistically.
