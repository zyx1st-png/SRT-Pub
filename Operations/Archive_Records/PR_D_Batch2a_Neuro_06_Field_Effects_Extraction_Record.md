---
id: SRT-OPS-PR-D-BATCH2A-NEURO06-EXTRACTION-2026-04-28
type: extraction_record
tags:
  - Operations
  - Extraction
  - Neuroscience
  - PR-D
  - FieldEffects
  - GWT
  - IIT
  - GRT
status: complete
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-28
reference_adjudication: Operations/Archive_Records/PR_D_Batch2_GRT_Deduplication_Adjudication.md
pr: PR-D Batch 2a — Extract Neuro 06 field effects interfaces
machine_summary: >
  Extraction record for PR-D Batch 2a. Moved SRT-NEURO-06 Part B §2.1–§2.3
  (synaptic synchrony / GWT / IIT comparisons) and §6.1–§6.2 (GRT / Hunt &
  Schooler comparison) to Neuroscience_Annex/07_Field_Effects_Interface.md.
  Owner file retains all Part A axioms, QUALIA-1/2, formal anchors, §6.3,
  and empirical patches. No formulas changed.
---

# PR-D Batch 2a: Neuro 06 Field Effects Extraction Record

**Date**: 2026-04-28
**PR scope**: Extract SRT-NEURO-06 Part B external-theory interface sections to Annex
**Adjudication reference**: [`Operations/Archive_Records/PR_D_Batch2_GRT_Deduplication_Adjudication.md`](PR_D_Batch2_GRT_Deduplication_Adjudication.md)

---

## 1. Sections Moved

| Source section | Destination | Content |
|---|---|---|
| NEURO-06 Part B §2.1 突触同步假说 | `Neuroscience_Annex/07_Field_Effects_Interface.md` §2.1 | Synaptic synchrony hypothesis — core claim, advantages, fatal flaws; Singer & Gray 1995 reference |
| NEURO-06 Part B §2.2 全局工作空间理论 (GWT) | `Neuroscience_Annex/07_Field_Effects_Interface.md` §2.2 | Global Workspace Theory — core claim, advantages, fatal flaws; fMRI ignition reference |
| NEURO-06 Part B §2.3 整合信息理论 (IIT) | `Neuroscience_Annex/07_Field_Effects_Interface.md` §2.3 | IIT Φ — core claim, advantages, fatal flaws; 2024 critique reference |
| NEURO-06 Part B §6.1 GRT核心主张 | `Neuroscience_Annex/07_Field_Effects_Interface.md` §6.1 | Hunt & Schooler (2019) GRT: panpsychism, resonant combination, resonance as information integration |
| NEURO-06 Part B §6.2 SRT-GRT会聚点 | `Neuroscience_Annex/07_Field_Effects_Interface.md` §6.2 | Three-row convergence table: EM field resonance, phase locking, resonance boundary |

**Total content moved**: 5 sections, approximately 40 lines of bridge/interface content.

---

## 2. Owner File Summary — What Replaced the Extracted Sections

### 2.1 §2 replacement

The `# 2 主流解法谱系` section now contains a **Part B Interface Summary** that:
- Points to `Neuroscience_Annex/07_Field_Effects_Interface.md`
- States the extracted materials are bridge/interface, not SRT Core definitions
- Confirms that GWT ignition does not define `\hat{G}_\theta`; IIT `Φ` does not define QUALIA-1/2 or Resonome; synaptic synchrony material does not replace Ax-FIELD-1 or Def-Ephaptic-Binding
- Lists owner formal anchors explicitly: QUALIA-1/2, Ax-FIELD-1, Def-Ephaptic-Binding, T-FIELD-1/2, C-FIELD-1, `κ_sync`, `Ĝ_macro`, H-Field predictions

### 2.2 §6 replacement

The `# 6 与广义共振理论 (GRT) 的整合` section now contains a **GRT Interface Annex Pointer** that:
- Points to `Neuroscience_Annex/07_Field_Effects_Interface.md` for §6.1 and §6.2
- States GRT is bridge/interface; GRT resonance does not define `κ_sync`, `Ĝ_macro`, or T-FIELD-2
- States convergence table `✓` marks are functional analogies, not ontological identities
- States §6.3 remains in owner because it contains SRT-internal differentiation claims

---

## 3. Sections NOT Moved — Owner File Retention

| Section | Reason retained |
|---|---|
| All Part A formal axioms (Ax-FIELD-1, Def-Ephaptic-Binding, T-FIELD-1/2, C-FIELD-1, Ax-TEMP-1/2, Ax-QUALIA-1/2) | Canonical SRT formal content |
| QUALIA-1 (Resonome: `R={λ_i,φ_i}`) | Defines SRT phenomenology |
| QUALIA-2 (L2 Incompleteness: `Π_L2(R_θ)≠R_θ`) | Canonical SRT claim |
| Ax-FIELD-1 (`ẋ=F(σ,θ)+α∇ε`) | Formal field coupling axiom |
| Def-Ephaptic-Binding (`κ_sync∝∫|E_LFP|²dV`) | Defines `κ_sync` |
| T-FIELD-2 (`Ĝ_macro=C_field∘Ĝ_micro`) | Nested operator theorem |
| T-FIELD-1, C-FIELD-1 | Coherence-binding theorem and corollary |
| §1 Binding problem and explanatory gap (including 2026 patch) | Problem-statement context, contains SRT-relevant canonical patch |
| §3 SRT差异点：场作为算子载体 | SRT-internal framework; contains canonical SRT ontology reconstruction table and dual-network claims |
| §4 代价与风险 | SRT-internal risk assessment |
| §5 可证伪预测与开放性问题 (H-Field-1 through H-Field-4) | Canonical falsifiable predictions and empirical patches |
| **§6.3 SRT独特贡献 over GRT** | SRT-internal differentiation claims (L0/L1/L2, θ, downward causality, d-value operationalization) |
| §7 神经调质与场动力学 | SRT-internal neurotransmitter-field modulation content |
| §8 结语 | SRT-internal framework conclusion |
| Appendix (推导链索引, Formalization Summary, Mechanism Explanation, 理论边界声明, §9 预印本补注) | Canonical derivation chains and formal summaries |
| All empirical patches (natural vision binding 2026-03-21, EM/UPE 2026-03-18, axonal theta 2026) | Canonical empirical anchors |

---

## 4. Annex File — Content and Guardrails

**File**: `Neuroscience_Annex/07_Field_Effects_Interface.md`

**Frontmatter**: `canonical: false`, `claim_mode: bridge`, `layer: bridge`, `epistemic_layer: bridge`

**Guardrail block** (at file top, after frontmatter):
- GWT ignition does not define SRT field binding or `L_0 → L_1` selection
- IIT `Φ` does not define Resonome, QUALIA-1, QUALIA-2, or field-binding thresholds
- GRT resonance does not define `κ_sync`, `Ĝ_macro`, `\hat{G}_\theta`, or T-FIELD-2
- Synaptic synchrony material is candidate neural proxy, not a replacement for SRT formal axioms
- §6.3 "SRT独特贡献" is not part of this Annex

**Per-section Annex notes added**:
- §2.1: Gamma synchrony is a candidate correlate of `κ_sync`, not its definition
- §2.2: GWT ignition is a candidate operational proxy for `L_0 → L_1` selection, not a definition
- §2.3: IIT `Φ` is treated as approximate proxy for `Irreducibility(Ĝ_θ)` — pointer to NEURO-09 integration equations
- §6.1: GRT's panpsychism is not endorsed or required by SRT
- §6.2: Convergence table `✓` marks are functional analogies; `ω_slowest^{shared}` is SRT's own operationalization

---

## 5. Files Modified

| File | Change type | Description |
|---|---|---|
| `Neuroscience/SRT_Neuro_06_Field_Effects.md` | Modified | §2 replaced with owner summary + pointer; §6.1–§6.2 replaced with GRT Annex pointer; §6.3 unchanged |
| `Neuroscience_Annex/README.md` | Modified | Added `07_Field_Effects_Interface.md` entry; updated Owner Files section; added Operations records |

## 6. Files Created

| File | Description |
|---|---|
| `Neuroscience_Annex/07_Field_Effects_Interface.md` | New Annex file containing extracted §2.1–§2.3 + §6.1–§6.2 bridge content |
| `Operations/Archive_Records/PR_D_Batch2a_Neuro_06_Field_Effects_Extraction_Record.md` | This file — extraction record |

---

## 7. Formula Safety Confirmation

- [ ] Ax-FIELD-1 (`ẋ=F(σ,θ)+α∇ε`) — **unchanged, remains in owner**
- [ ] Def-Ephaptic-Binding (`κ_sync∝∫|E_LFP|²dV`) — **unchanged, remains in owner**
- [ ] T-FIELD-2 (`Ĝ_macro=C_field∘Ĝ_micro`) — **unchanged, remains in owner**
- [ ] T-FIELD-1 (`Γ>Γ_c ⇒ Δφ_i→0`) — **unchanged, remains in owner**
- [ ] Ax-QUALIA-1 (`R={λ_i,φ_i}`) — **unchanged, remains in owner**
- [ ] Ax-QUALIA-2 (`Π_L2(R_θ)≠R_θ`) — **unchanged, remains in owner**
- [ ] No formulas moved to Annex
- [ ] No formulas deleted
- [ ] No formulas modified

---

## 8. Safety Record

- [ ] No Part A formal axioms changed.
- [ ] No formulas changed.
- [ ] QUALIA-1 / QUALIA-2 unchanged and remain in owner file.
- [ ] Ax-FIELD-1 unchanged and remains in owner file.
- [ ] Def-Ephaptic-Binding unchanged and remains in owner file.
- [ ] T-FIELD-1 / T-FIELD-2 unchanged and remain in owner file.
- [ ] C-FIELD-1 unchanged and remains in owner file.
- [ ] `κ_sync` definition unchanged and remains in owner file.
- [ ] `Ĝ_macro` definition unchanged and remains in owner file.
- [ ] H-Field predictions (H-Field-1 through H-Field-4) unchanged and remain in owner file.
- [ ] §6.3 SRT独特贡献 not moved — remains in owner file.
- [ ] Annex file has `canonical: false`.
- [ ] Annex guardrails present at file top.
- [ ] `SRT_Neuro_07_Evo_Devo.md` not modified.
- [ ] No Core/, Core_Law/, AI/, Philosophy/, Public/, Papers/, graphify-out/ files touched.
- [ ] No S0-S6, L0/L1/L2, Ψ_f, d-value, Ĝ_θ, T_dir canonical definitions changed.

---

## 9. Recommended Next Steps

**PR-D Batch 2b** (NEURO-07 extraction) is now unblocked for §3.2 (Levin interface), §5 (convergent evolution, partial), and §8 (Waddington). It should also include a navigation block correction for NEURO-07's §6 label (currently says "GRT" — should say "geometric regularity / Dehaene").

**NEURO-07 §6** (geometric regularity / Dehaene) requires a separate adjudication before extraction — its §6.4–6.5 subsections contain SRT-internal d_symbolic threshold claims.

**NEURO-06 owner file review**: The retained §3 (SRT差异点) contains some bridge-adjacent comparisons in §3.1 (root framework contrast table). These are SRT-internal reframings, not external-theory comparisons, and should remain in owner. No further extraction is needed for NEURO-06 in the current PR-D scope.
