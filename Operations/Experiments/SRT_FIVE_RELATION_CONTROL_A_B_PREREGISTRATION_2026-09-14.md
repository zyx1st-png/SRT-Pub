---
id: SRT-EXP-FIVE-RELATION-CONTROL-A-B-PREREG-20260914
type: experiment_spec
status: preregistered_draft
date: 2026-09-14
layer: meta
epistemic_layer: research_program
claim_mode: experiment_spec
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
dependency:
  - Operations/Audits/SRT_FIVE_RELATION_MINIMUM_TOOL_OPERATIONALIZATION_PASS_2026-09-14.md
  - Core_Law/SRT_Collective_Selection.md
  - Core/SRT_Core_21c_Bridge_Hypotheses.md
  - 90_Backstage/Incubation/_SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md
tags: [Experiment, Selection, Standing, Shaping, Bearing, Revision, ControlA, ControlB, Falsification]
---

# Five-relation minimum tool — Control A / B preregistration

> **Boundary:** noncanonical experimental specification. No new canonical metric is defined. All quantitative variables below are model-local proxies declared only for the experiment.

## 0. Purpose

Test whether SRT's five-relation typing adds discriminatory value beyond strong rival models that receive the same observable state information.

The experiment must not let SRT win by seeing extra data.

Both SRT and rival analyses receive the same full state history.

---

# Control A — matched performance, different consequence/revision topology

## A1. Environment

Use `N >= 4` adaptive agents in a shared resource/task environment.

Each round contains:

```text
candidate generation;
action / allocation;
outcome;
position-specific consequence;
possible update of future candidate-generation rules.
```

Two conditions use identical:

```text
task distribution;
agent capabilities;
visible option count;
initial policy parameters;
aggregate resource budget;
aggregate reward schedule;
short-horizon performance target;
random seeds where pairable.
```

## A2. Condition topology

### A-E — externalized consequence topology

A high-performing controller / scaffold can allocate actions that improve aggregate reward while a subset of agents bears persistent local cost.

Those burden-bearing agents have weak or zero writeback into the rule that generates later candidate sets.

### A-R — returned consequence topology

Keep the same aggregate task and cost envelope, but route local consequences back into the candidate-generation / access rule affecting the positions that bear them.

Affected positions can participate in revision of that rule.

## A3. Matching constraint

Tune parameters so that during the calibration horizon:

```text
aggregate reward_A-E ~= aggregate reward_A-R;
visible option count_A-E ~= visible option count_A-R;
aggregate cost_A-E ~= aggregate cost_A-R;
short-run stability_A-E ~= aggregate stability_A-R.
```

If matching fails, the test is invalid.

## A4. Model-local readouts

Do not call these canonical SRT quantities.

For each position `i` measure:

```text
reachable-option count under actual constraints;
reachable-option entropy;
exit / recovery cost;
probability of restoring a lost option after perturbation;
consequence-return coefficient;
rule-revision participation rate;
post-shift recovery time.
```

Also measure aggregate performance and stability.

## A5. Perturbation

After calibration, introduce a regime change that makes the old candidate-generation rule systematically mismatched.

Examples:

```text
resource relocation;
changed task payoff;
new failure mode;
removal of one support channel.
```

The perturbation must be identical across paired runs.

## A6. SRT-side preregistered classification

Before seeing results:

```text
A-E:
aggregate performance may remain high,
but Bearing and Revision are topologically separated;
position-specific future selectability can degrade without immediate aggregate failure.

A-R:
Bearing and Revision are more strongly coupled;
if the burden signal is informative, later shaping should adapt more effectively under regime change.
```

This is not a moral verdict.

## A7. Rival baselines

### Rival 1 — standard aggregate adaptive model

Use the same state history but optimize / classify only with aggregate reward, stability and prediction-error variables.

### Rival 2 — strong state-augmented rival

Allow the rival to include all position-specific costs, action constraints and update histories available to SRT.

It may use:

```text
multi-agent RL;
active inference;
control theory;
externality-aware welfare/accounting;
network adaptation.
```

No restriction prevents the rival from reproducing the same result if its own native framework supports it.

## A8. SRT success condition

SRT earns architecture-level support only if the five-relation typing supplies at least one of:

```text
A-S1 a preregistered classification difference missed by Rival 1 and not trivially reconstructed by Rival 2;
A-S2 a cross-position failure prediction that improves held-out perturbation prediction;
A-S3 a stable mapping rule that transfers unchanged to a second domain model.
```

## A9. SRT failure condition

Demote this contribution if:

```text
A-F1 Rival 2 reproduces all classifications/predictions with equal or lower representational burden;
A-F2 Bearing/Revision labels do no work after all state variables are included;
A-F3 the result depends on moral weighting rather than structural dynamics;
A-F4 matching cannot be achieved without changing other causal factors.
```

---

# Control B — matched standing/shaping, different generator revision

## B1. Environment

Use a single formed adaptive system or matched population with an explicit candidate generator / scaffold.

Calibration phase holds fixed:

```text
system boundary;
current scaffold;
current candidate set;
performance;
maintenance cost;
continued selectability;
training experience.
```

## B2. Conditions

### B-P — policy-only adaptation

The system may change action choice or policy weights inside a fixed candidate-generation architecture.

It cannot modify:

```text
candidate-generation rules;
access boundaries;
comparison rule family;
scaffold structure.
```

### B-G — generator-revision adaptation

The system has the same policy adaptation plus consequence-sensitive access to modify at least one generator-level component.

## B3. Perturbation

After calibration, introduce a structural shift for which no existing fixed candidate family contains an adequate response.

The shift must be chosen so that simple parameter retuning is insufficient in at least one preregistered region.

## B4. Model-local readouts

Measure:

```text
recovery latency;
post-shift performance;
new reachable strategy count;
structural model change;
external reset dependence;
scaffold withdrawal fragility;
recurrence of failure after second perturbation.
```

## B5. SRT-side preregistered classification

```text
B-P may remain stable and continued-selectable while lacking generative reselectability.
B-G has Revision only if consequence return changes the shaping/generator relation itself.
```

The test therefore preserves the existing repository distinction:

```text
continued selectability != generative reselectability.
```

## B6. Rival baselines

Rival models receive the same state and update access.

Strong baselines must include at least:

```text
meta-learning / structure learning;
adaptive control;
active inference with model learning;
open-ended search / evolutionary adaptation.
```

## B7. SRT success condition

SRT earns support only if its relation typing predicts or classifies a systematic difference that survives comparison with strong structure-learning rivals and transfers to another implementation.

## B8. SRT failure condition

Demote if:

```text
B-F1 Revision is exactly equivalent to an already standard structure-learning variable with no additional cross-layer constraint;
B-F2 the SRT classification changes when equivalent model parameterizations are used;
B-F3 the result depends only on giving B-G more computational capacity;
B-F4 no second-domain transfer preserves the same relation typing.
```

---

# 3. Anti-cheating rules

The following are forbidden after results are observed:

```text
adding a sixth relation to rescue a failed result;
changing Bearing admission because one condition performed unexpectedly;
calling any performance difference proof of ontology;
withholding state variables from rivals;
using a weak rival after a strong rival reproduces the result;
changing perturbation class after seeing results;
converting a null result into "SRT predicted flexibility" without preregistered metric.
```

---

# 4. Cross-domain transfer requirement

At least one control must later be instantiated in two domains with the same relation definitions.

Recommended pair:

```text
Domain 1: multi-agent computational allocation / coordination;
Domain 2: human-AI or organizational scaffold decision task.
```

The implementation mechanism may differ, but the mapping rules for Generation / Standing / Shaping / Bearing / Revision must remain fixed.

---

# 5. Current status

```text
Control A = PREREGISTERED DRAFT
Control B = PREREGISTERED DRAFT
execution = NOT STARTED
canonical consequence = NONE
scientific distinctiveness = NOT ESTABLISHED
architecture-level non-substitutability = NOT ESTABLISHED
Level 2 = HOLD
```

Next step: run strongest-rival preregistration review before any execution or parameter tuning.
