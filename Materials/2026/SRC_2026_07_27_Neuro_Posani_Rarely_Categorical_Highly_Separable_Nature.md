---
source_id: SRC-2026-07-27-NEURO-POSANI-RARELY-CATEGORICAL-HIGHLY-SEPARABLE-NATURE
title: "Rarely categorical, highly separable representations along the cortical hierarchy"
source_type: Nature_open_access_peer_reviewed_article
domain: neuroscience_population_coding
url: "https://doi.org/10.1038/s41586-026-10668-4"
doi: "10.1038/s41586-026-10668-4"
authors: "Lorenzo Posani; Shuqi Wang; Samuel P. Muscinelli; Liam Paninski; Stefano Fusi"
publication: "Nature"
date_received: "2025-02-13"
date_accepted: "2026-05-15"
date_published: "2026; exact online date not populated in supplied PDF"
date_added: "2026-07-27"
evidence_level: peer_reviewed_open_access_original_research
reliability_level: high_for_mouse_cortical_population_geometry_and_decodability_guardrail
content_access: "User-supplied 35-page Nature PDF; full-text close-read"
srt_relevance: very_high
integration_priority: high
related_srt_claims:
  - neural_manifold
  - candidate_capacity
  - selection_ready_geometry
  - decodability_anchoring_distinction
  - L0_accessible
  - L1_anchoring
  - L2_constraint
  - G_hat_theta
  - d_value
  - Psi_f
  - consciousness_proxy_guardrail
tags:
  - population_coding
  - mixed_selectivity
  - categorical_representation
  - cortical_hierarchy
  - representational_geometry
  - dimensionality
  - linear_separability
  - decodability
  - IBL
  - Neuropixels
  - Nature
status: source_card
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
id: SRC-2026-07-27-NEURO-POSANI-RARELY-CATEGORICAL-HIGHLY-SEPARABLE-NATURE
---

# SourceCard: Rarely Categorical, Highly Separable Cortical Representations

## 1. One-line summary

Posani, Wang, Muscinelli, Paninski, and Fusi show across 43 mouse cortical regions that single-region neuronal selectivity is usually diverse rather than clustered into fixed functional categories, while this diversity supports high-dimensional and highly linearly separable population representations; large-scale categorical organization reappears when regions or cortical modules are pooled.

## 2. Core source claims

Usable source-level claims:

1. The authors analyze more than 14,000 cortical units from the International Brain Laboratory Brainwide Map dataset across 43 cortical regions during a sensory-decision task.
2. A reduced-rank regression encoding model represents each neuron's time-varying sensitivity to eight task and behavioral variables: block prior, stimulus side, contrast, choice, outcome, wheel velocity, whisking power, and licking.
3. Average selectivity profiles differ across cortical regions and covary with large-scale anatomical connectivity.
4. The number of independently decodable task conditions increases along the sensory-cognitive cortical hierarchy.
5. Within individual cortical regions, statistically robust categorical clustering of neuronal response profiles is rare and is concentrated mainly in early sensory areas.
6. When neurons are pooled across anatomical modules or the whole cortex, categorical structure becomes stronger and partially aligns with anatomical region or module labels.
7. The authors introduce alpha-diversity, defined through the participation ratio of selectivity-coefficient distributions, to capture both uneven selectivity and categorical clustering.
8. Higher alpha-diversity is associated with higher representational dimensionality and greater linear separability of experimental-condition dichotomies.
9. After restricting analysis to conditions that are actually independently encoded by each area, nearly all cortical regions exhibit maximal or near-maximal separability.
10. Therefore, successful linear decoding from a population does not by itself establish that the decoded variable is uniquely privileged, functionally used, selected, or consciously represented.

## 3. Evidence and method

- Dataset: IBL Brainwide Map, Neuropixels recordings from mice performing a visually guided wheel-turning decision task.
- Spatial scope: 43 cortical regions; approximately 180 recording sessions before selectivity filtering.
- Encoding model: reduced-rank regression with shared temporal bases and neuron-specific coefficients.
- Selectivity space: time-summed coefficients for eight variables; time-varying variants were also tested.
- Clustering test: k-means or alternative clustering, silhouette score, and a covariance-matched unimodal Gaussian null model; session-dominated clusters were excluded.
- Population geometry: participation ratio, number of independent conditions, and cross-validated linear decoding.
- Separability: fraction of balanced condition dichotomies whose linear-decoder accuracy exceeds a shuffled-label null threshold.
- Robustness: alternative inclusion thresholds, clustering methods, time-varying profiles, condition-space analyses, and ePAIRS-style tests.

## 4. Main limits

1. The task contains a limited set of experimentally chosen sensory, motor, cognitive, and decision variables; unmeasured variables can alter inferred selectivity structure.
2. The full separability analysis is conditioned on a specific set of 16 binary condition combinations and on the conditions that each area can independently decode.
3. Linear separability is an analyst-defined capacity measure. It does not show that the animal or a downstream circuit actually uses every separable dichotomy.
4. The study is not a causal perturbation test of which readouts drive behavior, report, memory, or conscious access.
5. Data are from mice in one structured task; generalization to naturalistic behavior, other species, other cortical states, and non-cortical systems remains open.
6. Alpha-diversity and participation ratio are geometric summaries, not direct measurements of SRT's `L_0`, `L_1`, `L_2`, `d-value`, `Psi_f`, subjecthood, or consciousness.
7. The paper supports a population-coding and proxy-hygiene bridge, not SRT ontology.

## 5. SRT relevance

The material gives SRT a high-value distinction between **selection-ready representational capacity** and **actual reality anchoring**:

```text
high-dimensional / highly separable neural geometry
  = many potentially implementable distinctions or readouts
  != one distinction being selected, stabilized, acted on, or sedimented
```

The strongest bridge is:

```text
decodable
  != causally accessible
  != behaviorally selectable
  != consciously anchored
  != written back into L2
```

This source also forces a correction to overly literal compression language:

```text
L0-accessible -> L1 anchoring
  does not require
high-dimensional neural activity -> low-dimensional or categorical neural code
```

A single stable perception, judgment, or action can remain implemented by a high-dimensional distributed population state. SRT selection narrows effective commitment and consequence-bearing trajectories; it need not collapse neural embedding dimensionality.

## 6. Bidirectional gain card

### New interface

- `selection-ready geometry`: a measurable capacity layer described by diversity, independent-condition count, dimensionality, and separability.
- `decodability-anchoring dissociation`: an experimental window separating represented capacity from causal use, behavior, report, persistence, and write-back.
- multiscale organization: within-region diversity can coexist with module-level categorical structure.

### Reverse correction to SRT

- Do not equate high dimensionality with `L_0` itself.
- Do not equate low dimensionality or clustering with `L_1` anchoring.
- Do not treat a linear decoder as an implementation of `G_hat_theta` without causal, gating, consequence, and history evidence.
- Do not describe selection as necessarily reducing neural-state dimensionality.
- Do not infer `d-value`, `Psi_f`, consciousness, or subjecthood from decoding accuracy alone.

### Strengthened SRT content

- Neural states are continuous trajectories on population manifolds rather than fixed semantic labels.
- Local diversity and global anatomical organization are compatible across scale.
- Existing structure constrains future selection without requiring rigid within-region cell categories.
- SRT's added work can be stated more sharply: explain why one usable division becomes behaviorally and historically effective among many decodable divisions.

### SRT contribution back to the source

SRT can extend the source's geometry-capacity chain:

```text
diversity -> dimensionality -> separability
```

into a testable selection chain:

```text
selection-ready geometry
+ concern weighting
+ anchoring friction
+ historical constraint
+ gating / stabilization
-> actual behavioral or conscious anchoring
-> consequence-dependent L2 write-back
```

### Residual pressure

- The paper may support a simpler downstream-readout account in which `d-value`, `Psi_f`, and `L2` add no independent explanatory value.
- SRT must demonstrate residual prediction beyond geometry, task difficulty, reward, salience, uncertainty, and ordinary learning.
- If decodability and standard causal readout models fully predict persistence, switching, action, memory, and history dependence, the SRT neural bridge must narrow.

## 7. Suggested patch target

Primary targets:

```text
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
Neuroscience/SRT_Neuro_Predictions_Table.md
Neuroscience/SRT_Neuro_Axioms_Claim_Status.md
```

Patch record:

```text
Neuroscience/patches/SRT_Neuro_NEURAL18_Selection_Ready_Geometry_Decodability_Anchoring_Gate_v0_1.md
```
