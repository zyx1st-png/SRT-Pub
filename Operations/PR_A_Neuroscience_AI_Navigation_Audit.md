---
id: SRT-OPS-PR-A-NAV-AUDIT-2026-04-28
type: audit_record
tags:
  - Operations
  - Audit
  - Navigation
  - Neuroscience
  - AI
status: active_audit_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-28
reference_report: Operations/Non_Philosophy_Refactor_Audit_Report.md
pr: PR-A (Neuroscience + AI Navigation Audit)
machine_summary: >
  Audit record for PR-A: navigation-only additions to Neuroscience/ and AI/ owner files.
  Records which files were modified, what was added, which files were scanned but not modified,
  and which files require human review before any future refactor.
---

# PR-A Neuroscience + AI Navigation Audit Record

**Date**: 2026-04-28
**PR scope**: Neuroscience/ and AI/ owner files — navigation-only
**Reference report**: [`Operations/Non_Philosophy_Refactor_Audit_Report.md`](Non_Philosophy_Refactor_Audit_Report.md)

> **This PR did not**: move any content, delete any content, create any Annex directory, change any formula, change any canonical definition, modify any S0-S6 subjecthood threshold, modify any L0/L1/L2 / Ψ_f / d-value / Ĝ_θ / T_dir definition.

---

## 1. Files Modified

### 1.1 Neuroscience/

| File | Lines before | Navigation added | Notes |
|---|---|---|---|
| `SRT_Neural_Mechanisms.md` | 1170 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | Main neural mechanisms owner; has existing Quick Reference |
| `SRT_Consciousness_Mechanisms.md` | 654 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | Consciousness mechanisms owner; has existing Quick Reference |
| `_SRT_Neuro_Axioms.md` | 465 | Current Reading Map, Dependency Map (with Used-by list), Companion Links, Refactor Notes | Neuroscience axiom base; used by most Neuroscience/ files |
| `SRT_Clin_00_IIT_PCI.md` | 552 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | IIT/PCI/GNWT interface — bridge file |
| `SRT_Clin_01_Pathology.md` | 845 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | Pathology interface — bridge file |
| `SRT_Clin_02_FEP.md` | 440 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | FEP/Active Inference interface — already had Canonical Cross-Link and Neural Proxy Boundary |
| `SRT_Clin_03_DMN_Networks.md` | 569 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | DMN/ADHD/Schizophrenia interface — bridge file |

### 1.2 AI/

| File | Lines before | Navigation added | Notes |
|---|---|---|---|
| `SRT_AI_00_Crisis.md` | 717 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | Entry/foundation file for AI domain |
| `SRT_AI_01_Ontology.md` | 1443 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | Main AI ontology owner; has existing Quick Reference |
| `SRT_AI_02_Mortality_Wisdom.md` | 929 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | Mortality/wisdom theory file |
| `SRT_AI_03_Consciousness_Framework.md` | 1347 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | AI consciousness framework owner; has existing Quick Reference |
| `SRT_AI_Architecture.md` | 1273 | Current Reading Map, Dependency Map, Companion Links, Refactor Notes | Transformer/architecture analysis owner |
| `_SRT_AI_Bridge.md` | 676 | Current Reading Map, Dependency Map (with Used-by list), Companion Links, Refactor Notes | Bridge layer foundation; upstream of all AI/* owner files |

### 1.3 Operations/

| File | Action | Notes |
|---|---|---|
| `Operations/PR_A_Neuroscience_AI_Navigation_Audit.md` | Created (this file) | Audit record for PR-A |

---

## 2. Files Scanned but NOT Modified

### 2.1 Neuroscience/ — scanned, not modified

| File | Lines | Reason not modified |
|---|---|---|
| `NEUROSCIENCE_COMPACT_REGISTRY.md` | 138 | Registry/index file — no navigation addition needed |
| `README.md` | 43 | Directory index — no navigation addition needed |
| `SRT_Neural_Mechanisms_CompactCore.md` | 400 | Already hardened compact entry — do not modify |
| `SRT_Consciousness_Mechanisms_CompactCore.md` | 329 | Already hardened compact entry — do not modify |
| `SRT_Neuro_Axioms_Claim_Status.md` | 212 | Claim status file — already well-scoped |
| `SRT_Neuro_Predictions_Table.md` | 409 | Predictions table — already well-scoped |
| `SRT_Neuro_Experiments.md` | 745 | Experimental protocols — scoped correctly |
| `SRT_Neuroscience_Hardening_N1_N9_v0_1.md` | 347 | Recent hardening file — do not modify |
| `SRT_Neuroscience_Hardening_N10_BTSP_v0_1.md` | 228 | Recent hardening file — do not modify |
| `SRT_Neuroscience_Hardening_N11_Transition_Field_Subjective_Time_v0_1.md` | 406 | Recent hardening file — do not modify |
| `SRT_Neuroscience_Hardening_N12_Astrocyte_Plastic_Networks_v0_1.md` | 311 | Recent hardening file — do not modify |

### 2.2 AI/ — scanned, not modified

| File | Lines | Reason not modified |
|---|---|---|
| `AI_POSITIONING_NOTE.md` | 63 | Architecture-state reference note — already well-scoped |
| `SRT_AI_01_Ontology_CompactCore.md` | 265 | Compact entry — do not modify |
| `SRT_AI_03_Consciousness_Framework_CompactCore.md` | 244 | Compact entry — PH-SS hardened — do not modify |
| `SRT_AI_Architecture_CompactCore.md` | 218 | Compact entry — do not modify |
| `SRT_AI_Consciousness_Evaluation_Rubric.md` | 521 | Operational S0-S6 rubric — already well-scoped |
| `SRT_AI_Agency_Responsibility_Note.md` | 461 | Operational A0-A3 note — already well-scoped |

### 2.3 AI/ subdirectories — scanned, not modified

The AI directory contains existing split/annex subdirectories:
- `Architecture_Split/` — already split; do not modify without PR-C scoping
- `Consciousness_Framework_Split/` — already split; do not modify without PR-C scoping
- `Ontology_Annex/` — already has Annex structure; do not modify without PR-C scoping
- `Ontology_Split/` — already split; do not modify without PR-C scoping

These subdirectories indicate PR-C work may already be partially complete in the AI domain. A separate audit of their contents is recommended before starting PR-C.

---

## 3. Files Marked "Needs Human Review"

These files were identified in the directory scan but not modified in PR-A because their internal structure and claim levels have not been fully audited:

| File | Lines | Reason for review flag | Suggested next step |
|---|---|---|---|
| `Neuroscience/SRT_Neuro_06_Field_Effects.md` | 499 | Field effects content not fully read; depends on `SRT-NEURO-05` (not found in directory) | Read file; verify claim levels; check for external theory comparisons |
| `Neuroscience/SRT_Neuro_07_Evo_Devo.md` | 757 | Evolutionary/developmental dynamics; `claim_mode: canonical` — verify this is accurate for all claims | Read full file; check whether bioelectricity / Levin comparisons are inline |
| `Neuroscience/SRT_Neuro_08_Immune_Dist.md` | 861 | Distributed systems / immune; `claim_mode: canonical` — very large file; already has Canonical Cross-Link sections | Read full file; audit claim levels for immune/gut-brain sections |
| `Neuroscience/SRT_Neuro_09_Integ_Eq.md` | 568 | Integrative equations — content not read | Read file; identify whether external theory comparisons are mixed with SRT formal equations |
| `Neuroscience/SRT_Neuro_10_Advanced_Models.md` | 474 | Advanced models — content not read | Read file; check claim levels |

**Recommendation**: Before PR-B (Neuroscience interface extraction), run a targeted audit of these 5 files to classify their sections (formal SRT claim vs. external theory interface). Do not modify them in PR-A.

---

## 4. PR-B/PR-C Annex Extraction Candidates Identified

The following interface extraction opportunities were identified and flagged in each file's Refactor Notes. None were executed in PR-A.

### 4.1 Neuroscience_Annex/ candidates (for PR-B)

| Source file | Candidate Annex file | Content to extract |
|---|---|---|
| `SRT_Clin_00_IIT_PCI.md` | `Neuroscience_Annex/01_IIT_PCI_Interface.md` | Entire file is an IIT/PCI/GNWT interface |
| `SRT_Clin_01_Pathology.md` | `Neuroscience_Annex/02_Pathology_Interface.md` | Entire file is a pathology/NDE/schizophrenia interface |
| `SRT_Clin_02_FEP.md` | `Neuroscience_Annex/03_FEP_Interface.md` | Entire file is a FEP/Active Inference interface |
| `SRT_Clin_03_DMN_Networks.md` | `Neuroscience_Annex/04_DMN_Networks_Interface.md` | Entire file is a DMN/ADHD/schizophrenia network interface |
| `SRT_Neural_Mechanisms.md` (Part B) | `Neuroscience_Annex/05_Neural_Theory_Comparisons.md` | Part B external theory comparisons only |
| `SRT_Consciousness_Mechanisms.md` (Part B) | `Neuroscience_Annex/06_Consciousness_Theory_Comparisons.md` | Part B GWT/IIT/higher-order comparisons only |

**Important**: The 4 Clin files are entirely bridge/interface files and strong PR-B candidates. The Neural Mechanisms and Consciousness Mechanisms Part B sections require careful boundary identification before extraction.

### 4.2 AI_Annex/ candidates (for PR-C)

**Note**: The AI directory already has `Architecture_Split/`, `Consciousness_Framework_Split/`, `Ontology_Annex/`, and `Ontology_Split/` subdirectories. PR-C scoping should first audit whether these existing splits already cover the extraction candidates.

| Source file | Candidate Annex file | Content to extract |
|---|---|---|
| `SRT_AI_01_Ontology.md` (Part B) | `AI_Annex/01_LLM_Capability_Comparison.md` | Part B LLM capability comparison sections |
| `SRT_AI_03_Consciousness_Framework.md` (Part B) | `AI_Annex/02_AI_Consciousness_Theory_Comparisons.md` | Part B external AI consciousness theory comparisons |
| `SRT_AI_Architecture.md` (Part B) | `AI_Annex/03_Architecture_Theory_Comparisons.md` | Part B transformer/scaling comparisons |

---

## 5. Safety Record

This PR confirms:

- [ ] No formulas changed.
- [ ] No theory content changed (no additions, deletions, or rewriting of Part A or Part B body text).
- [ ] No files moved or deleted.
- [ ] No Annex directories created (`Neuroscience_Annex/` and `AI_Annex/` do not exist yet).
- [ ] S0-S6 subjecthood thresholds unchanged.
- [ ] L0/L1/L2, Ψ_f, d-value, Ĝ_θ, T_dir canonical definitions unchanged.
- [ ] CompactCore files not modified.
- [ ] PH-SS hardened files (`SRT_AI_03_Consciousness_Framework_CompactCore.md`) not modified.
- [ ] Core/, Core_Law/, Philosophy/, Papers/, Public/, graphify-out/ directories not touched.
- [ ] All added navigation blocks are plainly labeled as "navigation-only update."
- [ ] All Refactor Notes in modified files explicitly state that extraction must occur in a separate PR after human review.

---

## 6. Discovered: AI Directory Already Has Split Structure

During scanning, it was found that the AI/ directory already contains subdirectories created in a prior split pass:
- `Architecture_Split/`
- `Consciousness_Framework_Split/`
- `Ontology_Annex/`
- `Ontology_Split/`

**Implication for PR-C**: Before executing PR-C (AI interface extraction), a targeted audit of these split subdirectories is needed to determine:
1. Whether they already contain the interface content that PR-C would create.
2. Whether their frontmatter and guardrails are consistent with the standards established in PR #43.
3. Whether the owner files' navigation should point to these existing splits.

This is a **medium-priority follow-up** that should occur before PR-C begins.

---

## 7. Next Recommended PR

**PR-B: Neuroscience_Clin interface extraction**

Start with the 4 `SRT_Clin_*` files, which are the cleanest and most clearly scoped bridge/interface files in the Neuroscience domain. Each one is an entire-file interface; extraction is simpler than partial-file extraction.

Prerequisites for PR-B:
1. PR-A merged (done after this PR).
2. Human review of proposed Neuroscience_Annex/ structure.
3. Audit of `SRT_Neuro_06_Field_Effects.md` through `SRT_Neuro_10_Advanced_Models.md` (flagged as Needs Human Review above).
4. Decision on whether `SRT_Neural_Mechanisms.md` and `SRT_Consciousness_Mechanisms.md` Part B comparisons will be extracted or left in place.
