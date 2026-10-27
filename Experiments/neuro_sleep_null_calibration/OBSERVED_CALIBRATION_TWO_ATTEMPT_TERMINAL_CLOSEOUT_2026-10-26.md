---
id: SRT-OBSERVED-CALIBRATION-TWO-ATTEMPT-CLOSEOUT-20261026
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
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_TELEMETRY_INCIDENT_AND_REMEDIATION_DRAFT_2026-10-26.md
  - Experiments/neuro_sleep_null_calibration/OBSERVED_ONCE_REMEDIATION_READINESS_2026-10-26.md
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_REMEDIATION_SUFFIX_V1_2026-10-26.json
tags: [RIKEN, ObservedBaseline, Terminal, ResourceCalibration, StopLoss, NoRetry]
---

# Observed-only 47-graph calibration: two-attempt terminal closeout

**2026-10-27 evidence follow-up:** [RCE-20](RCE20_READ_ONLY_RESOURCE_EVIDENCE_REPORT_2026-10-27.md) directly verified the saved local OLD/NEW/joint terminals, completed-row identities, host claim/closure and exact file/hash-chain inventory. Its measured cost and Swap analysis supersedes the researcher-reported-only evidence boundary below for those checked artifacts. The original executions remain unchanged; this note preserves the provenance of the initial closeout.

**Historical closeout / non-canonical / no new execution authorization.** This document records the researcher's 2026-10-26 report of **two already-ended activities**. It is a documentation-only successor to engineering preparation records in #1132–#1134; their historically accurate, earlier `NOT YET RUN` statements must **not** be retroactively rewritten. The GitHub author has inspected the frozen execution-source Watchdog condition and related PRs, **not** the private Mac terminal files or numerical Q arrays. Local terminal quantities and verification outcomes below are **researcher-reported**, not newly replicated by this documentation commit. The [terminal conversation archive](https://github.com/zyx1st-png/SRT-Pub/pull/1134#issuecomment-6420229211) preserves the same provenance distinction.

## Fixed subject and immutable execution identities

- Initial primary sample: **47 fixed observed graphs × 200 canonical Louvain Q trials = 9,400 proposed trials**, full sample SHA-256 `f29acb99a05387b128f724bf818e3f402f7ced8a4080c12da4a936b9284d95c4`.
- **OLD / first formal attempt**: UUID `cf726336-0f3b-4506-9cd3-cb36da3f7e12`; execution HEAD `b4a4b34ed7432efbf0d289a8b244345f73cf6a43`. Official private verifier previously reported `VERIFIED_TERMINAL`, **six completed primary rows / 1,200 Q**, `completed=false`, `resume_allowed=false`. Stopped by Watchdog for an unknown scientific process-group member, later supported as worker-side `pmset` host telemetry; original private artifacts and old ledger are preserved. Do not revise its historical cause or execution identity.
- **NEW / single exceptional suffix attempt**: UUID `69fd0045-ac42-4711-bd26-c8dd9bb3a7c6`, HEAD `a415d6315a1c620e00227bf7df0b3666133778b6`; exactly the original **rows 7–47** frozen as a 41-row suffix, suffix SHA-256 `9dbb10990d0cdffa2a864e6aaec12ca42bafcf85783e05668c1b8e06b5d28808`, packet SHA-256 `208121aad2f3a9d07c0b6dc98a005b5a126a4f3cc3c887c24f7cb6bbfa7639ae`.
- The researcher reports authentic use of the unique, personally bound authorization through the formal entry; authorization-file SHA-256 `03a9e63e1c7760a4677bcaf79af1be28e85a92c7c58c2d1038eff1f59fe23bc2`. The previously generated pending-approval draft was left unchanged. The unique remediation claim was consumed and closed; there was **no bypass, UUID rotation or retry**.

## Terminal outcome

| Activity | Completed primary rows | Canonical Q | Status | Interpretation |
|---|---:|---:|---|---|
| OLD | 6 of 47 | 1,200 | `VERIFIED_TERMINAL` / non-resumable | Old worker telemetry caused operational stop |
| NEW | 14 of 41 | 2,800 | `STOPPED_BY_WATCHDOG` / `SWAP_GROWTH_LIMIT` | First 14 suffix rows saved; suffix row 15 interrupted and **not counted** |
| **TOTAL** | **20 of 47** (42.55%) | **4,000 of 9,400** | `VERIFIED_JOINT_TERMINAL`, `completed=false`, `resume_allowed=false` | Distinct metrology versions, incomplete fixed calibration |

**27 primary rows remain uncompleted.** Combined coverage is **6 OLD + 14 NEW**, *not* one continuous 20-row benchmark or an achieved 47-row cost survey. “Joint terminal verified” means the saved partial execution is audit-consistent, **not** that the planned scientific/resource calibration completed.

## Second stop and measured/charged resources

The Watchdog recorded host **Swap used** growth from **7,925,200,322 bytes (7.380918 GiB)** to **10,075,116,666 bytes (9.383184 GiB)**, with exact recorded difference **2,149,916,344 bytes**. The earlier 7.93/10.08 values were decimal GB and were incorrectly labeled GiB; RCE-20 corrects that unit error. The fixed safety threshold is **2 GiB = 2,147,483,648 bytes**; this exceeded the threshold by **2,432,696 bytes** (approximately **2.32 MiB**). Mac dynamically expanded the swap pool from 8 to 10 GiB. Frozen `nc0a_watchdog.py` uses `swap_peak - swap_initial > limits.swap_growth_stop_bytes`, so **`SWAP_GROWTH_LIMIT` is consistent with the approved fail-stop rule**, irrespective of the narrow overage. The terminal native-state values were cached before termination; terminal RSS=0 was measured after killing the group, not simultaneously with those Swap readings.

| Accounting field | Researcher-reported terminal |
|---|---:|
| NEW Watchdog supervised wall time | 583.13 s |
| NEW process-tree accounted CPU | 631.91 s |
| NEW sampled peak aggregate RSS | 1.64 GiB |
| **Aggregate OLD + NEW + closure conservative wall charge** | **807.89 s** |
| **Aggregate OLD + NEW + closure conservative CPU charge** | **1,020.95 s** |
| **Aggregate charged output** | **3,856,440 bytes** |
| Lowest Data/VM free space (shared APFS availability, **not additive**) | ~48.30 GiB |
| Lowest host free-memory fraction | 31% |
| Swap-pool free reported at stop | ~0.62 GiB |

Wall/CPU/sample-RSS, disk, temperature, AC and unknown-process group conditions reportedly **did not** trigger a separate stop. The RAM limit was a **sampled** 4-GiB policy, not an OS hard container. Host Swap growth is not the same measure as runner RSS; these samples do not identify which process or system activity caused the swap growth. The old and new activities have different host-telemetry instrumentation and cold/cache timing; keep all resource columns version-tagged.

## Audit and custody

The initial closeout recorded the researcher's report that the private NEW summary, run manifest, Control/Evidence/Watchdog chains, single-use host ledger, combined accounting JSON and terminal closure receipt were accepted by the official `VERIFIED_JOINT_TERMINAL` verifier. **RCE-20 has now repeated that read-only verification and independently recalculated file/chain hashes**: see the [exact SHA-256 inventory](RCE20_2026-10-27/evidence_sha256.csv) and [verification/chain-tip summary](RCE20_2026-10-27/verification_summary.json). File hashes and chain tips are distinct; in particular the NEW Watchdog file hash is `9911da472c11cafb59858df62d67195c8d8134c421c75a6af642eab008aea964`, while its chain tip is `5b0ee884a0b826e40e9fa4e25e4c6b10142b8f3490f99dffa6acf67b20c78d9a`. No original artifact was changed. Raw signals, neuron lists, partitions, Q arrays and private absolute paths remain private.

## Scientific and governance conclusion

**Resource stop-loss worked; fixed 47-graph resource calibration was not completed.** Nothing in the partial 20-row sample establishes the complete 47-row upper-tail runtime, source-window clustered uncertainty, robust U95, 4,900-graph observed baseline feasibility, biological null feasibility or G0/T1 admission. The 20 saved rows **do** support scoped, descriptive, independently auditable per-row cost analysis; do not extrapolate unsupported N strata/recordings, ignore cold-start/cache differences or treat partial coverage as representative.

Both research-specific activity authorizations are **spent and terminal**. **NO RESUME, NO UUID-ROTATED RETRY, NO AUTOMATIC REMAINDER-27 COMPLETION, NO RETROACTIVE BUDGET OR SWAP-THRESHOLD RELAXATION.** Preserve #1132/#1133/#1134 and all private receipts/logs as executed. Any genuinely new experiment needs a **new scoped scientific question**, independently reviewed prospective design, separately approved resource envelope and new personally entered researcher authorization; it is not a continuation of these consumed permissions. **G0/T1 stay `RESOURCE NO-GO`.**

**Next work is strictly read-only:** see `OBSERVED_CALIBRATION_NEXT_TASK_EVALUATION_2026-10-26.md` for evidence extraction, host-Swap attribution limits and whether a separately authorized experiment would add adequate scientific value.
