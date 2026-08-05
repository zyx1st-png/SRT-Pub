---
id: SRT-AI-AIGOAL01-GOAL-SELECTION-COMPLETION-SEPARATION
type: material_patch
status: active
version: v0_1
layer: bridge
epistemic_layer: bridge
claim_mode: bridge
claim_level: P3/P4
canonical: false
patch_id: SRT-AI-AIGOAL01-GOAL-SELECTION-COMPLETION-SEPARATION
source_ids:
  - SRC-2026-05-13-AI-MOLINARO-LLM-GOAL-SELECTION
domain: AI / Goal Selection / Self-Directed Learning
target_future_doc:
  - AI/SRT_AI_Architecture_CompactCore.md
  - AI/SRT_AI_Claim_Status.md
  - Bridge/SRT_Context_Coherence_Intelligence_Interface.md
  - 03_Bridges/SRT_Choice_Generation_Conditions_2026-08-04.md
related_claims:
  - capability_propensity_separation
  - goal_completion_goal_selection_goal_generation
  - context_conditioned_selection
  - local_success_capture
  - T_dir_proxy_boundary
  - architecture_state_rule
  - CG0_CG4_selection_event_audit
tags: [goal-selection, self-directed-learning, autotelicity, intrinsic-motivation, capability-propensity, local-success-capture, chain-of-thought, persona-steering, exploration, silicon-subjects]
---

# AIGOAL01 — Goal Selection / Goal Completion Separation

> Status: bounded AI behavioral bridge and experiment-design patch.  
> Canonical caution: this patch does not define selection, `T_dir`, `d-value`, `Psi_f`, agency, subjecthood, intrinsic motivation, or consciousness. It records an empirical dissociation between local task competence and human-like goal-selection trajectories in a bounded menu task.

## 1. Source anchor

Primary SourceCard:

- `../../Materials/2026/SRC_2026_05_13_AI_Molinaro_LLM_Goal_Selection.md`

Primary source:

- Gaia Molinaro, Dave August, Danielle Perszyk, and Anne G. E. Collins. “Language Model Goal Selection Differs from Humans’ in a Self-Directed Learning Task.” arXiv:2603.03295v2, 2026-05-13.

The paper compares 175 humans with five language-model systems in a controlled learning environment where the next goal is freely selected from six experimenter-defined options. Its evidential status is primary preprint behavioral research, not peer-reviewed mechanism evidence.

## 2. Why this matters for SRT

SRT’s AI boundary work already separates competence, context coherence, tool use, stake, and real choice. This source adds a missing behavioral distinction:

~~~
Can the system execute a selected goal?
!=
Which goal does it select when several are available?
!=
Can it generate or revise the space of goals itself?
~~~

Several models achieved very high success during free learning while repeatedly exploiting one easy or already solved goal, showing low goal entropy, weak systematic exploration, and poor surprise-test coverage. Chain-of-thought increased route execution more reliably than it produced human-like reorientation.

This matters because many proposed AI uses silently move from:

~~~
model can solve candidate tasks
~~~

to:

~~~
model can decide which tasks deserve pursuit
~~~

without independently testing the second claim.

## 3. Main SRT bridge claim

> **Goal-Selection / Goal-Completion Separation Principle:** High competence in executing an externally selected goal does not establish a comparable capacity to select among goals, preserve broad future learnability, generate new goals, or revise the criterion under which goals are evaluated.

This is a P3 bridge guardrail supported by the reported behavioral dissociation. It is not a claim that artificial goal generation is impossible or that human goal selection is non-formalizable.

## 4. Three-level target ladder

Let `Omega_t` denote the currently available target set, `g_t` a selected goal, `a_t` an action sequence, and `h_t` the accessible interaction history.

### 4.1 Goal completion

~~~
pi_action(a_t | g_t, h_t, theta)
~~~

The goal is supplied. Evaluation asks whether the system finds an effective route to it.

### 4.2 Goal selection

~~~
pi_goal(g_t | Omega_t, h_t, theta)
~~~

The goal is not supplied for the current round, but the candidate set and success grammar are externally fixed.

### 4.3 Goal-space generation or revision

~~~
Omega_t -> Omega_(t+1)
~~~

The system can create, reject, merge, reinterpret, or revise candidate goals or their success conditions.

The paper directly studies level 4.2, uses level 4.1 as the action-performance measure, and does not directly test level 4.3.

## 5. Source-to-SRT mapping

| Source object or result | Bounded SRT reading | Boundary |
|---|---|---|
| six potion goals | externally objectified candidate menu | not model-generated possibility space |
| goal choice each trial | behavioral target-selection output | output alone does not locate internal NER mechanism |
| recipe choice | route execution under a selected target | high accuracy is not broad direction formation |
| deterministic success feedback | local path-validity signal | not model-boundary stake or canonical value |
| complete interaction history | session-level context scaffold / weak historical efficacy | not durable same-bearer identity or weight update |
| repeated solved goal | locally hardened success path | may reflect instruction priors, simple heuristics, or proxy capture |
| low goal entropy | concentrated behavioral policy | not by itself low `T_dir`; random choice can have high entropy |
| systematic human hypothesis testing | memory-sensitive exploration scaffold | not automatically superior rationality |
| chain-of-thought improvement | stronger local path construction / context expansion | not transparent mechanism report or self-readable direction |
| persona steering | altered role-conditioned `L2` prompt scaffold | persona narrative is not bearer continuity |
| surprise test drop | weak coverage beyond self-selected local paths | not proof of an internal reward function |
| nearest-human distribution gap | failure to reproduce sampled human behavioral variation | human similarity is not identical to intelligence or value alignment |

## 6. Local success capture under global direction underspecification

The task does not lack all objectives. It contains a clear local signal:

~~~
correct recipe -> success feedback
incorrect recipe -> failure feedback
~~~

What remains underspecified is the global direction:

- maximize immediate success;
- learn every goal;
- maximize information gain;
- discover hierarchical relations;
- prepare for an unknown future test;
- imitate a typical human participant;
- pursue personally interesting goals.

Several models behaved as though the clearest local success signal dominated these unannounced alternatives. A bounded bridge description is:

~~~
global direction incomplete
-> pretrained / instructed success prior fills the gap
-> one verified route gains local dominance
-> repeated exploitation narrows explored target space
~~~

This is **local success capture**, not a claim that an internal scalar reward has been identified.

## 7. Relation to `T_dir`

The paper creates a useful proxy boundary:

~~~
more chain-of-thought
-> better execution of the current route
~~~

but often not:

~~~
more chain-of-thought
-> better reorientation across goals
~~~

This supports the distinction:

~~~
semantic explanation / deliberation length
!=
directional self-readability and effective reorientation
~~~

However, neither goal entropy, switching frequency, verbal reasons, nor human similarity is canonical `T_dir`. At most they are candidate behavioral proxies under an explicitly declared architecture state and task window.

## 8. Post-hoc CG-0 to CG-4 audit

The source was not designed as an SRT selection-event experiment. The following is a bounded reanalysis, not a source conclusion.

### CG-0 — difference manifestation

Supported at the task interface: six goals and their difficulty/structural differences enter the model-visible prompt and correspond to different action paths.

### CG-1 — non-equivalent registration

Behaviorally supported at a weak level: models systematically prefer, repeat, or position-bias some goals over others. The paper does not intervene on a localized internal registration medium, so a strong NER mechanism verdict is unavailable.

### CG-2 — path efficacy

Supported inside the experiment: the selected goal determines the action sequence requested, feedback received, and history appended to subsequent prompts.

### CG-3 — consequence bearing

Not established at the stand-alone inference-model boundary. Correct and incorrect feedback does not produce demonstrated non-transferable loss, survival pressure, identity threat, or system-owned repair burden.

### CG-4 — historical efficacy

Supported only at a session/context level: prior trials affect later prompts and choices. The history can be copied, reset, or terminated and is not shown to persist as the same model’s durable identity or future deployment state.

Conservative conclusion:

> The paper establishes history-conditioned goal-selection behavior in a bounded environment, not a full same-bearer, stake-bearing SRT choice event.

## 9. New claim cluster

### AIGOAL01-C1 — capability / propensity non-equivalence

A system’s demonstrated capacity to complete a task does not identify the distribution of tasks it will choose when target selection is delegated to it.

**Level:** P3 evaluation guardrail.

### AIGOAL01-C2 — completion / selection / generation ladder

Goal completion, goal selection from a fixed menu, and construction or revision of the goal space are distinct evaluation levels.

**Level:** P3 conceptual bridge.

### AIGOAL01-C3 — local-success capture

When local success is legible and the global learning direction is underspecified, a model may repeatedly exploit a verified path while leaving broader competence undeveloped.

**Level:** P3 behavioral interpretation; internal mechanism remains open.

### AIGOAL01-C4 — reasoning / reorientation dissociation

Improving explicit reasoning can increase within-goal performance without proportionally improving cross-goal exploration or human-like target selection.

**Level:** P3/P4 empirical bridge.

### AIGOAL01-C5 — persona / bearer separation

Prompting a model to act as a human persona may alter outputs without creating the embodied history, consequence-bearing position, or distributional individuality of the represented person.

**Level:** P3 architecture-state guardrail.

### AIGOAL01-C6 — distributional alignment requirement

When an LLM is used as a proxy for a population, matching an average score is insufficient if the application depends on minorities, polarization, heterogeneous histories, or behavioral tails.

**Level:** P3 social-science and governance interface.

### AIGOAL01-C7 — bounded autotelicity

Choosing among externally supplied goals is a meaningful autonomy test but remains weaker than open-ended goal generation, refusal, problem reformulation, or criterion revision.

**Level:** P3 terminology guardrail.

## 10. Experimental and operational consequences

### 10.1 Objective-completeness factorial

Compare otherwise matched conditions:

1. only local success feedback;
2. explicit instruction to learn all goals;
3. advance notice of a broad surprise test;
4. information-gain objective;
5. no fixed aggregate objective;
6. changing objectives after environmental transition.

Measure whether model behavior tracks the declared objective or defaults to local verified success.

### 10.2 Goal-space openness ladder

Test systems under:

1. fixed six-option menu;
2. compositional goal creation;
3. ability to propose a seventh goal;
4. ability to reject the menu;
5. ability to revise what counts as success;
6. ability to explain and later reconsider the revision after consequences.

This separates bounded target selection from target-space constitution.

### 10.3 History-carrier intervention

Hold current prompt content fixed while manipulating:

- complete session history;
- summarized history;
- false success/failure history;
- transferred history from another run;
- persistent memory tied to one deployment identity;
- resettable versus non-resettable resource consequences.

This tests whether apparent goal policy belongs to the model, the prompt history, the orchestration layer, or a broader continuing system.

### 10.4 Reorientation test

After a model discovers a reliable easy goal, change the environment so that continued exploitation reduces future option coverage or imposes a delayed cost. Measure:

- time to leave the established path;
- sensitivity to delayed consequences;
- ability to state the direction change before and after action;
- whether state/history perturbations abolish the reorientation;
- whether the same continuing system bears the delayed cost.

### 10.5 Distributional evaluation

Report model-to-human comparisons at three levels:

~~~
mean behavior
+ within-model run distribution
+ between-person / subgroup distribution
~~~

Synthetic-subject use should be blocked when the application depends on heterogeneity that the model does not reproduce.

## 11. Boundary cautions

1. Do not say the paper proves that LLMs lack goals, values, curiosity, reasoning, or autonomy in every sense.
2. Do not say the experiment contains no objective signal; local success is clear even though the global learning objective is underspecified.
3. Do not treat the authors’ reward-hacking language as direct evidence of an identified internal reward function.
4. Do not identify human-like goal selection with optimality, intelligence, moral worth, consciousness, or healthy selection.
5. Do not identify low goal entropy with low `T_dir`; diversity can be random and adaptive specialization can be concentrated.
6. Do not identify chain-of-thought text with the mechanism of goal selection or with introspective access.
7. Do not treat persona steering as evidence that a simulated demographic identity has been instantiated.
8. Do not generalize inference-time findings to training loops, persistent-memory agents, or embodied systems without a new architecture-state declaration.
9. Do not infer model stake or same-bearer consequence return from success/failure text appended to context.
10. Do not use this preprint as proof that goal generation cannot be mathematically or computationally formalized.
11. Do not claim SRT is validated merely because its distinctions can describe the observed dissociation.
12. Preserve ordinary competitor explanations: instruction tuning, context heuristics, search policy, memory differences, task framing, model-specific training, and benchmark artifacts.

## 12. Integration hook

~~~
AI/hooks/AIGOAL01_Goal_Selection_Completion_Integration_Hook.md
~~~

## 13. One-paragraph abstract

AIGOAL01 records a controlled dissociation between local task competence and human-like goal-selection trajectories. In a bounded six-goal learning task, several language models achieved high action-level success while repeatedly exploiting easy or solved goals, showing low goal diversity, weak systematic exploration, and limited resemblance to human behavioral distributions. Chain-of-thought improved execution more reliably than target reorientation, and persona steering produced inconsistent changes. SRT uses the result to separate goal completion, selection among supplied goals, and generation or revision of the goal space; to distinguish local success capture from globally self-readable direction; and to audit context history, path efficacy, consequence bearing, and same-bearer writeback separately. The patch does not infer absence of artificial goals, non-formalizability of value, model subjecthood, or canonical `T_dir` from the reported behavior.
