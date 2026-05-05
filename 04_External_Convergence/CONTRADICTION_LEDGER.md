---
id: SRT-CONTRADICTION-LEDGER
type: ledger
tags: [ExternalConvergence, Pressure, Contradiction]
status: active_v1
layer: meta
epistemic_layer: lab
claim_mode: ledger
canonical: false
---

# Contradiction Ledger

This ledger records counterexamples, failed predictions, pressure cases, and situations where another theory explains the data better.

Its purpose is to prevent confirmation bias.

Pressure does not automatically mean SRT has failed. It can mean the relevant claim should be downgraded, scoped, split by level, routed to bridge status, or revised.

## Ledger

| ID | Domain | SRT Construct Pressured | Pressure Type | Status | Summary | Related Evidence Card |
|---|---|---|---|---|---|---|
| CL-IG-FISHER-GENERIC-DIFFICULTY | mathematics / information geometry | `Psi_f` projection; selection cost | downgrade pressure | active_v1 | Fisher-geometric quantities may collapse into generic statistical distance, optimization stiffness, model identifiability, or analyst-chosen parameterization rather than SRT-specific `Psi_f` / payability. | [`EC-IG-FISHER-PSIF`](Mathematics_Information/EC-IG-Fisher-PsiF.md) |
| CL-THERMO-LANDAUER-OVEREXTENSION | physics / thermodynamics | selection cost; `Psi_f` projection | downgrade pressure | active_v1 | Landauer-style thermodynamic cost may be overextended from physical erasure / reset / durable record formation to all forms of selection, including reversible computation, purely formal selection, ordinary choice, or metaphorical constraint. | [`EC-THERMO-LANDAUER-SELECTION-COST`](Physics_Thermodynamics/EC-THERMO-LANDAUER-SELECTION-COST.md) |

## Pressure Details

### CL-IG-FISHER-GENERIC-DIFFICULTY

This is not a refutation of SRT. It is a downgrade pressure on the Fisher-`Psi_f` interface proposed in [`EC-IG-FISHER-PSIF`](Mathematics_Information/EC-IG-Fisher-PsiF.md).

The pressure is that Fisher-geometric quantities may measure generic statistical distance, optimization stiffness, model identifiability, or analyst-chosen parameterization rather than SRT-specific transition burden, payability, or `Psi_f`.

If a Fisher proxy cannot distinguish SRT-relevant transition burden from generic model difficulty, the related evidence card should be downgraded to E1 or retained as a bridge note rather than treated as structural convergence.

The Fisher metric must not be extended directly to `d-value` unless stake-coupled concern is independently operationalized through consequence return, non-substitutability, and relevant system-level burden.

### CL-THERMO-LANDAUER-OVEREXTENSION

This is not a refutation of SRT. It is a downgrade pressure on the Landauer-selection-cost interface proposed in [`EC-THERMO-LANDAUER-SELECTION-COST`](Physics_Thermodynamics/EC-THERMO-LANDAUER-SELECTION-COST.md).

The pressure is that Landauer-style thermodynamic cost may be overextended from physical erasure, reset, and durable record formation to all forms of selection, including reversible computation, purely formal selection, ordinary choice, or metaphorical constraint.

Landauer principle applies most directly to logically irreversible physical information processing, especially erasure / reset under specified thermodynamic conditions. Reversible computation is a pressure case because not every information transformation requires logical erasure at the step being analyzed.

Ordinary engineering dissipation may explain observed costs without supporting an SRT-specific selection-cost interface. Purely formal selection or mathematical restriction over possibilities does not automatically entail Landauer cost.

If later cards cannot separate physical erasure / record cost from loose metaphor, [`EC-THERMO-LANDAUER-SELECTION-COST`](Physics_Thermodynamics/EC-THERMO-LANDAUER-SELECTION-COST.md) should be downgraded toward E1 or routed to bridge note status.

## Required Practice

- Hard rule: For every 3 accepted E2+ supportive evidence cards in a domain, at least 1 pressure / contradiction entry must be registered for that same domain.
- Hard rule: If this condition is not met, that domain must not be summarized as externally convergent in [`EVIDENCE_INDEX.md`](EVIDENCE_INDEX.md).
- Every future evidence domain should include at least one pressure or contradiction entry.
- Strong support entries should be paired with a weakening condition.
- Alternative explanations should be preserved rather than hidden.
- If an external result only supports a bridge, do not upgrade it into a formal anchor.
