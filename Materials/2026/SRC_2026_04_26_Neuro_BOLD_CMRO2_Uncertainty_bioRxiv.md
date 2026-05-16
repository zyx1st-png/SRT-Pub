---
source_id: SRC-2026-04-26-NEURO-BOLD-CMRO2-UNCERTAINTY-BIORXIV
title: "Opposing BOLD signals and oxygen metabolism largely arise from statistical uncertainty in metabolic estimates"
source_type: bioRxiv_preprint_reanalysis
domain: neuroscience_measurement
url: "https://doi.org/10.64898/2026.04.21.719913"
doi: "10.64898/2026.04.21.719913"
authors: "Ole Goltermann; Alexander Huth; Christian Büchel"
publication: "bioRxiv preprint, version 1"
date_published: "2026-04-26"
date_added: "2026-05-11"
evidence_level: preprint_full_pdf_open_data_reanalysis
reliability_level: medium_for_proxy_uncertainty_guardrail_until_peer_review
content_access: "Full local PDF read from /Users/zhangyuxin/Downloads/2026.04.21.719913v1.full.pdf"
srt_relevance: high
integration_priority: medium_high
related_srt_claims:
  - hemodynamic_metabolic_proxy
  - BOLD_CMRO2_relation
  - metabolic_uncertainty_gate
  - Psi_f_metabolic_proxy
  - non_reductive_validation
  - proxy_scope_declaration
tags:
  - BOLD
  - CMRO2
  - fMRI
  - neurovascular_coupling
  - proxy_uncertainty
  - measurement
  - bioRxiv
status: source_card
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
id: SRC-2026-04-26-NEURO-BOLD-CMRO2-UNCERTAINTY-BIORXIV
---

# SourceCard: BOLD-CMRO2 Uncertainty Reanalysis

## 1. One-line summary

Goltermann, Huth, and Büchel reanalyse the open Epp et al. dataset and argue that much of the reported BOLD-CMRO2 sign discordance is not statistically robust once participant variability and CMRO2 estimate uncertainty are taken into account.

## 2. Core claims of source

Usable source-level claims:

1. The authors replicate the group-mean sign-discordance analysis and find roughly similar raw discordance to Epp et al. before uncertainty gating.
2. Task-evoked CMRO2 estimates show high voxel-wise and participant-level variability relative to BOLD percent-signal-change maps.
3. A participant-level sign-consistency test classifies only a tiny fraction of BOLD-active voxels as statistically concordant or discordant.
4. A group-level CMRO2 significance gate leaves 77.2% of BOLD-active voxels without a statistically reliable CMRO2 direction; among classifiable voxels, positive BOLD is mostly concordant while negative BOLD remains harder to interpret.
5. The authors conclude that the earlier widespread discordance claim likely reflects statistical uncertainty in model-based CMRO2 estimates rather than widespread physiological sign reversal.

## 3. Evidence / method

- Article type: bioRxiv preprint, version 1, not peer reviewed.
- Data: open dataset from Epp et al. (OpenNeuro `ds004873`), with complete derivatives for 38 of the original 40 participants.
- Measures: BOLD, CBF, CBV, T2*, R2', and model-based CMRO2 estimates from quantitative fMRI / mqBOLD and ASL derivatives.
- Task window: CALC versus CTRL conditions.
- Reanalysis: voxel-wise BOLD activation mask, coefficient-of-variation summaries, participant-level binomial sign-consistency tests, and group-level CMRO2 tests with FDR correction.
- Code availability: the PDF reports a public GitHub repository for scripts and summary statistics.

## 4. Limits

1. The preprint is a methodological reanalysis and has not yet passed peer review.
2. It does not prove that BOLD and oxygen metabolism are always concordant.
3. It does not settle negative BOLD physiology; the source itself keeps negative BOLD as a difficult, heterogeneous case.
4. It depends on the original derivative data and on a redefined voxel-wise BOLD activation mask.
5. CMRO2 remains a model-based quantitative fMRI estimate, not PET oxygen-tracer ground truth.

## 5. SRT relevance

The material gives SRT a measurement guardrail, not a new neuroscience ontology:

```text
hemodynamic / metabolic proxy
  -> usable only after uncertainty gating
  -> otherwise indeterminate, not evidence for sign reversal
```

For SRT, the key point is that a biological proxy may fail not because the underlying mechanism is absent, but because the proxy direction is underdetermined. This directly strengthens the existing non-reductive validation rule: BOLD, CMRO2, and metabolic-budget readouts cannot be promoted into `Psi_f`, `d-value`, or `L_2` claims unless their reliability, scope, and simpler alternatives have been declared.

## 6. Suggested patch target

Primary targets:

```text
SRT_EXP_MEASURE_MAP.md
Neuroscience/SRT_Neural_Mechanisms.md
```

Patch record:

```text
Neuroscience/patches/SRT_Neuro_NEURAL16_BOLD_CMRO2_Uncertainty_Gate_v0_1.md
```
