---
id: SRT-NEURO-NC0A-RESOURCE-READINESS-LEDGER-20261012
type: audit
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
tags: [Neuroscience, SyntheticNull, ResourceGate, Provenance, Draft]
---

# NC-0a execution readiness and historical time/identity evidence ledger

**Verdict at this draft checkpoint: NC-0a FORMAL RUN = NO-GO; biological G0/T1 = NO-GO.** This is an evidence-request and reconciliation record, **not** a filled resource benchmark, a formal preregistration freeze, or an experimental result.

## 1. Independent reviewer / source boundary

- Read-only R5 review [#6115880496](https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-6115880496), inspected HEAD `2467d1c5`, concluded **CONDITIONAL GO** for formal NC-0a **after** H1/H2; historical edge-set anchor H3 remains separate and required before NC-0.
- Previous Claude R4 informal four-case test and Codex R5 synthetic counterexample / micro-benchmarks are **known prior exploratory exposure** and must be preserved as such. Never reclassify their data as prespecified independent formal NC-0a evidence.
- The new `nc0a_contract_runner.py` and small-unit-test GitHub workflow are review-only preparation. **No** RIKEN signals, biological Q, formal 16×8×32E chains or full 16,000-oracle battery have been run by this follow-up.

## 2. Fixed formal NC-0a computational inventory (not a timing prediction)

| Item | Prespecified amount |
|---|---:|
| Synthetic cases | 4 families × 4 N = 16 |
| Long chains | 8/case = 128 |
| Checkpoints | E, 2E, 4E, 8E, 32E |
| Long-chain attempted proposals | 44,937,216 |
| Separate local-vs-full BFS oracle proposals | 16,000 |
| Case×metric paired comparisons | 48 |
| Proposal RNG | SHA-256 `NC_SYNTH_V1` namespaces, fixed root 20261009 |

**Important:** the ~1,797,712,000 G0 biological-null proposal estimate and ~9.8M Louvain trials are **different future workloads**. A synthetic checker does not demonstrate they fit available time.

## 3. Historical original PS-A `T_PS-A`: unresolved, never invent

The [private-source local handoff](PSA_RUNTIME_EVIDENCE_HANDOFF.md) and source-hashed offline [active-time auditor](psa_runtime_evidence.py) are now provided, alongside [synthetic-fixture unit tests](test_psa_runtime_evidence.py). These **do not** reconstruct the original intervals without the original private logs or independently verify source activity. A successful program result remains arithmetic-only and requires an independent evidentiary review.

The R5 reviewer reported archival provenance of multiple PS-A launches on 2026-09-24, 09-25, 10-08 and 10-09, with overwritten `environment.txt` and a long logging gap. The archived final run snapshot (~2h) is not the whole experiment; wall calendar time across two weeks includes inactive gaps. **Neither is an acceptable denominator.**

Required evidence for an auditable `T_PS-A`:

1. Identify each archived process invocation, job-range/remaining-work ledger, machine/CPU architecture, worker count, start/resume/stop timestamp, and abnormal termination. Hash original `commands.log`, run logs, scheduler logs, environment snapshots, and job-status/manifests **without altering them**. The evidence files are not fully available to this remote PR audit; enter actual SHA-256 strings only after reading them.
2. For each process, map **active** intervals to verifiable timestamped activity and explicitly classify excluded pauses/sleep/idle periods; publish both raw interval evidence and the reason for each exclusion. Do **not** infer that every gap means sleep, or that every timestamp between first/last run is CPU time.
3. Merge overlaps of **simultaneously running intervals** (union, not naive sum), separately report all work-contributing process-worker hours. Verify coverage of **6,006 unique completed jobs** and whether each resumed process continued unfinished work rather than duplicating completed outputs.
4. Establish the original hardware/OS/Python/dependency/Louvain settings for every contributing interval and compare the proposed synthetic benchmark machine and **at most 8 workers**. Document noncomparable or missing intervals: no silently extrapolated substitute.
5. Only after independent audit, record `T_PS-A` with calculation script SHA-256, the raw source-hash ledger, interval table, excluded gaps, estimated uncertainty, and same-machine comparability verdict. If material evidence is missing, **RESOURCE NO-GO** under the current preregistration. Any replacement budget rule must be prospectively amended and re-reviewed.

| Required ledger value | At present |
|---|---|
| Command/run log hashes and line ranges | **NOT ENTERED** |
| Complete active-interval table | **NOT RECONSTRUCTED** |
| Original worker/hardware comparability | **NOT VERIFIED** |
| Defensible comparable `T_PS-A` | **UNAVAILABLE — NO-GO** |

### Local evidence recovery follow-up — 2026-10-12

The [H2 historical audit](H2_RUNTIME_AUDIT_2026-10-12.md) independently recovered all 6,006 completed-job / 49,049 window metadata matches, historical 4/8-worker evidence, early dependency versions, seven tool duration records, one additional failed launch and system sleep records. The [read-only inventory tool](psa_history_inventory.py) preserves gaps and clock backsteps without inferring activity. Source SHA-256 and exact anchors are in that audit.

**H2 remains NO-GO.** Progress-supported partial intervals total 71.560963 elapsed hours; a mixed-clock conditional estimate is about 76.630770 hours. Neither is an accepted complete comparable `T_PS-A`. Actual aggregate process-tree CPU-hours remain unknown. The earlier unfilled table records the remote checkpoint; the linked local audit supplies recovered evidence without approving a denominator. Its absolute-budget candidate is only a prospective proposal requiring independent review, not a change to §6.1 or execution authority.

## 4. NC-0a independent absolute cap: unresolved before formal execution

The formal synthetic battery needs **separate** precommitted limits even if the G0 denominator is eventually recovered. The proposed [NC-0a resource-policy schema checker](nc0a_budget_preflight.py) has **no implicit defaults, cannot launch the full battery, and always reports only schema validity rather than execution authorization**. Its [tests](test_nc0a_budget_preflight.py) use intentionally fictional numbers and invalid approval links solely as fail-closed unit fixtures; do **not** treat those fields as a suggested budget.

The separately approved policy must specify:

- Host identity and dependency lock; explicit maximum wall clock time for **the entire 16-case battery**, total CPU-hour limit and maximum concurrent workers;
- Process/aggregate RAM ceiling and peak measurement method; baseline disk free-space bytes plus maximum temp/output allocation, output serialization policy and how failure/partial files count;
- Per-case cap and aggregate *remaining* resource ledger, mechanism for fail-closed cancellation on overrun and verifiable machine clock records;
- Immutable 16 fixture fingerprints, 128 long-chain seeds and 16 BFS oracle seeds *before chain execution*; no outcome-dependent replacements or extra draws;
- Case order/concurrency plan, atomic success artifact and immutable SHA-256, clear `interrupted` / `failed` status. A crash may be re-executed **from the original seed and step zero only under a documented recovery decision**, never using a new seed or silently filling in missing favorable cases;
- If the cap is exceeded, final formal result must be **NC-0a NO-GO**, not “pass on finished cases”; any budget amendment requires prospective review before further trials.

**Values have not been supplied/locked for this machine, and no reviewed `T_PS-A` is available; do not launch the formal battery.** The bounded contract unit tests are separate, explicitly labeled and do not consume formal-case data.

## 5. NC-0 historical graph-identity H3: separate gate

- R5 verified all six MAT SHA-256 and original runner script hashes against results, 6,006 job/subset integrity and 49,049 window Q records; **these verification claims originate in R5**, not a second re-execution here.
- No archived original historical edge-set or fingerprint was identified. A new graph fingerprint is **not** historical proof.
- Before biological G0: use the **original verified** SciPy-based MST / top-edge builder, archived realized neuron indices, preprocessing, exact seed/edge insertion semantics and original environment to reconstruct a declared reference graph. Independently reconstruct the candidate runner's initial graph and compare **labeled edge sets** for the prespecified **120** graph panel. Verify recorded Q max and *all 200 historical trial Q values where available* within a separately locked tolerance, keep the full reference lineage, and refuse silent repairs or cherry-picked cells.
- This is a **faithful reconstruction identity anchor**, not a comparison against an archived historical edge-list artifact. If reference semantics cannot be reproduced, **NC-0 = NO-GO**; do not rewrite archived PS-A results.

## 6. Gate interpretation

- A valid 48-comparison drift **PASS** remains `MIXING-UNRESOLVED`. The exact R5 three-state slow-chain counterexample shows non-rejection can coexist with poor equilibrium sampling and near-zero acceptance.
- New code must report acceptance/rejection rates, all per-accepted local topology checks, checkpoint full graph connectivity and three metrics, complete 16×1,000 BFS oracle traces and no dropped cells.
- Under original preregistration, **G0-only GO and T1-NOT-AUTHORIZED-RESOURCE** may be locked before any biological null outcomes; T1 cannot be turned on after inspecting G0. T1's circular-shift relative-phase limitation in R5 M4 remains open before authorizing T1.

**Next admissible operation:** independent review of H1 code, contract tests and the historical-time/absolute-budget evidence. **Not** a formal NC-0a run, biological null or NC-0 freeze.
