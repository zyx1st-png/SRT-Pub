---
id: SRT-OPS-PR-D-BATCH2B-NEURO07-EXTRACTION-2026-04-28
type: extraction_record
tags:
  - Operations
  - Extraction
  - Neuroscience
  - PR-D
  - EvoDevo
  - Levin
  - ConvergentEvolution
  - Waddington
status: complete
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-28
reference_audit: Operations/Archive_Records/PR_D_Batch2b_Neuro_07_PreExtraction_Audit.md
reference_adjudication: Operations/Archive_Records/PR_D_Batch2_GRT_Deduplication_Adjudication.md
pr: PR-D Batch 2b — Extract Neuro 07 Evo-Devo interface
machine_summary: >
  Extraction record for PR-D Batch 2b. Moved SRT-NEURO-07 §3.2.1–3.2.3
  (Levin bioelectric experiments), §5.1–5.2 (convergent evolution empirical
  basis — García-Moreno, Zaremba, Kempynck & Hecker, Science 2025), and §8
  (Waddington landscape reinterpretation) to
  Neuroscience_Annex/08_Evo_Devo_Interface.md.
  Owner file retains all Part A axioms, empirical patches (§3.2.4/3.2.5),
  SRT framework sections (§3.3/3.4, §5.3–5.5), §6 (geometric regularity),
  and all H-Evo predictions. Also corrects PR-B navigation label error
  ("§6 GRT" → geometric regularity / Dehaene). No formulas changed.
---

# PR-D Batch 2b: Neuro 07 Evo-Devo Extraction Record

**Date**: 2026-04-28
**PR scope**: Extract SRT-NEURO-07 bridge/interface sections to Annex; fix PR-B navigation label error
**Audit reference**: [`Operations/Archive_Records/PR_D_Batch2b_Neuro_07_PreExtraction_Audit.md`](PR_D_Batch2b_Neuro_07_PreExtraction_Audit.md)
**Adjudication reference**: [`Operations/Archive_Records/PR_D_Batch2_GRT_Deduplication_Adjudication.md`](PR_D_Batch2_GRT_Deduplication_Adjudication.md)

---

## 1. Sections Moved

| Source section | Destination | Content |
|---|---|---|
| NEURO-07 §3.2.1 双头涡虫实验 | `Neuroscience_Annex/08_Evo_Devo_Interface.md` §3.2.1 | Double-headed planaria experiment: gap junction manipulation, stable two-headed phenotype, SRT interpretation via θ_morpho |
| NEURO-07 §3.2.2 青蛙眼睛移位实验 | `Neuroscience_Annex/08_Evo_Devo_Interface.md` §3.2.2 | Frog eye transplant experiment: ectopic eye navigation, SRT interpretation via bioelectric anatomical map |
| NEURO-07 §3.2.3 癌症电学逆转实验 | `Neuroscience_Annex/08_Evo_Devo_Interface.md` §3.2.3 | Cancer electrical reversal: ion channel manipulation, normalization, SRT interpretation via Φ_coupling / d-value restoration |
| NEURO-07 §5 source citation block | `Neuroscience_Annex/08_Evo_Devo_Interface.md` §5 header | García-Moreno et al., Zaremba et al., Kempynck & Hecker, Science 387 (2025) source citation |
| NEURO-07 §5.1 回路趋同之谜 | `Neuroscience_Annex/08_Evo_Devo_Interface.md` §5.1 | Circuit convergence mystery: avian DVR vs. mammalian neocortex; 10g bird brain / 400g chimp equivalence |
| NEURO-07 §5.2 实证基础 (§5.2.1–5.2.3) | `Neuroscience_Annex/08_Evo_Devo_Interface.md` §5.2 | Three Science 2025 scRNA-seq studies: García-Moreno (chicken/mouse/gecko), Zaremba (avian pallium atlas), Kempynck & Hecker (deep learning regulatory elements) |
| NEURO-07 §8.1 经典 Waddington 景观 | `Neuroscience_Annex/08_Evo_Devo_Interface.md` §8.1 | Classical Waddington landscape: valleys (chreods), ridges, rolling ball |
| NEURO-07 §8.2 SRT 重新诠释 | `Neuroscience_Annex/08_Evo_Devo_Interface.md` §8.2 | SRT reinterpretation table: valley = L_2 attractor, ridge = L_0 barrier, ball = Ĝ_θ state, landscape = L_0^anatomical; three SRT unique contributions |

**Total content moved**: 8 sections / subsections, approximately 70 lines of bridge/interface content.

---

## 2. Navigation Label Correction

**Error corrected**: PR-B Refactor Notes (and Current Reading Map) contained "§6 GRT comparison" — wrong label. NEURO-07 §6 is "几何规则性与选择的符号化压缩" (geometric regularity / Dehaene / symbolic compression). No GRT / Hunt & Schooler content exists in NEURO-07.

**Changes made to NEURO-07 navigation block**:

| Location | Old text | New text |
|---|---|---|
| Refactor Notes heading | `(PR-B: navigation-only)` | `(PR-B: navigation-only; updated PR-D Batch 2b 2026-04-28)` |
| Refactor Notes line 2 | `Navigation-only update. No formulas changed. No theory content changed.` | `PR-B: Navigation-only update. No formulas changed. No theory content changed.` |
| Refactor Notes line 3 | `Candidate extraction, if any, must happen in a separate human-reviewed PR-D.` | `PR-D Batch 2b (2026-04-28): §3.2.1–3.2.3, §5.1–5.2, and §8 extracted to Neuroscience_Annex/08_Evo_Devo_Interface.md.` |
| Refactor Notes line 4 | `§3.2 Levin interface, §5 convergent evolution, §6 GRT, and §8 Waddington are possible future Annex candidates.` | `§6 (geometric regularity / Dehaene / symbolic compression) is NOT a GRT section. §6.1–6.2 are external empirical; §6.3–6.5 contain SRT-internal d_symbolic and η_compress / Ψ_f claims. Requires separate adjudication before extraction.` |
| Refactor Notes line 8 | `GRT comparison overlaps with SRT-NEURO-06 §6; a deduplication decision is needed before PR-D.` | Removed (replaced by §6 clarification above; GRT deduplication resolved in PR #51) |
| Current Reading Map bridge section | `§6 GRT comparison` | `§6 geometric regularity / Dehaene / symbolic compression (NOT a GRT section; full §6 remains pending separate adjudication)` |

---

## 3. Owner File Summary — What Replaced the Extracted Sections

### 3.1 §3.2 replacement

§3.2.1–3.2.3 body replaced with **Levin Interface Annex Pointer** that:
- Points to `Neuroscience_Annex/08_Evo_Devo_Interface.md`
- States that θ_morpho, Φ_coupling, and d-value are applied as interpretive terms in the experiments, not defined there
- States canonical definitions are in Part A: Ax-BIO-2b (θ_morpho), Ax-BIO-1 (L2^bioelectric)
- States §3.2.4 and §3.2.5 remain below as canonical empirical anchors

### 3.2 §5 replacement

§5 source citation + §5.1–5.2 body replaced with **Convergent Evolution Annex Pointer** that:
- Points to `Neuroscience_Annex/08_Evo_Devo_Interface.md` for §5.1 and §5.2
- States external empirical foundation is bridge/interface material
- States SRT-internal interpretation (S_d attractor topology, F_Bio functional equivalence, d-value universality) remains in §5.3–5.5
- Retains the source citation as a brief reference in the pointer block

### 3.3 §8 replacement

§8.1 + §8.2 body replaced with **Waddington Landscape Annex Pointer** that:
- Points to `Neuroscience_Annex/08_Evo_Devo_Interface.md`
- States Waddington landscape does not define Ĝ_devo, L2^bioelectric, or Generativity_devo ∝ 1/Ψ_f(θ_morpho)
- States definitions are in Part A (Ax-BIO-2, Ax-BIO-1, Ax-BIO-3)
- States correspondence table entries are bridge mappings, not canonical identities

---

## 4. Sections NOT Moved — Owner File Retention

| Section | Reason retained |
|---|---|
| All Part A axioms (Ax-BIO-1/2/2b/3, Ax-EVO-1/2/3, Ax-PATH-1/2) | Canonical SRT formal content |
| `Ĝ_devo:(L0^morpho, θ_genome, θ_physio) → L1^phenotype` | Formal operator definition |
| `L2^bioelectric ⊃ L2^synaptic` | Ax-BIO-1 canonical claim |
| `Generativity_devo ∝ 1/Ψ_f(θ_morpho)` | Ax-BIO-3 canonical axiom |
| T-EVO-1, T-EVO-2, C-EVO-1, C-EVO-2 | Theorems and corollaries |
| Evo-Devo Bridge Note (P3/P4 self-labeled) | Self-labeled guardrail — stays in owner by design |
| Science 2025 Empirical Anchor block (Part A) | Canonical empirical anchors for Ax-EVO-3/T-EVO-2 |
| §3.2 header ("Levin 实验的本体论意义") + Annex pointer | Owner navigation |
| **§3.2.4 癌症的机械窗口 (2026-03-16 patch)** | Dated empirical anchor — canonical |
| **§3.2.5 单细胞联结学习窗口 (2026-03-21 patch)** | Dated empirical anchor — canonical |
| §3.3 认知-形态同构 | SRT-internal ontological thesis |
| §3.4 癌症是算子的去联邦化 | SRT-internal cancer ontology using Ĝ_θ, d-value, Ψ_f^cross |
| §4 代价与风险 | SRT-internal risk assessment |
| §5 header + Annex pointer | Owner navigation |
| **§5.3 S_d 吸引子拓扑** | Contains `S_d = {σ ∈ L_0^anatomical : d(Ĝ_σ) > 0}` |
| **§5.4 F_Bio 多态等价性** | `F_Bio^{avian}(θ_DVR) ≅ F_Bio^{mammalian}(θ_neocortex)` |
| **§5.5 d 值通用性** | `d > 0 ⟺ effective L_0 → L_1 selection` — canonical d-value |
| **§6 (entire) 几何规则性与选择的符号化压缩** | §6.3–6.5 contain SRT-internal `Ψ_f ∝ 1/η_compress` and `d > d_symbolic`; §6.1–6.2 entangled via `→ SRT意义` annotations; requires separate adjudication |
| **§7 H-Evo-1 through H-Evo-4** | Canonical falsifiable predictions |
| §8 header + Annex pointer | Owner navigation |
| §9 合成生物学的启示 | SRT-internal application conclusions |
| §10 结语 | SRT-internal conclusion |
| Appendix (推导链索引, Formalization Summary, Mechanism Explanation, 理论边界声明) | Canonical derivation chains and formal summaries |

---

## 5. Annex File — Content and Guardrails

**File**: `Neuroscience_Annex/08_Evo_Devo_Interface.md`

**Frontmatter**: `canonical: false`, `claim_mode: bridge`, `layer: bridge`, `epistemic_layer: bridge`

**Guardrail block** (at file top, after frontmatter):
- `θ_morpho`, `Ĝ_devo`, and `L2^bioelectric` are defined in Part A (Ax-BIO-2b, Ax-BIO-2, Ax-BIO-1) — not in this Annex
- Levin experiments do not redefine `Generativity_devo` or `Ψ_f(θ_morpho)`; `Φ_coupling` is a bridge proxy
- Convergent evolution examples do not define Ax-EVO-1/2/3, S_d, F_Bio equivalence, or d-value universality
- Waddington landscape is analogical interface; does not define `Ĝ_devo`, `L2^bioelectric`, or `L_2` attractor topology
- §3.2.4/§3.2.5 empirical patches and all §6 material remain outside this Annex

**Per-section Annex notes added**:
- §3.2.1: `θ_morpho` is defined in Ax-BIO-2b; Levin experiment supports but does not define it; `Φ_coupling` is a bridge proxy
- §3.2.2: "anatomical map in bioelectric field" is bridge-level description of `L2^bioelectric` guidance; not a definition source
- §3.2.3: `Φ_coupling` collapse / d-value restoration is bridge interpretation applying owner §3.4 cancer mechanism; §3.2.4 stays in owner
- §5.1: Problem framing only; SRT interpretation of S_d remains in owner §5.3
- §5.2: Three studies support Ax-EVO-3 but do not define it; S_d, F_Bio, d-value universality remain in owner §5.3–5.5
- §8.2: Correspondence table entries are analogical bridge mappings, not ontological identities; all formal definitions in Part A

---

## 6. Files Modified

| File | Change type | Description |
|---|---|---|
| `Neuroscience/SRT_Neuro_07_Evo_Devo.md` | Modified | §3.2.1–3.2.3 replaced with Levin Annex pointer; §5 source citation + §5.1–5.2 replaced with convergent evolution pointer; §8.1–8.2 replaced with Waddington pointer; Refactor Notes updated (§6 GRT label corrected, PR-D Batch 2b noted); Current Reading Map §6 label corrected |
| `Neuroscience_Annex/README.md` | Modified | Added `08_Evo_Devo_Interface.md` entry; added NEURO-07 owner link; added Operations record link |

## 7. Files Created

| File | Description |
|---|---|
| `Neuroscience_Annex/08_Evo_Devo_Interface.md` | New Annex file containing extracted §3.2.1–3.2.3, §5.1–5.2, and §8 bridge content |
| `Operations/Archive_Records/PR_D_Batch2b_Neuro_07_Evo_Devo_Extraction_Record.md` | This file — extraction record |

---

## 8. Formula Safety Confirmation

- [ ] `Ĝ_devo:(L0^morpho,θ_genome,θ_physio)→L1^phenotype` — **unchanged, remains in owner**
- [ ] `L2^bioelectric ⊃ L2^synaptic` (Ax-BIO-1) — **unchanged, remains in owner**
- [ ] `Ĝ_neural ⊂ Ĝ_devo` (Ax-BIO-2) — **unchanged, remains in owner**
- [ ] `Generativity_devo ∝ 1/Ψ_f(θ_morpho)` (Ax-BIO-3) — **unchanged, remains in owner**
- [ ] `S_d = {σ ∈ L_0^anatomical : d(Ĝ_σ) > 0}` — **unchanged, remains in owner (§5.3)**
- [ ] `F_Bio^{avian}(θ_DVR) ≅ F_Bio^{mammalian}(θ_neocortex)` — **unchanged, remains in owner (§5.4)**
- [ ] `d > 0 ⟺ effective L_0 → L_1 selection` — **unchanged, remains in owner (§5.5)**
- [ ] `Ψ_f ∝ 1/η_compress` (§6.4) — **unchanged, remains in owner**
- [ ] `d > d_symbolic` (§6.5) — **unchanged, remains in owner**
- [ ] No formulas moved to Annex
- [ ] No formulas deleted
- [ ] No formulas modified

---

## 9. Safety Record

- [ ] No Part A formal axioms changed.
- [ ] No formulas changed.
- [ ] Evo-Devo Bridge Note unchanged and remains in owner file.
- [ ] `Ĝ_devo` definition unchanged and remains in owner file.
- [ ] `L2^bioelectric` definition unchanged and remains in owner file.
- [ ] Genome-as-Generative-Model unchanged and remains in owner file.
- [ ] Ax-BIO-1/2/2b/3 unchanged and remain in owner file.
- [ ] Ax-EVO-1/2/3 unchanged and remain in owner file.
- [ ] Ax-PATH-1/2 unchanged and remain in owner file.
- [ ] T-EVO-1/2, C-EVO-1/2 unchanged and remain in owner file.
- [ ] §3.2.4 cancer mechanical window patch (2026-03-16) not moved — remains in owner file.
- [ ] §3.2.5 Stentor learning patch (2026-03-21) not moved — remains in owner file.
- [ ] §5.3 S_d formal argument not moved — remains in owner file.
- [ ] §5.4 F_Bio equivalence not moved — remains in owner file.
- [ ] §5.5 d-value universality not moved — remains in owner file.
- [ ] §6 (entire) not moved — remains in owner file pending separate adjudication.
- [ ] H-Evo-1 through H-Evo-4 unchanged and remain in owner file.
- [ ] Annex file has `canonical: false`.
- [ ] Annex guardrails present at file top.
- [ ] No Core/, Core_Law/, AI/, Philosophy/, Public/, Papers/, graphify-out/ files touched.
- [ ] No S0-S6, L0/L1/L2, Ψ_f, d-value, Ĝ_θ, T_dir canonical definitions changed.

---

## 10. Recommended Next Steps

**PR-D Batch 2c** (NEURO-07 §6 extraction) requires a dedicated §6 adjudication first. The key issues:
1. `Ψ_f ∝ 1/η_compress` (§6.4) — is this extractable or must it stay as owner-level canonical content?
2. `d > d_symbolic` threshold (§6.5) — same question.
3. `→ SRT意义` annotations in §6.2 are tightly coupled to §6.3–6.5 SRT-internal content — requires a decision on how to handle them in extraction.

**NEURO-07 §6 adjudication** (PR-D0.6 or similar) should be the next step before any §6 extraction is attempted.
