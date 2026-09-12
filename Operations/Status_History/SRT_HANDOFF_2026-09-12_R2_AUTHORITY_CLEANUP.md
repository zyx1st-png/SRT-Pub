---
id: SRT-HANDOFF-2026-09-12-R2-AUTHORITY-CLEANUP
type: status_handoff
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
date: 2026-09-12
---

# SRT session handoff — R2 authority cleanup

> Snapshot only. Re-fetch live `main`, open PRs and `STATUS.md` before acting. This file records session state; it does not change canonical authority or close any theory gate.

## 1. Live baseline at handoff

```text
repository = zyx1st-png/SRT-Pub
main = 421edf1f47b414eb527beb18eafb1a2093ae30d9
main latest record = retrospective independent review of PR #947
```

`STATUS.md` on `main` is still dated 2026-09-11 and still describes the post-#947/#948 phase. It has not yet been refreshed for #949–#952.

## 2. Open PRs that control the next step

### PR #951 — record-layer author-adjudication calibration

```text
state = OPEN / DRAFT
scope = one audit file only
purpose = fold the accepted author calibration of #950 into the retrospective #947 review record
```

Required grouping in the final record:

```text
R2-A = F1 / F4 / F6 / F8 / F10 / F11
R2-B = F2 / F5 / F9
R2-C = F3 / F7
```

The record must keep these calibrations:

- `482 bearer files` = legacy occurrence surface, not 482 proven contradictions;
- pre-#947 `bearer` must not be auto-read as post-#947 P+E `Bearer`;
- retyping is claim-by-claim, never bulk replacement;
- #947 canonical routing is LANDED; runtime authority propagation was incomplete;
- no L0 canonical rewrite is authorized before the #949 creator–AI final-skeleton alignment gate.

Before merge: verify the current final head and current Governance Preflight result again; do not rely on an earlier green run if the head changed.

### PR #952 — R2-A authority truth-up

```text
state = OPEN / DRAFT
head branch = governance/r2a-authority-truth-up-20260912
snapshot head = fb1dec33377b97a6d48d919e8eef99b0eb9204ea
scope = F1 / F4 / F6 / F8 / F10 / F11 only
merge posture = DO NOT FAST-MERGE
```

Implemented direction:

- `CANONICAL_REGISTRY.md §C` is the only complete citation-priority owner;
- runtime/bootstrap surfaces may point to or project Registry, but must not maintain another complete competing chain;
- cross-owner ontology routing remains `Registry -> Generative Ontology Spine -> compatible local owners`;
- `One_Formation` is local One-formation elaboration within the spine, not a second owner of the whole formation order;
- the quotable Bearer shortcut restores the formed-One / Selection-position precondition;
- context-bundle authority parsing reads Registry §C directly;
- a permanent authority-routing regression checker is included;
- SPINE remains a curated/budgeted projection, not a false complete closure.

The branch's own full preflight passed before the Draft PR was opened, but #952 still requires an independent content review of the final head before merge.

## 3. Work not yet authorized / not yet started

Do not skip ahead from this handoff:

```text
R2-B = Bearer semantic quarantine / claim-hardness cleanup
  F2 legacy bearer disambiguation
  F5 E consistency-test vs independently applicable criterion
  F9 routing strength vs theorem strength

R2-C = supersession infrastructure
  F3 per-claim retyping ledger
  F7 local-owner authority / freeze typing
```

These come after R2-A is independently reviewed and dispositioned.

## 4. L0 hard gate

PR #949 established the B+ research direction, but the final L0 skeleton is not yet authorized for canonical rewrite.

Preferred current architecture remains:

```text
L0:
minimum non-neutrality / pre-object difference
-> subjectless active Selection
-> manifestation + relative backgrounding
-> active verticalization / non-flat differentiation
+ finite positionality
+ minimal historical asymmetry / non-equivalence to never-occurrence

then downstream:
verticality + recurrence / re-entry / lineage -> One / Selection-position
formed One + P + E -> Bearer routing direction
Bearer -> 承担 / concern / agency / subject / cognition / phenomenality = separately OPEN
```

Critical distinctions:

- L0 activity != agency / volition / subject initiative;
- L0 active verticalization != recurrent formed vertical organization != One;
- κ₀ / ε / cost / P0-04 are not automatically retained as independent L0 primitives;
- minimal historical asymmetry should not be inflated into a strong physical irreversibility / Landauer / granular-time theorem.

Before any L0 canonical rewrite, perform the creator–AI final-skeleton alignment gate from #949. Do not infer final author commitment from B+ shorthand, review consensus, repository smoothness, or absence of objections.

## 5. Exact next-session route

```text
1. AGENTS.md §Session Start bootstrap.
2. Re-fetch live main, STATUS.md and open PRs.
3. Inspect #951 final head + latest Governance Preflight.
4. If #951 is clean and matches the grouping above, merge/close out its provenance layer.
5. Rebase or re-audit #952 against the resulting main if needed.
6. Perform independent content review of #952 final head.
7. Resolve review findings; only then decide whether R2-A merges.
8. Do not start R2-B or L0 canonical rewrite before those gates are cleared.
```

## 6. Programme guards

```text
new Level 1 = NOT ASSIGNED
Level 2 = HOLD
scientific distinctiveness = NOT ESTABLISHED
whole-architecture non-substitutability = NOT ESTABLISHED
research_mode = U
```
