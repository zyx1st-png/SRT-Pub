---
id: SRT-PHIL-LONG-FILES-REORGANIZATION-PLAN-2026-04-27
type: reorganization_plan
tags:
  - Philosophy
  - Foundations
  - Axioms
  - Reorganization
  - Audit
  - Safe-Patching
  - Legacy-Preservation
  - PH-SS
status: plan_v1
layer: meta
epistemic_layer: bridge
claim_mode: plan
claim_level: P5
canonical: false
date: 2026-04-27
dependency:
  - Philosophy/SRT_Philosophy_Foundations.md
  - Philosophy/_SRT_Phil_Axioms.md
  - Philosophy/SRT_Philosophy_Foundations_CompactCore.md
  - Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md
  - Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
machine_summary: >
  Audit plan for optional deeper reorganization of SRT_Philosophy_Foundations.md (2056 lines)
  and _SRT_Phil_Axioms.md (379 lines). Records current structure, proposed Part A/B/C/D/E
  target mapping, safe vs risky patch sequence, and what not to touch. Mode 2 small structure
  notes (future-target comments, Part C/D anchors) have been added; full content reorganization
  is not yet executed and remains optional.
---

# Long Foundations + Axioms Reorganization Plan — 2026-04-27

> **Status**: Audit + Mode 2 structure notes only. Full content reorganization (moving blocks) is not yet executed.  
> **Purpose**: Map current section structure to the Part A/B/C/D/E target shape and identify safe vs risky future moves.  
> **Safety rule**: Do not delete any section. Do not move large blocks without a separate review pass.

---

## 0. Target structure

```text
Part A — Current Hardened Reading
Part B — Formal / Semi-formal Claims
Part C — Tradition Interface
Part D — Objection and Withdrawal Conditions
Part E — Legacy Notes / Preserved Drafts
```

---

## 1. `SRT_Philosophy_Foundations.md` (2056 lines)

### 1.1 Current section map

| Lines | Section | Proposed target | Safe to relabel? | Risk |
|---|---|---|---|---|
| 1–85 | Navigation: frontmatter, Quick Reference, Terminology, PH-SS Pointer, Reading Map, Companion Links | Part A (current entry) | already done | low |
| 86–213 | Part A: Domain Mapping Axioms (Ax-PhilF-1..7, H-PhilF-1, T-PhilF-2..7) | Part B: Formal / Semi-formal Claims | yes — Part A label is close enough; longer term rename to Part B | low |
| 215–338 | Axiom Mapping, Formal Bridge (Def 2.1/2.2), Theoretical Derivations (§3.1–3.4), Experimental Predictions | Part B: Formal / Semi-formal Claims | yes — add comment | low |
| 339 | Legacy marker: "SRT Philosophical Foundations: Axiomatic Epistemology" | Part E: Legacy Notes | already marked | done |
| 350 | "Part B: Expanded Theoretical Discourse" header | current label; future: split into Parts B/C/D | no large move yet | medium |
| 354–395 | §1 Explanatory Gap, §2 SRT advantages | Part B: Formal / Semi-formal Claims | pointer only | low |
| 396–437 | §3 Saturation / Marion gift paradox / Nagarjuna | Part C: Tradition Interface | pointer only | low |
| 438–557 | §4 Classic paradoxes (quantum, game theory, language, time, consciousness, cosmology) | Part C: Tradition Interface (with some Part B formal material) | pointer only | medium — paradox resolution contains formal claims |
| 558–1293 | §5 SRT Metaphysics Extensions (Spinoza, Kant, eliminativism, realism/idealism, FEP, Sorites, representation, Sellars) | Part C: Tradition Interface | pointer only | medium — §5.9–5.12 contain formal definitions |
| 1295–2041 | Interface sections: Synchronicity, Wittgenstein, Qualia, Daoism, Quantum-Consciousness, Epistemic Delegation, Mental Representation, Concepts, Self-Consciousness, Mind-Body | Part C: Tradition Interface | anchor added (Mode 2) | low — clearly tradition interface |
| 2042–2056 | Hardest Objections | Part D: Objection and Withdrawal Conditions | anchor added (Mode 2) | low |

### 1.2 Sections safe to relabel (Mode 2 only — no content move)

```text
Lines 1–85: already done (Current Reading Map + future-target added)
Line 339: already marked legacy
Lines 1295–2041: Part C anchor added (interface sections clearly tradition interface)
Lines 2042–2056: Part D anchor added (Hardest Objections clearly objection material)
```

### 1.3 Sections risky to move (do not move without full review)

```text
Lines 86–213: Part A formal axioms — relabeling low risk, moving content medium risk
Lines 215–338: formal bridge and derivations — closely tied to Part A; don't separate without careful review
Lines 354–437: §1–3 contain both formal claims and tradition interface — boundary is unclear
Lines 438–1293: §4–5 contain mixed formal + tradition material; §5.9–5.12 especially have formal definitions
```

### 1.4 What not to touch

```text
Formulas — do not alter
Frontmatter — do not change status or canonical fields
PH-SS guardrail pointer section — do not remove or replace
Current Reading Map — only extend with future-target note (done)
Companion Links — do not remove
Legacy markers (line 339) — preserve
Formula-role labels — preserve all from first and second pass
```

### 1.5 Recommended patch sequence (future)

```text
Step 1 (done): Add future-target structure note to Current Reading Map
Step 2 (done): Add Part C anchor before Synchronicity Interface (line 1295)
Step 3 (done): Add Part D anchor before Hardest Objections (line 2042)
Step 4 (optional, separate review): Add Part E anchor around line 339 legacy section
Step 5 (optional, long-term): Reorganize §4 and §5 into explicit Part C within Part B
Step 6 (optional, long-term): Split Part B into separate Part B (formal) + Part C (tradition)
Step 7 (optional, long-term): Merge Hardest Objections with O-Phil-11..20 or add cross-link
```

---

## 2. `_SRT_Phil_Axioms.md` (379 lines)

### 2.1 Current section map

| Lines | Section | Proposed target | Safe to relabel? | Risk |
|---|---|---|---|---|
| 1–73 | Navigation: frontmatter, Terminology, PH-SS Pointer, Reading Map, Guardrail Links | Part A (current entry) | already done | low |
| 74–191 | Part A: Domain Mapping Axioms (Ax-Phil-1..6, H-Phil-Ineffability, T-Phil-2..4) | Part B: Formal / Semi-formal Claims | Part A label close enough; future rename low risk | low |
| 192 | Legacy marker: "SRT Philosophical Axioms" | Part E: Legacy Notes | already marked | done |
| 201–267 | §1 Core Mapping, §2 Phil Axioms (Ax-Ph1/2), §3 Key Theorems | Part E: Legacy Notes / Preserved Drafts | pointer only | low |
| 268 | "Part B: Expanded Theoretical Discourse" | current label covers | pointer only | low |
| 269–308 | §1–6 Explanatory gap, SRT advantages, saturation, paradox, mechanisms, cost/risk, falsifiable predictions | Part B: Formal Claims + Part C: Tradition Interface mixed | pointer only | medium |
| 309–340 | 融合映射整合 (2026-02-14): panpsychism, subject identity, unity | Part C: Tradition Interface | pointer only | low |
| 342–372 | 信念与反紧缩条款 (2026-03-06): Ax-Phil-7, T-Phil-5 | Part B: Formal Claims | pointer only | low |
| 373–379 | 理论边界/防误用声明, Lineage/Source | Part D: Objection / boundary | pointer only | low |

### 2.2 Safe mode-2 additions

```text
Added to Current Reading Map: future-target structure note.
No content moved. No Part C/D anchors added (file too small to need them — the sections are readable as-is).
```

### 2.3 What not to touch

```text
Formulas — do not alter
Frontmatter — do not change
PH-SS guardrail pointer — preserve
Current Reading Map — only extended with future-target (done)
Legacy markers (line 192) — preserve
Formula-role labels (T-Phil-3, Ax-Ph1 labels from first pass) — preserve
```

### 2.4 Recommended patch sequence (future)

```text
Step 1 (done): Add future-target structure note to Current Reading Map
Step 2 (optional): Add Part E anchor around lines 192–267 legacy section
Step 3 (optional): Add Part C anchor before 融合映射整合 section
Step 4 (optional, long-term): Merge Part A formal axioms with Part B §1–6 into unified formal section
Step 5 (optional, long-term): Companion-to-owner merge of _SRT_Phil_Axioms_PH_SS_Guardrails.md guardrail definitions
```

---

## 3. Safety audit

| Check | Foundations.md | Axioms.md |
|---|---|---|
| Large block moves | none | none |
| Formula changes | none | none |
| Deletions | none | none |
| Canonical status promotion | none | none |
| Legacy material deleted | no — all preserved | no — all preserved |
| PH-SS pointer removed | no | no |
| Companion links removed | no | no |

---

## 4. Current state after Mode 2 patches

### `SRT_Philosophy_Foundations.md`

```text
Current Reading Map: extended with future-target structure (Part A/B/C/D/E)
Part C anchor: added before Synchronicity Interface (line 1295)
Part D anchor: added before Hardest Objections (line 2042)
```

### `_SRT_Phil_Axioms.md`

```text
Current Reading Map: extended with future-target structure (Part A/B/C/D/E)
No Part C/D anchors needed (file is short enough)
```

---

## 5. What is NOT done (deep reorganization still pending)

```text
Moving large content blocks to match Part B/C/D target
Splitting Part B into separate Part B and Part C sections
Deduplicating overlapping explanatory gap / paradox material between Foundations and Axioms
Full companion-to-owner merge
Full legacy deduplication
```

These remain optional and should be done only after a human review pass.
