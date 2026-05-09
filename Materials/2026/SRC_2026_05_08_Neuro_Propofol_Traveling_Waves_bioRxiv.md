---
source_id: SRC-2026-05-08-NEURO-PROPOFOL-TRAVELING-WAVES-BIORXIV
title: "Propofol-induced loss of responsiveness reorganizes cortical traveling waves in the human brain"
source_type: bioRxiv_preprint
domain: neuroscience_consciousness
url: "https://www.biorxiv.org/content/10.64898/2026.04.30.721975v1"
api_url: "https://api.biorxiv.org/details/biorxiv/10.64898/2026.04.30.721975"
doi: "10.64898/2026.04.30.721975"
authors: "V. M. Zarr; T. S. Davis; E. H. Smith; B. Greger; Z. W. Davis; P. A. House"
publication: "bioRxiv preprint, version 1"
date_published: "2026-05-05"
date_added: "2026-05-08"
evidence_level: preprint_abstract_and_official_metadata_only
reliability_level: medium_low_until_full_text_review
content_access: "Official bioRxiv API metadata and abstract available; direct HTML, PDF, and JATS XML locally blocked by Cloudflare during processing"
srt_relevance: high
integration_priority: medium_high
related_srt_claims:
  - traveling_wave_routing
  - wave_ignition_coupling
  - propofol_anesthesia
  - loss_of_responsiveness
  - D_align
  - C_wave
  - spike_wave_coupling
  - consciousness_state_transition
tags:
  - propofol
  - traveling_waves
  - anesthesia
  - consciousness
  - microelectrode_arrays
  - spike_wave_coupling
  - bioRxiv
status: source_card
---

# SourceCard: Propofol, Traveling Waves, and Loss of Responsiveness

## 1. One-line summary

Zarr and colleagues report, in a bioRxiv preprint, that propofol-induced loss of responsiveness in two human participants reorganized temporal-lobe cortical traveling waves, including propagation speed, direction, spectral structure, firing activity, and spike-wave relationships.

## 2. Core claims of source

The official bioRxiv abstract states that the study examined cortical traveling waves recorded with high-density microelectrode arrays in the temporal lobes of two human participants, both men, as they underwent general anesthesia with propofol.

The abstract-level claims usable for SRT are:

1. propofol produced robust state-dependent reorganization of traveling-wave dynamics;
2. the reported changes included increased propagation speed, shifted propagation directions, and altered spectral structure;
3. neuronal firing activity and spike-wave relationships also changed under propofol;
4. the authors interpret the result as evidence that propofol reshapes cortical spatiotemporal organization across spatial scales.

## 3. Evidence / method

Evidence level for this SourceCard is deliberately narrow:

- source: official bioRxiv metadata and abstract via DOI API;
- type: preprint, version 1, category neuroscience, type "new results";
- method visible from abstract: high-density microelectrode arrays in human temporal lobes, `N=2`, both participants male;
- local access limitation: direct bioRxiv HTML, PDF, and JATS XML requests returned Cloudflare challenge pages during processing, so methods, figures, statistics, and limitations were not close-read.

## 4. Limits

1. This is a preprint and should not be treated as peer-reviewed clinical consensus.
2. Current SRT processing used abstract-level information only.
3. The sample is small (`N=2`), male-only, and anatomically restricted to temporal-lobe recordings.
4. The result does not prove that consciousness is identical to traveling waves.
5. The result does not establish a general rule for all anesthetics, all brain regions, or all forms of unconsciousness.

## 5. SRT relevance

The material directly targets an existing SRT bridge:

```text
P_ignite = sigma(alpha C_wave + beta(Phi*d) + gamma D_align - delta)
```

Its main SRT relevance is that propofol loss of responsiveness may involve wave-route reorganization rather than simple wave shutdown. That pushes SRT to keep speed, direction, spectral structure, and spike-wave coupling separate.

SRT-compatible compression:

```text
propofol LOR
  -> wave direction / spectrum / spike-wave coupling reorganization
  -> D_align and C_wave can fail by retuning, not only by disappearance
  -> P_ignite and reportability can fall even when propagation speed increases
```

## 6. Suggested patch target

Primary target:

```text
Neuroscience/SRT_Consciousness_Mechanisms.md
```

Patch record:

```text
Neuroscience/patches/SRT_Neuro_CONSC14_Propofol_Traveling_Wave_Reorganization_v0_1.md
```

