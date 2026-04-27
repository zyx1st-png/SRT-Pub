---
id: SRT-PHIL-PH-SS-HARDENING-EXECUTION-PLAN-2026-04-27
type: execution_plan
tags:
  - Philosophy
  - Hardening
  - Execution-Plan
  - Soft-Spots
  - PH-SS
  - Machine-Readable
status: active_bridge_hardening
layer: L1-L2-bridge
epistemic_layer: bridge
claim_mode: plan
claim_level: P5
canonical: false
priority: high
visibility: read_after_01
date: 2026-04-27
dependency:
  - SRT-PHIL-HARDENING-SOFT-SPOTS-2026-04-27
  - SRT-PHIL-PH-SS-OBJECTION-CROSSWALK-2026-04-27
  - SRT-PHILOSOPHY-README
  - SRT-PHIL-HARDENING-TODO
machine_summary: >
  Execution plan that turns the PH-SS-01..PH-SS-12 philosophy soft spots into
  sequential repository edits: quick guardrails, foundations patch, axiom patch,
  objection ledger expansion, ethics/social ontology hardening, and validation pass.
---

# 02 — PH-SS Hardening Execution Plan

> **用途**：把哲学软点补丁从“好读的地图”转成后续可执行的仓库任务。  
> **定位**：计划文件，不定义理论。所有 P0/P1 仍归 Core / Core_Law / canonical files。

---

## 0. Execution summary

```yaml
execution_plan:
  goal: "Make the philosophy layer easier for humans and agents to read, harder to misread, and easier to upgrade without overclaiming."
  phases:
    - phase_0_navigation_visibility
    - phase_1_compact_foundations_patch
    - phase_2_axiom_guardrails
    - phase_3_objection_ledger_expansion
    - phase_4_ethics_normativity_patch
    - phase_5_social_ontology_patch
    - phase_6_non_reductive_validation_patch
    - phase_7_long_foundations_refactor
  done_when:
    - "Every major philosophy file points to the PH-SS map or its derived guardrails."
    - "Every strong selection / reality / value / consciousness claim has layer, cost, threshold, and withdrawal condition."
    - "SRT is visibly framed as selection realism + layered realism, not idealism, relativism, or mystical teleology."
```

---

## Phase 0 — Navigation visibility

**Status**: mostly done.

| Task | Files | Done condition |
|---|---|---|
| Add read-first soft-point file | `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md` | Exists with YAML + machine summary + PH-SS table |
| Add crosswalk file | `Philosophy/01_PH_SS_Objection_Crosswalk.md` | Exists with PH-SS → objection mapping |
| Add execution plan | `Philosophy/02_PH_SS_Hardening_Execution_Plan.md` | This file exists |
| Promote in Philosophy README | `Philosophy/README.md` | Reading path includes 00 / 01 / 02 |
| Promote in machine index | `_SRT_INDEX.md` | Domain entrypoints and machine notes include 00 / 01 / 02 |

---

## Phase 1 — Compact Foundations patch

**Target file**: `Philosophy/SRT_Philosophy_Foundations_CompactCore.md`

### Insert / update blocks

| Block | Purpose | PH-SS |
|---|---|---|
| `Selection Realism` | clarify SRT is not idealism, not physicalism, not panpsychism | PH-SS-04, PH-SS-12 |
| `Layered Realism` | make reality-strength ladder explicit | PH-SS-03 |
| `L0 as Modal Field of Selectability` | avoid hidden-world misread | PH-SS-01 |
| `Manifestational Priority` | clarify selection-before-existence | PH-SS-02 |
| `Purpose as High-d Attractor` | avoid mystical teleology | PH-SS-07 |
| `d-value Philosophical Reading` | avoid preference-reduction | PH-SS-08 |
| `Non-Reductive Validation` | avoid unfalsifiability | PH-SS-11 |

### Done condition

The compact core should contain this exact guardrail set in visible form:

```text
L0 is not a hidden object-world;
selection-before-existence is manifestational, not temporal;
theta is not subjective will;
Psi_f is not a single cost;
stabilization is not moral justification;
selected reality is not relativism;
not all selection is consciousness.
```

---

## Phase 2 — Axiom guardrails

**Target file**: `Philosophy/_SRT_Phil_Axioms.md`

### Required additions

| Proposed item | Content | PH-SS |
|---|---|---|
| `Def-Phil-L0-Selectability` | `L_0` as modal field of selectability / condition of possible manifestation | PH-SS-01 |
| `Def-Phil-Manifestational-Priority` | selection-before-existence is logical/generative, not temporal | PH-SS-02 |
| `Def-Phil-Reality-Strength` | E1/E2/E3/E4 reality strength levels | PH-SS-03 |
| `Def-Phil-PsiF-Layers` | `Psi_f^ont`, `Psi_f^inf`, `Psi_f^emb`, `Psi_f^norm` | PH-SS-05 |
| `Def-Phil-Normativity-Ladder` | descriptive / functional / evaluative normativity | PH-SS-06 |
| `Def-Phil-Subjecthood-Threshold` | selection event ≠ subjecthood | PH-SS-10 |

### Done condition

No axiom-like sentence should imply that:

- `L_0` is an object-like parallel world;
- selection happens before existence in chronological time;
- all selected things have the same reality strength;
- stable `L_2` means good or legitimate;
- all micro-selection is consciousness.

---

## Phase 3 — Objection Ledger expansion

**Target file**: `Philosophy/SRT_Philosophy_Objection_Ledger.md`

### Add or cross-link objections

| Proposed ID | Name | PH-SS |
|---|---|---|
| `O-Phil-11` | L0 hidden-world objection | PH-SS-01 |
| `O-Phil-12` | temporal priority objection | PH-SS-02 |
| `O-Phil-13` | reality-strength flattening objection | PH-SS-03 |
| `O-Phil-14` | Psi_f equivocation objection | PH-SS-05 |
| `O-Phil-15` | mystical teleology objection | PH-SS-07 |
| `O-Phil-16` | d-value preference-reduction objection | PH-SS-08 |
| `O-Phil-17` | social construction / institutional reification objection | PH-SS-09 |
| `O-Phil-18` | consciousness over-attribution objection | PH-SS-10 |
| `O-Phil-19` | non-reductive verification objection | PH-SS-11 |
| `O-Phil-20` | selected-reality relativism objection | PH-SS-12 |

### Done condition

Every objection entry should have:

```text
Strongest form:
What it targets:
SRT response:
Narrowing / withdrawal condition:
Editing rule:
```

---

## Phase 4 — Ethics / normativity patch

**Target files**:

- `Philosophy/SRT_Philosophy_Ethics.md`
- `Philosophy/SRT_Ethics_Agency.md`
- any ethics compact core file if present

### Required additions

| Addition | Purpose | PH-SS |
|---|---|---|
| Moral legitimacy ladder | block “stability = goodness” | PH-SS-06 |
| Hidden friction export test | detect oppression and cost-shifting | PH-SS-06, PH-SS-12 |
| Future selectability test | distinguish living norm from lethal closure | PH-SS-06 |
| Cross-subject `d-value` bandwidth | avoid single-agent value absolutism | PH-SS-08, PH-SS-09 |
| Reversibility / correction channel | avoid frozen moral `L_2` | PH-SS-06 |

### Minimal moral legitimacy ladder

```text
L0: local preference / local d-value intensity
L1: stabilized concern / repeated high-d selection
L2: shared norm / social recognition
L3: legitimate norm / preserves or expands future selectability without hidden friction export
L4: pathological norm / persists by occlusion, coercion, or asymmetric cost transfer
```

---

## Phase 5 — Social ontology patch

**Target files**:

- `Philosophy/SRT_Social_Economics_CompactCore.md`
- `Philosophy/SRT_Political_Philosophy.md`
- `Philosophy/SRT_Political_Philosophy_CompactCore.md`
- `Core_Law/SRT_Collective_Selection.md` as canonical-facing dependency only

### Required additions

| Addition | Purpose | PH-SS |
|---|---|---|
| Collective L2 definition | social facts as cross-subject stabilized selection | PH-SS-09 |
| Recognition / enforcement / memory loop | explain institutions without reducing them to individuals | PH-SS-09 |
| Money / law / identity / culture table | make social ontology legible | PH-SS-09 |
| Institutional legitimacy guardrail | block power = truth / stability = good | PH-SS-06, PH-SS-12 |
| Shared d-value | explain why society is more than coordination | PH-SS-08, PH-SS-09 |

### Minimal social ontology claim

> Social reality is not merely a sum of private beliefs and not merely a physical object. It is a collective `L_2` structure stabilized by repeated recognition, symbolic encoding, enforcement, memory, and consequence return.

---

## Phase 6 — Non-reductive validation patch

**Target files**:

- `Core/SRT_Core_24_Floor_Normativity_Verification.md`
- `Philosophy/SRT_Philosophy_Foundations_CompactCore.md`
- `Governance/SRT_CLAIM_LADDER.md` if claim-level clarification is needed

### Required additions

| Validation layer | Meaning |
|---|---|
| Direct measurement | allowed for proxies, not necessarily primitives |
| Operational proxy | measurable stand-in for `d-value`, `Psi_f`, `L2` stability, etc. |
| Cross-domain pattern | repeated selection-cost-stabilization structure across domains |
| Differential prediction | SRT predicts something FEP / IIT / GWT / RL alone does not clearly predict |
| Withdrawal condition | what would make SRT narrow, defer, or lose novelty |

### Minimal validation statement

> SRT should not require a single instrument to directly detect `L_0` or `d-value`. Its empirical discipline comes from proxy operationalization, cross-domain structural convergence, and differential predictions against nearby theories.

---

## Phase 7 — Long Foundations refactor

**Target file**: `Philosophy/SRT_Philosophy_Foundations.md`

### Refactor goals

| Move | Purpose |
|---|---|
| Add top-level “current hardened reading” section | prevent old preserved content from being mistaken as newest view |
| Move legacy / repeated blocks into annex notes | reduce duplication |
| Add formula-role labels | prevent poetic math overclaim |
| Insert core paragraph from `00_READ_FIRST` | make selection realism visible in main long file |
| Link PH-SS IDs near risky claims | agent-readable hardening hooks |

### Done condition

The first 500 lines of the long Foundations file should make clear:

```text
SRT = selection realism + layered realism + anti-relativist constraint realism.
Not subjective idealism.
Not hidden-world modal realism.
Not stability-as-goodness.
Not all-selection-is-consciousness.
```

---

## 8. Suggested commit sequence

```text
commit 1: Add PH-SS read-first map, crosswalk, execution plan
commit 2: Promote PH-SS files in README and machine index
commit 3: Patch compact foundations with selection realism / layered realism
commit 4: Patch axiom guardrails
commit 5: Expand objection ledger O-Phil-11..20
commit 6: Patch ethics and political files
commit 7: Refactor long foundations / annex legacy content
```

---

## 9. Do-not-do list

Do **not**:

- promote this file to canonical definition source;
- silently redefine `L_0`, `d-value`, `Psi_f`, or `T_dir` here;
- remove bold SRT slogans entirely;
- make SRT safer by making it vague;
- merge stability and legitimacy;
- equate `theta` with subjective preference;
- equate Fisher metric with the full meaning of `Psi_f`;
- imply all selection is consciousness.

---

## 10. Completion checklist

```text
[ ] README includes 00 / 01 / 02 reading order
[ ] _SRT_INDEX includes 00 / 01 / 02 in Philosophy entrypoints
[ ] Compact Core contains selection realism and layered realism guardrails
[ ] _SRT_Phil_Axioms contains L0 / priority / reality-strength / Psi_f-layer / normativity / subjecthood guardrails
[ ] Objection Ledger contains or cross-links O-Phil-11..20
[ ] Ethics contains moral legitimacy ladder
[ ] Social / political files contain collective L2 ontology
[ ] Validation file contains non-reductive validation statement
[ ] Long Foundations has current hardened reading near top
```
