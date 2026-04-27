---
id: SRT-PILOT-CARDS-V1-2026-04-27
type: pilot_cards
tags:
  - SRT
  - Experiments
  - Pilot-Cards
  - Validation
  - d-value
  - Salience
  - Psi_f
  - Prediction-Error
  - L2-Hardening
  - Memory
  - Habit
status: active_v1
layer: empirical_bridge
epistemic_layer: experimental
claim_mode: pilot_design
claim_level: P4-P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - Core/SRT_Validation_Template.md
  - Experiments/SRT_Experimental_Roadmap_v1.md
  - SRT_OPTIMIZATION_COMPLETION_AUDIT_2026-04-27.md
  - Papers/SRT_NonReductive_Verification_Outline.md
  - Papers/SRT_D_Value_Ontology_of_Concern_Outline.md
machine_summary: >
  First set of low-cost SRT pilot cards. It converts the experimental roadmap into three P0 pilot-ready
  designs: d-value vs salience, Psi_f vs prediction error, and L2 hardening vs memory/habit. Each card
  includes claim, baseline, SRT-specific prediction, task design, proxy measures, expected pattern,
  failure condition, narrowing condition, minimal analysis, and next implementation notes.
---

# SRT Pilot Cards v1

> **Purpose**: Convert SRT's experimental roadmap into small, testable pilot designs.  
> **Status**: Pilot-design bridge. These are not completed experiments.  
> **Use rule**: Treat each card as a draft research protocol. Before running, refine stimuli, ethics, sample size, and analysis plan.

---

## 0. Why these pilots first

These pilots target the three lowest-cost and highest-value empirical discriminations:

```text
1. d-value != salience
2. Psi_f != prediction error
3. L2 hardening != ordinary memory / habit
```

They are useful because they directly answer the most common reviewer objection:

> “Are SRT's core concepts just new names for existing constructs?”

---

## 1. Shared pilot standard

Each pilot must specify:

```text
SRT claim;
nearby theory / baseline;
SRT-specific prediction;
task design;
proxy measurements;
expected pattern;
failure condition;
narrowing condition;
minimal analysis;
next implementation step.
```

Minimum evidence standard:

```text
SRT proxy predicts outcome beyond baseline variables.
```

Minimum failure standard:

```text
Baseline variables fully explain the outcome -> narrow SRT claim.
```

---

# Pilot Card 1 — d-value vs Salience

## 1. Claim

`d-value` is not reducible to salience, confidence, arousal, reward, or preference intensity.

## 2. Nearby theory / baseline

```text
salience;
arousal;
confidence;
reward magnitude;
preference intensity;
attention capture.
```

## 3. SRT-specific prediction

Stimuli or scenarios with higher `d-value` should predict later memory persistence, action reorganization, non-substitutability, and future decision weighting beyond salience ratings.

## 4. Task design

Participants view short scenarios or objects matched for surface salience but varied in existential stake.

Example contrast:

```text
High salience / low d-value:
- flashy advertisement;
- dramatic but irrelevant news;
- visually intense image with no personal implication.

Lower or matched salience / high d-value:
- message affecting family responsibility;
- opportunity that changes future options;
- small promise / betrayal / obligation;
- loss of something non-substitutable.
```

Participants rate each item immediately, then complete delayed recall and choice tasks.

## 5. Proxy measurements

Primary:

```text
memory persistence;
future choice reweighting;
non-substitutability rating;
willingness to bear cost;
identity / future relevance rating.
```

Secondary:

```text
reaction time;
confidence;
arousal;
attention capture;
preference rating.
```

## 6. Expected pattern if SRT is right

After controlling for salience, arousal, confidence, and preference, high-`d-value` items still predict:

```text
better delayed recall;
stronger action-path change;
greater substitution resistance;
higher willingness to bear cost;
stronger future-option reweighting.
```

## 7. Failure condition

If salience, arousal, confidence, reward, and preference fully explain memory and action effects, `d-value` should be narrowed or treated as a redescription.

## 8. Narrowing condition

Restrict `d-value` to cases involving:

```text
identity relevance;
non-substitutability;
future-selectability;
commitment / loss / obligation;
subjecthood stakes.
```

## 9. Minimal analysis

Regression / mixed model:

```text
Outcome ~ salience + arousal + confidence + preference + d_proxy + participant_random_effect
```

Key test:

```text
d_proxy remains significant after baseline controls.
```

## 10. Pilot scale

Low-cost online pilot:

```text
N = 80-150 participants;
20-40 stimuli/scenarios;
immediate + delayed task, ideally 24h delay if feasible.
```

## 11. Implementation notes

First build a stimulus set with independent pre-ratings for:

```text
salience;
arousal;
preference;
d-value proxies;
identity relevance;
non-substitutability.
```

---

# Pilot Card 2 — Psi_f vs Prediction Error

## 1. Claim

`Psi_f` is not reducible to prediction error or task difficulty. It tracks transition cost / selection friction across information, embodiment, identity, and norm layers.

## 2. Nearby theory / baseline

```text
prediction error;
free energy / surprise;
task difficulty;
cognitive load;
switching cost;
uncertainty.
```

## 3. SRT-specific prediction

Two updates with similar prediction error can differ in `Psi_f` when one requires identity-relevant, norm-revising, or self-relevant re-anchoring.

## 4. Task design

Create matched feedback-update tasks.

Condition A — neutral update:

```text
Participant learns that an external estimate, category, or neutral prediction was wrong.
```

Condition B — self / norm update:

```text
Participant learns that a self-relevant judgment, social norm judgment, or identity-linked assumption was wrong.
```

Match conditions for objective error magnitude where possible.

## 5. Proxy measurements

Primary:

```text
update latency;
choice revision delay;
reframing resistance;
post-feedback hesitation;
confidence drop;
recovery time;
second-trial adaptation.
```

Secondary:

```text
subjective discomfort;
physiological proxy if available;
self-relevance rating;
norm relevance rating;
perceived cost of accepting update.
```

## 6. Expected pattern if SRT is right

Self/norm-revising updates show higher transition friction than neutral updates even when prediction error and task difficulty are matched.

Expected signature:

```text
same error size;
higher hesitation;
slower update;
more resistance;
more downstream instability;
stronger memory of correction.
```

## 7. Failure condition

If prediction error, task difficulty, uncertainty, and cognitive load fully explain update cost, `Psi_f` must be narrowed.

## 8. Narrowing condition

Separate:

```text
Psi_f^inf  = information-geometric update cost;
Psi_f^emb  = embodied / affective transition cost;
Psi_f^norm = normative / identity transition cost.
```

Only claim broader `Psi_f` where additional layer-specific friction is empirically visible.

## 9. Minimal analysis

Model:

```text
UpdateCost ~ prediction_error + task_difficulty + self_relevance + norm_relevance + condition + participant_random_effect
```

Key test:

```text
self/norm relevance predicts update cost beyond prediction error.
```

## 10. Pilot scale

Low-cost behavioral pilot:

```text
N = 80-150;
within-subject neutral vs self/norm update tasks;
reaction time + rating + delayed recall.
```

## 11. Implementation notes

Avoid overly threatening materials in early pilot. Start with mild self-relevant or norm-relevant judgments to reduce ethics burden.

---

# Pilot Card 3 — L2 Hardening vs Memory / Habit

## 1. Claim

`L_2` hardening is not ordinary memory or habit alone. It is a paired signature:

```text
reduced local selection cost + increased global reselection constraint + hysteresis
```

## 2. Nearby theory / baseline

```text
memory strength;
habit frequency;
practice amount;
schema formation;
attractor state;
reinforcement learning.
```

## 3. SRT-specific prediction

A hardened pattern should show both automation and rigidity. Memory alone may improve recall, but `L_2` hardening should produce local ease plus reversal cost.

## 4. Task design

Train participants on repeated rule-based selections.

Phase 1 — learning / repetition:

```text
Participants repeatedly apply a rule or category mapping.
```

Phase 2 — stabilization:

```text
Rule becomes fast and automatic.
```

Phase 3 — perturbation / reversal:

```text
Rule changes, exceptions appear, or context requires alternative selection.
```

## 5. Proxy measurements

Primary:

```text
reduced deliberation time during stabilization;
error increase after reversal;
reaction-time cost after reversal;
persistence of old rule;
subjective effort to switch;
hysteresis / carryover.
```

Secondary:

```text
explicit memory of rule;
confidence;
practice amount;
habit automaticity rating;
frustration / discomfort.
```

## 6. Expected pattern if SRT is right

Hardening shows paired signature:

```text
faster default selection before reversal;
higher cost when alternative selection is required;
old rule persists even when explicit memory of new rule is present.
```

## 7. Failure condition

If memory strength, practice, or ordinary habit fully explain automation and reversal cost, strong `L_2` hardening claims should be narrowed.

## 8. Narrowing condition

Treat `L_2` as an integrative vocabulary unless the paired signature appears:

```text
local ease + global rigidity + hysteresis
```

## 9. Minimal analysis

Model:

```text
ReversalCost ~ practice_amount + memory_strength + habit_rating + hardening_proxy + participant_random_effect
```

Key test:

```text
hardening_proxy predicts reversal cost beyond memory and practice.
```

## 10. Pilot scale

Low-cost online or lab pilot:

```text
N = 80-150;
rule-learning task;
within-subject reversal phase;
reaction time + error + explicit memory check.
```

## 11. Implementation notes

Start with simple abstract categories first. Later versions can use social norm learning or identity-relevant categories.

---

## 4. Pilot priority order

Recommended order:

```text
1. Pilot Card 1 — d-value vs salience
2. Pilot Card 3 — L2 hardening vs memory / habit
3. Pilot Card 2 — Psi_f vs prediction error
```

Reason:

```text
d-value pilot is most central and easiest to explain;
L2 hardening pilot is mechanically clean;
Psi_f pilot is important but needs more careful stimulus design.
```

---

## 5. Minimal first implementation package

Before running any pilot, create:

```text
stimulus bank;
pre-rating form;
analysis skeleton;
ethics note;
data dictionary.
```

Suggested next files:

```text
Experiments/SRT_D_Value_vs_Salience_Stimulus_Bank_v0.md
Experiments/SRT_D_Value_vs_Salience_Analysis_Plan_v0.md
Experiments/SRT_Pilot_Ethics_Note_v0.md
```

---

## 6. What would count as progress

Early pilots do not need to prove SRT.

They only need to show whether SRT concepts can produce measurable discriminations beyond baseline constructs.

Progress levels:

| Level | Meaning |
|---|---|
| P0 | stimuli and proxies defined |
| P1 | pre-rating completed |
| P2 | pilot data collected |
| P3 | SRT proxy beats at least one baseline |
| P4 | SRT proxy survives multiple baselines |
| P5 | replication or cross-domain version exists |

---

## 7. Minimal conclusion

The first experimental move should be modest:

```text
do not try to prove SRT;
try to separate one SRT construct from one nearby baseline.
```

If these pilots fail, SRT should narrow.  
If they succeed, SRT gains a credible empirical foothold.
