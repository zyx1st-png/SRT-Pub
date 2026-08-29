---
id: SRT-OPS-AUDIT-ATTENTION-DYNAMICS-RIVAL-ADDITION-P24-3-P24-4-20260826
type: audit_record
status: active
record_stage: rival_addition
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-08-26
dependency:
  - SRT-OPS-AUDIT-POST-RCA-SELECTION-D2-RANKING-20260817
  - SRT-CORE-24-DISCRIMINATING-PREDICTIONS
  - SRT-OPEN-TENSIONS
  - HOOK-PHIL-PH-ATTN01-REPRESENTATION-WEIGHT-ENGAGEMENT-OPERATIVITY
source_ids:
  - SRC-2026-08-26-PHIL-AMORNBUNCHORNVEJ-DISAGREEMENT-ATTENTION
tags: [P24-3, P24-4, RivalModel, Attention, LearnedInattention, Hysteresis, CandidateVisibility, D2]
---

# Attention-Dynamics Rival Addition — P24-3 / P24-4

> **Purpose:** add a source-backed ordinary rival family to the existing post-RC-A P24-3 / P24-4 discrimination workline.  
> **Status:** rival hardening only. This audit does not modify canonical P24 claims and does not claim the source model is the uniquely best rival.

---

## 0. Executive verdict

Amornbunchornvej's attention-dynamics model can reproduce several signatures currently relevant to P24-3 and P24-4 while assuming fully shared representation and without a Selection-specific variable.

Therefore add the following bounded rival family to future floor-challenge / visibility studies:

```text
R_ATT = persistent latent gain state
      + context-conditioned attention profile
      + separable total engagement
      + bounded / gated reweighting
```

The important scientific consequence is negative:

```text
fixation
hysteresis-like persistence
slow alternative reactivation
history-dependent weighting
reduced current salience
practical non-reachability within a horizon

!= by themselves

Selection-level D2
```

---

## 1. Rival schema

For a fixed represented basis `B`:

```text
lambda_t = persistent latent gain state
c_t      = current context
h_t      = unnormalized expressed gain
w_t      = normalized relative profile
s_t      = total engagement
```

Reference expression:

```text
h_i(lambda_t,c_t) > 0
w_t,i = h_i / sum_j h_j
s_t   = sum_j h_j
```

Evaluation:

```text
e_t(x|c) = s_t(c) * sum_i w_t,i(c) x_i
```

Bounded update class:

```text
lambda_{t+1} = lambda_t + delta_t
||delta_t||_infinity <= epsilon
```

The exact multiplicative form is source-specific and empirically exposed; future SRT studies may freeze an additive or alternative bounded attention-learning family as well. The rival role is broader than the source's exact formula:

> a persistent attentional state can gate its own revision and thereby generate entrenchment without candidate-basis loss.

---

## 2. What R_ATT can already explain

### 2.1 P24-3-adjacent signatures

R_ATT can produce:

- increasingly dominant weighting on a learned dimension;
- low absolute growth of long-ignored rival dimensions under proportional gating;
- switching / reallocation cost when task relevance changes;
- cross-context persistence of a dominant profile;
- finite-horizon practical non-reachability despite formal possibility of eventual reweighting;
- recovery trajectories that do not retrace the original state.

Hence:

```text
old path remains dominant after mismatch
```

is not sufficient to infer a distinct SRT mechanism.

### 2.2 P24-4-adjacent signatures

R_ATT can produce:

```text
represented consideration
+ negligible current weight
-> near-zero online influence
```

which may look behaviorally like candidate invisibility.

Therefore reduced report, gaze, choice frequency, or local influence does not by itself establish:

```text
basis loss
candidate-generation change
admissibility-rule change
```

---

## 3. Required discrimination layers for P24-4

Future P24-4 studies should separate at least:

### Layer A — representation / basis membership

Readouts:

- recognition;
- retrieval;
- articulation;
- use when dominant cue is removed.

### Layer B — current online operativity

Readouts under controlled perturbation:

- valuation change;
- choice-probability change;
- reaction-time / gaze / path effect;
- local causal efficacy.

### Layer C — candidate-generation / admissibility structure

Readouts should ask whether the option can be generated / admitted under controlled prompts or structural changes, not merely whether it currently receives low weight.

### Layer D — later historical efficacy

Where relevant, test whether an event changes later:

- probability / weighting;
- reachability / return cost;
- comparison rule;
- boundary / composition;
- candidate generator.

No single layer substitutes for the others.

---

## 4. Required rival discipline for P24-3

A future matched scaffold / floor-challenge study should pre-freeze whether `R_ATT` is allowed to contain:

```text
latent gain vector
context modulation
attention-dependent learning rate
bounded additive or multiplicative update
competitive coupling
finite memory / history state
engagement variable
```

and must freeze:

- calibration data;
- update family;
- memory window;
- parameter count / complexity budget;
- out-of-sample forecast target;
- failure condition.

Post-result expansion of attention state is not allowed in a D2 duel.

---

## 5. Strong negative controls

### 5.1 Behavioral silence control

If a consideration shows little online effect, test whether it remains encoded and retrievable.

```text
encoded + retrievable + silent
-> supports negligible-weighting class
not basis absence
```

### 5.2 Cue-removal control

Remove / disable the dominant cue or dimension and test whether the previously silent dimension becomes usable.

Rapid use after cue removal pressures a basis-loss interpretation.

### 5.3 Engagement control

Hold relative profile approximately fixed while varying task / domain demand. This tests whether total engagement varies independently and prevents relative-weight differences from absorbing every effect.

### 5.4 Same-current-profile / different-history control

Match current measured profile and engagement across different training histories, then challenge prospectively.

A difference shows current measurements are insufficient but is not by itself SRT-specific; the frozen rival may contain predeclared latent history state.

---

## 6. What would exceed R_ATT's natural scope?

The source model explicitly fixes the evaluative basis. Its natural scope is reweighting over already represented dimensions.

The following are therefore stronger targets, but still require comparison to other R2 families:

```text
new evaluative dimension acquisition
candidate-generator change
comparison-rule revision
boundary / composition revision
same-unit consequence-bearing differences
bearer-specific non-outsourcing
```

Important:

```text
outside R_ATT
!= automatically SRT-specific
```

Representation-learning, meta-learning, affordance, control and generative rivals remain live.

---

## 7. Relation to P24-3 ranking

The 2026-08-17 post-RC-A ranking already concluded that P24-3 is a calibration priority, not D2-ready, because ordinary learning / attractor / predictive-control / hysteresis families can reproduce its signatures.

This audit adds a more specific source-backed member:

```text
learned-inattention / self-gated attention dynamics
```

to that rival set.

Disposition:

```text
P24-3 priority: unchanged
D2 readiness: unchanged (NO)
rival burden: strengthened
```

---

## 8. Relation to P24-4 ranking

The 2026-08-17 ranking already identified attention and representation models as absorption risks for visibility/admissibility effects.

This source sharpens the exact false positive:

```text
option seems absent behaviorally
but is encoded and retrievable
and merely receives negligible current weight
```

Disposition:

```text
P24-4 auxiliary value: unchanged
candidate-absence inference: tightened
required dissociation controls: strengthened
```

---

## 9. Failure conditions for this rival addition

Do not over-strengthen R_ATT into an unrestricted absorber.

Its source-backed form is pressured if:

- encoded dimensions can have exactly zero evaluative contribution rather than graded-negligible contribution;
- long-ignored dimensions can leap to dominance under one ordinary update;
- valuation uses discrete subsystem selection rather than weighted summation;
- learning-gating and valuation-weighting states dissociate;
- fixed-basis assumptions fail because genuinely new evaluative dimensions are acquired.

A bounded D2 rival must preserve these failure exposures rather than widening after outcome observation.

---

## 10. Final disposition

```text
ADD R_ATT TO P24-3 / P24-4 RIVAL LIBRARY
NO CANONICAL CHANGE
NO D2 CLAIM
NO ATTENTION = SELECTION IDENTIFICATION
NO ENGAGEMENT = d IDENTIFICATION
NO WEIGHTING = GENERATIVE RESELECTABILITY IDENTIFICATION
```

Next legitimate use: include `R_ATT` as one preregistered bounded rival in a future P24-3 floor-challenge duel or P24-4 representation-vs-operativity calibration study.
