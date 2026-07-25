---
hook_id: HOOK-NEURO-NEURAL17-HGA-SPIKE-DISSOCIATION-GATE
patch_id: PATCH-NEURO-NEURAL17-HGA-SPIKE-DISSOCIATION-GATE
domain: neuroscience_measurement
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: integration_hook
id: HOOK-NEURO-NEURAL17-HGA-SPIKE-DISSOCIATION-GATE
status: active
integration_status: landed
landing_ledger:
  - target: "SRT_EXP_MEASURE_MAP.md"
    state: landed
    anchor: "High-gamma"
  - target: "Neuroscience/SRT_Neural_Mechanisms.md"
    state: landed
    anchor: "High-gamma"
closure_audit: Operations/Audits/Hook_Closure_Audit_2026-07-25.md
---

# Integration Hook: NEURAL17 HGA-Spike Dissociation Gate

## Target documents

```text
SRT_EXP_MEASURE_MAP.md
Neuroscience/SRT_Neural_Mechanisms.md
```

## Inserted sections

```text
SRT_EXP_MEASURE_MAP.md
  -> High-gamma local-spike dissociation gate

Neuroscience/SRT_Neural_Mechanisms.md
  -> High-gamma/spike dissociation gate
```

## Suggested compressed paragraph

High-gamma activity is SRT-usable only after its proxy target is declared. A 2026 Nature study trained macaques to decouple intracortical HGA and spike rate recorded from the same electrode, while showing that HGA related more closely to distributed co-firing than to nearby local spikes alone. For SRT, HGA should therefore default to a mesoscale input-synchrony / postsynaptic-integration proxy, not a direct local-output ruler. Claims that use HGA as evidence for local firing, selection bandwidth, `Psi_f`, `d`, ignition, or consciousness must add spike/population/perturbation controls and specify scope.

## Suggested mapping

| Measurement issue | SRT compression |
|---|---|
| same-electrode HGA and spikes can be decoupled | local-output proxy caution |
| HGA tracks distributed co-firing | mesoscale synchrony / input-integration window |
| HGA remains behaviorally informative | useful proxy, not direct construct |
| ONF/BMI perturbation context | strong dissociation evidence, scoped generalization |

## Do not include

- Do not claim HGA is useless.
- Do not claim local spikes never contribute to HGA.
- Do not use HGA alone as direct evidence for `Psi_f`, `d-value`, `T_dir`, `L_2`, consciousness, `C_wave`, or `D_align`.
- Do not ignore modality and cortical-area differences.
