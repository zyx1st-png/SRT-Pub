---
patch_id: PATCH-NEURO-NEURAL17-HGA-SPIKE-DISSOCIATION-GATE
source_ids:
  - SRC-2026-04-01-NEURO-HGA-SPIKE-DISSOCIATION-NATURE
domain: neuroscience_measurement
claim_level: bridge
canonical_status: domain_bridge_integrated
status: patch
target_documents:
  - "SRT_EXP_MEASURE_MAP.md"
  - "Neuroscience/SRT_Neural_Mechanisms.md"
related_claims:
  - high_gamma_activity_proxy
  - local_spiking_proxy
  - mesoscale_synchrony
  - input_output_distinction
  - non_reductive_validation
tags:
  - HGA
  - high_gamma
  - spikes
  - LFP
  - BMI
  - proxy_guardrail
  - Nature
---

# SRT Neuroscience Patch NEURAL17: HGA-Spike Dissociation Gate v0.1

> Status: neuroscience measurement bridge patch.
> Canonical caution: this patch does not define HGA, spikes, `Psi_f`, `d-value`, consciousness, `C_wave`, `D_align`, or `L_2`. It adds a reliability gate for using high-gamma readouts as SRT neural proxies.

## 0. Source anchor

Primary source:

- Tianhao Lei, Michael R. Scheid, Robert D. Flint, Joshua I. Glaser, and Marc W. Slutzky. (2026). "Active dissociation of intracortical spiking and high gamma activity." Nature. DOI: `10.1038/s41586-026-10331-y`.

Official source:

```text
https://www.nature.com/articles/s41586-026-10331-y
```

## 1. Why this matters for SRT

SRT often needs to use neural measurements as proxies for selection bandwidth, integration, local friction, ignition, and state availability. HGA is tempting because it is high-resolution, behaviorally informative, and widely used. This source adds a narrow but important constraint: HGA must not be treated as local spiking output by default.

The usable SRT lesson is methodological:

```text
same-electrode HGA-spike correlation
  != local output identity
```

## 2. Main SRT bridge claim

### Claim NEURAL17

High-gamma readouts require a source-scope gate before they can support SRT neural interpretation:

```text
HGA
  -> admissible as mesoscale synchrony / input-integration proxy by default
  -> admissible as local output-spiking proxy only with additional spike/population/perturbation support
```

This is a lab-facing bridge rule, not a new primitive. The SRT point is narrow:

```text
HGA-spike dissociation != gamma invalidity
HGA-spike dissociation == local-output proxy caution
```

## 3. Mapping table

| Source-level result | SRT interpretation | Guardrail |
|---|---|---|
| monkeys can decouple HGA and spike rate from the same electrode | HGA is not identical to local output spiking | do not equate HGA with nearby firing by default |
| HGA correlates with distributed co-firing across the array | HGA can index mesoscale synchrony/input integration | declare spatial scale and population context |
| spike-triggered HGA aligns with distributed co-firing contributors | postsynaptic/integrative source is plausible | keep biophysical source open but constrained |
| rapid ONF learning suggests intrinsic neural manifold support | dissociation is not merely arbitrary task noise | still treat BMI context as a perturbation window |
| HGA remains informative | proxy is useful but scoped | do not discard HGA; gate its interpretation |

## 4. Formal bridge

Minimum lab gate:

```text
R_HGA(e,t) = 1
  only if the target of interpretation is declared:
    local output spiking,
    local synaptic/input integration,
    or distributed population synchrony,
  and the evidence package supports that target.

If R_HGA(e,t) = 0:
  HGA(e,t) = mesoscale neural-state proxy at most.
```

SRT use:

```text
Psi_f^{neural_proxy}(e,t),
d^{neural_proxy}(e,t),
C_wave(e,t),
D_align(e,t)
  may use HGA only after R_HGA is declared.
```

This is not a canonical equation. It is a proxy-admission rule for gamma-band / broadband neural material.

## 5. Experimental / operational consequences

This patch adds a focused requirement:

```text
H-NEURAL17:
Any SRT experiment using HGA or broadband gamma as evidence for local
neuronal output, selection bandwidth, ignition, or consciousness must
report whether HGA is being used as output-spiking proxy, input-synchrony
proxy, or mixed proxy, and must provide controls appropriate to that level.
```

Potential failure condition:

```text
If future causal perturbation studies across modalities and cortical areas
show that local spike leakage fully explains HGA after distributed synchrony
is controlled, then the default SRT reading should be revised from
"mesoscale synchrony/input proxy" to a narrower modality-specific local-output proxy.
```

## 6. Boundary cautions

- Do not write that HGA is invalid.
- Do not write that HGA never tracks spikes.
- Do not equate high-gamma power with local neuronal output by default.
- Do not identify HGA with `Psi_f`, `d-value`, `T_dir`, consciousness, `C_wave`, `D_align`, or `L_2`.
- Keep recording modality visible: intracortical HGA, ECoG high gamma, EEG/MEG gamma, and model-derived broadband power are not interchangeable.
- Keep the source scope visible: peer-reviewed Nature article, macaque M1 intracortical arrays, ONF/BMI dissociation window.

## 7. Integration status

Integrated as:

```text
SRT_EXP_MEASURE_MAP.md
  -> High-gamma local-spike dissociation gate

Neuroscience/SRT_Neural_Mechanisms.md
  -> High-gamma/spike dissociation gate
```

Future synthesis should fold this into the neuroscience measurement roadmap and any experiment template that treats gamma-band power as a mechanistic readout.
