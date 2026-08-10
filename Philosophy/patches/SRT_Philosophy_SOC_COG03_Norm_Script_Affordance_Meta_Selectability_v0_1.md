---
patch_id: PATCH-PHIL-SOC-COG03-NORM-SCRIPT-AFFORDANCE-META-SELECTABILITY
id: PATCH-PHIL-SOC-COG03-NORM-SCRIPT-AFFORDANCE-META-SELECTABILITY
source_ids:
  - SRC-2026-08-10-PHIL-BERIO-MUSHOLT-NORMS-SCRIPTS-AFFORDANCES
domain: philosophy_social_cognition
claim_level: P3_bridge_hardening
canonical_status: non_canonical
status: active
target_future_doc:
  - Philosophy/SRT_Social_Cognition.md
related_claims:
  - affordance
  - invitation_gating
  - role_indexed_selection
  - distributed_constraint
  - script_automation
  - L2_downward_constraint
  - real_choice_moment
  - reselectability
  - H3_comparison_scale_rewrite
  - I5_second_order_selection_gate
  - J5_layered_reopening
  - historical_writeback
tags:
  - social_cognition
  - affordance
  - scripts
  - social_norms
  - roles
  - skills
  - contestability
  - reselectability
  - second_order_selection
layer: operations
epistemic_layer: bridge
claim_mode: hardening
canonical: false
type: theory_hardening_patch
---

# SRT Philosophy Patch SOC-COG03: Norm / Script / Affordance / Constraint Reselection v0.1

> **Status:** bounded P3 social-cognition bridge and hardening note.  
> **Canonical caution:** this patch does not define `L_2`, affordance, `d-value`, `Psi_f`, `T_dir`, freedom or the Real Choice Moment. It does not create a second theory of second-order selection. The working phrase `meta-selectability` is retained only as a broad social-cognition diagnostic for constraint inspectability / contestability / revision and is explicitly routed into the repository's existing `reselectability` family and H3/I5/J5 source-intuition work.

---

## 0. Source anchor

Primary source:

- Leda Berio and Kristina Musholt, *Seeing What To Do: Norms, Scripts, and Social Affordances*, user-supplied preprint, forthcoming in *Philosophers' Imprint*.

SourceCard:

```text
Materials/2026/SRC_2026_08_10_Phil_Berio_Musholt_Norms_Scripts_Social_Affordances.md
```

Existing SRT source-intuition crosswalk:

```text
01_Source_Intuition/SRT_CHOICEMAP_EMBODIED_POSITION_SECOND_ORDER_SELECTION_CONTINUATION_2026-08-09.md
```

The source is a philosophical synthesis. It uses empirical affordance and norm-psychology literature but does not itself establish a new neural mechanism or experimental law.

---

## 1. Why this matters for SRT

Current SRT social cognition already distinguishes a broad affordance landscape from the smaller subset that becomes a current invitation field. P1 also states that sedimented `L_2` structures can constrain future selection and that script execution does not by itself constitute a Real Choice Moment.

Berio and Musholt add a useful missing middle:

```text
social role / position
+
active script
+
interaction history
->
which physically available actions become socially salient, soliciting, awkward, prohibited or practically invisible
```

The stable increment is therefore not the generic claim that norms influence behavior. It is that social constraints can shape the **effective candidate field before final action selection**, and that disruption can sometimes make a previously transparent generating constraint available for inspection and revision.

---

## 2. Main SRT bridge claim

### Claim SOC-COG03-A — role-indexed invitation gating

At P3, interpersonal affordance gating should be treated as role- and script-sensitive rather than as a context-free filter over a common action menu.

Local bridge form:

\[
\mathcal I_t^{social}
=
\Gamma_{soc}(C_t,\theta_t,\Pi_t;\rho_t,\mathcal S_t,\mathcal H_t)
\big(\mathcal A_{all}\big),
\qquad
\mathcal I_t^{social}\subseteq\mathcal A_{all}.
\]

where the added local placeholders are:

- `rho_t`: current social role / position;
- `S_t`: active script or script cluster;
- `H_t`: relevant learned / interaction history.

These are **domain-local bridge placeholders**, not new canonical SRT variables.

The subset condition matters. This equation represents **instantaneous invitation gating over a current affordance field**. It does not itself represent J5 R3-level rewriting of the future candidate-generation mechanism. A later R3-like restructuring can change what `A_all` / its generator looks like in subsequent rounds; that is a distinct higher-order historical effect.

Compact claim:

```text
norm / role effects
need not wait until after a fixed option set is presented;
they may participate in determining what enters the live invitation field.
```

---

## 3. Distributed constraint carrier

### Claim SOC-COG03-B — ask where the effective constraint is carried, not only where a representation is located

Berio and Musholt allow scripts to be partly internalized and partly public / socio-material. A script may be carried across:

```text
neural habit
+
body skill
+
language
+
spatial layout
+
public artifact
+
role expectation
+
other-agent response
```

SRT compression:

> A historically effective social constraint can be distributed across several carriers so long as their coupled organization reliably shapes future selection.

This is compatible with a local projection of P1 `L_2` downward constraint, but the following identity is blocked:

```text
script = L_2
```

The useful questions are:

```text
Which structures carry the constraint?
How does the constraint alter the current candidate field?
How is it maintained or rewritten across interaction history?
```

---

## 4. Supportive automation versus choice-replacing automation

### Claim SOC-COG03-C — automation must be judged by what it enables at the next relevant level

The source's skill discussion blocks a crude equation:

```text
automation = less freedom
```

A learned skill can sediment low-level routines and thereby release attention / control capacity for higher-level variation, novelty and response.

SRT therefore needs a two-sided reading:

```text
supportive automation
=
reliable lower-level script
-> reduces routine burden
-> preserves or expands higher-level live selectability
```

versus:

```text
choice-replacing automation
=
scripted constraint
-> narrows or preempts the relevant live candidate field
-> blocks revision / contestation
-> future selectability at that level contracts
```

P1-T05 remains intact: script execution does not **by itself** count as a Real Choice Moment. This patch only blocks the invalid converse that all script execution is globally anti-choice.

---

## 5. Constraint reselection: relation to H3 / I5 / J5

### Claim SOC-COG03-D — a constraint can become an object of revision without yet qualifying as second-order selection

The source's bidirectional norm architecture supports a social-cognition pathway:

```text
explicit avowal
-> implementation conditions
-> repeated enactment
-> implicit script
```

and, in the other direction:

```text
implicit script
-> disruption / spotlighting
-> constraint becomes explicitly inspectable
-> possible contestation / revision
-> alternative enactment
-> possible new sedimentation
```

This motivates a broad P3 diagnostic phrase:

> **`meta-selectability` = the capacity for constraints that shape what becomes selectable to become inspectable, contestable and revisable.**

The phrase is intentionally **broader and weaker** than the author-confirmed 2026-08-09 I5 second-order-selection candidate. It is not an independent mechanism and should be read as a social-domain entry condition within the existing `reselectability` family.

### 5.1 H3 relation — what is rewritten?

H3 requires more than a changed action weight. History must alter which differences can become salient / comparable and the scale by which they are classified.

Therefore:

```text
constraint becomes explicit
!=
comparison-scale rewrite
```

A social script can become visible and criticizable without yet changing the distinctions by which future alternatives are generated or compared.

### 5.2 I5 relation — what licenses second-order-selection language?

I5 currently requires four non-substitutable conditions:

1. **same historical bearing position's consequence return**;
2. **comparison-scale / generation-rule rewrite** rather than mere weight change;
3. **future selectable-space change**;
4. **persistent later efficacy** in subsequent real selection.

Thus:

```text
constraint revision capacity
-> possible historical writeback
-> I5 admission test
-> qualified second-order-selection candidate
```

and explicitly:

```text
meta-selectability
!=
I5-qualified second-order selection
```

A purely institutional change can therefore satisfy the social revision pathway without yet licensing same-bearer second-order-selection language if consequence ownership / bearer continuity has not been established.

### 5.3 J5 relation — how deep is the reopening?

J5 classifies reopening depth:

```text
R1 weight layer
R2 category / object / boundary layer
R3 candidate-generation layer
R4 concern layer
```

`Reselect(Gamma_soc)` is only descriptive shorthand for revision of a local gating structure. Its realized depth can be:

- **R1-like** when an existing option's importance changes;
- **R2-like** when role categories / boundaries are recut;
- **R3-like** when previously unavailable response families become generatable;
- **R4-like** when what counts as an affected position's concern is redefined.

Therefore:

```text
Reselect(Gamma_soc)
!= automatically J5-R3
```

**Alternative-generation change is the specifically R3-like case.**

---

## 6. Social constraint-revision pathway: opening is not historical efficacy

### Claim SOC-COG03-E — durable social revision requires more than visibility

The source supports the possibility that script disruption changes salience. SRT adds a **social constraint-revision pathway**:

```text
Visibility
-> Contestability
-> Alternative generation
-> Enactability
-> Historical writeback
```

This is **not a second admission gate parallel to I5**. It is a domain-level process decomposition describing how a tacit social constraint may become revisable and historically effective. If one later wants to call the result a second-order-selection candidate, I5 must still be applied.

### 6.1 Visibility

The previously tacit script becomes identifiable as a constraint rather than remaining transparent background.

### 6.2 Contestability

The agent can question, interrupt or refuse the script without the challenge being automatically excluded from the interaction space.

### 6.3 Alternative generation

A different action or response structure can be formed, not merely a negative reaction to the old script. This is the stage most directly analogous to J5 R3 when the candidate-generation mechanism itself changes.

### 6.4 Enactability

The alternative can alter an actual path under real social resistance rather than remaining a verbally available possibility only.

### 6.5 Historical writeback

The enactment changes later expectations, access, role relations, habits or other future-selection conditions.

Therefore:

```text
new affordance becomes visible
!=
new affordance becomes historically effective
!=
I5-qualified second-order selection
```

---

## 7. Power / contestability consequence

The source's power asymmetry examples suggest a useful P3 decomposition:

```text
power over action
!=
power over the effective option field
!=
power over who may revise that option field
```

### 7.1 Action-level control

An agent can bias or compel selection among already visible options.

### 7.2 Field-level control

A social role, institution or script can shape what appears admissible, normal, soliciting or even thinkable as an interpersonal response.

### 7.3 Revision-level control

A structure can distribute the capacity to interrupt, challenge or rewrite the script asymmetrically.

Bounded social-theory implication:

> A system can offer many local choices while remaining deeply closed if affected positions cannot reopen or revise the constraints that organize those choices.

This is a political/social-theory bridge. It is not a canonical definition of domination or legitimacy, and it does not by itself establish I5 same-bearer second-order selection.

---

## 8. Relation to existing SRT surfaces

### 8.1 `Philosophy/SRT_Social_Cognition.md`

Current relevant handles include:

```text
Ax-Cog-2b Invitation Gating
SOC-COG02 Developmental Coordination Scaffold
```

SOC-COG03 should eventually sharpen the social side of invitation gating with role-indexed script parameters, distributed constraint carriers, supportive-vs-replacing automation, and constraint contestability / reselection.

### 8.2 P1 `L_2` downward constraint

The source provides a plausible social-cognition realization of historically sedimented constraint feeding back into current action possibilities.

Guard:

```text
script is one local carrier / projection candidate
!= entire L_2
```

### 8.3 P1 Real Choice Moment

Script made visible / challenged is a **choice opportunity**, not automatically a Real Choice Moment.

### 8.4 H3 / I5 / J5 source-intuition work

SOC-COG03 does not redefine these. It supplies a social-domain testbed:

```text
role/script gating
-> constraint becomes inspectable / contestable
-> possible revision
-> possible writeback
-> then ask whether H3/I5 is satisfied
-> classify reopening depth with J5
```

### 8.5 `T_dir`

Script disruption may create a local reorientation window by making a previously automatic direction or constraint readable.

Safe bridge:

```text
script disruption
-> possible increase in direction readability / reorientation opportunity
```

Forbidden identity:

```text
script disruption = T_dir increase
```

---

## 9. Mapping table

| Source / SRT concept | SRT P3 reading | Guardrail |
|---|---|---|
| interpersonal affordance | socially situated action possibility | not a new SRT primitive |
| role-indexed script | role-sensitive parameter on invitation gating | local bridge placeholders only |
| distributed script | distributed carrier of historical constraint | not `script = L_2` |
| skill as embodied script | sedimented low-level selection routine | automation can support higher-level choice |
| norm-violation discomfort | local mismatch / affective signal | not `Psi_f` identity |
| script disruption | makes tacit constraint inspectable | not automatically Real Choice |
| salience shift | effective invitation field changes | not `d-value` identity |
| constraint revision | social-domain reselectability entry | not yet H3/I5 second-order selection |
| alternative-generation rewrite | J5 R3-like reopening | not every `Reselect(Gamma_soc)` is R3 |
| social contestation | possible constraint-revision route | not durable change without enactment/writeback |
| power asymmetry | asymmetric ability to act / respond / revise | not a complete political legitimacy theory |

---

## 10. Experimental / operational consequences

These are P4 candidates generated by the bridge, not results of the source paper.

### P4-SOC03-1 — same physical context, different role/script

Hold physical affordances approximately fixed while manipulating role assignment, ownership, status or script expectation. Measure action generation, attention allocation, response latency, reported possibility and motor preparation.

Prediction window: role/script effects should appear in the candidate field before or alongside final policy choice if the gating claim is correct.

### P4-SOC03-2 — disruption and option generation

Compare participants before and after a script-disrupting intervention on generated interpersonal responses, perceived admissibility, willingness to enact alternatives and persistence across later interactions. This separates salience opening from durable writeback.

### P4-SOC03-3 — supportive automation test

Compare a well-learned skill condition with a rigid over-scripted condition under novel perturbation. Test whether automation reduces low-level burden while preserving rule-switching / novelty / revision, or improves routine execution while degrading higher-level reselection.

### P4-SOC03-4 — contestability / writeback / I5 discriminator

Manipulate whether participants can challenge an active norm and whether their challenge changes later group expectations or available responses. Then separately test whether the same affected historical position bears the consequences, whether comparison / generation rules change, whether future selectable space changes, and whether the change persists. This explicitly separates broad social revision from I5-qualified second-order-selection candidacy.

---

## 11. Boundary cautions

Do not infer:

```text
script = L_2
script execution = no agency at every level
script disruption = Real Choice Moment
social salience = d-value
awkwardness / blame / shame = Psi_f
explicit awareness = durable freedom
new option visibility = historical writeback
meta-selectability = I5 second-order selection
Reselect(Gamma_soc) = J5 R3 in every case
representation location settles causal efficacy
social power asymmetry automatically proves moral illegitimacy
Berio-Musholt empirically validate SRT
```

The source does not settle the low-level visual / neural implementation of script effects and remains neutral on several metaphysical questions about affordances themselves.

---

## 12. Integration hook

Primary pending synthesis target:

```text
Philosophy/SRT_Social_Cognition.md
```

Recommended owner-level compression, when the social-cognition/material-backflow phase is opened:

> **Social constraints can act before final action selection by shaping the effective invitation field itself: role-indexed, historically learned scripts may make some interpersonal actions salient, normal or soliciting while rendering others practically unavailable. Such automation is not intrinsically pathological; the relevant distinction is whether sedimented scripts release resources for higher-level live choice or replace the capacity to reopen and revise the constraints that generate the choice field. Constraint revision remains broader than H3/I5 second-order selection: only revisions tied to the same historical bearing position's consequence return, comparison/generation-rule rewrite, changed future selectable space and persistent later efficacy qualify as second-order-selection candidates.**

---

## 13. One-paragraph abstract

SOC-COG03 uses Berio and Musholt's script-based account of social affordances to sharpen SRT's social-cognition bridge without changing canonical definitions. The patch adds role-indexed invitation gating, treats scripts as potentially distributed carriers of historically effective constraint, distinguishes supportive skill automation from choice-replacing closure, and retains `meta-selectability` only as a broad P3 diagnostic within the repository's existing reselectability family. It explicitly crosswalks the social revision pathway to H3/I5/J5: visibility, contestability, alternative generation, enactability and writeback describe how a social constraint may become revisable, while I5 remains the stricter admission gate for second-order-selection candidacy and J5 classifies reopening depth. The patch preserves guards against `script=L_2`, `disruption=Real Choice`, `salience=d`, discomfort=`Psi_f`, and `Reselect(Gamma_soc)=R3` by default.
