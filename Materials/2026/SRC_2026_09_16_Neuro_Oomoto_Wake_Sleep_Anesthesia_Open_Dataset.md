---
source_id: SRC-2026-09-16-NEURO-OOMOTO-WAKE-SLEEP-ANESTHESIA-OPEN-DATASET
id: SRC-2026-09-16-NEURO-OOMOTO-WAKE-SLEEP-ANESTHESIA-OPEN-DATASET
title: "Multi-area single-cell calcium imaging dataset of the mouse cortex across wakefulness, sleep, and anesthesia"
source_type: peer_reviewed_data_descriptor_plus_open_dataset
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
domain: neuroscience_open_data_network_objectification
primary_authors: "Ikumi Oomoto; Daiki Kiyooka; Masafumi Oizumi; Masanori Murayama"
publication: "Scientific Data (2026)"
doi: "10.1038/s41597-026-08202-2"
url: "https://doi.org/10.1038/s41597-026-08202-2"
dataset_repository: "RIKEN CBS Data Sharing Platform"
dataset_doi_current_version: "10.60178/cbs.20260708-001"
date_published: "2026-09-10"
date_added: "2026-09-16"
evidence_level: peer_reviewed_data_descriptor_open_mouse_large_scale_two_photon_dataset
reliability_level: high_for_data_contents_and_reuse_scope; analysis_dependent_for_new_network_claims
srt_relevance: very_high_as_open_empirical_benchmark_asset_for_neural_objectification_and_scale_stability
integration_priority: very_high
related_srt_claims:
  - neuroscience_objectification
  - scale_stability
  - graph_construction
  - component_state_vs_organizational_state
  - measurement_representation
  - N3_relational_organization
  - N5_measurement_objectification
  - Phase8_boundary
  - NEURAL34_non_reopening
tags: [open-data, two-photon, single-cell, cortex, wakefulness, NREM, REM, anesthesia, EEG, EMG, network-benchmark, objectification]
---

# SourceCard: Oomoto et al. — reusable wake/sleep/anesthesia single-cell dataset

## 1. Pipeline 1 disposition

```text
Verdict: A — research-asset / benchmark integration
Contribution route: O-track strong infrastructure + reverse-constraint value
D-track: none yet; only after preregistered/reproducible reanalysis
Primary landing:
  Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
No canonical writeback.
No CompactCore writeback.
No NEURAL34 / Phase-8 reopening.
No new SRT metric.
```

This source is unusually valuable for SRT because it does not merely provide another paper-level association. It exposes the **underlying single-cell recordings and multiple processed representations** needed to test how neural conclusions change under declared objectification choices.

---

## 2. Source and dataset anchors

Peer-reviewed Data Descriptor:

```text
Oomoto I, Kiyooka D, Oizumi M, Murayama M. (2026).
Multi-area single-cell calcium imaging dataset of the mouse cortex
across wakefulness, sleep, and anesthesia.
Scientific Data.
DOI: 10.1038/s41597-026-08202-2
Published: 2026-09-10
```

Current repository record located during intake:

```text
RIKEN Center for Brain Science Data Sharing Platform
Version 3.0 — 2026-07-08
DOI: 10.60178/cbs.20260708-001
```

The repository page also records an earlier v2 DOI (`10.60178/cbs.20260409-001`). Any actual execution should pin an exact dataset version and file manifest rather than relying on the floating landing page.

The Data Descriptor reports:

- wide-field two-photon recordings from cortical layers 2/3;
- approximately **4,000–10,000 neurons per session**;
- acquisition at **7.65 Hz**;
- wakefulness, natural sleep including **NREM / REM**, and isoflurane anesthesia;
- spatial coordinates for individual neurons;
- processed MATLAB data including `ΔF/F`, deconvolved activity estimates, Gaussian-smoothed activity estimates, behavioral-state annotations and metadata;
- corresponding raw TIFF imaging movies and electrophysiological recordings.

The RIKEN record states that the open dataset is intended for functional-connectivity, network-organization, spatial-structure and computational benchmarking work. The repository-wide external reuse policy is CC BY 4.0 for open-access research data, but execution must still capture the exact record-level license and metadata at download time.

---

## 3. Why this is more than a citation asset

The dataset permits a controlled analysis structure of the form:

```text
same underlying biological recording
-> different signal representation / inclusion rule / node grain / graph rule
-> compare inferential stability.
```

That is materially stronger than citing published figures because the objectification choices themselves can be varied while preserving the underlying recording source.

The useful experimental pressure is:

> If a claimed neural system property disappears, reverses or changes interpretation under reasonable predeclared ways of turning the same recording into nodes, signals and edges, the analysis must report that scale/objectification dependence rather than present one chosen graph as the scale-free system itself.

This is a methodological constraint. It is not a claim that there is no real neural organization independent of analysis.

---

## 4. Relation to the existing Phase-8 adverse result

The 2026-09-03 neuroscience data-access audit required the exact combination:

```text
same relation candidates
+ PRE relation
+ controlled exposure-matched H+ / H- relation-specific history
+ common future probe / opportunity
+ rich present-state / common-driver controls
+ relation-identity outcome.
```

This dataset does **not** supply that design.

Therefore:

```text
Oomoto dataset != DATA-ACCESS-0 reversal
Oomoto dataset != Phase-8B authorization
Oomoto dataset != NEURAL34 matched-history execution
```

The prior audit explicitly requires a new visible charter if a weaker or different public-data question is chosen. The scale-stability benchmark created with this intake is exactly such an independent bounded question and preserves the earlier NO-GO result.

---

## 5. Appropriate first-use hierarchy

### Tier 0 — data integrity / replication

Before any SRT-facing analysis:

1. pin the dataset DOI/version and file manifest;
2. verify state labels, recording durations, neuron counts and spatial coordinates;
3. reconstruct at least one published Kiyooka network result or a close equivalent;
4. document any discrepancy before adding new analyses.

### Tier 1 — objectification sensitivity

Vary predeclared analysis choices such as:

```text
signal representation:
  ΔF/F / deconvolved / smoothed

cell inclusion:
  all QC-passing / activity-thresholded subsets

node grain:
  single cell / local aggregate / mesoscale aggregate

edge construction:
  declared correlation or other standard functional-connectivity rule

threshold / density:
  predeclared sensitivity grid
```

Primary question:

```text
Does the sign / magnitude / ordering of the brain-state inference
remain stable across reasonable objectifications?
```

### Tier 2 — matched measured component summaries

A later exploratory analysis may match windows on measured component summaries such as mean activity, variance, active fraction and available state covariates, then ask whether relational/network organization still differs.

Allowed wording:

```text
matched measured component summaries
```

Forbidden wording:

```text
identical neural state
```

because unmeasured synaptic, receptor, intracellular and circuit variables may carry differences.

---

## 6. State-comparison guard

The dataset contains physiological sleep and pharmacological anesthesia, but these conditions should not be collapsed into a single causal treatment axis.

The first benchmark therefore treats:

```text
Wake <-> NREM
and
Wake <-> Isoflurane
```

as separate state contrasts unless exact cohort/session metadata justify a stronger model.

Direct NREM-vs-anesthesia claims require explicit cohort, time-of-day, protocol and other confound handling rather than relying on a shared label such as "reduced consciousness".

---

## 7. Consciousness and ontology guard

This dataset can constrain neural organization across experimentally classified brain states. It cannot by itself establish:

```text
brain-state label = phenomenal state
modularity = consciousness
integration = consciousness
network grain = ontological One
single neuron / module / ROI = Bearer
```

Nor does the dataset prove SRT's pre-object / Selection / One / Bearer architecture. Its SRT value is downstream: it lets the repository test whether neural public objects and network conclusions are robust to the declared cuts used to construct them.

---

## 8. Owner-side subtraction

```text
Candidate increment:
  open dataset enables empirical objectification audit.

Likely owners:
  Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md
  Neuroscience/patches/SRT_Neuro_NEURAL33_Distributed_Ripple_Relational_Reinstatement_v0_1.md
  Core/SRT_Core_14_Dynamics_Scaling.md
  Operations/Audits/SRT_CONSTITUTION_PHASE8A_NEUROSCIENCE_BASELINE_DATA_ACCESS_AUDIT_2026-09-03.md

Verdict:
  partly owned + infrastructure increment.

Residual after subtraction:
  a presently accessible, high-dimensional biological dataset
  capable of supporting a bounded scale/objectification robustness benchmark.

Forbidden parallel construct:
  no new SRT scale variable, objectification score, consciousness score,
  NEURAL34 surrogate or canonical equation.
```

---

## 9. Execution status

```text
Source intake = complete
Dataset downloaded = NO
Participant/animal-level reanalysis = NOT STARTED
Protocol = specified separately
Confirmatory status = NONE
Published-result replication = NOT YET PERFORMED
```

Any future empirical result must be recorded as a new execution artifact rather than silently promoted from this SourceCard.
