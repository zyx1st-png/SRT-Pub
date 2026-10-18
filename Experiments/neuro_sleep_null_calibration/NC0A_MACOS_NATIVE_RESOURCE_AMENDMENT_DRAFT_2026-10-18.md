---
id: SRT-NEURO-NC0A-MACOS-RESOURCE-AMENDMENT-DRAFT-20261018
type: proposal
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
title: NC-0a macOS native resource amendment and approval packet
date: 2026-10-18
scope: prospective engineering proposal only; no execution authority
dependency:
  - Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
tags: [Neuroscience, SyntheticNull, ResourceGate, Draft]
---

# NC-0a macOS native resource amendment and approval packet

**Draft only; not effective and not an execution authorization.** The R10 V2 policy and its 2 GiB launch / 1 GiB stop free-swap checks remain unchanged. This document proposes a separately signed V3 macOS resource policy. No V3 policy is valid until this amendment and an absolute budget receive independent approval, the production reviewer trust anchor and off-machine authority/audit store are provisioned, and a detached signature binds the exact clean repository HEAD, policy, runtime and watchdog. Test keys and this packet cannot authorize formal work.

This proposal changes only resource-control semantics. It does not change the scientific protocol: 16 fixed graph cases, eight independent chains per case, 32E swap attempts per chain, E/2E/4E/8E/32E checkpoints, 16 independent 1,000-proposal BFS oracle streams, 48 comparisons, fixed formal seeds and thresholds, and `MIXING-UNRESOLVED`. It does not authorize biological G0/T1 or relax data-identity requirements.

## Why the free-swap threshold is replaced only prospectively

`vm.swapusage` reports `total`, `used`, and `free` for the currently configured swap pool. XNU's `VM_SWAPUSAGE` implementation derives `used` as total minus available; its swapfile creation thread may create additional files when configured conditions call for them. Therefore `free` is current-pool availability, not a guaranteed limit on future paging capacity or a direct measure of free APFS space. The XNU sources show the usage fields and arithmetic in the [Darwin XNU sysctl implementation](https://github.com/apple/darwin-xnu/blob/main/bsd/kern/kern_sysctl.c) and conditional swapfile creation in [XNU's compressor backing store](https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/vm/vm_compressor_backing_store.c).

The existing 2 GiB startup and 1 GiB stop thresholds lack evidence that those cut points predict remaining future paging capacity. They can reject a machine with substantial APFS headroom and normal pressure, or falsely reassure when the backing volume is nearly full. V3 would retain these fields as telemetry only and instead combine (a) system-wide memory-pressure readings, (b) sampled process-group RSS, (c) sampled change in `swap_used`, (d) free space on both the internal Data and VM mounts, and (e) process, CPU, wall, output-disk, power, sleep and thermal controls. The old V2 checks stay active until a separate reviewer approves this amendment and signs a V3 policy.

These controls remain sampled abort triggers. macOS does not provide the V3 runner a cgroup-style hard aggregate RAM limit. A transient allocation between samples can be missed; system OOM handling may kill other applications or the runner; process RSS may undercount shared memory. Neither `ru_maxrss` nor sampled RSS is the exact process-tree peak. This residual risk must be acknowledged in the signed policy.

## Proposed V3 operating envelope — all values require independent approval

| Resource | Prospective V3 value | Scope and limitation |
| --- | --- | --- |
| Actual compute workers | Maximum 4 | Role-registered computation workers; helpers and resource trackers are sampled but are not counted as science workers. Unknown members stop the run. |
| Wall time | 72 hours cumulative | Candidate only; inclusive of sleep and all failed/recovered invocations under one experiment ID. |
| Aggregate CPU | 288 CPU-hours cumulative | Candidate only; process-group CPU plus waited-child and watchdog accounting. CPU-hours are not wall-hours. |
| Task loss bounds | 12 hours per case; 30 minutes per BFS oracle stream | Stop before the bound; failed tasks remain recorded and are not silently skipped. |
| Process-group RSS | 4 GiB sampled ceiling, early stop at 90% of that ceiling | 0.5 s sampling candidate. This is not a hard limit and may miss short-lived peaks. |
| Host pressure | Stop below 20% system-wide free percentage | Based on `memory_pressure -Q`; unavailable/unparseable telemetry fails closed. |
| Swap | Record total/used/free; stop if sampled `swap_used` growth exceeds 2 GiB from invocation baseline | `free` is telemetry only. `swap_used` is system-wide and not attributable solely to this experiment; other processes can move it. |
| Internal storage | Require at least 40 GiB available on both `/System/Volumes/Data` and `/System/Volumes/VM` at launch; maintain at least 30 GiB on each | These are two mount readings over a shared APFS container on the reviewed host, not additive capacity. Stop before a 64 MiB / 5% safety margin above reserve. The measured Data and VM values must be refreshed at launch. |
| Result / temporary output | 4 GiB per-run allocation cap; independently check the output filesystem and its signed free-space reserve | If output is external, internal boot/VM reserves still apply because swap is on the internal VM volume. Failed `fsync` is a failed invocation. |
| Power and thermal | Require AC, normal `pmset -g therm`, and watchdog-owned `caffeinate` sleep assertion | Does not protect against forced power loss, OS crash, thermal throttling without warning, or external sleep / shutdown. |
| Completion / recovery | Fail closed on any missing case, hash mismatch, budget stop, abnormal exit or unanchored log; task-level restart only under the signed fixed-seed recovery rule | Every attempt counts against both absolute budgets. No outcome-driven retries. |

The internal VM mount is monitored because that is the system's swap backing volume. Data and VM free-space values can match because APFS volumes share container capacity; the two paths provide a direct check of both result and swap-storage mount visibility, not two independent disk pools. The monitoring cannot reserve APFS capacity against unrelated host writes. Maintain AC power and avoid running other memory-intensive workloads during any approved run.

## Bounded performance evidence and resource estimate

R10 measured 998,400 proposals on the N=3,900 factor-MST fixture with four workers in 130.600 s wall and 473.747 s aggregate CPU, with 644,988,928 bytes maximum sampled process-group RSS and approximately 97.875% proposal acceptance. Those measurements covered 8E only and are not a completion bound. The linear proposal-only estimate for the 44,937,216 long-chain proposals is approximately 98 minutes wall and 5.9 aggregate CPU-hours at that measured rate; it excludes workload variability, full report verification, host contention and recovery.

R11's prospectively fixed, nonformal long probe was limited to one N=3,900 factor-MST fixture, four chains of 32E each, engineering seed root `20261018`, and watchdog cutoffs of 20 minutes wall, **1 aggregate CPU-hour**, 2 GiB sampled RSS, 64 MiB run output, 1 GiB sampled swap-growth, and 20 GiB internal Data/VM reserve. It cannot run the formal 16-case battery. The first attempt failed with an adapter `KeyError` after 127.598 s wall / 474.771 CPU-s; its watchdog correctly recorded `runner_exited` with return code 1. That failure is retained as resource cost, not counted as a completed probe. After fixing the adapter to include the scheduled 32E endpoint, a new, empty run directory completed successfully: four independent chains each made 998,400 proposals (3,993,600 total), each at about 97.8% acceptance. The watchdog recorded 459.234 s wall / 1,813.454 aggregate CPU-s, 633,405,440 bytes peak sampled process-group RSS, 34% minimum host-wide free-memory percentage, no sampled increase in swap-used, 782,327 bytes of run-directory output, and six peak process-group members (four computation workers, one runner, one resource tracker). AC power, normal thermal/performance status, and the sleep assertion remained present. The four endpoint graph hashes were `9b0489dfae159e740c3462a702d4c7eb25718e9f8ade9bfded233785a9b06a70`, `2e52a784859b7b240cd070204ef64a8040cbde2847f37bbd12374cdebe40d406`, `13bd80920e4953ce03d22aede66c76248c28a656c050d9736d61643d76b79cd3`, and `e09df7cb9ce5e5a136924460db8446cce3f5880b6cae1ebe0c96c805c73b25b4`. The report SHA-256 values were `874ebaacbc8d26d7b7721e8864c24fc395b8a4e30dba7490f0077c9a7f12c2b2`, `722c0bc6ddc165ed65d1650f3b793becf6facdb70e1fb6016138528463225535`, `8b5d5e84bb055fae8970b54d80ae53ac081c9b08aecfdb882e14ec33a726da2f`, and `0f16228210d68200a7e9e0b1ffa53e168933ac61cb4a926312704e07f4ccc2fd`; the successful stdout SHA-256 was `05b394b48dce946dc33b0010e973f2a4fc90f2cc24324838cfa97ef1e284d833`, and watchdog-audit file SHA-256 was `835e773f36f462cfc7d1395b1e5b99f1520da7d0327cc7ea3c708c704ecb69d0`. The prior failed attempt's watchdog file SHA-256 was `148aa92e1868da6a2cc5575c1e5a5ca97453f8b84e2ff2e6a9d7c50e33f033d9`. These local synthetic-only outputs remain outside the repository; hashes are recorded here so the evidence can be checked without uploading raw run directories.

The successful run verifies exact-seed endpoint and report hashes, but no second full 32E replay was run; bit-for-bit replay equivalence across a repeated execution therefore remains unverified. It is a single topology/family measurement with no BFS stream and no 16-case orchestration, not a general performance or completion bound. A failed attempt remains in the resource account; a repaired harness is not evidence of a successful benchmark.

The 72-hour / 288-CPU-hour candidate allows roughly 44 times the R10 proposal-only full-workload projection, but that ratio is not a calibrated bound. It is a prospective loss ceiling, not a promised completion guarantee. The independent budget approver must decide whether to keep it or raise/lower it after reviewing the R11 32E probe and workload-specific uncertainty. Any change must be prospectively encoded and signed before formal launch. Do not use the unverified historical `T_PS-A` as a baseline. NC-0a cost does not establish G0 or T1 feasibility.

## Exact approval payload checklist

Before formal execution, an independent approver and separate resource-budget approver must complete and sign a new V3 authorization covering:

1. The full clean repository HEAD SHA at signing, plus exact preregistration hash, V3 resource amendment hash, runtime lock hash, watchdog contract/source hashes, execution-engine and audit-ledger hashes, and complete dependency versions.
2. Mac host identity hash, model, architecture, OS build, Python version, measured physical memory, refreshed Data/VM free space, baseline pressure/swap state and output-volume identity.
3. The unchanged protocol and seed manifest; maximum four workers; final absolute wall, aggregate CPU, per-case, oracle, RSS-sample, host-pressure, swap-growth, Data/VM reserve and output caps.
4. A newly minted canonical formal experiment UUID, unique private run path, fixed task-level recovery rule, and maximum invocation count. Reuse of another run ID or directory is prohibited.
5. A genuinely independent reviewer identity, review record URL and administrator-installed public-key fingerprint. The private key must not be held by the person operating the run or be available to the local launcher.
6. An independently initialized, append-only authority ledger and separately protected tip anchor retained off this Mac and outside the run/repository. It must anchor every start, terminal watchdog event, failed attempt, recovery and cumulative wall/CPU charge. A missing or unverifiable anchor means stop and manual reconciliation; never reset the budget.
7. Explicit acknowledgment that sampled macOS memory controls are not a hard cap and can miss transient peaks, and that an incomplete/aborted battery has no scientific pass status.

The production key fingerprint is currently not provisioned; no independent resource or amendment approval has been recorded; the actual experiment UUID and protected external ledger/anchor are not yet issued. The test key generated in regression tests is temporary and has no production trust role. This packet records no approval decision or reviewer signature.

## Pre-launch host conditions and decision gate

The latest read-only snapshot after the bounded tests found 34,485,176 KiB available on both `/System/Volumes/Data` and `/System/Volumes/VM` (about 32.89 GiB), below the V3 candidate 40 GiB launch floor by about 7.11 GiB; it is about 2.89 GiB above the proposed 30 GiB reserve. It found current swap total 11,264 MiB, used 9,968.06 MiB and free 1,295.94 MiB; system-wide memory free was 39%, and AC and thermal readings were normal. The prior V2 2 GiB free-swap launch check would fail by about 752.06 MiB, although the current-pool free reading is about 271.94 MiB above its 1 GiB stop threshold. Under V3 the free field would be telemetry, but this host still fails the candidate disk launch condition by about 7.11 GiB. Refresh all measurements immediately before any future authorization; do not delete files or change settings automatically.

Formal execution remains blocked until all of the following exist together: approved and hashed V3 amendment; independently signed absolute budget; independent reviewer key and approval payload bound to the final clean HEAD; matching frozen Python/dependency environment; off-machine protected ledger and audit anchor; and at least the approved internal Data/VM and output free-space conditions. Engineering acceptance or a successful probe cannot substitute for any of these gates.
