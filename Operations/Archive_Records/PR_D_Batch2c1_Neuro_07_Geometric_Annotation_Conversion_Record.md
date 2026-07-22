---
id: SRT-OPS-PR-D-BATCH2C1-NEURO07-ANNOTATION-CONVERSION-2026-04-29
type: conversion_record
tags:
  - Operations
  - AnnotationConversion
  - Neuroscience
  - PR-D
  - GeometricRegularity
  - Dehaene
status: complete
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
reference_adjudication: Operations/Archive_Records/PR_D0_6_Neuro_07_Geometric_Regularity_Adjudication.md
pr: PR-D Batch 2c-1 — Convert Neuro 07 geometric annotations
machine_summary: >
  Annotation conversion pass for NEURO-07 §6.2.2. Replaces four inline
  `→ SRT意义` / `→ Cross-ref` annotations with owner cross-reference notes
  pointing to §6.3–6.5. No empirical findings changed. No formulas changed.
  No sections moved. No Annex files created. Prerequisite for Batch 2c-2
  extraction of §6.1–6.2 to Neuroscience_Annex/09_Geometric_Regularity_Interface.md.
---

# PR-D Batch 2c-1: Neuro 07 Geometric Annotation Conversion Record

**Date**: 2026-04-29
**PR scope**: Annotation conversion only — convert 4 inline SRT annotations in §6.2.2 to owner cross-reference notes
**Adjudication reference**: [`Operations/Archive_Records/PR_D0_6_Neuro_07_Geometric_Regularity_Adjudication.md`](PR_D0_6_Neuro_07_Geometric_Regularity_Adjudication.md)

> **This PR did not**: create any Annex file, move any section, delete any content, change any formula, change any empirical finding, change any canonical definition.

---

## 1. Purpose

The adjudication in PR-D0.6 identified that §6.2.2's inline `→ SRT意义` and `→ Cross-ref` annotations were the key blocker for extracting §6.2 to Annex. These annotations contained inline references to owner-file canonical formulas (`η_compress`, `Ψ_f`, `d_symbolic`) in a way that would leave the Annex with dangling formula references if §6.2 were extracted without conversion.

This PR performs the conversion: replacing each inline formula-citation annotation with an explicit owner cross-reference note that:
- Preserves the pointer to the SRT interpretation
- Locates the interpretation in the owner file (§6.3, §6.4, §6.5)
- Clarifies that the empirical finding supports but does not define the SRT concept

After this conversion, §6.2 no longer contains inline formula references to canonical claims — it contains only: empirical findings `[R]` + explicit owner-section pointers. This makes §6.2 safely extractable in Batch 2c-2.

---

## 2. Annotations Converted

### 2.1 Finding 1 — 规则性效应

**Before**:
```
→ SRT 意义：支持 §6.4 的 $\eta_{compress} \propto 1/\text{MDL}$（规则形状 L₁ 编码代价低 = 低 $\Psi_f$）。
```

**After**:
```
→ SRT interpretation: see owner §6.4 (`η_compress`, `Ψ_f` relationship). This empirical finding supports the owner-file interpretation that geometric regularity can serve as an operational proxy for compression efficiency; it does not define `η_compress` or `Ψ_f`.
```

**Change type**: Inline formula citation → explicit owner-section cross-reference. The SRT formula `η_compress ∝ 1/MDL` remains in owner §6.4; the annotation now points to §6.4 as the definition source rather than citing the formula inline.

---

### 2.2 Finding 2 — 压缩编码

**Before**:
```
→ Cross-ref: §6.4 $\eta_{compress}$ 神经实现；MDL 作为 $\Psi_f$ 的操作化代理之一。
```

**After**:
```
→ SRT interpretation: see owner §6.4 (`η_compress` as neural implementation; MDL as one operational proxy for `Ψ_f`). The empirical finding is brain activity tracking MDL; the SRT formula remains defined in the owner file.
```

**Change type**: `Cross-ref` style inline citation → explicit owner-section cross-reference with boundary clarification. Adds explicit statement that the SRT formula is in the owner file.

---

### 2.3 Finding 3 — CNN 失败

**Before**:
```
→ **[H含义]**：CNN 失败本身为 SRT §6.3 的预测提供支持证据——背侧通路执行的是"离散符号化 $L_0 \to L_1$"选择，超出连续函数逼近的范围，与 SRT 的"本体论跃迁"框架一致。
```

**After**:
```
→ SRT interpretation: see owner §6.3 (`Ĝ_θ^{dorsal}` as symbolic selection / ontological transition). The empirical finding is CNN failure on late dorsal-prefrontal signals; the SRT operator-specialization claim remains in the owner file.
```

**Change type**: `[H含义]` inline SRT interpretation → explicit owner-section cross-reference. The finding label also updated from `**[R + H含义]**` to `**[R]**` for consistency — the `[H含义]` tag indicated an H-implication following the empirical finding, which is now replaced by the standardized owner cross-reference format. The empirical finding itself (CNN cannot explain late dorsal-prefrontal signal) is unchanged.

---

### 2.4 Finding 5 — 人类皮层扩展

**Before**:
```
→ SRT 意义：支持 §6.5 的 d 值阈值假设——顶叶扩展 = $d_{symbolic}$ 阈值所需的额外具身硬件（扩展皮层 = 更大 θ 参数空间）。
```

**After**:
```
→ SRT interpretation: see owner §6.5 (`d_symbolic` threshold; parietal expansion as embodied hardware condition). This empirical finding supports the owner-file interpretation but does not define `d_symbolic` or the d-value threshold.
```

**Change type**: Inline SRT interpretation → explicit owner-section cross-reference with boundary clarification. Adds explicit statement that `d_symbolic` is not defined by this finding.

---

## 3. What Was NOT Changed

| Item | Status |
|---|---|
| Empirical finding text for all 5 findings | **Unchanged** |
| Finding 4 (发育先天性, no SRT annotation) | **Unchanged** — no annotation to convert |
| §6.2 proof falsification directions (证伪方向) | **Unchanged** |
| §6.2.1 dual encoding table | **Unchanged** |
| §6.1 problem framing | **Unchanged** |
| §6.3 SRT layered selection architecture | **Unchanged** |
| §6.4 `η_compress = I(L_1;L_0)/H(L_1)` | **Unchanged** |
| §6.4 `Ψ_f(σ) ∝ 1/η_compress(σ)` | **Unchanged** |
| §6.5 `d > d_symbolic ⇒ symbolic selection pathway` | **Unchanged** |
| §6.5 d-value species table | **Unchanged** |
| `Ĝ_θ^{ventral}` / `Ĝ_θ^{dorsal}` operator definitions | **Unchanged** |
| All Part A axioms (Ax-BIO, Ax-EVO, etc.) | **Unchanged** |
| NEURO-07 frontmatter | **Unchanged** |
| All other §6 content | **Unchanged** |
| All non-§6 content in NEURO-07 | **Unchanged** |
| No Annex files created | **Confirmed** |
| No sections moved | **Confirmed** |
| No content deleted | **Confirmed** |

---

## 4. Files Modified

| File | Change type | Description |
|---|---|---|
| `Neuroscience/SRT_Neuro_07_Evo_Devo.md` | Modified | 4 annotations in §6.2.2 converted from inline formula citations to owner cross-reference notes |

## 5. Files Created

| File | Description |
|---|---|
| `Operations/Archive_Records/PR_D_Batch2c1_Neuro_07_Geometric_Annotation_Conversion_Record.md` | This file — annotation conversion record |

---

## 6. Safety Record

- [ ] No formulas changed.
- [ ] `η_compress = I(L_1;L_0)/H(L_1)` unchanged — remains in owner §6.4.
- [ ] `Ψ_f(σ) ∝ 1/η_compress(σ)` unchanged — remains in owner §6.4.
- [ ] `d > d_symbolic` unchanged — remains in owner §6.5.
- [ ] `Ĝ_θ^{ventral}: L_0^{visual} → L_1^{object}` unchanged — remains in owner §6.3.
- [ ] `Ĝ_θ^{dorsal}: L_1^{object} → L_1^{symbolic}` unchanged — remains in owner §6.3.
- [ ] Ax-BIO/EVO/PATH axioms unchanged.
- [ ] H-Evo-1 through H-Evo-4 unchanged.
- [ ] No Annex files created.
- [ ] No sections moved.
- [ ] No empirical findings deleted or modified.
- [ ] No Core/, Core_Law/, AI/, Philosophy/, Public/, Papers/, graphify-out/ files touched.
- [ ] No S0-S6, L0/L1/L2, Ψ_f, d-value, Ĝ_θ, T_dir canonical definitions changed.

---

## 7. Recommended Next Step

**PR-D Batch 2c-2**: Extract §6.1 and §6.2 (now with owner-pointer annotations) to a new `Neuroscience_Annex/09_Geometric_Regularity_Interface.md`.

Batch 2c-2 scope:
- Create `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` with full guardrail block
- Replace §6.1 + §6.2 body in owner with pointer block + §6.3–6.5 retained in full
- Update `Neuroscience_Annex/README.md` with §09 entry
- Update NEURO-07 navigation block (Refactor Notes) to note Batch 2c extraction

The annotation conversion in this PR makes §6.2 extractable: the `→ SRT interpretation: see owner §6.x` format is the correct Annex-note form, and the extracted §6.2 will not contain inline formula references to owner-file canonical formulas.
