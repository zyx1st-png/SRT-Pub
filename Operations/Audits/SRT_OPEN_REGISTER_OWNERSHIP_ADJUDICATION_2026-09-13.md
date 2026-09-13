---
id: SRT-AUDIT-OPEN-REGISTER-OWNERSHIP-ADJUDICATION-20260913
type: audit
status: active
record_stage: open_register_ownership_adjudication
layer: operations
epistemic_layer: os
claim_mode: governance
canonical: false
date: 2026-09-13
research_mode: U
root_question: Which surface owns which OPEN item, now that the author has adjudicated the five routing questions left open by the pre-audit?
comparative_claim: none
named_comparator: null
n_mode_triggered: false
dependency:
  - Operations/Audits/SRT_OPEN_REGISTER_RECONCILIATION_PREAUDIT_2026-09-13.md
  - STATUS.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - Core_Law/SRT_One_Formation.md
  - Core_Law/SRT_Collective_Selection.md
  - Core/SRT_OPEN_TENSIONS.md
  - Governance/SRT_EDIT_PROTOCOL.md
  - Governance/README.md
tags: [OpenRegister, Ownership, Adjudication, StatusContraction]
---

# OPEN register ownership — adjudication

> **Role**: records the author's answers to the five questions in
> `SRT_OPEN_REGISTER_RECONCILIATION_PREAUDIT_2026-09-13.md §5`, and the
> implementation constraints those answers carry. It authorizes the migration; it
> does not perform it, and it **closes no OPEN item**.
>
> **Provenance**: the author adjudicated in session on 2026-09-13 by adopting the
> external review's five recommendations (「我认同gpt的」). The recommendations
> are relayed below as the content of that decision; the decision itself is the
> author's. Per `AGENTS.md`, AI-generated alternatives are not author decisions
> and two models agreeing is not author convergence — this record exists because
> the author, not a reviewer, chose.

## A1 — no global OPEN owner

```text
Spine §9        = cross-owner ontology OPEN gates
local owner     = its own structural OPEN
OPEN_TENSIONS   = cross-owner hardening ledger / companion
```

`Core/SRT_OPEN_TENSIONS.md` does **not** become the declared owner of other
surfaces' OPEN items and does not replace any local owner. This preserves the
owner-based architecture instead of creating a single super-file of all
unresolved questions.

## A2 — S10 / S13 / S18 do not land together

**S10** (unique empirical / numerical Bearer admission threshold) and **S13**
(Bearer ↔ position stability) are Bearer hardening. Until the Bearer final
semantic owner is settled — which is S22, still OPEN — they are routed to
Spine §9 as **provisional routing**.

```text
S10, S13 -> Spine §9 / PROVISIONAL ROUTING
provisional routing != Spine acquiring final Bearer definition authority
```

The provisional marker is not decorative. S22 asks who owns Bearer; routing S10
and S13 into Spine unmarked would let the routing answer S22 by itself, which is
the same self-closing shape the pre-audit corrected in its own S22 row.

**S18** (scale attribution under tightly coupled nested Ones) **splits**; it is
not moved as one item:

```text
local formation / unit question      -> Core_Law/SRT_One_Formation.md
higher-order realization             -> Core_Law/SRT_Collective_Selection.md
cross-layer non-identity gate only   -> Spine §9
```

The split is required by the receiving file's own declared boundary, not merely
preferred. `SRT_Collective_Selection.md` states **"Does not define: `One /
Selection-position`"** and carries an R1 One-formation boundary: `One Formation`
owns `One / Selection-position`, and higher-order One language does not establish
collective ISP automatically. Moving S18 wholesale into Collective Selection
would cross that boundary. Note also that the file is `status: draft_v0`.

## A3 — W1 / W2 leave STATUS without being promoted

The typology is neither retained by STATUS nor raised into Spine canonical. It
moves to an explicit **noncanonical machine / audit taxonomy owner**, as
retrospective writeback-depth / audit labels — classification and checking tools,
not a universal ontology primitive.

**Implementation cost, recorded rather than glossed**: no such owner exists in
the repository today, so this answer requires creating one.
`Governance/README.md` 治理比例原则 4 — 「导航一进一出」— requires that a new
index/router merge, retire or repurpose an old entry. The 一出 here is
`STATUS.md §14`'s de-facto ownership of the typology, which the move retires.
The migration must make that retirement explicit; it may not simply add a file.

## A4 — S04 / S12 merge; S14 / S15 stay separate

**S04 + S12 → one record.** The repository's own notation already treats Concern
and 关切 as one term: `Core_Law/SRT_Generative_Ontology_Spine.md` writes
`Bearer -> Concern / 关切` and its §9 carries the single item
`Bearer <-> Concern / 关切`. STATUS split into two what the Spine records as one.

```text
merging two records != closing the question
the merged item stays OPEN
```

**S14 / S15 stay two.** `Bearer ↔ cognition` and `Bearer ↔ subject-position` are
distinct downstream burdens under the current architecture; merging them would
re-flatten a layering the architecture keeps apart.

## A5 — STATUS keeps programme verdicts and pointers

```text
STATUS OPEN content after migration =
  Level 2 = HOLD
  new Level 1
  scientific distinctiveness
  whole-architecture non-substitutability
  + pointers to Spine §9 / local owners / hardening ledger
```

No duplicated ontology OPEN register remains on the dashboard.

## What this adjudication does not decide

```text
S22 Bearer canonical ownership / sufficiency hardening = STILL OPEN
```

It also closes no other OPEN item, changes no canonical definition, assigns no
claim level, and does not open the One Formation owner cycle. Every item named
above remains OPEN in its new location.

## Migration constraints carried forward

From the pre-audit §4, unchanged:

1. rehome the four orphans **before** anything is removed from STATUS;
2. give W1/W2 its owner, with the 一进一出 retirement made explicit (A3);
3. for each remaining item, confirm the receiving surface states it, then remove
   the STATUS line **in the same commit**;
4. never remove and rehome in separate commits — the gap is where an item
   disappears;
5. mark S10 / S13 as provisional routing in the receiving surface (A2);
6. record the S04/S12 merge as a merge of records, never as a closure (A4).
