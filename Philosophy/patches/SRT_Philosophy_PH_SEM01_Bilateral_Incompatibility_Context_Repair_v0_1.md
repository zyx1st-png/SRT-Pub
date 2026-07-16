---
id: SRT-PH-SEM01-BILATERAL-INCOMPATIBILITY-CONTEXT-REPAIR
type: material_patch
status: patch_v0_1
layer: bridge
epistemic_layer: bridge
claim_mode: bridge
claim_level: P3/P4
canonical: false
patch_id: SRT-PH-SEM01-BILATERAL-INCOMPATIBILITY-CONTEXT-REPAIR
source_ids:
  - SRC-2026-07-16-SEMANTICS-SIMONELLI-IMPLICATION-SPACE
domain: Philosophy of Language / Formal Semantics / Decision Scaffolding
target_future_doc:
  - _SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md
  - Core_Law/SRT_Occlusion_Dynamics.md
  - _SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md
  - Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md
related_claims:
  - positive commitment versus negative exclusion
  - false-dilemma detection
  - defeasible incompatibility and context repair
  - pathological closure
  - reselection through recomposition
tags: [bilateralism, incompatibility, assertion, denial, defeasibility, context-repair, ChoiceMap, occlusion, reselection]
---

# PH-SEM01 — Bilateral Incompatibility and Context Repair

## 1. Source anchor

Primary source:

- Ryan Simonelli, *Implication Space Semantics as Bilateral Incompatibility Semantics*.
- 40-page penultimate draft dated 2026-04-10; forthcoming in *Topoi*.
- Full-text close-read from a user-supplied PDF.
- SourceCard: `../../Materials/2026/SRC_2026_07_16_Semantics_Simonelli_Implication_Space.md`.

Simonelli interprets Kaplan's implication-space semantics as a bilateral incompatibility semantics. A position consists of assertions and denials; its semantic significance is represented by the positions with which it forms an incoherent or materially clashing position. The framework allows persistence to fail, so an apparent material clash can be repaired by adding exception information. Simonelli also argues that committive consequence cannot be reduced to incoherence alone.

## 2. Why this matters for SRT

SRT decision and objecthood work needs to distinguish:

```text
selecting A
!=
asserting everything associated with A
!=
denying every alternative to A
!=
closing every route back to non-A
```

A single output label hides several structurally different acts. Simonelli's bilateral framework supplies a disciplined semantic analogue for making those differences explicit.

The main bridge is:

```text
positive commitment
+ explicit denial
+ left-open alternatives
+ typed incompatibility
+ repair conditions
```

This patch does not define ontological selection and does not turn a linguistic position into a subject or stake-bearer.

## 3. Main bridge claims

### PH-SEM01.1 — A decision position is not exhausted by the selected label

For a practical position `Π`, use the bridge schema:

\[
\Pi=\langle A_\Pi,D_\Pi,O_\Pi,C_\Pi\rangle
\]

where:

- `A_Π`: commitments positively adopted;
- `D_Π`: commitments explicitly denied;
- `O_Π`: alternatives or questions intentionally left open;
- `C_Π`: context, bearer boundary and time horizon under which the position is evaluated.

This is an SRT-side schema, not Simonelli's original notation.

The schema prevents the following collapse:

```text
not selected
=> denied
=> incompatible
=> impossible to reopen
```

### PH-SEM01.2 — Incompatibility must be typed

At minimum, distinguish:

| Type | Meaning | Persistence expectation |
|---|---|---|
| `Inc_strict` | logical contradiction, verified physical impossibility or definition-level exclusion | normally persistent under added context |
| `Inc_def` | defeasible material clash under current defaults | may be repaired by exception information |
| `Inc_norm` | conflict under a rule or institution | depends on rule scope and revision authority |
| `Inc_identity` | conflict with a maintained identity closure | depends on bearer and continuity criteria |
| `Inc_script` | apparent conflict produced by current L2 framing | high-priority challenge target |

Simonelli's framework deliberately lets material persistence fail. SRT must not generalize that permission to strict contradiction or physical impossibility.

### PH-SEM01.3 — Reselection may occur through context repair

Let `I_def` be the set of defeasible clashes. Define a candidate repair set:

\[
\operatorname{Repair}(\Gamma)
=
\{E\mid \Gamma\in I_{def},\;\Gamma\cup E\notin I_{def}\}
\]

Examples of `E` in practical decision systems include:

- adding an exception condition;
- separating time horizons;
- modularizing a system;
- distinguishing roles or bearers;
- changing the relevant boundary;
- adding a compensating institution;
- replacing a binary category with a typed one.

This gives SRT a second reopening route:

```text
withdrawal / reversal
or
context enrichment / recomposition
```

### PH-SEM01.4 — Exclusion and implication are irreducible dimensions

Simonelli's conclusion rejects reducing committive consequence to incoherence. SRT should preserve:

```text
what a position rules out
!=
what a position positively commits the bearer to do next
```

Accordingly, a ChoiceMap record must contain both:

- incompatibility / denial fields;
- positive consequence / obligation / next-action fields.

An exclusion-only model cannot determine which commitment should be withdrawn when a multi-element clash appears.

### PH-SEM01.5 — Incompatibility profiles do not establish agency or stake

A position may be formally rich while lacking:

- a continuing bearer;
- action control;
- consequence return;
- non-substitutability;
- payability;
- memory and history;
- self-readable direction.

Therefore:

```text
semantic position
!= choice event
!= agency
!= stake
!= subjecthood
```

### PH-SEM01.6 — Non-persistence supplies a false-dilemma diagnostic

A supposed incompatibility is suspect when:

1. it disappears after a legitimate exception is added;
2. it depends on a hidden time horizon;
3. it depends on treating two roles as one;
4. it depends on an unargued bearer boundary;
5. it is maintained only by refusing additional distinctions.

This does not show that every dilemma is false. It establishes a test before an incompatibility is treated as strict.

## 4. ChoiceMap implementation bridge

### 4.1 Suggested option schema

```yaml
option:
  assertions: []
  denials: []
  left_open: []
  positive_consequences: []
  incompatibilities:
    - target:
      type: strict | defeasible | normative | identity | script_generated
      basis:
      affected_bearer:
      horizon:
      repair_context:
  revision_conditions: []
```

### 4.2 Required audits

1. **Bilateral audit** — What does selecting this actually affirm and explicitly deny?
2. **Open-position audit** — Which alternatives remain undecided rather than rejected?
3. **Persistence audit** — Does the clash remain after relevant exception information is added?
4. **Repair audit** — Can modularity, timing, role separation or boundary change permit coexistence?
5. **Positive-consequence audit** — What follows from the option even when no incompatibility is present?
6. **Authority audit** — Who has standing to classify or revise the incompatibility?
7. **Bearer audit** — Who pays if the classification is wrong?

### 4.3 Candidate evaluation measures

For ChoiceMap experiments, possible non-canonical measures include:

- false-dilemma recovery rate;
- rate of `not selected -> denied` collapse;
- strict / defeasible classification accuracy;
- number of valid context-repair paths surfaced;
- percentage of incompatibilities with an explicit basis and reviser;
- percentage of options retaining at least one declared left-open path.

## 5. Occlusion / pathological closure bridge

A pathological closure candidate has the following structure:

```text
defeasible clash
-> reclassified as strict impossibility
-> exception evidence excluded
-> denial standing removed
-> repair proposals treated as incoherent by definition
-> incompatibility rule becomes self-sealing
```

This supports a future bridge note in `Core_Law/SRT_Occlusion_Dynamics.md`:

> Pathological occlusion is not merely a narrow set of accepted claims. It can involve a governance failure in which defeasible incompatibility rules are made persistent, their exception conditions become inadmissible, and affected bearers lose standing to propose repair contexts.

This is a diagnostic analogue only. It does not replace the canonical d / threshold dynamics.

## 6. Objecthood / reselection bridge

For objecthood-as-reselectability, the useful distinction is:

```text
reopening by undoing a commitment
!=
reopening by recomposing the context
```

A resilient object or institution may preserve identity not by returning to its prior state, but by adding distinctions that permit previously clashing commitments to coexist without destroying bearer continuity.

Candidate audit fields:

- which incompatibilities define current identity;
- which are strict and which are historically contingent;
- what repair context preserves the bearer while changing the closure;
- what reopening cost is paid;
- whether the repair expands real options or merely relabels the same lock-in.

## 7. Formal and conceptual guardrails

### Guardrail 1 — semantic incompatibility is not ontological impossibility

A discursive clash may track:

- default expectations;
- norms;
- incomplete information;
- language use;
- institutional rules.

It must not be projected directly onto physical reality.

### Guardrail 2 — defeasible clash is not strict contradiction

The failure of persistence is appropriate for `bird + not flies` when `penguin` repairs the default. It is not a license to claim that `p + not-p` becomes coherent after arbitrary additions.

### Guardrail 3 — `I` is not self-justifying

The set of incoherent positions is an input to the semantics. Practical use requires an account of:

- evidence;
- authority;
- learning;
- disagreement;
- revision;
- affected bearer standing.

### Guardrail 4 — incompatibility entailment is not an ordinary strength order

Because Containment can fail under non-persistence, `Gamma, phi` need not incompatibility-entail `phi`. Do not use profile inclusion as a monotone value, agency or commitment score.

### Guardrail 5 — soundness / completeness is calculus-relative

Formal adequacy relative to Ketonen's calculus does not establish empirical or ontological completeness.

### Guardrail 6 — exclusion cannot define the whole choice

Simonelli explicitly leaves implication and incompatibility as potentially irreducible dimensions. SRT must retain transition, consequence, history, bearer and cost.

## 8. Integration disposition

**Pipeline decision: A.**

Integrated as:

- a philosophy / formal-semantics bridge;
- a ChoiceMap bilateral-position and context-repair layer;
- an occlusion and reselectability integration hook.

Not integrated as:

- a canonical definition of selection;
- a proof that reality is inferential;
- a direct formalization of `L0/L1/L2`;
- a measure of `d-value`, `Psi_f` or `T_dir`;
- a subjecthood or stake test.

## 9. Surviving bridge summary

```text
position = assertions + denials + open remainder
material incompatibility may be defeasible
adding context may repair a clash
negative exclusion != positive consequence
semantic position != bearer-owned choice
```
