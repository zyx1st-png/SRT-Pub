---
id: SRT-NEURO-NEURAL25-INTEGRATION-HOOK
type: integration_hook
status: pending
canonical: false
claim_level: P3-P4
source_patch: Neuroscience/patches/SRT_Neuro_NEURAL25_Memory_as_Historical_Selection_Bias_v0_1.md
created: 2026-08-09
---

# NEURAL25 Integration Hook — Memory as historical selection bias

## Trigger

Reopen when any of the following workstreams is active:

1. `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` L2 / learning revision;
2. `Core/SRT_Core_24_Discriminating_Predictions.md` P24-3 experimental hardening;
3. a neuroscience experiment explicitly separating representation, control authority and historical write-back;
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

## Primary future experiment

Use a matched-current-state / different-history design. Match immediate reward, reliability, performance, fitted strategy weight and representation-strength proxies; then test whether deeper history still predicts alternative-path accessibility, switching cost and perturbation hysteresis.

## Failure trigger

If history depth adds no predictive value beyond current policy/representation variables for alternative accessibility, switching cost or hysteresis, downgrade NEURAL25 to ordinary memory/habit translation and do not claim SRT-specific L2 hardening.
