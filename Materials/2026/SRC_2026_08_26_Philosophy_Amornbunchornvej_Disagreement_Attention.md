---
id: SRC-2026-08-26-PHIL-AMORNBUNCHORNVEJ-DISAGREEMENT-ATTENTION
type: source_material
status: active
source_type: paper
source_scope: uploaded_pdf
source_verification: conversation_pdf_read_full
claim_level: source
canonical: false
date: 2026-08-26
tags: [Attention, Disagreement, Representation, Engagement, Plasticity, Lock, LearnedInattention, RivalModel, P24-3, P24-4]
---

# Amornbunchornvej 2026 — *Disagreement without Representational Deficit: Attention Dynamics over a Shared Evaluative Basis*

## 0. Source and disposition

Source used for this card: user-provided PDF in the 2026-08-26 reading session.

**SRT disposition:** high-value adjacent model / ordinary rival / empirical bridge; **not** a Selection-core source and **not** evidence that attention, valuation, engagement, bounded plasticity, or disagreement persistence are SRT-specific.

Recommended use:

```text
material card
+ bounded integration hook
+ P24-3 / P24-4 rival hardening
```

Do not promote directly to canonical theory.

---

## 1. Paper's central target

The paper breaks the inference:

```text
persistent evaluative disagreement or fixation
-> representational deficit / framework mismatch
```

It argues that persistence is compatible with fully shared representation. Given a shared evaluative basis, three separable structures can differ:

```text
representation / basis membership
!= relative attention profile
!= total engagement
```

A disagreement may therefore persist because the same represented considerations receive different relative weights, because the whole domain matters to different degrees, and/or because ordinary reweighting is bounded and slow.

The paper's central diagnostic conclusion is underdetermination:

```text
persistence alone does not discriminate
representational mismatch
from
shared representation + different weighting / engagement + bounded plasticity
```

---

## 2. Minimal model

### 2.1 Shared evaluative basis

The representable dimensions are held fixed:

```text
B = {b1, ..., bn}
```

The model does not address acquisition of genuinely new evaluative dimensions (basis extension).

### 2.2 Persistent gain state

Each dimension has positive gain:

```text
lambda_t in R^n
theta_t,i = exp(lambda_t,i) > 0
```

Hence a represented dimension may become arbitrarily weak without being mathematically annihilated.

Critical distinction:

```text
absent from basis
!=
present but functionally negligible
```

### 2.3 Profile and engagement

In context `c`, an unnormalized expression `h(lambda_t,c)` is decomposed into:

```text
w_i(c) = h_i / sum_j h_j
s(c)   = sum_j h_j
```

where:

```text
w = relative attention profile
s = total engagement with the domain
```

The valuation rule is:

```text
e_t(x | c) = sum_i h_i(lambda_t,c) x_i
           = s_t(c) * sum_i w_t,i(c) x_i
```

Thus identical relative priorities do not imply identical engagement.

### 2.4 Context modulation

A reference class uses:

```text
h_i(lambda,c) = exp(lambda_i + phi_i(c))
w(c) = softmax(lambda + phi(c))
```

The intended distinction is:

```text
persistent disposition
+ context-conditioned expression
-> current weighting
```

---

## 3. Dynamics and lock

### 3.1 A1 — bounded relative plasticity

Endogenous learning is:

```text
lambda_{t+1} = lambda_t + delta_t
||delta_t||_infinity <= epsilon
```

Equivalently, gain changes by a bounded multiplicative factor per step.

This yields:

```text
|Delta theta_i| <= (exp(epsilon)-1) theta_i
```

so low-gain dimensions can change only a small absolute amount per step.

Paper's key phrase / mechanism:

```text
attention gates its own revision
```

This can generate a self-maintaining pattern:

```text
low current weighting
-> little effective revision
-> continued low weighting
```

### 3.2 Lock

A state is locked on dimension `i*` across context class `C` when that dimension retains near-total profile dominance across contexts that would ordinarily pull weighting apart.

The important structural property is:

```text
cross-context dominance
```

not the semantic content or normative value of the dominant dimension.

### 3.3 Persistence bound

Given a lock margin and bounded per-step drift, the paper derives a finite lower bound on how long the lock must persist. In its multiplicative reference class the sharp form is proportional to:

```text
margin / plasticity ceiling
```

The philosophically useful result is not impossibility, but:

```text
exact impossibility
!= practical non-reachability within a relevant horizon
```

### 3.4 Recovery

The paper notes that restoring a formerly dominant gain does not generally restore the full old state because other coordinates have changed meanwhile:

```text
recovery is a further forward transition
!= inverse replay to the old state
```

---

## 4. Taxonomy of evaluative difference

The paper distinguishes at least:

1. different bases -> possible representational mismatch;
2. same basis + same profile + same engagement -> same evaluation under the model;
3. same basis + different profile -> evaluative disagreement without representational mismatch;
4. same basis + same profile + different engagement -> same relative priorities, different total domain importance;
5. same basis + different locked profiles -> persistent disagreement within the bounded-plasticity horizon.

It further separates:

```text
persistence of the source structure
!= inertia of one particular evaluative output gap
```

This source/output separation is methodologically useful beyond disagreement theory.

---

## 5. Empirical anchors consumed by the argument

### 5.1 Encoded, retrievable, not consulted

The strongest SRT-relevant empirical anchor is the Gao et al. (2024) dissociation discussed by the paper:

```text
feature encoded / recognized above chance
+ usable when dominant feature removed
+ no measurable online influence while dominant feature available
```

Paper's interpretation:

```text
knowledge present, influence absent
```

This supports the distinction:

```text
basis membership / availability
!= online operative weighting
```

### 5.2 No fixed total attention budget

The paper argues against treating normalized profile as a fixed total-attention budget. It separates:

```text
relative distribution w
from
total engagement s
```

and cites model-comparison evidence that total attention varies with task demand. A fixed-budget regime may reappear approximately when a soft engagement ceiling binds.

### 5.3 Learned inattention / learning traps

The paper treats learned inattention as the behavioral analogue of lock: dimensions trained as irrelevant become costly to re-attend to when later relevant. It also cites learning-trap / reduced-exploration phenomena as adjacent evidence for history-dependent entrenchment.

---

## 6. One state, two roles — pivotal empirical exposure

The paper identifies the state that gates learning with the state that weights valuation:

```text
learning-gating state
=
valuation-weighting state
```

This identification is necessary for its persistence dynamics to constrain evaluative disagreement directly.

The paper explicitly acknowledges that if these roles dissociate, the main persistent-disagreement result weakens.

SRT-side importance:

```text
what gets written / learned
must not be silently equated with
what currently weights evaluation / action
```

unless independently justified.

---

## 7. Complement to representational annihilation

The paper contrasts two structures:

```text
annihilation / basis absence
vs
negligible weighting within a shared basis
```

The distinction is empirically testable:

```text
annihilation candidate:
encoding / recognition near chance

negligible-weighting candidate:
encoding above chance
+ absent or near-absent online influence
```

This is a useful general diagnostic template for SRT candidate-field work.

---

## 8. Explicit scope limits and falsifiers

### 8.1 Fixed basis

The model redistributes over given dimensions. It does not explain:

```text
basis extension
new evaluative dimension acquisition
candidate-generator revision
```

### 8.2 Multiplicative-plasticity bet

The paper explicitly identifies multiplicative A1 as its weakest pivotal modeling choice. The fitted literature it reviews leans additive; published support is stronger for multiplicative decay than growth.

Therefore SRT must not import the paper's exact persistence law as an established empirical law.

### 8.3 Persistence only

A1 is a ceiling, not a floor. The model constrains how long a configuration can persist, not when disconfirming experience must unlock it.

### 8.4 History-blind bound

The persistence bound depends on current margin and plasticity ceiling; how the state was formed leaves no independent trace in the bound. Whether history matters only through current state or independently remains open.

### 8.5 Collected failure conditions

The paper states that its commitments fail or weaken if, among other things:

- an encoded basis dimension contributes exactly zero rather than graded-negligible influence;
- a long-ignored dimension leaps to dominance in one ordinary endogenous experience;
- evaluation follows a per-stimulus discrete maximum / system-selection architecture instead of smooth weighted summation;
- learning-gating and valuation-weighting states dissociate.

---

## 9. SRT relevance after subtraction

### 9.1 High-value contribution

The paper strongly supports maintaining these non-identities at bridge / audit level:

```text
representable
!= available / retrievable
!= relatively weighted
!= total engagement
!= online operative influence
!= SRT Selection
!= historical writeback
```

This is a category-hygiene ladder, not a new canonical ontology.

### 9.2 Candidate field

The paper supplies a concrete ordinary mechanism for cases where something remains representable but becomes behaviorally silent:

```text
candidate represented
+ very low weight
-> apparent invisibility without actual basis loss
```

Therefore behavioral invisibility alone cannot establish candidate absence or generator change.

### 9.3 Concern / matter / d guard

Do not equate:

```text
relative profile w
with matter / concern membership / d
```

and do not equate:

```text
total engagement s
with bearer-relative stake / d-value
```

The paper's variables describe attentional-evaluative organization, not SRT consequence bearing or non-substitutability.

### 9.4 L2 / P24-3 rival

Self-gated attention dynamics can absorb ordinary signatures including:

- fixation;
- selective-history entrenchment;
- slow alternative reactivation;
- switching cost;
- hysteresis-like persistence;
- practical non-reachability within a horizon.

Thus these signatures alone cannot establish SRT-specific L2 hardening or Selection-level D2.

### 9.5 P24-4 rival

The model can produce:

```text
represented option
+ negligible current weight
-> option behaves as if invisible in ordinary evaluation
```

Therefore P24-4 visibility/admissibility work must distinguish at least:

```text
basis absence
vs negligible weighting
vs genuine candidate-generation / admissibility revision
```

### 9.6 Generative reselectability boundary

The paper's explicit fixed-basis scope reinforces:

```text
reweighting existing dimensions
!= changing what dimensions / candidates can be generated or admitted
```

Any stronger rule / boundary / candidate-generator revision remains routed to existing SRT B13 / HEF owners rather than this attention model.

### 9.7 Bearer boundary

The paper presupposes agents and does not identify a consequence bearer. It supplies no same-unit-return, non-outsourcing, identity, or bearer-continuity criterion.

Hence:

```text
attention lock
!= bearer admission
```

### 9.8 Historical support, not novelty

The paper's claim that recovery is a forward transition rather than an inverse is useful external support for existing SRT history-bearing distinctions, but should not create a parallel construct.

---

## 10. Strongest SRT empirical reuse

### Assay A — representation vs influence

Measure independently:

```text
recognition / retrieval / articulation
```

and:

```text
online influence under controlled perturbation
```

so that behavioral silence cannot be misclassified as basis absence.

### Assay B — absent vs negligible vs operative

Construct matched cases:

```text
A: absent / not encoded
B: encoded but negligible online influence
C: encoded and operative
D: encoded + operative + later historical writeback
```

This can calibrate representation, current efficacy and later historical efficacy separately.

### Assay C — P24-3 floor challenge with frozen attention rival

Include a bounded latent-attention rival with preregistered state/update family when testing L2 hardening. SRT-specific progress would require an outcome difference the frozen rival prospectively excludes, not merely observation of entrenchment or hysteresis.

### Assay D — same apparent weighting, different history

Matching current `w` and `s` while varying formation history can test whether these are sufficient state descriptors. A future difference would show omitted history/state, but would not by itself establish SRT D2 unless a bounded R2 rival had already frozen its allowed memory architecture.

---

## 11. Final SRT verdict

```text
Selection-core novelty: low
bearer novelty: low
matter / concern category hygiene: high
candidate-field clarification: high
L2 / P24-3 ordinary-rival value: very high
P24-4 ordinary-rival value: very high
empirical-assay value: high
D2 proof value: none by itself
```

**Final disposition:** retain as a high-value source and rival-hardening material. Use to strengthen SRT's subtraction discipline and empirical decomposition; do not cite persistence, learned inattention, engagement, attention gating or recovery-nonidentity as uniquely SRT phenomena.
