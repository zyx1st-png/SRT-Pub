---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-PATH-EFFECT-DECISION-20260711
type: empirical_gate_decision
status: final_design_infeasible_v1
canonical: false
created: 2026-07-11
v1_decision_changed: false
future_tasks_executed: false
---

# Path-Effect Diagnostic Decision

## Decision: DESIGN INFEASIBLE

The decision follows the locked rule in `11_matched_endpoint_multifuture_spec.md`: use `DESIGN INFEASIBLE` if the feasibility gate fails or if the endpoint window would need post hoc widening.

### Gate audit

- A/B software and scientific completion: pass, 20/20 paths and 0 failures;
- same-A hash within seed: pass;
- A/B-only matching freeze: pass;
- at least 3/5 complete four-path groups: **fail, 0/5**;
- locked endpoint ranges: fail for every seed;
- post hoc window widening: prohibited and not performed;
- future execution authorization: not granted.

The systematic blocker was the `head_only` intervention. It plateaued at B accuracy `0.762`–`0.792` with NLL `0.621`–`0.694`, while full-network paths reached roughly `0.870`–`0.880` with NLL near `0.35`–`0.37`. Even the closest candidate tuples exceeded the accuracy tolerance by 2.34–4.61 times and the NLL tolerance by 2.38–3.47 times.

## Answers to the five terminal questions

1. **Was v1 failure mainly caused by endpoint mismatch?**
   Endpoint mismatch was a major observed defect in v1, and the new intervention set again failed to produce common support. The stronger causal claim that mismatch was the main reason for v1's negative result remains untested because no valid matched contrast was formed.

2. **Does an independent path effect exist after equal endpoints?**
   Not identified. This is neither evidence for nor evidence against a matched-endpoint path effect.

3. **Is the multi-future design better able to identify retained adaptability than a single C?**
   Conceptually it removes the single-task dependence, but empirically it was not evaluated because the B matching gate failed.

4. **Is there reason to enter an architecture-comparison stage?**
   No. Architecture comparison would add a new source of variation before the within-CNN counterfactual is identified.

5. **Should the result be interpreted as path dependence, retained plasticity, or no independent effect?**
   None. The supported interpretation is intervention-induced endpoint non-overlap and design infeasibility.

## Consequences

- v1 `SR_preC`: remains NO-GO;
- Fisher: remains lose and was not used for matching;
- four-state classification: remains unstable and was not revived;
- path-effect hypothesis: untested under matched endpoints;
- multi-future retained-adaptability outcome: not generated;
- architecture comparison: not authorized;
- CIFAR-10: not authorized;
- `SR_preC v2`: not created;
- full paper: not drafted;
- SRT canonical/Core/ChoiceMap: not modified.

Stage-4 stops with this file.
