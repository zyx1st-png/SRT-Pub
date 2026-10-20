---
id: SRT-NEURO-NC0A-CLOSURE-PSA-RUNTIME-RECONSTRUCTION-20261019
type: audit
status: draft
updated: 2026-10-21
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
  - Experiments/neuro_sleep_null_calibration/NC0A_RESEARCHER_AUTHORIZED_EXECUTION_AMENDMENT_V1_2026-10-18.md
  - Experiments/neuro_sleep_null_calibration/H2_RUNTIME_AUDIT_2026-10-12.md
  - Experiments/neuro_sleep_null_calibration/PSA_RUNTIME_EVIDENCE_HANDOFF.md
tags: [Neuroscience, NC0a, PS-A, Runtime, Results, Evidence]
---

# NC-0a formal closure and PS-A runtime reconstruction

**Review/update date:** 2026-10-21. **Execution identity:** PR #1114, HEAD `c1efb8738ec46d25a55ae8cafc6aad829977a53b`, experiment UUID `eb5f7ba1-aad0-48a1-9cdb-786b90c866e5`. The formal artifacts were checked against that locked HEAD; the bounded final PS-A source search was performed on 2026-10-20. This report is a noncanonical local audit record. Its update changes only the disposition wording and records durable copies of private metadata derivatives; it does not change the preregistration, source results, runtime records, execution HEAD, PR state, or any authorization.

**Disposition:** the **NC-0a synthetic battery PASS**: its anomaly screen, BFS oracle, graph invariants and recorded-result checks passed. The **full Gate NC-0a is not passed / remains NO-GO**, because the primary G0 resource criterion is still unmet. `MIXING-UNRESOLVED` remains mandatory. The historical full PS-A active-time denominator `T_PS-A` is still **not established**; the existing G0/T1 resource gate remains **RESOURCE NO-GO** until the historical evidence is completed or a separate prospective budget amendment is independently reviewed and adopted. A passing synthetic battery is not a G0 resource decision.

## 1. NC-0a result closure

The local run is at `~/.local/share/srt-pub/nc0a-pr1114-runs/eb5f7ba1-aad0-48a1-9cdb-786b90c866e5/`. Its public execution report is [PR comment #6270568230](https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-6270568230). The run manifest binds the preregistration hash, runtime lock, nine source files, seed manifest, watchdog contract, and locked HEAD. The researcher commitment SHA-256 is `f688039da0a208c18398fc47415184f9d37849162926bd3cca602e246791c352`.

I re-ran the saved-artifact checks with the locked Python 3.11.15 / NumPy 2.3.5 / SciPy 1.17.1 environment. The execution engine's completed-battery verifier passed; its per-case statistical screens and full-battery validator reproduced the stored summary. The authorization, execution and Watchdog hash-chain tips match the local audit summary, and the regenerated audit summary matches it. The public base64 summary decodes to the same JSON object as the local summary; all 16 public case-result hashes match the local result files. The GitHub audit-anchor validator passed. There was one invocation, one Watchdog start and terminal event, no retries or recovery, and no recorded failure.

The workload and integrity checks were:

| Contract item | Verified result |
|---|---:|
| Fixed synthetic cases | 16/16: four families × N={100, 340, 1150, 3900} |
| Independently seeded chains | 128/128, eight per case |
| Checkpoints | E, 2E, 4E, 8E, 32E; 640 chain-checkpoint records |
| Long-chain proposals | 44,937,216 attempted proposals |
| Independent BFS-oracle streams | 16/16 × 1,000 proposals = 16,000; zero mismatches |
| Paired 4E-versus-32E screens | 48/48 reproduced and passed |
| Stored mixing label | `MIXING-UNRESOLVED` in the full summary, all case reports and all chains |

The 48 paired t statistics, shown as absolute values in triangle / assortativity / initial-edge-overlap order, are:

| N | Family | Triangles | Assortativity | Edge overlap |
|---:|---|---:|---:|---:|
| 100 | ba-like | 2.244 | 1.027 | 0.636 |
| 340 | ba-like | 0.181 | 0.998 | 0.575 |
| 1150 | ba-like | 1.871 | 2.317 | 0.345 |
| 3900 | ba-like | 0.287 | 0.118 | 0.803 |
| 100 | er-like | 0.170 | 0.530 | 1.775 |
| 340 | er-like | 0.739 | 1.084 | 0.777 |
| 1150 | er-like | 0.614 | 0.355 | 2.005 |
| 3900 | er-like | 0.458 | 0.305 | 1.394 |
| 100 | factor-mst | 0.665 | 1.021 | 0.119 |
| 340 | factor-mst | 0.427 | 1.794 | 0.496 |
| 1150 | factor-mst | 0.533 | 0.313 | 0.984 |
| 3900 | factor-mst | 1.012 | 0.349 | 0.194 |
| 100 | ws-like | 0.848 | 1.080 | 1.066 |
| 340 | ws-like | 1.085 | 0.337 | 0.433 |
| 1150 | ws-like | 0.177 | 0.892 | 1.191 |
| 3900 | ws-like | 0.486 | 0.028 | 3.261 |

The rule is the preregistered two-sided paired t screen with df=7 and Bonferroni familywise alpha 0.05/48; the verified critical value is 5.369862606270659. The largest absolute t was 3.2605348975 and the smallest Bonferroni-adjusted p was 0.6649993675. Thus this run detected no 4E-to-32E drift under that rule. With eight chains, the comparison has low power for many departures; a failure to detect drift is not an equivalence result. The previously demonstrated slow-mixing / near-frozen-chain counterexample still passes this style of screen. This result therefore does not show stationarity, uniform sampling from connected fixed-degree graphs, adequate mixing, or a biological SRT effect.

The original R4 four-case reviewer-seeded exposure, R10 8E probe, R11 nonformal 32E factor-MST probe, and the separate NameError startup failure remain disclosed historical exposure. They are not part of this formal result and were not used to retune seeds, thresholds, graph families or chain count. The formal screen is synthetic calibration only; it is not an independent biological replication or validation of SRT.

### Execution resources

The recorded run began at 2026-10-19 13:56:43.673 UTC and ended at 15:09:16.283 UTC. Accounted cumulative wall time was 4,352.529 s (72 min 32.5 s); accounted process-group CPU was 17,356.060 s (4 h 49 min 16.1 s). Four compute workers were the maximum. The environment was macOS 15.7.4 arm64, 16 GiB physical RAM, Python 3.11.15, NumPy 2.3.5, SciPy 1.17.1; the runtime lock SHA-256 was `38ce29363945c32d7af318e14ea878e91053a1b68c3c8b64cca4edbddb9d6954`, and the manifested preregistration SHA-256 was `bf497d89e5695498451e49071007aec290d8a899b30b0fd31026f8f3faa55aaa`.

Watchdog recorded 824 resource samples. Its terminal record reports a sampled aggregate process-group RSS peak of 514,179,072 bytes (~490 MiB), minimum host-free memory of 33%, minimum Data/VM volume free space of 49,928,867,840 bytes (~46.5 GiB), output-directory size 2,552,137 bytes, four compute workers, AC power, active caffeinate sleep assertion, and no thermal warning. `swap_used` began and peaked at 10,484,250,050 bytes, then ended at 10,224,077,373 bytes; sampled swap use did not grow from the starting value. The initial free swap sample was about 1.24 GiB. No configured V3 stop condition was recorded as crossed.

RSS, memory pressure and swap were sampled telemetry, not OS-enforced limits; peaks between samples may have been missed. CPU-hours and elapsed wall are distinct. The reported CPU value is accounted process-group use, not a guarantee of exact per-core utilization. A successful local hash chain and public GitHub copy are inspectable evidence, not immutable independent custody. The run stayed within the researcher's accepted V1 limits; that does not prove those limits are a completion-time bound.

### Result evidence and release plan

The principal local and public anchors are:

| Artifact | SHA-256 / reference |
|---|---|
| Run manifest | `07aa974c0fb911296d517be2f805069b83a74329a08495d5f082c679afc21ec7` |
| Formal battery summary | `affd8b32c907aac930a80ce640137afbc9c182d990adc4d8f2108f464c9902c5` |
| Public/local audit summary file | `ccebba87966d713b63f0c52cf7bf56d7d4618e3126fc789b74abbc20ed5cc248` |
| Authorization, execution, Watchdog log tips | `4ef9a7cfe3778993cd6391b90aed8a23ab368bedb41efa03e0aa37155c92258d`; `abc6cf3413717bc44391ca54c7a593d2b66790403c40eebee30142fc7caf76b6`; `8b94b81dddd92daa13e3f82f4a46dc531743dff1fe3626cf43d50c7fa9133452` |
| 16 case-result SHA-256 values | Embedded in the audit summary and publicly anchored in PR comment #6270568230 |

Hash serialization note: the public comment's declared audit-summary hash is the SHA-256 of the local canonical JSON plus its newline. Its base64 field contains the same canonical JSON object without the final newline, so the decoded base64 byte hash is `10d340ce8ae6e49539f3f3e1a5c0ff2a6ae0d8d09618ec17016c7b5597b4360e`; parsed JSON objects match exactly and the protocol validator accepts the anchor. This is a serialization distinction, not a different summary.

For a later raw-result release, make a separate staging copy without editing the run directory. Include the 16 exact `result.json` files and their sidecars, run manifest and checksum, formal summary and checksum, seed manifest, execution and Watchdog logs, runner stdout, the public precommit reference, and the audit-summary JSON/SHA. Generate a sorted `SHA256SUMS` and a hash for the final archive; independently verify every staged file against the original before release. Review the operational logs for local usernames, absolute paths and host identifiers. If any are redacted, label those files as derived redacted copies, retain the unmodified private originals, record the redaction method and publish distinct hashes; never describe a redacted log as byte-identical raw evidence. This is a release plan only: no raw run file was copied, edited, uploaded or overwritten in this review.

## 2. PS-A history and `T_PS-A`

The source directory `.local/phase2_population_size_scaling/` was found in the main local workspace. It is untracked local evidence and remains untouched. The PR worktree is a separate worktree at the execution HEAD. A read-only full inventory of the original metadata returned 6,006 JSON job files, 6,006 unique completed jobs, 49,049 unique completed state-window records, 9,809,800 stored Q values, zero unclassified execution-log lines, and exact equality between the job/window IDs in the log and saved job files. The completed-job CSV and per-job hash manifest were initially created under `/tmp`; on 2026-10-20, the derived metadata and arithmetic artifacts were copied byte-for-byte into access-restricted persistent local storage, described in §3. The originals and source data remain untouched. This establishes output coverage; it does not establish how much time was spent producing every output.

Eight launches appear in `commands.log`; an additional failed `nohup` attempt appears in the historical session record but not in that file. Worker count was four for the first two commands and eight from the third command onward. The durations below are tool-recorded process durations where available, not CPU time. Progress spans are log envelopes and must not be read as continuous active runtime without qualification.

| Run | Start from command history (+08) | Workers | Logged progress / unique jobs and windows | Tool duration and status |
|---|---|---:|---|---|
| 1 | Sep 24 18:16:10 | 4 | 18:16:16.734–18:16:19.908; 1 job / 4 windows | 10.416 s, exit 0 |
| 2 | Sep 24 18:17:40 | 4 | 18:17:51.717–18:19:46.812; 1 / 4 | 127.084 s, exit 0; includes `py_compile` wrapper |
| 3 | Sep 24 18:20:38 | 8 | 18:20:50.703–18:22:14.344; 1 / 4 | 96.012 s, exit 0 |
| Failed unlogged launch | Sep 24 18:22:35.955 | configured 8 | No attributable progress or new job | Process absent by 18:23:01; elapsed/CPU cost not established |
| 4 | Sep 24 18:23:58 | 8 | 18:24:05.303–Sep 25 12:36:58.861; 1,994 / 12,960 | End time and tool duration missing; no process found in probe begun 16:26:41 and returned 16:26:49 |
| 5 | Sep 25 16:28:04 | 8 | 16:28:17.706–Oct 7 20:37:13.332; 2,995 / 26,947 | 151,457.683 s, exit -1; span includes long inactivity/sleep |
| 6 | Oct 8 10:55:26 | 8 | 11:03:00.829–17:16:29.236; 806 / 7,259 | 22,916.396 s, exit -1 |
| 7 | Oct 8 22:41:20 | 8 | 22:41:28.920–Oct 9 14:02:16.097; 178 / 1,609 | 28,117.260 s, exit 1; span includes verified sleep |
| 8 | Oct 9 14:32:10 | 8 | 14:32:24.059–16:38:14.857; 30 / 262 | 7,565.058 s, exit 0 |

The eight logged job counts sum to 6,006. Historical process snapshots show one main runner plus eight worker processes during sampled later sessions; no overlap between PS-A main runs was found in the available records. This is not a complete process accounting history. The unlogged launch has no attributable output; its resource cost is unknown rather than zero. The end of run 4 is also unknown. Seven tool durations sum to 210,289.910 s (58.413864 h); the missing eighth duration prevents treating this as a complete process-time total. Tool elapsed duration is not CPU-hours.

### Reproducible partial elapsed-time arithmetic

Using the current `psa_runtime_evidence.py`, I rebuilt a private, source-hashed manifest from the nine progress intervals recorded in the 2026-10-12 H2 audit. It binds the actual `execution.log` SHA-256, exact line/timestamp anchors, the newly regenerated 6,006-ID coverage CSV hash, the +08:00 log offset, and the observed 4/8-worker settings. The checker returned `ARITHMETIC_CHECK_ONLY_INDEPENDENT_REVIEW_REQUIRED`:

| Progress-supported partial segment | Workers | Elapsed | Nominal worker-hours* |
|---|---:|---:|---:|
| Sep 24 18:16:16.734–18:16:19.908 | 4 | 0.000882 h | 0.003527 |
| Sep 24 18:17:51.717–18:19:46.812 | 4 | 0.031971 h | 0.127883 |
| Sep 24 18:20:50.703–18:22:14.344 | 8 | 0.023234 h | 0.185869 |
| Sep 24 18:24:05.303–Sep 25 12:36:58.861 | 8 | 18.214877 h | 145.719018 |
| Sep 25 16:28:17.706–Sep 27 05:38:47.454 | 8 | 37.174930 h | 297.399440 |
| Oct 8 11:03:00.829–17:16:29.236 | 8 | 6.224557 h | 49.796460 |
| Oct 8 22:41:28.920–Oct 9 01:28:33.902 | 8 | 2.784717 h | 22.277738 |
| Oct 9 09:01:46.034–14:02:16.097 | 8 | 5.008351 h | 40.066807 |
| Oct 9 14:32:24.059–16:38:14.857 | 8 | 2.097444 h | 16.779551 |
| **Union / sum (these intervals do not overlap)** |  | **71.560963 h** | **572.356292** |

\* Worker-hours are elapsed interval × configured worker count. They are not measured worker CPU time. The interval selection is progress-supported, not a complete partition of the run history, and does not assert that all cores were busy at every second. Thus **71.560963 h is neither a complete `T_PS-A` nor a strict CPU-active lower bound**.

A conditional mixed-source candidate is 76.630770 h: the seven tool durations plus 65,580.861 s from run 4's command start through its last progress event. Its corresponding nominal worker-time candidate is 612.893380 worker-hours. This estimate is **not accepted** because it substitutes last progress for the missing run-4 process end and assumes a consistent tool-duration clock. For run 5, the session `started_at_ms`–`completed_at_ms` span was 1,051,773.507 s while its `duration` was 151,457.683 s. For run 7 those values were 55,256.554 s and 28,117.260 s; the difference is close to, but not exactly, the 27,181.872 s sleep envelope. No complete monotonic-clock calibration explains these differences.

### Inactivity, overlap, environment and remaining evidence gaps

The historical H2 audit identified 251 matched Sleep/Wake pairs totaling 867,097.733 s (240.860 h) of event envelopes. Two major intervals were Sep 30 11:56:35.185–Oct 7 20:37:00.494 (176.674 h) and Oct 9 01:28:40.903–09:01:42.775 (7.551 h). Those envelopes explain long gaps but are not exact corrections to process elapsed time. A `DarkWake` event on Oct 8 was explicitly not treated as sleep: PS-A progress continued during it. There were six execution-log clock backsteps totaling 1.218 s. Periodic gaps beginning Sep 27 cannot be classified as sleep or active CPU from surviving records. The retained command/execution records show sequential main-run launches; no simultaneous PS-A runs contributing work were found, but complete process-tree CPU integration is absent.

`environment.txt` is a final snapshot only: Python 3.14.0, NumPy 2.5.3, NetworkX 3.6.1, `python-louvain=unknown`, macOS 15.7.4 arm64, and eight workers. Earlier session metadata records Python 3.14.0, NumPy 2.5.3, SciPy 1.18.1, NetworkX 3.6.1, python-louvain 0.16; a later system diagnostic identifies a MacBookPro18,3 / 8 CPU / 16 GB host. The early runs used four workers and later runs used eight. These records support a likely same-host lineage, but not an immutable environment or host fingerprint for every run. Sampled worker CPU percentages were below full utilization; multiplying elapsed time by eight would not recover CPU-hours.

There were 27 repeated checkpoint records beyond the expected 49,049 × 20 = 980,980, representing at least 270 repeated saved/reported trials after four progress-counter resets. Unsaved in-flight work may add more duplicated cost. Job completion coverage cannot remove these costs.

The earlier H2 audit's candidate 76.630770 h remains unaccepted. No complete original process accounting is present; run 4 has no end time; early sleep/awake logs do not cover Sep 24–27; some historical ASL files are no longer present in the current power-management log directory; per-run immutable environment records are absent; and the session duration clocks do not reconcile. **A credible full and comparable `T_PS-A` cannot be recovered from the evidence currently available.** Do not use the 71.560963 h partial amount, 76.630770 h conditional candidate, total calendar span, nominal worker-hours, or last ~2 h session as the registered denominator.

### Final bounded source check — 2026-10-20

The last search was limited to sources that could plausibly preserve run 4's missing endpoint: the unchanged `.local/phase2_population_size_scaling/{commands.log,execution.log,state.json,jobs/}`, the already identified compressed historical Codex session, retained power-management ASL, current Unified Log process/termination messages for 2026-09-24 through 2026-09-25, and Python diagnostic reports. No MAT/signal data or new biological result was opened.

The historical session confirms `state.json` still said `status=running`, `active_pid=14502`, with its last `updated_at=2026-09-25T12:36:34+0800`; the last progress line is at 12:36:58.861. A process probe begun at 16:26:41+08 and returned at 16:26:49.737 found no PID 14502 and no active children, while the persisted state remained stale. A second command at 16:27:36 returned no matching runner process. The next recorded PS-A launch began at 16:28:04. These checks establish only that the process was absent by the first probe; they do not provide a termination event or show whether work continued silently, waited, or stopped during the gap after the last progress record. The retained Unified Log query returned no attributable termination record, no matching Python diagnostic report was present, and the retained power-management ASL begins on 2026-09-28, after this run.

**Closure of this reconstruction attempt:** no new reliable end timestamp, CPU accounting, or activity classification was recovered. Run 4's endpoint remains bounded only by the last progress and later absence observation, not measured. The evidence search is closed for this work package; `T_PS-A` remains unresolved and H2 remains `RESOURCE NO-GO`. Do not fill the gap with 16:26, the 16:28 next-run start, a sleep assumption, or the prior 76.630770 h conditional estimate. Reopen only if a new, independently hashable source is supplied or recovered; otherwise use a separately reviewed prospective resource amendment.

## 3. Source and derived evidence hashes

These hashes identify evidence without copying neural signal files into the repository. `P/` means `.local/phase2_population_size_scaling/` in the local main workspace. The private derivatives are held at `$HOME/Library/Application Support/SRT-Pub/PSA_RUNTIME_EVIDENCE_2026-10-19/` with directory mode 0700 and file mode 0600. This is durable local storage, not an independent backup or immutable custody service. The `/tmp` originals were left untouched; the listed hashes were checked against the persistent copies.

| Source or derivative | SHA-256 |
|---|---|
| `P/commands.log` | `a852da536b4673998025c5c08373909bf82f63d112e8b46ee1855039b0da163a` |
| `P/execution.log` | `4db0ecc7ca3ca7a32af9d59e745cc935a6db6819f9be8f84f64f6f5288759c55` |
| `P/environment.txt` | `3035a7394b7e12c4168e04019e11acbf0e62a71c812218d7f992fb321b2a6fa1` |
| `P/state.json` | `c4cefcbb909534efaf92b252e4720a947f287e442704dc16d015b39d9262d03a` |
| `P/checksums.txt` | `a94931e00a1519acb05345a0cedd4e01414fd07787b750f0b0e36d9ee0df6f18` |
| `P/data_inventory.txt` | `11f6eafb660d6d7d4696f3fe5c67d534b529659aead85259b321384e42ee39dd` |
| `P/population_size_scaling.py` | `0e7af206456348b9eb91d5771d7cd4d18fe312ea4508b71a5772d7a47370b625` |
| `P/summarize_population_size_scaling.py` | `ae54e980a721948a63ae9ed57b5317d3ae8701105627b77ba48968a921700751` |
| `P/louvain_seed_ledger.jsonl.gz` | `226e52fb4c2d510a5cf033305489b9e2ae197716c0eec6215c2368ebc3fd1ae6` |
| H2 audit report in this HEAD | `05c1adafe2e685099ea0a7d96e15e28f691a9f4263ef296aa326a174d3b1807f` |
| `psa_history_inventory.py` | `7441a3d655d87d340e8f8f4713f5922c957b8323fdf3a1e0325787aecdfb4c98` |
| `psa_runtime_evidence.py` | `0bfe4dbe024d40de610d5e7c595bcead14e12b6c30650a413e0b66bafc98918a` |
| Rebuilt private job coverage CSV (6,006 unique completed IDs) | `648fab574d2f57fbb507f33fe41772a027b47028138e48e175420725da5b583a` |
| Rebuilt private 6,006-file hash manifest | `c777ece16da04aa36faca63fbd77184dd4e0c4d52d54f1e467455efb1fcbef9c` |
| Rebuilt full inventory JSON | `19acbc85a84e2c70fe5936cff60d9b765bd2ab8812e180a66d4e5aa2350926aa` |
| Rebuilt partial-interval manifest | `fcd063cd629f609aab36f95d3cc216b6166172beb78392ecfbdf83b9d79282ee` |
| Rebuilt arithmetic-only audit result | `fcde6b26c001c874322ed109716199cc99d569c1fd292c5fb45955f06b32ec69` |
| Private evidence README / reproduction note | `0ed0acedde1b320ef4f273c286f97f17bad8c81319edbf455840951d3162f9bc` |
| Historical Codex session, current compressed file | `01ca04291cb1dbb5aba0e14ecf7d07cf958862fa44b906e136f89eb53d4b866e` |
| Same session decompressed stream (matches H2 audit's recorded source hash) | `d7d15ddf2204bcdf2b8cddb5c36f01cf7169882ac78de2089ffa34ff626ae3af` |
| Current `/var/log/powermanagement/2026.10.07.asl` | `dd1bc1c8c35566fd5dccaa7304ae9eaee6fe43b003e238920daa27c629e7688e` |
| Current `/var/log/powermanagement/2026.10.08.asl` | `474ef377455dd90b620085fb3ad573ecce44745eb492bb7e32dd5034af1b37af` |
| Current `/var/log/powermanagement/2026.10.09.asl` | `9e926f03b90413c73f7e8bcfc62da669ab5e2ebbeb57f2fb80d4ef8bea957111` |

The inventory is reproducible from the unchanged local source directory with `uv run python Experiments/neuro_sleep_null_calibration/psa_history_inventory.py /PRIVATE/original/phase2_population_size_scaling /PRIVATE/new-output --utc-offset +08:00`; it writes the three inventory outputs listed above. The partial interval manifest is preserved exactly because its input is a line-anchored, source-hashed audit object; the unchanged `psa_runtime_evidence.py` command in the private README regenerates the arithmetic-only result. The helper SHAs are `7441a3d655d87d340e8f8f4713f5922c957b8323fdf3a1e0325787aecdfb4c98` and `0bfe4dbe024d40de610d5e7c595bcead14e12b6c30650a413e0b66bafc98918a`, respectively. The H2 report also records hashes for Sep 28–30 ASL and two October diagnostics. Those files were not found at their former paths during this re-check; their hashes and the event extraction remain documented in the H2 report, not independently re-read from those missing originals here. No MAT file was opened or modified.

## 4. Next minimum work for G0/T1

The preregistration §6.1 explicitly requires a comparable complete `T_PS-A`; the current evidence cannot satisfy that condition. The V1 72-hour / 288-CPU-hour cap was a prospective NC-0a-only envelope. It does not replace `T_PS-A` for G0 or T1, and NC-0a runtime cannot be scaled directly to the biological workloads. A separate discussion-only proposal now defines a synthetic benchmark and prospective absolute-budget route in `G0_T1_PROSPECTIVE_RESOURCE_BUDGET_AMENDMENT_DRAFT_2026-10-20.md`; that proposal is not effective and does not change the current `RESOURCE NO-GO`.

Before any NC-0 freeze or biological G0 output, the minimum resource work is:

1. The bounded historical search described above is closed for the currently available evidence set. Do not continue open-ended searches or fill gaps by extrapolation. Reopen only if a new independently hashable original source appears. Otherwise use a dated prospective amendment replacing the historical relative denominator with separately reviewed absolute G0 and T1 budgets. The linked resource-amendment proposal is draft only; it is not effective authorization.
2. On the intended host and locked G0 implementation, benchmark representative **nonbiological synthetic** graphs across the actual N, edge, degree-heterogeneity, leaf and connectivity/bottleneck profiles. Time the full path: graph copy/build, the registered 4E swap proposal count and connectivity checks, 200 Louvain trials per null graph, audit/checkpoint writes and retry/failed-output handling. Measure process-tree CPU, elapsed wall, sampled peak RAM, and disk growth at the chosen worker count, with repeated runs sufficient to estimate variability and tail cost. NC-0a provides one useful same-host synthetic observation, not this G0 benchmark.
3. Separately benchmark T1's correlation and MST reconstruction on synthetic matrices with the required dimensions and window lengths, plus its 2.45M Louvain workload. Set T1-GO or `T1-NOT-AUTHORIZED-RESOURCE` before viewing any G0 null output; T1 must not become an outcome-triggered add-on.
4. Include full result retention in the storage plan. The H2 ledger's estimates—about 3.60 GB for raw G0 edge endpoints, 78.4 MB for Q values, and about 28.76 GB if 1.7977B proposals were retained at 16 bytes each—are rough arithmetic only, not measured output size. Benchmark the actual serialization and specify a compact but independently auditable proposal/audit record before execution.
5. Complete the separate NC-0 identity H3 gate: faithfully reconstruct the fixed 120 original graph panel and replay the registered identity/Q checks against the locked data/code/runtime lineage. This is not a new null-result inspection and must precede NC-0 freeze.

Do not inspect new biological null results to choose resource ceilings, benchmarks, worker counts, T1 status, or storage rules. Until a complete historical denominator or independently reviewed prospective replacement and representative synthetic resource evidence exist, **G0 and T1 remain unauthorized on resource grounds**.

## 5. Work performed and boundaries

Read-only checks used: current PR head/status query; local NC-0a completion verifier and hash-chain audit; recomputation of the 16 stored case screens and 48 t statistics; public audit-summary comparison; read-only PS-A job/log inventory; and the existing runtime-evidence arithmetic checker against a newly rebuilt private manifest. The inventory matched 6,006 jobs and the checker returned arithmetic-only status. The exact execution HEAD's two CI runs remain successful: Governance Preflight `39206882108` and Neuro Null Synthetic Contract Tests `39206882059`. The PS-A derivative copies were separately SHA-256 checked against their temporary-source copies. No test, benchmark or biological computation was run for this document-only amendment.

No source code, raw PS-A file, MAT signal, NC-0a run artifact, prior PR comment, scientific threshold, seed, or budget was changed. No formal computation, G0/T1 run, merge, PR state change, or NC-0 freeze occurred. The derived metadata inventory and interval arithmetic files now have byte-identical, permission-restricted copies in persistent local storage; their `/tmp` originals remain untouched. This report is intentionally `draft` and `canonical: false`. The public audit-summary JSON was re-fetched from PR comment #6270568230 and parsed equal to the local invocation audit JSON; all 16 locally stored case-result SHA-256 values matched the public manifest. The public base64 encodes the JSON without a trailing newline; the declared hash matches the local JSON file including its newline, as already disclosed above.
