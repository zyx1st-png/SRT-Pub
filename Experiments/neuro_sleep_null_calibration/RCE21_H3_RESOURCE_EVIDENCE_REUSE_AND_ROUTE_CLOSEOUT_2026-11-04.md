---
id: SRT-RCE21-H3-RESOURCE-EVIDENCE-REUSE-20261104
type: experiment-audit
status: draft
date: 2026-11-04
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/neuro_sleep_null_calibration/H3_120_SCIENTIFIC_CLOSURE_2026-10-26.md
  - Experiments/neuro_sleep_null_calibration/H3_120_PUBLIC_CLOSURE_2026-10-26.json
  - Experiments/neuro_sleep_null_calibration/G0_RIKEN_H3_FIXED_120_DUAL_ORDER_PACKET_DRAFT_2026-10-24.json
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_FIXED_SAMPLE_V1_2026-10-26.json
  - Experiments/neuro_sleep_null_calibration/RCE20_READ_ONLY_RESOURCE_EVIDENCE_REPORT_2026-10-27.md
  - Experiments/neuro_sleep_null_calibration/RCE20_2026-10-27/coverage_cost_47.csv
  - Experiments/neuro_sleep_null_calibration/RCE20_2026-10-27/NEXT_EXPERIMENT_DECISION.md
tags: [RIKEN, H3, RCE20, RCE21, ReadOnly, CostComparability, DecisionGate]
---

# RCE-21 — reuse H3 evidence before considering further observed-only calibration

**Result: `READ-ONLY DESK AUDIT COMPLETE / NEW COMPUTATION NO-GO / OBSERVED-ONLY RESOURCE CALIBRATION PAUSE RECOMMENDED`.** This is a scoped, noncanonical operations analysis, **not** a new experiment, researcher authorization, amendment or new CURRENT NEXT. The RCE-20 terminal 6+14 observed rows remain final; the two used UUIDs and the one-time exception remain spent. G0/T1 remain `RESOURCE NO-GO`.

## Question and sources

**Decision question:** Does the completed H3 evidence make another observed-only resource calibration sufficiently useful to justify a new experiment now? We assess source/size coverage, cost transferability and whether any missing evidence would unlock a named downstream resource decision. We do not treat “finish the remaining 27” as a decision in itself.

The audit read **already committed public text/JSON/CSV** at prior Draft #1135 head `f1de9da276a246e6c4327358dcaa090b0799d18d`, plus merged `main` routing (`AGENTS.md` → `SRT_AI_START.md` → `_SRT_AGENT_RETRIEVAL_PROFILE.md` → `STATUS.md`; local bootstrap in its controlling order). No private Mac run directory, saved Q vectors, source MAT/HDF5, new official verifier execution or independent private artifact rehash was performed **in RCE-21**. H3 scientific closure and RCE-20's private verifier/hash findings are inherited **as their original reported/provenance-bound evidence**, not freshly independently checked here. This desk audit directly checked public packet row identities, 47-row status/phase scalar exports and H3 public aggregate values.

Version/binding:
- H3 executed HEAD `147d5ca268ef0c579c41f314a6f5e5ec8cafc6d2`, UUID `e6abc8fd-831f-4076-b412-e5a7481a027b`; frozen H3 dual-order packet SHA-256 `669cc9148cb92e1d6bd57dce5276fe8ecdbda04bb7b35c2c9dbeef32a1875a4a`.
- RCE observed OLD `cf726336-0f3b-4506-9cd3-cb36da3f7e12` (6 completed), NEW `69fd0045-ac42-4711-bd26-c8dd9bb3a7c6` (14 completed), new executed HEAD `a415d6315a1c620e00227bf7df0b3666133778b6`; 20 completed/47 fixed; 27 uncompleted, including 1 partly executed/uncommitted.
- H3 and RCE share frozen source inventory SHA-256 `6a8357ac0b815c434421a31dc6c294c292b5c144713f49c52b5344038235ece2` and effective method SHA-256 `c0cf7f85a18bad844e190deefbe83e8ab55f0dbe194299be0ef94e2c828e38c3`. Same method identity is *not* same per-row metrology, graph/subset or run environment.

## 1. What H3 already pays for

H3's saved public closure verifies a **fixed 120-row panel**: 6 recording sessions × 2 states × 10 N, with 12 rows per N. It reports exact replay of **24,000 historical-order Q** and new computation of **24,000 canonical-order Q** (each H3 graph 200+200 = 400 trials). This was **not** the 4,900-graph population, nor new RCE-21 computation. H3 resource observations: **6,269.349765 s wall**, **6,479.524378 s accounted process-tree CPU**, sampled peak group RSS **2,033,582,080 B (~1.89 GiB)**, 1 worker, 1,148 resource samples, and a shared-APFS run directory terminal file-byte total of 4,091,123 B (Watchdog exit included emergency scratch). No full-population cost U95 or row-wise process memory peaks was established.

H3 encompasses **40 distinct recording/state/window identities**, and all six sessions. The RCE-20 47-row candidate includes **23 distinct window identities**, 14 already in the H3 set and **nine H3-unseen**. A public packet join on recording + state + numeric window + N gives **eight nominal H3/RCE row pairs** sharing the same source file and frame hashes and the same recorded Louvain seed-vector hashes; all eight have **different selected-neuron-subset hashes and graph IDs**. There are **zero exact shared graph IDs** between the prospective 47 RCE sample rows and H3's 120. This is deliberate H3 exclusion, **not an opportunity to reuse H3's computed Q values or to claim a direct paired-timing experiment**.

Of the nine H3-unseen source windows, RCE-20 has completed all three planned N observations for exactly **three**: `mouse01_sleep/NREM/window2`, `mouse02_sleep/NREM/window0`, and `mouse02_sleep/NREM/window1`. **Six are still not directly measured by either H3 or finished RCE canonical observed calibration:**

| Recording | State | Window (zero-based) | Missing planned RCE sizes |
|---|---|---:|---|
| mouse04_day1_sleep | NREM | 2 | N100, N765, N3900 |
| mouse04_day1_sleep | NREM | 4 | N100, N765, N3900 |
| mouse04_day2_sleep | Wake | 1 | N100, N765, N3900 |
| mouse04_day2_sleep | Wake | 4 | N100, N765, N3900 |
| mouse05_sleep | Wake | 0 | N100, N765, N3900 |
| mouse05_sleep | Wake | 5 | N100, N765, N3900 |

Thus the **H3 + RCE completed union is 43/49 finite-N source windows** with at least one recorded graph computation. This is *window provenance/identity coverage*, **not** new-runner resource cost coverage, graph-level repetition, a population sample, a G0 resource bound or a license to reuse old Q. RCE-20 alone has **11/23 planned windows, 4/6 sessions, 20/47 committed graphs**; six later-recording N strata remain thin.

## 2. Compatibility and cost transfer

The companion [strict comparability matrix](RCE21_2026-11-04/H3_RCE20_COST_COMPARABILITY.csv) juxtaposes each N without calculating misleading ratios.

| Aspect | H3 120 | RCE-20 20 committed observed | Reuse judgement |
|---|---|---|---|
| Sources and finite N | Six sessions; both states; all ten N | Four sessions; ten N; 11 of 23 planned windows | **GO** for source/size coverage and finding missing windows |
| Scientific kernel identity | Historical insertion-order **and** canonical sorted-edge trials | Canonical sorted-edge only; exactly 200 Q/graph | Shared effective method SHA helps reproducibility assessment; **no direct Q reuse** |
| Measured row wall cost | Both orders, **400 total Q** plus H3 runner reconstruction/recording | 200 canonical Q plus stage-by-stage source/build/identity/I-O; two OLD/NEW versions | **NO-GO** for direct row wall median multiplication, halving H3 time or inferring a canonical-only calibrated tail |
| H3 per-N cost distribution | 12 dual-order row times per N, retained as public min/median/max | 1–4 completed rows per N; q200 scalar phase time | **GO** for qualitative N dependence; **NO-GO** for paired quantitative transfer or pooled SE/U95 |
| Cache, I/O and identity-cost phases | No comparable detailed per-stage endpoint data in public H3 closure | Detailed RCE-20 scalar phase/CSV data | **NO-GO** for extrapolating the RCE cache+IO fractions to 4,900 without validation |
| Host and stopped-prefix selection | Completed 120-row H3, non-hard macOS sampled memory backend | Two right-truncated 6+14 attempts; host-level NEW Swap growth stop | Do not assume shared system load, stable cache state, independent samples or causal Swap attribution |
| G0 null/4E/T1 workload | Did **not** run null exchange+Q or T1 rebuild | Did **not** run null exchange+Q or T1 rebuild | **NO-GO** for upgrading biological G0/T1 from this evidence |

The H3 public `dual_order_row_cost_by_N` distributions cover **both** 200-Q orders and H3 reconstruction/recording costs; the RCE-20 `canonical_200_Q_including_shared_representation_wall_s` series is a **single canonical Q phase** within its full row. Their numerical ranges (see CSV) are presented **side by side only**, without ratios or interchangeability. Same effective Q method does not erase graph, old/new metrology, cache, cold-start, process instrumentation or sample-order differences. H3's row-by-recording timing distributions are not published in the public closure JSON used here; we cannot independently claim detailed per-session cost bounds from it.

A useful high-N diagnostic is available but *not* a safe tail model: H3's N3900 dual-order **400-Q** row median ~**188.79 s** (12 rows, six sessions), whereas RCE's four completed N3900 **200-Q phase** times span ~**83.29–91.41 s**, all from mouse01/mouse02, with separate build+identity overhead ~29–35 s. These are different units, graph subjects and observables. Their apparent approximate scaling is **not evidence** of an all-sessions 200-Q cost bound, nor a valid H3-to-RCE calibration factor.

## 3. What new computing would and would not change

**What a narrowly selected new observed-only pilot might change:** source/session coverage for the **six unseen windows** and estimates of *the new runner's* N765/N3900 construction/identity/Q/cache costs in later sessions, but only on that frozen sampled panel and host. A previously floated six-graph proposal (N765/N3900 across three later-recording regimes) would at most touch **three windows**, not all six unseen windows, and does not prove feasibility or population tails. Its ≤1h/≤1 CPUh candidate envelope is an unvalidated proposal, **not an approved bound**. Observed-calibration costs from earlier and later sessions are right-truncated and cannot supply a guaranteed held-out upper-tail estimate.

**What that pilot would not change:** G0's separate **49,000 null graphs, 9,800,000 null Q trials, and conditionally 1,797,712,000 4E proposals**; topology-dependent optimizer tails, scheduling/cold-cache, failed-work accounting, storage and external transfer; historical `T_PS-A` and T1 reconstruct costs. The current G0 resource amendment is `DRAFT / NOT EFFECTIVE`; independent new null-specific full-workload evidence and a prospective resource decision remain necessary. RCE-20 explicitly found `SWAP_GROWTH_LIMIT` on **host-wide** Swap with no per-process causal attribution. H3's separate smaller Swap growth on another session does not identify the source of RCE's growth, nor guarantee a new-run outcome.

**Value-of-information judgement:** Absent an existing **named, authorized downstream scientific or resource decision** that would change based on these exact later-window canonical observed costs, a third observed-only run would primarily buy descriptive precision rather than remove the binding G0/T1 resource obstacle. The marginal scientific value is **LOW at present**, while engineering, resource and private-data governance costs would be positive and the two historical single-use permissions are exhausted.

## 4. Final project-level decision recommendation

| Option | RCE-21 finding | Next action |
|---|---|---|
| A — Preserve H3+RCE20, park observed-only resource calibration | **RECOMMENDED / HIGH BENEFIT-COST** | Archive read-only facts; leave prior Draft PRs and private terminal artifacts intact; no new code, data handling or computational authorization. Return research attention to the one merged-main `CURRENT NEXT` cognition programme (CN-2 E2 paper-only task/readout feasibility) |
| B — Continue *desk-only* modelling | **ON-DEMAND, NOT A NEW AUTOMATIC CYCLE** | Only if a named future consumer needs an extra documented identity/coverage/comparability table, and only using saved evidence |
| C — Authorize targeted new observed-only calibration | **NO-GO NOW** | Reopen **only after** a specific downstream decision is identified, H3 reuse limits documented, a prospectively frozen discriminative sample/holdout with quantified information gain is designed, host resource isolation and strict numerical equivalence checked, and independent budget/data/attempt review completed. Never call it a resume or swap the old UUID |

**Proposed route disposition:** `OBSERVED_ONLY_RESOURCE_CALIBRATION = PARKED / ON_DEMAND SUPPORT`; `RCE21_DESK_AUDIT = COMPLETE`; `NEW COMPUTATION = NO-GO`; `G0/T1 = RESOURCE NO-GO`. This is **an AI-generated recommendation in an unmerged Draft documentation PR**, not a change to merged `STATUS.md`, current research owner, formal independent resource approval, or a researcher-signed status transition. The author can accept/adjust the park decision before any formal promotion.

### Exact re-entry trigger

Only reopen this resource-calibration subroute when **all** are explicit:

1. **Named downstream decision** (e.g. a prospective approved G0 resource-feasibility comparison) that a particular missing source/size cost measurement could materially change.
2. **Required evidence** and expected decision shift that cannot be obtained from existing H3+RCE20 facts or non-executing analysis.
3. **Separate new design and platform** with prospective selection, held-out/clustered inference plan, environment and Q parity, workload-specific CPU/wall/Swap/storage risk and permitted private-data handling.
4. **Fresh researcher and independent resource authorization** with immutable new IDs and no use of OLD/NEW spent claim or expanded historical caps.

If these are not present, **STOP**. Do not create an RCE-22 by default, launch new Q, replicate the remaining 27, or run G0/T1. These gates govern resource expenditure, not the author's ability to discuss SRT ideas.

## 5. Audit limits and reproducibility

- Public JSON+CSV arrays and SHA-bounded provenance were read through GitHub from **#1135 frozen HEAD**. Cross-join counts and per-N public cost distributions were calculated directly in a read-only in-memory pass.
- This document contains no raw Q arrays, neuron IDs, MAT payloads, private filesystem paths, credentials or unreported new terminal SHA-256. It does not claim independent on-Mac verification of H3 or RCE20 private artifacts.
- `main` `STATUS.md` continues to identify the **cognition / CN-2 E2** CURRENT NEXT; this historical resource subroute does not become another CURRENT NEXT. Old program and historical `NOT YET RUN` phrasing remain period-accurate, not rewritten.
- No code, scientific protocol, result, merged governance, execution log, ledger, receipt or authorization is changed by this PR.
