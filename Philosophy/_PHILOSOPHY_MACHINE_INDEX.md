---
id: SRT-PHILOSOPHY-MACHINE-INDEX
type: machine_index
tags:
  - Philosophy
  - Machine-Index
  - PH-SS
  - Selection-Realism
  - Layered-Realism
  - Objection-Led-Hardening
status: active_v3
layer: meta
epistemic_layer: bridge
claim_mode: index
claim_level: P5
canonical: false
date: 2026-04-27
dependency:
  - SRT-PHILOSOPHY-README
  - SRT-PHIL-HARDENING-SOFT-SPOTS-2026-04-27
  - SRT-PHIL-PH-SS-OBJECTION-CROSSWALK-2026-04-27
  - SRT-PHIL-PH-SS-HARDENING-EXECUTION-PLAN-2026-04-27
  - SRT-PHIL-SELECTION-REALISM-LAYERED-REALISM-PATCH-2026-04-27
  - SRT-PHIL-FOUNDATIONS-COMPACT-CORE
  - SRT-PHIL-AXIOMS-PH-SS-GUARDRAILS-2026-04-27
  - SRT-PHIL-OBJECTION-LEDGER-PH-SS-EXTENSION-2026-04-27
  - SRT-ETHICS-PH-SS-GUARDRAILS-2026-04-27
  - SRT-SOCIAL-POLITICAL-PH-SS-GUARDRAILS-2026-04-27
machine_summary: >
  Directory-local machine index for the Philosophy folder. Use this file to route SRT philosophy
  queries through the PH-SS hardening sequence, Compact Core v4, axiom guardrails, objection extension,
  ethics guardrails, and social/political guardrails. It does not define canonical SRT primitives.
---

# Philosophy Machine Index

> **Role**: Directory-local machine routing file for `Philosophy/`.  
> **Canonical status**: not canonical; does not define P0/P1 primitives.  
> **Main routing principle**: for philosophy hardening, start with PH-SS files, then Compact Core v4, then companion owner-file guardrails, then long / legacy / domain-specific files.

---

## 0. Fast route

```text
Philosophy/_PHILOSOPHY_MACHINE_INDEX.md
  -> Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md
  -> Philosophy/01_PH_SS_Objection_Crosswalk.md
  -> Philosophy/02_PH_SS_Hardening_Execution_Plan.md
  -> Philosophy/SRT_Philosophy_Foundations_CompactCore.md  # active_v4 main short entry
  -> Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md       # axiom companion guardrails
  -> Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md
  -> Philosophy/SRT_Ethics_PH_SS_Guardrails.md
  -> Philosophy/SRT_Social_Political_PH_SS_Guardrails.md
  -> target owner file
```

---

## 1. Current hardened reading

The Philosophy folder should currently be read through this frame:

```text
SRT = selection realism
    + layered realism
    + anti-relativist constraint realism
```

Core guardrails:

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

## 2. Primary philosophy hardening files

| File | Role | Status |
|---|---|---|
| `00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md` | read-first PH-SS map; 12 soft points and upgrade modules | active bridge hardening |
| `01_PH_SS_Objection_Crosswalk.md` | maps PH-SS IDs to objections, responses, withdrawal conditions, and owner files | active bridge hardening |
| `02_PH_SS_Hardening_Execution_Plan.md` | turns PH-SS into staged repository tasks | active bridge hardening |
| `03_Selection_Realism_Layered_Realism_CompactPatch.md` | merge-candidate patch; now mostly merged into Compact Core v4 | active bridge patch |
| `SRT_Philosophy_Foundations_CompactCore.md` | main short entry point for current hardened philosophy | active_v4 |
| `_SRT_Phil_Axioms_PH_SS_Guardrails.md` | companion guardrail file for axiom-layer over-readings | active bridge guardrail |
| `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md` | companion objection extension containing O-Phil-11..20 | active bridge hardening |
| `SRT_Ethics_PH_SS_Guardrails.md` | companion guardrail file for moral legitimacy, d-value, responsibility, and poetic formulas | active bridge guardrail |
| `SRT_Social_Political_PH_SS_Guardrails.md` | companion guardrail file for collective L2, institutions, markets, legitimacy, and friction export | active bridge guardrail |

---

## 3. PH-SS routing map

| PH-SS | Soft spot | First target | Current status |
|---|---|---|---|
| PH-SS-01 | `L_0` ontology ambiguity | Compact Core / `_SRT_Phil_Axioms_PH_SS_Guardrails.md` | compact core v4 done; axiom companion done |
| PH-SS-02 | selection-before-existence temporal misread | Compact Core / `_SRT_Phil_Axioms_PH_SS_Guardrails.md` | compact core v4 done; axiom companion done |
| PH-SS-03 | reality-strength flattening | Compact Core / Axiom companion / Foundations | compact core v4 done; axiom companion done; long file pending |
| PH-SS-04 | subjective idealism risk | Compact Core / Objection Ledger extension | compact core v4 done; objection extension done |
| PH-SS-05 | `Psi_f` layer confusion | Compact Core / Axiom companion / `Psi_f` canonical links | compact core v4 done; axiom companion done; canonical cross-check pending |
| PH-SS-06 | stabilization to value jump | Compact Core / Axiom companion / Ethics guardrail | compact core guardrail done; axiom companion done; ethics companion done |
| PH-SS-07 | mystical teleology risk | Compact Core / Objection extension / Core 24 | compact core v4 done; objection extension done; Core 24 link pending |
| PH-SS-08 | `d-value` philosophical status | Compact Core / Objection extension / Ethics guardrail / `d-value` canonical links | compact core v4 done; objection extension done; ethics companion done; canonical cross-check pending |
| PH-SS-09 | social ontology underdeveloped | Compact Core / Objection extension / Social-political guardrail | compact core v4 done; objection extension done; social-political companion done |
| PH-SS-10 | consciousness threshold | Compact Core / Axiom companion / Objection extension / AI / Neuroscience | compact core v4 done; axiom companion done; objection extension done; cross-domain pending |
| PH-SS-11 | non-reductive validation | Compact Core / Objection extension / Core 24 / Claim Ladder | compact core v4 done; objection extension done; Core 24 pending |
| PH-SS-12 | anti-relativism | Compact Core / Objection extension / Social-political guardrail | compact core v4 done; objection extension done; social-political companion done |

---

## 4. Active main files

| File | Use when |
|---|---|
| `SRT_Philosophy_Foundations_CompactCore.md` | Need the current short hardened statement of SRT philosophy. |
| `SRT_Philosophy_Foundations.md` | Need long historical / accumulated argument; beware legacy and duplicate sections. |
| `_SRT_Phil_Axioms.md` | Need philosophy-domain mapping axioms; read with the PH-SS guardrails companion. |
| `_SRT_Phil_Axioms_PH_SS_Guardrails.md` | Need safe readings of axiom-layer claims and six guardrail definitions. |
| `SRT_Philosophy_Objection_Ledger.md` | Need original strongest objections and claim-hygiene rules. |
| `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md` | Need O-Phil-11..20 for PH-SS-specific objections. |
| `SRT_Philosophy_Hardening_TODO.md` | Need current execution status and next tasks. |
| `SRT_Philosophy_Ethics.md` / `SRT_Ethics_Agency.md` | Need ethics / agency; read with `SRT_Ethics_PH_SS_Guardrails.md`. |
| `SRT_Ethics_PH_SS_Guardrails.md` | Need moral legitimacy ladder, friction-export test, future-selectability test, responsibility recalibration. |
| `SRT_Social_Economics_CompactCore.md` | Need social ontology and economics; read with `SRT_Social_Political_PH_SS_Guardrails.md`. |
| `SRT_Political_Philosophy.md` | Need political / institutional extension; read with `SRT_Social_Political_PH_SS_Guardrails.md`. |
| `SRT_Social_Political_PH_SS_Guardrails.md` | Need collective L2, institutional legitimacy, market/money guardrails, friction export, and reselection capacity. |

---

## 5. Query routing examples

| Query type | Route |
|---|---|
| “What is SRT philosophically?” | Compact Core v4 -> 00 read-first map |
| “Is SRT idealism?” | Compact Core v4 §1/§7 -> Objection Ledger extension O-Phil-20 / O-Phil-12 as needed |
| “What is L0?” | Compact Core v4 §4 -> PH-SS-01 -> Axiom guardrail Def-Phil-L0-Selectability -> Core_Law L0 anchor |
| “Does selection precede existence?” | Compact Core v4 §5 -> PH-SS-02 -> Axiom guardrail Def-Phil-Manifestational-Priority |
| “Does SRT make everything relative?” | Compact Core v4 §16 -> PH-SS-12 -> Objection extension O-Phil-20 -> Social-political guardrail |
| “Does SRT justify stable norms?” | Compact Core v4 §14 -> PH-SS-06 -> Axiom guardrail Def-Phil-Normativity-Ladder -> Ethics guardrail |
| “Does SRT imply panpsychism?” | Compact Core v4 §10 -> PH-SS-10 -> Axiom guardrail Def-Phil-Subjecthood-Threshold -> Objection extension O-Phil-18 |
| “How can SRT be tested?” | Compact Core v4 §17 -> PH-SS-11 -> Objection extension O-Phil-19 -> Core 24 pending |
| “How does SRT treat markets/institutions?” | Social Economics Compact Core -> Social-political guardrail -> PH-SS-09/12 |
| “How does SRT avoid is-ought gap?” | Ethics guardrail -> Objection extension O-Phil-17/20 -> Compact Core §14 |

---

## 6. Next owner-file upgrades

```yaml
next_owner_file_upgrades:
  long_foundations:
    - add_current_hardened_reading_near_top
    - mark_legacy_passages_as_superseded_by_compact_core_v4_where_needed
    - add_formula_role_labels
  direct_main_file_merges:
    - add_pointer_to_ethics_guardrail_in_SRT_Philosophy_Ethics.md
    - add_pointer_to_social_political_guardrail_in_SRT_Social_Economics_CompactCore.md
    - add_pointer_to_social_political_guardrail_in_SRT_Political_Philosophy.md
  cross_domain_files:
    - AI_consciousness_threshold_link
    - neuroscience_subjecthood_threshold_link
    - Core24_non_reductive_validation_link
```

---

## 7. Do-not-use-as

Do not use this file as:

- canonical definition source;
- replacement for Core / Core_Law;
- replacement for `SRT_Philosophy_Foundations_CompactCore.md`;
- evidence that all PH-SS tasks are completed.

It is only a routing surface.
