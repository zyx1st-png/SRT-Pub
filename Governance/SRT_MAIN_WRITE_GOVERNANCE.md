---
id: SRT-MAIN-WRITE-GOVERNANCE
type: governance_contract
status: active
date: 2026-09-24
updated: 2026-09-24
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency:
  - SRT-AUTHOR-ADJUDICATION-MAIN-WRITE-GOVERNANCE-20260924
  - SRT-EDIT-PROTOCOL
  - SRT-CANONICAL-FREEZE
  - SRT-AGENTS
tags: [Governance, Main, PullRequest, Authorization, Delegation, M0, M1, M2, Reconstructibility]
---

# SRT main write governance

> Core intuition: **generation may be free; sedimentation has a gate.**
>
> Operational corollary: **checks may be bypassed under bounded recovery authority; history may not be bypassed.**

This file controls authorization for writes that are intended to become inheritable repository state on `main`.

It is orthogonal to the A/B/C edit-risk classes in `SRT_EDIT_PROTOCOL.md`:

```text
A / B / C
= semantic/edit risk

M0 / M1 / M2
= authorization / adjudication mode
```

A change must be classified on both axes where both matter.

## 1. What `main` means

`main` is the repository's current effective, inheritable state.

Landing on `main` does **not** imply:

- eternal truth;
- canonical status;
- scientific validation;
- irreversibility.

It does imply:

- later agents may treat the landed state as current unless a stronger owner says otherwise;
- supersession must itself be reconstructible;
- the state transition must have an identifiable provenance path.

## 2. Default path

Normal state-changing work uses:

```text
generation / analysis
-> branch
-> commit
-> pull request
-> applicable checks / review
-> merge
-> inheritable main state
```

Direct push to `main` is not a normal workflow, including for the repository owner.

Automation may create commits and PRs. Automation should not use direct `main` writeback as the ordinary path.

## 3. M0 — reconstruction / mechanical closure

M0 applies when the write introduces no new interpretive or authorial choice.

Typical examples:

- deterministic regeneration by the owning generator;
- hash / index / bundle freshness restoration;
- typo / broken-link correction;
- path synchronization after an already-decided move;
- mechanical replacement of an already-authorized identifier;
- generated derivative refresh;
- purely mechanical CI/config closure that does not weaken a gate.

Requirements:

1. no new theory meaning;
2. no new programme state;
3. no new authority transition;
4. no new external commitment;
5. owning deterministic checks pass where applicable.

Merge authorization:

```text
checks pass
-> may auto-merge / machine-merge
```

A PR transition record should still exist for `main` writes.

## 4. M1 — delegated adjudication

M1 applies when complex interpretation is required but the decision space was already frozen and explicitly delegated.

M1 is allowed only when all of the following are true:

1. trigger conditions were fixed before the result;
2. allowed verdicts are finite or otherwise bounded;
3. the consequence of each relevant verdict was fixed in advance;
4. execution does not invent a new concept, criterion, owner, option or programme route;
5. an independent reviewer can check fidelity against the frozen rule.

Example shape:

```text
frozen rule
+ evidence
-> executor verdict
-> independent fidelity review
-> pre-authorized consequence
```

Independent review is not majority voting. Its job is to check:

- source / evidence fidelity;
- frozen-rule fidelity;
- criterion drift;
- conclusion widening;
- omitted counterevidence;
- whether the claimed consequence actually follows from the frozen verdict.

If executor and reviewer materially disagree on the verdict or rule meaning, do not vote. Escalate to M2.

Merge authorization:

```text
frozen delegation valid
+ executor result
+ independent fidelity PASS
+ no M2 trigger
-> may merge without a new author reply
```

## 5. M2 — explicit authorial choice

M2 applies when the repository would need a genuinely new choice rather than execution of an already-bounded choice.

M2 triggers include any unpreauthorized:

- new option or branch of action;
- new criterion / decision rule;
- new term-of-art or concept intended to harden;
- new owner;
- change of canonical / programme / OPEN authority;
- change of CURRENT NEXT;
- programme opening / closure not already dictated by a frozen rule;
- substantive supersession decision;
- external commitment, publication, destructive action or visibility change;
- interpretation required to resolve a material executor/reviewer disagreement.

M2 requires an **explicit author reply**.

Do not infer M2 authorization from:

- historical preference;
- long-run author direction;
- model confidence about what the author would choose;
- a bare `继续` while a choice remains open;
- model agreement.

The author reply may be natural language. It does not require a special syntax. It must make the selected direction sufficiently clear to reconstruct:

```text
what was authorized?
what was not authorized?
```

Where practical, preserve the author wording as A0-Q and separately record the bounded machine interpretation.

## 6. Bounded reusable authorization

An explicit M2 authorization may be reused without repeated confirmation when the implementation remains inside the authorized package.

Record or reconstruct four fields:

```text
Goal
Scope
Exclusions
Stop condition
```

Routine implementation choices inside those bounds do not require a new author message.

Authorization does not silently transfer across:

- repositories;
- programmes;
- experiments;
- external actions;
- theory owners.

Principle portability does not imply authorization portability.

Authorization expires when any of the following occurs:

1. the goal is complete;
2. scope is exceeded;
3. new evidence defeats a prerequisite of the authorization;
4. the author explicitly supersedes or revises it.

## 7. Automatic M1 -> M2 escalation

Before completing M1, ask:

> Can this task be completed without inventing a new option, criterion, concept, owner, authority transition, or external commitment?

If no, escalate to M2.

If uncertain whether the implementation is still rule execution or has become choice generation, treat it as M2.

## 8. Bare continuation

For write authorization:

```text
bare “继续”
-> inherits an already-authorized direction
-> permits routine bounded implementation
-> does not close an open M2 fork
```

If the immediately controlling surface still contains unresolved author options, continuation alone does not select one.

## 9. Merge eligibility vs merge authorization

Keep these separate:

```text
merge eligibility
= checks / consistency / review requirements are satisfied

merge authorization
= the relevant M0 / M1 / M2 authority exists
```

Policy:

- M0: eligible changes may auto-merge;
- M1: eligible + independent fidelity PASS may auto/machine-merge;
- M2: eligible + valid explicit author authorization + faithful implementation may machine-merge; the author need not personally press merge.

A green CI state never creates M2 authorization.

## 10. Emergency / recovery bypass

Repository administration may require recovery from a broken ruleset, CI deadlock or governance-control failure.

The preferred recovery path remains a PR.

If platform controls allow an administrator to bypass checks, use the narrowest recovery authority available and preserve:

- the PR;
- the recovery reason;
- changed paths;
- the check or rule bypassed;
- a post-recovery verification that normal protection is restored.

The governing principle is:

> **checks may be bypassed; history may not be bypassed.**

A recovery bypass must not be used as a convenience path for ordinary theory or programme writes.

## 11. GitHub platform target

The repository policy target is owned by:

`Governance/SRT_MAIN_PLATFORM_PROTECTION_TARGET_2026-09-24.md`

Repository documents are not evidence that GitHub settings are active. Platform state is the final fact source for branch/ruleset enforcement.

Until platform protection is actually enabled, agents must report the gap rather than claiming `main` is protected.

## 12. Relation to canonical edit rules

This governance contract does not weaken:

- `SRT_CANONICAL_FREEZE.md`;
- C-class independent semantic review;
- current owner / source / OPEN checks;
- generated-file owner discipline;
- programme-specific preregistration / stop-loss rules.

A C-class edit may also be M2. These are different axes.

## 13. Minimal provenance chain

For M2 semantic/state changes, the preferred reconstructible chain is:

```text
explicit author reply
-> author/source record or exact trace
-> bounded authorization interpretation
-> implementation PR
-> independent fidelity review where required
-> merge
```

For M1:

```text
prior authorization
-> frozen rule
-> evidence
-> executor verdict
-> independent fidelity review
-> pre-authorized consequence
-> merge
```

Do not silently upgrade machine analysis into author authority anywhere in these chains.
