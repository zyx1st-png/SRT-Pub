---
id: SRT-OPS-AUDIT-PRIMITIVE-ROLE-EXHAUSTIVENESS-ADJUDICATION-20260819
type: audit_record
status: active
record_stage: final_review_corrected_adjudication
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

> **Purpose**: resolve the fairness tension exposed by the merged derivational-surplus and exclusion-surplus audits. This is a governance attribution ruling only. It does not change P0-01, create a new axiom, demote Selection, reopen RC-A / Phase 0.5, or authorize a new Selection Grammar.

---

## 0. Executive adjudication

Current canonical P0-01 contains, among its positively load-bearing content, two distinguishable components relevant to this audit:

```text
R = audit-isolated AM-A minimal actualisation role
    non-objectified potential difference
    -> determinate manifest actuality

E = Selection-first existence / exhaustiveness commitment
    Selection precedes existence
    existence is an image of Selection
    exists x iff x in Range(G-hat)
```

Canonical source: `Core/SRT_Core_21_Minimal_Axioms.md`, P0-01 formal definition / range biconditional for `E`, and the AM-A minimum actualisation kernel for `R`.

**Canonical guard**:

```text
full current canonical P0-01 contains R and E,
plus restrictive scope / boundary riders that carry no additional
positive derivational load in this adjudication.
```

`R` is **not** proposed as a replacement definition of canonical Selection, and this audit does not split P0-01 into two canonical axioms. `R` is isolated only for derivational burden accounting because canonical P0-01 itself identifies an AM-A minimum actualisation kernel inside the fuller primitive package.

For **canonical storage**, no split is made here: the current P0-01 remains intact.

For **derivational attribution and rival fairness**, however, the audit must not silently transfer conclusions between the minimal kernel and the fuller package.

```text
R -> E = not currently established
```

This is an epistemic / audit-status statement. It is **not** an asserted logical independence theorem and must not be rewritten as `R -/-> E`.

Therefore:

```text
E-derived consequences
must not be scored as
minimal-kernel-R-specific derivational surplus.
```

This resolves the apparent conflict in the merged duel freeze between:

1. the background-fairness rule forbidding a target-bearing premise from being granted only to SRT and then counted as surplus; and
2. the rule that frozen V2-PAR does not automatically receive an `exists x iff x in Range(A)` biconditional.

Both rules can stand once the level of attribution is explicit.

---

## 1. Why `R` and `E` are separately tracked for audit purposes

### 1.1 Canonical co-location does not imply derivation

`Core/SRT_Core_21_Minimal_Axioms.md` P0-01 places the Selection-first existence / range commitment and the AM-A minimum actualisation kernel inside the same canonical primitive entry. Canonical co-location does not by itself establish a derivation from the minimum kernel to the stronger exhaustiveness / precedence commitment.

This is an **audit decomposition**, not a canonical ontology decomposition.

### 1.2 Frozen rival work supplies an audit representation, not an independence demonstration

Frozen V2-PAR was stipulated to preserve the target transition:

```text
non-objectified potential difference
-> determinate manifest actuality
```

without being granted:

```text
exists x iff x in Range(A)
```

The corrected #839 execution explicitly withdrew that biconditional as an off-spec addition. The subsequent #842 review showed that attempting to score the one-sided biconditional as rival-specific X1 surplus violates background fairness when the target depends on exactly that one-sided premise.

This does **not** prove that `R` is logically consistent with `not-E`, nor does it provide a formal independence proof. The frozen comparison simply supplies an audit representation in which the minimal actualisation role and the exhaustiveness commitment are not treated as the same scored premise.

That is sufficient for the narrower governance requirement:

```text
until R -> E is actually established,
do not attribute an E-carried result to R alone.
```

### 1.3 What is NOT concluded

This adjudication does not conclude:

```text
E is false
E should leave P0-01
R is the whole canonical Selection primitive
R is more fundamental than E
R and E are formally independent
V2-PAR has reduced Selection
Selection is dispensable
```

It only states that the current audit record has not established `R -> E`.

---

## 2. Two legal comparison / attribution modes

Future audits in this workline must declare one of the following modes before inspecting outcomes.

### Mode R — minimal actualisation-role attribution

Question:

> Does the audit-isolated AM-A minimal actualisation role itself yield a consequence unavailable to a role-matched rival?

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

**Scope guard**: `Mode R` is a Selection-related audit only because `R` is the canonically identified AM-A minimum kernel inside P0-01. A Mode-R result is not a result about the whole Selection primitive package unless the mode and the narrower premise set are restated alongside it.

### Mode P0-01 — full canonical primitive-package attribution

Question:

> What follows from SRT's full current P0-01 primitive package, including E and its restrictive boundary riders?

Use the current canonical P0-01 as the SRT object of attribution. For the positive derivational content at issue here, this includes `R + E`.

A rival may be compared with or without an analogous `E_rival`, but that comparison must be frozen **before** the target is evaluated.

In Mode P0-01:

- consequences carried by `E` may be recorded as **package-attributed consequences**;
- they must not be relabeled as R-specific surplus;
- if the rival lacks `E_rival`, the difference is an **explicit axiom/package burden difference**, not a fair-duel victory by itself;
- merely declaring `comparison_mode: P0-01` does not cure a one-sided target-bearing premise;
- if robustness matters, a strengthened rival `V2 + E_rival` must be declared prospectively and tested separately rather than added ad hoc after outcome inspection.

**Allowed non-comparative attribution label**:

```text
P0-01 PACKAGE CONSEQUENCE — ATTRIBUTABLE TO E
```

**Forbidden comparative inference without further work**:

```text
AM-A minimal actualisation role uniquely derives this
SRT defeats the role-matched rival because E was present only on the SRT side
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

A one-sided substantive commitment may be part of the SRT package being described, but its consequences must be **burden-attributed**, not treated as if they emerged from a matched minimal actualisation role or as a fair rival victory.

So:

```text
(R + E) -> target
R_v2 does not carry E_rival
```

may support the non-comparative statement:

```text
target is carried by the stronger SRT package under the declared premises.
```

It does **not** by itself support:

```text
R has unique derivational surplus
Selection is empirically or ontologically superior
V2 is defeated
```

For rival-comparative robustness of an E-carried target, prospectively freeze a symmetric strengthened rival such as `V2 + E_rival` before target inspection.

---

## 4. No-biconditional rule — clarified

The #839 rule that V2-PAR may not acquire a range biconditional after seeing the target remains correct.

The correction is interpretive:

```text
no automatic V2 biconditional
!=
permission to score SRT's one-sided biconditional as R-level surplus
or as an automatic full-package duel victory.
```

For Mode R, neither side may use E-type exhaustiveness to win the minimal-role comparison.

For Mode P0-01, SRT may use canonical E for internal package attribution because full P0-01 is the declared object. If rival robustness is tested, the strengthened rival must be frozen prospectively as a separate rival variant.

This reconciles the two merged #839 rules without editing either historical record.

---

## 5. Re-adjudication of current results

### 5.1 C1-C6 additive battery

**No verdict change and no weakening of the merged negative.** The corrected #839 battery ran the SRT side at canonical P0-01 strength, including both the AM-A minimum kernel and the Selection-first precedence / range biconditional.

Authoritative merged result:

```text
C1-C6 additive surplus
(tested at full current R+E package strength)
= not established
```

This adjudication must not relabel that full-package negative as merely an R-level null. In particular, a future `comparison_mode: P0-01` audit may not reopen C1-C6 on the claim that #839 tested only Mode R.

Where a narrower Mode-R bookkeeping question is asked later, the mode must be stated explicitly and may not replace the stronger historical fact above.

### 5.2 X0 no-prior-chooser

X0 remains a legitimate SRT-side ordering consequence in the full P0-01 package and is canonically attributed to P0-01 ordering.

For rival discrimination:

```text
Mode R: Outcome C / role-isomorphic
Mode P0-01: the SRT-side ordering consequence may be burden-attributed to E,
             but the one-sided E difference is not a fair rival victory.
```

No Selection-specific D2 follows.

### 5.3 X1 causality

The merged #842 result remains unchanged:

```text
instantiated-causality reading = Outcome C / role-isomorphic
pre-objective-propensity reading = invalid surplus under fairness
```

The second branch failed because the comparison scored SRT at the stronger `R + E` package against a rival frozen at the matched minimal role without `E_rival`, while the target depended on the one-sided E-type premise. The defect was therefore a **level / premise-assignment mismatch across the two sides**, not that #842 had mislabeled itself as an R-specific audit.

Merely declaring a future comparison `Mode P0-01` does not rehabilitate that result. Specifically:

```text
X1-P remains invalid as a rival-comparative surplus result.
```

This adjudication does **not** relabel X1-P as a citable `P0-01 PACKAGE CONSEQUENCE`. A future non-comparative package-attribution audit could separately ask what E entails, but any rival-comparative robustness claim would require a prospectively frozen `V2 + E_rival` construction.

### 5.4 X2 information readout

No change:

```text
Outcome C / role-isomorphic
```

The narrow readout ordering follows from the shared primitive actualisation role on both sides.

### 5.5 Current overall status

```text
full current canonical P0-01 remains unchanged
and contains R + E plus restrictive boundary riders

R -> E = not currently established
(this is not an independence theorem)

C1-C6 additive surplus
(tested at full current R+E package strength)
= not established

R-specific derivational surplus over frozen role-matched V2
in the separately audited role-level targets
= not established

X0 = Mode-R Outcome C / full-package ordering consequence without fair-duel victory
X1-I = Outcome C
X1-P = invalid surplus under fairness; not rehabilitated here
X2 = Outcome C

Selection primitive role residue = P unresolved primitive admission
Selection-level D2 count = 0
PD-A mature-null/rival-equivalent scoreboard increment = 0
```

**Quotation guard**: `Mode R` and `not R-attributable` are premise-attribution labels. Neither is a statement about the whole canonical Selection primitive unless the mode and premise set are restated explicitly.

---

## 6. Research-program consequence

The immediate next move is **not** another X3/C7 search.

Any future fruitfulness duel must first declare:

```text
comparison_mode: R | P0-01
```

and must attribute every claimed consequence to the narrowest premise set that actually carries it.

Use:

```text
comparison_mode: R
```

when the research question is specifically whether the **AM-A minimal actualisation kernel** earns distinctive explanatory load against a role-matched rival.

Use:

```text
comparison_mode: P0-01
```

when the research question concerns the stronger **full canonical Selection-first primitive package**, including the existence / exhaustiveness commitment and its burden.

Neither mode is the universal default. The question being asked fixes the mode before outcome inspection.

This PR does not execute a `V2 + E_rival` duel; it only specifies how such a rival would have to be frozen if a later, separately authorized package-robustness question genuinely requires it.

---

## 7. Stop rule

Stop with this attribution ruling.

Do not:

- edit P0-01 in this PR;
- split P0-01 canonically into two axioms;
- redefine canonical Selection as R alone;
- grant or remove a rival biconditional retrospectively;
- execute a `V2 + E_rival` duel in this pass;
- add X3/C7;
- open a D2 workline;
- infer redundancy or demotion from the lack of R-level surplus;
- infer any RC-A or Phase 0.5 change from this bookkeeping ruling.

A later canonical refactor, if ever desired, requires a separate author decision and must distinguish **canonical organization** from **derivational burden accounting**.

**Final disposition:** `R/E BURDEN-ACCOUNTING SPLIT ADOPTED / CANONICAL P0-01 UNCHANGED AND CONTAINS R+E PLUS RESTRICTIVE RIDERS / R->E NOT CURRENTLY ESTABLISHED (NOT AN INDEPENDENCE CLAIM) / C1-C6 FULL-PACKAGE ADDITIVE SURPLUS NOT ESTABLISHED / MODE R FOR MINIMAL-KERNEL ATTRIBUTION / MODE P0-01 FOR FULL-PACKAGE ATTRIBUTION / X0-X2 RESULTS UNCHANGED / SELECTION = P UNRESOLVED / D2 0 / PD-A +0 / RC-A AND PHASE 0.5 UNCHANGED / NO CANONICAL EDIT`.
