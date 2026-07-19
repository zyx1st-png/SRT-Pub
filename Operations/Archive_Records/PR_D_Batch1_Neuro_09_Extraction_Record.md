---
id: SRT-OPS-PR-D-BATCH1-NEURO-09-EXTRACTION-2026-04-28
type: migration_record
tags:
  - Operations
  - Migration
  - Neuroscience
  - Annex
  - PR-D
status: active_record_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-28
target_file: Neuroscience/SRT_Neuro_09_Integ_Eq.md
annex_file: Neuroscience_Annex/10_Integration_Theory_Comparisons.md
dependency:
  - Operations/Archive_Records/PR_B_Neuro_06_10_Navigation_Record.md
  - Operations/Archive_Records/PR_D0_Neuro_09_PreExtraction_Audit.md
  - Operations/Archive_Records/PR_D0_5_Neuro_09_Absorption_Table_Adjudication.md
---

# PR-D Batch 1 Neuro 09 Extraction Record

## Scope

This PR extracted selected external theory comparison/interface material from `Neuroscience/SRT_Neuro_09_Integ_Eq.md` into `Neuroscience_Annex/10_Integration_Theory_Comparisons.md`.

## Sections Moved

- §1 Babel Tower comparison.
- §2.2 SRT absorption table.
- §3 anti-neuromania defense.
- §4 panpsychism comparison.

## Owner File Retention

`Neuroscience/SRT_Neuro_09_Integ_Eq.md` now retains:

- `## Part B Interface Summary`.
- Pointer to `../Neuroscience_Annex/10_Integration_Theory_Comparisons.md`.
- Guardrail that Annex material is bridge/interface comparison and does not define SRT Core primitives.
- Explicit owner-anchor statement for Def-Phi-Unity, Ax-CLIN-1b, Ax-CLIN-2/3/4/5/6, T-INTEG-1, and C-INTEG-1.
- Explicit guardrails for IIT `Phi`, FEP/free-energy, GNWT ignition, HOT self-reference, and Orch-OR.

## Annex Contents

`Neuroscience_Annex/10_Integration_Theory_Comparisons.md` contains:

- `canonical: false` frontmatter.
- Boundary Guardrail block.
- §1 Babel Tower comparison.
- §2.2 SRT absorption table with translation-aid caption.
- §3 anti-neuromania defense.
- §4 panpsychism comparison.

`Neuroscience_Annex/README.md` identifies the directory as a Neuroscience bridge/interface Annex, states that Annex files do not define Core primitives, lists the new Annex, and links back to owner and Operations records.

## Content Not Moved

- Part A formal axioms were not moved.
- Def-Phi-Unity was not moved or modified.
- Ax-CLIN-1b was not moved or modified.
- Ax-CLIN-2/3/4/5/6 were not moved or modified.
- T-INTEG-1 / C-INTEG-1 were not moved or modified.
- H-Integ predictions were not moved.
- §2.1, §2.3, §2.4, §2.5, §5, §6, §7, §8 remained in the owner file.
- BioQuantum / Quantum hypothesis material remained in the owner file.

## Safety Record

- No formulas changed.
- No Part A formal axioms changed.
- BioQuantum section not moved.
- Def-Phi-Unity unchanged.
- Ax-CLIN-1b unchanged.
- `Psi_f` unchanged.
- C-INTEG-1 unchanged.
- No `Core/`, `Core_Law/`, `AI/`, `Philosophy/`, `Public/`, `Papers/`, or `graphify-out/` files touched.
- Annex is `canonical: false`.
- Annex guardrails added for IIT/Phi, FEP/Psi_f, GNWT, HOT, Orch-OR, and BioQuantum boundaries.

## Follow-Up Recommendation

Review the owner-file section numbering after future extraction batches. If additional Neuro 09 interface sections are moved later, consolidate Part B headings in a separate navigation-only cleanup PR rather than mixing cleanup with extraction.
