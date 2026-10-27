---
id: SRT-OBSERVED-CALIBRATION-NEXT-TASK-EVALUATION-20261026
type: experiment-proposal
status: draft
date: 2026-10-26
layer: operations
epistemic_layer: experimental
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_TWO_ATTEMPT_TERMINAL_CLOSEOUT_2026-10-26.md
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_FIXED_SAMPLE_V1_2026-10-26.json
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_REMEDIATION_SUFFIX_V1_2026-10-26.json
tags: [RIKEN, ResourceCalibration, DecisionGate, ReadOnly, NoNewRun]
---

# Next-task evaluation after the 6 OLD + 14 NEW terminal

**2026-10-27 follow-up:** the bounded T0–T3 analysis has been completed in [RCE-20](RCE20_READ_ONLY_RESOURCE_EVIDENCE_REPORT_2026-10-27.md). It supplies direct local evidence verification, 47-row coverage/cost tables and Swap attribution limits. T4 remains NO-GO; the historical proposal below does not grant new execution authority.

**Recommendation: `GO` for a narrow, read-only 20-row evidence audit; `NO-GO` for any fresh 27-row/full-baseline/null execution now.** No execution permission, additional UUID, retry or alternate run is created by this proposal. Source and cost facts come from the [two-attempt closeout](OBSERVED_CALIBRATION_TWO_ATTEMPT_TERMINAL_CLOSEOUT_2026-10-26.md) and the researcher's report, not a fresh direct read of private Q or Mac artifacts.

## 1. Why this new task is worth doing

The observed-only 47-graph calibration was designed to inform **resource feasibility** for broader scientific computation. Only **20/47** unique frozen graphs with **4,000/9,400** canonical Q have verified completed artifact records. The second run stopped on **host Swap used growth**, while its sampled scientific process-tree RSS remained under its own threshold. The unanswered practical questions are now:

1. **Value of existing evidence:** What is actually covered in the 20 completed graph/recording/N strata? How do graph construction, canonical Q, file I/O, cold cache and old/new instrumentation affect descriptive costs?
2. **Stop diagnosis:** Does retained Watchdog time-series evidence distinguish graph-specific memory growth, macOS swap-pool dynamics and unrelated concurrent host activity? If not, mark causal attribution **unknown**, not a scientific-executor defect.
3. **Decision usefulness:** Is completion of the missing **27** required for a concrete downstream scientific decision, or would it only demonstrate that a host can run longer? What evidence and compute environment would justify an entirely **new** study?

Without answers, changing code, buying hardware or commissioning a third run risks spending resources without better scientific inference.

## 2. Bounded candidate work packages

| Task | Decision now | Benefit / limits | Resource & risk |
|---|---|---|---|
| **T0: immutable terminal evidence inventory** | **GO / first** | Independent read-only local verifier pass for both old/new terminal directories, host claim/closure, hashes, authorized HEAD/UUID; obtain exact private anchor list without exposing private content | No new Q, no signal preprocessing, no change to source, ledgers or run artifacts; small local audit |
| **T1: 20-row cost/coverage analysis** | **GO / main** | Matrix for completed/uncompleted 47 rows by sample_order, graph N, recording/source window, cold/warm cache, row construction, Q phase, wall/CPU/I/O and available memory signals; separate six OLD and 14 NEW | Only read old/new recorded result JSON and validated audit logs; any missing field `UNKNOWN`; no projection to unsampled tails/U95 |
| **T2: host Swap attribution and failure timeline** | **GO / bounded descriptive** | Reconstruct startup-to-stop swap used/total/free, host free memory, RSS/CPU, row boundaries and Watchdog timestamps; if per-process OS memory-pressure evidence is absent, state causal attribution cannot be established | Read-only forensic timeline, no forced swap reset, no retest or active pressure experiment |
| **T3: value-of-information / resource options** | **GO / proposal only** | Present whether missing N/recording/source-window strata matter for G0/T1 resource decisions, and compare targeted new pilot vs isolated host vs hard-enforced Linux/cloud alternatives; identify permission/data constraints | Desk review; no live real-data execution, no promise of hardware feasibility |
| **T4: run missing 27, redo 47, 4,900 baseline or 4E null** | **NO-GO** | No authority to act under either spent UUID. Full 47 source-window clustered/tail coverage and signed new design still absent | Irreversible resource and governance risk. New scientific design + independent review + separately approved budget/authorization would be mandatory |

**Priority:** T0 → T1 → T2 → T3 as one **read-only** review task, not four parallel experimental efforts. T4 is deliberately outside the present task.

## 3. Read-only evidence and methods contract

Allowed inputs: private OLD/NEW `h3-summary.json`, `run-manifest.json`, `observed-cost-rows/*.json`, `h3-control.jsonl`, `h3-evidence.jsonl`, `watchdog.jsonl`, `remediation-account.json`, `remediation-closed.json`, original authorization/preparation evidence, host ledger and fixed public sample/packet. Use only the already-recorded row data **after** executing the official **read-only verifier**; do not modify or recompute Q, graph topology or raw signals. If a diagnostic requires private MAT/historical builder execution, mark it **not in scope** and propose separate authorization instead.

Required outputs in private workspace:
- **Terminal inventory:** immutable file SHA-256, official verifier result, unique OLD/NEW result identities, **20 completed** and **27 missing**, NEW unfinished suffix row 15 as *not committed*, and exact claim/closure terminal state.
- **Coverage and cost table:** 47 fixed sample rows with completed/partial/missing flags. For the 20 completed rows show exact recorded timing units and phase components if available; source-window clusters, graph size N, numerical-Q time, reconstruction/caching, RSS/host-memory telemetry; explicitly tag missing/ambiguous timestamps. Keep OLD and NEW as **two strata** because metrology and cache/cold-start differed.
- **Swap timeline:** launch baseline, sampled peaks and stop sample in **bytes** with time/row association; separate **host-level Swap** from **process-tree RSS**. State if needed process-attribution data were not captured. Avoid claiming peak swap growth was caused by row 15, by one graph size, or only by the scientific process.
- **One-page decision memo:** observed evidence, unknown/undersampled strata, whether new data are decision-critical, candidate resource environments, privacy/host controls, and a concise **new-study GO/NO-GO recommendation**. Share only aggregate/anonymized metadata in the public repo; never raw Q arrays or private graphs.

Do not pool row observations as independent samples when they share raw windows or recordings. The 47-row order was frozen prospectively, but the **stopping mechanism can bias the observed subset** toward early rows and lower-cost tasks. Do not treat 20/47 as a random representative sample or report a complete 47-row runtime bound, clustered U95, extrapolated G0 runtime or robust 4,900 baseline upper confidence limit.

## 4. Explicit acceptance gates

The read-only task is **accepted** only when:

1. The verified 6+14=20 / 4,000-Q total reconciles with exact 47 sample rows and original ordering; the 15th attempted NEW row is clearly excluded.
2. OLD and NEW terminal audit anchors, no-resume statuses, claim/receipt/closure and every reused result SHA remain consistent and no source/private experiment file was changed. If verification differs, stop analysis, report the discrepancy, do not repair data.
3. The table uses measured numbers with units and source artifact identity; no estimated figures are represented as measured. Unavailable host/background-process telemetry must be labeled unknown.
4. Research value is evaluated against actual downstream **decision gates**, especially whether missing N/recording/window coverage obstructs any resource bound for a prospective 4,900-graph observed baseline or 49,000-null G0-scale work. Distinguish a model-conditional point estimate from a statistical confidence bound and do not infer from the 20 finished rows without support.
5. A plain-language recommendation separates **(a) no further experiment**, **(b) a new narrowly targeted pilot**, and **(c) new isolated/hard-limited compute environment** with a documented evidence gap and prospective independent budget for each. Nothing launches any option.

## 5. Evaluation of a possible future experiment (not authorized)

A third, **new** study should be considered only if the read-only matrix demonstrates that completing a **specific missing size/recording/window stratum** is indispensable to a named SRT/RIKEN resource or scientific admission decision and that no existing H3/NC-0a evidence answers it. A blanket “finish the last 27 because they are unfinished” is **not** sufficient.

Before a new study could be approved, require all of the following:

- **Scientific value:** specific question, observable outputs, why current 20-row coverage fails, how targeted new observations would resolve it and what outcome would actually change a later decision.
- **Design independence:** new frozen target selection, graph/seed/Q identity and method compatibility, predeclared stopping/selection-bias handling, explicit interpretation of old/new heterogeneous cost data.
- **Resource realism:** independent resource feasibility review, conservative CPU/wall/I/O and tail estimates, host-wide Swap attribution uncertainty, real isolation of background processes and/or hard-enforced limits if moving platforms; validate runtime and numerical parity before using another environment. A macOS sampled RSS cap is **not** hard containment.
- **Data/security governance:** permitted private-data location and transfers, a separate append-only new-activity record, fresh approval and one-run identity, stable resource headroom, complete stop evidence, explicit maximum attempts. The consumed OLD/NEW exception cannot be rebranded as a new continuation.

**Decision today:** `READ_ONLY_ANALYSIS GO` / `NEW SCIENTIFIC COMPUTATION NO-GO` / `G0_T1 RESOURCE NO-GO`. Reassess only after verified T0–T3 outputs. Prefer making the next decision with existing data rather than new coding.

## 6. Short handoff for a local agent

> On the previously reviewed SRT-Pub source checkout, **read-only verify** the OLD and NEW terminal, fixed 47-row sample, host ledger and claim/closure; produce a private 47-row coverage/cost table and host-Swap timeline from saved artifacts only; distinguish 6 OLD / 14 NEW, 27 missing and the uncommitted NEW row 15; finish a one-page value-of-information and resource-options memo. Do **not** write to historical run directories, replay graphs or Q, launch supervised processes, rotate UUIDs, prepare approved authorizations, clean Swap or modify G0/T1. Mark missing private observations as unknown. Report evidence SHA-256 and source units; leave any public-facing summary in an independent Draft documentation PR subject to researcher review.
