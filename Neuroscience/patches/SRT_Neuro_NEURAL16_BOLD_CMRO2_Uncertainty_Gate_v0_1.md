---
patch_id: PATCH-NEURO-NEURAL16-BOLD-CMRO2-UNCERTAINTY-GATE
source_ids:
  - SRC-2026-04-26-NEURO-BOLD-CMRO2-UNCERTAINTY-BIORXIV
domain: neuroscience_measurement
claim_level: bridge
canonical_status: domain_bridge_integrated
status: patch
target_documents:
  - "SRT_EXP_MEASURE_MAP.md"
  - "Neuroscience/SRT_Neural_Mechanisms.md"
related_claims:
  - hemodynamic_metabolic_proxy
  - BOLD_CMRO2_relation
  - metabolic_uncertainty_gate
  - proxy_mapping_stability
  - Psi_f_metabolic_proxy
  - non_reductive_validation
tags:
  - BOLD
  - CMRO2
  - fMRI
  - metabolic_proxy
  - measurement_uncertainty
  - mapping_stability
  - neurovascular_coupling
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_patch
id: PATCH-NEURO-NEURAL16-BOLD-CMRO2-UNCERTAINTY-GATE
---

# SRT Neuroscience Patch NEURAL16: BOLD-CMRO2 Reliability and Mapping-Stability Gate

> Status: neuroscience measurement bridge patch.
> 2026-08-15 evidence upgrade: the original uncertainty gate is retained and extended into an ordered two-stage proxy-admission rule: `measurement reliability -> mapping stability -> SRT interpretation`.
> Canonical caution: this patch does not define `Psi_f`, metabolic cost, BOLD, CMRO2, neurovascular coupling, consciousness, or neuronal activity. It constrains how hemodynamic-metabolic readouts may be used as SRT proxies.

## 0. Source anchors

### 0.1 Target primary study

Samira M. Epp, Gabriel Castrillón, Beijia Yuan, Jessica Andrews-Hanna, Christine Preibisch, and Valentin Riedl. "BOLD signal changes can oppose oxygen metabolism across the human cortex." *Nature Neuroscience* 29, 1225-1236 (2026). DOI: `10.1038/s41593-025-02132-9`; version of record 2025-12-16.

Epp et al. report that about 40% of voxels with significant task-related BOLD changes show estimated CMRO2 changes of the opposite sign, with stronger discordance for negative BOLD and prominent effects in default-mode regions. They also report different CBF/OEF contributions in concordant versus discordant voxels, motivating the hypothesis that neurovascular-metabolic coupling may vary with regional and task state.

### 0.2 Statistical reanalysis

Ole Goltermann, Alexander Huth, and Christian Büchel. "Opposing BOLD signals and oxygen metabolism largely arise from statistical uncertainty in metabolic estimates." eLife Reviewed Preprint v1 (2026-06-23). DOI: `10.7554/eLife.111743.1`; original bioRxiv DOI: `10.64898/2026.04.21.719913`.

The eLife assessment rates the work as `important` with `convincing` evidence. The reanalysis argues that the widespread sign-discordance estimate is strongly inflated by uncertainty in model-based CMRO2 estimates: 77.2% of analysed BOLD-active voxels lack statistically reliable CMRO2 direction under the group-level gate. Public review also preserves an important caveat: a non-significant CMRO2 effect may reflect either insufficient power or a genuine near-null effect, so `indeterminate` is an epistemic classification rather than evidence of no metabolic change.

## 1. Why this matters for SRT

SRT uses physiological and neural measurements only as proxies for higher-level constructs such as selection budget, metabolic burden, local friction, anchoring dynamics, or task-state constraints. The Epp-Goltermann dispute exposes two separable failure modes that must not be collapsed:

```text
Failure mode A: target-direction uncertainty
  -> the inferred metabolic change itself is not statistically reliable

Failure mode B: proxy-mapping instability
  -> even when the target direction is reliable, the mapping from BOLD to metabolism
     may depend on region, task, baseline OEF/CBF/CBV, or other physiological context
```

The usable SRT lesson is methodological:

```text
proxy direction without uncertainty support
  -> indeterminate proxy

reliable proxy direction without declared mapping scope
  -> context-bounded proxy

only after both gates
  -> eligible for bounded SRT interpretation
```

Neither failure mode by itself supports an ontological claim.

## 2. Main SRT bridge claim

### Claim NEURAL16-A: Measurement Reliability Gate

Hemodynamic-metabolic proxies require an uncertainty gate before sign-level interpretation:

```text
Delta BOLD / Delta CMRO2 sign relation
  -> usable only when Delta CMRO2 direction is statistically supported
  -> otherwise classify as indeterminate, not concordant or discordant
```

Minimum lab gate:

```text
R_metab(v) = 1
  only if Delta CMRO2(v) differs from zero under a declared error model
  and/or participant-level sign consistency survives a declared correction rule.

If R_metab(v) = 0:
  class(v) = indeterminate
```

`indeterminate` means that the available data do not identify a reliable direction. It does not mean `Delta CMRO2 = 0`.

### Claim NEURAL16-B: Proxy-Mapping Stability Gate

Passing the uncertainty gate does not license a universal BOLD-to-metabolism mapping. A proxy relation must also declare and test the context in which it is assumed to hold.

At minimum, a BOLD-based metabolic interpretation should ask whether the relation is stable across the relevant combination of:

- positive versus negative BOLD response;
- cortical region / network;
- task or cognitive state;
- baseline OEF / CBF / CBV regime;
- acquisition and quantitative-model assumptions;
- participant or session when longitudinal inference is intended.

Operationally:

```text
reliable target direction
  + stable or explicitly modelled proxy-target relation in the declared context
  -> bounded proxy admission

reliable target direction
  + context interaction / mapping reversal not modelled
  -> context-bounded or ambiguous proxy result
```

This is a stability/scope requirement, not a new canonical SRT equation.

## 3. Combined evidence map

| Evidence | SRT interpretation | Guardrail |
|---|---|---|
| Epp et al. report widespread raw BOLD-CMRO2 sign discordance | BOLD sign should not be treated as a transparent identity with metabolic direction | do not convert the reported ~40% directly into a universal physiological reversal rate |
| Goltermann et al. find large variability in Delta CMRO2 estimates | model-based metabolic direction can be underdetermined | apply uncertainty gate before sign classification |
| 77.2% lack statistically reliable Delta CMRO2 direction under the group-level reanalysis gate | most voxels in that analysis become epistemically indeterminate | indeterminate is neither concordant nor discordant and is not proof of zero metabolism |
| positive BOLD is mostly concordant where Delta CMRO2 is classifiable | positive BOLD can remain a useful constrained proxy | still not direct `Psi_f`, `d`, consciousness, or neuronal-activity identity |
| negative BOLD remains more heterogeneous | negative BOLD needs separate mechanism-level treatment | no single monotonic rule for negative BOLD |
| Epp et al. report different CBF/OEF contributions and task-sensitive patterns | state-dependent mapping remains a live mechanism hypothesis | test mapping stability only after target-direction reliability is established |
| open-data reanalysis materially changes the interpretation | proxy claims should be auditable and reproducible | open data is a method gate, not proof of SRT |

## 4. Ordered proxy-admission rule

For SRT experiments using hemodynamic-metabolic measurements, use the following order:

```text
1. Measurement reliability
   Is the target direction/effect supported under a declared uncertainty model?

2. Mapping stability
   Is the proxy-target relation stable, or explicitly modelled as context-dependent,
   across the contexts required by the claim?

3. Construct discrimination
   Does the admitted proxy package distinguish the intended SRT construct from
   simpler physiological, behavioral, vascular, task, or arousal explanations?

4. SRT interpretation
   Only then may the result enter a bounded bridge claim.
```

This sequence is compatible with the repository's existing non-reductive validation rule and the generic requirement that proxy packages show basic stability across sessions, tasks, and perturbation contexts.

## 5. Experimental / operational consequences

### H-NEURAL16-A: uncertainty-gated classification

Any SRT experiment using BOLD-CMRO2 sign relations as evidence for metabolic cost, selection budget, or local friction must report:

- the error model for Delta CMRO2;
- participant- and/or voxel-level uncertainty;
- correction rule;
- concordant / discordant / indeterminate counts;
- sensitivity to activation-mask and model choices where relevant.

### H-NEURAL16-B: mapping-stability audit

If the claim generalizes a BOLD-based proxy across tasks, regions, states, or sessions, the analysis must test proxy-by-context interactions or provide a validated context-specific calibration. A pooled relation is insufficient when the target study itself motivates state- or region-dependent coupling.

Useful falsification design:

```text
matched reliable Delta CMRO2 direction
+ different task / baseline OEF / network context
-> test whether BOLD sign and magnitude preserve the declared mapping
```

If the mapping changes materially under matched target direction, the proxy must be scoped to context rather than promoted as a general readout.

## 6. Failure / revision conditions

The current narrow reading should be revised if any of the following occurs:

1. PET-validated or higher-SNR metabolic measurements show robust widespread sign reversal after uncertainty gating; this would strengthen a genuine neurovascular-metabolic dissociation window.
2. High-powered repeated-measures studies show that the BOLD-to-CMRO2 mapping is stable across the relevant task, region, and baseline-state contrasts; the mapping-stability caution could then be narrowed.
3. The reported Epp task/OEF/CBF interactions disappear once Delta CMRO2 reliability is controlled; the mapping-stability component should then be downgraded toward an uncertainty-only interpretation.
4. Conversely, reliable within-voxel target effects systematically switch BOLD mapping across task or physiological state; the context-dependent mapping component would be strengthened.

## 7. Boundary cautions

- Do not write that "40% of fMRI is wrong."
- Do not write that Epp et al. established a universal 40% physiological sign reversal.
- Do not write that the Goltermann reanalysis proves BOLD is always reliable.
- Do not treat `indeterminate` as evidence of a true null metabolic response.
- Do not use group-mean sign alone as evidence for metabolic direction.
- Do not collapse BOLD, CMRO2, CBF, OEF, or CBV into `Psi_f`, `d-value`, `T_dir`, consciousness, neuronal activity, or `L_2`.
- Do not use negative BOLD as a single monotonic proxy; it remains mechanistically heterogeneous.
- Do not infer state-dependent neurovascular coupling solely from apparent sign discordance before measurement reliability is established.
- Keep source status visible: Epp et al. is a peer-reviewed Nature Neuroscience primary study; Goltermann et al. is an eLife Reviewed Preprint with public assessment and reviews, not a revised Version of Record.

## 8. Integration status

Existing integration remains:

```text
SRT_EXP_MEASURE_MAP.md
  -> Hemodynamic-metabolic proxy uncertainty gate

Neuroscience/SRT_Neural_Mechanisms.md
  -> BOLD-CMRO2 uncertainty gate
```

2026-08-15 patch-level upgrade:

```text
NEURAL16
  Measurement Reliability Gate
    -> indeterminate class when target direction is unsupported

  Mapping Stability Gate
    -> context-bounded proxy when proxy-target mapping is not stable or not modelled

  Non-reductive Interpretation Gate
    -> no direct promotion into SRT constructs
```

Owner-document wording should be refreshed in the next governed synthesis / split-refresh pass so the formal owner text and connector-safe split copies inherit the same two-stage framing without creating a parallel mechanism namespace.
