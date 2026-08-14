---
hook_id: HOOK-PHIL-PH-PER01-PERCEPTUAL-LEARNING-SALIENCE-RESELECTABILITY
patch_id: PATCH-PHIL-PH-PER01-PERCEPTUAL-LEARNING-SALIENCE-RESELECTABILITY
domain: philosophy_perception_agency_reselectability
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: integration_hook
id: HOOK-PHIL-PH-PER01-PERCEPTUAL-LEARNING-SALIENCE-RESELECTABILITY
status: active
integration_status: pending
landing_ledger:
  - target: "Philosophy/SRT_Phenomenal_Structure_Interface.md"
    state: pending
    blocked_by: "single-source owner rewrite deferred; compare history/training-weighted salience with the owner's existing concern-weighted salience and current neuroscience salience/objectification bridges before landing"
  - target: "Philosophy/SRT_Social_Cognition.md"
    state: pending
    blocked_by: "requires a synthesis pass with T-Cog-5, PH-AG02 and SOC-COG03 so reweighting, salience reparameterization and existing H3/I5/J5 revision gates remain distinct"
  - target: "Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md"
    state: pending
    blocked_by: "retain S4/S5/S6 boundary and crosswalk interpersonal footprint with PH-AG03 responsibility-position trace plus PH-AG05/05A relational-position routes before owner-level landing"
closure_audit: Operations/Audits/Hook_Closure_Audit_2026-07-25.md
---

# Integration Hook: PH-PER01 Perceptual Learning / Salience / Reselectability

## 1. Primary source

```text
Materials/2026/SRC_2026_08_14_Phil_Nagase_McDowell_Perceptual_Learning.md
```

Patch:

```text
Philosophy/patches/SRT_Philosophy_PH_PER01_Perceptual_Learning_Salience_Reselectability_v0_1.md
```

## 2. Novelty boundary before landing

PH-PER01 must be read against existing coverage before any owner edit.

```text
PH-AG02 already covers:
learned knowledge as structural bias over attention / input-output coupling

SOC-COG03 already covers:
Visibility -> Contestability -> Alternative generation -> Enactability -> Historical writeback
with stronger H3/I5/J5 gates

T-Cog-5 already covers:
Pi(T_i) = w_td * I_intent + w_bu * S_salience + w_hist * H_value
```

The distinct PH-PER01 pressure is therefore:

```text
history as an additive priority input
!=
history changing the grouping / discrimination / S_salience map itself
```

Use the shorthand **reweighting versus reparameterization**. Do not present generic history-to-attention bias or generic constraint revision as new.

## 3. Target A — Phenomenal Structure Interface

Preferred neighborhood:

```text
stake-gated phenomenal structure / concern-weighted salience / future selectability
```

Suggested bounded paragraph:

The owner already uses **concern-weighted salience** as part of stake-gated phenomenal structure. PH-PER01 adds a separate **history/training-weighted** route: perceptual learning may change how later features are grouped and which become salient before explicit report or final action selection. In SRT this can be treated as one candidate constraint on which `L_1` manifestations or discriminations become available. History/training-weighted salience must remain distinct from concern-weighted salience and from canonical `d-value`; task/expertise effects do not independently establish bearer-level stake.

Do not insert until a synthesis pass can compare this route with current neuroscience salience / memory / objectification bridges.

## 4. Target B — Social Cognition

Preferred neighborhood:

```text
T-Cog-5 Attention as Priority-Guided Selection
Ax-Cog-2b Invitation Gating
SOC-COG03 Norm / Script / Affordance / Constraint Reselection
PH-AG02 Knowledge-biased Selection
```

Suggested bounded paragraph:

Current T-Cog-5 treats intention, bottom-up salience and history/value as additive contributors to priority. Nagase's perceptual-learning argument raises a narrower P3/P4 pressure: training history may sometimes change the feature grouping or the mapping that generates `S_salience`, rather than merely changing `w_hist` or another final priority weight. This is a reweighting-versus-reparameterization test, not an immediate theorem rewrite.

Compact crosswalk:

```text
PH-AG02:
learned structure -> attention / coupling bias

PH-PER01 delta:
learning -> grouping / discrimination / S_salience reparameterization candidate

SOC-COG03:
role + script + history -> social invitation gating
```

## 5. Language route — trigger, not a parallel pathway

Do not preserve the old PH-PER01 chain as a second revision architecture. Route it into SOC-COG03:

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

The last five stages are inherited from SOC-COG03.

If stronger second-order-selection language is used, retain the existing I5 conditions:

```text
same historical bearing-position consequence return
+ comparison-scale or generation-rule rewrite
+ changed future selectable space
+ persistent later efficacy
```

and J5 reopening depth:

```text
R1 weight / priority
R2 category / boundary
R3 candidate-generation mechanism
R4 concern boundary
```

Required guards:

```text
linguistic objectification != successful revision
linguistic objectification != historical writeback
linguistic objectification != I5-qualified second-order selection
linguistic objectification != J5 R3 by default
```

## 6. Target C — Agency / Subjecthood

Preferred neighborhood:

```text
S5 reflective self-integration / policy revision
S6 norm access / answerability / repair
responsibility-position trace
PH-AG03 constitutive commitment
PH-AG05 / PH-AG05A embodied-relational position
```

Suggested bounded paragraph:

Language can thicken agency without defining subjecthood by making some background constraints jointly visible and contestable. Nagase's interpersonal-footprint discussion can also thicken responsibility-position formation through joint construal, correction, identification and repair. This should be treated as a third **thickening route** beside PH-AG03's commitment route and PH-AG05/05A's embodied/relational-position route, not as a new independent definition of responsibility.

Crosswalk:

```text
PH-AG03:
commitment -> traceable answerable position

PH-AG05 / PH-AG05A:
M_rel / embodied social position -> relational maintenance or capture

PH-PER01:
interpersonal footprint -> joint construal / correction / identification
-> possible thickening of an already traceable responsibility position
```

Do not collapse:

```text
interpersonal footprint != responsibility-position trace != S6 responsibility
```

Language is neither necessary for S4 subjecthood nor sufficient for S5 agency or S6 responsibility.

## 7. Two-axis hardening to preserve

Any future synthesis should keep these axes separate:

| Axis | Diagnostic |
|---|---|
| systematic integration | Can capacities / cues / policies coordinate and improve one another? |
| reselectability | Can the constraints shaping the live field be inspected, inhibited, contested, revised or reopened? |

Required non-identity:

```text
systematic integration != reselectability
```

A highly coherent and fluent system may still be rigid at the level of constraint reopening.

## 8. P4 differential hook

Use T-Cog-5 as the null priority architecture and compare:

```text
MODEL R — reweighting:
fixed grouping / S_salience map
+ changed additive priority weights

MODEL P — reparameterization:
training history changes grouping / discrimination boundaries
or the mapping that produces S_salience before final priority selection
```

The PH-PER01 delta survives only if the history-conditioned reparameterization model explains matched-current-input behavior beyond additive `H_value` / priority-weight changes. If not, downgrade the distinct increment toward PH-AG02.

## 9. Compact guards

```text
concept != L2
perceptual learning != L2
salience != d-value
goal relevance != d-value
social "what matters" != d-value
history/training-weighted salience != concern-weighted salience
systematic integration != reselectability
language != subjecthood
language != agency
language != responsibility
interpersonal footprint != responsibility-position trace != S6 responsibility
rapid expertise effect != settled early cognitive penetration
```

## 10. Do not include

- Do not say Nagase or McDowell proves SRT.
- Do not import McDowellian conceptualism as a canonical SRT theory of perception.
- Do not convert conceptual capacity into `L_2` or perceptual salience into `d-value`.
- Do not call a learned salience/discrimination profile an `L_1` state; treat it as a constraint on later `L_1` manifestation/discrimination.
- Do not merge history/training-weighted salience with the owner's existing concern-weighted salience.
- Do not infer full agency or responsibility from language use.
- Do not deny non-linguistic subjecthood or agency merely because conversation is limited.
- Do not turn systematic integration into a scalar measure of freedom.
- Do not treat the radiologist example as settled neural evidence for early cognitive penetration.
- Do not open a new second-order-selection or meta-selectability mechanism parallel to the existing reselectability / H3-I5-J5 architecture.

## 11. Future synthesis question

The strongest SRT-specific question left by this source is:

> When learning has made a perceptual/action organization highly fluent and integrated, what keeps that organization reopenable by the same continuing bearer rather than turning coherence into rigid closure?
