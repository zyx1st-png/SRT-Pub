---
type: implementation_report
status: stage2_complete
claim_mode: evidence
canonical: false
---

# Implementation report

The implementation is isolated under `Experiments/choicemap_explicit_scaffolding/` and
does not import or mutate any prior experimental directory.

## Structure

- `environment_generator.py`: deterministic 16-node worlds and four families.
- `environment.py`: private regime/future-task truth, sanitized agent view, transitions,
  inert budget padding, and offline reachability oracle.
- `future_tasks.py`: frozen task catalog and exact solvability predicate.
- `search.py`: shared candidates and exact node-expansion accounting.
- `agents.py`: four main systems and five ablations.
- `choicemap.py`: multi-axis records, posterior, Pareto filter, commitment gate.
- `metrics.py`: paired episode runner and process logs.
- `analysis.py`: seed-level inference, gates, ablations, and figures.
- `tests/`: ten isolation, legality, fairness, exactness, switch, and reproducibility tests.

## Fairness

All systems receive the same legal candidate set and reserve. Early-finishing systems
consume inert interaction/model-call padding that cannot alter state or information.
Both active and total planning use are logged so the padding is auditable rather than
hidden. Agent code receives only `AgentView`; oracle and future-task methods remain on the
environment/evaluation side.

## Deviations

None. Pilot required no parameter adjustment. The final source tree, protocol, task split,
and confirmatory YAML are hashed immediately before the locked run; any later change would
invalidate that run and must be recorded as a deviation.
