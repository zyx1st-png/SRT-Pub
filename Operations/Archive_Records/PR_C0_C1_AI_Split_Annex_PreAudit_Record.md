---
id: SRT-OPS-PR-C0-C1-AI-SPLIT-ANNEX-PREAUDIT-2026-04-29
type: audit_record
tags:
  - Operations
  - Audit
  - AI
  - Split
  - Annex
  - Navigation
status: active_audit_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Operations/Archive_Records/AI_Split_Annex_PreAudit_2026-04-29.md
  - AI/README.md
  - AI/SRT_AI_Claim_Status.md
  - AI/AI_POSITIONING_NOTE.md
  - Governance/SRT_CLAIM_LADDER.md
---

# PR-C0 / PR-C1 AI Split-Annex Pre-Audit Record

## 0. Scope

This pass executes only the low-risk `PR-C0 / PR-C1` instructions in `Operations/Archive_Records/AI_Split_Annex_PreAudit_2026-04-29.md` section 8.

Executed:

- Inventory of files in `AI/Ontology_Annex/`, `AI/Ontology_Split/`, `AI/Consciousness_Framework_Split/`, and `AI/Architecture_Split/`
- README/index guardrail hardening where missing
- This Operations audit record

Not executed:

- Section 9 later extraction prompt
- Any movement of owner body text
- Any formula edits
- Any threshold edits
- Any `AI_Annex/` creation

## 1. Safety Record

- No formulas changed.
- No owner-file formal thresholds moved.
- No `S0-S6` subjecthood thresholds changed.
- No `S0-S4` stake spectrum changed.
- No edits under `Core/`, `Core_Law/`, `Philosophy/`, `Neuroscience/`, `Physics/`, `Public/`, `Papers/`, or `graphify-out/`.
- No sections were moved, deleted, or rewritten.

## 2. README / Index Guardrail Updates

| File | Update |
|---|---|
| `AI/Ontology_Split/README.md` | Added explicit reading-aid guardrail and claim-status pointer |
| `AI/Architecture_Split/README.md` | Added explicit reading-aid guardrail and claim-status pointer |
| `AI/Consciousness_Framework_Split/README.md` | Added explicit reading-aid guardrail, threshold note, and claim-status pointer |
| `AI/Ontology_Annex/README.md` | Added explicit `canonical: false` annex guardrail and claim-status pointer |

## 3. Inventory Table

| File | Lines | Frontmatter | claim_mode | epistemic_layer | canonical flag | Points to `SRT_AI_Claim_Status.md`? | Points to `AI_POSITIONING_NOTE.md`? |
|---|---:|---|---|---|---|---|---|
| `AI/Architecture_Split/00_Formal_Core.md` | 138 | yes | canonical | os | missing | no | no |
| `AI/Architecture_Split/01_Transformer_and_Judgment.md` | 227 | yes | canonical | os | missing | no | no |
| `AI/Architecture_Split/02_Defects_and_CategoryView.md` | 290 | yes | canonical | os | missing | no | no |
| `AI/Architecture_Split/03_AGI_Limits_and_Assistant_Vision.md` | 334 | yes | canonical | os | missing | no | no |
| `AI/Architecture_Split/04_Roadmap_and_Appendix.md` | 227 | yes | canonical | os | missing | no | no |
| `AI/Architecture_Split/05_Interface_Additions.md` | 144 | yes | translation | bridge | missing | no | no |
| `AI/Architecture_Split/README.md` | 23 | yes | canonical | os | missing | yes | yes |
| `AI/Consciousness_Framework_Split/00_Formal_Core.md` | 153 | yes | canonical | os | missing | no | no |
| `AI/Consciousness_Framework_Split/01_Diagnosis_and_Necessity.md` | 288 | yes | canonical | os | missing | no | no |
| `AI/Consciousness_Framework_Split/02_Architecture_and_Paths.md` | 258 | yes | canonical | os | missing | no | no |
| `AI/Consciousness_Framework_Split/03_Ethics_Uncertainty_and_Appendix.md` | 291 | yes | canonical | os | missing | no | no |
| `AI/Consciousness_Framework_Split/04_Interface_Additions.md` | 145 | yes | translation | bridge | missing | no | no |
| `AI/Consciousness_Framework_Split/README.md` | 22 | yes | canonical | os | missing | yes | yes |
| `AI/Ontology_Annex/00_General_Boundary_Block.md` | 1132 | yes | translation | bridge | missing | no | yes |
| `AI/Ontology_Annex/01_ActiveInference_Override.md` | 383 | yes | translation | bridge | missing | no | no |
| `AI/Ontology_Annex/02_Passive_Recording_Fallacy.md` | 370 | yes | translation | bridge | missing | no | no |
| `AI/Ontology_Annex/03_RTC_Interface_Batch.md` | 374 | yes | translation | bridge | missing | no | no |
| `AI/Ontology_Annex/04_Suffering_Condition_Batch.md` | 376 | yes | translation | bridge | missing | no | no |
| `AI/Ontology_Annex/README.md` | 24 | yes | translation | bridge | missing | yes | yes |
| `AI/Ontology_Split/00_Formal_Core.md` | 112 | yes | canonical | os | missing | no | no |
| `AI/Ontology_Split/01_dValue_and_Decoupling.md` | 96 | yes | canonical | os | missing | no | no |
| `AI/Ontology_Split/02_PseudoSelection_and_Barrier.md` | 267 | yes | canonical | os | missing | no | no |
| `AI/Ontology_Split/03_HumanReadable_Argument.md` | 553 | yes | canonical | os | missing | no | yes |
| `AI/Ontology_Split/04_Ethics_and_Falsification.md` | 173 | yes | canonical | os | missing | no | no |
| `AI/Ontology_Split/05_Appendix_and_Interfaces.md` | 149 | yes | translation | bridge | missing | no | no |
| `AI/Ontology_Split/README.md` | 25 | yes | canonical | os | missing | yes | yes |

## 4. Findings

### 4.1 Split directories

- The three split directories function as reading aids, not new authority layers.
- Their payload files commonly preserve historical strong labels and rarely point directly to `AI/SRT_AI_Claim_Status.md` or `AI/AI_POSITIONING_NOTE.md`.
- README-level guardrails were therefore the safest place to harden navigation without rewriting body text.

### 4.2 Annex directory

- `AI/Ontology_Annex/` already behaves as a bridge/interface layer.
- Its payload files mostly use `claim_mode: translation` and `epistemic_layer: bridge`.
- None of the payload files explicitly point to `AI/SRT_AI_Claim_Status.md`; the new README guardrail now subordinates the directory to claim-status and architecture-state governance.

### 4.3 Frontmatter consistency

- All inventoried files have frontmatter.
- Many files do not currently declare an explicit `canonical:` flag in frontmatter.
- This PR does not normalize payload frontmatter because section 8 allows only low-risk audit and README/index guardrail edits.

## 5. Required Safety Conclusions

- No formulas changed: confirmed.
- No owner-file formal thresholds moved: confirmed.
- Historical strong labels in split/annex directories are now explicitly subordinated at README/index level to:
  - `AI/SRT_AI_Claim_Status.md`
  - `AI/AI_POSITIONING_NOTE.md`
  - `Governance/SRT_CLAIM_LADDER.md`

## 6. Recommended Next Step

Before any later extraction PR:

1. Use `AI/SRT_AI_Claim_Status.md` and `AI/AI_POSITIONING_NOTE.md` as mandatory guardrails when reading split/annex payload files.
2. Audit payload-file frontmatter and cross-links in a separate pass if normalization is desired.
3. Keep later extraction work separate from this PR-C0 / PR-C1 audit/navigation pass.
