---
type: pilot_report
status: completed
claim_mode: diagnostic_evidence
canonical: false
---

# Pilot report

## Status

Completed: 5 pilot seeds × 4 environment families × 9 systems × 100 episodes =
18,000 episodes. All ten automated tests passed. Failed runs: 0. Smoke and pilot are
diagnostic/calibration stages and are not evidence for the confirmatory hypotheses.

## Software and audit findings

- Determinism, legal actions, exact reachability, regime isolation, future-task isolation,
  oracle isolation, ablation switches, and reproducibility passed.
- Every system consumed exactly 6 environment interactions and 144 node expansions per
  episode; active use is logged separately from inert post-completion padding.
- Required raw logs were written as true Parquet (`PAR1`) using the documented fallback
  writer in this dependency-limited runtime.
- Leakage audit: pass. No hidden regime, concrete future task, or RFS oracle field appeared
  in `AgentView`.
- No system was at a universal floor. Reversible-family current/future success was about
  0.896–0.898, providing a boundary condition with no ChoiceMap advantage rather than a
  perfect ceiling.

## Behavior checks

In hidden irreversible families, full ChoiceMap used about 2.98 probes without shift and
3.94 with shift. It did not degenerate into never committing. `C-noBranchMemory` probed
five times and then took the safe route at the locked step limit; this is an intended
mechanism-removal behavior and remains visible in the process logs.

No advantage appeared in Stable-Reversible. The diagnostic (non-confirmatory) projection
against the strongest baseline was:

- current-task difference: +3.15 percentage points;
- future-task difference in hidden irreversible families: +29.4 points;
- seed-bootstrap 95% interval: +25.6 to +33.4 points;
- RFS AUC difference: +0.203;
- irreversible-failure difference: -31.4 points;
- three ablations weakened future success by at least 3 points.

The five-seed paired permutation p-value is resolution-limited (approximately 0.064) and
is not interpreted. The locked confirmatory stage uses thirty independent seeds.

## Parameter decisions

No parameter was changed after pilot. The task was neither universally easy nor universally
hard; the Stable-Reversible boundary behaved as preregistered; budgets and leakage guards
held; and full ChoiceMap did not collapse into endless probing. Therefore the pilot YAML
values were copied unchanged into `configs/confirmatory_locked.yaml`.

The confirmatory configuration, experiment source tree, future-task split, and protocol
document are SHA256-locked in `manifests/protocol_hashes.json`. Confirmatory seeds remain
disjoint from calibration and pilot seeds.

