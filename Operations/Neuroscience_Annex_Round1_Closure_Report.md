---
id: SRT-OPS-NEUROSCIENCE-ANNEX-ROUND1-CLOSURE-2026-04-29
type: closure_report
tags:
  - Operations
  - Neuroscience
  - Annex
  - Closure
status: active_report_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Neuroscience_Annex/README.md
  - Operations/PR_B_Neuro_06_10_Navigation_Record.md
  - Operations/PR_D_Batch2c2_Neuro_07_Geometric_Regularity_Extraction_Record.md
---

# Neuroscience Annex Round 1 Closure Report

## 0. Executive Summary

Neuroscience Annex Round 1 is complete.

Round 1 created and stabilized four Annex files:

- `Neuroscience_Annex/07_Field_Effects_Interface.md`
- `Neuroscience_Annex/08_Evo_Devo_Interface.md`
- `Neuroscience_Annex/09_Geometric_Regularity_Interface.md`
- `Neuroscience_Annex/10_Integration_Theory_Comparisons.md`

The migrated material is bridge/interface/comparison material. Canonical-facing formal anchors remain in the owner files. This round should not be extended by further blind extraction; future extraction should return to audit-first / adjudication-first mode.

## 1. PR Chain

| PR | Purpose | Result |
|---|---|---|
| #45 | Navigation audit | Added navigation blocks |
| #46 | NEURO-06-10 audit | Identified extraction candidates |
| #47 | Navigation blocks for 06-10 | Owner maps added |
| #48 | NEURO-09 pre-extraction audit | Boundary clarified |
| #49 | Absorption table adjudication | Bridge wording required |
| #50 | NEURO-09 extraction | Created Annex 10 |
| #51 | GRT dedup adjudication | Corrected false duplication assumption |
| #52 | NEURO-06 extraction | Created Annex 07 |
| #53 | NEURO-07 pre-extraction audit | Boundary clarified |
| #54 | NEURO-07 Evo-Devo extraction | Created Annex 08 |
| #55 | NEURO-07 §6 adjudication | Boundary clarified |
| #56 | Annotation conversion | Converted four SRT annotations |
| #57 | NEURO-07 §6.1-6.2 extraction | Created Annex 09 |

## 2. Annex Inventory

| Annex | Owner | Content | Canonical? | Guardrails |
|---|---|---|---|---|
| `07_Field_Effects_Interface.md` | `Neuroscience/SRT_Neuro_06_Field_Effects.md` | Synaptic synchrony, GWT, IIT, and GRT interface material. | `canonical: false`; `claim_mode: bridge` | Does not define Core primitives, `κ_sync`, `Ĝ_macro`, QUALIA-1/2, field-binding thresholds, or T-FIELD-2; points back to owner. |
| `08_Evo_Devo_Interface.md` | `Neuroscience/SRT_Neuro_07_Evo_Devo.md` | Levin bioelectric experiments, convergent evolution empirical basis, and Waddington interface material. | `canonical: false`; `claim_mode: bridge` | Does not define Core primitives, `θ_morpho`, `Ĝ_devo`, `L2^bioelectric`, `Generativity_devo`, `S_d`, `F_Bio`, or d-value universality; points back to owner. |
| `09_Geometric_Regularity_Interface.md` | `Neuroscience/SRT_Neuro_07_Evo_Devo.md` | Geometric regularity problem framing and Dehaene/Sable-Meyer empirical basis. | `canonical: false`; `claim_mode: bridge` | Does not define Core primitives, `η_compress`, `Ψ_f`, `d_symbolic`, or `Ĝ_θ^{ventral/dorsal}`; points back to owner. |
| `10_Integration_Theory_Comparisons.md` | `Neuroscience/SRT_Neuro_09_Integ_Eq.md` | External consciousness theory comparisons: IIT, GNWT, FEP, HOT, Orch-OR, neuromania, panpsychism. | `canonical: false`; `claim_mode: bridge` | Does not define Core primitives; IIT/Phi, FEP/Psi_f, GNWT, HOT, Orch-OR, and BioQuantum guardrails point back to owner anchors. |

## 3. Owner-Retained Formal Anchors

### 3.1 SRT-NEURO-06 owner retained

- QUALIA-1 / QUALIA-2
- Ax-FIELD-1
- Def-Ephaptic-Binding
- T-FIELD-1 / T-FIELD-2
- C-FIELD-1
- `κ_sync`
- `Ĝ_macro`
- H-Field predictions
- §6.3 SRT独特贡献

### 3.2 SRT-NEURO-07 owner retained

- BIO/EVO/PATH axioms
- Evo-Devo Bridge Note
- `Ĝ_devo`
- `L2^bioelectric`
- Genome-as-Generative-Model
- `Generativity_devo`
- §3.2.4 / §3.2.5 empirical patches
- §5.3-§5.5
- §6.3-§6.5
- `η_compress`
- `Ψ_f ∝ 1/η_compress`
- `d_symbolic`
- H-Evo predictions

### 3.3 SRT-NEURO-09 owner retained

- Def-Phi-Unity
- Ax-CLIN-1b
- Ax-CLIN-2/3/4/5/6
- T-INTEG-1
- C-INTEG-1
- BioQuantum section

## 4. Safety Confirmation

- No Core definitions moved.
- No formulas changed in this closure PR.
- All Annex files are `canonical: false`.
- All Annex files are bridge/interface material.
- Owner summaries and guardrails exist.
- No BioQuantum movement.
- No §6.3-§6.5 movement from NEURO-07.
- No §6.3 movement from NEURO-06.

## 5. Index / Navigation Updates Performed

- `Neuroscience_Annex/README.md`: updated with Round 1 closure status and closure report link.
- `Neuroscience/README.md`: updated with Neuroscience Annex entry and non-canonical boundary.
- `_SRT_INDEX.md`: updated with `Neuroscience_Annex/README.md` as a bridge/interface annex index.
- `STATUS.md`: no update needed; current status dashboard is not the right place for this detailed closure chain.
- `README.md`: no update needed; public entry already routes Neuroscience through `Neuroscience/README.md`.
- `Operations/Non_Philosophy_Refactor_Audit_Report.md`: no update needed; historical audit remains unchanged.

## 6. Remaining Candidates — Do Not Act Yet

- NEURO-08 Immune / distributed systems: low readiness; AD/Tanycyte equations need boundary decision.
- NEURO-10 Advanced Models: navigation-only sufficient for now.
- NEURO-07 remaining owner content: mostly SRT-internal.
- NEURO-06 remaining owner content: mostly SRT-internal.
- Any AI Annex work should start with a separate AI audit.

## 7. Recommended Next Phase

- Pause Neuroscience extraction.
- Run a Round-1 consistency audit only if needed.
- The next larger direction can be AI Consciousness / Agency audit, but should not start with extraction.
- Alternatively, run a read-only NEURO-08 adjudication before any NEURO-08 changes.

## 8. Final Recommendation

Neuroscience Annex Round 1 is complete. Further extraction should require new audit/adjudication PRs.
