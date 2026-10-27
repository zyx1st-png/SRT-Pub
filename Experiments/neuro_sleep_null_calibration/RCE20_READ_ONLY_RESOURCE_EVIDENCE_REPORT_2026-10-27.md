---
id: SRT-RCE20-READ-ONLY-RESOURCE-EVIDENCE-20261027
type: experiment-audit
status: draft
date: 2026-10-27
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
---

# RCE-20: read-only resource evidence and feasibility assessment

**Evidence analysis completed; new computation NO-GO under the spent authorizations. G0/T1 remain RESOURCE NO-GO.** This report directly inspects saved local artifacts; it supersedes the *researcher-reported-only evidence boundary* of the initial #1135 closeout for the specifically checked files. It does not replace or edit either execution record. The unit correction below also corrects the earlier conversation: the numbers 7.93 and 10.08 were decimal GB, not GiB.

## 1. Scope, identities and what was actually verified

- Reference documentation: Draft #1135, `f1f0e8eba64fd95fff23838aaef44240df42979e`; resource proposal #1124 checked at `ff85deec88ff700affeb489c95d0ea6c6295eb4b`, still DRAFT / NOT EFFECTIVE.
- OLD: `cf726336-0f3b-4506-9cd3-cb36da3f7e12`, executed `b4a4b34ed7432efbf0d289a8b244345f73cf6a43`. NEW: `69fd0045-ac42-4711-bd26-c8dd9bb3a7c6`, executed `a415d6315a1c620e00227bf7df0b3666133778b6`.
- Full 47-row sample SHA-256 `f29acb99a05387b128f724bf818e3f402f7ced8a4080c12da4a936b9284d95c4`; 41-row suffix `9dbb10990d0cdffa2a864e6aaec12ca42bafcf85783e05668c1b8e06b5d28808`; remediation packet `208121aad2f3a9d07c0b6dc98a005b5a126a4f3cc3c887c24f7cb6bbfa7639ae`.
- Method SHA-256 `c0cf7f85a18bad844e190deefbe83e8ab55f0dbe194299be0ef94e2c828e38c3`; runtime lock `62ca4ed82e8ddbebe9513a3b33349405c0d7513b60e7651d813e9469276c0488`; source inventory `6a8357ac0b815c434421a31dc6c294c292b5c144713f49c52b5344038235ece2`.

Using the frozen #1134 implementation and locked Python 3.14.0, called `verify_original(OLD,state)`, `verify_run(NEW,state,_remediation_packet=load_packet())` and `verify_joint(NEW)`. Results: OLD and NEW **VERIFIED_TERMINAL**, combined **VERIFIED_JOINT_TERMINAL**, **6 + 14 = 20 unique graphs / 4,000 saved Q**, `completed=false`, `resume_allowed=false`. Both authorization attempts and the sole remediation exception are spent. No retry/new UUID, authorization, claim or host-ledger event was created in RCE-20.

The official verifier validates saved graph/input/seed/Q/partition hashes, ordered result records and terminal/accounting anchors. RCE-20 additionally recomputed all file SHA-256 values and seven hash chains using an independent standard-library implementation. It checked 52 original files (both run inventories, both preparation inventories, host ledger/receipt/lock files) before and after analysis: byte hashes, lengths, device/inode, mtime/ctime and link counts were unchanged. Exact identity comparisons do not independently rerun Louvain or prove graph derivation from raw signals. No MAT/HDF5 signal file was opened; current raw-MAT bytes were not newly attested. Recorded source identities retain their originally verified provenance.

Saved runtime: macOS 15.7.4 arm64, Python 3.14.0, NumPy 2.5.3, SciPy 1.18.1, NetworkX 3.6.1, python-louvain 0.16, h5py 3.16.0. Historical PS-A SciPy/HDF5 versions were not fully recorded; H3's successful replay is retained evidence, not proof that all historical environment details are pinned.

[Verification summary](RCE20_2026-10-27/verification_summary.json) distinguishes official checks from independent byte/chain recalculation. [Exact file inventory](RCE20_2026-10-27/evidence_sha256.csv) contains 56 entries: 52 private-artifact identities without private absolute paths, plus four frozen public input files. Local hashes and Git copies are not independently immutable custody or external human peer review. The analysis remains AI-assisted.

## 2. Fixed coverage: the missing evidence is structured

[47-row coverage/cost table](RCE20_2026-10-27/COVERAGE_COST_47.md), [full-precision CSV](RCE20_2026-10-27/coverage_cost_47.csv), [211 persisted phase measurements](RCE20_2026-10-27/phase_costs.csv).

Rows 1–6 are completed OLD, 7–20 completed NEW, row 21 partial/uncommitted NEW, rows 22–47 never started. OLD also began row 7 without committing a Q artifact; NEW's row 7 is its sole completed identity. No row is counted twice. Saved incomplete phases consume activity resources but are excluded from completed-row sums.

| N | Planned | OLD complete | NEW complete | Uncompleted |
|---:|---:|---:|---:|---:|
| 100 | 11 | 2 | 2 | 7 |
| 150 | 2 | 0 | 1 | 1 |
| 225 | 2 | 0 | 1 | 1 |
| 340 | 2 | 1 | 1 | 0 |
| 510 | 2 | 0 | 1 | 1 |
| 765 | 11 | 1 | 3 | 7 |
| 1150 | 2 | 1 | 0 | 1 |
| 1725 | 2 | 0 | 1 | 1 |
| 2600 | 2 | 0 | 1 | 1 |
| 3900 | 11 | 1 | 3 | 7 |

| Recording | Planned | OLD | NEW | Uncompleted |
|---|---:|---:|---:|---:|
| mouse01_sleep | 7 | 6 | 1 | 0 |
| mouse02_sleep | 9 | 0 | 9 | 0 |
| mouse03_sleep | 3 | 0 | 3 | 0 |
| mouse04_day1_sleep | 10 | 0 | 1 | 9 |
| mouse04_day2_sleep | 9 | 0 | 0 | 9 |
| mouse05_sleep | 9 | 0 | 0 | 9 |

Completed states are Wake 7 (OLD 2 / NEW 5), NREM 13 (OLD 4 / NEW 9); uncompleted are Wake 15 / NREM 12. All ten N values have at least one saved resource observation, but six N strata have only one graph (150,225,510,1150,1725,2600), and N=1150 has **OLD metrology only**. Four completed N=3900 graphs come exclusively from mouse01/mouse02. There is no completed observed-only N=3900 cost on mouse03/mouse04-day1/mouse04-day2/mouse05. This says nothing adverse about their historical H3 identity.

The 20 graphs cover **11/23** planned distinct source windows and **4/6** recording sessions. OLD has three completed windows, NEW nine, with one window shared across attempts. Of the **nine windows absent from H3**, exactly **three** now have all N=100,765,3900 observations: nine of the planned 27 unseen-window tasks. Six such windows remain wholly unmeasured: mouse04-day1 NREM windows 2/4, mouse04-day2 Wake windows 1/4, mouse05 Wake windows 0/5 (IDs are the frozen zero-based window indices). H3 plus these completed rows covers **43/49** source windows with at least one historical/canonical graph computation; this is coverage of recorded computations, not a newly validated cache-reuse grant. Among the remaining 27 tasks, 18 target these six windows, nine are coverage supplements. Twelve of the planned 23 windows have no completed RCE row; a thirteenth contains completed row 20 and partial row 21.

This is a right-truncated, source-ordered prefix after resource stops, not 20 random or independent observations. Graphs share windows; recordings/states, N and order are confounded. Do not apply independent-row standard errors, bootstrap these 20 as a population sample, or call missing work ignorable censoring. No new significance test or full-population forecast is performed.

## 3. Measured cost decomposition (OLD and NEW separate)

All times below are sums over **completed rows only**, seconds. Reconstruction is explicitly split to avoid hiding its verification cost.

| Component | OLD 6 rows | NEW 14 rows |
|---|---:|---:|
| HDF5/raw-window cache access | 1.665518 | 4.707097 |
| Correlation + zero-variance diagnostics | 0.390951 | 1.414757 |
| Inclusive historical graph builder | 3.748380 | 13.131412 |
| MST (inside builder; do not add again) | 3.518082 | 12.114749 |
| Edge-selection residual (inside builder) | 0.230298 | 1.016663 |
| Independent graph identity + canonical representation | 27.131073 | 95.751365 |
| Canonical 200 Q, including shared representation | 141.177802 | 430.590070 |
| Canonical 200 Q: process CPU | 134.932567 | 416.892838 |
| Resource snapshots before + after | 0.423764 | 0.003379 |
| Result serialization | 0.010353 | 0.031682 |
| Result file write/fsync | 0.004405 | 0.010987 |
| Phase audit append/fsync | 0.014189 | 0.030572 |
| Result audit append/fsync | 0.000679 | 0.001590 |
| Graph-start to result timestamp | 175.435123 | 547.005169 |

For these completed rows, correlation + builder is only 4.139331/14.546169 s (OLD/NEW), whereas graph-identity/canonical representation adds 27.131073/95.751365 s. Q200 costs 141.177802/430.590070 s: about 80.5%/78.7% of recorded committed-row wall. The identity stage is necessary in the measured contract; dropping it would measure a different implementation. Builder wall already contains MST and edge top-up; add neither component to builder again. Result-event timestamps precede that event's own append/fsync; controller/watchdog totals cover the missing tail and other activity costs.

| N | OLD rows | OLD Q200 wall range s | NEW rows | NEW Q200 wall range s |
|---:|---:|---:|---:|---:|
| 100 | 2 | 1.689315–1.744725 | 2 | 1.674327–1.699181 |
| 150 | 0 | UNKNOWN | 1 | 2.637351–2.637351 |
| 225 | 0 | UNKNOWN | 1 | 5.088592–5.088592 |
| 340 | 1 | 7.191260–7.191260 | 1 | 6.649827–6.649827 |
| 510 | 0 | UNKNOWN | 1 | 10.730668–10.730668 |
| 765 | 1 | 16.799893–16.799893 | 3 | 13.946556–16.041285 |
| 1150 | 1 | 26.573172–26.573172 | 0 | UNKNOWN |
| 1725 | 0 | UNKNOWN | 1 | 37.857961–37.857961 |
| 2600 | 0 | UNKNOWN | 1 | 58.650111–58.650111 |
| 3900 | 1 | 87.179437–87.179437 | 3 | 83.294706–91.409305 |

The ranges demonstrate observed size dependence, not record-independent scaling or tail bounds. N=3900 completed-row reconstruction including identity spans approximately 29–35 s and Q200 approximately 83–91 s here; graph structure, subset, source/session and host activity can change these costs. Complete per-recording and per-N aggregates are in [descriptive summary](RCE20_2026-10-27/descriptive_summary.json); raw Q values never enter this analysis.

| Recording / metrology | Complete rows | Row wall sum s | Q200 wall sum s | Reconstruction+ID sum s |
|---|---:|---:|---:|---:|
| mouse01_sleep / OLD | 6 | 175.435123 | 141.177802 | 31.270404 |
| mouse01_sleep / NEW | 1 | 122.189319 | 91.409305 | 29.642121 |
| mouse02_sleep / NEW | 9 | 325.965415 | 254.795895 | 68.267854 |
| mouse03_sleep / NEW | 3 | 91.282708 | 77.735042 | 12.287451 |
| mouse04_day1_sleep / NEW | 1 | 7.567727 | 6.649827 | 0.100107 |

OLD's resource snapshots launched host-monitor helpers inside the scientific process, contributing 0.423764 s over its six successful rows and ultimately an unknown-group stop. NEW uses external host telemetry; its corresponding in-worker snapshots cost 0.003379 s across 14 rows and have no host-helper launch. These small completed-row costs do not make OLD and NEW paired replicates: different graphs, source order, warm state and two separate starts prevent attributing timing differences solely to the fix.

## 4. Cache, I/O, setup and incomplete work

- OLD: 3 raw-window hits / 3 misses; 282,348,000 logical HDF5 array bytes loaded across completed rows. NEW: 5 hits / 9 misses; 774,588,000 logical bytes. The maximum saved retained window is **115,344,000 B = 110.001 MiB**, below the retained 256-MiB cache cap. Arrays/graphs/temporary correlations add memory; the cache cap is not a process limit. The same raw window at the OLD/NEW boundary is loaded again in NEW because caches do not survive activities.
- Completed-row before/after process I/O deltas: OLD **125,153,280 read / 663,552 write B**; NEW **358,838,272 read / 1,757,184 write B**. Endpoints omit some earlier/later metrology/audit writes, and cannot replace total filesystem-output accounting. The sum of exclusive phase I/O differs because phase counters and endpoint acquisition bracket different intervals. Native counters are process-attributed disk I/O, not physical SSD throughput; logical window bytes are a different measure.
- Supervised source/job/seed admission already reads approximately **8.099 GB per attempt**: OLD 8,099,422,208 B in 7.037681 s / 6.329615 CPU s; NEW 8,099,209,216 B in 8.092828 s / 6.553594 CPU s. These are recorded combined admission measurements, not pure hashing throughput; parent-side preflight is additional. Full source hashing can warm OS caches before row reads. Do not call these cold-disk tests or multiply setup cost by graph count.
- OLD partial row 7 saved subset/resource/cache/correlation phases but no builder/Q result. Its graph-start UTC is 11.544 ms after `watchdog_stop_requested`, while the stop record still identifies row 6: cross-process sampling/logging and the termination interval allow brief worker advancement. Do not turn that signed timestamp difference into negative compute time. NEW later completed that graph once.
- NEW partial row 21 saved subset/resource/cache/correlation and inclusive builder/MST/edge-selection phases; no completed independent graph-identity/canonical representation phase or Q phase/result was committed. Stop-request time is 26.136746 s after that graph's start; the exact interrupted call and its uncommitted cost are UNKNOWN. Its known completed phases are preserved in the phase CSV but cannot stand in for a completed Q observation.

Whole-activity wall includes admission, partial work, audit, shutdown and other gaps; it cannot be recovered by dividing complete-row sums by completed count. Sparse Watchdog rows 1/5 (OLD) and 10 (NEW) have no **strict task-and-time matched** periodic RSS sample. Their process row peaks are UNKNOWN, not zero. The official task-ID-only RSS join and lifetime `ru_maxrss` are separately described; lifetime high water is inherited across rows.

## 5. Activity and cumulative resource reconciliation

| Quantity | OLD | NEW |
|---|---:|---:|
| Watchdog supervised wall s | 183.267597 | 583.133237 |
| Watchdog process-tree/controller accounted CPU s | 188.484654 | 631.911462 |
| Committed-row timestamp intervals summed s | 175.435123 | 547.005169 |
| Unallocated whole-activity minus committed intervals s | 7.832474 | 36.128068 |
| Controller elapsed in summary s | 183.411021 | 583.224764 |
| Loop-sampled aggregate RSS high water GiB | 1.364639 | 1.640915 |
| Host free-memory minimum % | 33 | 31 |

The unallocated residual contains setup/partial-row work, gaps and monitoring; it is not an idle-time estimate or an exact additive phase. Watchdog CPU accounting uses the declared maximum of sampled process-group and waited-child CPU plus monitor CPU; it is not a direct per-stage CPU sum.

The reproduced cumulative account separately charges OLD wall **201.318418 s**, OLD CPU upper charge **332.891224 s**; NEW full-controller wall **601.575242 s**, native/high-water CPU **648.056392 s** before closing reserves. Adding the fixed NEW closing allowance (5 wall s / 40 CPU s / 65,536 output B) produces **807.893660 wall s (0.224415 h), 1,020.947616 CPU s (0.283597 CPU-h), 3,856,440 output B** total. Those charges include both attempts and uncertainty allowances, not one continuous 20-row runtime. All were within total caps; resource headroom does not revive a spent claim.

The final ordinary NEW disk/RSS snapshots include the emergency reserve; its release at stop explains part of the final output-size decrease. Use the charged complete account, not just directory size at an arbitrary sample. Preserve exact costs and distinct field semantics rather than trying to force sampled CPU and native waited CPU to match.

## 6. Swap stop: evidence and attribution

See the [Swap event analysis](RCE20_2026-10-27/SWAP_EVENT_ANALYSIS.md) and [saved time series](RCE20_2026-10-27/swap_timeline.csv). OLD has 34 persisted periodic samples; NEW 110. NEW baseline used **7,925,200,322 B = 7.380918 GiB**, cached final peak **10,075,116,666 B = 9.383184 GiB**; difference **2,149,916,344 B**, over 2 GiB by **2,432,696 B**. This validates the recorded `SWAP_GROWTH_LIMIT`; no threshold was changed.

Host Swap is not process RSS. No all-process memory history, per-process swap/page-out attribution, compressor timeline or exact native-reading timestamps were captured. The scientific process may contribute, other activity may contribute, or both; quantitative and causal attribution are **UNKNOWN**. Peak scientific RSS remained below 4 GiB, host free memory above 20%, AC/thermal/sleep checks remained valid. These observations do not disprove host Swap pressure or justify overriding the approved stop. Sampled monitoring can miss transient memory peaks.

## 7. Are the remaining 27 necessary?

**Not as an indivisible remainder.** Finishing a stopped list is not itself a scientific goal or an execution right. Important missing evidence is (a) six H3-unseen source windows, (b) large-N costs for later recording sessions, (c) corrected NEW metrology at N=1150, (d) repeated source-window/recording support and a predeclared held-out cost test. These gaps matter for forecasting a *canonical observed baseline*. Existing H3 already supplies all-N/six-session identity and dual-order cost evidence, so rereading H3's saved costs should precede commissioning redundant Q work. H3 does not supply the new runner's detailed cache/I/O instrumentation for its six unseen windows.

Even a complete 47 would remain an initial deliberately structured sample, not a reliable full-population predictive U95. A future total-cost model must include the 4,900 source builds, 980,000 observed Q trials, setup/cache/IO/scheduling and allowed-failure costs, account for clustered windows and unsupported tails, and pass prospectively frozen validation. The source graph feature census and exact execution/storage contract still need alignment with #1124's candidate model.

These observed-only data cannot measure 4E exchange cost, rewired-graph optimizer tails, lossless proposal compression, four-worker global scheduling or storage stability. G0 still requires its **49,000 null graphs, 9,800,000 null Q trials, 1,797,712,000 proposals** to be prospectively costed against the actual frozen executor. No new biological null result may tune that model. T1 has distinct matrix-reconstruction costs, a separate resource gate and G0-GO prerequisite. `T_PS-A` remains unresolved; RCE-20 does not repair its historical baseline. NC-0a's `MIXING-UNRESOLVED` interpretation remains unchanged.

## 8. Decision and bounded alternatives

[One-page decision memo](RCE20_2026-10-27/NEXT_EXPERIMENT_DECISION.md). **No real computation is authorized now.** Recommend closing the old two-attempt calibration permanently. Do not request a blanket remainder-27 restart. If the researcher continues toward a full observed baseline, first choose an execution environment with stable, attributable resource headroom and define a small new question addressing missing source/high-N costs; independently review that design and resource stop-loss before a new run.

RCE-20 supplies descriptive evidence and a documented decision basis. It does not activate #1124, relax Swap rules, approve a new UUID, infer a population bound or authorize G0/T1.

## 9. Reproduction and read-only evidence preservation

Private analysis scripts and their hashes are indexed in [analysis provenance](RCE20_2026-10-27/analysis_provenance.json); they never open signal files or call a Q runner. The original inputs remain at their existing private locations. To reproduce in a separate analysis output directory: use the frozen verifier source with bytecode writes disabled; verify OLD/NEW/joint; compare 47-row input identities and committed artifact hashes; export only scalar phase/cost fields; pair Watchdog rows by task ID and UTC graph interval; sum exclusive phases without nested MST/residual; recalculate byte hashes/chains; compare complete original inventories before/after. No execution entrypoint or claim-writing function is used.

The official implementation is shared with the executed pipeline; its successful saved-Q integrity check is not an independent implementation of Louvain or historical source reconstruction. RCE-20's independent recalculations cover byte hashes, chain links, order/count reconciliation, unit conversions and resource/coverage summaries. No original file, ledger or experiment identity was edited; all new files are analysis products. Public exports contain no signal, neuron list, edge list, partition, Q array, credentials or private absolute path. This analysis did not commission additional scientific computation.
