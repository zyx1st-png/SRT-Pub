---
id: SRT-OPS-PR-D-BATCH2C2-NEURO07-GEOM-EXTRACTION-2026-04-29
type: extraction_record
tags:
  - Operations
  - Extraction
  - Neuroscience
  - PR-D
  - GeometricRegularity
  - Dehaene
  - SymbolicCompression
status: complete
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
reference_adjudication: Operations/PR_D0_6_Neuro_07_Geometric_Regularity_Adjudication.md
reference_annotation_conversion: Operations/PR_D_Batch2c1_Neuro_07_Geometric_Annotation_Conversion_Record.md
pr: PR-D Batch 2c-2 — Extract Neuro 07 geometric regularity interface
machine_summary: >
  Extraction record for PR-D Batch 2c-2. Moved SRT-NEURO-07 §6.1
  (geometric regularity problem framing) and §6.2 (Dehaene/Sablé-Meyer
  fMRI/MEG empirical basis, with PR #56 converted annotations) to
  Neuroscience_Annex/09_Geometric_Regularity_Interface.md.
  Owner file retains §6.3–§6.5 (Ĝ_θ^{ventral/dorsal}, η_compress/Ψ_f,
  d_symbolic threshold) unchanged. No formulas changed.
---

# PR-D Batch 2c-2: Neuro 07 Geometric Regularity Extraction Record

**Date**: 2026-04-29
**PR scope**: Extract NEURO-07 §6.1–§6.2 to Annex; keep §6.3–§6.5 in owner
**Adjudication reference**: [`Operations/PR_D0_6_Neuro_07_Geometric_Regularity_Adjudication.md`](PR_D0_6_Neuro_07_Geometric_Regularity_Adjudication.md)
**Annotation conversion prerequisite**: [`Operations/PR_D_Batch2c1_Neuro_07_Geometric_Annotation_Conversion_Record.md`](PR_D_Batch2c1_Neuro_07_Geometric_Annotation_Conversion_Record.md)

---

## 1. Sections Moved

| Source section | Destination | Content |
|---|---|---|
| NEURO-07 §6 source citation (Sablé-Meyer, Dehaene) | `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` §6 header | Source citation for Dehaene/Sablé-Meyer empirical work |
| NEURO-07 §6.1 标准难题：几何规则性之谜 | `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` §6.1 | Geometric regularity problem framing — Himba, cross-cultural data, baboon/chimp contrast |
| NEURO-07 §6.2.1 双重编码系统 | `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` §6.2.1 | Dual-pathway table: ventral (CNN-explainable, shared with primates) vs. dorsal-prefrontal (human-unique) |
| NEURO-07 §6.2.2 关键发现 (5 findings) | `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` §6.2.2 | Five Dehaene fMRI/MEG findings with PR #56 converted `→ SRT interpretation: see owner §6.x` cross-references |
| NEURO-07 §6.2 证伪方向 | `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` §6.2 | Falsification directions with owner §6.3 cross-reference note added |

**Total content moved**: §6.1 + §6.2 (all subsections), approximately 35 lines of external empirical content.

**Prerequisite**: PR-D Batch 2c-1 (PR #56) converted 4 inline `→ SRT意义` / `→ Cross-ref` annotations in §6.2.2 to explicit `→ SRT interpretation: see owner §6.x` cross-references before this extraction.

---

## 2. Owner File Summary — What Replaced the Extracted Sections

§6.1–§6.2 body replaced with **Geometric Regularity Interface Annex Pointer** that:
- Points to `Neuroscience_Annex/09_Geometric_Regularity_Interface.md`
- States the Annex is bridge/interface material; does not define SRT Core primitives
- Explicitly retains `Ĝ_θ^{ventral}` / `Ĝ_θ^{dorsal}` in owner §6.3
- Explicitly retains `η_compress` and `Ψ_f(σ) ∝ 1/η_compress(σ)` in owner §6.4
- Explicitly retains `d_symbolic` and `d > d_symbolic` in owner §6.5
- States that `→ SRT interpretation` notes in Annex point back to owner §6.3–§6.5 and do not define those concepts
- Retains brief source citation (Sablé-Meyer, Dehaene) as pointer

---

## 3. Sections NOT Moved — Owner File Retention

| Section | Reason retained |
|---|---|
| All Part A axioms (Ax-BIO-1/2/2b/3, Ax-EVO-1/2/3, Ax-PATH-1/2) | Canonical SRT formal content |
| **§6.3 SRT解释：L_0 → L_1 选择的分层架构** | Contains `Ĝ_θ^{ventral}: L_0^{visual} → L_1^{object}` and `Ĝ_θ^{dorsal}: L_1^{object} → L_1^{symbolic}` — SRT formal operator specializations; FC-Ventral-1/2 falsification conditions |
| **§6.4 η_compress 的神经实现** | `η_compress = I(L_1;L_0)/H(L_1)` formal definition; `Ψ_f(σ) ∝ 1/η_compress(σ)` canonical Ψ_f formula |
| **§6.5 d_symbolic 阈值与符号化认知** | `d > d_symbolic ⇒ symbolic selection pathway` canonical d-threshold; d-value species table |
| §3.2.4 / §3.2.5 empirical patches | Dated canonical empirical anchors |
| §5.3–§5.5 S_d / F_Bio / d-value framework | SRT-internal formal claims |
| §7 H-Evo-1 through H-Evo-4 | Canonical falsifiable predictions |
| §9 synthetic biology, §10 conclusion | SRT-internal content |
| Appendix / Formalization Summary | Canonical derivation chains and formal summaries |

---

## 4. Annex File — Content and Guardrails

**File**: `Neuroscience_Annex/09_Geometric_Regularity_Interface.md`

**Frontmatter**: `canonical: false`, `claim_mode: bridge`, `layer: bridge`, `epistemic_layer: bridge`

**Guardrail block** (at file top, after frontmatter):
- Geometric regularity / Dehaene / Sablé-Meyer empirical content does not define `η_compress`, `Ψ_f`, `d_symbolic`, or `Ĝ_θ^{ventral/dorsal}`
- `η_compress = I(L_1;L_0)/H(L_1)` and `Ψ_f(σ) ∝ 1/η_compress(σ)` remain in owner §6.4
- `d > d_symbolic` remains in owner §6.5
- `Ĝ_θ^{ventral}` and `Ĝ_θ^{dorsal}` remain in owner §6.3
- `→ SRT interpretation` notes are owner cross-references, not definitions
- §6.3–§6.5 remain outside this Annex

**Per-section notes added**:
- §6.1: Annex note stating the SRT answer (Ĝ_θ^{ventral/dorsal}, η_compress, d_symbolic) is in owner §6.3–§6.5
- §6.2.2: Each finding's `→ SRT interpretation` note (converted in PR #56) explicitly names the owner section
- §6.2 证伪方向: Added note that SRT's "ontological transition" claim source is owner §6.3
- Footer note: Explicitly lists §6.3 formulas, §6.4 formulas, §6.5 formulas as outside this Annex

---

## 5. Files Modified

| File | Change type | Description |
|---|---|---|
| `Neuroscience/SRT_Neuro_07_Evo_Devo.md` | Modified | §6.1–§6.2 replaced with Geometric Regularity Annex pointer; Refactor Notes updated (Batch 2c noted); Current Reading Map §6 entry updated |
| `Neuroscience_Annex/README.md` | Modified | Added `09_Geometric_Regularity_Interface.md` entry; updated NEURO-07 owner link to cover both 08 and 09; added Operations records links |

## 6. Files Created

| File | Description |
|---|---|
| `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` | New Annex file — §6.1 + §6.2 external empirical content with guardrails and owner cross-references |
| `Operations/PR_D_Batch2c2_Neuro_07_Geometric_Regularity_Extraction_Record.md` | This file — extraction record |

---

## 7. Formula Safety Confirmation

- [ ] `Ĝ_θ^{ventral}: L_0^{visual} → L_1^{object}` — **unchanged, remains in owner §6.3**
- [ ] `Ĝ_θ^{dorsal}: L_1^{object} → L_1^{symbolic}` — **unchanged, remains in owner §6.3**
- [ ] `η_compress = I(L_1;L_0)/H(L_1)` — **unchanged, remains in owner §6.4**
- [ ] `Geometric Regularity ∝ η_compress ∝ 1/MDL(shape)` — **unchanged, remains in owner §6.4**
- [ ] `Ψ_f(σ) ∝ 1/η_compress(σ)` — **unchanged, remains in owner §6.4**
- [ ] `d > d_symbolic ⇒ symbolic selection pathway` — **unchanged, remains in owner §6.5**
- [ ] d-value species table — **unchanged, remains in owner §6.5**
- [ ] No formulas moved to Annex
- [ ] No formulas deleted
- [ ] No formulas modified

---

## 8. Safety Record

- [ ] No Part A formal axioms changed.
- [ ] No formulas changed.
- [ ] `Ĝ_θ^{ventral/dorsal}` unchanged and remain in owner §6.3.
- [ ] `η_compress` definition unchanged and remains in owner §6.4.
- [ ] `Ψ_f ∝ 1/η_compress` formula unchanged and remains in owner §6.4.
- [ ] `d_symbolic` threshold unchanged and remains in owner §6.5.
- [ ] §6.3 content unchanged.
- [ ] §6.4 content unchanged.
- [ ] §6.5 content unchanged.
- [ ] §3.2.4 / §3.2.5 empirical patches not moved.
- [ ] §5.3–§5.5 SRT framework not moved.
- [ ] H-Evo-1 through H-Evo-4 unchanged.
- [ ] Annex file has `canonical: false`.
- [ ] Annex guardrails present at file top.
- [ ] Annotation conversion prerequisite (PR #56) confirmed merged before this extraction.
- [ ] No Core/, Core_Law/, AI/, Philosophy/, Public/, Papers/, graphify-out/ files touched.
- [ ] No S0-S6, L0/L1/L2, Ψ_f, d-value, Ĝ_θ, T_dir canonical definitions changed.

---

## 9. Recommended Next Step

**PR-D Batch 2 Round-1 Closure**: The core Batch 2 extraction series (NEURO-06 §2/§6 in Batch 2a, NEURO-07 §3.2/§5/§8 in Batch 2b, NEURO-07 §6 in Batch 2c) is now complete. A closure PR should update `STATUS.md` and `_SRT_INDEX.md` to reflect the current Annex structure (four Annex files: 07, 08, 09, 10) and confirm that the remaining SRT-internal content in NEURO-07 (§6.3–§6.5, §9, §10, Appendix) is intentionally owner-retained.
