---
hook_id: HOOK-NEURO-NEURAL16-BOLD-CMRO2-UNCERTAINTY-GATE
patch_id: PATCH-NEURO-NEURAL16-BOLD-CMRO2-UNCERTAINTY-GATE
target_documents:
  - "SRT_EXP_MEASURE_MAP.md"
  - "Neuroscience/SRT_Neural_Mechanisms.md"
status: integrated
domain: neuroscience_measurement
---

# Integration Hook: NEURAL16 BOLD-CMRO2 Uncertainty Gate

## Target documents

```text
SRT_EXP_MEASURE_MAP.md
Neuroscience/SRT_Neural_Mechanisms.md
```

## Inserted sections

```text
SRT_EXP_MEASURE_MAP.md
  -> Hemodynamic-metabolic proxy uncertainty gate

Neuroscience/SRT_Neural_Mechanisms.md
  -> BOLD-CMRO2 uncertainty gate
```

## Suggested compressed paragraph

Metabolic readouts become SRT-usable proxies only after their direction survives uncertainty gating. A bioRxiv reanalysis of BOLD-CMRO2 discordance reports that most BOLD-active voxels lack statistically reliable CMRO2 direction after participant variability is considered; such voxels should be classified as indeterminate, not as evidence for physiological sign reversal. For SRT, this protects the `Psi_f^{metabolic}` bridge from reductionism: BOLD, CMRO2, and their sign relation can support metabolic-friction hypotheses only when the proxy scope, error model, and indeterminate class are explicit.

## Suggested mapping

| Measurement issue | SRT compression |
|---|---|
| noisy model-based CMRO2 direction | proxy-admission problem |
| group-mean sign discordance | insufficient for mechanism claims |
| 77.2% indeterminate after gate | ambiguous proxy result |
| positive BOLD mostly concordant when reliable | constrained proxy, not direct construct |
| negative BOLD heterogeneous | separate mechanism window |

## Do not include

- Do not claim BOLD is useless.
- Do not claim metabolic sign reversal never occurs.
- Do not identify CMRO2 with `Psi_f`.
- Do not use a single hemodynamic proxy as direct evidence for `d-value`, consciousness, or `L_2`.
- Do not hide the source status: preprint reanalysis, not peer-reviewed consensus.
