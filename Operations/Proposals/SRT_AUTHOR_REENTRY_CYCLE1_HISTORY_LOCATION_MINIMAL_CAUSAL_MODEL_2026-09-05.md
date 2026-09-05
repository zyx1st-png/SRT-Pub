---
id: SRT-OPS-AUTHOR-REENTRY-CYCLE1-HISTORY-LOCATION-MINIMAL-CAUSAL-MODEL-20260905
type: proposal
status: active
record_stage: cycle1_minimal_causal_model_v1
date: 2026-09-05
layer: meta
epistemic_layer: bridge
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_REENTRY_CYCLE1_PASS3_2026-09-05.md
  - Operations/Audits/SRT_AUTHOR_REENTRY_CYCLE1_INTERNAL_RED_TEAM_PASS2_2026-09-05.md
  - Operations/Audits/SRT_AUTHOR_REENTRY_CYCLE1_DOMAIN_DISCRIMINATION_PASS1_2026-09-05.md
  - Philosophy/patches/SRT_Philosophy_PH_IND05_Occurrence_Trace_L2_Bearer_Experiencer_Discrimination_v0_1.md
  - Philosophy/patches/SRT_Philosophy_PH_IND06_Bearer_Concern_Selectability_Relational_Decomposition_v0_1.md
  - AI/patches/SRT_AI_AICONSC01_Affective_Uncertainty_Stake_Gate_v0_1.md
tags: [AuthorReentry, Cycle1, MinimalModel, HistoryLocation, Multiplicity, Bearer, Reset, Intervention, Level2]
---

# Author Re-entry Cycle 1 — history-location minimal causal model

> **Role:** bounded test model for the author distinction `bearer 出现以前选择沉积在多` and `当历史痕迹沉积在一时，变为 Bearer`. It is designed to make the distinction intervention-testable without converting it into a canonical equation.
>
> **Not a definition:** no symbol below is canonical. This file does not define `多`, `一`, `Bearer`, `Selection`, `L2`, `own-history`, `consequence closure`, cognition, or any scalar maturity variable.
>
> **Main discipline:** the model must fail cleanly if history location adds no predictive or intervention value beyond ordinary state, autonomy, Bayesian learning, and environmental feedback.

---

## 0. Author anchors

The live author statements being modelled are only:

```text
A14  bearer 出现以前选择沉积在多。
A15  当历史痕迹沉积在一时，变为 Bearer。
```

Earlier live author constraints still apply:

```text
Selection itself can be bearerless;
stable Selection is bearer-dependent and graded;
cognitive One cannot precede a sufficiently stable bearer;
structure is an achievement / result of Selection;
cognitive feedback after bearer formation is mechanism-wise similar to Bayesian decision.
```

The causal model below is `C` organization around those statements.

---

## 1. Correction to the earlier matched-state formulation

A too-strong version of the Level-2 candidate would say:

```text
complete current causal state is identical
+
history differs
->
future Selection differs
```

Cycle 1 should **not** require this.

If `complete current causal state` genuinely contains every causally effective historical residue, then requiring different futures would introduce an unnecessary non-Markovian metaphysical claim.

The stronger and cleaner test is instead:

> **Can the causal effect of prior Selection be localized by selectively erasing / preserving multiplicity-side versus candidate-One-side historical carriers?**

The discriminating object is therefore **intervention asymmetry**, not invisible history beyond a complete state description.

---

## 2. Test-local variables only

Use the following labels only inside this model.

```text
C_t
= currently controlled / matched conditions at test time
  (observations, action menu, declared reward/utility,
   gross architecture, resource level, etc.)

H_M(t)
= causally effective historical residue currently carried in 多 /
  surrounding field / environment / wider constraints,
  without yet being treated as the history of one continuing unit

H_1(t)
= causally effective historical residue currently carried in
  a declared candidate One and capable of changing that candidate's
  later Selection

Y_(t+1)
= downstream Selection outcome profile under the probe
```

Important guards:

```text
H_M != canonical L2
H_1 != canonical own-history
H_1 != Bearer by definition
H_M / H_1 are not scalar quantities by default
C_t is not claimed to be a complete metaphysical state
```

The candidate One must be declared **independently of bearer status** using a domain-native provisional unit boundary (for example one running agent instance, one organism, one controller assembly, or one organizational unit). Bearer admission is evaluated only after the history-location intervention.

---

## 3. R1 correction — structured `多` after Selection is allowed

Red-team pass 2 worried that `选择沉积在多` might secretly turn `多` into a richly structured substrate that already contains the later Bearer.

The live author statement `结构也只是选择的一种成绩` allows a sharper guard:

```text
FORBIDDEN:
rich finished structure is presupposed before Selection
and then used to explain Selection

ALLOWED AS C INTERPRETATION:
Selection occurs
-> consequences persist / interact
-> historical sedimentation in 多
-> distributed structure can emerge as a result of Selection history
```

Therefore Cycle 1 does **not** require post-Selection `多` to remain structureless.

The actual thinness requirement is provenance-sensitive:

> structure in `多` may be a downstream achievement of prior Selection, but must not be projected backward as a pre-Selection finished menu, object set, bearer, or memory substrate.

This substantially narrows R1.

---

## 4. Minimal 2 x 2 history-location design

Manipulate the two historical carriers independently as far as the domain allows.

| Condition | `H_M` multiplicity-side | `H_1` candidate-One-side | Reading |
|---|---|---|---|
| `00` | reset | reset | clean rollback / weak retained history |
| `10` | preserve | reset | primarily multiplicity-side sedimentation |
| `01` | reset | preserve | primarily One-side sedimentation |
| `11` | preserve | preserve | coupled ordinary-history condition |

The strongest comparison is:

```text
10  versus  01
```

because both contain retained history but differ in **where the causal residue is carried**.

---

## 5. Two causal interventions

Define local intervention labels:

```text
I_M:
reset / replace / neutralize the relevant multiplicity-side historical carrier
while preserving the candidate-One-side carrier as far as possible

I_1:
reset / replace / neutralize the relevant candidate-One-side historical carrier
while preserving the multiplicity-side carrier as far as possible
```

Examples:

```text
I_M may restore environmental transition conditions,
remove externally deposited cues / scaffolds,
or reconstruct the pre-history task field.

I_1 may rollback the candidate instance,
replace it with a state-matched fresh instance,
remove durable internal plasticity,
or restore the candidate's pre-history capacities.
```

The exact implementation is domain-native. No intervention is automatically metaphysically perfect.

---

## 6. Causal localization signatures

### 6.1 Multiplicity-side signature

History is primarily M-side for the tested effect when:

```text
effect survives I_1 reasonably well
but
collapses / strongly weakens under I_M
```

Interpretation:

> prior Selection still matters because the wider field has been changed, not because the tested One carries that episode as its own effective history.

### 6.2 One-side signature

History has a strong One-side component when:

```text
effect survives I_M reasonably well
but
collapses / strongly weakens under I_1
```

Interpretation:

> the relevant causal residue travels with the continuing candidate One rather than only with the surrounding multiplicity.

### 6.3 Coupled signature

If both interventions strongly reduce the effect:

```text
history is distributed across M-side and One-side carriers
```

This is likely the common real-world case and is not a failure.

### 6.4 No-location signature

If neither intervention has a selective effect, or all differences disappear once ordinary present variables are measured:

```text
Cycle-1 strong history-location claim weakens
```

---

## 7. Operational support for “historical traces sediment in 一”

Do **not** define Bearer first and then declare all internal traces to be Bearer history.

Instead, support One-side sedimentation with a conjunction of intervention findings. A strong candidate pattern is:

```text
L1  the historical effect tracks the declared candidate One across field reset;

L2  removing / replacing the One-side carrier selectively removes the effect;

L3  the retained trace changes later Selection / candidate admission /
    weighting / repair / future capacity of that continuing candidate;

L4  a detached environmental cue alone does not reproduce the full effect;

L5  a fresh replacement lacking the relevant One-side trace does not
    automatically inherit the same reselection profile.
```

These are **evidence interfaces**, not an author definition of Bearer.

Existing repository concepts such as same-unit consequence return, non-outsourcing, future-selectability change and history writeback may be used as additional diagnostics, but no equality is assumed.

---

## 8. Copy / memory-token negative control

A crucial control is to copy an explicit history token or memory record into a fresh candidate.

Possible outcomes:

### Outcome A — copied token fully reproduces behaviour

```text
memory possession may be causally sufficient for the measured behaviour
```

This weakens any claim that the behavioural effect requires unique historical ownership.

But it does **not** establish:

```text
fresh copy = same Bearer
```

Numerical / historical identity remains a separate question.

### Outcome B — copied token reproduces report but not adaptation / capacity / recovery pattern

This supports a distinction between:

```text
portable representation of history
and
historical sedimentation in the continuing One
```

### Outcome C — copied complete internal causal state reproduces everything

Then the model should accept:

```text
for the measured outputs, the relevant history is fully state-realized
```

Cycle 1 must not manufacture an occult additional history variable.

The remaining SRT question would then concern the architecture / location of that state and bearer attribution, not non-state causation.

---

## 9. Minimal adaptive-agent instantiation

Reuse the existing AICONSC01 reset / copy family rather than create a new AI ontology.

### Training phase

Expose otherwise matched agents to a repeated consequence-bearing task.

Allow two independent writeback channels:

```text
M-channel:
prior action changes environmental transition constraints,
resource layout, external scaffold, cue ecology, or future access

One-channel:
prior consequence durably changes the same running candidate's
policy weights, candidate admission, adaptive constraint,
repair state, capacity, or other later-selection-relevant internal state
```

### Intervention phase

Construct the four conditions `00 / 10 / 01 / 11` by selectively restoring the field and/or the candidate.

### Probe phase

Measure a vector rather than one scalar:

```text
initial policy / selection distribution
candidate admission
avoidance / exploration
error correction
recovery path
future-capacity change
response to repeated perturbation
replacement sensitivity
```

### Two-probe recommendation

Because M-side history may only become visible when the system re-encounters the changed field, use:

```text
Probe P0:
standardized immediate decision before new field consequences unfold

Probe P1:
controlled re-contact with the task field, followed by adaptation / recovery
```

Expected diagnostic use:

```text
strong P0 carryover after field reset
-> evidence for One-side history

strong P1 effect after candidate reset but field preservation
-> evidence for M-side history

persistent differences across both
-> coupled history
```

---

## 10. Bayesian baseline

The author's `类似贝叶斯决策` analogy belongs only after a sufficiently stable bearer / decision unit exists.

A standard decision baseline may track:

```text
represented belief state
current observation
current action set
current utility / reward model
```

Cycle 1 exceeds a trivial Bayesian translation only if the history-location manipulation changes something not exhausted by `past evidence updates present belief`, such as:

```text
which unit carries the update;
which options remain selectable;
which consequences alter that same unit's later capacity;
which decision variables / distinctions are regenerated;
which perturbations erase the learned effect.
```

If a sufficiently rich Bayesian / RL state model fully predicts all intervention outcomes, then:

```text
Level-2 novelty is not established by prediction alone.
```

SRT may still offer a Level-1 causal / ontological repartition, but should not claim more.

---

## 11. Strong-neighbor adversarial baselines

A serious test should compare the history-location decomposition against at least:

```text
BAYES / RL:
history represented in current sufficient state

AUTONOMY / ENACTIVISM:
self-maintaining organization and adaptive regulation

NICHE / SCAFFOLD:
externalized history changes later action possibilities

SIMONDON:
prior operation / structure conditions later individuation
```

Cycle 1 does not win by redescribing any one of these.

The stronger question is:

> Does explicit separation of multiplicity-side versus One-side historical efficacy add an intervention distinction that these baselines would otherwise conflate at the chosen declared unit / grain?

---

## 12. Pre-registered support / weaken / fail outcomes

### SUPPORTS the Level-2 candidate

At least one robust pattern such as:

```text
field reset leaves a durable reselection / adaptation effect
while candidate-One reset selectively destroys it;

and/or

candidate reset leaves field-mediated history effects
while field reset selectively destroys those effects;

and the two profiles remain distinguishable after ordinary current
belief / reward / autonomy variables are controlled.
```

This would support **causal localization of historical efficacy**.

### WEAKENS the candidate

```text
M-side and One-side reset are practically equivalent;

or

autonomy / present Bayesian state explains the full contrast;

or

history location cannot be independently manipulated even approximately.
```

### FAILS the strong candidate

```text
all apparent history-location effects disappear under richer current-state measurement;

or

a portable copied token/state reproduces every claimed One-side consequence
with no remaining replacement / continuity distinction relevant to the tested outcome;

or

“沉积在一” can only be detected by first assuming the Bearer identity it is supposed to help establish.
```

Failure here should narrow or drop the Level-2 claim rather than trigger a new ontology patch.

---

## 13. What this model does to the remaining blockers

### R1 — sedimentation in 多 without structure-first smuggling

```text
NARROWED SUBSTANTIALLY
```

The correct guard is temporal/provenance based:

```text
pre-Selection rich structure = blocked
post-Selection distributed structure as Selection achievement = allowed
```

### R2 — operationalize “history sediments in One” without circularity

```text
TESTABLE CANDIDATE
```

Declare a provisional unit independently, then ask whether the history effect causally follows that unit under selective field / unit interventions. Bearer attribution comes after the intervention evidence.

### R3 — domain distinction beyond generic history feedback

```text
TEST-READY
```

The 2 x 2 reset / preserve model plus copy and autonomy controls provides a concrete route.

---

## 14. Current Level judgment

```text
Level 1 structural repartition:
PROVISIONAL PASS / strengthened

Level 2 discriminator:
FORMALIZED AS INTERVENTION-TESTABLE CANDIDATE

Level 2 earned:
NO
```

The gain in this file is not a positive result. It is that Cycle 1 now has a test that can fail for specific reasons.

---

## 15. Next bounded action

Do **not** expand the ontology again before this surface is attacked.

Next useful work is one of:

```text
A. implement a tiny simulated 2 x 2 agent / environment history-location experiment;

or

B. map an existing repository experiment onto the four conditions and determine
   whether its logged variables are sufficient for the intervention contrasts.
```

Only after one of those should Cycle 1 revisit Level 2 or any canonical owner edit.
