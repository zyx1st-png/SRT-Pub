---
id: SRT-OPS-PR-D-BATCH2B-NEURO07-AUDIT-2026-04-28
type: audit_record
tags:
  - Operations
  - Audit
  - Neuroscience
  - PR-D
  - EvoDevo
  - Levin
  - Waddington
  - GeometricRegularity
status: audit_complete
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-28
reference_adjudication: Operations/PR_D_Batch2_GRT_Deduplication_Adjudication.md
reference_extraction: Operations/PR_D_Batch2a_Neuro_06_Field_Effects_Extraction_Record.md
pr: PR-D Batch 2b Prep — NEURO-07 Extraction Boundary Audit
machine_summary: >
  Read-only boundary audit of SRT-NEURO-07 before PR-D Batch 2b.
  Finds §3.2.1–3.2.3 (Levin experiments), §5.1–5.2 (convergent evolution
  empirical basis), and §8 (Waddington) are ready for extraction.
  §6 (geometric regularity) must be excluded from Batch 2b — §6.3–6.5
  contain SRT-internal d_symbolic and η_compress definitions.
  Corrects PR-B navigation label error ("§6 GRT" → geometric regularity).
---

# PR-D Batch 2b Prep: NEURO-07 Extraction Boundary Audit

**Date**: 2026-04-28
**Auditor**: Claude (claude-sonnet-4-6), read-only pass
**File audited**: `Neuroscience/SRT_Neuro_07_Evo_Devo.md` (793 lines, fully read)
**Triggered by**: PR-D Batch 2 adjudication plan in [`Operations/PR_D_Batch2_GRT_Deduplication_Adjudication.md`](PR_D_Batch2_GRT_Deduplication_Adjudication.md) §7.3

> **This PR did not**: modify NEURO-07, create any Annex, change any formula, change any canonical definition.

---

## 0. Executive Summary

**Three sections are ready for Batch 2b extraction. One section (§6) must be excluded and separately adjudicated.**

| Question | Answer |
|---|---|
| Which sections can enter Batch 2b? | §3.2.1–3.2.3 (Levin experiments 1–3), §5.1–5.2 (convergent evolution empirical basis), §8 (Waddington landscape) |
| Which sections must stay in owner? | §3.2.4 / §3.2.5 (empirical patches), §3.3/3.4 (SRT morpho-cognitive framework), §5.3–5.5 (SRT d-value framework), §6.3–6.5 (SRT-internal d_symbolic / η_compress / Ψ_f), §9 synthetic biology, §10 conclusion, all appendix content |
| Which sections need separate adjudication? | **§6 (entire)** — §6.1–6.2 are external Dehaene empirical content, but §6.3–6.5 contain SRT-internal formulas (`η_compress`, `d_symbolic`, `Ψ_f ∝ 1/η_compress`) that make clean extraction impossible without first adjudicating the §6 boundary |
| Can `08_Evo_Devo_Interface.md` be created in Batch 2b? | Yes — for §3.2.1–3.2.3 + §5.1–5.2 + §8 content. §6 content added in a later Batch 2c after §6 adjudication |
| "§6 GRT" navigation label error? | Confirmed: NEURO-07's navigation block Refactor Notes contain "§6 GRT" — wrong label. §6 is geometric regularity / Dehaene / symbolic compression. Correction should be included in Batch 2b execution PR |

**Recommended strategy**: **Option A** — Extract §3.2.1–3.2.3 + §5.1–5.2 + §8 in Batch 2b; exclude §6; fix navigation label. See §11.

---

## 1. Scope and Safety Record

- Only new file: `Operations/PR_D_Batch2b_Neuro_07_PreExtraction_Audit.md` (this file)
- `Neuroscience/SRT_Neuro_07_Evo_Devo.md` — read, not modified
- No Annex files created
- No content moved
- No formulas changed
- No canonical definitions changed

---

## 2. File-Level Context

`SRT_Neuro_07_Evo_Devo.md` is the Evo-Devo / bioelectricity / morphogenesis owner file. Its role in the dependency chain:

- Depends on: SRT-NEURO-06 (field and resonance logic), SRT-CORE-000, SRT-NEURO-MECH-001
- Feeds: SRT-NEURO-08 (distributed systems / immune) and beyond

**Part A formal content** (lines 1–241) must stay in owner without exception:
- Ax-BIO-1/2/2b/3, Ax-EVO-1/2/3, Ax-PATH-1/2, T-EVO-1/2, C-EVO-1/2, Evo-Devo Bridge Note
- Key formulas: `L2^bioelectric ⊃ L2^synaptic`, `Ĝ_neural ⊂ Ĝ_devo`, `Ĝ_devo:(L0^morpho,θ_genome,θ_physio)→L1^phenotype`, `Generativity_devo ∝ 1/Ψ_f(θ_morpho)`
- Empirical Anchor block (Science 2025 papers for Ax-EVO-3/T-EVO-2)

**Part B** (lines 244–793) contains mixed canonical and bridge content — this is the extraction target.

---

## 3. Section Boundary Table

| Section | Content Type | Extraction Readiness | Must Stay in Owner? | Reason |
|---|---|---|---|---|
| §1 形态发生问题 / 癌症悖论 | Problem framing — external biology | Medium | No | External framing, but interleaved with SRT relevance; borderline |
| §2 主流解法谱系 (Gene-centric, SMT, TOFT) | Pure external theory comparison | High | No | Pattern matches NEURO-06 §2; but not in current Batch 2b scope |
| **§3.2.1** 双头涡虫实验 | SRT bridge interpretation of Levin experiment | **High** | No | Levin experiment + SRT interpretation using bridge terms (θ_morpho, Φ_coupling); no formula definitions |
| **§3.2.2** 青蛙眼睛移位实验 | SRT bridge interpretation of Levin experiment | **High** | No | Same pattern; anatomical map in bioelectric field is bridge claim |
| **§3.2.3** 癌症电学逆转实验 | SRT bridge interpretation of Levin experiment | **High** | No | Φ_coupling collapse / d-value restoration is bridge application, not definition |
| §3.2.4 癌症的机械窗口 (2026-03-16 patch) | Empirical anchor — canonical | **No** | **Yes** | Dated empirical patch; uses θ_physio and state-selective gating; must stay as canonical anchor |
| §3.2.5 单细胞联结学习窗口 (2026-03-21 patch) | Empirical anchor — canonical | **No** | **Yes** | Dated empirical patch (Stentor preprint); must stay as canonical anchor |
| §3.3 认知-形态同构 | SRT-internal framework | No | **Yes** | SRT's own isomorphism claim — not external comparison |
| §3.4 癌症是算子的去联邦化 | SRT-internal canonical claim | No | **Yes** | Uses Ĝ_θ, d-value, Ψ_f^cross — canonical SRT oncology claim |
| §4 代价与风险 | SRT-internal risk assessment | No | **Yes** | SRT-internal |
| **§5.1** 回路趋同之谜 | External problem framing | **High** | No | Pure framing — no SRT claims |
| **§5.2** 实证基础 (García-Moreno / Zaremba / Kempynck, Science 2025) | Pure external empirical content | **High** | No | Three independent Science 2025 papers; no SRT formulas |
| §5.3 SRT解释: S_d 吸引子拓扑 | SRT-internal formal argument | No | **Yes** | Contains `S_d = {σ ∈ L_0^anatomical : d(Ĝ_σ) > 0}` — SRT formal definition |
| §5.4 F_Bio 多态等价性 | SRT-internal framework | No | **Yes** | `F_Bio^{avian}(θ_DVR) ≅ F_Bio^{mammalian}(θ_neocortex)` — SRT formal claim |
| §5.5 d 值通用性 | SRT-internal canonical claim | No | **Yes** | `d > 0 ⟺ effective L_0 → L_1 selection` — canonical d-value definition |
| §6.1 几何规则性之谜 | External problem framing | Medium | No | Pure external framing — candidate for extraction |
| §6.2 实证基础 (Dehaene fMRI/MEG) | External empirical content | Medium | No | External data; BUT annotated with `→ SRT意义` that tie directly to §6.3–6.5 SRT claims |
| §6.3 SRT解释: L_0→L_1 选择分层架构 | **SRT-internal formal content** | **No** | **Yes** | `Ĝ_θ^ventral: L_0^visual → L_1^object` and `Ĝ_θ^dorsal: L_1^object → L_1^symbolic` are SRT formal operator specializations |
| §6.4 η_compress 的神经实现 | **SRT-internal canonical claim** | **No** | **Yes** | `Ψ_f(σ) ∝ 1/η_compress(σ)` is a SRT-canonical Ψ_f formula — cannot be in bridge Annex |
| §6.5 d_symbolic 阈值与符号化认知 | **SRT-internal canonical claim** | **No** | **Yes** | `d > d_symbolic ⇒ symbolic selection pathway` is SRT's own d-threshold claim; d-value table is canonical |
| §7 可证伪预测 (H-Evo-1 through H-Evo-4) | Canonical falsifiable predictions | No | **Yes** | H-Evo predictions are canonical SRT content |
| **§8.1** 经典 Waddington 景观 | External theory description | **High** | No | Pure external description of Waddington's landscape |
| **§8.2** SRT重新诠释 | SRT bridge mapping | **High** | No | SRT mapping table (valleys = L_2 attractors, ball = Ĝ_θ state) — applies SRT terms, does not define them; three SRT-unique contributions are bridge interpretation |
| §9 合成生物学的启示 | SRT-internal application | No | **Yes** | SRT-internal application conclusions |
| §10 结语 | SRT-internal conclusion | No | **Yes** | SRT-internal |
| Appendix / Formalization Summary | Canonical derivation chains and formulas | No | **Yes** | All Part A formal anchors |

---

## 4. Detailed Review of §3.2 Levin Interface

### 4.1 Extractable subsections: §3.2.1–3.2.3

These three experiments (double-headed planaria, frog eye transplant, cancer electrical reversal) follow an identical structure:
- **操作**: What was done to the organism
- **结果**: What happened
- **SRT 解释**: SRT's interpretation using bridge terms

The SRT interpretations use `θ_morpho`, `Φ_coupling`, `Ĝ`, `d-value` — these are **bridge applications** of already-defined concepts, not new definitions. They are the same type as the GWT/IIT interpretations in NEURO-06 §2.2–2.3, which were successfully extracted to Annex.

**Extraction decision**: Extractable to `Neuroscience_Annex/08_Evo_Devo_Interface.md`.

### 4.2 Must stay in owner: §3.2.4 and §3.2.5

Both are explicitly labeled as dated empirical patches:
- §3.2.4 "2026-03-16 patch": Cancer mechanical window. Uses `θ_physio`, `state-selective gating`, `L_2^{bioelectric}`, `L_1`. Contains detailed experimental boundary analysis. **Canonical empirical anchor — must stay.**
- §3.2.5 "2026-03-21 patch": Stentor associative learning. Uses `θ_physio`, `d ≥ d_UAL`, `L_2^{bioelectric}`. **Canonical empirical anchor — must stay.**

### 4.3 Must stay in owner: §3.3 and §3.4

- §3.3 认知-形态同构: "形态发生和认知是同构的" — this is SRT's own ontological thesis, not an external comparison. **Must stay.**
- §3.4 癌症是算子的去联邦化: Uses `Ĝ_θ`, `d-value`, `Ψ_f^cross`, `L_1`, `L_2` — SRT's own cancer ontology claim. **Must stay.**

### 4.4 Owner retention summary for §3.2

After extracting §3.2.1–3.2.3 to Annex, the owner should retain:
- §3.2 header with pointer to Annex for §3.2.1–3.2.3
- Clear statement that θ_morpho, Ĝ_devo, L2^bioelectric are not defined in the Levin experiments — they are defined in Part A (Ax-BIO-1/2/2b)
- Explicit retention of §3.2.4 and §3.2.5 empirical patches

### 4.5 Annex guardrail requirements for §3.2

- Levin bioelectric experiments do not define `θ_morpho` or `Ĝ_devo` — these are defined in Part A (Ax-BIO-1, Ax-BIO-2b).
- `Φ_coupling` used in §3.2 experiments is a bridge proxy for coupling strength, not a canonical SRT definition.
- The cancer d-value restoration claim (§3.2.3 SRT解释) is bridge interpretation, not a formal axiom.
- §3.2.4 and §3.2.5 empirical patches remain in the owner file as canonical anchors.

---

## 5. Detailed Review of §5 Convergent Evolution

### 5.1 Extractable subsections: §5.1 and §5.2

**§5.1** (problem framing — circuit convergence mystery) and **§5.2** (three Science 2025 studies: García-Moreno, Zaremba, Kempynck) are pure external content. No SRT formulas. The experimental findings are straightforwardly extractable.

### 5.2 Must stay in owner: §5.3–5.5

**§5.3** contains a formal SRT argument:
```
S_d = {σ ∈ L_0^anatomical : d(Ĝ_σ) > 0}
```
This is SRT's own formal construction — L_0^anatomical restricted to configurations where d > 0. The S_d set and its "topological necessity" argument are SRT-internal formal claims derived from SRT's core operator framework. They must remain in the owner file.

**§5.4** introduces `F_Bio^{avian}(θ_DVR) ≅ F_Bio^{mammalian}(θ_neocortex)` — functional isomorphism. This is SRT's own framework for substrate-independent cognition, not a description of external research.

**§5.5** states `d > 0 ⟺ effective L_0 → L_1 selection`. This is a canonical d-value statement. The species d-value table is SRT's own comparative claim. **Both must stay in owner.**

### 5.3 Boundary precision

The extraction boundary for §5 is:
- **Extract**: §5.1 (problem) + §5.2 (García-Moreno + Zaremba + Kempynck teams' findings only)
- **Keep in owner**: §5.3 (S_d attractor formal argument) + §5.4 (F_Bio equivalence) + §5.5 (d-value universality)

Owner summary after extraction should note: the external empirical data for convergent evolution is in the Annex; the SRT's own L_0-constraint interpretation (S_d, attractor convergence, F_Bio equivalence) remains in this owner file.

### 5.4 H-Evo predictions

H-Evo-1 through H-Evo-4 (located in §7) are canonical SRT falsifiable predictions. They **must not be extracted** regardless of which other sections move.

### 5.5 Ax-EVO-1/2/3 safety

Ax-EVO-1 (Unreliable Hardware), Ax-EVO-2 (d-Expansion), Ax-EVO-3 (Convergent Intelligence) are in Part A and are entirely unaffected by Part B extraction. The §5.3.2 connection to Ax-EVO-1 (`Reliability ∝ Redundancy(L_2)`) is in the owner S_d section (§5.3.2) which stays in owner — so the Ax-EVO-1 linkage is preserved.

---

## 6. Detailed Review of §6 Geometric Regularity / Dehaene

### 6.1 Confirmed: §6 has no GRT content

NEURO-07 §6 contains zero GRT / Hunt & Schooler / 广义共振理论 content. This was confirmed in the GRT deduplication adjudication. The "§6 GRT" navigation label is an error.

### 6.2 External vs. SRT-internal boundary within §6

| Subsection | Content type | Extractability |
|---|---|---|
| §6.1 (geometric regularity framing) | External cognitive anthropology problem statement | Extractable |
| §6.2 (Dehaene fMRI/MEG dual-pathway evidence) | External empirical data — BUT has embedded `→ SRT意义` annotations tying to §6.3–6.5 | Conditionally extractable — requires annotation handling |
| §6.3 (SRT selection architecture: ventral/dorsal `Ĝ_θ^{ventral/dorsal}`) | **SRT-internal** — formalizes `Ĝ_θ` as operator specializations | **Cannot extract** |
| §6.4 (`η_compress = I(L_1;L_0)/H(L_1)`, `Ψ_f ∝ 1/η_compress`) | **SRT-internal canonical** — introduces Ψ_f formula | **Cannot extract** |
| §6.5 (`d > d_symbolic`, d-value species table) | **SRT-internal canonical** — d-value threshold claim | **Cannot extract** |

### 6.3 Why §6 requires separate adjudication

The problem is not just that §6.3–6.5 are SRT-internal. The deeper issue is that §6.2 is not cleanly separable from §6.3–6.5:
- §6.2 lists five findings, each tagged with `→ SRT意义` that explicitly point to §6.4 (`η_compress`) and §6.5 (d_symbolic) claims
- If §6.2 is extracted without §6.3–6.5, the reader loses all SRT context for the `→ SRT意义` annotations
- The annotations would either need to be stripped (losing SRT interpretation) or replaced with Annex pointers (which requires defining what exactly the Annex says about §6.4 and §6.5)

This is a more complex extraction boundary than NEURO-06 §2 or §6.1–6.2, where the external content and SRT interpretation were in separate subsections. Here, the SRT interpretation is embedded in the external empirical section via annotation.

**Decision**: Exclude §6 entirely from Batch 2b. It needs a dedicated §6-specific adjudication (PR-D0.6 or similar) that decides: (1) whether §6.4's Ψ_f formula is extractable or owner-level canonical content; (2) how to handle the `→ SRT意义` annotations in §6.2; (3) whether §6.3's operator specializations belong in owner or Annex.

### 6.4 §6 is NOT a Batch 2b candidate

Recommendation: Exclude §6 from Batch 2b execution. Create a separate adjudication record for §6 before any extraction attempt.

---

## 7. Detailed Review of §8 Waddington Reinterpretation

### 7.1 Content analysis

**§8.1** (Classical Waddington landscape): ~6 lines describing valleys (chreods), ridges, rolling ball. Pure external theory framing. Entirely extractable.

**§8.2** (SRT reinterpretation): Contains a 4-row correspondence table mapping Waddington landscape features to SRT terms:
- Valley → L_2 attractor
- Ridge → L_0 barrier
- Rolling ball → Ĝ_θ current selection state
- Landscape → L_0^anatomical

Plus three "SRT unique contributions": dynamic landscape, active navigation by Ĝ^collective, valley arrival = L_1→L_2 solidification.

### 7.2 Extraction assessment

The §8.2 content **applies** SRT formal terms (Ĝ_θ, L_0, L_1, L_2, L_0^anatomical) to the Waddington metaphor — it does not **define** them. This is the same pattern as NEURO-06 §6.2 (SRT-GRT convergence table), which was successfully extracted. The SRT terms used here are defined in Part A and Core_Law.

**Extraction decision**: Extractable in full (§8.1 + §8.2) to `Neuroscience_Annex/08_Evo_Devo_Interface.md`.

### 7.3 Owner retention summary for §8

After extracting §8, owner should retain:
- A pointer noting that Waddington landscape interface is in Annex
- Explicit guardrail: Waddington landscape does not define Ĝ_devo, L2^bioelectric, or Generativity_devo — those are defined in Part A (Ax-BIO-2, Ax-BIO-1, Ax-BIO-3)

### 7.4 Annex guardrails for §8

Required guardrails when §8 is in Annex:
- Waddington landscape is an external metaphor interface; it does not define `Ĝ_devo`.
- `L_2^{bioelectric}` is defined in Part A (Ax-BIO-1), not by the Waddington reinterpretation.
- Waddington's valley ≠ `L_2 attractor` as canonical identity — it is an analogical mapping.
- The "active navigation" claim (Ĝ^collective) is a bridge interpretation; `Ĝ^collective` is formally defined in the owner file appendix Mechanism Explanation.

---

## 8. Owner Retention Rules

The following must remain in NEURO-07 regardless of any extraction:

| Item | Reason |
|---|---|
| **Part A: Ax-BIO-1, Ax-BIO-2, Ax-BIO-2b, Ax-BIO-3** | Core bioelectric / developmental axioms |
| **Part A: Ax-EVO-1, Ax-EVO-2, Ax-EVO-3** | Core evolution axioms |
| **Part A: Ax-PATH-1, Ax-PATH-2** | Pathology axioms |
| **Evo-Devo Bridge Note** (P3/P4 self-labeled) | Self-labeled guardrail — stays in owner by design |
| **T-EVO-1, T-EVO-2, C-EVO-1, C-EVO-2** | Theorems and corollaries |
| `Ĝ_devo`, `L2^bioelectric`, Genome-as-Generative-Model | Formal operator and layer definitions |
| `Generativity_devo ∝ 1/Ψ_f(θ_morpho)` | Formal axiom (Ax-BIO-3) |
| **H-Evo-1 through H-Evo-4** | Canonical falsifiable predictions |
| **§3.2.4 cancer mechanical window patch (2026-03-16)** | Dated empirical anchor |
| **§3.2.5 Stentor learning patch (2026-03-21)** | Dated empirical anchor |
| **§3.3 认知-形态同构** | SRT-internal ontological thesis |
| **§3.4 癌症是算子的去联邦化** | SRT-internal cancer ontology |
| **§5.3 S_d 吸引子拓扑** | Contains `S_d = {σ ∈ L_0^anatomical : d(Ĝ_σ) > 0}` |
| **§5.4 F_Bio 多态等价性** | SRT-internal substrate-independence framework |
| **§5.5 d 值通用性** | `d > 0 ⟺ effective L_0 → L_1 selection` — canonical d-value claim |
| **§6.3 SRT selection architecture** | `Ĝ_θ^{ventral/dorsal}` operator specializations |
| **§6.4 η_compress** | `Ψ_f ∝ 1/η_compress` — canonical Ψ_f formula |
| **§6.5 d_symbolic threshold** | `d > d_symbolic ⇒ symbolic selection` — canonical d-value threshold |
| **§7 H-Evo predictions** | Already listed above |
| **§9 synthetic biology** | SRT-internal application conclusions |
| **§10 conclusion** | SRT-internal |
| **Appendix** | All derivation chains and formal summaries |
| **Science 2025 Empirical Anchor block** (Part A) | Canonical empirical anchors for Ax-EVO-3/T-EVO-2 |

---

## 9. Navigation Label Correction Plan

### 9.1 The error

NEURO-07's navigation block (added in PR-B) Refactor Notes state:

> "§3.2 Levin interface, §5 convergent evolution, **§6 GRT**, and §8 Waddington are possible future Annex candidates."

"§6 GRT" is wrong. §6 is "几何规则性与选择的符号化压缩" (geometric regularity / symbolic compression) — Dehaene/Sablé-Meyer work. No GRT content exists in NEURO-07.

### 9.2 Corrected label

Replace:
```
- §3.2 Levin interface, §5 convergent evolution, §6 GRT, and §8 Waddington are possible future Annex candidates.
```

With:
```
- §3.2.1–3.2.3 Levin experiments (bridge interface), §5.1–5.2 convergent evolution empirical basis, and §8 Waddington reinterpretation are Annex candidates for PR-D Batch 2b.
- §6 (geometric regularity / Dehaene / symbolic compression) is NOT a GRT section. §6.1–6.2 are external empirical; §6.3–6.5 contain SRT-internal d_symbolic and η_compress / Ψ_f claims. Requires separate adjudication before extraction.
- §3.2.4, §3.2.5 (empirical patches), §3.3, §3.4, §5.3–5.5, §9, §10 must stay in owner.
```

### 9.3 How to execute this correction

The Refactor Notes label correction should be included in the **Batch 2b execution PR** — it is a navigation block text correction, not a theory change. It can be done in the same commit as the extraction, clearly labeled as a navigation label fix.

The correction is minimal: it replaces 4 words ("§6 GRT" → corrected multi-line description) in the Refactor Notes section at the top of the file, without touching any Part A axioms or theory content.

---

## 10. Proposed PR-D Batch 2b Plan

### 10.1 Annex file to create

`Neuroscience_Annex/08_Evo_Devo_Interface.md`

**Frontmatter**: `canonical: false`, `claim_mode: bridge`, `layer: bridge`, `epistemic_layer: bridge`, `owner: Neuroscience/SRT_Neuro_07_Evo_Devo.md`

**Content to include**:
1. §3.2.1 双头涡虫实验 (with Annex note: θ_morpho not defined here; defined in Ax-BIO-2b)
2. §3.2.2 青蛙眼睛移位实验 (with Annex note: bioelectric map = bridge proxy; not a formal definition)
3. §3.2.3 癌症电学逆转实验 (with Annex note: Φ_coupling and d-value are bridge applications, not definitions; §3.2.4 empirical patch stays in owner)
4. §5.1 回路趋同之谜 (problem framing)
5. §5.2 实证基础 (Science 2025 three papers: García-Moreno, Zaremba, Kempynck; with Annex note: S_d formal argument and F_Bio framework stay in owner §5.3–5.5)
6. §8.1 经典Waddington景观
7. §8.2 SRT重新诠释 (with Annex note: Waddington landscape does not define Ĝ_devo or L2^bioelectric; those are defined in Part A)

**Guardrail block** (mandatory at file top):
- θ_morpho, Ĝ_devo, L2^bioelectric are defined in Part A (Ax-BIO-2b, Ax-BIO-2, Ax-BIO-1) — not in this Annex
- Levin bioelectric experiments do not redefine Generativity_devo or Ψ_f(θ_morpho)
- Waddington landscape does not define Ĝ_devo or L_2 attractor topology
- S_d attractor formal argument (`d(Ĝ_σ) > 0`), F_Bio equivalence, and d-value universality claims remain in the owner file
- §6 geometric regularity / Dehaene content is not included in this Annex; see separate §6 adjudication record

### 10.2 Owner file modifications

Sections to replace with owner summaries + Annex pointers:
- §3.2: Replace §3.2.1–3.2.3 body with pointer to Annex; keep §3.2.4 and §3.2.5 in full; keep §3.2 header "Levin 实验的本体论意义"
- §5: Replace §5.1–5.2 body with pointer to Annex; keep §5.3–5.5 in full; keep §5 header
- §8: Replace §8.1 + §8.2 body with pointer to Annex; keep §8 header

### 10.3 Navigation label correction

In NEURO-07 Refactor Notes section: correct "§6 GRT" label as described in §9.2.

### 10.4 Batch split consideration

No split into 2b-1/2b-2 is needed. The three extractable content clusters (Levin, convergent evolution partial, Waddington) share the same destination Annex file and do not have circular dependencies. They can be handled in a single PR-D Batch 2b.

---

## 11. Final Recommendation

**Recommendation: Option A** — Extract §3.2.1–3.2.3 + §5.1–5.2 + §8 in Batch 2b; exclude §6; fix navigation label.

**Rationale**:

1. **§3.2.1–3.2.3, §5.1–5.2, §8 are clean extraction candidates.** Their content is external experiment descriptions or Waddington metaphor interface — the same type as NEURO-06 §2.1–2.3 and §6.1–6.2, which were successfully extracted in Batch 2a. The SRT interpretations in §3.2.1–3.2.3 are bridge applications, not definitions.

2. **§6 must be excluded.** The `Ψ_f ∝ 1/η_compress` formula in §6.4 and the `d > d_symbolic` threshold in §6.5 are canonical SRT claims that cannot reside in a `canonical: false` bridge Annex. The tight coupling between §6.2's `→ SRT意义` annotations and §6.3–6.5's SRT-internal content makes clean extraction impossible without first resolving how to handle the annotations. A separate adjudication (PR-D0.6 or similar) is required.

3. **Navigation label correction is low-cost and should be bundled into Batch 2b.** It corrects a documentation error (not a theory error) and prevents the "§6 GRT" misconception from propagating into future planning.

4. **Option B** (only §3.2 + §8, defer §5) is unnecessarily cautious — §5.1–5.2 are pure external empirical content with no SRT formulas, lower-risk than §3.2's bridge interpretations.

5. **Option C** (pause for navigation label only) wastes a PR on a trivial correction when the substantive extraction is ready.

6. **Option D** (§6 adjudication first) delays §3.2/§5/§8 extraction unnecessarily. The §6 adjudication can proceed in parallel or immediately after Batch 2b.

---

## 12. Safety Record

- [ ] No Neuroscience files modified.
- [ ] No formulas changed.
- [ ] No theory content changed.
- [ ] No Annex files created.
- [ ] No content moved.
- [ ] BIO-1 through EVO-3 unchanged.
- [ ] Evo-Devo Bridge Note unchanged.
- [ ] `Ĝ_devo` unchanged.
- [ ] `L2^bioelectric` unchanged.
- [ ] Genome-as-Generative-Model unchanged.
- [ ] H-Evo predictions unchanged.
- [ ] §6.4 `Ψ_f ∝ 1/η_compress` unchanged.
- [ ] §6.5 `d_symbolic` unchanged.
- [ ] Core/, Core_Law/, AI/, Philosophy/, Public/, Papers/ not touched.
- [ ] Only new file: `Operations/PR_D_Batch2b_Neuro_07_PreExtraction_Audit.md` (this file).
