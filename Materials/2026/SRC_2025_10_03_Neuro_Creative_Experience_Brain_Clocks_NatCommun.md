---
source_id: SRC-2025-10-03-NEURO-CREATIVE-EXPERIENCE-BRAIN-CLOCKS-NATCOMM
title: "Creative experiences and brain clocks"
source_type: peer_reviewed_open_access_original_research
domain: neuroscience_plasticity
url: "https://www.nature.com/articles/s41467-025-64173-9"
doi: "10.1038/s41467-025-64173-9"
authors: "Carlos Coronel-Oliveros; Joaquin Migeot; Fernando Lehue; et al."
publication: "Nature Communications 16, Article 8336"
date_published: "2025-10-03"
date_added: "2026-05-09"
evidence_level: peer_reviewed_full_text_open_access
reliability_level: high_for_reported_associations_medium_for_causal_generalization
content_access: "Full HTML and PDF available from Nature; code/data links available for most cohorts"
srt_relevance: high
integration_priority: high
related_srt_claims:
  - creative_experience
  - brain_age_gap
  - functional_connectivity_brain_clock
  - neural_plasticity
  - local_efficiency
  - global_coupling
  - L2_learning
  - selection_mobility
tags:
  - creativity
  - brain_clock
  - M_EEG
  - functional_connectivity
  - plasticity
  - expertise
  - learning
  - Nature_Communications
status: source_card
---

# SourceCard: Creative Experiences and Brain Clocks

## 1. One-line summary

Coronel-Oliveros and colleagues report that creative expertise and short-term creative learning are associated with lower functional-connectivity brain-age gaps, with effects linked to local efficiency, age-vulnerable hubs, and biophysical coupling.

## 2. Core claims of source

The paper builds M/EEG functional-connectivity brain clocks from `N=1240` participants and applies them to `N=232` participants across dance, music, visual arts, strategy video gaming, and short-term StarCraft II learning.

Usable source-level claims:

1. creative experts showed lower brain-age gaps than matched non-experts across domains;
2. short-term StarCraft II learning also lowered BAGs relative to baseline, with an active-control comparison;
3. higher expertise or performance related to lower BAGs;
4. age-vulnerable frontoparietal and related hubs showed increased connectivity linked to creative experience;
5. lower BAGs were associated especially with local efficiency, and in long-term expertise also with global efficiency and global coupling.

## 3. Evidence / method

- Article type: peer-reviewed original research, open access.
- Training sample: EEG functional connectivity from `N=1240` participants.
- Out-of-sample creative-experience sample: `N=232`.
- Model: machine-learning brain clocks using M/EEG functional connectivity, graph theory, Neurosynth meta-analytic maps, and whole-brain modeling.
- Reported main contrast: expertise effects were larger than short-term learning effects.

## 4. Limits

1. BAG is a functional-connectivity brain-clock proxy, not literal biological rejuvenation.
2. Cross-sectional expertise contrasts cannot by themselves prove lifelong causality or eliminate selection effects.
3. The pre/post learning study is stronger causally but smaller and task-specific.
4. EEG simulations from DTI structural data are approximations and require caution.
5. The result does not prove that creativity is uniquely protective beyond cognitively demanding, embodied, feedback-rich practice.

## 5. SRT relevance

The material strengthens SRT's learning/plasticity bridge:

```text
creative practice
  -> repeated high-dimensional novelty under feedback
  -> theta / L2 reconfiguration
  -> altered functional-connectivity topology
  -> lower BAG_FC proxy
```

Its most useful SRT contribution is a measurable window for the idea that learning is not only memory accumulation, but rewrites the future selection landscape. It also corrects a simple "expertise = rigid L2" reading: creative expertise can harden skill while preserving or improving functional-network mobility.

## 6. Suggested patch target

Primary target:

```text
Neuroscience/SRT_Neural_Mechanisms.md
```

Patch record:

```text
Neuroscience/patches/SRT_Neuro_NEURAL15_Creative_Experience_Brain_Clock_v0_1.md
```
