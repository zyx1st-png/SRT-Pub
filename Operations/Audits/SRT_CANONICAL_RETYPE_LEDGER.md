---
id: SRT-CANONICAL-RETYPE-LEDGER
type: audit
status: active
record_stage: r2c_author_a_landed
layer: operations
epistemic_layer: os
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
dependency:
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - CANONICAL_REGISTRY.md
  - Governance/SRT_CANONICAL_FREEZE.md
  - Operations/Audits/SRT_PR947_RETROSPECTIVE_INDEPENDENT_REVIEW_2026-09-12.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R2C_FREEZE_SPLIT_2026-09-12.md
  - STATUS.md
tags: [RetypingLedger, Supersession, ReverseAudit, CanonicalCleanup, R2C]
---

# SRT canonical retyping ledger

> **Role:** stable per-claim working ledger for the post-#947 reverse audit. This file records source claims, adjudicated dispositions and implementation state. It is **not** a canonical definition owner and cannot retire, redefine or promote a claim by itself.

## 0. Ledger contract

Allowed final disposition vocabulary:

```text
KEEP | RETYPE | DEMOTE | RETIRE | MERGE | SIMPLIFY | OPEN
```

Every substantive row must distinguish:

```text
claim identity
!= token occurrence

disposition decision
!= implementation landing

freeze class
!= epistemic / theorem strength

legacy wording
!= automatic contradiction
```

R2-B guard:

```text
pre-#947 bearer / same-bearer occurrences are quarantined;
no bulk replacement or token-level migration is permitted;
retyping is claim-by-claim only.
```

R2-C author-A governance rule:

```text
Freeze A / B are edit-safety classifications;
they do not upgrade P-level, theorem status, programme Level standing,
or scientific distinctiveness.
```

## 1. Required row fields

| Field | Meaning |
|---|---|
| Ledger ID | Stable row identifier |
| Source / anchor | File and section / theorem / claim anchor |
| Normalized claim | The actual proposition being judged, not merely a keyword |
| Current relation | Compatibility / conflict / ambiguity relative to current spine + local owner |
| Disposition | One of the seven allowed verbs |
| Current owner / target reading | Where surviving meaning is controlled |
| Decision authority | Author adjudication / canonical owner / governance decision / OPEN |
| Decision state | PROPOSED / AUTHOR-ACCEPTED / IMPORTED-ALREADY-LANDED / OPEN |
| Implementation state | NOT-STARTED / PARTIAL / LANDED / N-A |
| Notes | Scope guard / non-implication |

## 2. Imported already-paid dispositions

These rows do **not** begin a new reverse audit. They import dispositions already stated in the post-#947 canonical/status state so later work has an auditable starting surface.

| Ledger ID | Source / anchor | Normalized claim | Current relation | Disposition | Current owner / target reading | Decision authority | Decision state | Implementation state | Notes |
|---|---|---|---|---|---|---|---|---|---|
| R2C-001 | pre-#947 Bearer/history route; summarized in `STATUS.md §10–11` | history-to-reconstitution dependence defines Bearer | conflicts with current prospective P+E Bearer routing | RETIRE | Spine §7 Bearer route; retrospective history relation may survive separately | post-#947 author/canonical state | IMPORTED-ALREADY-LANDED | LANDED | Retires Bearer sufficiency, not history relevance |
| R2C-002 | pre-#947 onset route; `STATUS.md §11` | first constitutive history coupling is Bearer onset | conflicts with current prospective P+E route | RETIRE | Spine §7 | post-#947 author/canonical state | IMPORTED-ALREADY-LANDED | LANDED | No replacement onset theorem inferred |
| R2C-003 | pre-#947 SC ordering; `STATUS.md §11` | self-consequence closure is stronger than / above generic Bearer | conflicts with current typed layering | RETIRE | Spine Bearer routing | post-#947 author/canonical state | IMPORTED-ALREADY-LANDED | LANDED | Does not retire SC as a relation |
| R2C-004 | pre-#947 SC relation; `STATUS.md §10` | self-consequence closure itself is a Bearer gate | over-strong | RETYPE | retrospective self-effect closure relation; possible future Bearer research input remains OPEN | post-#947 author/canonical state | IMPORTED-ALREADY-LANDED | LANDED | No current Bearer admission power |
| R2C-005 | matched-history test family; `STATUS.md §10` | matched-history difference supplies Bearer score / admission | over-strong | RETYPE | retrospective dependence test only | post-#947 author/canonical state | IMPORTED-ALREADY-LANDED | LANDED | Presence/absence does not classify Bearer |
| R2C-006 | PH-IND02 PERS-2; `STATUS.md §10` | PERS-2 functions as a Bearer admission gate | over-strong | RETYPE | retrospective consequence/history relation family | post-#947 author/canonical state | IMPORTED-ALREADY-LANDED | LANDED | No current admission-gate status |
| R2C-007 | `Core_Law/SRT_One_Formation.md` + Registry §13 | One / Selection-position detailed formation semantics live in One Formation | compatible with spine delegation | KEEP | `SRT-ONE-FORMATION` local canonical semantic owner | R1 author owner adjudication + registry | IMPORTED-ALREADY-LANDED | LANDED | `P1-candidate` remains; no theorem promotion |

## 3. R2-C F7 rows — author option A landed

Author adjudication: `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R2C_FREEZE_SPLIT_2026-09-12.md`.

| Ledger ID | Source / anchor | Normalized claim | Current relation | Disposition | Current owner / target reading | Decision authority | Decision state | Implementation state | Notes |
|---|---|---|---|---|---|---|---|---|---|
| R2C-008 | `Governance/SRT_CANONICAL_FREEZE.md` vs Registry §13 | One Formation is a registered canonical semantic owner delegated to by a Freeze-A spine but had no freeze classification | edit-safety mismatch | KEEP | One Formation remains local canonical semantic owner; Freeze A added | 2026-09-12 author option A | AUTHOR-ACCEPTED | LANDED | `status: draft` / `P1-candidate` unchanged; Freeze A is edit protection only |
| R2C-009 | `Governance/SRT_CANONICAL_FREEZE.md` vs Registry §13a | Individuation is a major downstream hybrid subject model but had no A/B freeze classification | mutability class ambiguous | RETYPE | Freeze B downstream hybrid model; later subject-entry / sigma reconstruction remains OPEN | 2026-09-12 author option A | AUTHOR-ACCEPTED | LANDED | Freeze B is cross-check protection, not theorem or subject-threshold ratification |

## 4. Reverse-audit admission rule

A new row may enter the ledger only when all of the following are named:

```text
source file + anchor;
normalized claim;
current spine/local-owner relation;
proposed disposition;
authority required to finalize it.
```

A mere search hit, token count, wording similarity or file age is insufficient.

## 5. Implementation rule

A row becomes `LANDED` only after the actual source / owner / governance surfaces required by its disposition have been changed and validated. The ledger itself cannot mark a canonical claim retired merely by changing the row.

For C-risk canonical edits, the normal edit protocol still applies.

## 6. Programme guards

```text
F3 ledger infrastructure = ACCEPTED / ACTIVE;
F7 local-owner freeze typing = AUTHOR A / LANDED;
R2-C F3/F7 = COMPLETE after STATUS / generated propagation;
old-canonical reverse audit = NEXT SEPARATE PROGRAMME STEP / not started by this landing;
L0 canonical rewrite = HOLD behind #949;
new Level 1 = NOT ASSIGNED;
Level 2 = HOLD;
scientific distinctiveness = NOT ESTABLISHED;
whole-architecture non-substitutability = NOT ESTABLISHED.
```
