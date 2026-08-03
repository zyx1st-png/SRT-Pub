---
source_id: SRC-2026-08-03-NEURO-MISAWA-INFORMATIONAL-TUNING-TRAVELING-WAVES
title: "Awake cortex stabilizes traveling waves for global and reliable information routing"
source_type: peer_reviewed_open_access_original_research
domain: neuroscience_consciousness_traveling_waves_information_routing
url: "https://doi.org/10.1016/j.isci.2026.116728"
doi: "10.1016/j.isci.2026.116728"
authors: "Ryuta Misawa et al."
publication: "iScience"
date_published: "2026"
date_added: "2026-08-03"
evidence_level: peer_reviewed_primary_abstract_and_open_metadata
reliability_level: high_for_reported_rat_ECoG_state_comparison; full_methods_close_read_pending
content_access: "Primary PubMed abstract, publisher highlights, and open metadata; Neuroscience News used only as discovery trail"
srt_relevance: high
integration_priority: high_B1_measurement_proxy_B2_consciousness_claim
related_srt_claims:
  - T_dir_proxy_guardrail
  - directional_information_routing
  - consciousness_mechanism
  - traveling_waves
  - information_quantity_quality_dissociation
  - selective_resynchronization
  - state_transition
tags:
  - traveling_waves
  - ECoG
  - informational_tuning
  - transfer_entropy
  - wakefulness
  - anesthesia
  - consciousness
  - information_routing
  - iScience
status: source_card
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
id: SRC-2026-08-03-NEURO-MISAWA-INFORMATIONAL-TUNING-TRAVELING-WAVES
---

# SourceCard: Informational Tuning of Awake Cortical Traveling Waves

## 1. One-line summary

Misawa and colleagues report that visual-evoked cortical traveling waves in awake rats are more stable and display richer large-scale motifs than under anesthesia, while information flow is more reliably aligned with wave propagation direction despite raw transfer-entropy magnitude not simply increasing with wakefulness.

## 2. Core source claims

Usable source-level claims:

1. The study used large-scale, high-density electrocorticography to observe visual-evoked traveling waves across much of the rat cortex.
2. Awake and anesthetized states were compared within the same broad measurement framework.
3. Traveling-wave patterns were more stable in the awake condition.
4. Awake cortex exhibited a richer repertoire of large-scale propagation motifs.
5. Information flow was evaluated in relation to the direction of traveling-wave propagation.
6. In the awake state, information flow was more reliably aligned with propagation direction, a relation the authors call informational tuning.
7. Raw transfer-entropy magnitude alone did not track wakefulness monotonically; anesthesia could show substantial or higher aggregate transfer entropy while exhibiting poorer directional alignment.
8. The authors interpret wakeful cortical dynamics as enabling more reliable global routing rather than merely more total information transfer.
9. The study concerns neural state organization and routing; it does not establish a sufficient condition for consciousness.
10. The source provides a measurement and mechanism window, not an ontology of awareness or selection.

## 3. Evidence and method

- Species: rats.
- Recording: large-scale high-density ECoG spanning broad cortical territory.
- Perturbation or state contrast: awake versus anesthetized conditions.
- Stimulation: visual-evoked activity.
- Dynamic object: traveling-wave propagation motifs and their temporal stability.
- Information measure: directional information flow using transfer-entropy analyses.
- Proposed measure: alignment between wave propagation direction and information-flow direction, termed informational tuning.
- Primary evidence boundary: peer-reviewed primary abstract and publisher highlights were available; detailed preprocessing, anesthesia protocol, statistics, and supplementary robustness checks were not fully close-read in this pass.

## 4. Main limits

1. Wakefulness and anesthesia are broad state contrasts; anesthetic-specific effects may contribute to observed dynamics.
2. Visual-evoked ECoG does not exhaust spontaneous, multisensory, cognitive, or human conscious processing.
3. Transfer entropy is an analyst-facing statistical measure and does not by itself establish causal communication.
4. Directional alignment can support reliable routing without implying self-access, subjective awareness, value, or stake.
5. Informational tuning is not shown to be necessary or sufficient for consciousness across all states.
6. The paper does not identify canonical `T_dir`, `d`, `Psi_f`, `G_hat_theta`, or `L_2`.
7. Full-method close-read is still required before importing effect sizes, exact electrode coverage, preprocessing choices, or strong causal language.

## 5. SRT relevance

The most stable SRT contribution is a negative and methodological distinction:

```text
more aggregate information transfer
!=
more wakeful or more consciously organized processing
```

The source suggests that **directional reliability and coordination** may matter more than raw information quantity. This aligns with SRT's refusal to reduce consciousness or direction-readability to bandwidth, integration, or transfer volume alone.

A safe bridge is:

```text
informational tuning
= candidate proxy for directionally organized neural routing
```

An unsafe identity is:

```text
informational tuning = T_dir
traveling-wave stability = consciousness
transfer entropy = d-value or Psi_f
```

Canonical `T_dir` concerns the selecting system's readability of its own current selection direction and its capacity for reorientation. The source measures alignment between two externally estimated neural directions. The missing bridge includes internal access, behavioral reorientation, consequence sensitivity, and bearer-specific history.

## 6. Bidirectional gain card

### New interface

- `direction-versus-volume dissociation`: information-flow magnitude and directional organization can move differently across states.
- `informational tuning`: a candidate laboratory measure for propagation–information alignment.
- traveling-wave stability and motif repertoire as state-sensitive neural organization measures.

### Reverse correction to SRT

- Do not describe consciousness as simply more information flow.
- Do not identify an externally estimated neural direction with canonical `T_dir`.
- Do not infer subjecthood, stake, or internal readability from stable propagation alone.
- Do not treat anesthesia as a pure on/off manipulation of consciousness without drug- and state-specific controls.

### Strengthened SRT content

- Directional organization can be empirically separated from aggregate transfer volume.
- Reliable routing may require stable coordination among large-scale neural dynamics.
- Consciousness-facing experiments should report direction, stability, and routing fidelity in addition to power or information quantity.

### SRT contribution back to the source

SRT can propose a stronger test sequence:

```text
propagation-information alignment
-> internal availability
-> behaviorally demonstrated reorientation
-> consequence-sensitive persistence
-> history-dependent future selection
```

This would test whether directional routing is merely coordinated communication or contributes to a system-readable selection direction.

### Residual pressure

If informational tuning predicts wakefulness and behavior as well as or better than SRT-specific variables, SRT must clarify whether `T_dir` adds measurable explanatory content beyond ordinary routing fidelity and state classification.

## 7. Pipeline verdict and revival trigger

**Verdict: B1 for experimental proxy; B2 for consciousness or `T_dir` claims.**

Revival trigger:

> Reopen when `T_dir` is operationalized experimentally, when the selective-resynchronization paper requires a direction-versus-volume neural comparison, or when the neuroscience synthesis revisits anesthesia and traveling-wave consciousness proxies.

No PatchNote is created in this pass because the full methodological close-read is incomplete and the strongest surviving use is a bounded measurement proxy and anti-overclaiming guardrail.
