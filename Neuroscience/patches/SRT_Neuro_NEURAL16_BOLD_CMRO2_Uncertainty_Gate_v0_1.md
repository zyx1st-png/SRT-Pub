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
  - Psi_f_metabolic_proxy
  - non_reductive_validation
tags:
  - BOLD
  - CMRO2
  - fMRI
  - metabolic_proxy
  - measurement_uncertainty
  - neurovascular_coupling
---

# SRT Neuroscience Patch NEURAL16: BOLD-CMRO2 Uncertainty Gate v0.1

> Status: neuroscience measurement bridge patch.
> Canonical caution: this patch does not define `Psi_f`, metabolic cost, BOLD, CMRO2, or neurovascular coupling. It adds a reliability gate for using hemodynamic-metabolic readouts as SRT proxies.

## 0. Source anchor

Primary source:

- Ole Goltermann, Alexander Huth, and Christian Büchel. (2026). "Opposing BOLD signals and oxygen metabolism largely arise from statistical uncertainty in metabolic estimates." bioRxiv preprint, version 1. DOI: `10.64898/2026.04.21.719913`.

Local processing used the full PDF supplied at:

```text
/Users/zhangyuxin/Downloads/2026.04.21.719913v1.full.pdf
```

## 1. Why this matters for SRT

SRT uses physiological and neural measures as proxies for selection budget, metabolic burden, local friction, and anchoring dynamics. This source adds a narrow but important constraint: sign-level claims about BOLD and oxygen metabolism must not be made from group-mean direction alone when model-based CMRO2 estimates are noisy.

The usable SRT lesson is methodological:

```text
proxy direction without uncertainty support
  -> indeterminate proxy
  -> not evidence for or against an SRT construct
```

## 2. Main SRT bridge claim

### Claim NEURAL16

Hemodynamic-metabolic proxies require an uncertainty gate before they can support SRT interpretation:

```text
Delta BOLD / Delta CMRO2 sign relation
  -> usable only when Delta CMRO2 direction is statistically supported
  -> otherwise classify as indeterminate, not concordant or discordant
```

This is a lab-facing bridge rule, not a new primitive. The SRT point is narrow:

```text
metabolic-proxy ambiguity != physiological sign reversal
```

## 3. Mapping table

| Source-level result | SRT interpretation | Guardrail |
|---|---|---|
| high variability in Delta CMRO2 estimates | model-based metabolic proxies can be directionally underdetermined | do not treat group means as direct physiology |
| 77.2% of BOLD-active voxels lack significant Delta CMRO2 direction | most sign classifications should become indeterminate under uncertainty gating | indeterminate is not discordant |
| positive BOLD is mostly concordant where CMRO2 is reliable | positive BOLD may remain useful as a constrained proxy | still not direct `Psi_f` or `d` |
| negative BOLD has higher sign opposition and more uncertainty | negative BOLD needs separate mechanism-level handling | do not make one monotonic rule |
| open-data reanalysis changes interpretation | proxy claims should be reproducible and auditable | open data is a method gate, not proof of SRT |

## 4. Formal bridge

Minimum lab gate:

```text
R_metab(v) = 1
  only if Delta CMRO2(v) differs from zero under a declared error model
  and/or participant-level sign consistency survives correction.

If R_metab(v) = 0:
  class(v) = indeterminate
```

SRT use:

```text
Psi_f^{metabolic_proxy}(v,t)
  may be used only when R_metab(v,t) is declared and sufficient.
```

This is not a new canonical equation. It is a proxy-admission rule for fMRI / CMRO2 material.

## 5. Experimental / operational consequences

This patch adds a focused requirement:

```text
H-NEURAL16:
Any SRT experiment using BOLD-CMRO2 sign relations as evidence for
metabolic cost, selection budget, or local friction must report
uncertainty-gated classifications, including an indeterminate class.
```

Potential failure condition:

```text
If PET-validated or higher-SNR metabolic measures show robust widespread
sign reversal after uncertainty gating, then the current narrow reading
should be revised from "mostly proxy uncertainty" to a genuine
neurovascular-metabolic dissociation window.
```

## 6. Boundary cautions

- Do not write that BOLD is invalid.
- Do not write that BOLD and CMRO2 are always concordant.
- Do not use group-mean sign alone as evidence for metabolic direction.
- Do not collapse BOLD, CMRO2, CBF, or CBV into `Psi_f`, `d-value`, or `L_2`.
- Do not use negative BOLD as a single monotonic proxy; it remains mechanistically heterogeneous.
- Keep the source status visible: bioRxiv preprint and methodological reanalysis.

## 7. Integration status

Integrated as:

```text
SRT_EXP_MEASURE_MAP.md
  -> Hemodynamic-metabolic proxy uncertainty gate

Neuroscience/SRT_Neural_Mechanisms.md
  -> BOLD-CMRO2 uncertainty gate
```

Future synthesis should compress this into the neuroscience measurement roadmap and any experiment template that uses fMRI metabolic readouts.
