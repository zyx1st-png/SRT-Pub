---
id: SRT-OPS-AUDIT-PRIMITIVE-ROLE-EXHAUSTIVENESS-ADJUDICATION-20260819
type: audit_record
status: active
record_stage: adjudicated
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-08-19
dependency:
  - SRT-CORE-21A-MINIMAL-AXIOMS
  - SRT-OPS-AUDIT-SELECTION-PRIMITIVE-DERIVATIONAL-SURPLUS-DUEL-SPEC-20260819
  - SRT-OPS-AUDIT-SELECTION-PRIMITIVE-DERIVATIONAL-SURPLUS-DUEL-EXECUTION-20260819
  - SRT-OPS-AUDIT-SELECTION-EXCLUSION-SURPLUS-X1-X2-SPEC-20260819
  - SRT-OPS-AUDIT-SELECTION-EXCLUSION-SURPLUS-X1-X2-EXECUTION-20260819
tags: [Selection, PrimitiveRole, Exhaustiveness, Precedence, Range, RivalFairness, GOV_SUB01]
---

# Primitive Role vs Exhaustiveness / Precedence — Governance Adjudication

> **Purpose**: resolve the fairness tension exposed by the merged derivational-surplus and exclusion-surplus audits. This is a governance attribution ruling only. It does not change P0-01, create a new axiom, demote Selection, or authorize a new Selection Grammar.

---

## 0. Executive adjudication

Current canonical P0-01 packages two kinds of content together:

```text
R = primitive actualisation role
    non-objectified potential difference
    -> determinate manifest actuality

E = Selection-first existence / exhaustiveness commitment
    Selection precedes existence
    existence is an image of Selection
    exists x iff x in Range(G-hat)
```

For **canonical storage**, no split is made here: both remain inside current P0-01.

For **derivational attribution and rival fairness**, however, they must be accounted separately.

```text
R -/-> E   (not currently established)
```

Therefore:

```text
E-derived consequences
must not be scored as
primitive-role-R-specific derivational surplus.
```

This resolves the apparent conflict in the merged duel freeze between:

1. the background-fairness rule forbidding a target-bearing premise from being granted only to SRT and then counted as surplus; and
2. the rule that frozen V2-PAR does not automatically receive an `exists x iff x in Range(A)` biconditional.

Both rules can stand once the level of comparison is explicit.

---

## 1. Why `R` and `E` are separable for audit purposes

### 1.1 Canonical co-location does not imply derivation

P0-01 currently states both the Selection-first existence claim and the AM-A primitive actualisation kernel. Co-location inside one canonical axiom entry does not by itself prove that the exhaustiveness / precedence content follows from the minimum actualisation role.

### 1.2 Existing rival work already demonstrates logical room between them

Frozen V2-PAR preserves the target transition:

```text
non-objectified potential difference
-> determinate manifest actuality
```

without receiving:

```text
exists x iff x in Range(A)
```

The corrected #839 execution explicitly withdrew that biconditional as an off-spec addition. The subsequent #842 review showed that attempting to score the one-sided biconditional as X1 surplus violates background fairness when the target depends on exactly that one-sided premise.

This establishes an audit fact, not a metaphysical reduction:

```text
primitive actualisation role can be represented in the frozen comparison
without already carrying E.
```

That is sufficient to require separate burden accounting.

### 1.3 What is NOT concluded

This adjudication does not conclude:

```text
E is false
E should leave P0-01
R is more fundamental than E
V2-PAR has reduced Selection
Selection is dispensable
```

It only states that the current audit record has not established `R -> E`.

---

## 2. Two legal comparison modes

Future audits must declare one of the following modes before inspecting outcomes.

### Mode R — primitive-role comparison

Question:

> Does the primitive actualisation role itself yield a consequence unavailable to a role-matched rival?

Use:

```text
SRT side: R + shared B'
Rival side: R_v2 + same shared B'
```

where `R_v2` is the already-frozen pre-objective actualisation role.

In Mode R:

- `E` may remain true in canonical SRT, but it is **not an admissible scored premise** for establishing R-specific surplus;
- a consequence that needs `E` fails the R-level primitive-link attribution;
- V2-PAR does not need to be granted a range biconditional, because the comparison is not allowed to score SRT's range biconditional either;
- noun substitution into a generic existence-ordering schema does not create a new R-level surplus.

**Required label** if `E` is needed:

```text
NOT R-ATTRIBUTABLE / REQUIRES SEPARABLE E COMMITMENT
```

### Mode P0-01 — full-package attribution

Question:

> What follows from SRT's full current P0-01 package, including E?

Use:

```text
SRT package = R + E
```

A rival may be compared with or without an analogous `E_rival`, but this must be frozen **before** the target is evaluated.

In Mode P0-01:

- consequences of `E` may be recorded as **package-attributed consequences**;
- they must not be relabeled as R-specific surplus;
- if the rival lacks `E_rival`, the difference is an **explicit axiom/package burden difference**, not a fair-duel victory by itself;
- if robustness matters, a strengthened rival `V2 + E_rival` must be declared prospectively and tested separately rather than added ad hoc after outcome inspection.

**Allowed label**:

```text
P0-01 PACKAGE CONSEQUENCE — ATTRIBUTABLE TO E
```

**Forbidden label without further work**:

```text
primitive Selection role uniquely derives this
```

---

## 3. Background-fairness rule — clarified

The merged fairness rule remains valid but is now level-indexed.

### 3.1 For Mode R

A claimed R-specific surplus is invalid if SRT uses a target-bearing premise not contained in R and not symmetrically present in the rival comparison.

Thus:

```text
R + E -> target
```

cannot be cited as:

```text
R -> target.
```

### 3.2 For Mode P0-01

A one-sided substantive commitment may be part of the object being compared, but its consequences must be **burden-attributed**, not treated as if they emerged from a matched primitive role.

So:

```text
(R + E) -> target
R_v2 -/-> target
```

supports only:

```text
target is a consequence of the stronger SRT package under this frozen comparison.
```

It does not by itself support:

```text
R has unique derivational surplus
Selection is empirically or ontologically superior
V2 is defeated.
```

---

## 4. No-biconditional rule — clarified

The #839 rule that V2-PAR may not acquire a range biconditional after seeing the target remains correct.

The correction is interpretive:

```text
no automatic V2 biconditional
!=
permission to score SRT's one-sided biconditional as R-level surplus.
```

For Mode R, neither side may use E-type exhaustiveness to win the role comparison.

For Mode P0-01, SRT may use canonical E because full P0-01 is the declared object of attribution. If a strengthened rival is needed, it must be frozen prospectively as a separate rival variant.

This removes the previous apparent contradiction without editing the merged historical records.

---

## 5. Re-adjudication of current results

### 5.1 C1-C6 additive battery

No change:

```text
C1-C6 additive R-level surplus = not established
```

Some SRT-side consequences remain primitive-linked at the role level (for example the narrow manifest-event admission), but no discriminating R-level surplus over role-matched V2 was established.

### 5.2 X0 no-prior-chooser

X0 remains a legitimate SRT-side ordering consequence in the full P0-01 package and is canonically attributed to P0-01 ordering.

For rival discrimination:

```text
Mode R: Outcome C / role-isomorphic
Mode P0-01: package consequence may be attributed to E,
             but this is not R-specific surplus.
```

No Selection-specific D2 follows.

### 5.3 X1 causality

The merged #842 result remains unchanged:

```text
instantiated-causality reading = Outcome C / role-isomorphic
pre-objective-propensity reading = invalid surplus under fairness
```

This adjudication explains why the second branch is invalid: it attempted to score E as if it were R-specific surplus.

### 5.4 X2 information readout

No change:

```text
Outcome C / role-isomorphic
```

The narrow readout ordering follows from the shared primitive actualisation role on both sides.

### 5.5 Current overall status

```text
Selection primitive role = P unresolved primitive admission
R-specific derivational surplus over frozen role-matched V2 = not established
P0-01 package contains additional E burden / commitment
Selection-level D2 count = 0
PD-A mature-null/rival-equivalent scoreboard increment = 0
```

---

## 6. Research-program consequence

The immediate next move is **not** another X3/C7 search.

Any future fruitfulness duel must first declare:

```text
comparison_mode: R | P0-01
```

and must attribute every claimed consequence to the narrowest premise set that actually carries it.

The recommended default for testing whether the **primitive role currently named Selection** earns distinctive explanatory load is:

```text
comparison_mode: R
```

because this prevents package-level exhaustiveness from laundering itself into role-level surplus.

A full-P0-01 package audit is legitimate only when the research question is explicitly about the consequences and burden of the stronger Selection-first ontology as a package.

---

## 7. Stop rule

Stop with this attribution ruling.

Do not:

- edit P0-01 in this PR;
- split P0-01 canonically into two axioms;
- grant or remove a rival biconditional retrospectively;
- add X3/C7;
- open a D2 workline;
- infer redundancy or demotion from the lack of R-level surplus.

A later canonical refactor, if ever desired, requires a separate author decision and must distinguish **canonical organization** from **derivational burden accounting**.

**Final disposition:** `R/E AUDIT SPLIT ADOPTED / CANONICAL P0-01 UNCHANGED / MODE R DEFAULT FOR ROLE-SURPLUS CLAIMS / MODE P0-01 FOR PACKAGE ATTRIBUTION / EXISTING C1-C6 X0-X2 RESULTS UNCHANGED / SELECTION = P UNRESOLVED / D2 0 / PD-A +0 / NO CANONICAL EDIT`.
