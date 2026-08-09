---
id: SRT-NEURO-NEURAL25-INTEGRATION-HOOK
type: integration_hook
status: active
canonical: false
claim_level: P3-P4
claim_mode: evidence
layer: operations
epistemic_layer: os
integration_status: pending
landing_ledger:
  - target: "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
    state: pending
    blocked_by: "Reopen only when the L2 / learning synthesis is active and the final source bibliographic status is reviewed."
  - target: "Core/SRT_Core_24_Discriminating_Predictions.md"
    state: pending
    blocked_by: "Requires calibration, power simulation, comparator-model recovery, fixed perturbation implementation and preregistration before P24-3 hardening."
  - target: "03_Bridges/SRT_Selection_Event_CompactCore.md"
    state: pending
    blocked_by: "Only a bounded CG-1 / CG-2 / CG-4 example may be added; do not redefine the selection-event ladder from this neuroscience case."
source_patch: Neuroscience/patches/SRT_Neuro_NEURAL25_Memory_as_Historical_Selection_Bias_v0_1.md
experimental_protocol: Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md
protocol_status: pilot_ready_v0_1
created: 2026-08-09
updated: 2026-08-09
---

# NEURAL25 Integration Hook — Memory as historical selection bias

## Current protocol state

The independent P4 protocol now exists at:

`Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md`

It freezes the conceptual experiment architecture, H1–H5, comparator models M0–M3, matching logic, failure classes, and preregistration gates. It is **not yet the formal sample-size lock**; Stage-0 model recovery, an independent calibration cohort, power simulation, exact perturbation implementation, and ethics approval remain required before a confirmatory animal cohort.

## Trigger

Reopen when any of the following workstreams is active:

1. `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` L2 / learning revision;
2. `Core/SRT_Core_24_Discriminating_Predictions.md` P24-3 experimental hardening;
3. execution of `SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md` Stage 0–3;
4. a memory-theory section in the book or philosophy layer asks whether memory is exhausted by representation.

## Minimal surviving claim

> Memory is not exhausted by retained content. In action-guiding systems, historical traces can have causal efficacy by changing future candidate accessibility, effective control weight, switching cost and hysteresis.

## Required guardrail

Do not integrate as `memory = selection weight` or `memory is not representation`.

Keep four distinctions explicit:

```text
content representation
!= candidate accessibility
!= control authority
!= historical path restructuring
```

## Frozen experimental wedge

Use a matched-current-state / different-history design. Match immediate reward, reliability, performance, fitted strategy weight and representation-strength proxies; then test whether deeper history still predicts alternative-path accessibility, switching cost and perturbation hysteresis.

The strong SRT-facing result additionally requires the P24-3 triple signature:

```text
local trained-path efficiency
+
alternative-path constraint
+
hysteresis
```

and out-of-sample discrimination against a flexible latent-history comparator. A residual history coefficient alone is not an SRT-specific result.

## Failure trigger

If history depth adds no predictive value beyond current policy/representation variables for alternative accessibility, switching cost or hysteresis, downgrade NEURAL25 to ordinary memory/habit translation and do not claim SRT-specific L2 hardening.

If history matters but the flexible ordinary latent-history comparator predicts held-out animals as well as or better than the constrained shared-hardening model, retain only the weaker statement that history matters; do not claim SRT-specific structural advantage.
