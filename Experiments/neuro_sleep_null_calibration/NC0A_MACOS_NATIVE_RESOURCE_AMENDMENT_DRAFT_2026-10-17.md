---
id: SRT-NEURO-NC0A-MACOS-RESOURCE-AMENDMENT-DRAFT-20261017
type: proposal
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
title: NC-0a macOS native resource and safety amendment proposal
date: 2026-10-17
scope: prospective engineering proposal only
dependency:
  - Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
tags: [Neuroscience, SyntheticNull, ResourceGate, Draft]
---

# NC-0a macOS native resource and safety amendment proposal

**This draft has no execution authority.** Policy V1 remains bound to `CGROUP_V2_HARD`. A separately versioned macOS policy schema is now implemented, but the formal launcher must continue rejecting it until this amendment has independent approval, the absolute budget is approved, the production trust anchor and external ledger are installed, and a fresh signed policy binds the revised limits and code. A test key or a local self-signature is not an approval.

## Scope and rationale

The NC-0a preregistration requires a prospectively locked absolute resource budget, including peak RAM and failed-case behavior. It does not prescribe Linux or cgroup v2. The cgroup requirement was added later to address R7's measured short-lived RSS spike that escaped polling. A macOS backend could preserve the scientific protocol while accepting a weaker *machine-protection* guarantee, but only if that difference is explicit and independently approved. A sampled RSS maximum must never be reported as a hard memory limit or a true process-tree peak.

The scientific contract remains unchanged: 16 fixed synthetic cases, eight chains per case, 32E proposals per chain, E/2E/4E/8E/32E checkpoints, 16 independent 1,000-proposal BFS-oracle streams, 48 paired comparisons and existing thresholds, fixed formal seeds, and the `MIXING-UNRESOLVED` interpretation. No result-dependent retry or null-result-dependent T1 decision is allowed. This proposal does not authorize G0 or T1 and does not replace biological data identity requirements.

## Bounded evidence behind the proposal

On 2026-10-17, an Apple M1 Pro with 16 GiB RAM, macOS 15.7.4 and Python 3.11.15 ran the separate-seed `nc0a_macos_feasibility_probe.py` (root 8062026). The earlier R9c disk snapshot was about 26 GiB free; R10 later measured about 32.2 GiB free. Both are below the proposed 40 GiB formal launch minimum. Every counted run was nonformal and wrapped by the watchdog with strict small caps. The largest fixture used N=3900 and about 31,200 edges. R9c short parallel probes allowed at most 5,000 proposals per worker; R10 added an 8E multiworker run, still far short of 32E.

| Family | 2-worker proposals/s; sampled group RSS | 4-worker proposals/s; sampled group RSS | 8-worker proposals/s; sampled group RSS | One-chain 1E -> 4E proposals/s |
| --- | ---: | ---: | ---: | ---: |
| BA-like | 3,845; 127 MiB | 7,401; 203 MiB | 9,863; 363 MiB | 2,266 -> 2,194 |
| Factor-MST | 5,715; 467 MiB | 10,498; 482 MiB | 11,112; 576 MiB | 2,795 -> 2,413 |

These are timing observations, not 32E or full-battery time bounds. Four workers retain much of the measured throughput while reducing sampled RSS, CPU contention and pressure versus eight. The 1E and 4E probes saved and SHA-256-checked full chain JSON reports (about 1.1–2.2 KiB each); measured save/fsync took about 2–7 ms per report, but full formal audit cost was not measured. R10 reproduced the unknown-member stops and confirmed the process-table title races and a lingering `resource_tracker` lifecycle race; see the implementation snapshot below. The original stopped run is not counted as a successful protected computation.

Local raw summary SHA-256 anchors were `d0627cf334eacada41a88e07cf18b9fa93cbcbc0d096b5c5f7720746f34625b6`, `903795a4e7e49d2ae64d9c1bb670ae72a29d0a274773757473723dbd9e19fe8d`, and `ab2752e486007931a38daf0bcbd5ee7868f22a799ffaed471cfed62aea0d0d8b`. They reside in temporary local directories and are not durable remote artifacts; the committed bounded probe provides a repeatable method. The R7 transient 136,282,112-byte child RSS event against an 83,886,080-byte cap was missed by polling at 11,976,704 bytes, so these sampled values cannot resolve the short-peak risk.

## Candidate operating envelope for independent review

| Control | Proposed prospective value | Enforcement and limitation |
| --- | --- | --- |
| Compute workers | 4 actual computation workers maximum | Count by verified role and process identity; monitor parent, workers, and helpers. An unknown group member fails closed. The observed Python-spawn exit-race false stop needs repair before authorization. |
| Cumulative wall / CPU | 72 hours elapsed wall; 288 aggregate CPU-hours | Count across every invocation, failed attempt, restart, and recovery under one experiment UUID. Wall accounting includes sleep; monotonic/UTC divergence or unreadable accounting fails closed. Values are candidates, not approved limits or a completion guarantee. |
| Per-case / oracle | 12 elapsed hours per case; 30 minutes per oracle stream | Prospective loss limits; stop and audit before any increase. Preserve failed records. |
| Memory | 4 GiB **sampled** process-group RSS ceiling, stop at or before 90%; host memory-pressure free percentage stop at 20%; require at least 2 GiB free swap at launch and stop when sampled free swap reaches 1 GiB or sampled swap growth reaches 2 GiB, whichever comes first | RSS sampling may miss short spikes, shared pages may be double-counted, and host pressure/swap telemetry is not a process hard cap. These are abort triggers, not a guaranteed peak limit. Record sample interval and raw samples. An OS OOM kill, swap storm, severe pressure, or missing telemetry is a failed/unknown run requiring audit. The current examined Mac had less than 1 GiB free swap and fails this proposed launch rule. |
| Disk | 4 GiB run-output cap; at least 40 GiB free on the internal boot volume before launch and 30 GiB maintained; monitor output and boot/swap volumes separately | Stop before reserve breach or failed fsync. External output storage does not remove boot-volume swap risk. The R10 snapshot had about 32.2 GiB free and still fails this proposed preflight. |
| Power / thermal | AC power, prevent idle sleep with an owned assertion, monitor sleep divergence and thermal warnings | No claim of avoiding power loss or forced sleep. Interrupted work is recovered only under the frozen task-level rule. |

The 72-hour and 288-CPU-hour figures are a **review candidate** informed by bounded 1E–8E probes. The 8E evidence is one four-worker run on the largest factor-MST fixture, not a representative sample of all 16 cases or the full 32E path. The candidate leaves substantial nominal room for longer-chain slowdown, case diversity, checkpoint work, host contention, and recovery, but the probes do not establish a statistical upper bound or prove that this allowance is sufficient. The historical `T_PS-A` remains unverified and cannot justify these numbers. Before approval, run further representative nonformal probes, freeze the host load and exact dependency environment, verify storage capacity, and have an independent reviewer accept both the estimated cost and possible incomplete-run loss. A different approved budget may be appropriate; it must be set before the formal run and signed anew.

## Required implementation and review before any formal macOS launch

1. Introduce a separately named `MACOS_SAMPLED_PRESSURE` policy only under a versioned, dated amendment. Keep `CGROUP_V2_HARD` semantics intact; never alias the two. Preflight and launcher must require a signed policy whose backend, thresholds, watchdog/protocol/preregistration/dependency hashes, HEAD, experiment UUID, and approved machine identity match. Reject legacy or unsigned policy on the new path.
2. Verify actual worker classification through spawn and exit races at two, four, and eight workers; retain fail-closed handling of unknown group members and record any benign false stop as a failed, costed invocation. Add native host pressure events if practical, but keep explicit that neither events nor polling bounds transient RSS.
3. Test stop-and-kill on sustained RSS, pressure, CPU, wall, disk, worker crash, parent/watchdog crash, sleep divergence, OOM/forced kill, and missing telemetry. Confirm no orphan workers and durable failed/unknown records. A short-lived unobserved memory spike must remain documented as residual risk; do not assert it has been solved by polling frequency.
4. Freeze the macOS version, Python and full dependency closure, CPU architecture, executable and source hashes, output schema, and exact result-verification procedure. Use an independently protected production public-key fingerprint, approval, authorization-use ledger, and off-machine log anchors. An unreadable or missing ledger/anchor forbids a new run or recovery pending audit.
5. Freeze recovery before launch: verify completed task hashes and unique IDs; never repeat completed tasks; never skip failed tasks; allow at most the approved, reason-coded task-level retry schedule without changing seeds; account for all attempts. Any incomplete case or ledger gap is not success, and a failure to finish within budget requires new independent adjudication rather than silent extension.

The principal residual risk is an unobserved transient memory peak causing macOS compression, swap growth, app disruption, or an OS kill before the watchdog polls. The researcher and independent approver must explicitly accept this host risk; the acceptance cannot be represented as proof of an enforced RAM ceiling. G0 and T1 require separate scientific, memory, and cost review because their graph and optimization workloads differ materially from NC-0a.

## R10 implementation snapshot — evidence only, no authorization

The previous `UNKNOWN_PROCESS_GROUP_MEMBER` false stop was reproduced as two Darwin process-table races: a live child could be rendered as `(Python)` or `(git)`, and the `multiprocessing.resource_tracker` could outlive the runner long enough to be adopted by PID 1. A fixed process-count tolerance was not added. The current watchdog uses a per-invocation, random-token-bound live PID-role registry; collapsed titles remain unresolved for at most two seconds while ordinary RSS/CPU/host monitoring continues, then fail closed unless the exact PID is registered with matching parent and process group. The runner now stops and waits for Python 3.11's resource tracker only after the pool has shut down. Repeated signed toy launches passed at 2, 4, and 8 workers (three repetitions each); the injected over-cap worker was terminated, and an orphaned tracker is not counted as success.

On 2026-10-17, the maximum-size factor-MST fixture (`N=3900`, `E=31,200`, engineering seed root `8062026`) ran four chains to 8E under the macOS watchdog. Across 998,400 proposals, observed probe wall time was 130.60 s, watchdog wall time 132.01 s, accounted process-group CPU 473.75 s, aggregate proposals per wall second 7,644.7, weighted acceptance 97.875%, peak sampled process-group RSS 644,988,928 bytes, and output JSON bytes 10,165 (four reports, each SHA-256 checked). The sampled host memory-free minimum was 33%; sampled swap grew by 87,954,555 bytes and remained under the nonformal 256 MiB growth cap; AC, sleep assertion and thermal checks stayed normal. No unknown process was observed. This 4-worker run preceded addition of the free-swap reserve check and therefore is performance evidence, not a test of the final swap-space stop rule. After that change, a 1-worker 1E replay completed under the current backend with 1 GiB test launch minimum and 512 MiB stop reserve; sampled free swap stayed at 1,204,352,450 bytes and used swap did not grow. Its stable-result SHA-256 exactly matched the earlier 1E run (`d5ea18b3e01351cb955164743b41c3511fff24bd3633eae9c216d63e6cc42f4e`). Fault injection of free swap falling below the reserve stopped and killed the process group as `SWAP_FREE_RESERVE_BREACH`. The 1-worker 1E run completed in 12.07 s probe / 12.57 s watchdog wall, accounted 12.90 CPU seconds, and sampled 456,474,624 bytes peak group RSS. The 8E results retain `MIXING-UNRESOLVED` and are engineering performance observations only.

The full preregistered chain workload is 44,937,216 proposals. A linear point projection from the 4-worker 8E run is about 98 minutes wall and 5.9 CPU-hours for proposal work. This is not a completion bound: only one largest fixture family and one chain length were measured, host load and longer-run throttling remain uncertain, and full-battery scheduling/recovery adds overhead. The earlier 9–18 hour estimate was not validated as a bound. The 72-hour/288-CPU-hour Mac envelope above remains a candidate only; it is not automatically approved or proven necessary/sufficient.

The run used a temporary 30 GiB boot-volume launch floor and 20 GiB live reserve only for bounded testing. At the time, internal free space was about 32.2 GiB, below the proposed 40 GiB formal launch minimum, and free swap was below 1 GiB, below the new 2 GiB candidate minimum. Both conditions block formal preflight. The full test result and exact hashes are in the R10 PR Conversation comment; the local raw probe artifacts remain outside GitHub.
