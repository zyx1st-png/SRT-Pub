---
source_id: SRC-2026-04-01-NEURO-HGA-SPIKE-DISSOCIATION-NATURE
title: "Active dissociation of intracortical spiking and high gamma activity"
source_type: Nature_open_access_peer_reviewed_article
domain: neuroscience_measurement
url: "https://www.nature.com/articles/s41586-026-10331-y"
doi: "10.1038/s41586-026-10331-y"
authors: "Tianhao Lei; Michael R. Scheid; Robert D. Flint; Joshua I. Glaser; Marc W. Slutzky"
publication: "Nature"
date_published: "2026-04-01"
date_added: "2026-05-12"
evidence_level: peer_reviewed_open_access_original_research
reliability_level: high_for_intracortical_HGA_local_spike_proxy_guardrail
content_access: "Official Nature full text read from https://www.nature.com/articles/s41586-026-10331-y"
srt_relevance: high
integration_priority: medium_high
related_srt_claims:
  - high_gamma_activity_proxy
  - local_spiking_proxy
  - mesoscale_synchrony
  - neural_measurement_guardrail
  - non_reductive_validation
  - proxy_scope_declaration
tags:
  - HGA
  - high_gamma
  - spikes
  - LFP
  - BMI
  - macaque
  - M1
  - proxy_guardrail
  - Nature
status: source_card
---

# SourceCard: HGA-Spike Dissociation

## 1. One-line summary

Lei, Scheid, Flint, Glaser, and Slutzky show that rhesus macaques can actively dissociate intracortical high-gamma activity from spike rate recorded on the same electrode, challenging the common shortcut that HGA is a direct local-spiking proxy.

## 2. Core claims of source

Usable source-level claims:

1. HGA is widely used as a mesoscale cortical signal, but its biophysical source remains contested.
2. The authors designed an orthogonal neurofeedback BMI in which HGA and spike rate from a control electrode drove different cursor dimensions.
3. Monkeys learned to modulate HGA and spike rate independently, including when the two signals were recorded from the same intracortical electrode.
4. HGA correlated more strongly with low-dimensional synchronous co-firing patterns distributed across the array than with nearby local spikes alone.
5. The authors argue that HGA is better explained as arising mainly from summed postsynaptic potentials triggered by distributed synchronous spiking than as a simple sum of local spikes.

## 3. Evidence / method

- Article type: peer-reviewed open-access Nature article.
- Model: adult rhesus macaques with 96-channel intracortical arrays in M1.
- Task: hand-control and orthogonal neurofeedback BMI tasks.
- Signals: intracortical high-gamma power and threshold-crossing spike rates, including same-electrode comparisons.
- Key causal lever: behavioral control required independent modulation of HGA and spikes.
- Data/code: Nature page reports public Figshare data and analysis code repositories.

## 4. Limits

1. The main experimental window is macaque M1 with intracortical arrays; it does not automatically generalize to all cortical areas or all recording modalities.
2. The high-gamma band emphasized in the methods is conservative and high-frequency; lower broadband definitions may need separate handling.
3. The result does not make HGA useless, nor does it deny that HGA and local spiking can correlate in many contexts.
4. BMI training and ONF control are special perturbation contexts; passive task correlations should still be interpreted with care.
5. The paper supports a proxy guardrail, not a direct SRT construct definition.

## 5. SRT relevance

The material gives SRT a neural measurement guardrail:

```text
HGA alone
  -> mesoscale synchrony / input-integration proxy by default
  -> not direct local output-spiking proxy
```

For SRT, the important correction is not anti-gamma skepticism. It is proxy hygiene. HGA can remain useful for tracking neural state, integration, attention, motor control, or BMI-relevant dynamics, but any claim that uses HGA as local output, selection intensity, `Psi_f`, `d-value`, consciousness, or `L_2` evidence must first declare its target level and supporting controls.

## 6. Suggested patch target

Primary targets:

```text
SRT_EXP_MEASURE_MAP.md
Neuroscience/SRT_Neural_Mechanisms.md
```

Patch record:

```text
Neuroscience/patches/SRT_Neuro_NEURAL17_HGA_Spike_Dissociation_Gate_v0_1.md
```
