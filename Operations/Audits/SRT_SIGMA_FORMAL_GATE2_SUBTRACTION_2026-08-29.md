---
id: SRT-OPS-AUDIT-SIGMA-FORMAL-GATE2-SUBTRACTION-20260829
type: audit_record
status: active
record_stage: external_subtraction_executed
date: 2026-08-29
layer: meta
epistemic_layer: os
claim_mode: evidence
claim_level: P3/P4_governance
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Audits/SRT_SIGMA_ATTRIBUTION_CONTROL_INVARIANCE_AUDIT_2026-08-29.md
  - Operations/Audits/SRT_SIGMA_REPARAMETERIZATION_FEASIBILITY_PROBE_2026-08-29.md
  - Operations/Audits/SRT_SIGMA_TRACE_ATTRIBUTION_UNIQUENESS_PROBE_2026-08-29.md
  - Operations/Audits/SRT_SIGMA_CONTROL_DISSOCIATION_PROBE_2026-08-29.md
  - Bridge/SRT_Adjacent_Theory_Interface_Index.md
tags: [SigmaSR, Gate2, InformationGeometry, FisherRao, Cencov, Attribution, Shapley, CausalStrength, Autonomy, Subtraction]
---

# σ_sr Formal Gate-2 Subtraction (2026-08-29)

> **Scope:** source-backed external subtraction after the internal A/B/C probes. This file does not promote any external formalism into SRT and does not claim novelty from notation differences.
>
> **Source status:** primary / proceedings / journal sources were checked for the roles below. This is an audit record, not yet a material-registry import or a canonical comparison owner.

---

## 0. Executive verdict

The external literature already owns all three generic repair problems at a mature level:

```text
DEFECT B coordinate / representation invariance
-> mature information-geometry territory

DEFECT A contribution / interaction allocation
-> mature axiomatic attribution / Shapley territory

DEFECT C causal influence / control strength
-> mature causal-inference / interventional-information territory
```

In addition, information-theoretic autonomy already asks a highly role-matched question:

```text
how much is the system's next state determined by its own history
vs environmental history / external control?
```

Therefore SRT must not claim novelty for:

```text
using an invariant metric;
attributing mixed contributions;
separating self-determination from external influence;
measuring causal control;
internalization / endogenization;
or splitting provenance from influence in the abstract.
```

The surviving value of the sigma audit is currently **internal architectural hardening**, not a publication-ready external novelty claim.

---

## 1. Gate B subtraction — Fisher-Rao / information geometry

### Source anchors

- Čencov/Chentsov characterization tradition: Fisher-Rao is characterized, up to scale under the appropriate conditions, by invariance/monotonicity requirements on statistical manifolds under Markov embeddings/maps.
- Modern Information Geometry literature continues to state Fisher metric invariance/covariance under reparameterization of statistical models.

### What this subtracts

The generic idea:

```text
bare Euclidean parameter norm is coordinate dependent
-> replace it with an invariant statistical-manifold metric
```

is **not SRT novelty**.

The reparameterization defect found internally is real, but its generic mathematical repair language is established prior art.

### What remains SRT-specific only as an admission problem

SRT still has to answer:

```text
Does G_theta define / induce a regular statistical model in the relevant domain?
Are trace/ext objects tangent/update directions or final-state components?
Which statistical distribution is the metric about?
Does the existing Core22 Fisher bridge license this particular projection?
```

Those are SRT integration burdens, not new information geometry.

### Verdict

`B-NOVELTY = N0 for generic invariant-metric repair`.

---

## 2. Gate A subtraction — axiomatic attribution and interactions

### Source anchors

Sundararajan, Taly & Yan (ICML 2017), **Axiomatic Attribution for Deep Networks**:

```text
Sensitivity
Implementation Invariance
-> Integrated Gradients candidate satisfying the axioms
```

This is directly relevant to the present requirement that an attribution should not change merely because two implementations realize the same function.

Shapley / Shapley-Taylor work goes further by explicitly allocating feature and interaction contributions under axioms such as:

```text
linearity
dummy
symmetry
efficiency
interaction-distribution
```

Flow-based / recursive Shapley work in graphical models additionally targets propagation of source effects and includes implementation invariance, sensitivity and affine scale invariance among desirable properties.

### What this subtracts

The generic move:

```text
nonlinear interaction term has no unique owner
-> choose an explicit axiomatic attribution rule
```

is not novel.

Neither is the observation that interaction effects require a principled allocation rule rather than naïve additive ownership.

### What remains SRT-specific as an architecture choice

SRT has not yet selected what the attribution target is:

```text
historical source contribution?
L2 writeback contribution?
current endogenous organization?
current causal influence?
```

Different attribution rules answer different questions.

The residual is therefore **typing before attribution**, not invention of attribution theory.

### Verdict

`A-NOVELTY = N0 for generic axiomatic contribution allocation`.

---

## 3. Gate C subtraction — causal influence / causal contribution

### Source anchors

Causal-inference literature already contains explicit measures of causal strength based on intervention.

Relevant role families include:

```text
Ay & Polani information flow
Janzing et al. causal strength / arrow-removal intervention
Jung et al. do-Shapley causal contribution
Janzing et al. intrinsic causal contributions via structure-preserving interventions
```

These literatures explicitly distinguish ordinary association from intervention-sensitive causal contribution.

Recent intrinsic-contribution work separates information added by a node from information inherited from ancestors, then uses structure-preserving interventions and Shapley symmetrization to quantify contribution.

### What this subtracts

The generic claim:

```text
parameter magnitude != causal control
and
control should be quantified by intervention-sensitive influence
```

is prior art.

The internal DEFECT-C toy example is still diagnostically useful for SRT, but the repair concept is not novel.

### What remains SRT-specific as a target choice

SRT may need to specify which effect object matters:

```text
next realized output;
future candidate-space deformation;
future selectability;
L2 writeback;
bearer consequence closure.
```

Choosing one is an SRT model-design problem. Causal-strength mathematics itself is not.

### Verdict

`C-NOVELTY = N0 for generic causal-control measurement`.

---

## 4. Strongest role-matched neighbor — information-theoretic autonomy

### Source anchor

Bertschinger, Olbrich, Ay & Jost, **Autonomy: An information theoretic perspective**, Biosystems 91(2), 2008.

The paper's stated objective is to quantify autonomy as self-determination relative to external control.

A first measure conditions consecutive system-state dependence on environmental history; the paper then notes that the appropriate autonomy measure changes when the system itself controls the environment.

Most importantly for the present audit, the authors explicitly state that a purely observational measure leaves ambiguity over whether observed effects should be attributed to the system or the environment, motivating a causal-structure-aware variant.

### Why this is close to sigma_sr

SRT's current motivation says, approximately:

```text
next selection constrained by own historical trace
vs
non-self external condition
```

The autonomy literature already asks, approximately:

```text
next system state determined by own previous state/history
vs
environmental history / external causal influence
```

This is a serious role-level overlap, not merely verbal similarity.

### What it does not automatically settle for SRT

It does not, by itself, answer:

```text
SRT bearer admission;
trace ownership under shared L2;
subject-position phase-transition claims;
phenomenality;
the exact Core22 projection architecture.
```

But it materially subtracts any claim that SRT invented the generic self-history-versus-environment control ratio problem.

### Verdict

`ROLE-MATCH PRESSURE = HIGH`.

---

## 5. Current subtraction matrix

| SRT repair burden | Mature external owner family | SRT may borrow role | SRT may claim generic novelty? |
|---|---|---:|---:|
| coordinate invariance | Fisher-Rao / Čencov information geometry | yes, conditionally | **no** |
| implementation-invariant attribution | Integrated Gradients / axiomatic attribution | yes | **no** |
| nonlinear interaction allocation | Shapley / Shapley-Taylor / recursive Shapley | yes | **no** |
| causal control strength | Pearl/Janzing/Ay-Polani/do-Shapley | yes | **no** |
| self-history vs environment autonomy | information-theoretic autonomy | comparison/rival | **no** |
| co-regulation -> self-regulation | developmental/scaffolded cognition | comparison/rival | **no** |

---

## 6. Residual after formal subtraction

The strongest surviving SRT question is no longer:

```text
How can we measure self-history?
```

nor:

```text
How can external structure become internal?
```

nor:

```text
How can we build an invariant attribution scalar?
```

All are crowded territories.

The narrower residual is:

> **Current SRT compresses at least four roles—historical provenance, boundary-relative endogeneity, ongoing dependence, and present causal control—into a trace/ext scalar that is then used as an individuation order parameter. Which role, if any, is constitutively relevant to subject-position entry, and can that role be connected to the others without circularly presupposing bearer/selector status?**

Compactly:

```text
provenance
!= endogeneity
!= dependence
!= control

which one is the individuation variable?
```

This is an SRT internal dependency-architecture problem.

It may become externally interesting only if SRT can establish one of:

1. a nontrivial theorem that one typed relation predicts / constrains another under explicit conditions;
2. a D2 case where rival autonomy/control measures match but the SRT-typed distinction predicts something additional;
3. a bounded no-go showing no single scalar can carry all four roles, with consequences for theories that conflate historical ownership and control.

None is established yet.

---

## 7. Implication for outcome selection

After external subtraction:

### SURVIVES

Broad current reading is not supported by the internal probes.

### SURVIVES-WITH-REPAIR

Possible, but most candidate repair mathematics is borrowed prior art. The SRT contribution would be correct role typing and integration, not inventing Fisher/Shapley/causal strength.

### SPLIT

Currently the strongest **internal** architectural hypothesis.

But splitting a scalar into provenance/control by itself is not yet externally novel because autonomy and attribution literatures already separate related roles.

### RETYPE

Also credible: retain current sigma as a model-local historical/writeback proxy and remove stronger control/natural-boundary interpretations until separately supported.

### NO-GO

A useful future result if one can prove, under broad conditions, that no single representation-invariant scalar can simultaneously satisfy the intended provenance and control roles. No such theorem exists in this audit yet.

---

## 8. What not to do next

Do not:

```text
edit frozen sigma owners immediately;
rename two new canonical sigmas;
claim Fisher fixes SRT;
claim Shapley gives bearer ownership;
claim information-theoretic autonomy confirms SRT;
write a publication pitch around internalization;
return to neural-unity paper selection.
```

---

## 9. Recommended next decision point

The read-only discovery phase has now produced enough evidence to force an architectural choice.

Before another broad audit, answer:

> **What is the intended semantic target of the individuation order parameter?**

Candidate choices to compare in a bounded decision packet:

```text
P — provenance / own-history attribution
E — current endogeneity to declared unit
D — independence from ongoing external support
C — causal control over next selection / future selectability
S — split architecture: no single scalar carries all roles
R — retype sigma as model-local proxy and suspend natural-boundary language
```

This is an author/theory-design decision after evidence gathering. It should not be hidden inside another audit.

---

## 10. Source anchors checked

- Sundararajan, Taly & Yan (2017), *Axiomatic Attribution for Deep Networks*, ICML / PMLR 70.
- Sundararajan, Dhamdhere & Agarwal (2020), *The Shapley Taylor Interaction Index*, ICML / PMLR 119.
- Singal, Michailidis & Ng (2021), *Flow-based Attribution in Graphical Models: A Recursive Shapley Approach*, ICML / PMLR 139.
- Jung et al. (2022), *On Measuring Causal Contributions via do-interventions*, ICML / PMLR 162.
- Janzing et al. (2024), *Quantifying intrinsic causal contributions via structure preserving interventions*, AISTATS / PMLR 238.
- Bertschinger, Olbrich, Ay & Jost (2008), *Autonomy: An information theoretic perspective*, Biosystems 91(2):331–345, DOI 10.1016/j.biosystems.2007.05.018.
- Information-geometry sources confirming Fisher-Rao invariance / Čencov characterization under the relevant statistical/Markov-map setting.

The role-matched literature is mature enough that no generic repair concept above should be advertised as an SRT invention.

---

## 11. Terminal status

```text
FORMAL GATE-2 EXECUTED: YES
DEFECT-B GENERIC REPAIR NOVELTY: SUBTRACTED
DEFECT-A GENERIC ATTRIBUTION NOVELTY: SUBTRACTED
DEFECT-C GENERIC CAUSAL-CONTROL NOVELTY: SUBTRACTED
SELF-HISTORY VS ENVIRONMENT AUTONOMY NOVELTY: HIGH PRIOR-ART PRESSURE
CURRENT BEST SRT RESIDUAL: ROLE TYPING / DEPENDENCY ARCHITECTURE
PUBLICATION-READY NOVELTY: NOT ESTABLISHED
OWNER EDIT AUTHORIZED: NO
B1 CONSUMED: 0
NEXT: BOUNDED SIGMA SEMANTIC-TARGET DECISION PACKET, NOT ANOTHER BROAD AUDIT
```
