---
source_id: SRC-2026-08-19-NEURO-HUERTA-VAGAL-CYTOKINE-REPRESENTATION
id: SRC-2026-08-19-NEURO-HUERTA-VAGAL-CYTOKINE-REPRESENTATION
title: "Neural representation of cytokines by vagal sensory neurons"
source_type: peer_reviewed_primary_mouse_in_vivo_experiment
domain: neuroscience_neuroimmune_interoception_vagus_representation
primary_authors: "Tomás S. Huerta; Adrian C. Chen; Saher Chaudhry; Aisling Tynan; Timothy Morgan; Kicheon Park; Richard Adamovich-Zeitlin; Bilal Haider; Jian Hua Li; Mitali Nagpal; Stavros Zanos; Valentin A. Pavlov; Michael Brines; Theodoros P. Zanos; Sangeeta S. Chavan; Kevin J. Tracey; Eric H. Chang"
publication: "Nature Communications"
publication_date: "2025"
date_added: "2026-08-19"
doi: "10.1038/s41467-025-59248-6"
primary_sources:
  - "Huerta TS et al. Neural representation of cytokines by vagal sensory neurons. Nature Communications. 2025;16:3840. doi:10.1038/s41467-025-59248-6"
evidence_level: peer_reviewed_primary_full_text_mouse_in_vivo_calcium_imaging_transcriptomics
reliability_level: high_for_cytokine_specific_nodose_response_and_DSS_state_dependence; moderate_for_natural_end_organ_generalization; limited_for_pure_history_effect_and_human_generalization
srt_relevance: very_high_as_bounded_state_dependent_peripheral_representation_and_history_interface_bridge
integration_priority: very_high
related_srt_claims:
  - interoception
  - neuroimmune_coupling
  - state_dependent_representation
  - historical_efficacy
  - candidate_formation
  - bearer_physiology
  - d_value_proxy_boundary
  - Psi_f_proxy_boundary
  - NEURAL25
  - attention_immune_reweighting
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
tags:
  - vagus
  - nodose_ganglion
  - cytokines
  - interoception
  - inflammation
  - colitis
  - calcium_imaging
  - transcriptomics
  - state_dependent_representation
  - history_guard
---

# SourceCard: Huerta et al. — *Neural representation of cytokines by vagal sensory neurons*

## 1. One-line summary

In vivo calcium imaging shows that mouse nodose-ganglion sensory neurons represent IL-1β, TNF and IL-10 with distinguishable real-time response patterns before information reaches the brain; DSS colitis increases baseline nodose activity while reducing specific cytokine responses and the separability of cytokine response clusters, indicating that inflammatory state changes the peripheral sensory interface itself.

## 2. Core claims of source

### 2.1 Nodose neurons carry cytokine-specific real-time response patterns

The authors imaged PHOX2B+ nodose-ganglion sensory neurons in VGLUT2–GCaMP6f mice and applied IL-1β, TNF and IL-10 to the cervical vagus nerve. Individual cytokine-evoked calcium responses differed across amplitude, duration, rise slope, integral, peak number and decay slope. Maximum response amplitude differed significantly among the three cytokines.

**PDF anchors:** pp. 1–3; Results section `Nodose ganglia neurons have cytokine-specific neural responses`; Fig. 1b–d and caption.

The safe source-level claim is:

```text
specific cytokines
-> distinguishable nodose-ganglion response dynamics
```

not:

```text
one cytokine = one dedicated neuron
```

### 2.2 The coding pattern is mixed rather than a pure labelled-line architecture

Sequential IL-1β/TNF experiments identified IL-1β-specific, TNF-specific, multi-cytokine and non-cytokine-responsive groups. Among the analyzed responders, TNF-specific neurons were 40.7%, multi-cytokine 28.6%, IL-1β-specific 17.1% and non-cytokine 13.6%. Cytokine-responsive cells were spatially distributed without an obvious topographic organization.

**PDF anchors:** pp. 2–4; Fig. 2a–d.

This supports a population/mixed-coding interpretation rather than a simple dedicated-line reading.

### 2.3 In the tested range, response profile tracked cytokine identity more clearly than concentration

The authors tested several concentrations of IL-1β, TNF and IL-10 and report no evidence that concentration changed the response profiles in those dose-response experiments. Applying the same cytokines to the proximal colon also produced stereotyped activity patterns similar to direct vagal application.

**PDF anchors:** p. 2, dose-response paragraph; Supplementary Fig. 3.

Boundary:

```text
no concentration effect detected in the tested range
!= vagal afferents never encode cytokine intensity
```

### 2.4 DSS colitis produces a high-baseline / lower-response state

At peak DSS colitis, more nodose neurons were spontaneously active at baseline, but spontaneous calcium-transient amplitude was lower than in controls. In the longitudinal cohort, spontaneous-transient amplitude remained reduced at days 7 and 14.

**PDF anchors:** pp. 5, 8–9; Fig. 4a–g and caption.

The source therefore supports the dissociation:

```text
more active neurons at baseline
!= stronger event-specific response
```

### 2.5 Inflammation changes cytokine responses selectively, not as one global gain scalar

TNF-specific response amplitude was reduced in DSS mice (`P = 0.0062`) and IL-10-specific response amplitude was also reduced (`P = 0.0003`), whereas IL-1β response amplitude did not show a significant change. Across the multidimensional response space, cytokine clusters were less separable in DSS colitis than controls; the reported Calinski–Harabasz clustering score was 47.11 versus 19.62 (`P = 0.0019`).

**PDF anchors:** pp. 6–7 and 11; Fig. 6a–e and caption.

This is stronger than a generic `inflammation -> response down` statement. The observed transformation is cytokine-specific and multidimensional.

### 2.6 The peripheral interface itself is transcriptionally altered during colitis

Bulk RNA-seq of vagal ganglia at peak DSS colitis identified upregulation of neuronal-signalling-associated genes/pathways and downregulation of inflammatory/cytokine-signalling-associated genes/pathways. Reported neuronal-side changes include genes associated with membrane excitability, ion channels and neurotransmitter release; inflammatory-side reductions include cytokine-response and JAK–STAT-related pathways.

**PDF anchors:** pp. 5, 10; Fig. 5a–d.

The safe inference is that inflammatory state is associated with a changed sensory-neural operating condition. The experiment does not isolate which transcriptomic change causes which calcium-response change.

### 2.7 Resolution-phase persistence is suggestive, but not a pure history-only result

At day 14, symptom-based disease activity scoring was nearly back to normal while nodose spontaneous-transient amplitude remained reduced. Colon length was still shortened at this time point. The authors therefore suggest that altered nodose activity can persist into the resolution phase and may reflect end-organ health more sensitively than overt symptom scoring.

**PDF anchor:** p. 5, paragraph immediately before `DSS-colitis is associated with vagal ganglia transcriptomic changes...`; Fig. 4f–g.

Critical boundary:

```text
overt symptom recovery
!= sensory-interface recovery
```

but the paper does **not** establish:

```text
fully matched present bodily state
+ different history
-> different representation
```

because current tissue state was not fully matched.

## 3. Evidence / method

The study combines:

- in vivo miniscope calcium imaging of vagal ganglia in VGLUT2–GCaMP6f mice;
- direct cervical-vagus application of IL-1β, TNF and IL-10;
- proximal-colon cytokine application as an end-organ check;
- DSS-induced colitis;
- histology, serum/colon cytokine assays and bulk RNA-seq;
- multidimensional clustering of cytokine-evoked calcium-transient features.

For direct-vagus experiments, cytokines were applied to the exposed cervical vagus as 15 µL droplets. Saline controls activated a separate subset interpreted as likely mechanosensitive neurons.

**PDF anchors:** pp. 9, 12; Methods sections `Nodose ganglion isolation and stabilization`, `Application of solutions directly on the vagus nerve`, `DSS-induced model of colitis`, `Bulk RNA transcriptomic analysis`, `Multidimensional cluster analysis`.

The DSS-colitis imaging experiments used male mice; the authors cite estrogen-related reduction of DSS severity as the reason.

## 4. Limits

1. **Mouse model:** the central disease-state results are from DSS colitis in mice and do not establish the same coding transformation in humans.
2. **Direct nerve application:** much of the cytokine-specific response work uses cytokines directly on the exposed vagus nerve; this is strong for response capacity but is not identical to a fully natural organ-to-nerve signalling sequence.
3. **Limited cytokine set:** the core comparison concerns IL-1β, TNF and IL-10; it does not establish a universal cytokine code.
4. **Concentration boundary:** absence of a detected dose-profile effect in the tested range is not evidence of universal concentration insensitivity.
5. **History confound:** persistence during resolution does not isolate history from remaining tissue/state differences.
6. **Representation language:** distinct response patterns and cluster separability establish an experimentally useful neural representation; they do not by themselves establish semantic content, consciousness, subjecthood or SRT Selection.
7. **Causal transcriptomics boundary:** RNA-seq changes are associated with the DSS state; the study does not causally assign each transcriptional change to the altered response geometry.

## 5. SRT relevance

### 5.1 Source-backed pressure

The strongest source-backed structure is:

```text
bodily / inflammatory state
-> changed peripheral sensory operating condition
-> changed neural representation available to downstream brain circuits
```

with two useful dissociations:

```text
baseline activity magnitude
!= event-specific discriminability

current overt symptoms
!= current sensory-interface state
```

### 5.2 Contribution route

**O-track — primary / retained.** The source provides a high-quality empirical instance for organizing a state-dependent peripheral-representation layer between bodily state and central processing:

```text
body state
-> state-dependent peripheral representation
-> downstream central access/control
```

It also constrains older single-scalar SRT neuroscience language: inflammatory state cannot safely be represented as a globally monotone change in neural activity, perceptual access or canonical `Psi_f`.

**D-track — not established by the source.** The paper does not compare SRT with active-inference, predictive-processing, allostatic or ordinary state/history models. A separate frozen-comparator experiment is required before any SRT-specific history/bearer claim is admitted.

### 5.3 History / candidate-formation guard

This source motivates—but does not prove—the P4 question:

```text
matched current bodily state
+ different inflammatory history
-> different future sensory response geometry ?
```

A stronger SRT-specific extension would additionally separate matched exposure/current state from bearer-specific future consequence. Those are SRT-side hypotheses, not Huerta et al.'s findings.

### 5.4 Explicit non-identities

```text
cytokine-specific neural response
!= SRT Selection

nodose ganglion
!= bearer / subject

inflammation
!= canonical Psi_f

neural activity magnitude
!= information / separability

state-dependent representation
!= L0 evidence

history persistence
!= historical efficacy proved under matched present state
```

## 6. Suggested patch target

Primary bridge:

```text
Neuroscience/VAGAL_CYTOKINE_REPRESENTATION_HISTORY_SRT_BRIDGE_2026-08-19.md
```

Integration hook:

```text
Neuroscience/hooks/VAGAL_CYTOKINE_Representation_History_Integration_Hook.md
```

Cross-read:

```text
Neuroscience/ATTENTION_IMMUNE_REWEIGHTING_SRT_BRIDGE_2026-08-18.md
Neuroscience/INTEROCEPTIVE_PRECISION_SRT_BRIDGE.md
Neuroscience/SRT_Neuro_08_Immune_Dist.md
```

No P0/P1 owner, canonical `d`, canonical `Psi_f`, subjecthood criterion, consciousness criterion or new neuroscience claim number should be changed from this source.

## 7. Final evidence verdict

**Pipeline 1 verdict: A, bounded non-canonical P3/P4 bridge material.**

The durable increment is a source-backed state-dependent peripheral-representation layer plus a strong correction against collapsing inflammatory state into one neural/perceptual scalar. The most informative SRT-specific history/bearer experiments remain prospective and unearned.