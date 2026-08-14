---
patch_id: PATCH-PHIL-PH-PER01-PERCEPTUAL-LEARNING-SALIENCE-RESELECTABILITY
id: PATCH-PHIL-PH-PER01-PERCEPTUAL-LEARNING-SALIENCE-RESELECTABILITY
source_ids:
  - SRC-2026-08-14-PHIL-NAGASE-MCDOWELL-PERCEPTUAL-LEARNING
domain: philosophy_perception_agency_reselectability
claim_level: P3_bridge_hardening
canonical_status: non_canonical
status: active
target_future_doc:
  - Philosophy/SRT_Phenomenal_Structure_Interface.md
  - Philosophy/SRT_Social_Cognition.md
  - Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md
related_claims:
  - perceptual_learning
  - salience_restructuring
  - candidate_field_shaping
  - affordance_invitation_gating
  - L2_downward_constraint
  - historical_writeback
  - reselectability
  - constraint_objectification
  - responsibility_position_trace
  - language
  - agency
  - subjecthood_guardrails
tags:
  - perception
  - perceptual_learning
  - salience
  - affordance
  - language
  - normativity
  - agency
  - responsibility
  - reselectability
layer: operations
epistemic_layer: bridge
claim_mode: hardening
canonical: false
type: theory_hardening_patch
---

# SRT Philosophy Patch PH-PER01: Perceptual Learning / Salience / Constraint Reselection v0.1

> **Status:** bounded P3 philosophy/perception bridge and hardening note.  
> **Canonical caution:** this patch does not define `L_2`, `d-value`, `Psi_f`, `G_hat_theta`, subjecthood, agency, responsibility or second-order selection. It adds a mechanism-oriented bridge between historical learning, perceptual organization, later candidate accessibility and constraint reselectability.

---

## 0. Source anchor

Primary source:

```text
Daniel Arvage Nagase
The Intimate Harmony Between the Intellect and Sensibility:
McDowell and Perceptual Learning
Principia 30(2): 279–305 (2026)
DOI 10.5007/1808-1711.2026.e103531
```

SourceCard:

```text
Materials/2026/SRC_2026_08_14_Phil_Nagase_McDowell_Perceptual_Learning.md
```

The source is a peer-reviewed philosophy article. It offers a reconstruction of McDowell with selected empirical examples but does not establish a new neural mechanism or test SRT directly.

---

## 1. Why this matters for SRT — and what is already covered

Current SRT already contains several neighboring claims, so PH-PER01 must not present them as new.

### Existing coverage A — PH-AG02 already has learned structuring bias

`PH-AG02 Knowledge-biased selection` already distinguishes triggering causes from learned structuring biases and allows learned knowledge to organize attention and input-output coupling without becoming an explicit premise at each use.

Therefore this generic claim is **not** the PH-PER01 increment:

```text
learning / knowledge
-> attention bias
-> different response accessibility
```

PH-PER01 instead asks whether learning can alter the organization of the salience/discrimination field itself, rather than merely add another bias term over a fixed field.

### Existing coverage B — SOC-COG03 already has constraint revision

`SOC-COG03` already supplies:

```text
Visibility
-> Contestability
-> Alternative generation
-> Enactability
-> Historical writeback
```

and explicitly routes stronger second-order-selection claims through existing H3/I5/J5 conditions.

Therefore PH-PER01 does **not** add a second social-reselection pathway. Nagase's language discussion is treated only as one possible trigger by which a previously transparent constraint enters the already existing SOC-COG03 revision pathway.

### Existing coverage C — T-Cog-5 already adds history and salience in attention priority

Current `Philosophy/SRT_Social_Cognition.md` states:

```text
Pi(T_i)
= w_td * I_intent
+ w_bu * S_salience
+ w_hist * H_value
```

This additive form already represents top-down intention, bottom-up salience and historical value/habit as contributors to attention priority.

### Stable PH-PER01 delta — reweighting versus reparameterization

Nagase's useful pressure is narrower and more discriminating:

```text
HISTORICAL REWEIGHTING:
fixed salience / grouping structure
+ changed weights or priorities
-> different selected target

versus

HISTORY-CONDITIONED REPARAMETERIZATION:
training history
-> changed grouping / discrimination boundaries / salience organization
-> a changed S_salience landscape itself
-> different later target / candidate accessibility
```

The second pattern is the genuine PH-PER01 increment. The claim is **not** that Nagase proves T-Cog-5 false or that `S_salience` must be mathematically redefined now. It registers a P3/P4 pressure: an additive priority map may need a history-conditioned salience term or upstream perceptual-organization map when data show that training changes the feature partition / discrimination geometry itself rather than only the final priority weight.

Compact distinction:

```text
history as one additive input to priority
!=
history changing the salience function / grouping structure that priority operates on
```

This is the main reason to retain PH-PER01 rather than absorb it entirely into PH-AG02 or SOC-COG03.

---

## 2. Main bridge claim A — perceptual learning can reshape the salience landscape

Nagase's radiologist case supports the claim that expert learning can change which regions are grouped together and which traces become perceptually salient.

Bounded SRT bridge:

```text
historical learning
+ task / goal structure
-> altered grouping / salience organization
-> altered perceptual discrimination
```

At P3, this suggests one possible implementation route for history-conditioned manifestation:

```text
L2-relevant history
-> changed constraint on later perceptual organization
-> changed constraint on which L1 manifestations / discriminations become available
```

Do **not** call the learned salience/discrimination profile itself "L1-level". `L_1` is the manifest selected actuality; the learned profile belongs on the constraint/organization side of the bridge.

The following identities are blocked:

```text
concept = L2
perceptual learning = L2
salience = d-value
expertise = G_hat_theta
```

The paper does not identify a low-level SRT operator and does not settle where, neurally or computationally, the reorganization occurs.

---

## 3. Main bridge claim B — candidate-field shaping can precede final choice

Nagase's virtue discussion is structurally compatible with the existing SRT invitation-gating distinction.

The relevant difference is not always:

```text
same live options
+ different final weights
```

It can instead be:

```text
historically shaped perception / norm sensitivity
-> different action opportunities become salient
-> different live invitation field
-> later action selection
```

This does not imply that a physically possible action literally ceases to exist. It means the action may fail to enter the current field as a practically salient invitation.

### Crosswalk to PH-AG02

Use PH-AG02 for the broad claim that learned knowledge can function as an action-organizing bias. Use PH-PER01 only when the proposed effect is stronger:

```text
PH-AG02 neighboring case:
learned structure biases attention / coupling over a field

PH-PER01 delta candidate:
learning changes grouping / discrimination / S_salience organization of the field itself
```

This boundary prevents the new patch from relabeling existing knowledge-bias content as novelty.

### Crosswalk to SOC-COG03

PH-PER01 should not create a second affordance theory. Use it as a perceptual-learning companion to:

```text
Philosophy/patches/SRT_Philosophy_SOC_COG03_Norm_Script_Affordance_Meta_Selectability_v0_1.md
```

SOC-COG03 supplies role/script/history-sensitive social invitation gating; PH-PER01 supplies a complementary philosophical route through learned grouping, salience and perceptual organization.

---

## 4. Main bridge claim C — linguistic articulation as one SOC-COG03 revision trigger

The source gives language a role stronger than simple storage or report. Stable labels can de-contextualize patterns, make higher-order relations available and bring patterns into joint attention and criticism.

Do not encode this as a second pathway parallel to SOC-COG03. The safer relation is:

```text
transparent learned constraint
-> linguistic articulation / naming
-> de-contextualization / joint attention
-> Visibility
-> Contestability
-> Alternative generation
-> Enactability
-> Historical writeback
```

Here the last five stages are inherited from `SOC-COG03`; linguistic articulation is merely one candidate **entry trigger** into that existing pathway.

Compact claim:

> Language can provide one route by which a structure that previously shaped selection from the background becomes visible and jointly inspectable; whether this visibility becomes durable reselection remains governed by the existing SOC-COG03 / H3-I5-J5 architecture.

### Inherited stronger conditions

If a linguistic challenge is later described as second-order selection, PH-PER01 inherits the same stricter I5 requirements already used by SOC-COG03:

```text
same historical bearing-position consequence return
+ comparison-scale or generation-rule rewrite
+ changed future selectable space
+ persistent later efficacy
```

J5 then classifies reopening depth rather than assuming every revision is R3:

```text
R1-like: weight / priority change
R2-like: category or role-boundary change
R3-like: candidate-generation mechanism change
R4-like: concern-boundary change
```

Thus:

```text
linguistic objectification
!= successful revision
!= historical writeback
!= I5-qualified second-order selection
!= J5 R3 by default
```

### Guard against language exceptionalism

```text
language may thicken constraint objectification
!= language is necessary for subjecthood
!= language is sufficient for agency
!= language is sufficient for responsibility
```

Non-linguistic animals can still possess organized perception, concern, memory and degrees of agency; stronger responsibility claims remain separately gated.

---

## 5. Main bridge claim D — interpersonal footprint as a third responsibility-position thickening route

Nagase's conclusion treats shared life as a web in which actions and attitudes leave interpersonal "footprints". Conversation allows people to negotiate how those footprints are understood and how reactions should be calibrated.

SRT compression:

```text
action
-> consequence / effect on another bearer or relationship
-> interpersonal interpretation
-> possible correction / contestation
-> identification / endorsement
-> answerability / repair pathway
```

This can enrich the non-canonical `responsibility-position trace` architecture in:

```text
Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md
```

but it must be cross-read with two already existing routes rather than treated as a standalone third theory:

```text
PH-AG03:
commitment under incomplete guarantee
-> responsibility-position trace

PH-AG05 / PH-AG05A:
embodied / relational / collective position maintenance
-> M_rel / position effects among concrete others
-> possible reselection or capture consequences

PH-PER01:
interpersonal footprint
-> jointly interpreted impact / correction / identification
-> possible thickening of an already traceable responsibility position
```

The PH-PER01 contribution is specifically the **joint construal / correction of interpersonal impact**, not the creation of responsibility from social interpretation alone.

The following identity is blocked:

```text
interpersonal footprint = responsibility-position trace = S6 responsibility
```

A footprint is at most candidate material for a later responsibility relation. S6 still requires norm access, consequence understanding, selectable alternatives, revision/inhibition and repair/answerability conditions.

---

## 6. New hardening distinction — integration is not reselectability

Nagase treats systematic rationality largely as a matter of how well capacities are integrated. This is a useful description of flexible cross-capacity coordination but it should not be imported into SRT as a one-dimensional measure of rational freedom.

SRT must preserve:

```text
systematic integration
!=
reselectability
```

A system can be:

```text
highly integrated
+ internally coherent
+ behaviorally fluent
```

while still being:

```text
low in constraint inspectability
+ low in contestability
+ low in policy / generation-rule reopening
```

This gives a two-axis diagnostic:

| Axis | Question |
|---|---|
| integration | How extensively can capacities / cues / policies coordinate and improve one another? |
| reselectability | Can the structures shaping the live field themselves be inspected, inhibited, contested, revised or reopened? |

The distinction protects SRT from equating coherence with freedom.

---

## 7. Relation to `d-value` and "what matters"

Nagase's conclusion moves from reason-giving to shared ethical significance and the ability to "say what matters" and "have a say in what matters".

This is relevant to socially structured concern, but it does not define canonical `d-value`.

Required guard:

```text
social / ethical significance
!= d-value
```

Safer SRT ordering:

```text
bearer-level stake / concern
-> socially and linguistically structured significance
-> normative salience / interpersonal meaning
```

The source can therefore help explain how concern becomes socially articulated and negotiated without being used to derive the existence of stake from language or social norms.

---

## 8. Empirical caution — radiology is a strong example, not a settled cognitive-penetration result

The expert-radiologist case is useful because rapid lesion discrimination and altered grouping/salience resist a simple "same perception, then slow explicit inference" picture.

However:

```text
expertise-dependent perceptual organization
!= settled proof of early cognitive penetration
```

The exact boundary among early sensory processing, attention, learned perceptual organization and very rapid post-perceptual processing remains an empirical issue outside what this philosophy paper alone can settle.

SRT should therefore use the case as a **mechanism-neighbor and differential-test prompt**, not as proof of a specific neural stage.

---

## 9. Compact cross-theory chain

The source-backed and SRT-extended layers should be kept separate:

```text
SOURCE-BACKED:
learning / conceptual training
-> grouping + salience reorganization
-> altered perceptual discrimination
-> altered perception of action opportunities
-> language-enabled de-contextualization / shared reflection
-> interpersonal interpretation / responsibility discourse

SRT P3 BRIDGE:
historical constraint
-> possible S_salience / grouping reparameterization
-> future invitation-field shaping
-> live candidate-field difference
-> possible linguistic entry into existing SOC-COG03 revision pathway
-> possible responsibility-position thickening
```

The second block is an SRT bridge, not Nagase's terminology.

---

## 10. Compact guards

```text
concept != L2
perceptual learning != L2
salience != d-value
goal relevance != d-value
what matters socially != d-value
systematic integration != reselectability
language != subjecthood
language != agency
language != responsibility
linguistic objectification != I5-qualified second-order selection
interpersonal footprint != responsibility-position trace != S6 responsibility
rapid expert discrimination != proof of early cognitive penetration
source argument != evidence for canonical G_hat_theta / Psi_f / d / L2 identities
```

---

## 11. Differential tests — make the delta adjudicable

The strongest P4 use of PH-PER01 is to distinguish **priority reweighting** from **salience / grouping reparameterization** under matched current input.

### P4-A — T-Cog-5 reweighting versus reparameterization

Use the current T-Cog-5 priority form as the null architecture:

```text
Pi(T_i)
= w_td * I_intent
+ w_bu * S_salience
+ w_hist * H_value
```

Compare two model families under the same current stimulus and task:

```text
MODEL R — reweighting only:
S_salience feature map / grouping held fixed
history changes w_hist, w_td, or final priority weights

MODEL P — reparameterization:
training history changes feature grouping, discrimination boundary,
or the mapping that produces S_salience before final priority selection
```

Candidate discriminators:

- same physical stimulus, different training history;
- early grouping / segmentation or discrimination-boundary differences;
- transfer to novel exemplars not explainable by a learned final-response weight alone;
- altered salience structure persisting when explicit task instruction and reward are matched;
- model comparison asking whether history-conditioned `S_salience` / grouping predicts behavior beyond additive `H_value` reweighting.

Failure / downgrade condition:

> If matched-input expertise effects are fully explained by changed additive weights over an unchanged feature/salience representation, PH-PER01's distinct delta should be downgraded toward PH-AG02 rather than retained as a separate reparameterization bridge.

### P4-B — reselectability under matched competence

```text
matched current task competence
+ matched broad option availability
+ different constraint inspectability / contestability
-> different reselectability under perturbation
```

### P4-C — linguistic trigger into existing revision pathway

```text
constraint remains behaviorally effective
+ linguistic articulation increases Visibility / Contestability
-> test Alternative generation / Enactability / Historical writeback
```

A momentary verbalization effect alone is insufficient. Durable claims must retain SOC-COG03's later-stage and I5/J5 gates.

These are P4-oriented research prompts only; the source itself does not provide these tests.

---

## 12. Integration targets

### Target A — Phenomenal Structure Interface

Potential future insertion:

```text
The owner already uses concern-weighted salience for stake-gated phenomenal structure. PH-PER01 adds a distinct history/training-weighted route: learning may alter grouping and perceptual salience organization before explicit report or final action selection. Keep history/training-weighted salience distinct from concern-weighted salience and from canonical d-value; the former can modify which L1 manifestations/discriminations become available without by itself establishing bearer-level stake.
```

### Target B — Social Cognition

Potential future insertion near T-Cog-5 / invitation gating:

```text
Role/script-sensitive invitation gating can be complemented by a perceptual-learning pressure on the current additive priority form: history may not only contribute through H_value but may also change the grouping / S_salience map on which priority selection operates. Treat this as a reweighting-versus-reparameterization test, not an immediate rewrite of T-Cog-5.
```

### Target C — Agency / Subjecthood

Potential future insertion:

```text
Language can thicken agency by serving as one trigger into the existing constraint-visibility / contestability pathway, and interpersonal footprint discussion can thicken responsibility-position traces through joint construal, correction and repair. Cross-read this with PH-AG03 commitment and PH-AG05/05A relational position; these are S5/S6-supporting routes, not subjecthood criteria by themselves.
```

No target should be rewritten from this single source without a later synthesis pass.
