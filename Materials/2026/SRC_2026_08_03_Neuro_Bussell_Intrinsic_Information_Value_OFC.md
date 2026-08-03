---
source_id: SRC-2026-08-03-NEURO-BUSSELL-INTRINSIC-INFORMATION-VALUE-OFC
title: "Representations of the intrinsic value of information in mouse orbitofrontal cortex"
source_type: peer_reviewed_open_access_original_research
domain: neuroscience_information_seeking_value_representation
url: "https://www.nature.com/articles/s41593-026-02377-y"
doi: "10.1038/s41593-026-02377-y"
authors: "Jennifer J. Bussell; Ryan P. Badman; David Márton; Ethan S. Bromberg-Martin; L. F. Abbott; Kanaka Rajan; Richard Axel"
publication: "Nature Neuroscience"
date_published: "2026-07-30"
date_added: "2026-08-03"
evidence_level: peer_reviewed_open_access_primary_fulltext
reliability_level: high_for_mouse_information_seeking_behavior_and_OFC_population_representation
content_access: "Primary Nature Neuroscience full text close-read; Neuroscience News used only as discovery trail"
srt_relevance: high
integration_priority: high_B1
related_srt_claims:
  - d_value_reward_dissociation
  - information_value
  - uncertainty_reduction
  - T_dir_proxy_guardrail
  - future_selectability
  - value_representation
  - curiosity
tags:
  - information_seeking
  - curiosity
  - intrinsic_value
  - orbitofrontal_cortex
  - microendoscope
  - reinforcement_learning
  - uncertainty
  - Nature_Neuroscience
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
id: SRC-2026-08-03-NEURO-BUSSELL-INTRINSIC-INFORMATION-VALUE-OFC
---

# SourceCard: Intrinsic Information Value in Mouse OFC

## 1. One-line summary

Bussell and colleagues show that mice prefer advance information about a probabilistic water outcome even when the information cannot alter that outcome and can be purchased only by sacrificing water reward; orbitofrontal population activity contains distinguishable representations related to predicted information and predicted water value.

## 2. Core source claims

Usable source-level claims:

1. The authors developed an odor-based task in which one option provides advance information about whether water will arrive and another option provides no such information, while objective reward probability remains equal.
2. Across the main preference task, most mice preferred the information-providing option.
3. The preference survived reversals of the spatial location of the information option for most information-preferring mice.
4. Mice continued to prefer information when choosing it reduced the amount of water available, allowing information value to be expressed in water-equivalent units.
5. Shortening the delay between the predictive cue and reward reduced information preference, linking information value to the duration of uncertainty or anticipation.
6. A reinforcement-learning model fit behavior better when it included distinct value functions or prediction errors for information and water.
7. Microendoscopic calcium imaging recorded 1,138 OFC regions of interest in seven mice during task performance.
8. OFC activity contained representations of cues predicting information and cues predicting water reward.
9. Information and water representations could be demixed at the population level and were not reducible to side or odor identity in the reported analyses.
10. The study establishes a tractable mouse model for information valuation but does not determine why information has value or identify the complete causal circuit that creates that value.

## 3. Evidence and method

- Behavioral sample: 36 mice in the main information-preference analysis.
- Task: odor-guided forced and free-choice trials with matched reward probabilities across information and no-information ports.
- Value tradeoff: water amount at the information port was varied to estimate willingness to pay for information.
- Delay manipulation: interval between information and reward was varied to test sensitivity of information preference to uncertainty duration.
- Modeling: Rescorla-Wagner-style reinforcement-learning models with separate information and water value terms.
- Neural sample: 1,138 OFC ROIs recorded with miniaturized microscopes in seven mice.
- Analyses: coding indices, side-reversal controls, population projections, decoding, and a latent-variable population model.
- Primary result: information value and water value are behaviorally tradeable yet neurally distinguishable within the recorded OFC population.

## 4. Main limits

1. Calling the value "intrinsic" means that the information did not alter the task's reward outcome; it does not establish metaphysical intrinsic value.
2. The behavior may reflect uncertainty aversion, anticipatory affect, learned reinforcement, evolutionary proxy value, or a mixture of these mechanisms.
3. OFC representation is not the same as causal generation of information-seeking behavior; the complete circuit remains unresolved.
4. Population separability does not establish canonical `d`, `T_dir`, consciousness, agency, or subjecthood.
5. Water restriction and a highly trained laboratory task constrain generalization to spontaneous curiosity and human knowledge seeking.
6. The neural imaging sample is smaller than the behavioral sample.
7. Information in this task does not improve action selection or alter the eventual reward, so it cannot be treated straightforwardly as a future-choice-capacity benefit.

## 5. SRT relevance

The source provides strong evidence for a bounded distinction:

```text
represented local value
!=
immediate physiological reward magnitude
```

This is compatible with SRT's rule that canonical `d` must not be reduced to reward, salience, preference strength, or pain. However, the source also creates a genuine pressure point: the mice pay for information that does not alter the available action or final reward outcome.

The material therefore should not be used only as SRT confirmation. It asks:

> Can a system value reduction of uncertainty even when the information does not expand current instrumental choice?

Two live SRT interpretations remain possible:

1. **Historically inherited proxy value**: information seeking retains value because it was generally adaptive across evolutionary or learning history, even in a locally non-instrumental task.
2. **Directional readability value**: reducing uncertainty may locally improve the readability of expected state transitions without increasing option count.

Neither interpretation is established by the paper.

## 6. Bidirectional gain card

### New interface

- `information-water tradeoff`: willingness to sacrifice primary reward for advance information.
- separate learned value channels for information and water.
- a laboratory window for distinguishing reward magnitude, uncertainty duration, and information preference.

### Reverse correction to SRT

- Do not write `d = reward` or `d = information value`.
- Do not infer `T_dir` from preference for predictive cues; the task does not measure self-readable selection direction.
- Do not assume all valued information improves future action or expands choice.
- Do not describe OFC decoding as the origin of value.

### Strengthened SRT content

- Multiple local value dimensions can coexist and compete within one decision architecture.
- A system can pay an immediate bodily cost for a non-bodily cognitive variable.
- External reward and information preference should be separated in experiments claiming to measure concern or direction.

### SRT contribution back to the source

SRT can propose a three-way experimental decomposition:

```text
reward value
vs
uncertainty reduction
vs
future reselection benefit
```

Future variants should manipulate whether information changes later action, whether consequences return to the same bearer, and whether information changes future policy or memory rather than merely anticipation.

### Residual pressure

If information remains strongly valued when it has no instrumental, anticipatory, uncertainty-reducing, social, or learned proxy role, SRT needs a broader account of value than future choice preservation alone.

## 7. Pipeline verdict and revival trigger

**Verdict: B1, with a narrow A-capable guardrail claim.**

Stable narrow claim:

```text
information value and water reward value can be behaviorally traded and neurally distinguished;
therefore reward magnitude alone is not a sufficient local account of value representation.
```

Revival trigger:

> Reopen when the `d-value` stake gate, `T_dir` operationalization, or a new SRT experiment explicitly needs to distinguish reward value, uncertainty reduction, and future-choice benefit.

No PatchNote is created in this pass because the unresolved pressure is as important as the supporting interface.
