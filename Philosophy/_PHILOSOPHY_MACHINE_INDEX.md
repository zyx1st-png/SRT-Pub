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
status: active_v1
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
machine_summary: >
  Directory-local machine index for the Philosophy folder. Use this file to route SRT philosophy
  queries through the PH-SS hardening sequence and the active_v4 Compact Core. It does not define
  canonical SRT primitives.
---

# Philosophy Machine Index

> **Role**: Directory-local machine routing file for `Philosophy/`.  
> **Canonical status**: not canonical; does not define P0/P1 primitives.  
> **Main routing principle**: for philosophy hardening, start with PH-SS files, then Compact Core v4, then long / legacy / domain-specific files.

---

## 0. Fast route

```text
Philosophy/_PHILOSOPHY_MACHINE_INDEX.md
  -> Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md
  -> Philosophy/01_PH_SS_Objection_Crosswalk.md
  -> Philosophy/02_PH_SS_Hardening_Execution_Plan.md
  -> Philosophy/SRT_Philosophy_Foundations_CompactCore.md  # active_v4 main short entry
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

---

## 3. PH-SS routing map

| PH-SS | Soft spot | First target | Current status |
|---|---|---|---|
| PH-SS-01 | `L_0` ontology ambiguity | Compact Core / `_SRT_Phil_Axioms.md` | compact core v4 done; axioms pending |
| PH-SS-02 | selection-before-existence temporal misread | Compact Core / `_SRT_Phil_Axioms.md` | compact core v4 done; axioms pending |
| PH-SS-03 | reality-strength flattening | Compact Core / Foundations | compact core v4 done; long file pending |
| PH-SS-04 | subjective idealism risk | Compact Core / Objection Ledger | compact core v4 done; ledger expansion pending |
| PH-SS-05 | `Psi_f` layer confusion | Compact Core / `Psi_f` canonical links | compact core v4 done; canonical cross-check pending |
| PH-SS-06 | stabilization to value jump | Ethics / Political Philosophy | compact core guardrail done; ethics pending |
| PH-SS-07 | mystical teleology risk | Compact Core / Core 24 | compact core v4 done; Core 24 link pending |
| PH-SS-08 | `d-value` philosophical status | Compact Core / `d-value` canonical links | compact core v4 done; canonical cross-check pending |
| PH-SS-09 | social ontology underdeveloped | Social Economics / Political Philosophy | compact core v4 done; social files pending |
| PH-SS-10 | consciousness threshold | Compact Core / AI / Neuroscience | compact core v4 done; cross-domain pending |
| PH-SS-11 | non-reductive validation | Compact Core / Core 24 / Claim Ladder | compact core v4 done; Core 24 pending |
| PH-SS-12 | anti-relativism | Compact Core / Political Philosophy | compact core v4 done; political links pending |

---

## 4. Active main files

| File | Use when |
|---|---|
| `SRT_Philosophy_Foundations_CompactCore.md` | Need the current short hardened statement of SRT philosophy. |
| `SRT_Philosophy_Foundations.md` | Need long historical / accumulated argument; beware legacy and duplicate sections. |
| `_SRT_Phil_Axioms.md` | Need philosophy-domain mapping axioms; pending PH-SS guardrail cleanup. |
| `SRT_Philosophy_Objection_Ledger.md` | Need strongest objections and claim-hygiene rules; pending O-Phil-11..20 expansion. |
| `SRT_Philosophy_Hardening_TODO.md` | Need current execution status and next tasks. |
| `SRT_Philosophy_Ethics.md` / `SRT_Ethics_Agency.md` | Need ethics / agency; pending moral legitimacy ladder update. |
| `SRT_Social_Economics_CompactCore.md` | Need social ontology and economics; pending collective L2 guardrail update. |
| `SRT_Political_Philosophy.md` | Need political / institutional extension; pending friction-export and legitimacy diagnostics. |

---

## 5. Query routing examples

| Query type | Route |
|---|---|
| “What is SRT philosophically?” | Compact Core v4 -> 00 read-first map |
| “Is SRT idealism?” | Compact Core v4 §1/§7 -> Objection Ledger O-Phil-2 -> PH-SS-04/12 |
| “What is L0?” | Compact Core v4 §4 -> PH-SS-01 -> Core_Law L0 anchor |
| “Does selection precede existence?” | Compact Core v4 §5 -> PH-SS-02 -> `_SRT_Phil_Axioms.md` pending guardrail |
| “Does SRT make everything relative?” | Compact Core v4 §16 -> PH-SS-12 -> Objection Crosswalk |
| “Does SRT justify stable norms?” | Compact Core v4 §14 -> PH-SS-06 -> ethics files pending |
| “Does SRT imply panpsychism?” | Compact Core v4 §10 -> PH-SS-10 -> AI / Neuroscience pending |
| “How can SRT be tested?” | Compact Core v4 §17 -> PH-SS-11 -> Core 24 pending |

---

## 6. Next owner-file upgrades

```yaml
next_owner_file_upgrades:
  _SRT_Phil_Axioms.md:
    - Def-Phil-L0-Selectability
    - Def-Phil-Manifestational-Priority
    - Def-Phil-Reality-Strength
    - Def-Phil-PsiF-Layers
    - Def-Phil-Normativity-Ladder
    - Def-Phil-Subjecthood-Threshold
  SRT_Philosophy_Objection_Ledger.md:
    - O-Phil-11_L0-hidden-world
    - O-Phil-12_temporal-priority
    - O-Phil-13_reality-strength-flattening
    - O-Phil-14_PsiF-equivocation
    - O-Phil-15_mystical-teleology
    - O-Phil-16_d-value-preference-reduction
    - O-Phil-17_social-construction-institutional-reification
    - O-Phil-18_consciousness-over-attribution
    - O-Phil-19_non-reductive-verification
    - O-Phil-20_selected-reality-relativism
  ethics_and_political_files:
    - moral_legitimacy_ladder
    - friction_export_test
    - future_selectability_test
    - cross_subject_d_value_bandwidth
    - reversibility_correction_channel
```

---

## 7. Do-not-use-as

Do not use this file as:

- canonical definition source;
- replacement for Core / Core_Law;
- replacement for `SRT_Philosophy_Foundations_CompactCore.md`;
- evidence that all PH-SS tasks are completed.

It is only a routing surface.
