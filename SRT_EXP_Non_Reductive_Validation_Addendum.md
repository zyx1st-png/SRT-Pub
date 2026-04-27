---
id: SRT-EXP-NON-REDUCTIVE-VALIDATION-ADDENDUM
type: canonical_addendum
tags: [Experiment, Measurement, Proxy, Non-Reductive Verification, Core 24, Validation]
status: draft_v1
layer: L2
epistemic_layer: lab
claim_mode: canonical_addendum
created: 2026-04-27
dependency: [SRT-EXP-MEASUREMAP, SRT-CORE-24-CANONICAL-MERGE-DRAFT, SRT-PSI-F-CANONICAL, SRT-D-VALUE-CANONICAL]
---

# Non-Reductive Validation Addendum

> **Purpose**: This addendum provides a merge-ready validation rule for `SRT_EXP_MEASURE_MAP.md`. It is separated only to avoid unsafe overwrite of the large measurement-map file during remote editing.

---

## Proposed Insertion Target

Recommended insertion point in `SRT_EXP_MEASURE_MAP.md`:

- before `## 5) 使用原则`; or
- as a new subsection under `## 5) 使用原则`; or
- near the existing proxy-boundary statements that say proxy conclusions must declare their operational scope.

---

## Merge-Ready Rule

### Non-Reductive Validation Rule

SRT concepts should be tested through convergent structural consequences rather than a single direct objective ruler. A proxy may support an SRT construct only when it helps distinguish selection friction, concern-weighted non-substitutability, or hardening from simpler alternatives such as loss, reward, salience, memory, convention, or generic task difficulty.

---

## Operational Consequence

A measurement package should not ask whether one variable directly “is” `Ψ_f`, `d-value`, or `L_2`. It should ask whether a set of proxies jointly detects the structured consequences expected from the construct.

| Construct | Non-reductive validation target | Simpler alternatives to control against |
|---|---|---|
| `Ψ_f` | structured transition difficulty, recovery burden, switching cost, update curvature | generic effort, task difficulty, prediction error, raw energy use |
| `d-value` | concern-weighted non-substitutability, cost-bearing, identity/stake continuity | preference intensity, reward, salience, pain, self-report |
| `L_2` hardening | local cost reduction plus global constraint plus hysteresis | memory, habit, convention, environmental stability |

---

## Minimum Acceptance Criteria

A proxy package is acceptable only if it satisfies all three conditions:

1. **Multi-proxy convergence**: at least two independent proxy classes point in the same direction.
2. **Alternative exclusion**: the result is not fully explained by a simpler construct such as reward, salience, memory, or generic task difficulty.
3. **Scope declaration**: the conclusion states the operational scope and does not back-project the proxy as the ontology itself.

---

## Failure Conditions

### F-EXP-NR-1 — Proxy Collapse

If one proxy is treated as identical to the SRT construct, the measurement layer collapses into reductionism and should be rejected.

### F-EXP-NR-2 — Alternative Explanation Failure

If a proxy package cannot distinguish `Ψ_f`, `d-value`, or `L_2` from simpler alternatives, the result should be reported as an ambiguous proxy result, not as support for SRT.

### F-EXP-NR-3 — Cross-Session Failure

If the proxy package does not show minimal stability across sessions, tasks, or perturbation contexts, its relation to the target construct remains weak.

---

## Relation to Core 24

This addendum imports only the measurement principle from `Core/SRT_Core_24_Canonical_Merge_Draft.md`. It does not import the full floor-replacement or dynamic normativity thesis into the experimental map.
