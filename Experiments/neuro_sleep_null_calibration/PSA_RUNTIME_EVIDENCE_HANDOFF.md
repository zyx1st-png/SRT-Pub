---
id: SRT-NEURO-PSA-ACTIVE-TIME-LOCAL-EVIDENCE-HANDOFF-20261012
type: audit
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: protocol
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/neuro_sleep_null_calibration/NC0A_READINESS_AND_RESOURCE_LEDGER_2026-10-12.md
tags: [Neuroscience, NullCalibration, Runtime, Evidence, Handoff]
---

# PS-A historical active-time evidence — local-only handoff

**Current disposition: T_PS-A unavailable, H2 remains NO-GO.**

## Source availability and boundary

The remote GitHub repository does not track the historical original .local/phase2_population_size_scaling/commands.log, overwritten environment snapshots or all raw resumed-run interval logs. Codex R5 inspected some of these in a different local workspace, but its PR review summary is not a complete primary-source interval ledger. Do not infer a time from the final ~2-hour run, the multi-week calendar span, or one small benchmark sample.

The script psa_runtime_evidence.py is an offline, metadata-only source/interval arithmetic checker. It does not copy RIKEN signals to GitHub.

## Local operator steps (not completed here)

1. In a local workspace containing .local/phase2_population_size_scaling, read commands.log, each source run/scheduler log, the per-run environment evidence and job status artifacts. Do not commit raw logs or job records.
2. Make a PRIVATE manifest JSON following the example below. For each independently verified ACTIVE interval give the original source SHA-256, timestamped start and end line anchors, worker count, actual host ID and explanation of why that entire period is active. A calendar span or unexplained line gap is not sufficient.
3. Derive a metadata-only CSV containing exactly 6,006 unique completed job identifiers with columns job_id,state. Hash this CSV. This is a coverage check, not a new biological analysis.
4. Execute locally from Experiments/neuro_sleep_null_calibration:

   python psa_runtime_evidence.py /PRIVATE/PATH/psa_active_intervals.json --output /PRIVATE/PATH/psa_active_interval_audit.json

5. Independently review pauses, overlap, duplicated resumed work, worker/machine variability and comparability to the planned synthetic benchmark host. The arithmetic program never changes the scientific resource gate to GO.

## Example unfilled private manifest — deliberately NOT executable

~~~json
{
  "purpose": "PS-A_ACTIVE_TIME_METADATA_ONLY_V1",
  "timestamp_naive_utc_offset": "+08:00",
  "sources": [
    {"id": "runlog", "path": "/PRIVATE/PATH/original_run.log", "sha256": "FILL_WITH_ORIGINAL_SHA256"}
  ],
  "job_coverage_csv": {
    "path": "/PRIVATE/PATH/unique_completed_jobs.csv",
    "sha256": "FILL_WITH_CSV_SHA256",
    "id_column": "job_id",
    "status_column": "state",
    "completed_value": "complete"
  },
  "verified_active_intervals": [
    {
      "id": "session_001",
      "source_id": "runlog",
      "machine_id": "FILL_VERIFIED_MACHINE_ID",
      "workers": 8,
      "activity_basis": "verified_progress",
      "basis_note": "FILL_REAL_EVIDENCE_FOR_CONTINUOUS_ACTIVITY",
      "start": {"line": 0, "unique_text": "FILL_EXACT_START_LOG_SUBSTRING"},
      "end": {"line": 0, "unique_text": "FILL_EXACT_END_LOG_SUBSTRING"}
    }
  ]
}
~~~

The timezone +08:00 is illustrative ONLY; check the actual machine offset. Line numbers 0 are intentionally invalid. The checker requires log lines with one explicit ISO-style date/time per anchor; other timestamp formats need reviewed parser changes.

The only successful arithmetic status is ARITHMETIC_CHECK_ONLY_INDEPENDENT_REVIEW_REQUIRED. The sum of verified intervals is a candidate active elapsed duration, not directly measured CPU hours or proof of uninterrupted CPU use.

## Formal NC-0a aggregate resource limits — still unfilled

Before 16 cases × 8 chains × 32E execution, separately lock and independently review an absolute overall wall/CPU time budget, maximum parallel workers no higher than eight, peak process/aggregate RSS, usable disk and output reservation, per-case deadlines, machine/dependency manifest, case order, interruption and recovery policy. The new runner has per-chain limits but is not an approved full-battery execution launcher.

Never choose resource numbers to force a GO. If historical active time cannot be grounded, keep H2 NO-GO or obtain a prospective dated and independently reviewed alternate-budget amendment BEFORE any formal NC-0a.

## Minimal source-grounded PR return

- Original source log paths/identifiers and SHA-256 only (no raw contents), active interval table and excluded gap rationale.
- 6,006 unique completed job count and metadata CSV SHA-256.
- Candidate union active duration and separate nominal process-worker time with machine/worker comparability notes.
- Independent reviewer/date and unresolved gaps.
- Explicit RESOURCE REVIEW PASS or NO-GO, without conflating the arithmetic check with independent scientific authorization.

If primary logs/active work evidence are absent, report H2 unresolved rather than inventing an original runtime.