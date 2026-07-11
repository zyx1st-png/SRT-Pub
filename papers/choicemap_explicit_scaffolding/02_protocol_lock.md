---
type: preregistration
status: locked_v1
claim_mode: protocol
canonical: false
---

# Protocol lock

## Primary question

Under matched computational and interaction budgets, does an explicit ChoiceMap scaffold
preserve more genuinely reachable future options and improve performance on unforeseen
future tasks, without materially sacrificing current-task performance?

## World and splits

- Directed graph: 16 nodes; three resources; three regimes.
- Families: Stable-Reversible, Hidden-Reversible, Hidden-Irreversible,
  Hidden-Irreversible-Shift.
- Probe: cost 0.04; reliability 0.78, except the stable boundary family at 0.96.
- Irreversible commitments: correct closes 1/8 targets; wrong consumes one resource and
  closes 4/8 targets.
- Future tasks: eight frozen templates, concrete task hidden until current completion.
- Pilot: five seeds × 100 episodes × family × system.
- Confirmatory: thirty disjoint seeds × 200 episodes × family × system.
- Held-out templates and regime combinations are recorded in manifests.

## Systems

Main: Greedy, Search, OptionScalar, ChoiceMap. Ablations: C-noProbe,
C-noReversibility, C-noBranchMemory, C-immediateCommit, C-scalarized.

## Locked budgets

- Maximum decision interactions: 6 per episode; every system actually consumes six,
  with inert post-completion padding.
- Planning horizon: 2.
- Node expansions: 24 per reserved decision slot, 144 per episode for every system.
- Same world seed, future-task draw, legal actions, model, and history allowance.
- Wall-clock is supplementary and may differ.

## Locked ChoiceMap thresholds

- posterior entropy block: 0.55 nats;
- top-two probability-gap block: 0.55;
- irreversible downside block: 0.08;
- minimum information-gain/cost ratio: 1.0;
- credible regime inclusion: posterior probability > 0.10;
- worst-case acceptability floor: 0.90.

The option scalar weight is 0.01. Scalarized-ablation weights are fixed in the locked YAML.

## Hypotheses and gates

- H1/Gate A: ChoiceMap current success minus strongest baseline >= -0.03.
- H2/Gate B: after Gate A, ChoiceMap future-task success is higher than Greedy, Search,
  and OptionScalar in hidden irreversible families.
- H3: seed-level RFS AUC difference is positive.
- H4: wrong and irreversible commitments decline.
- H5: removing at least two of probe, reversibility, branch memory, or delayed commitment
  materially weakens the advantage.
- H6: advantage concentrates in hidden/irreversible/shifted worlds; a large advantage in
  Stable-Reversible triggers a fairness/leakage investigation.

Practical future-success threshold: +5 percentage points with seed-bootstrap 95% lower
bound > 0. Key secondary threshold: >=20% relative reduction in irreversible failure.

## Analysis

The seed is the independent unit. Report paired seed mean/median differences, 95%
seed-bootstrap interval, paired sign-permutation test, standardized effect, environment
interaction, ablations, held-out family views, worst-family performance, compute audit,
and failed runs. Episode-level pseudo-replication is prohibited.

## Stop and rerun rules

Stop as design failure for leakage, budget mismatch, >1% failed runs, incomplete logs,
ceiling/floor across all systems, or unreliable exact reachability. Failed runs remain in
`failed_runs.csv`. Rerun is permitted only for a documented software fault, never for an
unfavorable result. A post-lock code/config change is a deviation and requires a new hash;
it cannot silently replace the locked run.

## Decision

`GO` requires H1, practical H2 with positive interval, superiority over Search and
OptionScalar, direction consistency in most hidden irreversible settings, no single-task
driver, at least two weakening ablations, and clean budget/leakage audits.
`CONDITIONAL GO` is limited, stable improvement below the full threshold or confined to
the shift family. `NO-GO` covers failure of noninferiority or strong-baseline superiority.
Ceiling/floor, leakage, invalid reachability, or incomplete execution is
`INCONCLUSIVE / DESIGN FAILURE`.

