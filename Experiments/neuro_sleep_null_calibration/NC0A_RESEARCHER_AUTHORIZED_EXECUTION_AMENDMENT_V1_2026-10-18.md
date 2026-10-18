---
id: SRT-NEURO-NC0A-RESEARCHER-AUTHORIZED-EXECUTION-V1
type: proposal
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
title: NC-0a researcher-authorized execution amendment
date: 2026-10-18
scope: prospective execution governance for the synthetic NC-0a battery only
dependency:
  - Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
  - Experiments/neuro_sleep_null_calibration/NC0A_MACOS_NATIVE_RESOURCE_AMENDMENT_DRAFT_2026-10-18.md
tags: [Neuroscience, SyntheticNull, ResearcherAuthorization, Draft]
---

# NC-0a researcher-authorized execution amendment V1

**Prospective draft; not an execution authorization.** This amendment records the researcher's decision to keep independent scientific review while taking personal responsibility for whether to execute the synthetic NC-0a battery. It replaces the previous requirement for third-party cryptographic execution signatures, an administrator-installed reviewer trust anchor, and an off-machine real-time signed authority ledger **for this NC-0a route only**. It does not claim that researcher self-authorization is independent approval, that GitHub history is immutable, or that an AI-assisted review is external human peer review.

The previous signed-approval and custodian design remains preserved in the earlier R7–R11 records, `nc0a_execution_engine.py`'s signed launcher, `nc0a_authority_ledger.py`, the V3 resource draft, and the 2026-10-18 production-readiness handoff. Those requirements were introduced to prevent replay, local ledger resets and unreviewed execution. The researcher has explicitly decided that this cryptographic separation is disproportionate for this synthetic-only run and accepts the resulting accountability and tamper-resistance limits. The old mode is not silently rewritten; its launcher remains available as a legacy route. This amendment is the only route that expresses the new policy.

## Activation conditions for one run

This draft becomes operational only for a single, uniquely identified NC-0a run after all of the following are recorded together:

1. At least two distinct independent review records cover the exact clean HEAD and jointly cover methods, statistics and implementation. Each record must identify the reviewer as a human reviewer or an AI model, link to its public PR #1114 comment, state a decision, and list any blocking findings. Open blockers stop execution. AI review records must explicitly say they are not external human peer review. These records support scrutiny; the launcher does not claim to cryptographically prove reviewer identity or independence.
2. The researcher fills the V1 commitment package, confirms the exact protocol, a single UUID and private output path, and chooses an absolute resource envelope no higher than the candidate ceilings below. The researcher accepts every listed residual risk and records a UTC confirmation time.
3. The full canonical commitment object and its SHA-256 are posted to a top-level PR #1114 comment **before the first process starts**. The launcher fetches that public comment and checks that its embedded commitment exactly matches the local package. The public post is an inspectable external copy, not an immutable custody service.
4. The final clean Git HEAD, preregistration, this amendment, runtime lock, all execution source hashes, fixed seed manifest, protocol and host environment match the commitment. Any commit or dependency change requires a new review and commitment.
5. The exact experiment UUID is bound to one absolute run directory. Recovery must use that same directory, plan, seed schedule and task order. A new directory or UUID is a new commitment and must be precommitted separately; it cannot be used to silently duplicate or replace an outcome.
6. The Watchdog's sampled macOS preflight passes immediately before each invocation. The signed-by-self resource values and volume UUIDs must match the current host. The internal Data and VM volumes must each satisfy the 40 GiB launch floor and 30 GiB reserve. The result path must be on the identified internal APFS Data volume.
7. The researcher types the exact confirmation phrase containing the experiment UUID. This is a deliberate human action, not an independent authorization credential.

The launcher reuses the existing formal task dispatcher and `MACOS_SAMPLED_PRESSURE` Watchdog. It does not invoke a test-only executor, alter scientific seeds, or skip the scientific/task-integrity checks. This is a separate prospective researcher-commitment gate; it does not call the legacy third-party-signature launcher. The Watchdog samples process-group RSS and system memory pressure, monitors swap growth, internal storage, AC power, sleep assertion and thermal state, and terminates the supervised process group when a configured stop condition fires. Sampled RSS is not an OS-enforced memory ceiling and can miss a transient peak.

## Fixed scientific contract

This amendment changes execution governance only. It retains 16 fixed synthetic graph cases (four families × N={100,340,1150,3900}), eight independently seeded chains per case, 32E attempted swaps per chain, the E/2E/4E/8E/32E checkpoints, 16 separate 1,000-proposal BFS-oracle streams, 48 paired comparisons, the existing fixed seed derivation, connectivity/degree/edge-count invariants, all current test thresholds and failure rules. Any failed screen, oracle mismatch, invalid graph, missing case or incomplete checkpoint is recorded; it cannot be repaired by choosing new seeds, dropping a case, changing a threshold or retrying until results pass. A statistical screen pass must continue to be labeled `MIXING-UNRESOLVED`.

The prior exposure remains disclosed: R4 reported an informal reviewer-seeded check of four of the sixteen cases before formal execution; R10 reported an 8E performance probe; R11 reported a separate nonformal 32E factor-MST probe, including an initial failed harness attempt and a successful four-chain attempt. None is formal NC-0a validation; none may be counted as a formal result or used to adjust a threshold after seeing the data.

## Candidate absolute envelope; not approved by inclusion here

The H2 audit did not establish an accepted historical `T_PS-A`. Therefore the candidate ceilings below are prospective loss limits for NC-0a only, not a reconstructed historical baseline, a completion-time guarantee, or a resource basis for G0/T1. The researcher must record the actual chosen values in the commitment and may choose lower values. This V1 launcher rejects values above the following ceilings; a higher limit requires a new prospective code and policy review.

| Control | Candidate ceiling or rule | Basis and limitation |
| --- | --- | --- |
| Compute workers | 4 | Reuses the tested macOS spawn path and the R11 4-worker long-chain probe. |
| Cumulative elapsed wall time | 72 hours, including sleep and all inter-invocation gaps | About 44–50× the proposal-only projection from the available 8E/32E probes. The projection does not measure the full battery and is not an upper bound. |
| Cumulative accounted CPU | 288 CPU-hours | About 49–51× the proposal-only projection. CPU-hours are separate from elapsed wall time. |
| Per-case / per-oracle stop | 12 hours / 30 minutes | A task loss ceiling. Failures and retries count against the overall caps. |
| Sampled process-group RSS | 4 GiB cap with existing early-stop margin | Sampled telemetry only; not a hard limit or complete process-tree peak. |
| System memory pressure | Stop below 20% free | macOS `memory_pressure` sample; cannot prevent an allocation peak between polls. |
| Swap | Record current pool total/used/free; stop if sampled system-wide `swap_used` grows by more than 2 GiB from invocation start | `free` is telemetry, not future paging capacity; system-wide changes are not attributable only to NC-0a. |
| Internal Data and VM volumes | At least 40 GiB free at launch; maintain 30 GiB reserves | Checked separately even though they share an APFS container. Current measurements must be refreshed; unrelated host writes can consume space. |
| Run output | At most 4 GiB allocated; retain at least the committed output-volume reserve (candidate 30 GiB) | Each result and audit file is created without overwrite. A full disk or failed `fsync` stops the run. |
| Host state | AC power, normal thermal/performance telemetry, active `caffeinate` sleep assertion | Does not protect against power loss, OS crash or unreported thermal throttling. |
| Recovery | Fixed-order, same-seed task-level restart from zero, at most one operational retry per case | Completed results must re-verify; failed attempts are preserved; no outcome-dependent retry. Unpaired or damaged logs block automatic resume. |

The successful R11 engineering probe measured 3,993,600 proposals over four 32E chains on one N=3900 factor-MST fixture: 459.234 seconds wall, 1,813.454 CPU-seconds, about 633 MB peak sampled process-group RSS, 34% minimum sampled system free memory, and no sampled increase in swap-used. The R10 8E probe measured 998,400 proposals in 130.600 seconds wall and 473.747 CPU-seconds. Linear proposal-only projections for the 44,937,216 long-chain proposals are approximately 86–98 minutes wall and 5.7–5.9 CPU-hours. These are short, topology-specific performance observations. The 16,000 full-BFS oracle proposals, all case metrics, graph generation, reports, host contention and failure recovery were not represented by the 32E probe. The candidate caps are therefore generous stop limits, not a reliable completion bound.

The 72-hour/288-CPU-hour values remain **candidate values pending the researcher's explicit decision**. This amendment does not use the incomplete 71.56-hour or conditional 76.63-hour PS-A figures as `T_PS-A`. NC-0a execution, even if complete, does not close H2 and does not authorize or establish the feasibility of biological G0 or T1.

## Local records, external copies and recovery

For each UUID, the run directory stores the exact researcher commitment package, formal run manifest, per-case immutable reports, `execution.jsonl`, Watchdog `watchdog.jsonl`, stdout, and per-invocation audit summaries. The existing fsynced hash-chain logs reject altered records, malformed tails and unpaired starts. Resource totals include failed invocations; elapsed wall is charged from the first invocation timestamp, so pauses and sleep do not reset the wall cap. On resume, the local logs must verify, every start must have a terminal record, the same package and directory must be present, and the latest exact audit-summary JSON/hash must already be posted to GitHub. An unknown cost, missing summary, mismatched public anchor, or incomplete battery summary prevents resume.

After each invocation, the researcher posts the generated audit summary and SHA-256 to a top-level PR comment before attempting recovery. At completion or failure, the final summary and hashes should also be posted. A normal GitHub comment and local hash chain are **not** immutable or independently administered; the repository owner could edit or delete them. Their purpose is to leave a publicly inspectable provenance trail, not to claim tamper-proof custody. The launcher does not require a third-party signing key or a remote administrator ledger.

Operational retry is restricted to recorded execution failures. A statistical NO-GO, any failed anomaly criterion, or a valid but scientifically unfavorable result is terminal and cannot be rerun. If the watchdog or host fails so that start/terminal pairing or resource cost cannot be established, the run remains incomplete and the launcher refuses automatic resume; a new execution decision and public explanation are required.

## Remaining risks and scope boundary

- Researcher self-authorization has no third-party authorization guarantee. This is a deliberate governance choice, not an independent approval.
- Different AI-model reviews can provide useful adversarial checks, but they do not constitute external human peer review. The record must say which occurred.
- Public GitHub copies and local hash chains are editable by sufficiently privileged repository/local administrators.
- Sampled macOS memory controls may miss short-lived peaks; system OOM can disrupt the application or operating system before a poll.
- Resource caps may stop an incomplete battery; that is a recorded NO-GO, not a license to increase the cap or change scientific conditions after inspecting results.
- H2 remains open. This NC-0a-only prospective envelope does not change the pre-registered G0/T1 resource gate, data identity requirements, or NC-0 freeze criteria.

The state of this document is draft until an independent current-HEAD methods/statistics/implementation review is recorded and the researcher completes a specific commitment. Even after those records exist, launch remains subject to the current Mac disk, power, thermal, memory-pressure, environment, and Watchdog preflight.
