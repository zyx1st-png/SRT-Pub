---
id: SRT-OBSERVED-CALIBRATION-TELEMETRY-INCIDENT-20261026
type: engineering-audit
status: draft
date: 2026-10-26
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_RESOURCE_REQUEST_2026-10-26.md
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_FIRST_ATTEMPT_INCIDENT_EVIDENCE_2026-10-26.json
tags: [RIKEN, ObservedBaseline, Watchdog, Incident, NoRetry]
---

# First observed-only attempt: worker telemetry conflict

**Verified operational interruption; researcher-approved remediation policy for engineering only (2026-10-26); no remediation execution authorized or enabled.**
This corrective branch is stacked on #1132's executed HEAD
`b4a4b34ed7432efbf0d289a8b244345f73cf6a43`.
The original UUID `cf726336-0f3b-4506-9cd3-cb36da3f7e12` remains consumed,
`completed=false`, `resume_allowed=false`. Its original files, authorization,
control/evidence/Watchdog chains, and host ledger are unchanged. This report
supersedes the *provisional cause assessment* in the
[incident comment](https://github.com/zyx1st-png/SRT-Pub/pull/1132#issuecomment-6411647409),
without changing that historical comment or the approved one-attempt rule.

## Read-only evidence and cause

The official `observed_calibration_runner.py --verify <original-run-directory>`
returns `VERIFIED_TERMINAL`, six rows verified, `completed=false`, and no resume.
The public JSON dependency contains actual re-read file hashes, chain tips,
host start/finish records, process diagnostics, and per-row costs; it contains
no private paths, signal arrays, Q vectors, partitions, or neuron subsets.

| Original artifact | SHA-256 / chain tip |
|---|---|
| Terminal summary file | `4eae491304bd80294854c79227067144f2d6bb42ecdec42ae085adb1d81cc0b1` |
| Run manifest file | `92f52e49d82c81c208693f96ab4e2a0791dbdbc7dde04f710f6e28a8c1907a97` |
| Control chain tip | `c2dfcdac2046f26ef7531903fb1c420473bd48bab694caa0806e5d68988ff845` |
| Watchdog chain tip | `11c0e7b90dcc5b58bac6a4a7c436506f51fdf7bf0386535dddccdb23b81730f4` |
| Scientific evidence chain tip | `212f93b225146aabfb6a7eebb458856f5c90075c7f8993441d1a8cc7a28fe3da` |

At `2026-10-26T08:18:46.099420+00:00`, `watchdog_stop_requested` records
`UNKNOWN_PROCESS_GROUP_MEMBER`: PID 85411, PPID 84340, PGID 84340, state `U`,
captured executable title `(pmset)`. PID 84340 is the scientific runner/group
leader. Its command hash is
`3bc59fe9f1cb1631b2b38d66a47283601beea8f9a120e7813965f24b09083482`,
which is the SHA-256 of the captured title `(pmset)`, **not full argv**.
The exact helper launch time and batt-versus-therm invocation were not recorded.
The detection timestamp must not be relabeled as the process's birth time.

The reported task is row 6, `mouse01_sleep|N765|rep-085|NREM|window-002`.
Its durable result follows at `08:18:46.110438Z`; row 7 starts at
`08:18:46.110964Z`. Row 7 records identity, pre-snapshot, raw-cache read and
correlation phases before termination, with no committed Q result. Thus the
Watchdog task label and the last durable scientific stage are different
snapshots; they must not be presented as simultaneous exact stage telemetry.

Source inspection confirms the mechanism: the old `_private_process_row()`
calls host sampling before and after each row. Those functions synchronously
spawn `memory_pressure -Q`, `sysctl vm.swapusage`, and `pmset -g batt/therm`.
The children inherit the scientific process group. `classify_process_group()`
correctly rejects these unregistered children. The PPID/PGID/title, row-boundary
timing and this unique worker-side pmset call path support the telemetry conflict
as the cause; no full-argv or process-lifetime trace is claimed. The external
Watchdog's own helpers run outside the supervised group and remain appropriate.

## Minimal repair and validation

The production row function now obtains only in-process native resource
counters and filesystem free-space endpoints. Host pressure, Swap, AC, thermal,
Data/VM and process-tree RSS continue to come from the **unchanged external
Watchdog**. Each new row points to `watchdog.jsonl` and its graph/task identity.
Those are periodic samples, possibly delayed across row boundaries, not exact
row endpoints. No matching sample means unknown. Legacy rows retain their
original endpoint fields and remain verifiable; implementation hashes
distinguish the two metrology versions.

No process whitelist, worker count, sampled-memory semantics, stopping limit,
scientific algorithm, seed, sample, authorization validator or consumed-attempt
gate changes. No real calibration was run to validate this repair.

Target macOS arm64 / Python 3.14.0 validation uses only synthetic HDF5 signals
and engineering seeds. Tests exercise the actual private-row function with
synthetic input admission and builder; `subprocess.Popen` is forbidden inside
that function. Graph edges, original labels, seeds, all 200 canonical Q values,
partition hashes and zero-variance diagnostics must equal the existing helper.
Real supervised synthetic tests cover the repaired row path, native macOS
external telemetry/sleep assertions, and an unknown child that must be stopped.
Captured `(pmset)`, full pmset commands, memory_pressure and vm.swapusage remain
unknown when put inside the worker group. Existing negative authorization,
budget, corruption, no-overwrite and consumed-attempt tests still apply.

Validation results on the target Mac:

- The new subprocess-prohibition regression fails as expected when the executed
  HEAD's original row function is loaded in an isolated synthetic test process.
  The failure is the worker's host-telemetry subprocess call; no repository or
  historical file is replaced for this negative control.
- Final affected suites: **94 passed, 53 subtests passed in 36.36 s**, including
  observed calibration, Q protocol, Watchdog, H3 pilot and H3-120. The optional
  hash-pinned historical *code* test uses synthetic signals only. Ruff and
  compilation pass. GitHub CI status belongs to the corrective PR's commit.
- A separate AI subagent found no new static scientific/safety blocker. Its
  first four-test check had one Mac-native synthetic supervision stop with no
  retained stop reason (the old assertion omitted the summary and teardown
  removed temporary files); the other three checks passed. This anomaly is
  **unresolved and is not attributed to any guessed cause**. One diagnostic
  run and a pre-fixed batch of three further Mac-native runs completed; the
  latter took 1.1953/1.1909/1.1958 s wall, 1.3829/1.3862/1.3896 s CPU, with
  92.7–93.6 MB sampled peak RSS and no unknown PIDs. These later passes do not
  erase the first stop. Assertions now print the full summary on failure.

The unexplained synthetic stop must be included in remediation review. These
results establish readiness **for that review**, not execution authorization or
a guarantee against other host/process races. No real RIKEN Q was recalculated
by the subagent or by this repair's tests.

## What the six rows establish

The verified prefix contains 1,200 completed canonical Q trials, all from one
recording, three windows, and five N levels. Three raw-window loads and three
cache hits each retain 94,116,000 bytes. Costs below are observations from this
interrupted, instrumented attempt, not forecasts.

| Order / N | Durable row wall (s) | 200-Q wall / self CPU (s) | Reconstruction outer wall (s) | Raw cache |
|---|---:|---:|---:|---|
| 1 / 100 | 2.960 | 1.745 / 1.697 | 0.623 | miss |
| 2 / 1150 | 27.885 | 26.573 / 25.272 | 1.186 | hit |
| 3 / 340 | 8.025 | 7.191 / 6.950 | 0.724 | miss |
| 4 / 3900 | 116.829 | 87.179 / 83.499 | 29.399 | hit |
| 5 / 100 | 2.283 | 1.689 / 1.618 | 0.499 | miss |
| 6 / 765 | 17.453 | 16.800 / 15.897 | 0.517 | hit |

Reconstruction sums identity, raw-window, correlation, inclusive builder and
independent identity/canonical-representation phases; MST and edge-selection
residual are nested and are not added again. Q totals are 141.178 s wall /
134.933 s self CPU; outer reconstruction wall totals 32.948 s. N=3900 includes
25.654 s of independent graph-identity/canonical representation. This is a
useful measured cost component, not evidence of an algorithmic defect.

The full interrupted Watchdog interval is 183.268 s wall / 188.485 s accounted
CPU, including admission and incomplete row 7; formal preflight separately
records 7.246 s wall / 6.289 s self CPU. Peak sampled tree RSS is 1,465,270,272
bytes; minimum host memory telemetry 33%; sampled Swap growth 45,801,800 bytes;
minimum Data/VM free space 49,150,107,648 bytes; terminal output 963,530 bytes.
Row 1 and row 5 have no Watchdog RSS sample, so their tree peaks are unknown.
Lifetime process `ru_maxrss` is distinct from sampled tree/row peaks.

These costs preserve actual graph/Q identity, cache behavior and phase evidence.
They do not measure the other 41 graphs, five other recordings, a cold SSD,
all N strata, complete 47-row runtime, U95, a 4,900-graph baseline or G0/T1.
The repaired path removes old host-command endpoint overhead: preserve that
version difference when using the prefix as historical cost evidence.

## Separate prospective remediation policy — RESEARCHER-APPROVED FOR ENGINEERING ONLY / NOT RUN ENABLED

Current code still rejects this sample after its recorded attempt, even with a
different UUID. The old authorization cannot match a new HEAD. This PR creates
no exception, new real UUID, authorization, precommit or run directory.

The researcher **approved the one-time 41-row suffix remediation principle and aggregate resource boundary for engineering preparation**, recorded in [#1133 decision](https://github.com/zyx1st-png/SRT-Pub/pull/1133#issuecomment-6412266654) after [limited repair review](https://github.com/zyx1st-png/SRT-Pub/pull/1133#issuecomment-6412223225). This is an explicit scope-limited **policy approval to build and test a prospective exception**, **not a real run authorization, not approval of unimplemented exception code and not a bypass of the consumed-run ledger gate**. The review was source/evidence-based, not human peer review or independent Mac-machine replication. Any future exception is restricted to at most **one** new separately authorized activity on exactly the originally frozen 41-row suffix.
The six completed rows remain immutable scientific/old-instrumentation cost
evidence and are not recomputed or represented as newly measured repaired rows.
The combined inventory would still be the same 47 graphs, reported as two
activities with different instrumentation and cache starts; it would not be
called one uninterrupted or homogeneous resource measurement.

A future minimal gated implementation would require a new HEAD-bound
researcher decision that names the consumed UUID, exact old summary hash,
manifest hash, audit tips, six prefix artifact hashes, unchanged full sample,
and exact 41-row suffix hash. It must re-run the old audit verifier, establish
this specific operational cause (not a scientific failure), reject missing or
ambiguous evidence, and confirm there is no earlier remediation claim. A new
append-only host-ledger claim would reference the old run and consume the sole
exception before any signal processing. A fresh UUID alone grants nothing;
old ledger entries must never be removed, reset, or relabeled.

The researcher **approved retaining 4h wall / 4 CPUh as the aggregate finite-loss envelope** across the original attempt and any single authorized remedy, not a fresh four-hour allocation. The recorded old supervised interval used 183.26759672164917 s wall / 188.48465399999998 s CPU, and old formal preflight used 7.245956416998524 s wall / 6.2890250000000005 s CPU. Assuming these are non-overlapping charges, the upper remaining amount **before all new preparation is 14,209.486446861352 s wall / 14,205.226321 s CPU**; verify charge semantics and any overlaps, then subtract new source/ledger verification, live preflight, runtime and monitoring costs before freezing the new budget. Unused capacity is not authorization. Keep 1 worker, 4 GiB **sampled** RSS (not hard RAM containment), **1 GiB combined output across both attempts**, one ≤256 MiB retained cache, 32 MiB per-result cap and every existing Mac safety threshold. Cache reload, new identity preflight, failed work, logging and stopping consume the approved remaining envelope. Any new stop exhausts the exception. No reserve
40, sample replacement, further retry, full baseline or null computation follows.

The researcher has accepted the **prospective one-exception policy** and the requirement to report combined coverage as **six old-instrumentation plus 41 new-instrumentation rows, not a single homogeneous 47-row run**. The exceptional launcher, atomic append-only one-use claim, fixed exact suffix hash, original hash verification, and aggregate charging must now be implemented and synthetic-tested; no real exceptional attempt is enabled. The one unresolved native-Mac synthetic supervision stop must remain disclosed, and future predeclared tests must retain full terminal/Watchdog evidence on failure. Independent incremental review of that **new code** and a subsequent final-HEAD, fresh-UUID, privately confirmed researcher **run-specific authorization** remain required. The active original resource request and its consumed-attempt host ledger are not rewritten or unlocked by this policy record. No reserve 40, additional retry, full observed baseline, G0 or T1; **G0/T1 stay RESOURCE NO-GO**.
