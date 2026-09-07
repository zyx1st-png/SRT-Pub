---
id: SRC-2026-09-07-NEURO-OSAKO-REUSABLE-MODULAR-ARCHITECTURE
source_id: SRC-2026-09-07-NEURO-OSAKO-REUSABLE-MODULAR-ARCHITECTURE
type: material_source_card
status: active
layer: materials
epistemic_layer: evidence
claim_mode: evidence
canonical: false
title: "Reusable modular architecture enables flexible cognitive operations in the mouse brain and artificial recurrent networks"
source_type: peer_reviewed_primary_research
domain: neuroscience_population_dynamics_working_memory_modularity
authors: "Yuma Osako; Greggory R. Heller; Sofie Ährlund-Richter; Timothy J. Buschman; Mriganka Sur"
publication: "Nature Neuroscience"
date_received: "2025-09-09"
date_accepted: "2026-07-13"
date_published: "2026; exact online date not populated in supplied PDF"
date_added: "2026-09-07"
doi: "10.1038/s41593-026-02410-0"
url: "https://doi.org/10.1038/s41593-026-02410-0"
evidence_level: peer_reviewed_mouse_electrophysiology_population_geometry_plus_data_constrained_rnn_perturbation
reliability_level: high_for_reported_task_specific_reuse_and_population_geometry_bounded_for_cluster_level_in_vivo_causality
content_access: "User-supplied 31-page Nature Neuroscience PDF; close-read from supplied primary paper"
srt_relevance: very_high
integration_priority: high
related_srt_claims:
  - N1_neural_object_state_representation_identity
  - N2_historical_ownership_present_efficacy
  - N3_relational_distributed_organization
  - N5_measurement_objectification_decoding
  - N6_bearer_consequence_attribution
  - PH_IND02
  - PH_IND03
  - Cycle1_One_Bearer_genesis
  - Cycle2_two_sided_Selection_One_formation
  - NEURAL18_decodability_anchoring_guardrail
tags: [NeuralReuse, Modularity, ComputationalReuse, RepresentationalReuse, WorkingMemory, mPFC, PPC, Neuropixels, NeuralSubspace, FunctionalClusters, RNN, TrainingHistory, Objectification, Bearer, OneFormation]
---

# SourceCard — Osako et al. 2026, reusable modular neural architecture

## 1. One-line summary

Osako et al. report that mice performing a delayed match-to-sample with delayed report task reuse neural population subspaces for both stimulus representation and memory maintenance, with the mPFC showing a particularly strong content-independent reusable memory subspace; functional clustering and data-constrained RNN perturbations are consistent with a modular architecture, while training history biases the geometry of the reusable memory representation.

---

## 2. Source-native conceptual distinction

The paper explicitly distinguishes two forms of reuse:

```text
representational reuse
= repeated engagement of neural circuitry to encode the same type of information
  across different contexts / task epochs

computational reuse
= engagement of the same neural circuitry to perform the same type of computation
  across different task epochs even when the processed information changes
```

This distinction is load-bearing for SRT-side reading because it separates:

```text
same represented content
from
same reusable operation
```

The paper does not identify either of these with an ontological One, Bearer, subject, or SRT Selection-position.

---

## 3. Core source-backed findings

### 3.1 Task and recordings

Mice performed a delayed match-to-sample with delayed report task using two sequential auditory tones separated by two memory delays. The study recorded neuronal activity in medial prefrontal cortex (mPFC) and posterior parietal cortex (PPC) and analyzed population-level coding geometry across stimulus, delay, and report epochs.

Regional mPFC/PPC perturbation in animals showed that these areas are broadly required across task epochs. This is distinct from the later cluster-specific perturbation analysis, which is performed in data-constrained RNNs rather than as a direct cell-cluster-specific in-vivo lesion.

### 3.2 Representational reuse

A classifier trained on the neural population during one stimulus epoch generalized to the other stimulus epoch. The shared stimulus subspace also generalized into passive listening blocks.

Bounded source claim:

```text
same stimulus-processing geometry can be reused across time / context
```

This supports representational reuse, not numerical identity of a neural object or bearer.

### 3.3 Computational reuse in memory maintenance

During Delay 1 the animal had to maintain sensory-stimulus information; during Delay 2 it had to maintain information about the upcoming behavioral choice. In mPFC, classifiers trained on one delay generalized across these different memory contents, and greater overlap of the memory-maintenance subspaces was associated with better behavioral performance.

Bounded source claim:

```text
same memory-maintenance computation
can operate on different contents
```

The effect was stronger in mPFC than PPC.

### 3.4 Functional clustering is task- and region-dependent

The authors report non-uniform functional organization and identify neuronal clusters with different response profiles. In mPFC, distinct subpopulations contributed strongly to stimulus processing versus memory maintenance. PPC showed more multiplexed participation, with cluster-to-functional-subspace relations less nearly one-to-one.

The study therefore does not support a simple universal rule that functional computation is always implemented by cleanly segregated fixed modules.

### 3.5 Data-constrained RNN perturbation

RNNs were trained to reproduce the measured mPFC neural dynamics. In silico silencing of the putative stimulus-processing cluster impaired performance when applied during stimulus epochs; silencing the putative memory-maintenance cluster impaired performance during delay epochs. Silencing the connection from the stimulus cluster to the memory cluster during stimulus epochs also impaired performance.

Safe interpretation:

```text
RNN perturbation supports a candidate modular circuit mechanism
consistent with the observed neural population structure
```

Do not rewrite this as:

```text
cell-cluster-specific in-vivo causal proof of the proposed module architecture
```

### 3.6 Training history sculpts representational geometry

The orientation of coding directions in the memory-maintenance subspace was associated with the sequence of task training. The authors reproduced this history dependence in RNNs by varying pre-training histories.

Safe source claim:

```text
training history can bias the geometry of a reusable neural computation
```

This is ordinary learned-history sensitivity unless an additional discriminator is independently shown.

---

## 4. Main source limits

1. The study concerns mice in one highly structured delayed match-to-sample task; generalization to naturalistic cognition, other species, and other task regimes remains open.
2. Functional modularity is region- and task-dependent: mPFC is more cleanly modular in this study, while PPC is more multiplexed.
3. The paper itself notes that the discrepancy with prior reports of nonmodular organization may reflect task demands, especially flexible input-output mapping.
4. Whether the observed functional clusters are learned or pre-existing remains open.
5. Population classifiers and subspace geometry identify information structure and reuse but do not by themselves establish bearer identity, causal ownership, subjecthood, phenomenality, or numerical identity.
6. Cluster-specific causal perturbation is performed in a data-constrained RNN; the authors explicitly leave time-specific in-vivo manipulation of the corresponding animal clusters for future work.
7. Training-history effects are reproduced by ordinary RNN learning, so history sensitivity itself is not an SRT-specific residual.

---

## 5. GOV-SYN01 contribution separation

### Layer A — source-backed evidence / pressure

Claimed:

- representational reuse of stimulus-processing subspaces;
- computational reuse of a memory-maintenance subspace across different contents, especially in mPFC;
- functional clustering associated with stimulus versus memory computations;
- mPFC/PPC difference between stronger modularity and more multiplexed organization;
- task-specific relation between shared memory subspace and behavioral performance;
- training-history bias of coding geometry;
- data-constrained RNN lesion evidence consistent with modular function and inter-module dependence.

### Layer B — SRT-side bounded synthesis

Permitted only as separately marked interpretation:

- `same computation != same represented content != same bearer`;
- a continuing functional locus need not be a fixed membership set;
- functional/module identity and bearer/One identity must be separately earned;
- history-shaped geometry is a generic-learning baseline, not SRT evidence;
- reusable computation is a useful negative control for SRT claims that infer One/Bearer from stable function or repeated representation;
- Osako should be read together with NEURAL18 / Posani: local functional clustering can depend strongly on task and scale, while decodability or clustering still does not establish anchoring or bearer status.

### Layer C — discriminating empirical increment

**None claimed in this pass.**

The paper does not provide a matched SRT-versus-rival test of:

- One/Bearer formation;
- consequence ownership;
- primitive bearerless Selection;
- Selection-position formation;
- an SRT-specific history variable beyond ordinary recurrent learning;
- phenomenality or subjecthood.

---

## 6. Framework routing

Primary routing under `Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md`:

```text
N1 — neural object / state / representation identity
N2 — historical retention / present efficacy
N3 — relational / distributed organization
N5 — measurement objectification / decoding / subspace construction
N6 — bearer / consequence attribution
```

Secondary pressure:

```text
N4 — current processability / reusable computational capacity
```

No active neuroscience deep well is opened by this SourceCard.

---

## 7. Cycle-1 / Cycle-2 subtraction preview

### Cycle 1

The paper strengthens the generic baseline:

```text
training history
-> present representational geometry
-> later task performance
```

and shows this form can be reproduced in ordinary RNN learning. Therefore it pressures, rather than rescues, any Cycle-1 attempt to treat history-conditioned state or reusable memory dynamics as an independent SRT-specific Bearer-genesis discriminator.

### Cycle 2

Functional specialization, modular reuse, distributed/multiplexed organization, and history-shaped geometry can all arise in ordinary neural/RNN dynamics. They do not establish the Cycle-2 residual of primitive bearerless Selection or the genetic formation of a continuing Selection-position / One.

A reusable functional module is therefore a useful **neighbor / negative control**, not a synonym for One.

---

## 8. Hard guardrails

Do not write:

```text
Osako et al. prove SRT
memory subspace = ontological One
functional cluster = Bearer
same computation = same bearer identity
training-history bias = SRT history ownership
RNN cluster lesion = direct cluster-specific in-vivo causal proof
mPFC modularity is a universal cortical architecture
neural subspace reuse proves Selection sedimentation
computational reuse proves subjecthood or consciousness
```
