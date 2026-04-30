---
id: SRT-OPS-PR-C4A-AI-ARCH-ENGINEERING-INTERFACE-EXTRACTION-2026-04-29
type: extraction_record
tags: [Operations, AI, Architecture, Annex, Extraction, Engineering-Interface]
status: active_record_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Operations/PR_C2_AI_Interface_Extraction_Adjudication.md
  - AI/SRT_AI_Architecture.md
  - AI/Architecture_Split/05_Interface_Additions.md
  - AI/Architecture_Annex/README.md
  - AI/Architecture_Annex/01_Engineering_Interfaces.md
machine_summary: >
  Extraction record for the first small-batch AI architecture interface extraction.
  Moves only selected engineering-interface material into AI/Architecture_Annex, leaving
  formalization, mechanism explanation, falsification conditions, ACT alignment formulas,
  attention-selection formulas, and d_k / SRT d-value disambiguation in the split/owner layer.
---

# PR-C4a AI Architecture Engineering Interface Extraction Record

## 0. Scope

This PR executes the first small-batch AI architecture interface extraction recommended by `Operations/PR_C2_AI_Interface_Extraction_Adjudication.md`.

Extracted from `AI/Architecture_Split/05_Interface_Additions.md`:

1. `Temporal-Development Continual-Learning Window`
2. `Taxonomy Mapping: LLM Internal Concept Control -> SRT`

Created:

- `AI/Architecture_Annex/README.md`
- `AI/Architecture_Annex/01_Engineering_Interfaces.md`

Updated:

- `AI/Architecture_Split/05_Interface_Additions.md` with owner summaries and annex pointers
- `AI/Architecture_Split/README.md` with annex links
- `ANNEX_REGISTRY.md` with the AI architecture annex entry

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

The extracted material is engineering-interface content:

- The continual-learning block discusses a developmental continual-learning engineering window.
- The internal concept-control block maps steering / hidden-state control / anti-refusal channels to SRT as a taxonomy proxy.

Neither block defines SRT architecture axioms, AI subjecthood, `d-value`, `Psi_f`, `G_hat_theta`, or consciousness thresholds.

## 3. Owner Replacement Pattern

The split source now keeps short owner summaries and links to the annex:

- `Temporal-Development Continual-Learning Window` -> `AI/Architecture_Annex/01_Engineering_Interfaces.md#1-temporal-development-continual-learning-window`
- `LLM Internal Concept Control` -> `AI/Architecture_Annex/01_Engineering_Interfaces.md#2-taxonomy-mapping-llm-internal-concept-control--srt`

## 4. Guardrails Added in Annex

The new annex explicitly states:

- Continual learning is not subjecthood.
- Internal concept steering is not personality or personhood.
- Anti-refusal activation is a risk-direction interface, not evidence of intrinsic agency.
- `d-value` entries in the table are proxies / translation aids and do not define canonical d.
- `Psi_f` entries are bridge usage only and must route back to canonical `Psi_f` source if used formally.

## 5. Next Recommendation

Do not continue with larger AI architecture extraction in the same PR.

Next safe candidate, if desired, should be a separate read-only adjudication or extraction PR for either:

1. Human-like AGI Program Themes taxonomy; or
2. ACT alignment interface, but only after formula-boundary adjudication.
