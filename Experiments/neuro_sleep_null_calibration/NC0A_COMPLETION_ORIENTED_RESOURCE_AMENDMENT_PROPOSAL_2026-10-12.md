---
id: SRT-NEURO-NC0A-COMPLETION-RESOURCE-AMENDMENT-PROPOSAL-20261012
type: audit
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: protocol
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
  - Experiments/neuro_sleep_null_calibration/H2_RUNTIME_AUDIT_2026-10-12.md
  - Experiments/neuro_sleep_null_calibration/NC0A_READINESS_AND_RESOURCE_LEDGER_2026-10-12.md
tags: [Neuroscience, NullCalibration, ResourceGate, Prospective, Draft]
---

# Prospective completion-oriented resource amendment — proposal only

**Status: NOT APPROVED; no NC-0a / NC-0 / G0 / T1 execution authorization.** This is a proposed dated change to the operational budget **only**, in response to the author's stated willingness to spend greater computing resources to finish the investigation. It does not amend the governing preregistration §6.1 until separately accepted and independently reviewed. It does not report a new synthetic, biological or statistical result.

## 1. Why a prospective amendment is appropriate

The independent H2 audit recovered verified partial progress envelopes of **71.560963 elapsed hours** and a **conditional 76.630770-hour** whole-history reconstruction but explicitly **did not establish** the comparable complete `T_PS-A`. Actual aggregate process-tree CPU hours are unknown. Neither candidate can be put into the extant `1.5*T_pred_G0 <= 2.5*T_PS-A` or `1.5*T_pred_T1 <= 1.5*T_PS-A` resource rules. Current resource verdict stays **H2 NO-GO**.

The investigator has stated the objective is to **finish the agreed science** even at higher computational cost. The defensible response is to propose **prospectively reviewed absolute resource budgets** and a fail-closed execution system, not to claim the old comparison denominator exists or waive the scientific gates.

### Proposed narrow change

**Replace only the unavailable PS-A-relative wall-time *authorization denominator* with separately approved absolute, machine-specific resource envelopes for (i) formal synthetic NC-0a, (ii) primary biological G0 and (iii) secondary T1.** Retain original PS-A time evidence as descriptive provenance, explicitly `NOT ESTABLISHED`. Preserve every planned finite-N, subset count, graph recipe, exchange kernel, 4E attempts, 200 Louvain restarts, all Q classification rules, trial pairing and initial seed contract. Do not use real G0 outputs to choose the new budget, sampler or T1 GO status.

Any design change after prespecified synthetic results or biological null inspection requires a separately dated, independent prospective review; running until a favorable result is expressly prohibited.

## 2. Budget approval checklist — none of these figures is approved yet

A budget must be signed and *externally monitored* at the correct stage:

| Gate | Workload | Budget decision required before |
|---|---|---|
| Formal NC-0a | 16 synthetic cases; 128 32E chains; 44,937,216 attempted proposals and 16,000 BFS oracle proposals | **Any formal NC-0a run** |
| Primary G0 | ~49,000 graph-null realizations; ~1,797,712,000 proposals; 9.8M Louvain trials | **NC-0 protocol freeze and first biological G0** |
| Secondary T1 | ~12,250 source-surrogate graphs; 2.45M Louvain trials plus correlation/MST rebuild | **Before inspection of *any* biological G0 null output** |

Each envelope must state absolute aggregate **inclusive wall time**, total process-tree **user+system CPU seconds**, worker concurrency, cumulative work-unit progress, process-tree peak RSS plus host RAM constraints, available/consumed disk and result storage, retry costs, watchdog sampling, excluded/suspended intervals handling, machine/OS/dependency identity, task-level deadlines, post-failure result policy and the approving reviewer.

**Suggested review baseline only for formal NC-0a (from H2 audit, not permission):** no more than **48 hours inclusive wall**, **256 CPU-hours**, **8 workers**, **10 GiB aggregate memory**, **4 GiB transient/failed outputs**, and **20 GiB free disk preserved**, with **12-hour maximum per case** and **30-minute maximum for its BFS-oracle trace**. The author has agreed to spend resources but has **not** explicitly selected these figures; the reviewer may propose a larger or smaller envelope **before execution** based on independently checked speed evidence. These are *loss limits*, not evidence that the experiment fits.

**G0 and T1 absolute ceilings: PENDING — DO NOT FILL FROM 71.56h OR 76.63h.** First benchmark the fully audited program on prespecified nonbiological representative graph sizes/topologies and time the inherited optimizer in a small non-outcome-based setting, measure memory/storage/parallel contention and set complete-task bounds with uncertainty margin. A completion-oriented proposal may choose several days or weeks rather than reject simply because it exceeds the original PS-A baseline. However **completion preference is not authorization for unlimited wall time, unlimited money or unrestricted cloud provisioning**.

Before biological null inspection, declare and record **both** an approved G0 envelope and either (a) approved T1 envelope / `T1-GO`, or (b) explicit `T1-NOT-AUTHORIZED-RESOURCE`; no optional T1 rescue after seeing G0. Do not split, omit, cherry-pick or selectively release partial animal results if a cap is hit.

## 3. Execution engineering required, not yet complete

H1 review-only `nc0a_contract_runner.py` and `nc0a_budget_preflight.py` do **not** constitute a hardened production launcher: the former has only local soft per-chain deadlines, while the latter checks the schema and deliberately cannot authorize execution.

A separately reviewed **external watchdog** independent of the computational process must enforce the aggregate limits and terminate the complete process group on any breach. Required measurements:

- UTC and monotonic/boot-inclusive wall timing; track sleep/wake events and fail closed on unapproved suspend, power failure or clock inconsistency.
- Sum user/system CPU across the actual child-process tree (not worker_count × wall time); aggregate RSS without double-counting shared pages when practicable, plus host-wide memory pressure.
- Count completed/remaining fixed cases, exact attempted proposals, failures, interrupted work and cumulative cost across the **entire** attempt, including prior failed attempts.
- Disk output/temporary files including abandoned partial writes; preserve full hashes and signed failure ledger.
- Deterministic resume or restart only per frozen recovery policy, original seed and locked case order, with *no* parameter modification based on observed metrics. A case that timed out cannot silently be declared PASS or selectively retried until it passes.
- Independent observer/auditor approval of dry-run fail-stop behavior (e.g. killed/slept/stalled subprocess and disk/memory limit simulated locally), **without formal NC-0a data**.

The initially available M1 Pro / 16 GiB / limited SSD may require more storage, sequential execution, or an approved external compute host. Migration to another CPU/OS/runtime requires a frozen reproducibility and benchmark comparability plan; do not treat Python/NumPy/BLAS/Louvain seeds as automatically byte-identical across machines.

## 4. Scientific correctness gates are unchanged

- **NC-0a is a 48-comparison low-power *drift anomaly screen***, not a certificate of equilibrium or near-uniform fixed-degree random graphs. The R5 exact three-state near-frozen-chain counterexample remains part of the audit; PASS remains `MIXING-UNRESOLVED`.
- The original 4E procedure is a finite-length start-graph-dependent topology perturbation. Any future claim about **equilibrated degree-only excess** requires a separately *prospectively* defined, Q-relevant and well-powered additional validation, not merely paying for more of the original 4E calculations.
- **NC-0 identity H3** remains essential: faithfully reconstruct and compare all 120 original panel graphs against the original builder, logged 200-Q trials and frozen data/subset hashes. NO biological null before NC-0 lock.
- Statistical result must be reported under the locked thresholds including unfavorable/invalid outcomes. Larger budgets **do not** change accept/reject thresholds, animals, targets, or evidence strength.
- A prospective independent expert must validate the proposed *budget change*, stop policy and claim boundaries; the prior Codex R5/H2 reviewer does not automatically constitute an independent second signoff.

## 5. Proposed step-by-step decision route

1. **Resource amendment peer review:** verify H2 evidence, evaluate the rationale for replacing its unrecoverable denominator, require an authorized NC-0a envelope, watchdog and fail-stop test plan; explicitly accept/reject this prospective change in PR with review HEAD. No formal experiment now.
2. **Complete H1:** verify 16-case runner contract, resource-safe orchestration, immutable seed manifest, checkpoint audit and BFS full-oracle 16-case completion criteria. Execute only bounded microtests before approval.
3. **Formal NC-0a after prospective lock and authorization:** one complete prespecified 16×8×32E synthetic diagnostic; no deletion, repeated seed-search or post-result threshold changes. Record NO-GO on failure.
4. **Prior to NC-0:** independently review and finish 120-original-graph identity/Q replay (H3), original G0/T1 code and optimizer identity, prospective benchmark uncertainty and separate absolute G0/T1 resource envelopes. Record T1 GO/NO-GO before any G0 observation.
5. **G0, then T1 if authorized:** long-running monitored, immutable, crash-safe execution; report actual measured time and all results regardless of direction, avoid claim inflation, and only then consider publication value.

## 6. Awaiting explicit approvals

- Independent review of *whether the prospective replacement* of the existing PS-A-relative resource comparison is acceptable.
- Author approval of concrete maximum time/resources for NC-0a and later G0/T1, not inferred from general willingness.
- Reviewed, fail-stop external monitor and separate locked manifest; no execution from this document.

**Disposition remains: H2 historical comparable baseline NOT ESTABLISHED; existing §6.1 RESOURCE NO-GO; prospective replacement only PROPOSED.**
