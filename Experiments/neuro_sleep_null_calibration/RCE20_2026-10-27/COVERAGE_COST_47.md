---
id: SRT-RCE20-COVERAGE-COST-20261027
type: experiment-audit
status: draft
date: 2026-10-27
layer: operations
epistemic_layer: experimental
canonical: false
claim_mode: evidence
---

# Fixed 47-row coverage and cost table

Saved-artifact descriptive measurements only. `OLD` and `NEW` have different metrology and independent one-entry caches. Times are seconds. `Build+ID` = correlation/diagnosis + inclusive historical builder + independent graph identity/canonical representation. `Q200` includes shared canonical representation construction. `Row` = graph-start to graph-result timestamp, excluding activity admission and the result event's own fsync. `I/O read` = native process endpoint read-byte difference, not physical SSD bytes. `RSS` = maximum retained periodic Watchdog sample whose task ID **and UTC** lie within this row; `UNKNOWN` means no matching sample. This stricter join can differ from the official verifier's task-ID-only RSS join. Full precision, per-phase CPU, hashes and cache bytes are in [CSV](coverage_cost_47.csv); nested builder components are not added twice. Uncommitted work appears in [phase measurements](phase_costs.csv), excluded from successful row costs.

| # | Record | State/window | N | Status/attempt | Cache | Row s | Build+ID s | Q200 s | Q CPU s | Read MiB | Sampled RSS MiB |
|---:|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | mouse01_sleep | wake/0 | 100 | COMPLETED / OLD | MISS | 2.959923 | 0.021604 | 1.744725 | 1.696920 | 64.859 | UNKNOWN |
| 2 | mouse01_sleep | wake/0 | 1150 | COMPLETED / OLD | HIT | 27.885303 | 1.183907 | 26.573172 | 25.271527 | 0.516 | 274.828 |
| 3 | mouse01_sleep | NREM/1 | 340 | COMPLETED / OLD | MISS | 8.025213 | 0.143634 | 7.191260 | 6.949814 | 28.414 | 282.578 |
| 4 | mouse01_sleep | NREM/1 | 3900 | COMPLETED / OLD | HIT | 116.828832 | 29.395128 | 87.179437 | 83.499075 | 0.027 | 1263.000 |
| 5 | mouse01_sleep | NREM/2 | 100 | COMPLETED / OLD | MISS | 2.283098 | 0.011105 | 1.689315 | 1.617840 | 25.523 | UNKNOWN |
| 6 | mouse01_sleep | NREM/2 | 765 | COMPLETED / OLD | HIT | 17.452754 | 0.515026 | 16.799893 | 15.897391 | 0.016 | 343.812 |
| 7 | mouse01_sleep | NREM/2 | 3900 | COMPLETED / NEW | MISS | 122.189319 | 29.642121 | 91.409305 | 88.126447 | 55.043 | 1572.734 |
| 8 | mouse02_sleep | wake/1 | 1725 | COMPLETED / NEW | MISS | 42.136794 | 3.682908 | 37.857961 | 37.226628 | 33.125 | 515.734 |
| 9 | mouse02_sleep | wake/2 | 150 | COMPLETED / NEW | MISS | 3.136042 | 0.018888 | 2.637351 | 2.611576 | 34.168 | 482.797 |
| 10 | mouse02_sleep | NREM/0 | 100 | COMPLETED / NEW | MISS | 2.059287 | 0.011713 | 1.674327 | 1.658707 | 15.312 | UNKNOWN |
| 11 | mouse02_sleep | NREM/0 | 765 | COMPLETED / NEW | HIT | 16.592829 | 0.498920 | 16.041285 | 15.281721 | 0.016 | 496.281 |
| 12 | mouse02_sleep | NREM/0 | 3900 | COMPLETED / NEW | HIT | 121.967772 | 34.891027 | 86.913861 | 84.036269 | 0.059 | 1010.734 |
| 13 | mouse02_sleep | NREM/1 | 100 | COMPLETED / NEW | MISS | 2.210324 | 0.016702 | 1.699181 | 1.671524 | 29.324 | 254.406 |
| 14 | mouse02_sleep | NREM/1 | 765 | COMPLETED / NEW | HIT | 14.494924 | 0.498977 | 13.946556 | 13.531845 | 0.000 | 326.078 |
| 15 | mouse02_sleep | NREM/1 | 3900 | COMPLETED / NEW | HIT | 111.905769 | 28.441063 | 83.294706 | 82.138144 | 0.047 | 1221.688 |
| 16 | mouse02_sleep | NREM/4 | 510 | COMPLETED / NEW | MISS | 11.461674 | 0.207656 | 10.730668 | 10.161363 | 29.242 | 307.141 |
| 17 | mouse03_sleep | wake/0 | 225 | COMPLETED / NEW | MISS | 5.706446 | 0.037191 | 5.088592 | 4.271248 | 41.582 | 273.797 |
| 18 | mouse03_sleep | wake/0 | 2600 | COMPLETED / NEW | HIT | 70.503009 | 11.728490 | 58.650111 | 56.235324 | 0.035 | 818.719 |
| 19 | mouse03_sleep | NREM/1 | 765 | COMPLETED / NEW | MISS | 15.073253 | 0.521771 | 13.996340 | 13.853245 | 33.785 | 333.688 |
| 20 | mouse04_day1_sleep | wake/0 | 340 | COMPLETED / NEW | MISS | 7.567727 | 0.100107 | 6.649827 | 6.088797 | 70.477 | 401.656 |
| 21 | mouse04_day1_sleep | wake/0 | 3900 | PARTIAL_NOT_COMMITTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 22 | mouse04_day1_sleep | NREM/1 | 1150 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 23 | mouse04_day1_sleep | NREM/2 | 100 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 24 | mouse04_day1_sleep | NREM/2 | 765 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 25 | mouse04_day1_sleep | NREM/2 | 3900 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 26 | mouse04_day1_sleep | NREM/3 | 100 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 27 | mouse04_day1_sleep | NREM/4 | 100 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 28 | mouse04_day1_sleep | NREM/4 | 765 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 29 | mouse04_day1_sleep | NREM/4 | 3900 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 30 | mouse04_day2_sleep | wake/1 | 100 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 31 | mouse04_day2_sleep | wake/1 | 765 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 32 | mouse04_day2_sleep | wake/1 | 3900 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 33 | mouse04_day2_sleep | wake/3 | 510 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 34 | mouse04_day2_sleep | wake/4 | 100 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 35 | mouse04_day2_sleep | wake/4 | 765 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 36 | mouse04_day2_sleep | wake/4 | 3900 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 37 | mouse04_day2_sleep | NREM/2 | 1725 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 38 | mouse04_day2_sleep | NREM/3 | 150 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 39 | mouse05_sleep | wake/0 | 100 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 40 | mouse05_sleep | wake/0 | 765 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 41 | mouse05_sleep | wake/0 | 765 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 42 | mouse05_sleep | wake/0 | 3900 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 43 | mouse05_sleep | wake/5 | 100 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 44 | mouse05_sleep | wake/5 | 765 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 45 | mouse05_sleep | wake/5 | 3900 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 46 | mouse05_sleep | NREM/2 | 225 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 47 | mouse05_sleep | NREM/2 | 2600 | NOT_STARTED / NONE | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

Rows 1–6 belong to OLD, rows 7–20 to NEW; row 7 also has partial **OLD** work without an OLD Q artifact. Row 21 has partial NEW build evidence and no committed Q. Rows 22–47 never started. These are 20 completed, one partial uncommitted and 26 never-started primary rows. Each complete row has exactly 200 saved Q values checked by the existing verifier; no Q was rerun.
