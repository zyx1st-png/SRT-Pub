---
id: SRT-OPS-AUDIT-SIGMA-ATTRIBUTION-CONTROL-INVARIANCE-20260829
type: audit_record
status: active
record_stage: active_planning
date: 2026-08-29
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Proposals/SRT_SELECTION_FIRST_ARCHITECTURE_REBASE_MASTER_PLAN_2026-08-28.md
  - Operations/Audits/SRT_SELECTION_FIRST_REBASE_OWNER_MATRIX_2026-08-28.md
  - Core_Law/SRT_Individuation.md
  - Core_Law/SRT_L1_Formalism.md
  - Core_Law/SRT_Collective_Selection.md
  - Core/SRT_Core_22_Equations.md
  - _SRT_SYMBOL_TABLE.md
  - Core/SRT_OPEN_TENSIONS.md
  - Philosophy/SRT_Social_Cognition.md
  - Operations/Audits/SRT_SELECTION_FIRST_DERIVATIONAL_SPINE_TRIAGE_2026-08-28.md
tags: [ArchitectureRebase, R4pre, SigmaSR, Attribution, Control, Invariance, Reparameterization, TPROJ1, Fisher, R2DOWNB, R2UPNAT]
---

# σ_sr Attribution / Control / Invariance Audit — R4-FG (2026-08-29)

> **Scope:** read-only formal-consistency audit. This file does not redefine `σ_sr`, `θ^trace`, `θ^ext`, bearer, selector, Stable ISP, `Ψ_f`, Fisher geometry, or any P0/P1/P2 owner. It creates no new canonical scalar or threshold.
>
> **B1 boundary:** this audit consumes **zero** owner-edit slots. Any later semantic edit to `_SRT_SYMBOL_TABLE.md`, `Core/SRT_Core_22_Equations.md`, `Core_Law/SRT_Individuation.md`, `Core_Law/SRT_L1_Formalism.md`, or another theory owner requires a separate authorized PR. Any edit to a frozen anchor is C-class/high-risk under the rebase programme and consumes B1 if landed.
>
> **Main question:** under the already-declared projection/closure assumptions, is `σ_sr` a representation-stable and semantically typed quantity, and if not, exactly which burden fails: attribution, coordinate invariance, or control interpretation?

---

## 0. Executive problem statement

Current individual owner:

\[
\theta_t=\theta_t^{trace}+\theta_t^{ext},
\qquad
\sigma_{sr}(P,t)=
\frac{\|\theta_t^{trace}\|}
{\|\theta_t^{trace}\|+\|\theta_t^{ext}\|}.
\]

`SRT_Individuation.md` defines `θ^trace` by **P's own prior-output writeback** and `θ^ext` by external conditions. It then interprets `σ_sr` as a one-dimensional tracking candidate for how strongly the next selection is constrained by the pattern's own history relative to non-self external conditions.

The rebase must not assume that these are automatically the same semantic burden.

Four relations must be kept distinct:

```text
PROVENANCE   who/what historically generated a parameter contribution?
ENDOGENEITY  is the contribution currently inside the declared unit/boundary?
DEPENDENCE   does the capability persist when ongoing external support is withdrawn?
CONTROL      how much does the contribution causally influence the current/future output?
```

Candidate anti-collapse rule:

```text
provenance != endogeneity != dependence != control
```

This audit asks which of these `θ^trace / θ^ext` and `σ_sr` are licensed to represent.

---

## 1. Blast radius / freeze map — first deliverable

A nontrivial `RETYPE`, `SPLIT`, or `NO-GO` verdict would not be local to one book-derived intuition.

### Frozen / high-authority surfaces

| Surface | Current load | Risk if σ semantics change |
|---|---|---|
| `_SRT_SYMBOL_TABLE.md` | explicit `σ_sr := ||θ^trace||/(||θ^trace||+||θ^ext||)` entry; `σ_sr^sub`, `σ_sr^self`, `σ_sr^health`, `σ_sr^coll`; Usage Rule 12 namespace | **FROZEN / C-class semantic blast** |
| `Core/SRT_Core_22_Equations.md` | individual T-PROJ-1 and collective T-PROJ-1^coll claim L1 scalar projections under closure assumptions | **FROZEN / C-class semantic blast** |

### Direct theory-bearing dependents

```text
Core_Law/SRT_Individuation.md
  Def-IND-1 / T-IND-1 / T-IND-2 / T-IND-3

Core_Law/SRT_L1_Formalism.md
  sigma ODE
  threshold structure
  chi-kernel family / P-univ invariance work
  T-PROJ-1 projection theorem

Core_Law/SRT_Collective_Selection.md
  sigma_sr^coll
  shared-L2 trace/ext reclassification
  collective four-variable dynamics

Core_Law/SRT_Irreversibility.md
Core_Law/SRT_Occlusion_Dynamics.md
Core_Law/SRT_Collective_Tower_Hardening_Notes.md
Neuroscience/SRT_Clin_02_FEP.md
Core/SRT_OPEN_TENSIONS.md
_SRT_INDEX.md
```

### Consequence for governance

```text
this audit = read-only = B1 unchanged

future scope note inside frozen anchor = owner edit
future sigma semantic retyping = owner edit
future equation replacement = owner edit
future threshold reinterpretation = owner edit
```

No owner mutation is authorized by a positive or negative result in this file.

---

## 2. Owner subtraction before proposing a new problem

### 2.1 `SRT_Individuation` already owns the individual split

The owner does **not** leave `ext -> trace` unspecified in the weak sense of “no formal object exists.” It already fixes:

```text
theta^trace = contribution written by P's own prior outputs
theta^ext   = contribution written by environment / other operators / external conditions
```

Therefore R4-F must not be phrased as:

```text
missing owner for external scaffolding becoming own history
```

That formulation is withdrawn.

### 2.2 `SRT_Collective_Selection §4.4.1` already reclassifies shared L2

At collective scale:

\[
\Theta^{coll,trace}
:=\sum_i w_i\theta_i^{trace}+\Theta_{shared}^{L_2},
\]

\[
\Theta^{coll,ext}
:=\sum_i w_i\theta_i^{ext}-\Theta_{shared}^{L_2}.
\]

The owner explicitly explains the move by saying shared `L_2` is no longer a **new external input relative to the collective**.

This is a boundary/endogeneity-relative reclassification. It is not evidence that every individual external contribution can or must later become individual `θ^trace`.

### 2.3 `SRT_Social_Cognition T-Cog-7` already owns the developmental bridge

T-Cog-7 gives a bridge-only developmental mapping:

```text
co-regulation -> self-regulation
external social scaffolding -> sedimented self-regulatory L2
```

Its own guard forbids using that bridge to redefine canonical `θ`, `d`, `Ψ_f`, or `L2`.

Therefore the Q16 developmental sentence is provenance/input for the audit, not a new SRT theorem.

### 2.4 Residual after subtraction

The live internal question is narrower:

> individual `θ^trace` is defined with a provenance/authorship criterion, while collective trace reclassification uses a declared-unit/boundary criterion and developmental bridges use an assimilation/dependence story. Are these compatible readings of one quantity, scale-specific proxies, or evidence that multiple indices have been compressed into one symbol?

---

## 3. T-PROJ-1 changes the audit target

`Core/SRT_Core_22_Equations.md` and `SRT_L1_Formalism` do not present the four-variable L1 system as free-floating equations. T-PROJ-1 claims it as a projection of the master dynamics under closure assumptions including, at minimum:

```text
C1 slow-fast separation
C2 L2-writeback Markov closure
C3 stable-ISP compactness / bounded projection domain
C4 direction-projection separability
```

Collective projection adds further collective assumptions.

Therefore the primary audit question is **not**:

```text
is the ratio formula aesthetically invariant?
```

It is:

```text
Are the currently declared C1-C4 sufficient to make the sigma projection
well-defined, representation-stable, and semantically interpretable?

If not, which additional assumption / metric / attribution rule is required?
```

### C4 caution

Do **not** silently identify “direction-projection separability” with unique provenance attribution.

C4 may already carry part of the decomposition burden, but the audit must establish whether it entails any of the following:

```text
unique trace/ext decomposition
coordinate-invariant norm
implementation-invariant attribution
output-control interpretation
```

If it does not, a missing closure condition remains possible.

---

## 4. Three defects must be tested separately

### DEFECT A — Attribution / decomposition uniqueness

Question:

> after nonlinear, interacting, recurrent writeback, is there a unique way to assign the current parameter state into “written by P's own history” and “written externally” components?

Potential failure:

```text
same current theta
+ same realized operator
+ interacting causal history
-> multiple admissible allocations between theta^trace and theta^ext
```

A metric alone cannot solve this problem.

Possible repair families to investigate later:

```text
explicit structural causal attribution
Shapley-style contribution allocation
path-integrated attribution
owner-specific intervention decomposition
```

No repair family is adopted here.

### DEFECT B — Coordinate / reparameterization dependence

Minimal probe:

Let two parameterizations implement the same operator family:

\[
\theta' = A\theta
\]

with invertible admissible `A`, while the realized input-output/statistical model is unchanged.

Ask whether:

\[
\sigma_{sr}'
=
\frac{\|A\theta^{trace}\|}
{\|A\theta^{trace}\|+\|A\theta^{ext}\|}
\]

must equal `σ_sr`.

Under a generic Euclidean norm the answer is not guaranteed.

#### Candidate repair: invariant metric

A local metric can replace bare coordinate norm only if its domain is licensed.

Fisher-Rao is a **named candidate** because the repository already uses Fisher geometry conditionally and because information geometry supplies parameterization-invariant distances on statistical manifolds.

But:

```text
Fisher candidate != automatic repair
```

Required admission before use:

```text
theta parameterizes a declared statistical model
+ regularity conditions
+ metric projection is valid for the intended operator family
+ no reversal of the repository's existing rule that Fisher geometry is a conditional bridge/projection, not primitive ontology
```

Čencov-style uniqueness results apply inside a statistical-model / Markov-morphism setting; they do not license importing Fisher geometry into an arbitrary `G_theta` solely because coordinates exist.

### DEFECT C — Parameter magnitude is not causal control

Even if attribution is unique and the metric is invariant:

```text
large component magnitude
!=
large influence on current operator output
```

Minimal counterpressure:

```text
large self-written component in a locally insensitive direction
vs
small externally sourced component at a high-sensitivity decision direction
```

The relevant comparison may require a sensitivity / intervention / causal-strength object rather than a bare parameter magnitude.

Candidate families:

```text
Jacobian / local sensitivity weighting
Fisher sensitivity where a statistical model is admissible
interventional ablation
causal-strength / information-flow measures
implementation-invariant attribution
```

Again, none is adopted here.

---

## 5. Execution order

The defects are not one test.

Preferred sequence:

```text
B0 blast-radius / freeze check             DONE IN THIS AUDIT
B1 T-PROJ-1 C1-C4 scope check              FIRST FORMAL GATE
B2 coordinate-invariance probe             DEFECT B
B3 attribution-index freeze                provenance/endogeneity/dependence
B4 decomposition-uniqueness probe          DEFECT A
B5 control-interpretation probe             DEFECT C
B6 cross-scale / collective consistency
B7 external Gate-2 subtraction
```

Why coordinate invariance first:

> if the scalar changes under a pure change of representation, there is no reason yet to spend effort interpreting its provenance/control semantics.

Why attribution comes before control:

> a control-weighted quantity is uninterpretable if membership in the trace component is itself underdetermined.

---

## 6. Index freeze — provenance, endogeneity, dependence, control

Before DEFECT A is evaluated, use at least the following typed questions.

| Index | Question | Does current owner clearly define it? |
|---|---|---|
| provenance | who/what historically generated the contribution? | **partly yes** — individual `θ^trace` uses own-prior-output writeback |
| endogeneity | is the contribution currently inside the declared unit? | **scale-dependent** — collective owner explicitly uses boundary-relative reclassification |
| dependence | if ongoing external support is withdrawn, does the capability persist? | **bridge-level only** in developmental/scaffolding work |
| control | how strongly does it alter current/future operator output? | **not established by bare norm alone** |

### Minimal divergence cases

| Case | Provenance | Ongoing dependence | Current control | Pressure |
|---|---|---:|---:|---|
| internalized developmental scaffold | external-origin | low after successful internalization | potentially high | provenance and dependence diverge |
| still co-regulated child | external-origin | high | potentially high | external support remains load-bearing |
| dormant self-written habit | self-origin | low | low | trace membership does not imply control |
| active self-written policy | self-origin | low | high | intended strong-self-history case |
| externally trained fixed parameter | external-origin | low ongoing dependence | high | external provenance can dominate control |
| collective shared L2 | mixed/member-generated | boundary-relative | variable | classification changes with declared unit |

This table is a stress test, not a bearer/selector definition.

---

## 7. R4-F and R4-G are one audit with two non-identical burdens

Withdraw the earlier split as two separate audits.

```text
R4-F = what licenses membership in theta^trace?
R4-G = once admitted, what does the size of theta^trace mean for current control?
```

They belong in one audit because both constrain the interpretation of `σ_sr`, but they must not be collapsed:

```text
membership / attribution
!=
causal efficacy / control
```

### Bearer-selector guard

Do not write:

```text
Bearer = sigma_provenance > 0
Selector = sigma_control high
```

That would silently redefine both roles and reintroduce sigma bootstrap.

Allowed future question only:

> can a provenance-like and a control-like readout provide a useful formal interface for the already-owned `Bearer != Selector` distinction after bearer admission and selector admission are independently specified?

---

## 8. Pre-frozen outcomes

### OUTCOME S — SURVIVES

Current `θ^trace / θ^ext`, current closure assumptions, and current norm are already sufficient to establish:

```text
well-defined decomposition
+ acceptable representation invariance
+ licensed interpretation of sigma for its claimed role
```

No owner edit required beyond possible documentation.

### OUTCOME SR — SURVIVES WITH REPAIR

The semantic target survives, but one explicit additional closure/metric/attribution condition is required.

Examples:

```text
C5-style attribution well-formedness condition
or
admissible invariant metric under declared statistical projection
```

Any landed repair to a frozen/theory owner is a separate B1-counted edit.

### OUTCOME SPLIT — TWO READOUTS ARE REQUIRED

A provenance/endogeneity quantity and a control/influence quantity are both coherent but cannot be represented by one scalar without information loss.

Possible consequence:

```text
sigma_prov / sigma_hist      provenance-like historical attribution readout
sigma_ctrl                   control/influence readout
```

These names are placeholders only. This audit does not create them.

`SPLIT` is a positive structural result, not an automatic demotion.

### OUTCOME R — RETYPE

Current `σ_sr` remains useful only for a narrower role, for example source-weight / writeback-history proxy, while stronger “self-history control ratio” language is withdrawn or restricted.

### OUTCOME N — NO-GO / DEMOTE

No non-arbitrary decomposition/metric can make the current scalar stable enough for the intended order-parameter role under the declared model class.

Then threshold/natural-boundary claims depending on the scalar require re-evaluation.

---

## 9. Direct consequence for R2-UP-NAT

R2-UP-NAT asks whether `σ_sr^sub` is an independently evidenced natural phase boundary or a conventional/model-relative admission line.

This audit is upstream.

```text
if sigma is not representation-stable
-> natural-boundary evidence is not yet interpretable

if sigma survives only under a declared metric/model class
-> any natural-boundary claim is scoped to that class

if sigma splits
-> which readout carries the proposed transition must be re-frozen
```

Do not use a threshold to rescue a poorly typed order parameter.

---

## 10. Direct consequence for T-CHI-1 / family-level invariance work

Existing L1 hardening already asks whether the `chi` transition kernel preserves a structural transition across an admissible function family.

That is a useful methodological precedent:

```text
freeze a family
state invariants
state non-invariants
prove what survives substitution
```

But it is downstream of `σ_sr` itself.

Therefore:

```text
chi-family invariance
presupposes that the coordinate/order parameter it receives is sufficiently well-defined
```

If DEFECT B or A fails, T-CHI-1 is not thereby falsified as a conditional mathematical statement; its interpretation becomes conditional on a repaired/declared sigma representation.

---

## 11. External Gate-2 preregistration — do not execute before internal gates

Two external literatures must be separated.

### 11.1 Phenomenon / incorporation neighbors

```text
Vygotsky / internalization
extended mind / scaffolded cognition
Sterelny / scaffolded mind
Malafouris / material engagement
niche construction
participatory sense-making
sensorimotor incorporation / endogenization
```

These pressure the natural-language claim “external support becomes own capacity.” They are **not** the first literature for the metric problem.

### 11.2 Formal role-matched neighbors

```text
information geometry / Fisher-Rao / Cencov-style invariance
axiomatic attribution / Shapley-style allocation / Integrated Gradients
causal influence / causal strength / intervention-based control
information-theoretic autonomy / system-environment decomposition
```

Formal Gate 2 should ask:

```text
Has the invariance / attribution / causal-control problem already been solved
under assumptions role-matched to SRT's operator setting?
```

Do not claim novelty merely because no rival uses the symbol `sigma_sr`.

### Important Fisher guard

The repository already treats Fisher geometry as borrowed conditional structure in `Core_22` / `Psi_f` bridges.

Therefore:

```text
Fisher may repair coordinate invariance under a declared statistical projection
!=
Fisher is automatically the canonical metric of theta-space
```

Any stronger promotion requires its own claim-level and freeze review.

---

## 12. Compact Q11-Q17 source-intuition ledger

This section supplies the R4-pre bookkeeping without creating a second long chapter audit.

| Source | First-pass result after owner subtraction | Route |
|---|---|---|
| Q11 pre-cropping / menu generation | substantially overlapped by `SRT_Choice_Generation_Conditions`; no new primitive-menu theory | owner-subtracted / candidate-generation context |
| Q12 stakes / consequence return | later bearer/concern owners are stricter; do not recover book definition as canonical | R2C context only |
| Q13 caring | strong autonomy/enactivism overlap and existing concern decomposition | no standalone novelty claim |
| Q14 value | routed to value/d-value owners; not reopened here | deliberately out of scope |
| Q15 concern width | routed to d/concern-domain owners; not reopened here | deliberately out of scope |
| Q15b agency | useful intuition: borne history can acquire control authority; becomes DEFECT C question, not new agency definition | R4-G input |
| Q16 subject sedimentation | useful intuition: co-regulation can become self-regulation; already has T-Cog-7 bridge; becomes index-divergence stress case | R4-F input after subtraction |
| Q17 consciousness | strong “bearing -> qualia/internal aspect” language is blocked by current HP-B / phenomenality-open discipline | historical source only / do not recover as answer |

### R4-pre disposition

```text
Q11-Q17 MINED
NO NEW PRIMITIVE
NO ext->trace OWNER-GAP CLAIM
R4-F + R4-G MERGED INTO SIGMA SEMANTICS AUDIT
Q17 PHENOMENAL STRONG CLAIM NOT RECOVERED
```

---

## 13. Relationship to R2-CORE / OPEN_TENSIONS §13

This audit is middle-level.

Even a successful repair or split does not establish Selection-primitive fruitfulness.

Keep four levels separate:

```text
primitive co-admission
!= constitutive admission criterion
!= generative derivation
!= P2/P3 bridge/model projection
```

The R2-CORE derivational-spine triage is the execution grammar for the `OPEN_TENSIONS §13` fruitfulness burden.

A result here may provide a cleaner middle-level target for that later audit, but it cannot retroactively assign primitive credit.

---

## 14. Required next action after this audit

Do **not** edit a frozen anchor immediately.

First executable probe:

```text
1. freeze a tiny operator/statistical-model family with two equivalent parameterizations;
2. define trace/ext histories before coordinate transformation;
3. test Euclidean-norm sigma under admissible reparameterizations;
4. if it fails, test whether a declared Fisher-Rao metric projection restores invariance;
5. record whether the statistical-manifold assumptions required by Fisher are genuinely available;
6. only then proceed to attribution uniqueness and causal-control weighting.
```

Required reporting:

```text
functional model invariant?
sigma invariant?
metric assumptions declared?
trace/ext membership invariant?
control ranking invariant?
```

A negative result is terminal evidence for the current formulation, not a reason to change the test post hoc.

---

## 15. Terminal audit status

```text
R4-F ORIGINAL OWNER-GAP FORMULATION: WITHDRAWN
R4-FG REFRAMED AS: SIGMA ATTRIBUTION / CONTROL / INVARIANCE AUDIT
FROZEN-ANCHOR BLAST RADIUS: HIGH
CURRENT B1 COST: 0 (READ-ONLY)
C1-C4 SUFFICIENCY: OPEN
DEFECT A ATTRIBUTION UNIQUENESS: OPEN
DEFECT B REPARAMETERIZATION INVARIANCE: OPEN / FIRST EXECUTABLE TEST
DEFECT C MAGNITUDE-TO-CONTROL INTERPRETATION: OPEN
FISHER: NAMED CONDITIONAL CANDIDATE, NOT ADOPTED
ALLOWED OUTCOMES: SURVIVES / SURVIVES-WITH-REPAIR / SPLIT / RETYPE / NO-GO
NEXT: MINIMAL REPARAMETERIZATION FEASIBILITY PROBE
```
