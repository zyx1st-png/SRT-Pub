---
type: final_decision
status: completed
claim_mode: adjudication
canonical: false
---

# Final decision: GO

## Decision

**GO—for a second-stage cross-environment engineering validation only.**

This is a narrow GO. It does not promote the scaffold to canonical theory, does not prove
SRT, and does not show that the full ten-part ChoiceMap is uniquely optimal.

## Required questions

1. **Did ChoiceMap improve unforeseen future-task success without harming the current
   task?** Yes. Current success was noninferior (+3.28 points vs the strongest baseline),
   while hidden-irreversible future success improved by +33.21 points.
2. **Did it preserve more genuinely reachable future tasks?** Yes. RFS AUC improved by
   +0.2129 and irreversible failure fell by 69.46% relative.
3. **Did it exceed ordinary compute-matched search?** Yes, by +33.21 future-success points
   under identical interaction, planning, and node-expansion budgets.
4. **Did it exceed a scalar option-preservation reward?** Yes, by +33.21 points against
   the locked OptionScalar baseline.
5. **Which modules were necessary?** Reversibility metadata, delayed commitment, and the
   non-scalarized rule were supported in this implementation. Probe and branch memory were
   not necessary for the future-success metric; their ablations actually preserved more
   future success while giving up some current performance.
6. **Was the advantage confined to hidden/irreversible settings?** Yes in this test. The
   Stable-Reversible difference was essentially zero (-0.05 points).
7. **Is a cross-environment second stage warranted?** Yes, specifically to challenge the
   safe-route alternative, tune a genuinely strong scalar/risk-sensitive baseline without
   post-result bias, and test whether branch memory helps when old branches must actually
   be reactivated.
8. **What can this support about SRT?** Only a scoped P4 bridge: explicit reversibility and
   commitment structure can improve a current/future trade-off in a designed synthetic
   world. It cannot support SRT ontology, “selection precedes existence,” a complete
   selection operator, consciousness, d-value, Psi_f, Fisher cost, or the prior failed
   resynchronization program.

## Why GO is retained despite the ablation caveat

All locked GO gates passed: noninferiority, practical future advantage with positive
seed-bootstrap lower bound, superiority over Search and OptionScalar, direction consistency,
task/regime/seed robustness, two-plus weakening mechanism removals, and clean budget/leakage
audits. The conservative ablations do not dominate full ChoiceMap on both objectives:
they preserve more future success but give up 8–9 current-success points relative to full
ChoiceMap. The correct conclusion is therefore a narrow engineering GO with an explicit
mechanism qualification, not a universal or ontological GO.

## Next-stage falsification target

The next experiment should add a preregistered constrained/risk-sensitive search baseline
that is allowed to choose the safe route while meeting the same current-task margin. If
that baseline matches the full current/future frontier, the independent value of the
full ChoiceMap architecture should be downgraded or rejected.

