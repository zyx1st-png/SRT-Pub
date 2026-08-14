---
source_id: SRC-2026-04-26-NEURO-BOLD-CMRO2-UNCERTAINTY-BIORXIV
title: "Opposing BOLD signals and oxygen metabolism largely arise from statistical uncertainty in metabolic estimates"
source_type: eLife_reviewed_preprint_reanalysis
domain: neuroscience_measurement
url: "https://doi.org/10.7554/eLife.111743.1"
doi: "10.7554/eLife.111743.1"
all_versions_doi: "10.7554/eLife.111743"
preprint_doi: "10.64898/2026.04.21.719913"
authors: "Ole Goltermann; Alexander Huth; Christian Büchel"
publication: "eLife Reviewed Preprint, version 1"
date_preprint: "2026-04-26"
date_reviewed_preprint: "2026-06-23"
date_added: "2026-05-11"
date_updated: "2026-08-15"
evidence_level: reviewed_preprint_full_text_open_data_reanalysis_public_reviews
reliability_level: medium_high_for_proxy_uncertainty_guardrail_with_open_peer_review_caveats
content_access: "Full local PDF read for preprint; eLife Reviewed Preprint metadata, assessment, abstract, and public reviews verified online 2026-08-15"
srt_relevance: high
integration_priority: medium_high
related_primary_source:
  title: "BOLD signal changes can oppose oxygen metabolism across the human cortex"
  authors: "Samira M. Epp; Gabriel Castrillón; Beijia Yuan; Jessica Andrews-Hanna; Christine Preibisch; Valentin Riedl"
  publication: "Nature Neuroscience 29, 1225-1236 (2026)"
  doi: "10.1038/s41593-025-02132-9"
  version_of_record: "2025-12-16"
related_srt_claims:
  - hemodynamic_metabolic_proxy
  - BOLD_CMRO2_relation
  - metabolic_uncertainty_gate
  - proxy_mapping_stability
  - Psi_f_metabolic_proxy
  - non_reductive_validation
  - proxy_scope_declaration
tags:
  - BOLD
  - CMRO2
  - fMRI
  - neurovascular_coupling
  - proxy_uncertainty
  - mapping_stability
  - measurement
  - reviewed_preprint
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

Goltermann, Huth, and Büchel reanalyse the open Epp et al. dataset and argue that much of the reported BOLD-CMRO2 sign discordance is not statistically robust once participant variability and uncertainty in model-based CMRO2 estimates are taken into account. The work has since become an eLife Reviewed Preprint with public peer review; the eLife assessment rates the question as important and the evidence as convincing, while the reviews preserve caveats about distinguishing low power from genuine null metabolic responses.

## 2. Original target claim: Epp et al.

The reanalysis directly targets:

- Samira M. Epp, Gabriel Castrillón, Beijia Yuan, Jessica Andrews-Hanna, Christine Preibisch, and Valentin Riedl. "BOLD signal changes can oppose oxygen metabolism across the human cortex." *Nature Neuroscience* 29, 1225-1236 (2026). DOI: `10.1038/s41593-025-02132-9`; version of record 2025-12-16.
- Epp et al. report that about 40% of voxels with significant task-evoked BOLD changes show estimated CMRO2 changes of the opposite sign, with stronger discordance for negative BOLD and prominent effects in default-mode regions.
- They further report that concordant and discordant voxels differ in baseline oxygen extraction fraction and in how task-related oxygen demand is accommodated: concordant voxels rely more strongly on CBF changes, whereas discordant voxels show a larger OEF contribution.

Usable interpretation of Epp et al. for SRT is narrow: the BOLD-to-metabolism mapping cannot be assumed to be a transparent, context-free identity. The strong numerical claim of widespread physiological sign reversal, however, must be read together with the uncertainty reanalysis below.

## 3. Core claims of Goltermann et al.

Usable source-level claims:

1. The authors replicate the group-mean sign-discordance analysis and obtain raw discordance broadly similar to Epp et al. before uncertainty gating.
2. Task-evoked CMRO2 estimates show high voxel-wise and participant-level variability relative to BOLD percent-signal-change maps.
3. A participant-level sign-consistency test classifies only a small fraction of BOLD-active voxels as statistically concordant or discordant.
4. A group-level CMRO2 significance gate leaves 77.2% of BOLD-active voxels without a statistically reliable CMRO2 direction; among classifiable voxels, positive BOLD is mostly concordant while negative BOLD remains harder to interpret.
5. The authors conclude that the earlier widespread discordance claim likely reflects substantial statistical uncertainty in model-based CMRO2 estimates rather than widespread physiological sign reversal.

## 4. Evidence / method

- Article status: eLife Reviewed Preprint v1, published 2026-06-23; the underlying preprint was posted 2026-04-26.
- eLife assessment: significance `important`; strength of evidence `convincing`.
- Data: open dataset from Epp et al. (OpenNeuro `ds004873`), with complete derivatives for 38 of the original 40 participants.
- Measures: BOLD, CBF, CBV, T2*, R2', and model-based CMRO2 estimates from quantitative fMRI / mqBOLD and ASL derivatives.
- Task window: CALC versus CTRL conditions.
- Reanalysis: voxel-wise BOLD activation mask, coefficient-of-variation summaries, participant-level binomial sign-consistency tests, and group-level CMRO2 tests with FDR correction.
- Code availability: public analysis code and summary statistics are reported by the authors.

## 5. Limits and live dispute

1. The reviewed preprint does not prove that BOLD and oxygen metabolism are always concordant.
2. It does not settle negative BOLD physiology; both the source and its public reviews keep negative BOLD as a difficult, heterogeneous case.
3. One public reviewer notes that a non-significant CMRO2 effect can reflect either insufficient power or a genuine near-null metabolic response. Therefore `indeterminate` is an epistemic classification, not evidence that metabolism is unchanged.
4. The reanalysis depends on the original derivative data, a redefined voxel-wise BOLD activation mask, and model-based quantitative MRI estimates.
5. CMRO2 remains a model-based quantitative fMRI estimate rather than oxygen-tracer PET ground truth.
6. Epp et al.'s task- and region-dependent CBF/OEF patterns remain a legitimate mechanism hypothesis where metabolic direction is independently reliable; the uncertainty critique limits the strength and prevalence claim rather than logically eliminating all state-dependent neurovascular coupling.

## 6. SRT relevance

The combined Epp-Goltermann packet gives SRT a two-stage measurement guardrail, not a new neuroscience ontology:

```text
Stage A: measurement reliability
  Delta CMRO2 direction must survive an explicit uncertainty model
  -> otherwise: indeterminate proxy

Stage B: mapping stability
  after the target direction is reliable, test whether BOLD-to-metabolic mapping
  is stable across region / task / baseline vascular-metabolic state
  -> otherwise: context-bounded proxy mapping
```

For SRT, the key point is therefore stronger than generic "measurement noise" but weaker than an ontological conclusion:

```text
proxy value != target construct
and
proxy mapping need not be context-invariant
```

BOLD, CMRO2, CBF, OEF, and related metabolic-budget readouts cannot be promoted into `Psi_f`, `d-value`, consciousness, or `L_2` claims unless reliability, mapping scope, and simpler alternatives have been declared.

## 7. Suggested / existing SRT targets

Existing targets:

```text
SRT_EXP_MEASURE_MAP.md
Neuroscience/SRT_Neural_Mechanisms.md
```

Patch record:

```text
Neuroscience/patches/SRT_Neuro_NEURAL16_BOLD_CMRO2_Uncertainty_Gate_v0_1.md
```

2026-08-15 evidence upgrade: retain NEURAL16 as the single owner patch; do not create a parallel BOLD ontology. Extend the gate from uncertainty-only language to the ordered pair `measurement reliability -> mapping stability` while preserving the indeterminate class and non-reductive boundary.
