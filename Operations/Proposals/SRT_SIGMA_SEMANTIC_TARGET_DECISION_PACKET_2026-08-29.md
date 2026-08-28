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
  - Core/SRT_Core_22_Equations.md
  - _SRT_SYMBOL_TABLE.md
tags: [SigmaSR, AuthorDecision, SemanticTarget, Provenance, Endogeneity, Dependence, Control, Split, Retype]
---

# σ_sr Semantic-Target Author Decision Packet (2026-08-29)

> **Status:** bounded author/theory-design decision packet. No option below is adopted by this file.
>
> **Why a decision is now warranted:** the read-only phase has completed internal defect probes A/B/C plus formal Gate-2 subtraction. Opening another broad audit before choosing the intended semantic target would increase documentation without reducing the main ambiguity.
>
> **Governance:** choosing an option here does not itself edit an owner. Any semantic change to `_SRT_SYMBOL_TABLE.md`, `Core/SRT_Core_22_Equations.md`, `Core_Law/SRT_Individuation.md`, or `Core_Law/SRT_L1_Formalism.md` requires a separate freeze-aware owner-edit PR and consumes B1 if landed.

---

## 0. Evidence that constrains the decision

The following results are now on record.

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

Therefore a repair is valuable to SRT, but the repair technique itself is not a safe novelty claim.

---

## 1. Decision question

What should the **primary semantic target** of the individuation `sigma_sr` architecture be?

The choice must not be made by asking which formula is easiest to preserve. It should be made by asking which relation is actually supposed to do the theoretical work in subject-position individuation.

---

## 2. Option P — PROVENANCE / own-history attribution

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

## 3. Option E — ENDOGENEITY relative to a declared unit

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

## 4. Option D — ONGOING DEPENDENCE / support independence

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

## 5. Option C — CAUSAL CONTROL over next selection / future selection space

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

## 6. Option S — SPLIT architecture

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
- split itself is not externally novel; autonomy/attribution literatures already separate related roles;
- phase-transition claims must specify which readout carries the proposed transition.

### Decision consequence

Would require a later owner-edit design packet before any canonical change.

---

## 7. Option R — RETYPE current σ_sr as a model-local proxy

### Reading

Keep the existing ratio for models where a declared affine parameterization, source-labelled trace/ext channels, and norm convention are part of the model contract.

Treat it as:

```text
model-local historical/writeback balance proxy
```

rather than an unconditional representation-independent natural order parameter.

### Advantages

- lowest-risk repair;
- preserves existing computational work inside declared models;
- honest about E1-E4;
- does not force immediate invention of replacement quantities.

### Burdens

- weakens current universal/natural-boundary language;
- `sigma_sr^sub/self/health` thresholds become model-class conditional until stronger invariance is established;
- may require frozen-anchor wording edits to make scope explicit.

### Decision consequence

Likely C-class/high-risk semantic repair to frozen anchors if adopted and landed; consumes B1.

---

## 8. Evidence-weighted recommendation — NOT an author decision

The audit evidence currently favors a **staged S + R posture**:

### Immediate safety posture — R

Until a stronger construction exists:

> treat the current bare ratio as a model-local historical/writeback proxy under a declared representation, and suspend unconditional claims that its numeric value is a representation-independent control ratio or natural phase coordinate.

This is the minimum claim repair consistent with the executed probes.

### Research architecture — S

Investigate whether historical attribution and current control require separate readouts.

Do **not** canonically create `sigma_prov` / `sigma_ctrl` yet.

First require:

```text
role definitions
+ attribution/influence mathematics
+ cross-scale consistency
+ evidence that the split earns explanatory or D2 surplus beyond autonomy/causal-attribution rivals
```

### Why not choose C immediately

The current formula failed the direct control probe.

### Why not choose P immediately

Provenance is the closest existing wording, but the uniqueness problem remains unresolved and provenance alone does not justify the phase-transition interpretation.

### Why not choose E or D immediately

They are useful diagnostics but would be larger semantic departures and are heavily occupied by neighboring autonomy/scaffolding literatures.

---

## 9. Author decision fields

Choose one primary route, or explicitly choose the staged route.

```text
[ ] P — provenance
[ ] E — endogeneity
[ ] D — ongoing dependence
[ ] C — causal control
[ ] S — split architecture
[ ] R — retype current sigma as model-local proxy
[ ] S+R — staged: retype now, investigate split
[ ] HOLD — no owner edit; keep research unresolved
```

Optional scope decision:

```text
[ ] keep sigma_sr^sub/self/health active as model-conditional thresholds
[ ] suspend natural-boundary interpretation pending repaired/split readout
[ ] separate subject-position and self-consciousness threshold review
```

---

## 10. What follows from each decision

| Decision | Next PR type | B1? | Immediate downstream |
|---|---|---:|---|
| P | attribution-rule feasibility/spec first; owner edit only later | not yet / later yes | R2-DOWN-B |
| E | unit/boundary semantics spec | not yet / later yes | collective/individual consistency |
| D | perturbation/dependence bridge spec | no unless owner changed | developmental/scaffold bridge |
| C | control-functional feasibility spec | no until owner edit | R2-UP-NAT / selector interface |
| S | split architecture design, noncanonical first | no initially | R2-DOWN-B + R2-UP-NAT |
| R | frozen-anchor scope-repair PR | **yes if landed** | Symbol Table / Core22 / Individuation / L1 formalism |
| S+R | R owner-scope repair + separate noncanonical split research | **R consumes 1 B1** | safest staged route |
| HOLD | no sigma owner edit | 0 | proceed only on unrelated workstreams |

---

## 11. Hard guards

Whatever route is selected:

```text
sigma cannot bootstrap bearer admission;
trace membership cannot define bearer by itself;
control share cannot define selector by itself;
subject-position threshold does not prove phenomenality;
Fisher is conditional bridge mathematics, not automatic theta ontology;
Shapley/causal strength are borrowed tools, not SRT novelty;
current neural-unity paper is not reactivated merely because sigma is repaired.
```

---

## 12. Terminal status

```text
READ-ONLY DISCOVERY SUFFICIENT FOR DECISION: YES
MORE BROAD AUDIT BEFORE DECISION: NOT RECOMMENDED
EVIDENCE-WEIGHTED DEFAULT: STAGED S+R
AUTHOR DECISION: PENDING
CANONICAL EDIT AUTHORIZED: NO
CURRENT B1: 0 / 4
```
