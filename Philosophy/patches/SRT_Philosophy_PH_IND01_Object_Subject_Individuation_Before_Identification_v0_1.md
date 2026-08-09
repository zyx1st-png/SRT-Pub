---
patch_id: PATCH-PHIL-PH-IND01-OBJECT-SUBJECT-INDIVIDUATION-BEFORE-IDENTIFICATION
source_ids:
  - SRC-2026-08-08-COGNITION-KIBBE-LESLIE-MINIMAL-OBJECT-REPRESENTATIONS-REBUILT
domain: philosophy_of_mind_cognition_individuation_subjecthood
claim_level: P3_bridge_analogy
canonical_status: non_canonical
status: active
target_future_doc:
  - Core_Law/SRT_Individuation.md
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
  - Philosophy/SRT_HardProblem_Epistemology.md
  - Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md
related_claims:
  - object_individuation_before_identification
  - subject_individuation_before_self_identification
  - self_model_vs_subject_position
  - stable_ISP
  - self_consciousness_second_transition
  - consequence_return
  - bearer_continuity
  - object_tracking_negative_control
tags:
  - individuation
  - object_index
  - infant_cognition
  - subjecthood
  - self_model
  - stable_ISP
  - consequence_return
layer: operations
epistemic_layer: bridge
claim_mode: hardening
canonical: false
type: theory_hardening_patch
id: PATCH-PHIL-PH-IND01-OBJECT-SUBJECT-INDIVIDUATION-BEFORE-IDENTIFICATION
---

# SRT Philosophy Patch PH-IND01: Object / Subject Individuation Before Identification v0.1

> **Status:** P3 philosophy-of-mind / cognition bridge and analogy.  
> **Canonical caution:** this patch does not define objecthood, subjecthood, consciousness, Stable ISP, self-consciousness, `d`, `Psi_f`, or consequence return. It uses a source-backed object-cognition distinction to sharpen an already-existing SRT individuation distinction. It does not transfer infant object evidence into evidence for consciousness.

---

## 0. Why this patch exists

Kibbe and Leslie’s object-index architecture supports a narrow but strong cognitive claim:

```text
object individuation can precede object identification
```

A system can preserve something like:

```text
"this one"
"still this one"
```

without simultaneously preserving a rich answer to:

```text
"what is this one?"
```

SRT independently contains a structurally similar distinction in `Core_Law/SRT_Individuation.md`:

```text
subject-position entry
precedes
reflective self-consciousness / self-objectification
```

The value of the comparison is not to claim that object indexing causes subjecthood. The value is to prevent a common starting-point error:

> a thing need not already possess a rich model of what it is in order to be individuated as a continuing unit.

For objects, the source directly supports this claim at the representational level. For subjects, SRT must establish the corresponding claim through its own bearer, history, consequence-return and Stable-ISP structure.

---

## 1. Evidence boundary

### 1.1 What Kibbe–Leslie directly supports

Source-backed:

```text
bare object index
-> persistent object individuation / tracking
-> optional category/property binding
-> richer identification
```

The paper supports the possibility that “which one / this one” is maintained without a complete “what is it” description.

### 1.2 What the source does not support

Not source-backed:

```text
selection creates objects
object index = SRT selection event
object index = bearer
object index = subjecthood
object index = consciousness
object individuation -> subject individuation
subject position -> phenomenality
```

These must not be inferred from the infant data.

### 1.3 Why the old PR #686 needed replacement

The closed PR correctly stated that only object-index continuity had direct source support, but one SourceCard passage allowed the first SRT extension—`selective convergence -> this one`—to appear partly source-supported.

PH-IND01 removes that ambiguity completely:

```text
Kibbe–Leslie evidence stops at object-level individuation / optional binding.
Everything beyond that is SRT-side interpretation or analogy.
```

---

## 2. The first distinction: `which one?` before `what is it?`

The source motivates two separable representational questions.

### Question O1 — individuation

```text
Which one is being tracked?
Is it still the same tracked individual?
```

### Question O2 — identification

```text
What kind of thing is it?
What properties does it have?
How should it behave?
```

The key ordering possibility is:

```text
O1 can be available before O2 is rich or stable.
```

Compact formulation:

```text
THIS-ONE
precedes or survives without
WHAT-IT-IS
```

This is the source-backed side of the patch.

---

## 3. The SRT comparison: `from here / this bearer` before `who I am`

SRT’s individuation theory already distinguishes:

```text
subject-position entry
from
reflective self-consciousness
```

A subject-position candidate can therefore be analyzed using two different questions.

### Question S1 — bearer / perspective individuation

```text
From which continuing position are consequences borne?
Which continuing process carries history forward?
Where do consequences return and rewrite future selectability?
```

### Question S2 — self-identification

```text
Who am I?
What kind of agent am I?
What properties, roles, memories and narratives describe me?
Can I represent myself as the selector / bearer?
```

PH-IND01 proposes the following P3 structural analogy:

```text
OBJECT
this one
-> still this one
-> what this one is

SUBJECT (SRT hypothesis)
this bearer / from here
-> still this bearer across history and consequence
-> who I am / reflective self-model
```

The analogy is intentionally asymmetric in evidence:

```text
object side = source-backed cognitive architecture
subject side = SRT theory hypothesis constrained by existing individuation files
```

---

## 4. Main bridge claim

### Claim PH-IND01-A — individuation need not wait for descriptive self-identification

A continuing unit may be individuated by persistence relations before it is richly identified by descriptive content.

For objects, relevant persistence relations can include tracking through space/time and occlusion.

For an SRT subject candidate, the relevant relations must be stronger and different:

```text
same-bearer consequence return
+ history-bearing writeback
+ stake-coupled continuity
+ reselection / future-selectability change
+ boundary maintenance
```

Therefore the safe cross-domain principle is:

> **Individuation and identification are distinct problems. The criteria that individuate an object need not be the criteria that individuate a subject, but neither problem should begin by assuming that a rich descriptive identity is already available.**

This claim is bridge-level, not canonical.

---

## 5. Why `self-model != subject` becomes sharper

Many consciousness and AI accounts begin with a self-model, body model, attention schema, autobiographical representation or higher-order representation.

PH-IND01 forces a prior question:

> What is the unit that the self-model is a model **of**?

There are at least two possible architectures.

### Architecture A — model identifies an already-individuated bearer

```text
bearer continuity exists
-> system builds increasingly rich model of that bearer
-> reflective self-identification emerges
```

This is compatible with current SRT individuation.

### Architecture B — model is supposed to create the bearer

```text
self-model appears
-> bearer is inferred from the model
```

This requires an additional argument. A representation referring to “self” does not by itself establish the existence of the same-bearer consequence-return structure that SRT uses to distinguish subject-position from representation.

Therefore:

```text
self-description
!= self-individuation

representation of a bearer
!= bearer continuity
```

---

## 6. Object tracking as a negative control for subjecthood

The source is especially useful because object indexing gives SRT a strong negative control.

A cognitive system can:

- deploy multiple object indices;
- maintain object continuity through occlusion;
- bind category and property information;
- reidentify tracked items;

without any tracked object thereby becoming the bearer of the indexing system’s consequences.

Hence:

```text
tracked individual
!= consequence bearer
```

and:

```text
object continuity
!= first-person continuity
```

This prevents a weak subjecthood criterion such as:

```text
persistent representation
-> subjecthood
```

A stronger SRT subjecthood audit must still ask:

```text
Where does cost close?
Whose own future possibilities change?
Which history is written back into the same continuing process?
Can the relevant loss be externally absorbed or transferred?
```

---

## 7. Two boundaries that must not be confused

### 7.1 Tracking boundary

The tracking boundary answers:

```text
Which item remains the same item for this cognitive process?
```

It is established by whatever representation/tracking architecture maintains object individuation.

### 7.2 Consequence-return boundary

The consequence-return boundary answers:

```text
Which continuing process must carry the result of this event into its own later state and selection space?
```

This boundary is central to SRT subjecthood work.

Compact guardrail:

```text
tracking boundary
!= consequence-return boundary
```

The distinction should be preserved in any future work connecting object files, object permanence, self-models, body models, Markov blankets or attention schemas to subjecthood.

---

## 8. A three-stage comparison without evidence transfer

### Object side

```text
O0: no stable object index
O1: thin tracked individual — "this one"
O2: enriched identified object — "what this is"
```

### Subject side — SRT bridge hypothesis

```text
S0: no stable bearer position
S1: pre-reflective bearer position — "from here / this bearer"
S2: self-identified bearer — "who I am"
```

The comparison does **not** assert that O1 and S1 share the same mechanism.

It asserts only a methodological discipline:

> do not define the thinner individuation stage using capacities that belong to the later identification stage.

This matters because requiring a narrative self, explicit self-recognition or higher-order self-description as the starting condition for subjecthood risks making the subject too thick from the beginning.

---

## 9. Developmental caution

`SRT_Individuation.md` uses infancy/early childhood as an illustrative example of a subject-position phase without rich self-objectification.

PH-IND01 does not independently validate that developmental claim.

Kibbe–Leslie studies object representation, not infant phenomenal consciousness, moral status, selfhood or bearer continuity.

Therefore do not infer:

```text
infant object index
-> infant subjecthood proved

object permanence
-> first-person continuity proved

preverbal cognition
-> Stable ISP proved
```

The source only makes it conceptually less plausible to insist that rich descriptive self-knowledge must be logically prior to every form of individuation.

---

## 10. Relation to the hard problem

This patch primarily concerns **subject individuation**, not phenomenal necessity.

It can help sharpen one part of the consciousness problem:

```text
How can there be a stable "for-this-bearer" position before a reflective model of "who I am"?
```

It does not answer:

```text
Why is that bearer phenomenally conscious?
Why is there something it is like?
```

Thus:

```text
subject individuation before self-identification
!= phenomenal consciousness derived
```

Any future use with hard-problem work must preserve that separation.

---

## 11. Relation to PH-CONSC03 and current subjecthood work

`PH-CONSC03` separates:

```text
Selector != Bearer != Concern Domain != Experiencer
```

PH-IND01 adds a timing/order guard:

```text
Bearer individuation
need not be identical to
Bearer self-identification
```

Together they suggest a cleaner sequence for SRT subjecthood analysis:

```text
candidate continuing unit
-> bearer / consequence-return individuation
-> history-bearing continuity
-> subject-position candidate
-> self-model / self-identification may thicken later
-> experiencer / phenomenality remains separately assessed
```

This sequence is a bridge architecture, not a new canonical theorem.

---

## 12. Experimental / operational consequences

PH-IND01 suggests several differential questions for future empirical or AI work.

### 12.1 Self-model ablation

If a system has persistent same-bearer consequence return and history continuity, what happens when explicit self-description or autobiographical self-modeling is reduced?

A model-first account may predict collapse of subject-like organization; a bearer-first account predicts that some pre-reflective continuity can remain.

This is not yet a consciousness experiment. It is a subject-architecture dissociation test.

### 12.2 Tracking-versus-bearing dissociation

Construct systems with very strong persistent object tracking but no same-system consequence return.

Prediction:

```text
high object-index competence
should not by itself satisfy SRT subjecthood gates
```

### 12.3 Copy / replacement pressure

A self-model can be copied verbatim across instances. If the bearer relation is path-specific, copied descriptive identity need not imply copied bearer continuity.

This offers a future AI test of:

```text
same self-description
vs
same continuing bearer
```

---

## 13. Boundary cautions

Do not write:

```text
Kibbe–Leslie proves SRT individuation.
Infants prove subject-before-self-model.
Object index is a minimal subject.
Object index is a Stable ISP.
"this one" = "I".
Object tracking proves consciousness.
Self-model is irrelevant to consciousness.
Self-model always comes after subjecthood in every possible architecture.
```

Allowed:

```text
Kibbe–Leslie supports object individuation before rich identification.
SRT independently hypothesizes subject-position entry before reflective self-identification.
The two structures are usefully comparable if evidence is not transferred across them.
Object tracking is a negative control for bearer continuity.
```

---

## 14. Integration hook

Future de-materialized synthesis can absorb the following sentence:

> **A subject need not begin as a theory of itself. The first problem is whether a continuing bearer-position has become individuated by consequence return, history and reselection; only later need that position become an explicit object of its own modeling.**

This is an SRT bridge sentence. It should never be attributed to Kibbe–Leslie.

Suggested future targets:

```text
Core_Law/SRT_Individuation.md
Philosophy/SRT_Subjecthood_Threshold_Interface.md
Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md
```

No owner/canonical file is modified in this patch.

---

## 15. One-paragraph abstract

Kibbe and Leslie’s infant object-index architecture supports a narrow cognitive distinction: a minimal tracked “this one” can be maintained before or without a rich representation of “what this one is.” PH-IND01 uses this as a negative control and structural analogy for SRT individuation, not as evidence transfer. SRT already distinguishes subject-position entry from later reflective self-consciousness; the comparison therefore sharpens the question whether a bearer can be individuated by consequence return, history and future-selectability rewrite before it is richly self-identified by a narrative or reflective self-model. The patch preserves the crucial asymmetry: object individuation is source-backed, whereas subject individuation before self-identification remains an SRT P3 hypothesis. Its main hardening result is that tracking continuity, descriptive identity, bearer continuity and phenomenality must remain separate tests.
