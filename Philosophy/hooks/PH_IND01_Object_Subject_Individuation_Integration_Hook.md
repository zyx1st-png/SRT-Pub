---
id: HOOK-PH-IND01-OBJECT-SUBJECT-INDIVIDUATION
source_patch: Philosophy/patches/SRT_Philosophy_PH_IND01_Object_Subject_Individuation_Before_Identification_v0_1.md
source_ids:
  - SRC-2026-08-08-COGNITION-KIBBE-LESLIE-MINIMAL-OBJECT-REPRESENTATIONS-REBUILT
type: integration_hook
status: active
record_stage: pending
integration_status: pending
layer: operations
epistemic_layer: bridge
claim_mode: integration_plan
canonical: false
target_documents:
  - Core_Law/SRT_Individuation.md
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
  - Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md
landing_ledger:
  - target: "Core_Law/SRT_Individuation.md"
    state: pending
    blocked_by: "Future individuation synthesis may add the bearer-individuation-before-self-identification distinction; source evidence remains object-level only and no canonical edit is authorized in this material pass."
  - target: "Philosophy/SRT_Subjecthood_Threshold_Interface.md"
    state: pending
    blocked_by: "Future subjecthood synthesis may add bearer individuation != bearer self-identification; object tracking must remain a negative control rather than evidence for subjecthood."
  - target: "Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md"
    state: pending
    blocked_by: "Future synthesis may add the OBJECT/SUBJECT comparison only as SRT P3 bridge architecture; do not attribute the subject-side sequence to Kibbe–Leslie."
---

# PH-IND01 Integration Hook — Object / Subject Individuation Before Identification

## Purpose

Integrate the surviving SRT-side distinction without importing the source’s object-cognition evidence into subjecthood or consciousness claims.

## Source-backed payload

```text
object individuation
can precede / survive without
rich object identification or property binding
```

This is the only direct evidential payload from Kibbe–Leslie that future SRT prose may cite as source support.

## SRT-only bridge payload

```text
subject-position individuation
may precede
reflective self-identification / self-modeling
```

This is an SRT P3 structural analogy consistent with current `SRT_Individuation.md`; it is not a result of the infant object paper.

## Target 1 — `Core_Law/SRT_Individuation.md`

Future bounded insertion, if separately authorized:

> A subject need not begin as a theory of itself. Subject-position entry concerns whether a continuing position has become history-bearing, consequence-bearing and reselectable; reflective self-identification is a later thickening in which that already-continuing position becomes an object of its own modeling.

Required guard:

```text
Kibbe–Leslie object evidence
!= evidence for subjecthood threshold
```

No change to the existing two-transition structure is required.

## Target 2 — `Philosophy/SRT_Subjecthood_Threshold_Interface.md`

Add a timing distinction alongside the bearer gate:

```text
bearer individuation
!= bearer self-identification
```

A self-model may identify or enrich an already-individuated bearer; a model of “self” does not by itself establish same-bearer consequence return.

## Target 3 — `Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md`

Potential synthesis pair:

```text
OBJECT:
this one -> still this one -> what this one is

SUBJECT:
this bearer / from here -> still this bearer across history -> who I am
```

Label the entire second row as SRT bridge architecture.

## Negative-control use

Use object indexing as a negative control:

```text
persistent tracked individual
!= consequence bearer
```

This is particularly useful against theories that infer subjecthood from persistence, global access, self-description or tracking alone.

## Relation to later hard-problem work

This hook is compatible with any later distinction between:

```text
perspective-center individuation
and
phenomenal necessity
```

but it does not depend on an unmerged consciousness patch and must remain independently valid.

## Forbidden integration

Do not write:

```text
object index = minimal subject
"this one" = "I"
infant object permanence proves consciousness
Kibbe–Leslie proves SRT subject individuation
self-model is unnecessary in every consciousness architecture
```

## Exit condition

Mark this hook integrated only when a target owner or synthesis file explicitly preserves all four distinctions:

```text
object tracking
!= object identification
!= bearer continuity
!= phenomenal consciousness
```
