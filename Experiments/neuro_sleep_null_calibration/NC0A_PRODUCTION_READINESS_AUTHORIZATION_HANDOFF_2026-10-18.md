---
id: SRT-NEURO-NC0A-PRODUCTION-READINESS-HANDOFF-20261018
type: proposal
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
title: NC-0a production environment and independent authorization handoff
date: 2026-10-18
scope: candidate approval packet; no execution authority
dependency:
  - Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
  - Experiments/neuro_sleep_null_calibration/NC0A_MACOS_NATIVE_RESOURCE_AMENDMENT_DRAFT_2026-10-18.md
tags: [Neuroscience, SyntheticNull, ResourceGate, Handoff]
---

# NC-0a production environment and independent authorization handoff

**Decision state: NOT READY TO SIGN FOR EXECUTION.** This packet presents checkable evidence and the decisions an independent approver must make. It is not an approval, resource-policy JSON, signature, experiment UUID, or instruction to start the formal battery. The V3 amendment remains a draft. This packet does not amend the scientific preregistration, authorize NC-0a, or authorize biological G0/T1.

## Evidence fixed at preparation

Prepared against clean PR HEAD `5755d660745f8dc5572b7e2d3d9e5642c3d3f458` on 2026-10-18. **The signing HEAD must be re-read after this packet and any repair commits land**; a signature over this preparation HEAD would be stale. Both then-current PR checks (`governance-preflight`, `unit-tests-only`) passed. A newly created, isolated local virtual environment is at `~/.local/share/srt-pub/nc0a-pr1114-py311/bin/python` (absolute local path: `/Users/zhangyuxin/.local/share/srt-pub/nc0a-pr1114-py311/bin/python`). It uses Apple Silicon Python 3.11.15, NumPy 2.3.5, SciPy 1.17.1, macOS 15.7.4; the underlying Python binary SHA-256 is `b0af800fb9c6f2be1cf2d0f91b32e1c91c46de3fd7a6082b6f2228907aceaf65`. The committed runtime lock was not edited. Reproduce the environment with `uv venv --python /opt/homebrew/bin/python3.11 <private-venv-path>` and `uv pip install --python <private-venv-path>/bin/python numpy==2.3.5 scipy==1.17.1`; then verify the exact versions and selected interpreter before any signed launch. The environment is local and mutable until the final custodian freezes and records it.

From `Experiments/neuro_sleep_null_calibration/`, `.../nc0a-pr1114-py311/bin/python -m unittest discover -v` completed **98/98 tests in 73.667 s** on the Mac. Two `ResourceWarning`s came from unclosed `execution.log` reads in the historical `psa_history_inventory.py` tests; no test failed. These are bounded tests, not the formal 16-case battery or a production approval. The V3 signing review must recheck final-HEAD CI and runtime identity after any subsequent code change.

| Source at preparation | SHA-256 |
| --- | --- |
| NC-0a preregistration | `bf497d89e5695498451e49071007aec290d8a899b30b0fd31026f8f3faa55aaa` |
| V3 macOS resource amendment **draft** | `6bd0882bf9a7b4cbc7bca7618606fd0a707f3276b156779eb5db1e19c58f9547` |
| H2 historical runtime audit | `05c1adafe2e685099ea0a7d96e15e28f691a9f4263ef296aa326a174d3b1807f` |
| macOS arm64 runtime lock | `38ce29363945c32d7af318e14ea878e91053a1b68c3c8b64cca4edbddb9d6954` |
| execution engine | `f8e8964b1325daf2117709b1d8bb7ab11edb87693a3553b00dab71469df67683` |
| watchdog | `2edf4f10441f543d7918b46e393423f27ce97e3ccbd816de677e28b7166699c3` |
| authority ledger implementation | `be2b507ade1b577a471f530820b65a6e24c518e4a871d780004f358480a937d1` |

The original PS-A complete, comparable `T_PS-A` remains **unavailable**. H2 recovered partial active intervals but did not approve a complete denominator. The independent resource approver must explicitly decide a **prospective absolute NC-0a budget**: no numeric cap may be inferred from the unavailable `T_PS-A`. The 71.56/76.63-hour historical partial/conditional figures and the engineering probe must not be represented as an accepted baseline. This decision can govern the synthetic NC-0a run only; it does **not** replace the preregistered G0/T1 time-relative gates. Replacing those later requires a separate dated, independently reviewed amendment.

## Candidate decision sheet: NC-0a only

The exact scientific workload is unchanged: 16 fixed synthetic cases, 128 independent fixed-seed chains, 32E attempted swaps per chain, E/2E/4E/8E/32E checkpoints, 16 independent 1,000-proposal BFS oracle traces, 48 paired comparisons and original thresholds. Every screen PASS retains `MIXING-UNRESOLVED`. Failed, partial, budget-stopped and recovered attempts remain in the result and resource history; no outcome-driven reruns.

The V3 **candidate**, requiring an explicit accept/change/reject decision, is: four compute workers; 72 hours cumulative elapsed wall time including sleep; 288 cumulative CPU-hours; 12 hours per case; 30 minutes per oracle stream; 4 GiB sampled process-group RSS ceiling with a 90% early-stop trigger; host free-memory stop below 20%; 2 GiB sampled increase in system swap-used since invocation baseline; at least 40 GiB free on both internal Data and VM mount paths at launch and at least 30 GiB thereafter; and a 4 GiB run-output allocation cap plus a separately signed free-space reserve for the chosen output volume. Wall and CPU costs include failed/recovered invocations. These are loss ceilings, **not** a measured completion upper bound. The approver must choose the final numeric values in a dated resource decision before any policy is signed; no default applies.

The prior engineering-only N=3,900 factor-MST 32E probe used seed root `20261018`, four chains and **3,993,600 proposals**. The first attempt failed (`KeyError`) after 127.598 wall seconds / 474.771 CPU seconds and remains a costed failure. The corrected independent attempt completed in 459.234 wall seconds / 1,813.454 aggregate CPU seconds, with 633,405,440 bytes maximum *sampled* group RSS, at least 34% sampled host free memory, no sampled swap-used growth, and 782,327 bytes of output. Exact endpoint and file hashes are recorded in the V3 draft. One fixture and one successful probe do not cover all families, scheduler tails, interruptions, or a full-battery duration bound. macOS RSS is sampled, not an OS hard aggregate cap; a transient peak can be missed, cause swap or app disruption, or result in an OS kill. The signed approval must acknowledge that residual risk explicitly.

## Host and storage evidence; action required

At `2026-10-18T03:09:52Z`, `/System/Volumes/Data` and `/System/Volumes/VM` each reported 35,578,380 KiB available (33.93 GiB), reflecting shared APFS container capacity. This is about **6.07 GiB below** the V3 candidate 40 GiB launch floor. The Mac reported 44% system-wide free memory, swap total 13,312 MiB / used 12,662.81 MiB / free 649.19 MiB, AC power and no thermal or performance warning. Swap `free` describes the current configured pool, not guaranteed future paging capacity; V3 treats it as telemetry. All values are snapshots and must be remeasured at authorization and immediately before any later launch.

Read-only size survey (rounded): `~/Library/Caches` 16.8 GiB, `~/.cache` 3.4 GiB, `~/Downloads` 14.6 GiB, repository `.local` 35.6 GiB, system `/System/Volumes/VM` about 13.0 GiB. Homebrew cache accounts for about 3.84 GiB, browser cache about 2.72 GiB, `wx-cli` cache about 2.61 GiB, Codex cache about 2.29 GiB, and the uv cache about 0.62 GiB. Caches are candidates for **researcher-reviewed** cleanup only: some may contain valuable offline state. `Downloads` is user data; `.local` contains original research data and audit evidence; VM swap is system managed. No file was deleted, moved, or cleaned in this preparation. The researcher must choose any space reclamation and remeasure the internal floor with safety margin.

`/Volumes/KIOXIA` is currently mounted over USB as ExFAT, volume UUID `0E5DC84B-1E22-3C9B-9E3B-220EBA8607C1`, with 510,938,054,656 bytes (about 475.8 GiB) free. Read-only directory `fsync` succeeded; the same mount/UUID was observed before and after the 98-test run. That does **not** prove multi-day connection stability, file-write durability, atomic rename/link behavior, or crash recovery. The current report writer uses `os.link` for atomic no-overwrite commit (`nc0a_contract_runner.py`, `save_report_once`) and the engine also uses `os.replace` and directory `fsync`; a dedicated disposable write/failure test is still needed before any output-volume choice. ExFAT's `noowners` mount and removable USB connection make it unsuitable as the independently protected authority store. No external-disk test files were created because this task forbids deleting or moving files without the researcher's approval. **KIOXIA is not yet validated or selected as formal output.** A reviewed APFS output volume is the lower-risk path; any ExFAT adaptation requires code/tests and renewed independent review. Recovery must verify the signed volume UUID, mount path, report hashes and all partial attempts before resuming, and stop if the device disappears or remounts under another identity.

## Independent custody blocker in the present ledger design

`AuthorityLedger` opens the ledger with `O_WRONLY|O_APPEND`, locks it with `flock`, appends/fsyncs each record, and uses `os.replace` to update a separately located tip anchor. It verifies sequence/hash continuity and rejects an incomplete tail. These are useful accidental-corruption checks. However, the code checks group/world write bits, **not an independent owner or immutable remote receipt**; the launcher must be able to write the ledger and replace the anchor. An operator with those filesystem rights can rewrite both histories, or initialize a fresh matching pair outside the intended store. Two directories and a hash chain do not provide independent custody. Placing both on a user-writable USB or network share does not fix this. A truly protected anchor that the operator cannot replace would make the present `append()` fail. Therefore the current implementation cannot yet meet the stated off-machine, operator-proof authority requirement.

**Minimum repair before signing:** give a separately administered off-machine custodian the only write/reset authority for the experiment UUID. The launcher may submit begin/finish/audit-digest events through a narrow authenticated append API, but must never receive ledger or tip replacement rights. The custodian serializes concurrent events, stores immutable earlier tips or WORM snapshots, and returns a custodian-signed sequence/tip receipt. The launcher must verify each receipt against an administrator-installed custodian trust anchor before dispatch, after every terminal event, and on recovery. Network/custodian loss or an unpaired start fails closed with unknown cost requiring manual reconciliation. Add real end-to-end tests for concurrent starts, rollback/truncation, lost receipt, crash, and same-UUID cross-directory replay; then obtain independent review of the code and deployment. An equivalently restricted administrator-controlled service is acceptable only if the operator demonstrably cannot rewrite past entries or reset the budget. No such service or production reviewer key has been deployed in this preparation.

## Signer and operator handoff

| Responsible party | Required decision or action; current state |
| --- | --- |
| Codex/engineer | Isolated lock-matching environment and 98 bounded tests completed. Rework independent ledger custody and prove chosen output filesystem semantics before another final code review. Do not start formal NC-0a. |
| Researcher/operator | Select safe internal-space cleanup (without touching research originals), ensure Data/VM meet the approved floor, choose a stable output volume, keep AC and normal pressure/thermal conditions, and accept any personal-host operational risk. No cleanup or output-volume designation was performed here. |
| Independent methods/resource approvers | Decide **approve or reject** the exact V3 amendment and final absolute NC-0a envelope given the unavailable `T_PS-A` denominator; this decision does not authorize G0/T1. Explicitly review the 32E evidence, sampled-memory residual risk, incomplete-run loss, fixed scientific protocol and retry limits. Record identities, dated decision and public review URLs. No decision has been recorded here. |
| Separate administrator/custodian | Control the production reviewer private key, install the public-key fingerprint at the root-owned launcher trust path, deploy the independent off-machine ledger/anchor service and receipts, and issue one formal experiment UUID. No production key, trust anchor, ledger, receipt or UUID was created here. |
| Formal signers, only after all repairs | Freeze final clean Git HEAD, preregistration/V3/lock/code hashes, exact host and output-volume identity, dependency manifest, policy JSON and its SHA-256, final budgets, one run path, recovery rule and allowed attempts. Sign the launcher-defined Ed25519 approval payload; verify the signature and custodian receipt in a nonformal preflight. Test keys and this packet are never formal credentials. |

A future formal gate must reject any missing or inconsistent item, keep the PR Draft, and record `FORMAL NC-0a NOT AUTHORIZED`. Only a separately authorized later phase may run `nc0a_execution_engine.py`'s formal launcher.
