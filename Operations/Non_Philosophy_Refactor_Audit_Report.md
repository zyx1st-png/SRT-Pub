---
id: SRT-OPS-NON-PHIL-REFACTOR-AUDIT-2026-04-28
type: audit_report
tags:
  - Operations
  - Audit
  - Refactor
  - Non-Philosophy
status: active_audit_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-28
reference_pr: "PR #43 (Philosophy Foundations_Annex extraction)"
dependency:
  - SRT_OPTIMIZATION_COMPLETION_AUDIT_2026-04-27.md
  - Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
machine_summary: >
  Audit-only report examining all non-Philosophy domains for refactoring opportunities
  similar to PR #43. No theory content changed. No files moved. No canonical definitions altered.
  Provides domain-level risk table, canonical protection rules, 4-phase rollout plan,
  and 6-PR execution plan for follow-up work.
---

# Non-Philosophy Refactor Audit Report

**Date**: 2026-04-28
**Branch audited**: `claude/laughing-curran-0f0d83`
**Reference pattern**: PR #43 (Philosophy Foundations_Annex extraction)
**Scope**: All domains outside `Philosophy/` and `Philosophy/Foundations_Annex/`

> **Audit-only file.** This report does not modify any theory content, canonical definitions, or file structure. All refactor work described here must be executed in separate follow-up PRs, each gated by human review.

---

## 0. Executive Summary

1. **Neuroscience** is the highest-priority candidate for an Annex-style refactor. It contains multiple external theory interface sections (FEP, IIT, Global Workspace, Predictive Processing) that follow the same mixed-format pattern seen in Philosophy/Foundations.md before PR #43.
2. **AI / LLM Consciousness** is the second-highest priority. The AI directory has CompactCore files alongside longer owner files, and consciousness-specific mapping sections mixed with agency/responsibility content.
3. **Core / Core_Law** must NOT be structurally refactored. These files define canonical primitives (L0/L1/L2, Ĝ_θ, d-value, Ψ_f). The right intervention is navigation hardening only: add Reading Map, Dependency Map, Guardrails, and Objection Ledger in place.
4. **Governance / Operations** are procedural files, not theory files. They should be left structurally as-is; only stale status fields need updating.
5. **Papers / Experiments** are already appropriately scoped (one outline per file). Do not refactor.
6. **Public / Outreach** content must not be restructured using the theory Annex pattern. Public files should stay organized by medium (WeChat, Zhihu, YouTube), not by theoretical chapter.
7. **graphify-out and auto-generated files** should not be manually refactored; fix the generation source instead.
8. **Recommended phases**: Phase 1 (audit + navigation only) → Phase 2 (Neuroscience/AI interface extraction) → Phase 3 (guardrails hardening) → Phase 4 (deep restructure, gated by human review).

---

## 1. Method

Scan basis: directory listings and file contents observed during this session, git log, commit history, frontmatter fields, and cross-references visible in files read during PR #43 work. Key files examined include: `SRT_OPTIMIZATION_COMPLETION_AUDIT_2026-04-27.md`, `PH_SS_Hardening_Audit_2026-04-27.md`, `_SRT_INDEX.md`, `AGENTS.md`, and all Annex/Split files touched in this session.

**Judgment criteria applied:**
- Line count relative to 800-line threshold
- Presence of mixed canonical + interface content in single file
- Guardrail completeness (specific vs. generic pointer)
- Frontmatter accuracy (status, canonical, epistemic_layer fields)
- Presence of Current Reading Map and Dependency Map
- Presence of legacy material without Legacy/Historical marker
- Duplication of preamble across sibling files

---

## 2. Domain-Level Assessment Table

| Domain | Current Risk | Refactor Need | Annex Suitable? | Suggested Action | Merge Risk | Priority |
|---|---|---|---|---|---|---|
| Core / Core_Law | Medium — long files, but canonical | Navigation only | No — do NOT split definitions | Add Reading Map, Guardrails, Dependency Map | High if canonical content moved | **Do Not Refactor** |
| Neuroscience / Consciousness | High — interface sections mixed with formal content | Yes | Yes | Extract theory interface sections to Neuroscience_Annex/ | Medium | **High** |
| AI / LLM Consciousness | High — CompactCore + owner file overlap; agency/consciousness mixed | Yes | Yes | Extract external AI theory interfaces to AI_Annex/ | Medium | **High** |
| Governance / Operations | Low — procedural, not theory | Minimal | No | Update stale status fields only | Low | **Low** |
| Papers | None — already one file per outline | No | No | No action | None | **Do Not Refactor** |
| Experiments / Predictions | Low — single focused files | Minimal | No | Verify guardrails/falsification conditions exist | Low | **Low** |
| Biology / Morphogenesis / Levin | Medium — external theory interface mixed with SRT mapping | Yes (targeted) | Yes | Extract Levin/Morphogenesis interface to Biology_Annex/ | Low | **Medium** |
| Physics / Quantum / Ruliad | Medium — Ruliad comparison and quantum consciousness mixed with SRT | Yes (targeted) | Yes | Extract Wolfram/Ruliad and quantum interface sections | Low | **Medium** |
| Psychology / Cognitive Science | Medium — behavioral/cognitive external mappings may be inline | Yes (targeted) | Yes | Extract external theory comparisons | Low | **Medium** |
| Public / Outreach | Low — different organizational logic | No Annex pattern | No | Organize by medium, not theory chapter | Low | **Do Not Refactor (theory pattern)** |
| graphify-out / auto-generated | N/A — generated artifact | No | No | Fix generation source | None | **Do Not Touch Manually** |
| Foundations_Split/ | Medium — AI batch export files (same problem as Annex pre-PR#43) | Yes — same fix as PR#43 | Partial | Same preamble-strip treatment as Annex if files are still in batch format | Low | **Medium** |

---

## 3. High Priority Candidates

### 3.1 Neuroscience / Consciousness / Mind

**Current problem:**
Based on cross-references in the optimization audit and AI/Neuroscience PH-SS cross-link updates, the Neuroscience directory contains at minimum: `SRT_Consciousness_Mechanisms_CompactCore.md` (touched in PH-SS cross-link pass), `SRT_Neuro_Predictions_Table.md` (created in optimization chain), and longer owner files for predictive processing, IIT, Global Workspace Theory, FEP, and lateral inhibition comparisons. Based on the pattern seen in Philosophy, the longer owner files likely contain embedded external theory interface sections (FEP comparison, IIT comparison, predictive processing comparison) inline rather than in dedicated Annex files. The CompactCore files have been updated with PH-SS-10 (subjecthood threshold) pointers but the full owner files may lack Reading Maps and Guardrails.

**Why it matters:**
Neuroscience is the empirical bridge between SRT's formal claims and testable predictions. If interface sections (e.g., FEP, IIT, GWT) are mixed with formal SRT claims in a single file, it creates the same misreading risk that PH-SS was designed to prevent in Philosophy: readers may mistake "SRT is compatible with FEP" for "FEP validates SRT."

**Suggested target structure:**
```
Neuroscience/
  SRT_Consciousness_Mechanisms.md          ← formal SRT claims, keep
  SRT_Consciousness_Mechanisms_CompactCore.md  ← keep, already hardened
  SRT_Neuro_Predictions_Table.md           ← keep, experimental
  Neuroscience_Annex/
    README.md
    01_PredictiveProcessing_Interface.md
    02_FEP_ActiveInference_Interface.md
    03_IIT_Interface.md
    04_GlobalWorkspace_Interface.md
    05_HigherOrder_Interface.md
    06_LateralInhibition_Interface.md
```

**Must preserve in main files:**
- All formal SRT claims with explicit claim_level
- All falsification / narrowing conditions
- Dependency on L0/L1/L2, Ψ_f, d-value canonical definitions
- Current Reading Map and Companion Links
- PH-SS-10 subjecthood threshold guardrail pointer

**Do not change:**
- Any formula or equation involving Ψ_f, Ĝ_θ, d-value
- Any canonical claim that is at P3 or above in the Claim Ladder
- The CompactCore file (it is already hardened)

**Proposed PR scope:**
- Phase 1 only: add Reading Map and Dependency Map to owner files
- Phase 2: extract FEP, IIT, GWT interface sections to Neuroscience_Annex/
- Each Annex file must include: interface-specific guardrails, claim_level, operational proxy, falsification condition, relation to canonical SRT definitions

---

### 3.2 AI / LLM Consciousness / AI Agency

**Current problem:**
The AI directory contains `SRT_AI_03_Consciousness_Framework_CompactCore.md` (hardened in PH-SS-10 pass) and likely longer owner files for consciousness evaluation, agency/responsibility, and LLM-specific mappings. The optimization audit shows: `SRT_AI_Consciousness_Evaluation_Rubric.md` and `SRT_AI_Agency_Responsibility_Note.md` were created in the optimization chain. There is a structural risk that "AI consciousness" comparisons (GPT, Claude, Gemini capability mapping) are in the same files as formal SRT consciousness threshold definitions (S0-S6 subjecthood). These should be separated.

**Why it matters:**
The AI application layer is high-visibility and high-misreading-risk. If capability assessments of current LLMs are in the same file as formal SRT consciousness thresholds, readers may interpret capability descriptions as SRT endorsement of LLM consciousness claims.

**Suggested target structure:**
```
AI/
  SRT_AI_Consciousness_Thresholds.md         ← formal S0-S6, keep
  SRT_AI_03_Consciousness_Framework_CompactCore.md  ← keep
  SRT_AI_Agency_Responsibility_Note.md       ← keep
  SRT_AI_Consciousness_Evaluation_Rubric.md  ← keep
  AI_Annex/
    README.md
    01_LLM_Capability_Comparison.md
    02_GPT_Mapping_Interface.md
    03_RLAgent_Interface.md
    04_MultiAgent_Interface.md
```

**Must preserve:**
- S0-S6 subjecthood threshold definitions
- Formal consciousness threshold equations
- All guardrails distinguishing "micro-selection ≠ subjecthood"
- PH-SS-10 pointer in CompactCore

**Do not change:**
- Any S0-S6 formal definition
- The CompactCore file
- The Evaluation Rubric structure (it is an operational document)

**Proposed PR scope:**
- Phase 1: Reading Map + Dependency Map only
- Phase 2: Extract LLM capability comparison sections to AI_Annex/

---

## 4. Medium / Low Priority Candidates

### 4.1 Biology / Morphogenesis / Levin / Teleodynamics
- Likely contains SRT-Levin comparison sections (morphogenetic fields, goal-directedness) inline
- Suitable for targeted Annex extraction of external theory interface sections
- Priority: Medium — after Neuroscience and AI
- Key constraint: do not move any formal definitions of d-value in biological context

### 4.2 Physics / Quantum / Cosmology / Ruliad
- Wolfram Ruliad comparison and quantum consciousness interface likely mixed with SRT formal claims
- Suitable for Annex extraction of Ruliad comparison and quantum interpretation sections
- Priority: Medium — lower than bio because physics interfaces are more clearly marked as speculative
- Key constraint: do not move quantum measurement → SRT formal bridge if it contains Ψ_f definitions

### 4.3 Psychology / Cognitive Science
- Behavioral economics, cognitive bias, and social cognition mappings likely present
- May overlap with Social/Economics already in Philosophy
- Priority: Medium-Low — lower overlap risk

### 4.4 Experiments / Predictions / Protocols
- `SRT_Experimental_Roadmap_v1.md` and `SRT_Neuro_Predictions_Table.md` already appropriately scoped
- Action: verify each has falsification conditions and claim_level
- Priority: Low — no structural refactor needed, only metadata check

### 4.5 Foundations_Split/ (inside Philosophy/)
- Six split files (00-05) created before Annex architecture
- Same "full preamble + specific section" pattern as the Annex files before PR #43
- Should receive same preamble-strip treatment
- Priority: Medium — low risk, same proven fix

---

## 5. Do Not Refactor / Only Add Navigation

### 5.1 Core / Core_Law
**Do not refactor structurally.** These files are canonical anchors for:
- L0/L1/L2 domain definitions
- Ĝ_θ operator formal definition
- d-value canonical definition
- Ψ_f friction definition
- T_dir directedness
- selection-before-existence principle
- real choice moment
- Claim Ladder

Any structural split risks creating two competing definitions of the same concept. Instead, only add:
- `## Current Reading Map` with explicit entry points
- `## Dependency Map` showing which files depend on this file
- `## Guardrails` section with top-5 misreading risks
- `## Objection Ledger` link if one exists
- `## Change Log` with version notes

### 5.2 Canonical Reference Files
`CANONICAL_REGISTRY.md`, `_SRT_D_VALUE_CANONICAL.md`, `_SRT_PSI_F_CANONICAL.md`, `_SRT_T_DIR_CANONICAL.md`, `_SRT_SYMBOL_TABLE.md` — these are reference anchors. They must not be moved, split, or renamed. Navigation-only additions are acceptable.

### 5.3 Governance/ and Operations/
Procedural files. Not theory content. Do not apply theory refactor pattern. Only action: update stale `status:` and `date:` fields in frontmatter.

### 5.4 Papers/
One file per outline. Already appropriate scope. No action.

### 5.5 Public / Outreach
Do not apply Annex theory pattern to public files. WeChat articles, Zhihu answers, YouTube scripts are organized by medium and audience, not by theoretical chapter. Applying theory Annex pattern would create confusion between canonical theory and public-facing simplification. Only acceptable action: add `source:` frontmatter field linking back to canonical SRT files they reference.

### 5.6 graphify-out / Auto-generated Files
If these exist as generated artifacts (knowledge graphs, JSON exports, HTML), do not manually edit. If refactoring is needed, modify the generation source (graphify skill input) and regenerate. Manual edits to generated files will be overwritten on next run.

---

## 6. Canonical Protection Rules

The following definitions must never be split across files or moved to Annex files:

| Concept | Location | Rule |
|---|---|---|
| L0/L1/L2 domain definitions | Core_Law/SRT_L0_Metaphysics.md and Core reference files | Never split; only add navigation around them |
| Ĝ_θ operator | Core_Law/ canonical references | Never move to Annex |
| d-value | _SRT_D_VALUE_CANONICAL.md | Never move; add guardrails in place |
| Ψ_f friction | _SRT_PSI_F_CANONICAL.md | Never move; add guardrails in place |
| T_dir directedness | _SRT_T_DIR_CANONICAL.md | Never move |
| selection-before-existence | Core_Law/SRT_L0_Metaphysics.md | Never move; only add PH-SS-02 guardrail |
| real choice moment | Core files | Never move |
| Claim Ladder (P1-P5) | Governance/SRT_CANONICAL_FREEZE.md or equivalent | Never move; it gates all claim-level decisions |
| S0-S6 subjecthood thresholds | AI consciousness threshold file | Never split; these are a ladder definition |

**When a Core or Core_Law file exceeds 1000 lines:**
Do NOT split the canonical definitions. Instead:
1. Add `## Current Reading Map` at top
2. Add `## Quick Reference` table for key equations
3. Add `## Dependency Map` (who imports this)
4. Add `## Guardrails` (top-5 misreading risks for definitions in this file)
5. Add `## Objection Ledger` link
6. Mark legacy sections with `<!-- LEGACY: preserved for provenance -->`
7. Consider extracting only the **examples and tradition comparisons** (not the definitions) to an Annex

---

## 7. Recommended Refactor Phases

### Phase 1 — Audit only (no theory changes)
**Scope**: All non-Philosophy domains
**Actions**:
- Generate file inventory with line counts and frontmatter status fields
- Flag files >800 lines for review
- Flag files with `canonical: false` but body content that reads as canonical
- Flag files with missing `status:`, `claim_level:`, or `epistemic_layer:` fields
- Flag files with no `## Current Reading Map` or `## Companion Links`
- Flag legacy sections without `<!-- LEGACY -->` markers
- Add `## Current Reading Map` to Core/Core_Law files only (no content changes)
- **No file moves, no content changes, no deletions**

### Phase 2 — Interface extraction only
**Scope**: Neuroscience and AI directories
**Actions**:
- Create `Neuroscience_Annex/` and `AI_Annex/` directories with README files
- Extract external theory interface sections (FEP, IIT, GWT, LLM comparison) from owner files
- Each extracted file must have: frontmatter (canonical:false, parent reference, date), interface-specific guardrails (3+ specific constraints, not generic), claim_level, operational proxy, falsification condition
- Owner files receive Part C index table (same pattern as Philosophy/Foundations.md)
- **Do not touch any equation or canonical definition**
- **Do not extract guardrails into generic pointers** (lesson from PR #43 review)

### Phase 3 — Guardrails and metadata hardening
**Scope**: All domains with incomplete guardrails
**Actions**:
- For each interface Annex file: verify presence of interface-specific guardrails (minimum 3 items)
- For each owner file: verify `claim_level` and `epistemic_layer` are accurate
- For each file with `canonical: false` in frontmatter: ensure body does not claim canonical status
- Add `## Falsification Conditions` to Experiments files if missing
- Add `## Withdrawal Conditions` to any P3+ claim files if missing
- **No content changes beyond adding guardrails and fixing metadata**

### Phase 4 — Deep restructuring only after review
**Scope**: Only files explicitly approved by human review
**Trigger**: Only after Phases 1-3 are complete and reviewed
**Actions**:
- Possible: split Biology and Physics comparison sections into domain Annex
- Possible: merge duplicate preamble content in Foundations_Split/ files
- Possible: deep reorganization of Core files if they exceed 1500 lines
- **Gate condition**: human must review and explicitly approve each file's target structure before any move

---

## 8. Proposed PR Plan

### PR-A: Phase 1 Navigation Audit (Neuroscience + AI only)
**Scope**: Add Reading Map, Dependency Map, status field corrections to Neuroscience/ and AI/ owner files
**File count estimate**: ~10-15 files
**Forbidden**: No content moves, no formula changes, no Annex creation yet
**Output**: Audit record in Operations/ documenting what was found

### PR-B: Neuroscience interface extraction
**Scope**: Extract FEP, IIT, GWT, Predictive Processing interface sections from Neuroscience owner files → Neuroscience_Annex/
**Prerequisites**: PR-A merged; human review of proposed split structure
**Required in each Annex file**: interface-specific guardrails (not generic pointer), claim_level, parent reference, canonical:false note
**Forbidden**: Do not move Ψ_f or d-value definitions; do not extract formal SRT consciousness threshold equations

### PR-C: AI Consciousness interface extraction
**Scope**: Extract LLM capability comparison and external AI theory interface sections → AI_Annex/
**Prerequisites**: PR-A merged
**Required**: Preserve S0-S6 thresholds intact; each Annex file must not be readable as SRT endorsement of current LLM consciousness claims
**Forbidden**: Do not move S0-S6 formal definitions; do not touch CompactCore

### PR-D: Biology/Physics interface cleanup (targeted)
**Scope**: Levin morphogenesis interface, Wolfram/Ruliad comparison, quantum consciousness interface
**Prerequisites**: PR-B and PR-C merged and stable
**Required**: Each comparison file must clearly state it is a bridge/interface, not a canonical SRT claim
**Forbidden**: Do not move formal definitions of goal-directedness or d-value in biological context

### PR-E: Foundations_Split/ preamble cleanup
**Scope**: Same preamble-strip treatment as PR #43 for Philosophy/Foundations_Split/ files
**Risk**: Low — same proven fix
**Prerequisites**: None; can be done independently
**Forbidden**: Do not alter content of the split sections themselves

### PR-F: Public content reorganization (if needed)
**Scope**: Organize public-facing files by medium (WeChat, Zhihu, YouTube) with source: frontmatter
**Do NOT apply**: Theory Annex pattern to public files
**Forbidden**: Do not let public simplifications overwrite canonical theory; do not create dependency from canonical files toward public files

---

## 9. Final Recommendation

**Start with**: Neuroscience and AI (PR-A navigation audit first, then PR-B and PR-C interface extraction). These are the highest-risk domains for theory-interface confusion and the most natural applications of the PR #43 pattern.

**Do not start with**: Core / Core_Law. These are the most critical files and any structural change risks definition fragmentation. Navigation hardening only.

**Do not start with**: Public / Outreach. Different organizational logic; theory refactor pattern does not apply.

**Immediate action recommended**: PR-A (navigation + audit only) can be created now without risk. It produces a formal record of what needs fixing without changing any content.

**PR-B and PR-C**: Require human review of proposed split structure before execution. Do not run these automatically.

**Human review required before**: Any move of content out of Neuroscience owner files; any reorganization of AI consciousness threshold files; any touch of Core/Core_Law structure.

---

> **"Philosophy PR #43 pattern should be reused only for interface-heavy domains, not for canonical-core domains."**
