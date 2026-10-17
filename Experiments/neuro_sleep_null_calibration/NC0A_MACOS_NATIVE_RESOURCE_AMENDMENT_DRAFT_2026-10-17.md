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

**This draft has no execution authority.** The currently signed formal launcher requires `CGROUP_V2_HARD`; it must continue to reject macOS formal runs until a dated prospective amendment, independent safety review, approved absolute budget, production trust anchor, and revised signed policy are in place. A test key or a local self-signature is not an approval.

## Scope and rationale

The NC-0a preregistration requires a prospectively locked absolute resource budget, including peak RAM and failed-case behavior. It does not prescribe Linux or cgroup v2. The cgroup requirement was added later to address R7's measured short-lived RSS spike that escaped polling. A macOS backend could preserve the scientific protocol while accepting a weaker *machine-protection* guarantee, but only if that difference is explicit and independently approved. A sampled RSS maximum must never be reported as a hard memory limit or a true process-tree peak.

The scientific contract remains unchanged: 16 fixed synthetic cases, eight chains per case, 32E proposals per chain, E/2E/4E/8E/32E checkpoints, 16 independent 1,000-proposal BFS-oracle streams, 48 paired comparisons and existing thresholds, fixed formal seeds, and the `MIXING-UNRESOLVED` interpretation. No result-dependent retry or null-result-dependent T1 decision is allowed. This proposal does not authorize G0 or T1 and does not replace biological data identity requirements.

## Bounded evidence behind the proposal

On 2026-10-17, an Apple M1 Pro with 16 GiB RAM, macOS 15.7.4, Python 3.11.15 and about 26 GiB free boot-volume disk ran the separate-seed `nc0a_macos_feasibility_probe.py` (root 8062026). Every counted run was nonformal and wrapped by the existing watchdog with a 0.5 s polling interval and strict small caps. The largest fixture used N=3900 and about 31,200 edges. Short parallel probes allowed at most 5,000 proposals per worker; longer single-chain probes stopped at 1E or 4E, not 32E.

| Family | 2-worker proposals/s; sampled group RSS | 4-worker proposals/s; sampled group RSS | 8-worker proposals/s; sampled group RSS | One-chain 1E -> 4E proposals/s |
| --- | ---: | ---: | ---: | ---: |
| BA-like | 3,845; 127 MiB | 7,401; 203 MiB | 9,863; 363 MiB | 2,266 -> 2,194 |
| Factor-MST | 5,715; 467 MiB | 10,498; 482 MiB | 11,112; 576 MiB | 2,795 -> 2,413 |

These are timing observations, not 32E or full-battery time bounds. Four workers retain much of the measured throughput while reducing sampled RSS, CPU contention and pressure versus eight. The 1E and 4E probes saved and SHA-256-checked full chain JSON reports (about 1.1–2.2 KiB each); measured save/fsync took about 2–7 ms per report, but full formal audit cost was not measured. The watchdog recorded a separate factor-MST four-worker invocation as `UNKNOWN_PROCESS_GROUP_MEMBER` during a Python spawn exit race; its computation completed but it is **not counted as a successful protected run**. It is a required engineering fix, not evidence of false scientific acceptance.

Local raw summary SHA-256 anchors were `d0627cf334eacada41a88e07cf18b9fa93cbcbc0d096b5c5f7720746f34625b6`, `903795a4e7e49d2ae64d9c1bb670ae72a29d0a274773757473723dbd9e19fe8d`, and `ab2752e486007931a38daf0bcbd5ee7868f22a799ffaed471cfed62aea0d0d8b`. They reside in temporary local directories and are not durable remote artifacts; the committed bounded probe provides a repeatable method. The R7 transient 136,282,112-byte child RSS event against an 83,886,080-byte cap was missed by polling at 11,976,704 bytes, so these sampled values cannot resolve the short-peak risk.

## Candidate operating envelope for independent review

| Control | Proposed prospective value | Enforcement and limitation |
| --- | --- | --- |
| Compute workers | 4 actual computation workers maximum | Count by verified role and process identity; monitor parent, workers, and helpers. An unknown group member fails closed. The observed Python-spawn exit-race false stop needs repair before authorization. |
| Cumulative wall / CPU | 72 hours elapsed wall; 288 aggregate CPU-hours | Count across every invocation, failed attempt, restart, and recovery under one experiment UUID. Wall accounting includes sleep; monotonic/UTC divergence or unreadable accounting fails closed. Values are candidates, not approved limits or a completion guarantee. |
| Per-case / oracle | 12 elapsed hours per case; 30 minutes per oracle stream | Prospective loss limits; stop and audit before any increase. Preserve failed records. |
| Memory | 4 GiB **sampled** process-group RSS ceiling, stop at or before 90%; host memory-pressure free percentage stop at 20%, plus native warning/critical event handling if implemented and verified | RSS sampling may miss short spikes, shared pages may be double-counted, and host pressure is not a process hard cap. These are abort triggers, not a guaranteed peak limit. Record sample interval and raw samples. An OS OOM kill, swap storm, severe pressure, or missing telemetry is a failed/unknown run requiring audit. |
| Disk | 4 GiB run-output cap; at least 40 GiB free on the internal boot volume before launch and 30 GiB maintained; monitor output and boot/swap volumes separately | Stop before reserve breach or failed fsync. External output storage does not remove boot-volume swap risk. Current examined host had only about 26 GiB free and would fail this proposed preflight. |
| Power / thermal | AC power, prevent idle sleep with an owned assertion, monitor sleep divergence and thermal warnings | No claim of avoiding power loss or forced sleep. Interrupted work is recovered only under the frozen task-level rule. |

The 72-hour and 288-CPU-hour figures are a **review candidate** based on bounded 1E–4E probes, with substantial allowance for 32E slowdown, case diversity, checkpoint work, host contention, and recovery. The probes do not establish a statistical upper bound. The historical `T_PS-A` remains unverified and cannot justify these numbers. Before approval, rerun representative longer nonformal probes, freeze the host load and exact dependency environment, verify storage capacity, and have an independent reviewer accept both the estimated cost and possible incomplete-run loss. A larger approved budget may be appropriate; it must be set before the formal run and signed anew.

## Required implementation and review before any formal macOS launch

1. Introduce a separately named `MACOS_SAMPLED_PRESSURE` policy only under a versioned, dated amendment. Keep `CGROUP_V2_HARD` semantics intact; never alias the two. Preflight and launcher must require a signed policy whose backend, thresholds, watchdog/protocol/preregistration/dependency hashes, HEAD, experiment UUID, and approved machine identity match. Reject legacy or unsigned policy on the new path.
2. Verify actual worker classification through spawn and exit races at two, four, and eight workers; retain fail-closed handling of unknown group members and record any benign false stop as a failed, costed invocation. Add native host pressure events if practical, but keep explicit that neither events nor polling bounds transient RSS.
3. Test stop-and-kill on sustained RSS, pressure, CPU, wall, disk, worker crash, parent/watchdog crash, sleep divergence, OOM/forced kill, and missing telemetry. Confirm no orphan workers and durable failed/unknown records. A short-lived unobserved memory spike must remain documented as residual risk; do not assert it has been solved by polling frequency.
4. Freeze the macOS version, Python and full dependency closure, CPU architecture, executable and source hashes, output schema, and exact result-verification procedure. Use an independently protected production public-key fingerprint, approval, authorization-use ledger, and off-machine log anchors. An unreadable or missing ledger/anchor forbids a new run or recovery pending audit.
5. Freeze recovery before launch: verify completed task hashes and unique IDs; never repeat completed tasks; never skip failed tasks; allow at most the approved, reason-coded task-level retry schedule without changing seeds; account for all attempts. Any incomplete case or ledger gap is not success, and a failure to finish within budget requires new independent adjudication rather than silent extension.

The principal residual risk is an unobserved transient memory peak causing macOS compression, swap growth, app disruption, or an OS kill before the watchdog polls. The researcher and independent approver must explicitly accept this host risk or choose a Linux cgroup-v2 environment. This risk acceptance cannot be represented as proof of an enforced RAM ceiling. G0 and T1 require separate scientific, memory, and cost review because their graph and optimization workloads differ materially from NC-0a.
