---
id: SRT-RCE20-SWAP-EVENT-20261027
type: experiment-audit
status: draft
date: 2026-10-27
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
---

# Swap event analysis from saved Watchdog evidence

**Stop-rule consistency VERIFIED; process-level causal attribution UNKNOWN.** All bytes below are actual saved readings; GiB = bytes / 2^30. This is forensic saved-artifact analysis, with no pressure experiment or new source computation. [Full time series](swap_timeline.csv) has both attempts' initial baseline, all periodic resource records and cached terminal native state. `STOP_CACHED_STATE` deliberately leaves live RSS/free-memory columns unknown: terminal RSS=0 is after termination, whereas native Swap state was cached earlier.

| Quantity | OLD | NEW |
|---|---:|---:|
| Periodic records | 34 | 110 |
| Persisted interval median s | 5.476561 | 5.264637 |
| Persisted interval range s | 4.879690–5.571706 | 4.551397–6.124206 |
| Initial Swap used B | 5,397,419,130 | 7,925,200,322 |
| Initial Swap used GiB | 5.026738 | 7.380918 |
| Peak retained by monitor B | 5,443,220,930 | 10,075,116,666 |
| Used growth B | 45,801,800 | 2,149,916,344 |
| Pool total initial/peak GiB | 6/6 | 8/10 |
| Final pool free B | 1,024,395,837 | 662,301,573 |
| Minimum pool free sampled B | 999,230,013 | 441,188,352 |
| Loop-sampled process-group RSS peak B | 1,465,270,272 | 1,761,918,976 |
| Host free-memory minimum % | 33 | 31 |
| Stop reason | UNKNOWN_PROCESS_GROUP_MEMBER | SWAP_GROWTH_LIMIT |

Configured loop polling is 0.5 s; regular logs are deliberately written about every 5 s, with host native telemetry sampled/cached on a separate ≥2-s rule. Actual record gaps above are **not** the maximum resource-check detection latency. An exact acquisition UTC is absent for individual native readings. Peak summary fields may reflect loop samples not durably emitted as regular records, so a peak's exact time/RSS pairing can be UNKNOWN.

## NEW time relation (all timestamps UTC, 2026-10-26)

| Retained event | Swap used B | Pool total B | Process RSS B | Host free % | Interpretation |
|---|---:|---:|---:|---:|---|
| Run baseline | 7,925,200,322 | 8,589,934,592 | UNKNOWN | UNKNOWN | No exact acquisition UTC; formal runner lease starts 15:15:58.357676 |
| 15:16:19.477585 / row 7 | 7,908,423,106 | 8,589,934,592 | 1,649,131,520 | 44 | Largest *persisted regular* RSS; monitor's cumulative peak was larger, exact peak time unknown |
| 15:19:35.875714 | 7,807,759,810 | 8,589,934,592 | see CSV | see CSV | Minimum regular Swap used; used amount initially decreased |
| 15:25:14.659991 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Start of partial full-sample row 21, N3900, mouse04-day1 Wake window 0 |
| 15:25:34.167155 | 7,955,944,570 | 8,589,934,592 | 971,276,288 | 39 | Partial row 21; wall 575.854961 s |
| 15:25:39.585129 | 8,148,746,240 | 8,589,934,592 | 1,044,234,240 | 31 | Last ordinary periodic sample; used growth 223,545,918 B, below stop threshold |
| 15:25:40.796737 | UNKNOWN at exact request time | UNKNOWN | UNKNOWN | UNKNOWN | Watchdog requests SWAP_GROWTH_LIMIT; wall 582.437873 s; raw native snapshot not included in this event |
| 15:25:41.404580 terminal | 10,075,116,666 | 10,737,418,240 | UNKNOWN live / 0 after kill | UNKNOWN live / minimum31 | Cached pre-stop native state first persisted here; final process RSS=0 is a distinct post-kill sample |

The source reads Swap before deciding the stop and keeps `latest_macos_state`, `swap_peak` and pool peaks for the terminal record; it does not newly read Swap after killing the group. Thus the final native state supports the threshold calculation, but its record UTC is not its exact sampling time. The abrupt difference between the last periodic reading and cached terminal reading cannot be converted into an instantaneous per-process swap rate. Current-pool `total/free` dynamically changed; neither initial free space nor an 8-GiB initial pool was a fixed future swap-capacity promise. Data/VM free-space minimum 51,855,462,400 B (48.294163 GiB) stayed above the unchanged reserve and is not additive across the two APFS views.

Exact rule check: 10,075,116,666 − 7,925,200,322 = **2,149,916,344 B**; threshold **2,147,483,648 B**; overage **2,432,696 B = 2.320000 MiB**. Small overage does not invalidate the approved strict `>` stop rule. No statement is made about an unsampled true peak.

## What is and is not attributable

- NEW's completed-row RSS endpoints range roughly 150–488 MiB, with temporary build/identity allocations much larger. Retained raw-window cache at most 110.001 MiB is not the complete memory footprint. Sampled RSS is resident memory, not total virtual memory, compressor usage or process swap allocation.
- This stop happened during row 21, after its last durable builder/MST/edge-selection phase and before a durable independent identity/Q phase. This is temporal association. **Which call was active at the crossing is UNKNOWN**; no Q artifact for row 21 exists.
- There is no time series of all other host processes, per-process swap/page-out bytes, compressor/physical-footprint accounting or total virtual allocation. Scientific-process contribution: **UNKNOWN**. Other applications/system contribution: **UNKNOWN**. Their shares: **UNKNOWN**. No leak diagnosis follows from these data.
- No unknown child was observed in NEW; one compute process was the recorded maximum. AC power/normal thermal/caffeinate remained valid; free-memory minimum 31% and sampled RSS peak 1.640915 GiB did not cross their own gates. These independent metrics do not disprove a host-level Swap stop.
- OLD's stop is a different operational failure: helper `(pmset)` with captured PID/PPID/PGID, not a Swap breach. OLD stopped requesting termination while the worker advanced from completed row 6 to uncommitted row 7. Retain that sampling/termination race rather than forcing the last task label to match the child's last log.

A future host comparison would need prospectively chosen telemetry and environment control; current process lists or a restarted Mac cannot reconstruct 2026-10-26 attribution. No new active diagnostic or trial was run. The consumed exception stays closed, irrespective of unspent time/CPU caps.
