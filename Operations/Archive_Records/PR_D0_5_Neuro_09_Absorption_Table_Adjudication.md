---
id: SRT-OPS-PR-D0-5-NEURO-09-ABSORPTION-ADJUDICATION-2026-04-28
type: adjudication_record
tags:
  - Operations
  - Adjudication
  - Neuroscience
  - PreExtraction
  - PR-D0.5
status: active_adjudication_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-28
target_file: Neuroscience/SRT_Neuro_09_Integ_Eq.md
target_section: "§2.2 SRT absorption table"
reference_audit: Operations/Archive_Records/PR_D0_Neuro_09_PreExtraction_Audit.md
machine_summary: >
  Read-only adjudication of the SRT-NEURO-09 §2.2 absorption table.
  Permits PR-D Batch 1 movement only as bridge/interface material with owner
  summary retention and explicit guardrails for IIT/Phi, FEP/Psi_f, GNWT,
  HOT, Orch-OR, and BioQuantum boundaries.
---

# PR-D0.5 Neuro 09 Absorption Table Adjudication

## 0. Executive Summary

This record adjudicates the §2.2 SRT absorption table in `Neuroscience/SRT_Neuro_09_Integ_Eq.md` after the PR-D0 pre-extraction audit.

Decision summary:

- All five rows can move to a future Annex **only as bridge/interface translation rows**, not as definitions.
- The owner file must retain a short summary explaining that the table is an external-theory-to-SRT bridge translation.
- IIT / `Phi` and FEP / free-energy rows have the highest canonical-like risk and require the strongest guardrails.
- GNWT ignition, HOT self-reference, and Orch-OR rows are eligible for Annex movement with explicit non-definition wording.
- PR-D Batch 1 is permitted under decision **B: move the table, but retain owner summary + guardrails**.

Key anti-misreading decisions:

- IIT / `Phi` mappings do not redefine Def-Phi-Unity or C-INTEG-1.
- FEP / free-energy mappings do not redefine `Psi_f`.
- GNWT ignition is a comparison to `L_0 -> L_1` transition, not its definition.
- HOT self-reference does not define `\hat{G}_\theta`.
- Orch-OR remains a hypothesis-level physical-mechanism comparison only and must not be merged with BioQuantum material in Batch 1.

## 1. Scope and Safety Record

Scope:

- Read-only analysis of `Neuroscience/SRT_Neuro_09_Integ_Eq.md` §2.2.
- Row-level adjudication of IIT / `Phi`, GNWT ignition, FEP / free energy, HOT, and Orch-OR mappings.
- Added this Operations adjudication record only.

Safety record:

- No Neuroscience files modified.
- No Annex directory created.
- No `Neuroscience_Annex/` directory created.
- No content moved.
- No formulas changed.
- No frontmatter changed.
- No `claim_mode`, `canonical`, `status`, `layer`, or `epistemic_layer` changed.
- No canonical definitions changed.
- Def-Phi-Unity unchanged.
- `Psi_f` unchanged.
- Ax-CLIN-1b unchanged.
- BioQuantum section unchanged.
- No `Core/`, `Core_Law/`, `AI/`, `Philosophy/`, `Public/`, `Papers/`, or `graphify-out/` file touched.

## 2. Row-Level Adjudication Table

| Row | Boundary Decision | Owner Retention | Annex Eligibility | Required Guardrail | Remaining Risk |
|---|---|---|---|---|---|
| IIT / `Phi` | Bridge translation subordinated to owner-file Def-Phi-Unity and C-INTEG-1. The row is not a new `Phi` definition. | Keep owner summary noting that Def-Phi-Unity and C-INTEG-1 remain formal anchors. | Eligible for Annex movement with explicit bridge label. | "IIT `Phi` mappings do not redefine Def-Phi-Unity or C-INTEG-1; they are comparative translations only." | Medium-high because the current row uses equation-like wording. |
| GNWT ignition | Bridge comparison between ignition/broadcast models and SRT transition language. It is not the definition of `L_0 -> L_1`. | Keep owner summary pointing to Ax-CLIN-1b / clinical gate material if needed. | Eligible for Annex movement. | "GNWT ignition is compared to `L_0 -> L_1` transition language; it does not define that transition." | Medium-low. |
| FEP / free energy | Bridge translation with high canonical-like risk. It must not redefine `Psi_f` or collapse free energy into ontological friction. | Keep owner summary with `Psi_f` guardrail. Do not leave the row unqualified in owner or Annex. | Eligible only with strong guardrail; otherwise defer. | "FEP/free-energy mappings do not redefine `Psi_f`; free-energy language is an interpretive bridge translation only." | High because the current row can be read as `free energy = ontological friction`. |
| HOT | Bridge comparison between higher-order representation and operator self-reference. It is not a definition of `\hat{G}` or `\hat{G}_\theta`. | Keep only summary-level pointer if needed. | Eligible for Annex movement. | "HOT self-reference does not define `\hat{G}_\theta`; it is a comparison to self-reference motifs." | Medium-low. |
| Orch-OR | Hypothesis-level physical-mechanism comparison. It does not establish a quantum mechanism for SRT selection. | Keep no row in owner unless a one-line pointer is useful; BioQuantum remains separate. | Eligible for Annex movement as hypothesis-level comparison. | "Orch-OR is hypothesis-level physical-mechanism comparison only; BioQuantum material remains outside Batch 1 unless separately reviewed." | Medium. |

## 3. Guardrail Text for Future Annex

Future `Neuroscience_Annex/10_Integration_Theory_Comparisons.md` must include this guardrail block near the top:

> **Boundary Guardrail**
>
> This Annex is bridge/interface material. It does not define SRT Core primitives.
>
> IIT `Phi` mappings do not redefine Def-Phi-Unity or C-INTEG-1 in `Neuroscience/SRT_Neuro_09_Integ_Eq.md`.
>
> FEP/free-energy mappings do not redefine `Psi_f`; free-energy language is used only as an interpretive bridge translation.
>
> GNWT ignition is a comparison to `L_0 -> L_1` transition language, not the definition of that transition.
>
> HOT self-reference does not define `\hat{G}_\theta`.
>
> Orch-OR is a hypothesis-level physical-mechanism comparison only.
>
> BioQuantum material remains outside PR-D Batch 1 unless separately reviewed.

Additional Annex table caption recommendation:

> The absorption table below is a translation aid between external consciousness theories and SRT vocabulary. It is not a definition table, not a canonical registry, and not a replacement for the owner-file formal anchors.

## 4. Owner Summary Required After Extraction

If §2.2 is extracted in PR-D Batch 1, `Neuroscience/SRT_Neuro_09_Integ_Eq.md` should retain this owner summary near the extraction point:

> The former §2.2 absorption table is an external-theory-to-SRT bridge translation. The full table has been moved to the Annex for comparison use. It does not define SRT Core primitives.
>
> Def-Phi-Unity, Ax-CLIN-1b, T-INTEG-1, and C-INTEG-1 remain the owner-file formal anchors for integration, clinical gating, and `Phi`/`d` orthogonality. The Annex only compares IIT, GNWT, FEP, HOT, and Orch-OR to those anchors; it does not redefine `Phi`, `Psi_f`, `d-value`, `L_0/L_1/L_2`, or `\hat{G}_\theta`.

Minimum owner retention requirements:

- State that the absorption table is bridge translation.
- Point to the Annex for the complete table.
- Name Def-Phi-Unity, Ax-CLIN-1b, T-INTEG-1, and C-INTEG-1 as owner formal anchors.
- State that the Annex does not define Core primitives.

## 5. PR-D Batch 1 Permission Decision

Decision: **B. The §2.2 table can be moved, but the owner file must retain summary + guardrails.**

Reasoning:

- Moving all rows is acceptable if the future Annex marks the table as bridge/interface material.
- Keeping only low-risk rows in Annex while leaving IIT/FEP in the owner would preserve the most ambiguous rows in the highest-risk location; that would not solve the boundary problem.
- A full move with guardrails is clearer than partial extraction because all rows share the same function: external-theory translation.
- The owner file should keep formal anchors, not the full translation table.

Conditions for PR-D Batch 1:

1. Add owner summary before or at the extraction point.
2. Add an Annex pointer.
3. Add the Annex guardrail block from §3.
4. Preserve Def-Phi-Unity, Ax-CLIN-1b, T-INTEG-1, C-INTEG-1, and all Part A anchors in the owner file.
5. Keep BioQuantum outside Batch 1 unless separately reviewed.

## 6. Final Recommendation

PR-D Batch 1 may begin after this adjudication.

Recommended next step:

- Extract §1, §2.2, §3, and §4 into `Neuroscience_Annex/10_Integration_Theory_Comparisons.md` only if the owner file retains the summary and guardrails specified above.
- Do not postpone §2.2 while extracting §1/§3/§4 unless the team wants a narrower first extraction PR. The adjudication here resolves §2.2 enough for guarded Annex movement.
- No additional human review is required before PR-D Batch 1 if the future PR follows this record's owner-retention and Annex-guardrail requirements.

Final recommendation: **Proceed to PR-D Batch 1 with full §2.2 Annex movement under strict bridge guardrails.**
