---
id: SRT-OPS-PR-D0-6-NEURO07-GEOM-ADJUDICATION-2026-04-29
type: adjudication_record
tags:
  - Operations
  - Adjudication
  - Neuroscience
  - PR-D
  - GeometricRegularity
  - Dehaene
  - SymbolicCompression
  - eta_compress
  - d_symbolic
status: adjudication_complete
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
reference_extraction: Operations/PR_D_Batch2b_Neuro_07_Evo_Devo_Extraction_Record.md
pr: PR-D0.6 — Adjudicate Neuro 07 geometric regularity boundary
machine_summary: >
  Read-only boundary adjudication for NEURO-07 §6 "几何规则性与选择的符号化压缩"
  before any Batch 2c extraction. Finds §6.1 (problem framing) cleanly
  extractable. §6.2 (Dehaene fMRI/MEG empirical) conditionally extractable
  — blocked by inline `→ SRT意义` annotations that point to §6.4 (Ψ_f ∝
  1/η_compress) and §6.5 (d_symbolic); annotation conversion required first.
  §6.3–6.5 must remain in owner (SRT formal operator specializations and
  canonical Ψ_f / d_symbolic definitions). Recommends Option B (new
  Neuroscience_Annex/09 file for §6.1–6.2) with a two-step Batch 2c execution:
  annotation conversion pass first, then extraction.
---

# PR-D0.6: Neuro 07 Geometric Regularity Boundary Adjudication

**Date**: 2026-04-29
**Adjudicator**: Claude (claude-sonnet-4-6), read-only pass
**File audited**: `Neuroscience/SRT_Neuro_07_Evo_Devo.md` §6 only (lines 497–605)
**Triggered by**: `Operations/PR_D_Batch2b_Neuro_07_Evo_Devo_Extraction_Record.md` §10 (recommended next step)

> **This PR did not**: modify `SRT_Neuro_07_Evo_Devo.md`, create any Annex file, move any section, change any formula, change any canonical definition.

---

## 0. Executive Summary

**§6 can be partially extracted — but §6.2's inline SRT annotations are a hard prerequisite blocker.**

| Question | Answer |
|---|---|
| Can §6.1 (problem framing) be extracted? | **Yes** — pure external cognitive anthropology framing; no SRT formulas; same type as §5.1 which was extracted in Batch 2b |
| Can §6.2 (Dehaene fMRI/MEG empirical) be extracted? | **Conditionally** — the five findings in §6.2.2 carry inline `→ SRT意义` annotations that point directly to §6.4 (`η_compress`, `Ψ_f`) and §6.5 (`d_symbolic`); these must be converted to Annex-compatible cross-reference notes before extraction is safe |
| Can §6.3 (SRT layered selection architecture) be extracted? | **No** — `Ĝ_θ^{ventral}` and `Ĝ_θ^{dorsal}` are SRT formal operator specializations; must stay in owner |
| Can §6.4 (`η_compress` / `Ψ_f`) be extracted? | **No** — `Ψ_f(σ) ∝ 1/η_compress(σ)` is a canonical Ψ_f formula; `η_compress = I(L_1;L_0)/H(L_1)` is a formal definition; both must stay in owner |
| Can §6.5 (`d_symbolic` threshold) be extracted? | **No** — `d > d_symbolic ⇒ symbolic selection pathway` is a canonical d-value threshold claim; d-value species table is SRT-internal; must stay in owner |
| How to handle `→ SRT意义` annotations in §6.2? | Convert to explicit owner cross-references ("→ Owner §6.3–6.5") in a prep pass before extraction; do not strip them without replacement |
| Separate Annex or append to existing 08? | **New file** `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` — §6 content is symbolic compression / cognitive neuroscience, not Evo-Devo; conceptual mismatch with 08 |
| Recommended strategy | **Option B** — new §09 Annex for §6.1–6.2, two-step Batch 2c execution |

**Critical blocker**: The `→ SRT意义` annotations in §6.2.2 create tight coupling between empirical findings and §6.4–6.5 SRT-internal formulas. If §6.2 is extracted without converting these annotations, readers of the Annex will encounter dangling references to undefined formulas. If the annotations are stripped without replacement, SRT interpretive context is lost. The conversion step (replacing inline formula references with owner cross-reference pointers) is mandatory before extraction.

---

## 1. Scope and Safety Record

- **Only new file**: `Operations/PR_D0_6_Neuro_07_Geometric_Regularity_Adjudication.md` (this file)
- `Neuroscience/SRT_Neuro_07_Evo_Devo.md` — read, **not modified**
- No Annex files created
- No content moved
- No formulas changed
- No canonical definitions changed
- `Ψ_f ∝ 1/η_compress` — untouched, remains in owner §6.4
- `d > d_symbolic` — untouched, remains in owner §6.5
- `Ĝ_θ^{ventral/dorsal}` — untouched, remains in owner §6.3

---

## 2. Subsection Boundary Table

| Subsection | Content Type | Extraction Readiness | Must Stay in Owner? | Reason |
|---|---|---|---|---|
| §6.1 几何规则性之谜 | Pure external empirical (cognitive anthropology) | **High** | No | Pure external problem framing (Himba, cross-cultural data, baboon vs. human comparison); no SRT formulas; structurally parallel to §5.1 which was extracted in Batch 2b |
| §6.2.1 双重编码系统 (table) | External empirical data | **High** | No | Dual-pathway table (ventral CNN-explainable, dorsal human-unique) is external neuroscience; no SRT formulas; safe to extract |
| §6.2.2 关键发现 (5 findings) | Hybrid — external empirical + inline SRT annotation | **Medium** (conditional) | No — conditional on annotation conversion | Empirical findings [R] are external; `→ SRT意义` annotations link directly to §6.4 (`η_compress`, `Ψ_f`) and §6.5 (`d_symbolic`); must convert annotations to Annex-compatible cross-references before extraction |
| §6.2 证伪方向 | Hybrid — empirical challenge directions referencing SRT framework | **Medium** (conditional) | Borderline | References "CNN失败 → 本体论跃迁" (§6.3 SRT claim) and "先天性" (§6.5 related); extractable if accompanied by Annex note pointing to owner §6.3–6.5 for SRT context |
| §6.3 SRT解释：分层架构 | **SRT-internal formal content** | No | **Yes** | `Ĝ_θ^{ventral}: L_0^visual → L_1^object` and `Ĝ_θ^{dorsal}: L_1^object → L_1^symbolic` are formal SRT operator specializations; FC-Ventral-1/2 falsification conditions are SRT-internal; cannot reside in `canonical: false` Annex |
| §6.4 η_compress 神经实现 | **SRT-internal canonical formula** | No | **Yes** | `η_compress = I(L_1;L_0)/H(L_1)` is a formal definition; `Ψ_f(σ) ∝ 1/η_compress(σ)` is a canonical Ψ_f claim; `Geometric Regularity ∝ η_compress ∝ 1/MDL` is SRT's empirical operationalization of Ψ_f; cannot be in bridge Annex |
| §6.5 d_symbolic 阈值与符号化认知 | **SRT-internal canonical claim** | No | **Yes** | `d > d_symbolic ⇒ symbolic selection pathway` is SRT's own d-threshold definition; d-value species table is SRT-internal comparative framework; the `d_symbolic` threshold is a named SRT-specific d-value boundary |

---

## 3. Detailed Review of §6.1

**Content**: External cognitive anthropology problem framing (~15 lines). Describes the "geometric regularity mystery": human prehistorical geometry use (Lascaux-era symbols, cross-cultural parallels), Himba tribe data, baboon/chimp negative controls, and the core puzzle — why humans perceive geometric regularity without formal education.

**Assessment**: This is pure external content with no SRT formulas, no SRT operator references, no θ parameters. It is structurally identical to §5.1 (circuit convergence mystery) which was extracted in Batch 2b. The parallel is exact: both sections pose an external empirical puzzle whose SRT-internal answer is in later subsections (§6.3–6.5 for §6.1; §5.3–5.5 for §5.1).

**Extraction decision**: **Extractable** in full to a future Annex.

**Owner retention after extraction**: A pointer block noting that the geometric regularity problem framing is in Annex; the SRT answer (layered selection architecture, η_compress, d_symbolic threshold) is in §6.3–6.5 below.

---

## 4. Detailed Review of §6.2

### 4.1 §6.2.1 Dual encoding table

Pure external neuroscience data: a two-row table showing ventral pathway (early, occipitotemporal, CNN-explainable, shared with non-human primates) vs. dorsal-prefrontal pathway (late, IPS+ITG+prefrontal, only explainable by symbolic geometric models, human-unique). No SRT formulas. The column "计算模型 — 仅符号化几何特征模型可解释" is an empirical finding from Dehaene's experiments, not an SRT claim.

**Assessment**: Cleanly extractable. No SRT formula dependencies.

### 4.2 §6.2.2 Five key findings — the annotation problem

Each finding is tagged `[R]` (Reference = external data) with embedded `→ SRT意义` or `→ Cross-ref` annotations:

| Finding | Empirical content [R] | `→ SRT意义` target |
|---|---|---|
| 1. 规则性效应 | Higher regularity → stronger IPS/ITG/prefrontal modulation | `§6.4: η_compress ∝ 1/MDL; 低 Ψ_f` |
| 2. 压缩编码 | Brain activity ∝ MDL | `§6.4: η_compress 神经实现; MDL 作为 Ψ_f 的操作化代理` |
| 3. CNN 失败 | CNN can't explain late dorsal-prefrontal signal | `§6.3: 本体论跃迁; 离散符号化 L_0 → L_1 选择` |
| 4. 发育先天性 | 6yo children show same IPS/ITG activation | No `→ SRT意义`; contains confound note |
| 5. 人类皮层扩展 | Human parietal cortex has largest expansion | `§6.5: d_symbolic 阈值; 顶叶扩展 = d_symbolic 所需具身硬件` |

**The annotation problem**: Four of five findings have inline `→ SRT意义` or `→ Cross-ref` annotations that explicitly name §6.4 formulas (`η_compress`, `Ψ_f`) and §6.5 claims (`d_symbolic`). If §6.2 is extracted to Annex as-is, the Annex would contain inline references to owner-file canonical formulas — creating a situation where an Annex file actively points to owner formulas as if defining them, blurring the bridge/canonical boundary.

**What the annotations are NOT**: They are not independent definitions of `η_compress` or `d_symbolic`. They are pointers saying "this empirical finding supports the SRT formula in §6.4/6.5." The formulas themselves remain in §6.4–6.5.

**Resolution path**: The `→ SRT意义` annotations should be converted to explicit cross-references before extraction:
- Replace: `→ SRT意义：支持 §6.4 的 η_compress ∝ 1/MDL`
- With: `→ Annex note: SRT interpretation is in owner file §6.4 (η_compress, Ψ_f) and §6.5 (d_symbolic). See owner file [`../Neuroscience/SRT_Neuro_07_Evo_Devo.md`]`

This conversion preserves the connection between empirical data and SRT theory without the Annex containing inline formula references. The conversion is a minimal text change, not a theory change.

### 4.3 §6.2 证伪方向

The falsification conditions reference SRT-level claims: "CNN失败 → 本体论跃迁必需" is an inference supported by §6.3; "先天性" relates to §6.5's hardware threshold. These can be extracted alongside §6.2 with an Annex note redirecting to owner §6.3 and §6.5 for the SRT-framework context.

### 4.4 Extraction decision for §6.2

**Conditionally extractable** — requires annotation conversion as a prerequisite. The conversion can be done in the same Batch 2c PR (not a separate prep PR), provided it is treated as a "Annex-safety annotation conversion" step within the extraction workflow, not a theory change.

**Risk if extracted without conversion**: Annex file contains inline formula references (`η_compress`, `Ψ_f`, `d_symbolic`) without definitions — creates reader confusion and undermines the bridge/canonical boundary. **Do not extract §6.2 without this conversion.**

---

## 5. Detailed Review of §6.3

**Content**: SRT's formal reinterpretation of the dual-pathway finding as a layered selection architecture.

**Key formal elements**:
- `Ĝ_θ^{ventral}: L_0^{visual} → L_1^{object}` — formal SRT operator specialization (ventral stream as continuous compression selection)
- `Ĝ_θ^{dorsal}: L_1^{object} → L_1^{symbolic}` — formal SRT operator specialization (dorsal stream as symbolic rule extraction)
- CNN comparison: CNN is a forward model for ventral, but fails for dorsal — SRT explanation is "ontological transition from continuous manifold to discrete symbol space"
- FC-Ventral-1/2 falsification conditions: These are SRT-specific predictions about θ parameterization
- Commentary on θ's developmental parameterization

**Assessment**: These are formal SRT operator specializations. `Ĝ_θ^{ventral}` and `Ĝ_θ^{dorsal}` are not external neuroscience findings — they are SRT's own framework applied to neuroanatomy. Specifically, `Ĝ_θ^{dorsal}: L_1^{object} → L_1^{symbolic}` is SRT's claim that symbolic cognition is a second-order selection operation, not just a feature extension. This is an owner-level theoretical claim.

Furthermore, the ontology claim — "背侧通路 = 本体论跃迁 from continuous manifold to discrete symbol space" — is central to §6.5's `d > d_symbolic` threshold claim. Extracting §6.3 to Annex would sever this connection.

**Extraction decision**: **Cannot extract.** Must remain in owner as SRT-internal formal content.

---

## 6. Detailed Review of §6.4

**Content**: Defines `η_compress` and derives the canonical Ψ_f relationship.

**Key formal elements**:
- `η_compress = I(L_1;L_0)/H(L_1)` — formal definition of compression efficiency (cognitive compression bandwidth)
- `Geometric Regularity ∝ η_compress ∝ 1/MDL(shape)` — empirical operationalization of η_compress via Dehaene data
- `Ψ_f(σ) ∝ 1/η_compress(σ)` — canonical Ψ_f formula connecting phenomenological friction to compression efficiency

**Assessment**: This section introduces `η_compress` as an SRT-defined quantity and derives `Ψ_f ∝ 1/η_compress`. This is SRT's own theoretical claim, not a description of Dehaene's findings. Dehaene found that brain activity correlates with MDL — SRT interprets this as evidence that `η_compress` (SRT's compression efficiency) provides a neural implementation proxy for `Ψ_f` (SRT's ontological friction). The formula `Ψ_f ∝ 1/η_compress` is a canonical-level SRT claim that would be circular or undefined in a `canonical: false` Annex.

**Specifically**: A `canonical: false` Annex file that contains `Ψ_f(σ) ∝ 1/η_compress(σ)` would create a situation where a canonical formula is housed in a bridge file — exactly the violation that the Annex extraction protocol is designed to prevent.

**Extraction decision**: **Cannot extract.** `η_compress` definition and `Ψ_f ∝ 1/η_compress` formula must remain in owner.

---

## 7. Detailed Review of §6.5

**Content**: SRT's d-value threshold claim for symbolic cognition.

**Key formal elements**:
- `d > d_symbolic ⇒ symbolic selection pathway emerges` — canonical d-value threshold
- Three hardware conditions for `d_symbolic`: θ_neural capacity (parietal expansion), Γ_Ĝ refresh rate, η_compress recursion
- d-value species table (reflexive d≈0 / continuous compression 0 < d < d_symbolic / symbolic d > d_symbolic)
- Phase transition analogy: `Ĝ` "crystallizes" a symbolic layer when d > d_symbolic
- Connection to Ax-EVO-2 (major evolutionary transitions as d-expansions)

**Assessment**: `d_symbolic` is a named threshold specific to SRT's d-value framework. The claim `d > d_symbolic ⇒ symbolic selection pathway` is SRT's own theoretical prediction about what happens at a critical d-value. The d-value species table is SRT's comparative framework, not an empirical finding from Dehaene's experiments. The connection to Ax-EVO-2 makes this an owner-level canonical claim.

Importantly: the three hardware conditions in §6.5 reference `η_compress` (from §6.4), creating a within-§6 dependency. §6.5 cannot be extracted independently of §6.4, and §6.4 cannot be extracted (as established above). Therefore §6.5 also cannot be extracted.

**Extraction decision**: **Cannot extract.** `d_symbolic` threshold and d-value species table must remain in owner.

---

## 8. Annex Strategy Options

### Option A — No extraction

Complete §6 stays in owner. Only add an exclusion note to `Neuroscience_Annex/08_Evo_Devo_Interface.md` and `Neuroscience_Annex/README.md` confirming §6 is owner-retained.

**Pros**:
- Zero risk. No annotation conversion needed. No new files.
- §6.3–6.5 SRT-internal formulas remain safely in owner with full context.
- No chance of accidental formula boundary violation.

**Cons**:
- Bridge content (§6.1 external framing, §6.2 Dehaene empirical) remains mixed with canonical content (§6.3–6.5 SRT-internal) in owner file — the same problem this PR-D series is designed to solve.
- Future extraction becomes harder as no conversion plan is established.

### Option B — Partial extraction to new Neuroscience_Annex/09

Create `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` for §6.1 + §6.2 (with annotation conversion). Keep §6.3–6.5 in owner.

**Pros**:
- Consistent with Batch 2a/2b extraction pattern (§6.1 parallel to §5.1; §6.2 parallel to §5.2)
- Clearly named, topic-specific Annex file — geometric regularity content is distinct from Evo-Devo content of 08
- Maintains separation of external empirical interface from SRT-internal formal claims
- Annotation conversion is well-defined and manageable (four annotations to convert in §6.2.2)

**Cons**:
- Requires annotation conversion pass as prerequisite — adds one step to Batch 2c
- Small risk of conversion errors if annotations are rephrased incorrectly
- Creates a third Annex file for NEURO-07 content (08 and 09 both sourced from NEURO-07)

**Risk mitigation**: Annotation conversion is mechanical — replace `→ SRT意义：[formula/claim]` with `→ Annex note: SRT interpretation in owner §6.3–6.5`. No formulas change; no theory changes; only the pointer target changes from inline-claim to owner-section-reference.

### Option C — Partial extraction into existing 08_Evo_Devo_Interface.md

Append §6.1–6.2 to existing `Neuroscience_Annex/08_Evo_Devo_Interface.md`. Same annotation conversion requirement.

**Pros**:
- No new file needed; keeps NEURO-07 Annex content in one file.

**Cons**:
- **Conceptual mismatch**: `08_Evo_Devo_Interface.md` is scoped to Evo-Devo content (Levin bioelectric experiments, convergent evolution, Waddington landscape). §6 is about geometric regularity / symbolic compression / fMRI — a distinct cognitive neuroscience topic. Merging them would make the 08 Annex thematically incoherent.
- Same annotation conversion requirement as Option B.
- Future §6 updates would require modifying a file whose thematic identity is Evo-Devo.

**Verdict**: Not recommended. The conceptual mismatch outweighs the file-count convenience.

### Option D — Owner-only with navigation cleanup

No extraction now. Update NEURO-07's navigation block to explicitly mark §6.1–6.2 as "external empirical, pending annotation conversion before extraction" and §6.3–6.5 as "owner-retained SRT-internal." No Annex changes.

**Pros**:
- Defers complexity. No annotation conversion risk. Keeps §6 intact.
- Explicit in the navigation block about WHY extraction is pending.

**Cons**:
- Bridge content remains in owner file indefinitely unless Batch 2c is explicitly planned.
- Annotation conversion plan gets deferred — may not happen if Batch 2c is deprioritized.

---

## 9. Required Guardrails if Future Extraction Happens

If §6.1–6.2 are extracted to `Neuroscience_Annex/09_Geometric_Regularity_Interface.md`, the Annex **must** include:

**Top-level guardrail block**:
- Geometric regularity / Dehaene empirical content is external interface material.
- It does not define `η_compress`. `η_compress = I(L_1;L_0)/H(L_1)` is defined in the owner file (§6.4).
- It does not define `Ψ_f`. `Ψ_f(σ) ∝ 1/η_compress(σ)` is a canonical Ψ_f formula in the owner file (§6.4).
- It does not define `d_symbolic`. `d > d_symbolic ⇒ symbolic selection pathway` is a canonical d-threshold in the owner file (§6.5).
- It does not define `Ĝ_θ^{ventral}` or `Ĝ_θ^{dorsal}`. These are SRT formal operator specializations in the owner file (§6.3).
- `→ SRT意义` annotations from §6.2.2 have been converted to owner cross-references; SRT interpretations are in owner §6.3–6.5.
- §6.3 (layered selection architecture), §6.4 (η_compress / Ψ_f), §6.5 (d_symbolic threshold) remain owner formal anchors and are not part of this Annex.

**Per-section Annex notes** (required in §6.2.2 after annotation conversion):
- After finding 1 (规则性效应): "Annex note: SRT interpretation (η_compress ∝ 1/MDL, low Ψ_f for regular shapes) is in owner §6.4. This finding supports but does not define η_compress."
- After finding 2 (压缩编码): "Annex note: MDL as Ψ_f operational proxy is developed in owner §6.4. Brain activity ∝ MDL is the external empirical finding."
- After finding 3 (CNN失败): "Annex note: SRT's 'ontological transition' interpretation of CNN failure is in owner §6.3. The empirical finding (CNN cannot explain late dorsal-prefrontal signal) is the extracted content."
- After finding 5 (人类皮层扩展): "Annex note: d_symbolic threshold interpretation (parietal expansion = embodied hardware for d_symbolic) is in owner §6.5. The empirical finding (human parietal cortex has largest cross-species expansion) is the extracted content."

---

## 10. Proposed PR-D Batch 2c Plan

**Recommended approach**: **Option B — two-step execution**

### Batch 2c-1: Annotation conversion (prep pass)

**Scope**: Modify `Neuroscience/SRT_Neuro_07_Evo_Devo.md` §6.2.2 only — convert four `→ SRT意义` annotations to explicit owner-section cross-references.

**Exact changes** (all within §6.2.2, replacing inline formula references with owner-section pointers):

| Current annotation | Converted annotation |
|---|---|
| `→ SRT意义：支持 §6.4 的 $\eta_{compress} \propto 1/\text{MDL}$（规则形状 L₁ 编码代价低 = 低 $\Psi_f$）` | `→ SRT interpretation: see owner §6.4 (η_compress, Ψ_f relationship). This finding supports §6.4's claim but does not define η_compress.` |
| `→ Cross-ref: §6.4 $\eta_{compress}$ 神经实现；MDL 作为 $\Psi_f$ 的操作化代理之一` | `→ SRT interpretation: see owner §6.4 (η_compress as neural implementation, MDL as Ψ_f operational proxy).` |
| `→ **[H含义]**：CNN 失败本身为 SRT §6.3 的预测提供支持证据——背侧通路执行的是"离散符号化 $L_0 \to L_1$"选择，超出连续函数逼近的范围，与 SRT 的"本体论跃迁"框架一致` | `→ SRT interpretation: see owner §6.3 (Ĝ_θ^{dorsal} as ontological transition; discrete symbolic L_0→L_1 selection). CNN failure is the empirical finding; the SRT framework claim is in §6.3.` |
| `→ SRT意义：支持 §6.5 的 d 值阈值假设——顶叶扩展 = $d_{symbolic}$ 阈值所需的额外具身硬件（扩展皮层 = 更大 θ 参数空间）` | `→ SRT interpretation: see owner §6.5 (d_symbolic threshold, parietal expansion as embodied hardware condition). This finding supports §6.5 but does not define d_symbolic.` |

**What does NOT change in Batch 2c-1**:
- No formulas change
- §6.3–6.5 content untouched
- No sections moved
- No Annex files created

**Safety rationale**: This is a documentation-layer change — converting inline formula citations to explicit section cross-references. The underlying claims are identical; only the pointer format changes. After conversion, §6.2 no longer contains inline references to owner-file canonical formulas, making it safely extractable.

### Batch 2c-2: Extraction

**Scope**: After Batch 2c-1 is merged, extract §6.1 + §6.2 (with converted annotations) to `Neuroscience_Annex/09_Geometric_Regularity_Interface.md`.

**Files to create**:
- `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` — with full guardrail block per §9 above

**Files to modify**:
- `Neuroscience/SRT_Neuro_07_Evo_Devo.md` — replace §6.1 + §6.2 body with owner summary + Annex pointer; §6.3–6.5 unchanged
- `Neuroscience_Annex/README.md` — add 09 entry + NEURO-07 owner link (already listed)
- NEURO-07 Refactor Notes — update to note Batch 2c extraction

**Must stay in owner after Batch 2c-2**:
- §6.3 (Ĝ_θ^{ventral/dorsal} operator specializations, FC-Ventral falsification conditions)
- §6.4 (η_compress definition, Ψ_f ∝ 1/η_compress formula)
- §6.5 (d_symbolic threshold, d-value species table, Ax-EVO-2 connection)
- §6 source citation block (Sablé-Meyer / Dehaene — retains as brief pointer in owner summary)

**No split into 2c-1/2c-2 alternative**: If the annotation conversion is judged low-risk enough, Batch 2c-1 and 2c-2 can be merged into a single Batch 2c PR. The two-step split is recommended only if the project governance requires human review of the annotation conversion before extraction proceeds.

---

## 11. Final Recommendation

**Recommendation: Option B — New `Neuroscience_Annex/09_Geometric_Regularity_Interface.md` for §6.1–6.2; owner retains §6.3–6.5.**

**Rationale**:

1. **§6.1 is a clean extraction candidate.** It is pure external cognitive anthropology problem framing — same type as §5.1, which was extracted successfully in Batch 2b. No SRT formulas, no ambiguity.

2. **§6.2 is extractable after annotation conversion.** The empirical findings (Dehaene fMRI/MEG data, dual-pathway table, CNN failure, parietal expansion) are pure external neuroscience. The only blocker is the inline `→ SRT意义` annotations. These can be converted to explicit owner-section cross-references in a targeted prep pass (Batch 2c-1), after which §6.2 is safely extractable.

3. **§6.3–6.5 must remain in owner.** This is unambiguous:
   - `Ĝ_θ^{ventral/dorsal}` are SRT formal operator specializations, not external descriptions
   - `Ψ_f ∝ 1/η_compress` is a canonical Ψ_f formula — cannot live in `canonical: false` Annex
   - `d > d_symbolic` is a canonical d-value threshold claim with a named threshold
   - §6.5 depends on §6.4's `η_compress` definition; they cannot be separated

4. **A separate §09 Annex file is better than appending to §08.** `08_Evo_Devo_Interface.md` is thematically Evo-Devo (Levin, convergent evolution, Waddington). §6 is cognitive neuroscience / symbolic compression. Merging them would make 08 thematically incoherent and harder to navigate.

5. **Option A (no extraction) is acceptable as a conservative default.** If Batch 2c capacity is constrained, §6 can remain entirely in owner without harm. The annotation conversion cost is low, but the extraction decision can be deferred without operational cost — the adjudication record (this document) preserves the decision for the next person who revisits.

**Recommended execution sequence**:
1. This adjudication (PR-D0.6) — read-only, creates this document ✓
2. PR-D Batch 2c-1 — annotation conversion in §6.2.2 (4 annotations)
3. PR-D Batch 2c-2 — extraction of §6.1–6.2 to `Neuroscience_Annex/09_Geometric_Regularity_Interface.md`

Or, if single-PR preferred: PR-D Batch 2c (combined) — annotation conversion + extraction in one PR with two distinct commit layers.

---

## 12. Safety Record

- [ ] No Neuroscience files modified.
- [ ] No formulas changed.
- [ ] No theory content changed.
- [ ] No Annex files created.
- [ ] No content moved.
- [ ] `Ψ_f ∝ 1/η_compress` unchanged.
- [ ] `d > d_symbolic` unchanged.
- [ ] `Ĝ_θ^{ventral/dorsal}` unchanged.
- [ ] Ax-BIO/EVO axioms unchanged.
- [ ] H-Evo predictions unchanged.
