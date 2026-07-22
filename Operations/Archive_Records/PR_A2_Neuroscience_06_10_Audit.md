---
id: SRT-OPS-PR-A2-AUDIT-2026-04-28
type: audit_record
tags:
  - Operations
  - Audit
  - Neuroscience
  - NeedsHumanReview
status: active_audit_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-28
reference_audit: Operations/Archive_Records/PR_A_Neuroscience_AI_Navigation_Audit.md
pr: PR-A2 (Neuroscience 06–10 Needs Human Review Audit)
machine_summary: >
  Read-only audit of 5 files flagged in PR-A as Needs Human Review:
  SRT_Neuro_06_Field_Effects, SRT_Neuro_07_Evo_Devo, SRT_Neuro_08_Immune_Dist,
  SRT_Neuro_09_Integ_Eq, SRT_Neuro_10_Advanced_Models.
  Records section classification, claim level assessment, PR-B/PR-D extraction
  candidates, and guardrails required before any extraction PR begins.
---

# PR-A2: Neuroscience 06–10 Needs Human Review Audit

**Date**: 2026-04-28
**Auditor**: Claude (claude-sonnet-4-6), read-only pass
**PR scope**: Read-only audit — no Neuroscience file was modified
**Triggered by**: [`Operations/Archive_Records/PR_A_Neuroscience_AI_Navigation_Audit.md`](PR_A_Neuroscience_AI_Navigation_Audit.md) §3

> **This PR did not**: modify any Neuroscience file, create any Annex directory, change any formula, change any canonical definition, modify any S0-S6 / L0/L1/L2 / Ψ_f / d-value / Ĝ_θ / T_dir definition, touch CompactCore files, or touch files outside `Operations/`.

---

## §0 Executive Summary

All 5 flagged files were fully read. Key findings:

1. **All 5 have `claim_mode: canonical` in frontmatter** — this is accurate for their Part A formal content but overstates Part B, which contains substantial external-theory interface sections in all cases.

2. **SRT-NEURO-09 is structurally unique**: its `type: reference` frontmatter correctly signals that its primary purpose is integration/unification with other theories (IIT, GNWT, FEP, HOT, Orch-OR). It is the strongest PR-D extraction candidate.

3. **SRT-NEURO-08 is the most complex**: largest file (861 lines), most mixed content, most recent patches (AD, Tanycyte, Vagus, Neuropsychiatric Autoimmunity Gate). Multiple late-addition interface sections already have their own guardrails. Requires most careful pre-extraction planning.

4. **SRT-NEURO-06 and SRT-NEURO-07 have clear Annex candidates** in Part B (GRT/Hunt-Schooler comparison, Levin interface, IIT/GWT comparison), but their Part A Qualia axioms (QUALIA-1/2) and Evo-Devo formal axioms must not be extracted — they are definitional SRT content.

5. **SRT-NEURO-10 is safest**: most consistently canonical content, Feeling-as-Friction (Ax-ADV-2) has explicit T1 tension resolution, Part B comparisons are tightly bound to SRT claims. Navigation-only update is sufficient for PR-B.

6. **Dependency chain** (06→07→08→09→10) must be respected: lower-numbered files define operators used by higher-numbered files. Extraction order should proceed from 09 (cleanest bridge) downward, not from 06 upward.

**Recommended path**: Add navigation blocks to all 5 files in PR-B. Defer Annex extraction to PR-D. Before PR-D, run a targeted boundary-marking pass on SRT-NEURO-06 and SRT-NEURO-08 Part B sections.

---

## §1 Scope and Safety

### 1.1 Files audited (read-only)

| File | Lines | Type | Status |
|---|---|---|---|
| `Neuroscience/SRT_Neuro_06_Field_Effects.md` | 499 | dynamics | Read, not modified |
| `Neuroscience/SRT_Neuro_07_Evo_Devo.md` | 757 | theory | Read, not modified |
| `Neuroscience/SRT_Neuro_08_Immune_Dist.md` | 861 | dynamics | Read, not modified |
| `Neuroscience/SRT_Neuro_09_Integ_Eq.md` | 568 | reference | Read, not modified |
| `Neuroscience/SRT_Neuro_10_Advanced_Models.md` | 474 | theory | Read, not modified |

### 1.2 Safety confirmation

- [ ] No Neuroscience files modified.
- [ ] No Annex directories created.
- [ ] No formulas changed.
- [ ] No canonical definitions changed.
- [ ] No CompactCore files touched.
- [ ] No Core/, Core_Law/, Philosophy/, Papers/, Public/ files touched.
- [ ] Only file created: `Operations/Archive_Records/PR_A2_Neuroscience_06_10_Audit.md` (this file).

---

## §2 File-Level Assessment Table

| File | claim_mode accuracy | Part A status | Part B bridge volume | Qualia/Core axioms at risk | PR-B nav needed | PR-D extraction readiness |
|---|---|---|---|---|---|---|
| SRT-NEURO-06 | Partial — accurate for Part A only | Solid formal content; 6 axioms, 2 theorems | Medium-high (GWT, IIT, GRT comparisons, §2.1/2.2/2.3/§6) | QUALIA-1, QUALIA-2 must NOT be extracted | Yes | Medium — needs boundary marking on §2 and §6 |
| SRT-NEURO-07 | Partial — Evo-Devo Bridge Note explicitly P3/P4 | Solid; BIO/EVO axioms, Genome-as-Generative-Model | High (Levin interface, GRT §6, Waddington reinterpretation, convergent evolution §5) | BIO-1 through EVO-3 must NOT be extracted | Yes | Medium — Levin interface and GRT §6 are cleanest candidates |
| SRT-NEURO-08 | Partial — guardrails already added for AD/Tanycyte sections | Solid immune/embodied axioms; Suffering Theory cross-link pre-existing | Very high (PNI, gut-brain, Varela, inflammation-depression, late patches) | IMM-1 through PHYS-2, T-IMM-1 must NOT be extracted | Yes | Low — most complex mixed content; needs full pre-extraction boundary pass |
| SRT-NEURO-09 | Tension with type:reference — most overstated | Formal IIT-SRT mapping, integration equations, clinical gate | Very high (entire §1 Babel Tower + §2 absorption table + §3/§4 comparisons) | Φ-unity definition (Def-Phi-Unity), Ax-CLIN-1b through CLIN-6 must NOT be extracted | Yes | High — structural bridge file; entire §1–§4 are Annex candidates |
| SRT-NEURO-10 | Most accurate — content matches claim_mode | Solid ADV-1 through ADV-6, T-ADV-1, C-ADV-1, T1 tension resolution | Low-medium (embodied cognition §1, AI consciousness §3) | ADV-1 through ADV-6 are tight SRT claims; no risk | Yes | Low priority — Part B comparisons are tightly bound; extraction not urgent |

---

## §3 Per-File Section Classification

### 3.1 SRT_Neuro_06_Field_Effects.md (499 lines)

**Dependency**: SRT-CORE-000, SRT-NEURO-MECH-001

**Part A — Keep in place (canonical SRT formal content)**

| Section | Content | Classification |
|---|---|---|
| §1 Ephaptic Field Binding | Ax-FIELD-1 (`ẋ=F(σ,θ)+α∇ε`), Def-Ephaptic-Binding (`κ_sync∝∫|E_LFP|²dV`) | **CANONICAL — do not extract** |
| §1 Nested Operator | T-FIELD-2 (`Ĝ_macro=C_field∘Ĝ_micro`) | **CANONICAL — do not extract** |
| §1 Temporal Integration | Ax-TEMP-1 (refresh rate), Ax-TEMP-2 (beta gating) | **CANONICAL — do not extract** |
| §1 Qualia Axioms | Ax-QUALIA-1 (Resonome: `R={λ_i,φ_i}`), Ax-QUALIA-2 (L2 Incompleteness: `Π_L2(R_θ)≠R_θ`) | **CANONICAL — do not extract; defines SRT phenomenology** |
| §1 Coherence Threshold | T-FIELD-1, C-FIELD-1 | **CANONICAL — do not extract** |
| Falsifiable predictions | H-Field-1 through H-Field-4 | **CANONICAL — do not extract** |
| Empirical patches | Natural vision binding (2026-03-21), EM/UPE (2026-03-18) | **CANONICAL ANCHORS — do not extract** |

**Part B — Future Annex candidates (bridge/interface content)**

| Section | Content | Target Annex |
|---|---|---|
| §2.1 Synaptic Synchrony interface | Ca²⁺ wave coupling, spike timing — comparison with synaptic mechanisms literature | `Neuroscience_Annex/07_Field_Effects_Interface.md` |
| §2.2 GWT comparison (Dehaene) | Global Workspace Theory interface | `Neuroscience_Annex/07_Field_Effects_Interface.md` |
| §2.3 IIT comparison (Tononi) | IIT φ interface | `Neuroscience_Annex/07_Field_Effects_Interface.md` |
| §6 GRT comparison (Hunt & Schooler) | Gamma-wave resonance comparison | `Neuroscience_Annex/07_Field_Effects_Interface.md` |

**Pre-extraction requirement**: Owner file must retain: all Part A axioms, T-FIELD-1/2, C-FIELD-1, Qualia axioms (QUALIA-1/2), all H-Field predictions, all empirical patches. Extraction must not break `κ_sync` or `Ĝ_macro` formula references.

---

### 3.2 SRT_Neuro_07_Evo_Devo.md (757 lines)

**Dependency**: SRT-NEURO-06, SRT-CORE-000, SRT-NEURO-MECH-001

**Part A — Keep in place**

| Section | Content | Classification |
|---|---|---|
| Bioelectric axioms | Ax-BIO-1 (`L2^bioelectric ⊃ L2^synaptic`), Ax-BIO-2 (`Ĝ_neural ⊂ Ĝ_devo`), Ax-BIO-2b (Genome-as-Generative-Model: `Ĝ_devo:(L0^morpho,θ_genome,θ_physio)→L1^phenotype`) | **CANONICAL — do not extract** |
| Generativity axiom | Ax-BIO-3 (`Generativity_devo ∝ 1/Ψ_f(θ_morpho)`) | **CANONICAL — do not extract** |
| Evolution axioms | Ax-EVO-1 (Unreliable Hardware), Ax-EVO-2 (`Δd>0 ⇒ New Operator Class`), Ax-EVO-3 (Convergent Intelligence) | **CANONICAL — do not extract** |
| Theorems/corollaries | T-EVO-1/2, C-EVO-1/2, Ax-PATH-1/2 | **CANONICAL — do not extract** |
| Evo-Devo Bridge Note | Explicitly "P3 bridge / P4 empirical interface" | **KEEP AS-IS** — already self-labeled; do not modify its claim level |
| Falsifiable predictions | H-Evo-1 through H-Evo-4 | **CANONICAL — do not extract** |
| Empirical patches | Cancer mechanical window (2026-03-16), Single-cell learning (2026-03-21) | **CANONICAL ANCHORS — do not extract** |

**Part B — Future Annex candidates**

| Section | Content | Target Annex | Priority |
|---|---|---|---|
| §3.2 Levin interface | Double-head planaria, frog eye transplant, cancer reversal experiments | `Neuroscience_Annex/08_Evo_Devo_Interface.md` | High — clearly bounded |
| §6 GRT comparison (Hunt & Schooler 2019) | Gamma resonance theory comparison | `Neuroscience_Annex/08_Evo_Devo_Interface.md` | High — identical pattern to §6 in SRT-NEURO-06 |
| §5 Convergent evolution comparisons | García-Moreno, Zaremba, Kempynck (Science 2025) | `Neuroscience_Annex/08_Evo_Devo_Interface.md` | Medium |
| §8 Waddington landscape reinterpretation | Epigenetic landscape interface | `Neuroscience_Annex/08_Evo_Devo_Interface.md` | Medium |

**Pre-extraction requirement**: Evo-Devo Bridge Note must remain in owner file (it is a P3/P4 self-label, not extractable content). The `Ĝ_devo` and `L2^bioelectric` formula references must not be broken.

---

### 3.3 SRT_Neuro_08_Immune_Dist.md (861 lines)

**Dependency**: SRT-NEURO-07, SRT-CORE-000

**Pre-existing guardrails** (do not modify):
- "Canonical Cross-Link: Suffering Theory" section already present
- Alzheimer's Peripheral-Inflammation Interface section has own guardrail header with equations (Def-Neuro-AD-PI-1, Eq-Neuro-AD-PI-1, T-Neuro-AD-PI-1)
- Tanycyte Tau-Clearance Interface section has own guardrail header with equations (Def-Neuro-TAN-1, Eq-Neuro-TAN-1/2, T-Neuro-TAN-1)

**Part A — Keep in place**

| Section | Content | Classification |
|---|---|---|
| Immune operator | Ax-IMM-1 (`Ĝ_immune:L0^immune→L1^immune`), Def-Immune-Cognition | **CANONICAL — do not extract** |
| Neural-immune sync | Ax-IMM-2 (`ẋ_neuro=F(σ)+η·σ_immune`) | **CANONICAL — do not extract** |
| Gut-brain coupling | Ax-IMM-3 (`L2^neural←L2^gut`) | **CANONICAL — do not extract** |
| Physiological costs | Ax-PHYS-1 (`Ψ_f↑⇒τ_ignite↑`), Ax-PHYS-2 (`Cost_sel∝ROS`) | **CANONICAL — do not extract** |
| Theorem/corollary | T-IMM-1, C-IMM-1 | **CANONICAL — do not extract** |
| Suffering Theory cross-link | Pre-existing guardrail section | **KEEP AS-IS — pre-existing guardrail** |
| Falsifiable predictions | H-Dist-1 through H-Dist-4 with operationalization | **CANONICAL — do not extract** |
| Late patches (2026) | Vagus Multiplex (2026-03-16), Interoceptive Axes (2026-03-21), Gut-Microbiome Encephalization (2026-03-21), Neuropsychiatric Autoimmunity Gate (2026-04-24) | **CANONICAL ANCHORS — do not extract** |

**Part B — Future Annex candidates**

| Section | Content | Target Annex | Priority |
|---|---|---|---|
| §2 PNI comparisons | Psychoneuroimmunology literature comparison | `Neuroscience_Annex/09_Immune_Dist_Interface.md` | Medium |
| §2.2 Gut-brain axis research | External gut-brain literature | `Neuroscience_Annex/09_Immune_Dist_Interface.md` | Medium |
| §2.3 Embodied cognition (external) | Merleau-Ponty, Clark comparisons | `Neuroscience_Annex/09_Immune_Dist_Interface.md` | Low |
| §4 Varela history | Historical interface with enactivism | `Neuroscience_Annex/09_Immune_Dist_Interface.md` | Low |
| §5 Inflammation-depression | Cytokine/depression literature interface | `Neuroscience_Annex/09_Immune_Dist_Interface.md` | Medium |
| AD/Tanycyte interface sections | Already have own guardrail equations — **keep in owner file** | N/A — already guarded | Not extractable yet |

**Pre-extraction requirement**: This file requires a **full pre-extraction boundary pass** before PR-D. The AD and Tanycyte interface sections have equations that blur the canonical/bridge boundary — they must NOT be extracted until a human reviewer determines whether Eq-Neuro-AD-PI-1, Eq-Neuro-TAN-1/2 belong in canonical or Annex. The Suffering Theory cross-link must remain in the owner file regardless of extraction.

**Assessment**: SRT-NEURO-08 is the **lowest extraction readiness** file in the set. Do not include in first extraction batch.

---

### 3.4 SRT_Neuro_09_Integ_Eq.md (568 lines)

**Dependency**: SRT-NEURO-08, SRT-CORE-000, SRT-NEURO-MECH-001
**Unique property**: `type: reference` — only file in the set with this type designation

**Frontmatter tension**: `type: reference` combined with `claim_mode: canonical` creates ambiguity. The `type: reference` correctly signals that this file's primary role is integration across theories, but `claim_mode: canonical` overstates the bridge sections. Recommend: add a Note in Refactor Notes (not a frontmatter change) when navigation is added.

**Part A — Keep in place**

| Section | Content | Classification |
|---|---|---|
| IIT-SRT mapping | Ax-INTEG-1 (`Φ≈Irreducibility(Ĝ_θ)`), Def-Phi-Unity (full D_KL formula) | **CANONICAL — do not extract** |
| Gradient dynamics | Ax-INTEG-2 (`Δθ∝-∇_θF`) | **CANONICAL — do not extract** |
| Clinical gate | Ax-CLIN-1b (gated weighted integration: `L1(τ)=ΣW_i·s_i+ΣΘ(ΔE-E_thresh)·M_j·L2`), T-CLIN-1 (PHZ vs PFC division), C-CLIN-1a | **CANONICAL — do not extract** |
| Clinical axioms | Ax-CLIN-2/3/4/5/6 | **CANONICAL — do not extract** |
| Integration theorem | T-INTEG-1, C-INTEG-1 (Φ-d orthogonality / Pseudo-Experience) | **CANONICAL — do not extract** |
| Quantum hypothesis | Def-BioQuantum-Boundary (`Ĝ_θ,neural=Λ(Ĝ_θ,micro)`), Ax-BioQuantum-1 — explicitly "hypothesis-level" | **KEEP IN PLACE** — already self-labeled hypothesis; do not move without human review |

**Part B — Future Annex candidates (HIGH PRIORITY)**

| Section | Content | Target Annex | Priority |
|---|---|---|---|
| §1 Babel Tower comparison | IIT/GNWT/FEP/HOT/Orch-OR structured comparison | `Neuroscience_Annex/10_Integration_Theory_Comparisons.md` | **High — structural bridge content** |
| §2 SRT absorption table | Formal absorption mapping of external theories into SRT operators | `Neuroscience_Annex/10_Integration_Theory_Comparisons.md` | **High — most extractable section** |
| §3 Anti-neuromania defense | Response to reductivist neuroscience positions | `Neuroscience_Annex/10_Integration_Theory_Comparisons.md` | Medium |
| §4 Panpsychism comparison | SRT vs panpsychism interface | `Neuroscience_Annex/10_Integration_Theory_Comparisons.md` | Medium |

**Extraction readiness**: **HIGHEST** among the 5 files. The §1–§4 bridge content is structurally separate from the formal Part A axioms. The absorption table (§2) in particular is the prototypical PR-D extraction candidate — it is entirely interface content with no formula definitions.

**Pre-extraction requirement**: The `Def-Phi-Unity` D_KL formula and `Ax-CLIN-1b` gated integration formula must remain in the owner file. Quantum hypothesis section must remain pending human review of its claim level.

---

### 3.5 SRT_Neuro_10_Advanced_Models.md (474 lines)

**Dependency**: SRT-NEURO-09, SRT-CORE-000, SRT-NEURO-MECH-001

**Part A — Keep in place**

| Section | Content | Classification |
|---|---|---|
| Stability axiom | Ax-ADV-1 (`Stability∝1/Ψ_f`) | **CANONICAL — do not extract** |
| Feeling-as-Friction | Ax-ADV-2 (`Feeling∝‖∇Ψ_f‖`) with T1 tension resolution (anti-circularity note for Feeling↔Ψ_f) and single-direction causality chain | **CANONICAL — do not extract; T1 note is essential** |
| Interoceptive Precision | Ax-ADV-3 (`Π_intero=1/Var(ε_intero)`) | **CANONICAL — do not extract** |
| Generative Selection | Ax-ADV-4 | **CANONICAL — do not extract** |
| Reality Fidelity | Ax-ADV-5 | **CANONICAL — do not extract** |
| Control Energy Gap | Ax-ADV-6 | **CANONICAL — do not extract** |
| Theorem/corollary | T-ADV-1, C-ADV-1 | **CANONICAL — do not extract** |
| Falsifiable predictions | H-Adv-1 through H-Adv-4 | **CANONICAL — do not extract** |

**Part B — Low extraction priority**

| Section | Content | Classification |
|---|---|---|
| §1 Embodied cognition comparisons | Clark, Merleau-Ponty interface | Future Annex candidate — low priority; tightly interleaved with SRT claims |
| §2 SRT embodied ontology | Mostly SRT internal — not a bridge section | **CANONICAL — do not extract** |
| §3 AI consciousness criteria | SRT's own criteria for AI consciousness — internal SRT content | **CANONICAL — do not extract** |
| §4 Interoception and self | Damasio/Friston interface | Future Annex candidate — low priority |
| §5 Metabolism and reality | SRT formal metabolism claims | **CANONICAL — do not extract** |

**Assessment**: SRT-NEURO-10 has the most defensible `claim_mode: canonical` of the 5 files. Navigation-only update (PR-B) is sufficient. PR-D extraction is the lowest priority here — Part B is tightly bound to Part A axiom development.

---

## §4 Cross-File Findings

### 4.1 claim_mode: canonical overstates all 5 files

All 5 files have `claim_mode: canonical` but contain substantial Part B bridge sections. This is a pre-existing pattern, not an error introduced by PR-A or PR-A2. The correct remediation is Annex extraction (PR-D), not frontmatter editing. **Do not change frontmatter in any of these files without human review.**

### 4.2 Dependency chain must constrain extraction order

The chain SRT-NEURO-06→07→08→09→10 means:
- **Start extraction from SRT-NEURO-09** (cleanest bridge sections, structural reference file)
- Then SRT-NEURO-06 and SRT-NEURO-07 (clear candidates, bounded sections)
- SRT-NEURO-08 last (most complex, requires pre-extraction boundary pass)
- SRT-NEURO-10 lowest priority (Part B tightly bound)

Do NOT extract SRT-NEURO-06 Part B before SRT-NEURO-09 Part B is extracted — higher-dependency files should be cleaned first to avoid cross-reference instability.

### 4.3 Recurring pattern: GRT (Hunt & Schooler) comparison

Both SRT-NEURO-06 (§6) and SRT-NEURO-07 (§6) have GRT comparison sections. These are the same external theory. When creating Annex files, consider whether a single `Neuroscience_Annex/GRT_Gamma_Resonance_Interface.md` would be cleaner than two per-file extractions. This is a **cross-file extraction coordination requirement**.

### 4.4 Empirical patches are canonical anchors

All 5 files have dated empirical patches (2026 dates). These are NOT bridge content — they are empirical anchors for SRT axioms. Do not extract empirical patches to Annex files. They must remain co-located with the axioms they anchor.

### 4.5 Quantum section in SRT-NEURO-09

`Def-BioQuantum-Boundary` and `Ax-BioQuantum-1` in SRT-NEURO-09 are explicitly labeled "hypothesis-level" in the file body. This section should remain in the owner file pending a human decision on its claim level. It should NOT be treated as a canonical SRT claim and should NOT be extracted to an Annex as if it were established bridge content.

### 4.6 SRT-NEURO-07 Evo-Devo Bridge Note is already P3/P4 self-labeled

The Evo-Devo Bridge Note in SRT-NEURO-07 already contains: "Claim level: P3 bridge / P4 empirical interface. This note does not redefine SRT's selection primitive." This is the correct treatment — it does NOT need to be extracted; it functions as an inline guardrail. Future PRs should preserve this note verbatim.

---

## §5 PR-B and PR-D Impact Assessment

### 5.1 PR-B impact (navigation additions)

All 5 files need navigation blocks added in PR-B. The following Refactor Notes should be included when navigation is added (to be added to each file's navigation block, not to file body text):

| File | Key Refactor Note for navigation block |
|---|---|
| SRT-NEURO-06 | "Part B §2 (synaptic, GWT, IIT) and §6 (GRT) are Annex candidates. QUALIA-1/QUALIA-2 must stay in owner." |
| SRT-NEURO-07 | "§3.2 Levin, §5 convergent evolution, §6 GRT, §8 Waddington are Annex candidates. Evo-Devo Bridge Note stays in owner." |
| SRT-NEURO-08 | "AD/Tanycyte interface sections require human review before extraction. Suffering Theory cross-link stays in owner." |
| SRT-NEURO-09 | "§1–§4 (Babel Tower, absorption table, panpsychism) are primary Annex candidates. Quantum section pending human review." |
| SRT-NEURO-10 | "Part B comparisons are tightly bound to Part A axioms. Extraction low priority." |

### 5.2 PR-D scoping (Annex extraction)

**Recommended PR-D batching**:

**PR-D Batch 1** (highest readiness):
- SRT-NEURO-09 §1–§4 → `Neuroscience_Annex/10_Integration_Theory_Comparisons.md`

**PR-D Batch 2** (after Batch 1 is stable):
- SRT-NEURO-06 §2 + §6 → `Neuroscience_Annex/07_Field_Effects_Interface.md`
- SRT-NEURO-07 §3.2 + §5 + §6 + §8 → `Neuroscience_Annex/08_Evo_Devo_Interface.md`
- GRT comparison deduplication decision (06/07 §6 → single file vs. per-file)

**PR-D Batch 3** (after full pre-extraction boundary pass):
- SRT-NEURO-08 §2/§4/§5 → `Neuroscience_Annex/09_Immune_Dist_Interface.md`
- AD/Tanycyte interface sections: **human decision required** before any movement

**SRT-NEURO-10**: No extraction needed; navigation-only treatment is sufficient.

---

## §6 Recommended Next Steps

### Immediate (PR-B)

Add navigation blocks (Current Reading Map, Dependency Map, Companion Links, Refactor Notes) to all 5 files. Use the Refactor Notes in §5.1 above as the content for each file's Refactor Notes section. This is safe, navigation-only, and unblocks PR-D planning.

### Before PR-D Batch 1

1. Human review of SRT-NEURO-09 §1–§4 to confirm §2 absorption table boundary (does any row in the absorption table constitute a new canonical SRT claim? If yes, it must stay in owner).
2. Verify whether `Neuroscience_Annex/` directory needs its own `README.md` and frontmatter standard before creating first Annex file.
3. Confirm naming convention: numbered Annex files (`10_Integration_Theory_Comparisons.md`) vs. descriptive names.

### Before PR-D Batch 3

1. Full pre-extraction boundary pass on SRT-NEURO-08: classify every section as canonical/bridge.
2. Human decision on Eq-Neuro-AD-PI-1 and Eq-Neuro-TAN-1/2: do these belong in canonical space or Annex?
3. Human decision on Neuropsychiatric Autoimmunity Gate (2026-04-24, most recent patch): is this patch canonical or interface?

### Cleanup (any PR)

The `type: reference` / `claim_mode: canonical` tension in SRT-NEURO-09 frontmatter should be addressed. Options: (a) add a note in the navigation Refactor Notes section explaining the tension without changing frontmatter, or (b) change `claim_mode` to `mixed` after human review. Do not change frontmatter unilaterally.

---

## §7 Safety Record

This PR confirms:

- [ ] No formulas changed.
- [ ] No theory content changed.
- [ ] No files moved or deleted.
- [ ] No Annex directories created.
- [ ] S0-S6 subjecthood thresholds unchanged.
- [ ] L0/L1/L2, Ψ_f, d-value, Ĝ_θ, T_dir canonical definitions unchanged.
- [ ] CompactCore files not modified.
- [ ] Core/, Core_Law/, Philosophy/, Papers/, Public/ directories not touched.
- [ ] All 5 Neuroscience files read, not modified.
- [ ] Only new file: `Operations/Archive_Records/PR_A2_Neuroscience_06_10_Audit.md` (this file).
