---
id: SRT-OPS-PROPOSAL-SIGMA-SEMANTIC-TARGET-DECISION-20260829
type: proposal
status: active
record_stage: author_decision_pending
date: 2026-08-29
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: mixed_governance_P2_P3_candidate
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Audits/SRT_SIGMA_ATTRIBUTION_CONTROL_INVARIANCE_AUDIT_2026-08-29.md
  - Operations/Audits/SRT_SIGMA_REPARAMETERIZATION_FEASIBILITY_PROBE_2026-08-29.md
  - Operations/Audits/SRT_SIGMA_TPROJ1_C1_C4_SUFFICIENCY_CHECK_2026-08-29.md
  - Operations/Audits/SRT_SIGMA_TRACE_ATTRIBUTION_UNIQUENESS_PROBE_2026-08-29.md
  - Operations/Audits/SRT_SIGMA_CONTROL_DISSOCIATION_PROBE_2026-08-29.md
  - Operations/Audits/SRT_SIGMA_FORMAL_GATE2_SUBTRACTION_2026-08-29.md
  - Core_Law/SRT_Individuation.md
  - Core_Law/SRT_L1_Formalism.md
  - Core_Law/SRT_Collective_Selection.md
  - Core/SRT_Core_22_Equations.md
  - _SRT_SYMBOL_TABLE.md
tags: [SigmaSR, AuthorDecision, SemanticTarget, Provenance, Endogeneity, Dependence, Control, Split, Retype, GateD, ConventionalOrderParameter]
---

# σ_sr Semantic-Target Author Decision Packet (2026-08-29)

> **Status:** bounded author/theory-design decision packet. No option below is adopted by this file.
>
> **Why a decision is now warranted:** the read-only phase has completed internal defect probes A/B/C plus formal Gate-2 subtraction. Opening another broad audit before choosing the intended semantic target would increase documentation without reducing the main ambiguity.
>
> **Governance:** choosing an option here does not itself edit an owner. Any semantic change to a theory owner or frozen anchor requires a separate freeze-aware owner-edit PR and consumes B1 if landed.

---

## 0. Owner fact that changes the interpretation of this repair

`Core_Law/SRT_Individuation.md §八` already states:

```text
T-IND-1:
P1-T06 四条件的同时成立需要一个统一阶参候选；非唯一推出

σ 作为阶参（Def-IND-1）:
P2 canonical interpretation
阶参选择是规约性的；可替换为等价形式
```

Therefore the current reparameterization result does **not** overturn an owner claim that `σ_sr` is the unique natural order parameter. The owner already denies that stronger reading.

The live drift is instead between that owner-level conventionality and stronger frozen/downstream surfaces that present `σ_sr` as an unqualified order parameter / master-equation scalar projection without carrying the same representation-relative qualification.

Hence Option R should be read as:

```text
frozen/downstream surface truth-up
-> to an already-existing owner conventionality statement
```

not as:

```text
post-hoc demotion of the Individuation owner
```

This distinction is central to any later B1 authorization rationale.

---

## 1. Evidence that constrains the decision

### E1 — bare norm is not representation invariant

Equivalent operator behavior can be preserved under an invertible parameter-coordinate transformation while:

\[
\sigma_{sr}: 0.5 \rightarrow 10/11\approx0.9091.
\]

C1-C4 do not currently specify a gauge/metric that excludes this counterexample.

### E2 — trace attribution is not uniquely closed

Current owners provide writeback mechanisms and a `P_{L2->theta}` projection symbol, but no unique allocation rule for mixed self/external causal history and no transformation law for the decomposition.

### E3 — current owners use non-identical trace semantics

```text
Individuation:
trace = P's own prior-output writeback

T-PROJ-1:
trace = L2-writeback contribution

Collective Selection:
shared L2 is reclassified as collective trace by declared-boundary endogeneity
```

No general theorem currently equates these roles.

### E4 — bare parameter magnitude is not current control

A fixed model can have:

```text
bare trace share ~0.9091
Jacobian/control-like trace share ~0.00990
external ablation effect = 100 x trace ablation effect
```

So provenance/writeback magnitude and causal control cannot be identified without extra assumptions.

### E5 — generic repair mathematics is prior art

Information geometry, axiomatic attribution, causal-strength measures, and information-theoretic autonomy already own the generic mathematical problems.

In particular, the autonomy literature already occupies the phenomenon-level question of self-history/self-determination versus environmental history/external control and already diagnoses attribution ambiguity.

Therefore a repair is valuable to SRT, but the repair technique or the generic provenance/control distinction is not a safe novelty claim.

### E6 — the collective branch carries the same burden and the strongest semantic divergence

`Core_Law/SRT_Collective_Selection` defines:

\[
\sigma_{sr}^{coll}
=
\frac{\|\Theta^{coll,trace}\|}
{\|\Theta^{coll,trace}\|+\|\Theta^{coll,ext}\|}
\]

and explicitly reindexes shared `L_2` as collective-internal:

```text
Theta_coll,trace
= weighted individual trace + shared L2

Theta_coll,ext
= weighted individual ext - shared L2
```

because shared `L_2` is no longer new input relative to the declared collective boundary.

This is exactly the scale-relative endogeneity reading that differs most from individual provenance. Any R repair that omits `σ_sr^coll` / `T-PROJ-1^coll` would recreate the inconsistency exposed by DEFECT A.

---

## 2. Decision question

What should the **primary semantic target** of the individuation `σ_sr` architecture be?

The choice must not be made by asking which formula is easiest to preserve. It should be made by asking which relation is actually supposed to do the theoretical work in subject-position individuation.

---

## 3. Option P — PROVENANCE / own-history attribution

### Reading

`σ_sr` tracks the relative amount/weight of current operator structure attributable to the unit's own prior-output history versus external provenance.

### Advantages

- closest to the literal wording of `SRT_Individuation`;
- preserves the historical-sedimentation intuition;
- naturally distinguishes self-authored history from imposed state under an explicit attribution convention.

### Burdens

- DEFECT A requires an attribution rule for mixed interactions;
- DEFECT B requires a representation-stable measurement convention;
- high provenance does not imply high current control;
- provenance alone does not prove bearer, selector, subject or natural phase boundary.

### External pressure

Axiomatic/causal attribution is mature; generic “who contributed what” is not novel.

### Decision consequence

If chosen, strong `self-history control ratio` language should be removed or separately qualified.

---

## 4. Option E — ENDOGENEITY relative to a declared unit

### Reading

`σ_sr` tracks how much of the currently operative structure is endogenous to the declared unit/boundary rather than currently supplied from outside.

### Advantages

- aligns more closely with `Collective_Selection` shared-L2 reclassification;
- handles incorporation/internalization better than strict historical authorship;
- naturally scale-relative.

### Burdens

- requires independent unit/boundary declaration; cannot be used to prove the unit whose boundary it presupposes;
- scale changes can change the classification;
- endogeneity does not imply historical self-authorship or control;
- risks collapsing toward autonomy/Markov-blanket literature.

### Decision consequence

Would be a substantive retyping away from the current individual-owner provenance wording.

---

## 5. Option D — ONGOING DEPENDENCE / support independence

### Reading

`σ_sr` tracks whether a capability persists when ongoing external support/scaffolding is withdrawn.

### Advantages

- captures developmental internalization and scaffold assimilation intuitively;
- gives an operational perturbation test.

### Burdens

- a capability can be historically external-origin yet now independent;
- a highly endogenous system can remain environmentally dependent for energy/information;
- dependence is perturbation- and timescale-relative;
- heavy prior-art pressure from autonomy/scaffolding/incorporation theories.

### Decision consequence

Would require a major semantic shift and should not preserve current formula by name without a separate derivation.

---

## 6. Option C — CAUSAL CONTROL over next selection / future selection space

### Reading

`σ_sr` tracks how much current/future operator behavior is causally controlled by own-history-derived structure relative to external influence.

### Advantages

- closest to the motivating sentence “next selection is constrained by its own history”;
- potentially relevant to `Bearer != Selector` interfaces;
- admits intervention/sensitivity tests.

### Burdens

- the current bare-norm formula fails the minimal control-dissociation probe;
- requires an explicit influence functional and target variable;
- causal-strength/autonomy literatures are mature;
- control does not itself prove provenance, bearing, subjecthood or phenomenality.

### Decision consequence

Choosing C means the **current** `sigma_sr` formula cannot simply be retained as the final control measure without a nontrivial repair theorem.

---

## 7. Option S — SPLIT architecture

### Gate type: **Gate-D, not Gate-N**

The live SRT question is **not**:

```text
SRT discovered that provenance != control
```

That phenomenon/mathematical separation is already occupied by autonomy, attribution and causal-influence literatures.

The live question is derivational:

> **Which relation—provenance, endogeneity, ongoing dependence, causal control, or some typed combination—is actually required by the already-landed SRT individuation/subject-position architecture, and can that requirement be derived without circularly using `sigma` to prove the domain in which `sigma` is defined?**

That is a **Gate-D derivability / architecture question**.

### Reading

No single scalar is required to carry provenance, endogeneity, dependence and control.

At minimum distinguish:

```text
historical/source attribution role
!=
current control/influence role
```

Potentially keep endogeneity/dependence as separate diagnostics rather than additional canonical scalars.

### Advantages

- best fit to E1-E4;
- avoids forcing one mathematical object to answer four questions;
- provides a cleaner formal location for the already-owned `Bearer != Selector` distinction without defining either role by a scalar;
- allows different external mathematics to be used for different jobs.

### Burdens

- increases formal complexity;
- requires deciding which, if any, object retains the symbol `sigma_sr`;
- split itself is not externally novel;
- the derivational requirement still has to be earned from SRT owners;
- phase-transition claims must specify which readout carries the proposed transition.

### Decision consequence

Would require a later owner-edit design packet before any canonical change.

Do **not** create canonical `sigma_prov` / `sigma_ctrl` variables merely to instantiate the split.

---

## 8. Option R — TRUTH-UP / RETYPE current σ_sr as a model-local proxy

### Reading

Keep the existing ratio for models where a declared affine parameterization, source-labelled trace/ext channels, and norm convention are part of the model contract.

Treat it as:

```text
model-local historical/writeback balance proxy
```

rather than an unconditional representation-independent natural order parameter.

### Why this is not an owner demotion

`SRT_Individuation §八` already says the order-parameter choice is conventional and replaceable by an equivalent form.

Therefore R is best described as:

> **truth-up frozen/downstream surfaces to the owner's existing conventionality statement.**

### Advantages

- lowest-risk repair;
- preserves existing computational work inside declared models;
- aligns frozen/downstream wording with the actual owner burden table;
- does not force immediate invention of replacement quantities;
- leaves T-IND-1 largely intact because T-IND-1 requires a unified order-parameter candidate, not unique derivation of this exact scalar.

### Burdens

- unconditional representation-independent/natural-coordinate language must be removed or scoped;
- `sigma_sr^sub/self/health` numerical thresholds remain model-class conditional until stronger invariance is established;
- T-IND-1 / threshold prose that says “structural threshold” may need a narrow representation-relative scope note without changing the underlying four-condition transition claim.

### Decision consequence

A later B1 repair should be justified as cross-owner consistency repair, not theory retreat.

---

## 9. R2-UP-NAT disposition after owner check

The former question:

```text
R2-UP-NAT:
sigma_sr^sub = natural phase boundary or conventional admission line?
```

is too coarse.

The current owner already answers the **σ-specific** version:

```text
current sigma as unique/natural order parameter?
-> NO CLAIM; order-parameter choice is conventional and replaceable
```

Therefore mark:

```text
R2-UP-NAT-sigma = CLOSED-BY-OWNER + #863
```

Do **not** close the broader question:

```text
Does P1-T06 individuation exhibit a reproducible natural transition/boundary
in some independently justified dimension or invariant family?
```

`SRT_Individuation` itself retains that as an open burden via adjacent positive/negative boundary cases.

So the closure is:

```text
naturalness of this bare sigma coordinate = closed / not claimed
naturalness of an underlying individuation transition = still open
```

---

## 10. Evidence-weighted recommendation — NOT an author decision

The evidence currently favors a **staged S + R posture**.

### Immediate safety posture — R

Until a stronger construction exists:

> truth-up frozen/downstream surfaces so the current bare ratio is explicitly read as a model-local historical/writeback proxy under a declared representation, consistent with `SRT_Individuation`'s existing statement that order-parameter choice is conventional and replaceable.

### Research architecture — S / Gate-D

Investigate which relation the subject-position transition actually requires.

Do **not** frame this as novelty for discovering `provenance != control`.

Do **not** canonically create `sigma_prov` / `sigma_ctrl` yet.

First require:

```text
owner derivability
+ role definitions
+ attribution/influence mathematics where needed
+ cross-scale consistency
+ bounded-rival subtraction
+ explanatory/D2 surplus only after derivability survives
```

---

## 11. Future single-B1 repair scope if R is author-authorized

If the author chooses R or S+R, execute **one repair PR = one B1 slot**, even though several files must move together.

### Semantic/owner surfaces that must be synchronized in the same repair

```text
_SRT_SYMBOL_TABLE.md                         FROZEN anchor
Core/SRT_Core_22_Equations.md               FROZEN anchor
Core_Law/SRT_Individuation.md               owner truth source / minimal scope precision only if needed
Core_Law/SRT_L1_Formalism.md                single-P sigma ODE / T-PROJ-1
Core_Law/SRT_Collective_Selection.md         sigma_coll / shared-L2 reindex / collective ODE / T-PROJ-1^coll
Core/SRT_Core_22_Equations.md §0-C           collective projection anchor in same frozen file
```

### Pointer/stale-surface synchronization to inspect in that same PR

```text
Core_Law/SRT_Irreversibility.md
Core_Law/SRT_Occlusion_Dynamics.md
Core_Law/SRT_Collective_Tower_Hardening_Notes.md
Neuroscience/SRT_Clin_02_FEP.md
Core/SRT_OPEN_TENSIONS.md
_SRT_INDEX.md
```

These pointer surfaces do not each consume B1 separately. B1 counts the landed theory-owner repair PR / owner-edit budget event, not the number of touched files.

### Mandatory collective guard

Do not repair individual `sigma_sr` while leaving `sigma_sr^coll` untouched.

The collective branch is where source provenance and boundary-relative endogeneity diverge most strongly; omitting it would reproduce the exact inconsistency exposed by DEFECT A.

---

## 12. Fisher follow-up status

`Eq-Bridge-IG-01` already provides one repository-local precedent for using Fisher geometry as a conditional local orthogonal decomposition, including as support for C4/C4^coll.

This makes the following a legitimate later **bounded feasibility probe**:

> can the same declared statistical-manifold structure support an invariant trace/ext tangent or path decomposition?

But this is **not required to justify R** and should not delay the truth-up repair if R is authorized.

Possible outcomes:

```text
YES -> candidate B repair inside a restricted statistical-model class
NO  -> explicit boundary of the existing IG bridge
```

Either way, Fisher remains conditional bridge mathematics and does not solve provenance attribution or causal control automatically.

---

## 13. Author decision fields

Choose one primary route, or explicitly choose the staged route.

```text
[ ] P — provenance
[ ] E — endogeneity
[ ] D — ongoing dependence
[ ] C — causal control
[ ] S — split architecture / Gate-D
[ ] R — truth-up current sigma as model-local proxy
[ ] S+R — staged: truth-up now, investigate Gate-D split
[ ] HOLD — no owner edit; keep research unresolved
```

Optional scope decision:

```text
[ ] keep sigma_sr^sub/self/health active as model-conditional thresholds
[ ] close sigma-specific natural-coordinate interpretation
[ ] keep broader natural-transition question open
[ ] separate subject-position and self-consciousness threshold review
```

---

## 14. What follows from each decision

| Decision | Next PR type | B1? | Immediate downstream |
|---|---|---:|---|
| P | attribution-rule feasibility/spec first; owner edit only later | not yet / later yes | R2-DOWN-B |
| E | unit/boundary semantics spec | not yet / later yes | collective/individual consistency |
| D | perturbation/dependence bridge spec | no unless owner changed | developmental/scaffold bridge |
| C | control-functional feasibility spec | no until owner edit | selector interface |
| S | Gate-D split architecture design, noncanonical first | no initially | derivational spine + R2-DOWN-B |
| R | single cross-owner truth-up repair PR | **1 B1 if landed** | frozen surfaces + single/collective sigma sync |
| S+R | R truth-up repair + separate noncanonical Gate-D research | **R consumes 1 B1** | safest staged route |
| HOLD | no sigma owner edit | 0 | proceed only on unrelated workstreams |

---

## 15. Hard guards

Whatever route is selected:

```text
sigma cannot bootstrap bearer admission;
trace membership cannot define bearer by itself;
control share cannot define selector by itself;
subject-position threshold does not prove phenomenality;
Fisher is conditional bridge mathematics, not automatic theta ontology;
Shapley/causal strength are borrowed tools, not SRT novelty;
provenance != control is not an SRT novelty claim;
current neural-unity paper is not reactivated merely because sigma is repaired.
```

---

## 16. Terminal status

```text
READ-ONLY DISCOVERY SUFFICIENT FOR DECISION: YES
MORE BROAD AUDIT BEFORE DECISION: NOT RECOMMENDED
EVIDENCE-WEIGHTED DEFAULT: STAGED S+R
S GATE TYPE: GATE-D
R RATIONALE: OWNER-CONSISTENCY TRUTH-UP
R2-UP-NAT-SIGMA: CLOSED
BROADER NATURAL-TRANSITION QUESTION: OPEN
AUTHOR DECISION: PENDING
CANONICAL EDIT AUTHORIZED: NO
CURRENT B1: 0 / 4
```
