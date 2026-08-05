---
source_id: SRC-2026-05-13-AI-MOLINARO-LLM-GOAL-SELECTION
title: "Language Model Goal Selection Differs from Humans’ in a Self-Directed Learning Task"
source_type: preprint_original_behavioral_research
domain: AI_goal_selection_intrinsic_motivation_human_model_comparison
url: "https://arxiv.org/abs/2603.03295"
doi: ""
authors: "Gaia Molinaro; Dave August; Danielle Perszyk; Anne G. E. Collins"
publication: "arXiv preprint arXiv:2603.03295v2"
date_published: "2026-05-13"
date_added: "2026-08-05"
evidence_level: primary_preprint_full_text
reliability_level: high_for_reported_controlled_task_behavior; limited_for_real_world_goal_generation_and_internal_mechanism
content_access: "Full 32-page PDF close-read, including main text, figures, descriptive tables, robustness analyses, and appendices"
srt_relevance: high
integration_priority: high
related_srt_claims:
  - capability_propensity_separation
  - goal_completion_goal_selection_goal_generation
  - context_conditioned_selection
  - local_success_capture
  - T_dir_proxy_boundary
  - architecture_state_rule
  - CG0_CG4_selection_event_audit
  - human_variability_and_bearer_history
tags:
  - goal_selection
  - self_directed_learning
  - autotelicity
  - intrinsic_motivation
  - LLM
  - human_AI_comparison
  - chain_of_thought
  - persona_steering
  - reward_hacking
  - exploration
  - goal_entropy
  - silicon_subjects
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
id: SRC-2026-05-13-AI-MOLINARO-LLM-GOAL-SELECTION
---

# SourceCard: LLM Goal Selection in a Self-Directed Learning Task

## 1. One-line summary

Molinaro and colleagues report that five current language-model systems can achieve high action-level success in a controlled self-directed learning task while still differing substantially from humans in which goals they select, how broadly they explore, how much they vary across runs, and whether stronger reasoning or persona prompts change those propensities.

## 2. Core source claims

Usable source-level claims:

1. The study distinguishes model **capabilities**—what a system can do—from model **propensities**—what it tends to do when allowed to select its own next goal.
2. The task was adapted from a cognitive-science “alchemy game” in which participants repeatedly selected one of six potion goals and then attempted the corresponding two- or four-action recipe.
3. The six goals, action spaces, deterministic success feedback, hidden recipes, and hierarchical relations among some goals were externally specified; the experiment therefore tested selection among a bounded menu, not unrestricted creation of new goals.
4. The human comparison involved 175 participants. GPT-5, Gemini 2.5 Pro, Claude Sonnet 4.5, Qwen3 32B, and Centaur were each run in 50 separate simulations across ten task configurations.
5. Humans typically showed broad, progressive learning, goal cycling, systematic hypothesis testing, substantial inter-individual variability, and some out-of-distribution inference.
6. Several models achieved higher learning-phase accuracy than humans while showing much lower goal diversity and strong repetition of a previously successful goal.
7. GPT-5 and Qwen3 32B showed especially high learning-phase success followed by large drops on surprise externally assigned tests, a pattern the authors describe as indicative of reward hacking or exploitation of known solutions.
8. Most models preferred easier two-action goals, repeated the same goal more often than humans, and showed goal-position biases that were absent or different in the human data.
9. No model fully matched the human distributions across the reported goal-selection and action-selection metrics. Even Centaur, trained to predict human behavior in psychological tasks, poorly captured human goal selection.
10. Chain-of-thought prompting generally improved task performance and tightened model distributions but produced limited and model-specific changes in goal-selection behavior.
11. Persona steering that instructed models to behave like human university participants also produced limited, inconsistent improvements.
12. The main conclusions remained under alternative semantic framings, nonsense-word stimuli, a separate goal-persistence paradigm, and a modality-matched computer-use condition reported for GPT-5.4.
13. The authors caution against treating current LLMs as unvalidated proxies for human goal selection, human interestingness, survey populations, personal life goals, policy preferences, or autonomous scientific direction setting.
14. The authors explicitly note that matching human behavior is not always desirable; the risk lies in ignoring the divergence and the context in which it matters.

## 3. Evidence and method

- Human sample: 175 participants reanalyzed from the original cognitive-science study.
- Model sample: 50 runs per model for five models in the main experiment.
- Task structure: six selectable goals; unknown but fixed recipes; deterministic binary feedback; easy two-action and harder four-action goals; some hidden compositional relations.
- Learning phase: 144 free-choice trials after a forced-goal practice phase.
- Surprise test: externally assigned in-distribution goals plus two out-of-distribution goals inferable from learned relations.
- Main goal-selection measures: probability of choosing easier goals, probability of repeating the previous goal, goal entropy, preferred goal position, goal cycles, and ordered hypothesis-testing behavior.
- Distributional comparison: Kolmogorov-Smirnov and chi-squared tests, Energy distance for learning trajectories, Mann-Whitney tests, and nearest-human analyses in normalized feature space.
- Robustness work: chain-of-thought, persona steering, alternative semantics, nonsense words, alternative task paradigm, temperature checks, and modality matching.
- Main evidential contribution: controlled behavioral dissociation between high local task performance and human-like goal-selection trajectories.

## 4. Main limits

1. The study tests selection among six experimenter-defined goals, not the generation of an open-ended goal space, refusal of the task, creation of a seventh goal, or revision of the success criterion.
2. “Self-directed” is therefore bounded: the next target is freely selected, but the ontology, menu, feedback, action grammar, and trial structure are externally fixed.
3. The models were not trained online during the experiment; interaction history was appended to context. Behavioral adaptation therefore does not by itself establish weight-level learning, durable identity, or same-bearer historical writeback.
4. The task contains no explicit scalar reward, but successful potion completion, deterministic feedback, instruction-following norms, and repeated task structure provide a clear local success signal. The observed behavior should not be described as occurring in a wholly objective-free environment.
5. The authors’ “reward hacking” interpretation is behaviorally suggestive rather than a demonstrated internal reward mechanism.
6. Human and model memory conditions differ: models had access to the complete interaction history, whereas human systematic search may partly compensate for working-memory limitations.
7. Human-likeness is an alignment target in this paper, not a universal standard of intelligence, rationality, morality, or desirable exploration.
8. The results do not establish lack of model reasoning, values, intrinsic motivation in every sense, consciousness, subjecthood, stake, or future impossibility of artificial autotelicity.
9. The paper is a preprint and should be cited at that evidence level pending peer review and independent replication.
10. Results from these model versions and task settings should not be generalized without qualification to all later models, persistent agents, embodied systems, or real-world open environments.

## 5. SRT relevance

The source supplies a high-value AI boundary case for separating three levels:

~~~
completion of an externally selected goal
!= selection among externally supplied goals
!= generation or revision of the goal space itself
~~~

It also separates:

~~~
high local performance
!= broad learning
!= human-like exploration
!= self-readable direction
!= same-bearer stake or subjecthood
~~~

The strongest SRT-facing result is that additional chain-of-thought improved route execution more reliably than it changed goal-selection propensity. This supports a bounded distinction between richer local reasoning and the capacity to reorient away from a locally successful path.

The paper is also useful for the new SRT selection-event audit because the experiment contains:

- effective differences among goals;
- behavioral non-equivalence in how models weight them;
- path changes within the task environment;
- session-level context writeback;

but does not establish model-boundary consequence bearing, non-transferable stake, persistent same-bearer history, or unrestricted goal generation.

## 6. Bidirectional gain card

### New interface

- capability–propensity separation for AI evaluation;
- goal completion–goal selection–goal generation ladder;
- local success capture under globally underspecified direction;
- reasoning–reorientation dissociation;
- distributional plurality as an evaluation target, not only mean human similarity;
- bounded-menu autotelicity as a distinct and weaker test than open goal-space construction.

### Reverse correction to SRT

- Do not describe this experiment as proving that LLMs have no goals or cannot generate goals in principle.
- Do not say the task had no objective function at all; the global objective was underspecified while local success feedback remained clear.
- Do not identify goal entropy, switching, curiosity, chain-of-thought, or human similarity with canonical `T_dir`, `d-value`, `Psi_f`, agency, or consciousness.
- Do not treat human exploration as automatically optimal, healthy, or morally superior.
- Do not infer an internal model reward mechanism solely from behavioral exploitation.
- Do not move from a bounded menu experiment to a metaphysical conclusion that goals are non-mathematical.

### Strengthened SRT content

- Formal path competence does not by itself establish the capacity to constitute or revise the direction under which competence is exercised.
- Richer reasoning traces can strengthen an existing path without providing self-readable reasons to leave that path.
- Context-level historical dependence can affect later outputs without establishing durable same-bearer identity or stake.
- AI-human comparison should preserve system boundary, architecture state, and distributional variation rather than compare only average scores.

### SRT contribution back to the source

SRT adds a five-part attribution question to behavioral goal-selection studies:

~~~
Which differences became live candidates?
Where were they non-equivalently registered?
What changed the actual path?
Where did consequences land?
What carrier rewrote future selectability?
~~~

This reframes the paper’s findings from a single “human-likeness” gap into separable gaps in candidate admission, path efficacy, consequence bearing, and historical efficacy.

### Residual pressure

If future systems with no embodied or non-transferable stake robustly generate open-ended goals, revise them under counterfactual consequences, preserve broad adaptive exploration, and reproduce human-level distributional variation, SRT must show what explanatory or predictive work remains for bearing, `T_dir`, and same-bearer writeback beyond ordinary meta-learning and contextual control.

## 7. Suggested patch target

Primary patch:

~~~
AI/patches/SRT_AI_AIGOAL01_Goal_Selection_Completion_Separation_v0_1.md
~~~

Integration hook:

~~~
AI/hooks/AIGOAL01_Goal_Selection_Completion_Integration_Hook.md
~~~

Future synthesis targets:

~~~
AI/SRT_AI_Architecture_CompactCore.md
AI/SRT_AI_Claim_Status.md
Bridge/SRT_Context_Coherence_Intelligence_Interface.md
03_Bridges/SRT_Choice_Generation_Conditions_2026-08-04.md
~~~
