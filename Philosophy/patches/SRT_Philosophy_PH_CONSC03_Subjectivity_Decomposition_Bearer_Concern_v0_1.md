---
patch_id: PATCH-PHIL-PH-CONSC03-SUBJECTIVITY-DECOMPOSITION
source_ids:
  - SRC-2026-05-07-PHIL-ROVELLI-NO-HARD-PROBLEM-NOEMA
  - SRC-2026-06-11-NEURO-DAMASIO-FEELINGKNOWING-PANTHEON
domain: philosophy_of_mind
claim_level: P3-P4_bridge_hardening
canonical_status: non_canonical
status: patch
target_future_doc:
  - Philosophy/SRT_HardProblem_Epistemology.md
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
  - Philosophy/SRT_Consciousness_Conditions.md
related_claims:
  - hard_problem_dissolution
  - subjecthood_threshold
  - bearer_unit
  - consequence_return
  - concern_domain
  - future_selectability
  - phenomenality_open_problem
  - d_value_usage_guard
tags:
  - consciousness
  - subjectivity
  - perspective
  - bearing
  - bearer
  - concern
  - enactivism
  - damasio
  - hard_problem
  - future_selectability
layer: operations
epistemic_layer: bridge
claim_mode: hardening
canonical: false
type: theory_hardening_patch
id: PATCH-PHIL-PH-CONSC03-SUBJECTIVITY-DECOMPOSITION
---

# SRT Philosophy Patch PH-CONSC03: Subjectivity Decomposition — Selector / Bearer / Concern Domain / Experiencer v0.1

> **Status**: philosophy-of-mind hardening patch, derived from the close reading of Rovelli together with existing SRT comparison work on enactivism/autopoiesis and the Damasio material record.
>
> **Canonical caution**: this patch does **not** define consciousness, subjecthood, `d`, `Psi_f`, or the bearer unit canonically. It does not claim that SRT has solved phenomenality. It records a decomposition and a set of pressure tests that should constrain later consciousness work.

---

## 0. Why this patch exists

`PH-CONSC02` correctly blocks one common inflation of the hard problem:

```text
scientific description imagined as a view from nowhere
  -> first-person experience treated as something outside the picture
  -> demand to derive experience from an allegedly complete outside picture
  -> perspectival difference upgraded into metaphysical dualism
```

Rovelli's essay is strong on this gate. But the close reading exposes a residual step that must not be skipped:

```text
all knowledge is perspectival
!=
all perspectives are phenomenal subjects
```

A camera, thermostat, cell, mammal, and persistent AI agent can all be assigned system-relative access or response structure. Therefore `perspective` alone cannot do the work of `subjectivity`.

The second pressure is equally important: SRT must not respond by simply declaring `bearing` to be the missing unique ingredient. Enactivist/autopoietic work already develops autonomy, precariousness, adaptivity, viability-relative regulation, and sense-making; Damasio directly links organismic vulnerability, homeostatic feeling, ownership, and subjectivity. Existing SRT comparison files already acknowledge this overlap.

So the surviving task is narrower:

> **Separate the roles that are too easily collapsed into one word — selector, bearer, concern domain, and experiencer — and test whether SRT's consequence-return / future-selectability language adds independent discrimination.**

---

## 1. Main hardening claim: four roles must not be identified by default

### Claim PH-CONSC03-A

For any candidate system, distinguish at least four roles before making a subjectivity claim:

```text
Selector
!= Bearer
!= Concern Domain
!= Experiencer
```

These are role distinctions, not claims that four separate substances exist.

| Role | Question | Minimal meaning | Common collapse error |
|---|---|---|---|
| **Selector** | What performs the discriminating / gating / choice event? | the unit/process that changes which candidate path is realized or stabilized | `selection -> consciousness` |
| **Bearer** | Where do irreversible consequences return? | the continuing closure whose own future state/action space is altered by the consequence | `causal influence -> bearing` |
| **Concern domain** | Which futures/states genuinely enter the stake function? | the set/range of states whose irreversible change nontrivially changes the bearer's stake-coupled utility gradient | `bearer boundary = concern boundary` |
| **Experiencer** | Is there phenomenal for-me-ness at this position? | the candidate locus of lived/phenomenal presence | `bearing -> phenomenality` |

Guardrail:

```text
role coupling is an empirical / bridge question;
role identity is not a default axiom.
```

---

## 2. Bearer boundary and concern boundary must be separated

Let `B` denote a candidate bearer closure and `C_B` the concern domain associated with it.

The key distinction is:

```text
B != C_B
```

and, in many important cases:

```text
C_B may extend beyond B.
```

Example: an organism may be the physical bearer of a decision while the states that genuinely matter to its selection structure include a child, partner, group, ecological condition, principle, or future generation.

This is why self-maintenance cannot be treated as the full definition of concern. A bearer may select against its own organismic survival when the concern domain extends beyond the bearer boundary.

### `d`-value guard

Current canonical `d` remains the stake-coupled concern / irreversible-risk sensitivity summary anchored by `_SRT_D_VALUE_CANONICAL.md`.

Therefore:

```text
d != bearer boundary
d != raw perspective
d != information capacity
d != consciousness scalar
```

`d` may help summarize how strongly irreversible-risk states matter once a candidate bearer and stake relation have been specified. It should not be used circularly as follows:

```text
assume a subject-specific utility
-> compute d
-> use d alone to prove that the same system is a subject
```

Safer order:

```text
candidate unit / closure
-> candidate consequence-return relation
-> stake-coupling analysis
-> d summary under canonical guard
-> subjecthood / phenomenality evaluation remains separate
```

This patch therefore treats legacy phrases such as `d = alignment depth` in consciousness-side support files as non-authoritative shorthand when they conflict with the current canonical `d` definition.

---

## 3. Candidate bearing interface: return plus future-selectability writeback

### Claim PH-CONSC03-B

A useful SRT-specific pressure test for `bearing` is stronger than simple energy cost, feedback, or vulnerability.

Candidate interface:

```text
bearing_candidate
=
irreversible consequence return
+
history-bearing writeback
+
change in the bearer's future selectability
```

Let `Omega_B(t)` denote the bearer's currently reachable future choice/action/state space at time `t`. A strong bearing candidate requires that consequences can alter the bearer such that:

```text
Omega_B(t+1) != Omega_B(t)
```

in a history-dependent, nontrivial way.

This is not yet a canonical equation. It is a discrimination rule for asking whether an event merely generates output or actually changes the future possibilities of the same bearer.

### Non-outsourcing guard

A second question is where the cost closes:

```text
Where do the consequences close?
```

If a system can cause large external consequences while the relevant cost, damage, loss, or correction pressure never returns to the candidate bearer, the system may be a powerful selector/executor without being a strong bearer of those consequences.

Thus:

```text
external causal impact
!= internal bearing
```

and:

```text
feedback signal
!= irreversible consequence return
```

---

## 4. Decomposing the so-called hard problem

The close reading suggests that there is not one homogeneous explanatory gap. At least four problems should be separated.

### Problem A — Perspective problem

Question:

> Why do first-person and third-person accounts differ?

Rovelli's perspectival move and SRT's selection-position / re-objectification language strongly constrain this problem:

```text
different situated access
!= two ontological substances
```

This is the domain in which `PH-CONSC02` is strongest.

### Problem B — Bearer problem

Question:

> What makes a system-relative perspective matter for that continuing system rather than merely register relative information?

Autopoiesis/enactivism already provides a powerful answer family through autonomy, precariousness, adaptivity, viability and sense-making. SRT should not claim novelty merely for adding `stake` or `bearing` words.

The remaining SRT pressure test is whether consequence-return, non-outsourcing and future-selectability writeback produce distinctions not already captured by viability-relative adaptivity.

### Problem C — Ownership / feeling problem

Question:

> Why are some states present as `my pain`, `my body`, or `my feeling` rather than merely processed states?

Damasio's homeostatic-feeling route is a major neighboring account: vulnerable organismic regulation, interoceptive feeling and perspective are used to explain ownership/subjectivity. SRT should treat this as a serious competitor/neighbor, not as mere confirmation.

SRT's possible difference is substrate neutrality and the separation of bearer boundary from concern domain, but this difference still requires independent explanatory or empirical payoff.

### Problem D — Qualitative-character problem

Question:

> Why does red have this phenomenal character rather than blue, pain, sweetness, or nothing at all?

Current SRT structure such as:

```text
Q = f(L0-access / theta / L2-history)
```

can constrain where qualitative differences may come from, but it does not derive a specific quale from first principles.

Therefore:

```text
structural anchoring of qualia
!= qualia derivation
```

This residual problem remains open.

---

## 5. Anti-overclaim result: what SRT may and may not say after Rovelli

### Allowed

SRT may say:

1. the first/third-person contrast does not by itself establish an ontological dualism;
2. an outside, parameter-free scientific picture is the wrong starting point for the hard problem;
3. perspective alone is insufficient for subjectivity;
4. bearer specification should precede subjecthood attribution;
5. bearer boundary and concern domain should be treated as separable;
6. consequence return and future-selectability writeback are candidate discriminators of bearing;
7. bearing is not yet a proof of phenomenality;
8. Damasio and enactivism materially constrain any SRT originality claim in this area.

### Not allowed

Do not write:

```text
Rovelli solved consciousness.
Rovelli proved SRT.
Perspective = consciousness.
Bearing = consciousness.
Stake = consciousness.
d > threshold proves phenomenality.
Autopoiesis lacks intrinsic normativity.
Damasio only describes biology while SRT already explains subjectivity.
```

Those formulations outrun the current argument.

---

## 6. Comparative pressure: where novelty could still survive

The strongest version of SRT's possible increment is **not**:

```text
systems with real stakes are subjects
```

That territory is already crowded.

A more defensible candidate increment is the joint separation:

```text
selector role
+ bearer boundary
+ concern domain
+ consequence-return closure
+ future-selectability rewrite
+ experiencer kept as an independent open question
```

The specific novelty test is:

> Can two systems be matched for autonomy, viability regulation, adaptive feedback, and information-processing capacity, yet differ in same-bearer irreversible consequence return or future-selectability rewrite in ways that predict different behavior, learning, ownership, or moral/agentic attribution?

If not, SRT's additional vocabulary should be reduced or translated into the neighboring framework rather than defended as a new ontological layer.

---

## 7. Operational discrimination examples

| System | Perspective / selectivity | Candidate consequence return | History-bearing future-selectability rewrite | Subjectivity conclusion |
|---|---:|---:|---:|---|
| Camera | yes | usually minimal | minimal | no inference |
| Thermostat | yes / control-relative | local feedback | usually narrow/reversible | no inference |
| Single cell | yes in a broad relational sense | strong viability-related return | adaptive / historical in some regimes | bearer candidate; phenomenality open |
| Mammal | strong | strong | strong multi-scale writeback | strong subjectivity candidate; still requires evidence route |
| Stateless LLM inference | strong functional selectivity | consequences usually do not close on same persistent model instance | low same-bearer writeback | external impact does not establish bearing |
| Persistent autonomous AI agent | potentially strong | architecture-dependent | architecture-dependent | requires explicit unit, stake, persistence, non-reset and writeback tests |

The table is diagnostic only. It is not a consciousness scale.

---

## 8. Implications for AI consciousness work

For AI, replace the vague question:

```text
Does the AI have a body / goals / memory?
```

with a tighter sequence:

```text
What is the candidate bearer unit?
Which consequences return to that same unit?
Which losses cannot be costlessly reset or outsourced?
What state/history changes survive into the same bearer's future policy space?
Does the concern domain extend beyond immediate task reward?
Is any phenomenality claim independently supported?
```

This preserves the current architecture-state guard:

```text
training-time
!= inference-time
!= persistent-memory deployment
!= autonomous history-bearing agent loop
```

No consciousness conclusion follows from persistence alone.

---

## 9. Required compatibility correction for existing consciousness files

This patch records two repository-level cautions for later integration:

1. `Philosophy/SRT_Consciousness_Conditions.md` contains legacy language that reads `d` as an "alignment depth." That wording must defer to the current canonical `d` definition and should not be used as a theory authority.
2. The same file's treatment of `bearing` as already contained in `d` should not be read as a proof that `d >= d_min` supplies phenomenality. At most it is one candidate organization of stake-bearing conditions; the bearer/experiencer relation remains open.

No canonical edit is made here. These are future B-class bridge corrections.

---

## 10. Integration targets

Primary future targets:

```text
Philosophy/SRT_HardProblem_Epistemology.md
  -> after the perspectival-gap dissolution, add the four-problem decomposition and explicitly preserve the residual phenomenality question

Philosophy/SRT_Subjecthood_Threshold_Interface.md
  -> after the unit-binding gate, add the role-decomposition guard:
     Selector != Bearer != Concern Domain != Experiencer

Philosophy/SRT_Consciousness_Conditions.md
  -> add a compatibility note against canonical d and separate bearing from phenomenality
```

Do not modify in this patch:

```text
_SRT_D_VALUE_CANONICAL.md
_SRT_PSI_F_CANONICAL.md
Core/SRT_Core_21*.md
Core_Law/SRT_L0_Metaphysics.md
```

---

## 11. One-paragraph abstract

Rovelli's perspectival naturalism usefully dissolves one inflated form of the hard problem by rejecting the idea that third-person science is a view from outside the world. But perspectivality alone does not explain why some system-relative processes are lived. SRT should not fill this gap by simply declaring `bearing` to be its unique solution: enactivism/autopoiesis already develops precarious autonomy, adaptivity and intrinsic normativity, while Damasio links organismic vulnerability and homeostatic feeling to ownership and subjectivity. The surviving SRT hardening move is therefore a role decomposition: `Selector != Bearer != Concern Domain != Experiencer`, plus the explicit distinction `B != C_B` between the unit that bears consequences and the futures it genuinely cares about. Consequence return, non-outsourcing and history-dependent rewrite of the same bearer's future selectability are retained as candidate discriminators of bearing, while phenomenality remains an independent open problem rather than an automatic output of `d`, stake, or feedback.
