---
id: SRT-OPS-PR-D-BATCH2-GRT-ADJ-2026-04-28
type: adjudication_record
tags:
  - Operations
  - Adjudication
  - GRT
  - PR-D
  - Neuroscience
status: adjudication_complete
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-28
reference_audit: Operations/PR_A2_Neuroscience_06_10_Audit.md
pr: PR-D Batch 2 Prep — GRT Deduplication Adjudication
machine_summary: >
  Read-only adjudication of the supposed GRT / Hunt & Schooler duplication
  between SRT-NEURO-06 and SRT-NEURO-07. Finding: the duplication does not
  exist. NEURO-07 §6 is geometric regularity / Dehaene content, not GRT.
  Only NEURO-06 §6 has a dedicated GRT comparison section. Recommends
  independent extraction of NEURO-06 §6 and correction of a navigation
  block error in NEURO-07.
---

# PR-D Batch 2 Prep: GRT Deduplication Adjudication

**Date**: 2026-04-28
**Auditor**: Claude (claude-sonnet-4-6), read-only pass
**Triggered by**: PR-A2 audit cross-reference finding in [`Operations/PR_A2_Neuroscience_06_10_Audit.md`](PR_A2_Neuroscience_06_10_Audit.md) §4.3
**Files read**: `Neuroscience/SRT_Neuro_06_Field_Effects.md`, `Neuroscience/SRT_Neuro_07_Evo_Devo.md`

> **Primary finding**: The GRT duplication problem identified in PR-A2 does not exist in the current file state. NEURO-07 §6 is not a GRT section — it is a geometric regularity / symbolic compression section (Dehaene/Sablé-Meyer work). Only NEURO-06 §6 contains a dedicated GRT comparison. This report adjudicates the original question and documents the error in the PR-A2 cross-reference.

> **This PR did not**: modify any Neuroscience file, create any Annex, change any formula, change any canonical definition, move any section.

---

## 0. Executive Summary

**The supposed GRT duplication between NEURO-06 §6 and NEURO-07 §6 does not exist.**

A direct read of both files reveals:
- **NEURO-06 §6** ("与广义共振理论 (GRT) 的整合"): Contains a substantive, dedicated GRT comparison section referencing Hunt & Schooler (2019). ~28 lines of bridge content. This is the only GRT section in the 06–07 pair.
- **NEURO-07 §6** ("几何规则性与选择的符号化压缩"): Contains a geometric regularity / symbolic compression section based on Sablé-Meyer, Bhatt et al. (*eLife* 2025) and Dehaene team fMRI/MEG work. No GRT content. No Hunt & Schooler reference. No "广义共振理论" mention anywhere in the file body.

The PR-A2 audit assumed that because NEURO-06 §6 is a GRT section, NEURO-07 §6 would be analogously a GRT section. This assumption was incorrect — NEURO-07's section numbering happens to place unrelated content at §6.

**Consequences**:
1. The "shared GRT Annex vs. two separate Annexes" question is moot — there is only one GRT section.
2. PR-D Batch 2 can extract NEURO-06 §6 independently, without waiting for NEURO-07 GRT coordination.
3. NEURO-07's navigation block Refactor Notes contain an error ("§6 GRT") that should be corrected.
4. NEURO-07's actual §6 (geometric regularity / Dehaene) is a separate, unrelated Annex candidate that should be evaluated on its own merits.

**Recommended strategy**: Modified Option C → direct to B (one per-owner Annex for NEURO-06 §6 only). See §8.

---

## 1. Scope and Safety Record

### 1.1 Files read (read-only)

| File | Lines | Action |
|---|---|---|
| `Neuroscience/SRT_Neuro_06_Field_Effects.md` | 532 | Read, not modified |
| `Neuroscience/SRT_Neuro_07_Evo_Devo.md` | 793 | Read, not modified |

### 1.2 Safety confirmation

- [ ] No Neuroscience files modified.
- [ ] No Annex files created.
- [ ] No formulas changed.
- [ ] No canonical definitions changed.
- [ ] No frontmatter changed.
- [ ] No sections moved.
- [ ] QUALIA-1 / QUALIA-2 unchanged.
- [ ] Ax-FIELD-1, T-FIELD-2, κ_sync, Ĝ_macro unchanged.
- [ ] BIO-1 through EVO-3, Ĝ_devo, L2^bioelectric unchanged.
- [ ] Only new file: `Operations/PR_D_Batch2_GRT_Deduplication_Adjudication.md` (this file).

---

## 2. Source Section Inventory

### 2.1 SRT-NEURO-06 GRT content

| Section | Content Summary | Function | Move Risk |
|---|---|---|---|
| §6.1 GRT核心主张 | Hunt & Schooler (2019): consciousness as fundamental property; macroscopic consciousness = resonant combination of microscopic consciousness; resonance as physical mechanism of information integration | External theory summary — bridge interface only | Low: no SRT formula defined here |
| §6.2 SRT与GRT的会聚点 | Convergence table: EM field resonance ↔ Ĝ field carrier ✓; phase locking ↔ N_ephaptic ✓; resonance boundary ↔ ω_slowest^shared ✓ | Interface mapping — bridge content | Low: mappings are candidate proxies, not canonical identities |
| §6.3 SRT的独特贡献 (over GRT) | Four differentiators: (1) three-domain L0→L1→L2 framework; (2) embodied parameter θ; (3) downward causality; (4) operationalization via d-value and Φ | SRT-internal contrast claims | **Medium**: items (1)–(4) make SRT-internal claims; these are NOT bridge content — they belong in the owner file or in a dedicated SRT-internal summary, not extractable to a pure bridge Annex |

**Key finding on §6.3**: The "SRT独特贡献" subsection (§6.3) contains SRT-internal claims that contrast SRT with GRT, but the claims themselves (L0/L1/L2 framework, θ, downward causality, d-value operationalization) are canonical SRT content. This subsection should NOT be extracted to a GRT Interface Annex. It must remain in the owner file or a separate SRT-internal summary.

**Total GRT bridge content in NEURO-06**: §6.1 + §6.2 (~20 lines). §6.3 stays.

---

### 2.2 SRT-NEURO-07 GRT content

| Section | Content Summary | Function | Move Risk |
|---|---|---|---|
| §6 全节 (lines 529–637) | "几何规则性与选择的符号化压缩" — Sablé-Meyer/Bhatt et al. (*eLife* 2025), Dehaene team fMRI/MEG, MDL compression, symbolic cognition, d_symbolic threshold | Convergent evolution → symbolic cognition interface — **NOT GRT** | N/A: this section is entirely different content |
| Navigation block Refactor Notes | "§3.2 Levin interface, §5 convergent evolution, **§6 GRT**, and §8 Waddington are possible future Annex candidates." | **ERROR**: §6 label in navigation block incorrectly identifies this section as GRT | Navigation block correction needed |
| Any other mention of Hunt/Schooler/GRT/广义共振 | **None found** in file body (793 lines read in full) | — | — |

**Confirmed**: NEURO-07 contains zero GRT / Hunt & Schooler / 广义共振理论 content in its body text. The navigation block Refactor Notes entry "§6 GRT" is erroneous.

---

## 3. Overlap / Difference Analysis

| Theme | Present in NEURO-06? | Present in NEURO-07? | Same or Different? | Deduplication Recommendation |
|---|---|---|---|---|
| GRT core claims (Hunt & Schooler 2019) | **Yes** — §6.1, explicit citation | **No** | N/A — no overlap | No deduplication needed |
| EM field resonance as consciousness mechanism | **Yes** — §6.2 bridge mapping | **No** | N/A | No deduplication needed |
| SRT vs GRT contrast (three-domain, θ, downward causality) | **Yes** — §6.3, SRT-internal content | **No** | N/A | §6.3 stays in NEURO-06 owner |
| "广义共振" terminology | **Yes** — section title and body | **No** | N/A | — |
| Gamma resonance / phase locking | **Yes** — §6.2 (N_ephaptic binding) | **No** | N/A | — |
| Symbolic compression / Dehaene geometric regularity | No | **Yes** — §6 entire section | N/A | Separate evaluation (§7.4 below) |
| Hunt & Schooler citation | **Yes** — §6.1 | **No** | N/A | — |

**Overall**: No overlap exists between the GRT-related content of NEURO-06 and anything in NEURO-07. The PR-A2 report's §4.3 finding ("GRT comparison appears in both NEURO-06 §6 and NEURO-07 §6") was erroneous.

---

## 4. Owner Retention Rules

### 4.1 What must remain in SRT-NEURO-06 (regardless of extraction)

| Item | Reason |
|---|---|
| QUALIA-1 (Resonome: `R={λ_i,φ_i}`) | Defines SRT phenomenology — not extractable |
| QUALIA-2 (L2 Incompleteness: `Π_L2(R_θ)≠R_θ`) | Canonical SRT claim — not extractable |
| Ax-FIELD-1 (`ẋ=F(σ,θ)+α∇ε`) | Formal field coupling axiom — not extractable |
| Def-Ephaptic-Binding (`κ_sync∝∫|E_LFP|²dV`) | Defines κ_sync — not extractable |
| T-FIELD-2 (`Ĝ_macro=C_field∘Ĝ_micro`) | Nested operator theorem — not extractable |
| T-FIELD-1, C-FIELD-1 | Coherence-binding theorem — not extractable |
| Ax-TEMP-1, Ax-TEMP-2 | Temporal dynamics axioms — not extractable |
| H-Field-1 through H-Field-4 | Falsifiable predictions — not extractable |
| Empirical patches (natural vision binding, EM/UPE) | Canonical anchors — not extractable |
| **§6.3 SRT的独特贡献** | SRT-internal contrast claims (L0/L1/L2, θ, downward causality, d-value operationalization) — **must stay in owner** |

### 4.2 What must remain in SRT-NEURO-07 (regardless of any future extraction)

| Item | Reason |
|---|---|
| Ax-BIO-1 (`L2^bioelectric ⊃ L2^synaptic`) | Levin-Layer Axiom — not extractable |
| Ax-BIO-2 (`Ĝ_neural ⊂ Ĝ_devo`) | Nested Operator Axiom — not extractable |
| Ax-BIO-2b (Genome-as-Generative-Model: `Ĝ_devo:(L0^morpho,θ_genome,θ_physio)→L1^phenotype`) | Formal generative model axiom — not extractable |
| Ax-BIO-3 (`Generativity_devo ∝ 1/Ψ_f(θ_morpho)`) | Sub-Critical Generativity — not extractable |
| Ax-EVO-1/2/3, Ax-PATH-1/2 | Evolution and pathology axioms — not extractable |
| Evo-Devo Bridge Note (P3/P4 self-labeled) | Already self-labeled guardrail — must remain in owner |
| T-EVO-1/2, C-EVO-1/2 | Theorems — not extractable |
| H-Evo-1 through H-Evo-4 | Falsifiable predictions — not extractable |
| Cancer mechanical window patch (2026-03-16) | Canonical empirical anchor — not extractable |
| Single-cell learning patch (2026-03-21) | Canonical empirical anchor — not extractable |
| **§6 geometric regularity (Dehaene/Sablé-Meyer)** | Contains SRT-internal d_symbolic threshold claims — partial extraction only after separate evaluation |

---

## 5. Annex Strategy Options

### Option A — Shared GRT Annex (`Neuroscience_Annex/07_GRT_Gamma_Resonance_Interface.md`)

**Status: Moot.** There is only one GRT section (NEURO-06 §6.1–§6.2). A "shared" Annex would have only one source. If created, it would simply be a single-source Annex attributed to NEURO-06.

**If created as a single-source Annex anyway**:
- Advantages: Creates a clean destination for any future GRT content; consistent naming convention
- Disadvantages: Creates a "shared" file with no sharing — misleading framing
- **Verdict**: Unnecessary overhead for this PR-D batch

---

### Option B — Two Per-Owner Annexes

**Status: Only one is needed.** NEURO-07 has no GRT content, so no `Neuroscience_Annex/08_Evo_Devo_GRT_Interface.md` is needed.

The correct single extraction is:
- `Neuroscience_Annex/07_Field_Effects_Interface.md` — extracts NEURO-06 §6.1 + §6.2 (GRT comparison) **plus** NEURO-06 Part B §2 (synaptic/GWT/IIT comparisons) as a unified field dynamics interface file

Or, if GRT content is separated from §2 content:
- `Neuroscience_Annex/07_GRT_Interface.md` — NEURO-06 §6.1 + §6.2 only

NEURO-07 does not need a parallel Annex for GRT.

---

### Option C — No Extraction Yet

**Not applicable for NEURO-06 §6.1–§6.2.** These sections are clearly bounded bridge content with no canonical SRT formula definitions. The extraction risk is low. Delaying extraction serves no purpose.

**Partially applicable for NEURO-07 §6** (geometric regularity): This section warrants a separate evaluation before extraction — its §6.3–6.5 subsections (d_symbolic threshold, ηcompress, cognitive phase transitions) contain SRT-internal claims that may not be extractable. A separate adjudication for NEURO-07 §6 is recommended before any PR-D batch targeting it.

---

### Option D — Shared GRT Annex + Owner-Specific Summaries

**Status: Inapplicable.** The deduplication problem that would motivate this option does not exist.

---

## 6. Required Guardrails for Future GRT Annex (NEURO-06 §6.1–§6.2)

When `Neuroscience_Annex/07_Field_Effects_Interface.md` (or a dedicated GRT file) is created in PR-D Batch 2, it must carry the following guardrails:

1. GRT (Hunt & Schooler) comparison is bridge/interface material — it does not define any SRT canonical claims.
2. GRT does not define QUALIA-1 or the SRT Resonome (`R={λ_i,φ_i}`).
3. Gamma resonance does not define Ĝ_θ or its field-coupling formalism.
4. GRT does not redefine κ_sync or T-FIELD-2.
5. The convergence table in §6.2 presents candidate proxy mappings, not canonical identity claims; the `✓` marks indicate functional analogy, not ontological identity.
6. **§6.3 (SRT独特贡献 over GRT) must NOT be extracted** — it contains SRT-internal differentiation claims and belongs in the owner file.
7. The owner file (NEURO-06) must retain a "Companion pointer" to the Annex file, noting that the Annex contains only §6.1–§6.2 bridge content and that §6.3 remains in the owner.

---

## 7. Proposed PR-D Batch 2 Plan (Revised)

### 7.1 What the deduplication finding changes

The original PR-D Batch 2 plan (from PR-A2 §5.2) assumed:
- SRT-NEURO-06 §2 + §6 → `Neuroscience_Annex/07_Field_Effects_Interface.md`
- SRT-NEURO-07 §3.2 + §5 + **§6 (GRT)** + §8 → `Neuroscience_Annex/08_Evo_Devo_Interface.md`
- GRT cross-file deduplication decision required

Revised plan:
- NEURO-07 §6 is **not** a GRT section — remove it from the GRT deduplication scope entirely
- NEURO-07 §6 (geometric regularity) needs a separate adjudication

### 7.2 PR-D Batch 2a (recommended: execute first)

**Target**: NEURO-06 Part B interface sections

**Extractions**:
| Source | Extraction | Annex file |
|---|---|---|
| NEURO-06 §2.1 (synaptic synchrony comparison) | Extract | `Neuroscience_Annex/07_Field_Effects_Interface.md` |
| NEURO-06 §2.2 (GWT/Dehaene comparison) | Extract | `Neuroscience_Annex/07_Field_Effects_Interface.md` |
| NEURO-06 §2.3 (IIT/Tononi comparison) | Extract | `Neuroscience_Annex/07_Field_Effects_Interface.md` |
| NEURO-06 §6.1 (GRT core claims) | Extract | `Neuroscience_Annex/07_Field_Effects_Interface.md` |
| NEURO-06 §6.2 (SRT-GRT convergence table) | Extract | `Neuroscience_Annex/07_Field_Effects_Interface.md` |
| NEURO-06 §6.3 (SRT独特贡献 over GRT) | **Stay in owner** | — |

**What stays in NEURO-06**: All Part A axioms, QUALIA-1/2, T-FIELD-1/2, C-FIELD-1, §3 (SRT framework), §4 (costs/risks), §5 (predictions + evidence), §6.3, §7 (neural modulators), §8 (conclusion), empirical patches, appendix.

**Readiness**: High. NEURO-06 §2 and §6.1–§6.2 sections are clearly bounded bridge content with no ambiguous formula definitions.

### 7.3 PR-D Batch 2b (after 2a is stable)

**Target**: NEURO-07 Part B interface sections (excluding §6)

**Extractions**:
| Source | Extraction | Annex file |
|---|---|---|
| NEURO-07 §3.2 (Levin interface) | Extract | `Neuroscience_Annex/08_Evo_Devo_Interface.md` |
| NEURO-07 §5 (convergent evolution) | Extract (partial — see §7.4) | `Neuroscience_Annex/08_Evo_Devo_Interface.md` |
| NEURO-07 §8 (Waddington reinterpretation) | Extract | `Neuroscience_Annex/08_Evo_Devo_Interface.md` |
| NEURO-07 §6 (geometric regularity) | **Separate adjudication required first** | — |

**What stays in NEURO-07**: All Part A axioms, Evo-Devo Bridge Note, §3.1 (SRT framework), §3.3/3.4 (morpho-cognitive isomorphism, cancer de-federation), §4 (costs/risks), §7 (predictions), §9 (synthetic biology), §10 (conclusion), empirical patches.

### 7.4 NEURO-07 §6 — separate adjudication required

NEURO-07 §6 ("几何规则性与选择的符号化压缩") contains:
- **Bridge sections**: §6.1 (binding problem narrative), §6.2 (empirical fMRI/MEG findings), §6.3 (SRT's L0→L1 selection architecture interpretation)
- **SRT-internal sections**: §6.4 (ηcompress as neural implementation), §6.5 (d_symbolic threshold and cognitive phase transition) — these contain SRT-internal claims that may not be extractable

A dedicated adjudication is recommended before including NEURO-07 §6 in any extraction batch. It should not be bundled into the GRT scope.

### 7.5 Navigation block correction needed

NEURO-07's navigation block Refactor Notes say:
> "§3.2 Levin interface, §5 convergent evolution, **§6 GRT**, and §8 Waddington are possible future Annex candidates."

This contains an error. "§6 GRT" should read "§6 geometric regularity / Dehaene / symbolic compression (partial — d_symbolic sections need separate adjudication)".

This correction should be made in PR-D Batch 2b (when NEURO-07 is first touched) or in a targeted navigation correction PR. It is a documentation error, not a theory error — but it should not propagate into PR-D planning for NEURO-07.

---

## 8. Final Recommendation

**Recommendation: B (modified) — one per-owner Annex, NEURO-06 only**

Full rationale:

1. **The deduplication problem is moot.** NEURO-07 has no GRT content. Option A (shared GRT Annex) and Option D (shared + summaries) address a problem that does not exist.

2. **NEURO-06 §6.1–§6.2 should be extracted to `Neuroscience_Annex/07_Field_Effects_Interface.md`** in PR-D Batch 2a, bundled with the §2 (synaptic/GWT/IIT) bridge sections. This creates a single, coherent "field dynamics external theory comparisons" Annex.

3. **NEURO-06 §6.3 must stay in the owner file.** It is SRT-internal content.

4. **NEURO-07 needs no GRT Annex.** Its §6 geometric regularity content needs a separate adjudication before extraction.

5. **NEURO-07 navigation block needs a one-line correction** (change "§6 GRT" to reflect the actual content). This should be done when NEURO-07 is first touched in PR-D Batch 2b.

6. **PR-D Batch 2 can proceed as Batch 2a (NEURO-06) immediately after this adjudication merges.** No inter-file coordination needed for the GRT question.

---

## 9. Error Provenance Note

The PR-A2 audit report (`Operations/PR_A2_Neuroscience_06_10_Audit.md`) §3.2 listed:

> "§6 GRT comparison (Hunt & Schooler 2019): Gamma resonance theory comparison | `Neuroscience_Annex/08_Evo_Devo_Interface.md` | High — identical pattern to §6 in SRT-NEURO-06"

This was an inference error. At the time of PR-A2, the auditor correctly identified that NEURO-06 §6 is a GRT section. The "identical pattern to §6" inference then assumed that NEURO-07's §6 would mirror NEURO-06's §6. In reality, NEURO-07 §6 is a completely different section (geometric regularity). The PR-A2 report also carried this error into the navigation blocks added in PR-B.

This type of structural inference error — assuming that section numbers in sibling files contain analogous content — is a known hazard when auditing a large file corpus. The current adjudication corrects it.

**No theory content was harmed.** The error was in the navigation Refactor Notes label only. The PR-B navigation blocks did not move any content.

---

## 10. Safety Record

This PR confirms:

- [ ] No Neuroscience files modified.
- [ ] No formulas changed.
- [ ] No theory content changed.
- [ ] No files moved or deleted.
- [ ] No Annex directories or files created.
- [ ] S0-S6 subjecthood thresholds unchanged.
- [ ] L0/L1/L2, Ψ_f, d-value, Ĝ_θ, T_dir canonical definitions unchanged.
- [ ] QUALIA-1 / QUALIA-2 unchanged.
- [ ] Ax-FIELD-1, T-FIELD-2, κ_sync, Ĝ_macro unchanged.
- [ ] BIO-1 through EVO-3, Ĝ_devo, L2^bioelectric unchanged.
- [ ] CompactCore files not touched.
- [ ] Core/, Core_Law/, AI/, Philosophy/, Public/, Papers/ not touched.
- [ ] Only new file: `Operations/PR_D_Batch2_GRT_Deduplication_Adjudication.md` (this file).
