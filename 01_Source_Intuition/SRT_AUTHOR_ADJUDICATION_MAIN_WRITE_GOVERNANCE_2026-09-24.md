---
id: SRT-AUTHOR-ADJUDICATION-MAIN-WRITE-GOVERNANCE-20260924
type: author_adjudication
status: frozen
date: 2026-09-24
layer: source_intuition
epistemic_layer: author
claim_mode: author_adjudication
canonical: false
tags: [Governance, Main, Authorization, Delegation, M0, M1, M2, Reconstructibility]
---

# Author adjudication — main write governance and delegated adjudication

## 0. Scope

This record preserves the explicit author choices made during the 2026-09-24 discussion about how repository state should enter `main`.

It governs repository write authorization and provenance. It does not define SRT ontology and does not authorize unrelated theory, experiment, publication, or external action.

## 1. Author source

The following are direct author replies from the governing dialogue.

### A0-Q1 — delegated interpretive adjudication may proceed without repeated author confirmation

> “能”

Context resolved in the dialogue: when an interpretive decision is already governed by a frozen rule and receives an independent fidelity review, it may be landed without returning to the author for another confirmation.

### A0-Q2 — new authorial choices require explicit reply

> “认同，继续，需要显性回复，方便对齐想法”

Author meaning accepted in dialogue:

- an M2 authorial choice must not be inferred from historical preference, long-run direction, or likely intent;
- the explicit reply is valuable both for governance provenance and for exposing current author intuition.

### A0-Q3 — authorization may be bounded but reusable

> “认同，继续”

Context resolved in the dialogue: once an explicit author choice establishes a bounded goal, scope, exclusions and stop condition, routine implementation inside that authorization does not require repeated confirmation. A new semantic choice reopens M2.

### A0-Q4 — merge execution need not be performed personally by the author

> “认同”

Context resolved in the dialogue: M2 requires a valid explicit author authorization, but the author does not need to press the merge button personally after faithful implementation and review.

## 2. Author-approved governance direction

The author accepted the following direction:

1. generation should remain comparatively free in branches, Draft PRs, experiments and dialogue;
2. `main` is the current inheritable repository state, not a claim of eternal truth;
3. state-changing writes should pass through an explicit, reconstructible transition boundary;
4. author authority and direct-push ability are distinct;
5. checks may be bypassed for recovery where explicitly allowed, but repository history / provenance must not be bypassed;
6. machine reasoning may be deep, but it must not silently enlarge the authorized decision space;
7. explicit author authorization is required for a genuinely new M2 choice;
8. prior authorization may be reused only within its bounded object, scope and stop condition;
9. independent review is an anti-drift / fidelity check, not majority voting and not a substitute for author convergence where M2 is open.

## 3. Bare “继续” boundary

This adjudication narrows the repository-wide interpretation of bare continuation for authorization purposes:

```text
bare “继续”
-> may continue an already authorized route
-> may execute routine bounded implementation
-> does not resolve a still-open M2 fork
-> does not create a new owner / criterion / concept / programme / authority transition
```

This is a write-authorization rule. Topic-specific acceptance semantics may still be recorded elsewhere, but they cannot be used to infer an unspoken M2 decision.

## 4. Non-actions

This adjudication does not itself:

- modify any SRT canonical theory owner;
- alter current GRG research disposition;
- authorize a new experiment;
- authorize publication or external communication;
- make GitHub platform protection active;
- convert a machine conclusion into author evidence.

Implementation is owned by `Governance/SRT_MAIN_WRITE_GOVERNANCE.md`.
