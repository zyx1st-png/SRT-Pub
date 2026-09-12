---
id: SRT-R2C-SUPERSESSION-INFRASTRUCTURE-20260912
type: audit
status: active
record_stage: independent_audit_author_gate_preparation
date: 2026-09-12
layer: operations
epistemic_layer: os
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
root_question: What minimum supersession infrastructure closes R2-C F3/F7 without beginning the old-canonical reverse audit or promoting draft local-owner claims?
dependency:
  - Operations/Audits/SRT_PR947_RETROSPECTIVE_INDEPENDENT_REVIEW_2026-09-12.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - CANONICAL_REGISTRY.md
  - Governance/SRT_CANONICAL_FREEZE.md
  - Governance/SRT_EDIT_PROTOCOL.md
  - Core_Law/SRT_One_Formation.md
  - Core_Law/SRT_Individuation.md
  - STATUS.md
tags: [R2C, Supersession, RetypingLedger, Freeze, LocalOwner, OneFormation, Individuation]
---

# R2-C independent audit — supersession infrastructure

> **Scope:** R2-C only: `F3` per-claim supersession ledger and `F7` local-owner authority / freeze typing. This record does not begin the old-canonical reverse audit, does not alter L0, does not satisfy #949, and does not assign any new Level.

## 1. Live gate verified

Baseline at audit start:

```text
main = 650f3adcd1d87bd5565144d76ece04d02c924f82
R2-A = COMPLETE
R2-B = COMPLETE / #954 merged
R2-C F3/F7 = NEXT SEPARATE GATE / NOT STARTED
old-canonical reverse audit = AFTER R2-C
#949 = REQUIRED BEFORE ANY L0 CANONICAL REWRITE
L0 rewrite = HOLD
```

The only open PR at audit start is #949, whose scope is the creator–AI final-skeleton gate for later L0 work. It is not an R2-C implementation vehicle.

---

## 2. F3 finding — the repository has dispositions but no per-claim working ledger

The post-#947 repository already uses the disposition vocabulary:

```text
KEEP | RETYPE | DEMOTE | RETIRE | MERGE | SIMPLIFY | OPEN
```

and `STATUS.md` already contains a small supersession summary for #931/#933. But there is no stable per-claim surface recording:

```text
which source claim is being judged;
where it occurs;
what exact cross-owner conflict or compatibility is alleged;
which disposition was selected;
which current owner controls the replacement / surviving reading;
who authorized the disposition;
whether implementation has actually landed.
```

That gap matters because the spine's rule

```text
older conflicting cross-layer inference -> cleanup / retyping debt
```

is otherwise invocable without an auditable adjudication trail.

### F3 required properties

The ledger should therefore:

1. be **audit / governance infrastructure, not a definition owner**;
2. use a stable per-claim ID;
3. preserve the original source path and anchor;
4. record the normalized claim rather than merely a token occurrence;
5. type the conflict / compatibility against the current spine and local owner;
6. restrict final dispositions to the seven §9 verbs;
7. separate **decision state** from **implementation state**;
8. preserve explicit author / canonical provenance;
9. allow `OPEN` as a legitimate result rather than forcing replacement theory;
10. forbid bulk `bearer` token migration after R2-B's legacy quarantine.

### Recommended F3 artifact

```text
Operations/Audits/SRT_CANONICAL_RETYPE_LEDGER.md
```

The ledger is intentionally under `Operations/Audits/`: it records adjudication and implementation state but cannot overrule a canonical owner by itself.

---

## 3. F7 finding — freeze strength and claim strength are currently conflated by omission

### 3.1 `SRT_One_Formation.md`

Current frontmatter / registry typing:

```text
status = draft
claim_mode = canonical
claim_level = P1-candidate
role = thin L1 canonical semantic owner for One / Selection-position formation
```

The registry explicitly routes One / Selection-position definition questions to it. The frozen cross-owner spine also delegates detailed One formation semantics to it.

But `Governance/SRT_CANONICAL_FREEZE.md` lists the spine in Freeze A and does **not** list `SRT_One_Formation.md` in A or B.

This creates the exact F7 asymmetry:

```text
frozen cross-owner owner
-> delegates detail to
unfrozen local canonical semantic owner.
```

The clean repair is **not** to promote `P1-candidate` into a theorem. Freeze is edit-safety, not epistemic truth.

### 3.2 `SRT_Individuation.md`

Current typing:

```text
status = draft_v0
claim_mode = hybrid
role = downstream subject-position / self-consciousness model
```

The registry already says:

```text
One_Formation owns formed One / Selection-position;
P1-T06 owns stronger Stable-ISP standing;
Individuation is downstream and may not use sigma_sr / sigma_sr^sub to define One.
```

Its own R1 boundary note says legacy subject-entry / ISP-entry language remains pending later reconstruction. It therefore still needs controlled mutability.

Freezing it as an A-level canonical anchor would protect unresolved legacy language too strongly. Leaving it completely untyped, however, fails to distinguish a major core L1 model from ordinary freely editable text.

---

## 4. Key governance distinction

R2-C should explicitly separate two axes:

```text
Axis 1 — authority / claim hardness
canonical semantic owner | hybrid model | P1-candidate | P2 | P3/P4 | OPEN ...

Axis 2 — edit-safety / freeze class
Freeze A | Freeze B | runtime / navigation | unlisted
```

These axes are not equivalent.

Therefore:

```text
Freeze A does not mean theorem;
Freeze B does not mean noncanonical;
draft status does not mean freely rewritable if the file is already a registered semantic owner;
canonical semantic ownership does not require promoting every positive claim to P1 theorem status.
```

This distinction resolves F7 without a hidden claim-strength ratchet.

---

## 5. Recommended F7 disposition

### Option A — split edit-safety by owner role **[RECOMMENDED]**

```text
SRT_One_Formation.md
- authority: KEEP current local canonical semantic owner role;
- claim hardness: KEEP status=draft, claim_level=P1-candidate;
- freeze: RETYPE -> Freeze A;
- reason: frozen spine delegates current One definition here, so silent rewrites must require explicit authorization.

SRT_Individuation.md
- authority: KEEP / RETYPE only as downstream hybrid subject-position model already described by registry;
- claim hardness: unchanged; no subject theorem promotion;
- freeze: RETYPE -> Freeze B;
- reason: important core L1 model requiring cross-check, but unresolved sigma / subject-entry language must remain reconstructible.
```

Add one governance note:

```text
freeze class controls edit safety only and does not upgrade P-level, canonical truth, theorem status or Level standing.
```

### Option B — protect One owner only; leave Individuation explicitly OPEN

```text
One_Formation -> Freeze A;
Individuation freeze classification -> OPEN / unlisted pending subject reconstruction.
```

This is defensible and narrower, but it leaves a major downstream local model outside A/B even though the registry routes subject-position questions to it.

### Option C — ledger only; defer F7

```text
create F3 ledger;
leave freeze lists untouched;
F7 remains OPEN;
R2-C remains incomplete.
```

This is maximally conservative but does not close the current programme gate.

---

## 6. F3 seed policy

The initial ledger may import only dispositions that are **already paid** by current author/canonical state. Importing them is not a new reverse audit.

Safe initial rows include the already-recorded #931/#933 supersessions:

```text
history-to-reconstitution = Bearer definition -> RETIRE;
first constitutive history coupling = Bearer onset -> RETIRE;
SC > generic Bearer -> RETIRE;
self-consequence closure as a relation -> RETYPE as retrospective self-effect closure;
matched-history tests -> RETYPE as retrospective dependence tests;
PH-IND02 PERS-2 -> RETYPE as retrospective consequence/history relation family.
```

F7 rows should remain `OPEN / AUTHOR GATE` until the author selects an option.

---

## 7. What R2-C does not authorize

Even if Option A is selected, R2-C still does not itself authorize:

```text
claim-by-claim old-canonical reverse audit beyond imported already-adjudicated rows;
L0 canonical rewrite;
Individuation subject-threshold repair;
Bearer -> actual 承担 / concern / agency / subject / cognition / phenomenality closure;
formal P+E N&S theorem;
independently applicable E admission criterion;
new Level 1;
Level 2 exit;
scientific distinctiveness;
whole-architecture non-substitutability.
```

After R2-C closes, the old-canonical reverse audit may begin from the spine / ledger, with L0 body rewriting still blocked by #949.

---

## 8. Independent verdict

```text
F3 = READY TO LAND as audit infrastructure;
F7 = AUTHOR DECISION REQUIRED;
recommended author choice = A;
canonical theory edit = NOT REQUIRED for the gate itself;
freeze/governance edit = HOLD pending explicit author adjudication;
R2-C = NOT YET CLOSED;
```
