---
source_id: SRC-2026-09-16-NEURO-KIYOOKA-SCALE-DEPENDENT-FUNCTIONAL-NETWORKS
id: SRC-2026-09-16-NEURO-KIYOOKA-SCALE-DEPENDENT-FUNCTIONAL-NETWORKS
title: "Single-cell resolution functional networks during unconsciousness are segregated into spatially intermixed modules"
source_type: peer_reviewed_primary_article
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
domain: neuroscience_network_scale_objectification
primary_authors: "Daiki Kiyooka; Ikumi Oomoto; Jun Kitazono; Yoshihito Saito; Midori Kobayashi; Chie Matsubara; Kenta Kobayashi; Masanori Murayama; Masafumi Oizumi"
publication: "Cell Reports 45(2), 116902"
doi: "10.1016/j.celrep.2025.116902"
url: "https://doi.org/10.1016/j.celrep.2025.116902"
date_published: "2026-02-24"
date_added: "2026-09-16"
evidence_level: peer_reviewed_primary_mouse_widefield_two_photon_calcium_imaging_multiscale_network_analysis
reliability_level: high_for_reported_scale_dependent_network_result; moderate_for_generalization_beyond_declared_graph_construction; low_for_consciousness_identity_claims
srt_relevance: high_for_neural_objectification_scale_dependence_and_relational_organization
integration_priority: high
related_srt_claims:
  - neuroscience_objectification
  - graph_construction
  - coarse_graining
  - component_state_vs_organizational_state
  - NEURAL33_boundary
  - N3_relational_organization
  - N5_measurement_objectification
  - Core14_scale_guard
  - consciousness_non_identity
tags: [single-cell, calcium-imaging, network-modularity, coarse-graining, scale, sleep, anesthesia, wakefulness, objectification, graph-construction]
---

# SourceCard: Kiyooka et al. — scale-dependent functional network organization

## 1. Pipeline 1 disposition

```text
Verdict: A — bounded non-canonical empirical/objectification integration
Contribution route: O-track strong; D-track not yet claimed
Primary landing:
  Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
No canonical writeback.
No CompactCore writeback.
No NEURAL34 reopening.
No new SRT scalar / operator / network metric.
```

The source is valuable because its strongest result is not merely that sleep or anesthesia changes cortical network segregation. It shows that the **state contrast itself depends on the spatial / analytic scale at which the network is constructed**.

That makes it a direct empirical pressure on the current Neuroscience Reconstruction Framework question:

```text
measurement / graph construction / node grain
may change which organizational property is observed;
therefore an analyst-defined neural object or scale
must not be treated as a scale-free natural unit by default.
```

This source does **not** prove SRT ontology and does not establish that every scale-dependent result is an objectification artefact. It instead provides a strong empirical case in which objectification choices are load-bearing for the reported network property.

---

## 2. Source-level findings

Primary source:

```text
Kiyooka D, Oomoto I, Kitazono J, Saito Y, Kobayashi M,
Matsubara C, Kobayashi K, Murayama M, Oizumi M. (2026).
Single-cell resolution functional networks during unconsciousness are
segregated into spatially intermixed modules.
Cell Reports 45(2):116902.
DOI: 10.1016/j.celrep.2025.116902
```

The authors use wide-field two-photon calcium imaging of approximately 10,000 cortical neurons across multiple cortical regions in awake, naturally sleeping and isoflurane-anesthetized mice, and compare functional-network structure across spatial scales.

The load-bearing published results are:

1. at **single-cell resolution**, sleep and anesthesia show higher network modularity than wakefulness;
2. single-cell modules remain **spatially intermixed** across states;
3. after coarse-graining to a **mesoscale** description, the state-wise modularity difference is not consistently retained;
4. mesoscale modules are comparatively **spatially localized**;
5. therefore the apparent integration/segregation organization is explicitly **scale dependent** in the reported analysis.

Safe compression:

```text
same biological recordings
+ different declared network grain
-> materially different organizational description.
```

Blocked compression:

```text
fine scale = true scale;
mesoscale = false scale;
network modularity = consciousness;
coarse-graining always destroys the causal organization;
SRT uniquely predicted this result.
```

---

## 3. SRT relevance

### 3.1 Direct N3/N5 objectification pressure

The current neuroscience framework already distinguishes:

```text
recorded neuron / ensemble / ROI / graph edge
!= automatically natural causal or historical unit
```

and already treats pair / graph construction and coarse-graining as possible information-losing objectification operations.

This source gives that framework a concrete empirical anchor:

> A system-level property can change when the same underlying activity is redescribed using a different declared node grain.

The source therefore strengthens a methodological burden rather than creating a new ontology primitive:

```text
when a neural conclusion is claimed to be about "the network",
its stability under reasonable changes of node definition / scale
becomes an empirical question.
```

### 3.2 NEURAL33 relation

NEURAL33 already owns the stronger guard:

```text
component activity variables alone need not exhaust organizational state.
```

Kiyooka et al. do not reproduce the NEURAL33 ripple/reinstatement package. Their increment is different:

```text
organizational state description itself
can be scale-sensitive.
```

Therefore this source is an **adjacent empirical realization / constraint**, not a new NEURAL33 theorem and not evidence for relation-specific memory reinstatement.

### 3.3 Core 14 relation

`Core/SRT_Core_14_Dynamics_Scaling.md` currently treats cross-scale consistency as a conditional P3 bridge requiring declared state spaces, observables, scale map, norm and tolerance. This source is compatible with that guard because it demonstrates why approximate cross-scale agreement cannot be assumed.

It does **not** establish a universal failure of coarse-graining, nor does it license revival of old strict-conjugacy or entropy claims.

---

## 4. Consciousness boundary

The paper frames wakefulness, sleep and anesthesia as states relevant to reduced consciousness. For SRT use, keep the evidential step narrow:

```text
behavioral / physiological brain-state category
!= phenomenal state identity

network modularity
!= consciousness

single-cell segregation
!= unconsciousness mechanism by itself
```

Mouse sleep/anesthesia data can constrain neural-state theories, but the dataset has no first-person report and does not establish necessity or sufficiency for phenomenality.

Accordingly this source must not be used to promote `Ax-CONSC-MECH-3`, a phase-binding identity, IIT-like integration identity, or a Bearer/subjecthood inference.

---

## 5. Owner-side subtraction

```text
Candidate-looking increment:
  scale changes the observed integration / segregation organization.

Likely owners:
  Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md
  Neuroscience/patches/SRT_Neuro_NEURAL33_Distributed_Ripple_Relational_Reinstatement_v0_1.md
  Core/SRT_Core_14_Dynamics_Scaling.md

Bounded probe:
  objectification / graph-construction pressure is already owned;
  component-state != organizational-state is already owned;
  conditional cross-scale consistency is already owned.

Verdict:
  partly owned + reverse constraint.

Residual after subtraction:
  a strong, reusable neural empirical case in which
  state-dependent network conclusions themselves change across declared grain.

Constructive use:
  turn the existing objectification question into an executable
  scale-stability benchmark on open biological data.

Forbidden parallel construct:
  no new "SRT modularity", "objectification score", scale scalar or rung.
```

---

## 6. What this source newly authorizes

It authorizes a **bounded non-confirmatory benchmark protocol** asking whether an inference remains stable under predeclared reasonable changes in:

```text
signal representation
cell inclusion
node grain
edge construction
temporal window
```

The first implementation is specified in:

`Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md`.

That protocol is independent of the existing Phase-8/NEURAL34 charter and cannot inherit its identity, Case verdict or confirmatory status.
