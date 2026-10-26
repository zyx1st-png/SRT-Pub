---
id: SRT-OBSERVED-CALIBRATION-RESOURCE-REQUEST-20261026
type: experiment-proposal
status: active
record_stage: researcher-resource-approved-awaiting-single-run-authorization
date: 2026-10-26
effective_date: 2026-10-26
independent_ai_review_record: https://github.com/zyx1st-png/SRT-Pub/pull/1132#issuecomment-6409902896
researcher_resource_decision: https://github.com/zyx1st-png/SRT-Pub/pull/1132#issuecomment-6409967378
layer: operations
epistemic_layer: experimental
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/neuro_sleep_null_calibration/H3_120_SCIENTIFIC_CLOSURE_2026-10-26.md
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_FIXED_SAMPLE_V1_2026-10-26.json
  - Experiments/neuro_sleep_null_calibration/G0_CANONICAL_Q_ORDER_PROSPECTIVE_AMENDMENT_DRAFT_2026-10-23.md
tags: [RIKEN, ObservedBaseline, ResourceCalibration, ResourceApproved]
---

# Observed-only resource calibration request

**RESEARCHER-APPROVED RESOURCE ENVELOPE ONLY (2026-10-26) / NO REAL CALIBRATION HAS RUN / NO RUN AUTHORIZATION.** The researcher separately accepted the limited [Claude Opus 5.5 AI technical/resource review (owner-relayed, not independent human/GitHub signature)](https://github.com/zyx1st-png/SRT-Pub/pull/1132#issuecomment-6409902896) and approved the [fixed 47-graph, 4h/4-CPUh stop-loss request and disclosed risks](https://github.com/zyx1st-png/SRT-Pub/pull/1132#issuecomment-6409967378). This is a **new prospective observed-only decision**, not an automatic extension of the #1131 H3-specific review route. The status `active` means **this exact resource proposal is approved on the currently unmerged #1132 branch**; it does **not** activate a run, create an authorization credential, or modify frozen science. Before biological signal processing, a clean final execution HEAD, new UUID/private internal-APFS output path, fresh live Mac/source/host checks and a **separate personally entered UUID-bound researcher confirmation** are mandatory. This request does not approve a full 4,900-graph baseline, biological 4E nulls, G0, T1 or a representative G0 benchmark. G0/T1 remain **RESOURCE NO-GO**.

Dependencies checked on 2026-10-26: #1124 `ff85deec88ff700affeb489c95d0ea6c6295eb4b` (resource discussion Draft); #1128 `577cfde1000090c1325419417aa5b2c83325a3a2`; #1131 `a56ef684caf03b7748c8c9d713e44db75d17a43d` (method activation on that unmerged branch); #1130 executed `147d5ca268ef0c579c41f314a6f5e5ec8cafc6d2`. This PR is stacked on #1130; inherited original records and scientific protocol are unchanged. The engineering supplies the existing task's bounded follow-up, not another programme owner or STATUS next route.

## Frozen initial sample and reserve

The deterministic generator is `observed_calibration_sample.py`; its generated manifest SHA-256 is **`f29acb99a05387b128f724bf818e3f402f7ced8a4080c12da4a936b9284d95c4`**. Inventory SHA-256 is `6a8357ac0b815c434421a31dc6c294c292b5c144713f49c52b5344038235ece2`; method SHA-256 is `c0cf7f85a18bad844e190deefbe83e8ab55f0dbe194299be0ef94e2c828e38c3`. Validation rebuilds the manifest from its fixed public identities and requires exact content, order and byte-hash identity.

The 4,900 rows contain 49 distinct source-frame windows, each used by 100 graph tasks (ten selected subsets at each N). H3 covers 40 windows. For each of the nine uncovered windows, choose one graph at each N=100,765,3900: 27 graphs. Add one Wake and one NREM graph at every N: 20 graphs. The supplement source index is `(N_index + 3*state_index) mod 6` in the frozen six-recording order. Rank candidates by SHA-256 of the selector version, selection purpose and graph ID; break ties by graph ID. Exclude all 120 H3 graph IDs and already selected graphs. No Q value, optimizer result, graph feature or runtime enters ranking.

**47 graphs / 9,400 new canonical Louvain trials**, no historical replay and no swaps. N=100,765,3900 each contribute 11 graphs; the seven other N values each contribute two. Source counts: mouse01 7, mouse02 9, mouse03 3, mouse04-day1 10, mouse04-day2 9, mouse05 9. State counts: 22 Wake / 25 NREM; 23 unique source windows. Fixed execution order groups source recording/state/window, then ascending N and graph ID to expose raw-window cache reuse without changing per-graph identities/seeds. The existing H3 canonical results are not recalculated or credited as newly timed work; H3 supplies historical cost evidence only.

This is a deliberately structured initial measurement sample, **not a probability sample or sufficient full-population U95 calibration**. N=100/765/3900 and uncovered windows are oversampled. The manifest also freezes a 40-row optional reserve, four non-H3/non-primary rows per N selected by a separate identity-only hash: two training and two sealed validation rows per N. No reserve row is executable by this launcher. Activation requires a separately reviewed amendment/authorization for the entire 40, not a result-selected subset. Training-only triggers are missing cost support, >25% held-row underprediction or U95/median >1.5; an instrumentation/integrity failure stops and requires correction review, never substitution by reserve rows. Freeze the training resource model/code/hash before exposing sealed validation costs; no refit after opening. Q values never enter cost-based expansion. Neither batch automatically grants baseline/G0 GO.

## Researcher-approved finite loss limits (2026-10-26; single-run authorization still pending)

| Item | Approved stop ceiling / condition |
|---|---|
| Total wall | 4 hours; measured identity preflight is subtracted from supervised remaining allocation |
| Total accounted CPU | 4 process-tree/controller CPU-hours; measured preflight process CPU is subtracted |
| Compute parallelism | 1 worker, the supervised serial scientific child; shared host activity lock |
| RSS | 4 GiB aggregate sampled RSS; **not an OS hard memory limit** |
| Raw-window cache | One immutable window, retained array ≤256 MiB; evict before loading another; temporary HDF5/NumPy allocations are additional RSS |
| Run output | 1 GiB total, including logs/results/metadata; each result additionally ≤32 MiB before writing |
| Output | New UUID directory on internal APFS, inside the fixed private observed-calibration parent |
| Internal Data / VM | Each ≥40 GiB available at launch; nominal ≥30 GiB retained; preserve inherited 5% / 64-MiB anticipatory reserve margins; readings are not additive |
| Host memory / Swap | Stop below 20% free-memory telemetry or >2 GiB growth in used Swap; record used/current-pool total/free separately |
| Power / temperature / sleep | AC required; normal thermal state required; live caffeinate assertion required; unavailable telemetry or material sleep/clock anomaly stops |

H3 measured 6,269 s wall / 6,480 s accounted CPU for 120 reconstructions plus 48,000 Q trials. Weighting its per-N median dual-order row times by this initial sample's N counts gives about 50 minutes; using the per-N largest of twelve measured row times gives about 67 minutes. Those use the whole 400-Q row cost for a 200-Q activity, but are still **sensitivity calculations**, not completion bounds: windows/subsets, separate counters, durable phase logging and cache patterns differ. Four hours allows about 3.6× the latter wall scenario as a finite-loss allowance; the owner-relayed independent AI review recommended APPROVE and the researcher approved that loss envelope. This is **not a validated safety factor or completion guarantee**. Source identity hashing and HDF5/metrology overhead are separately recorded and consume allocation. The serial budget does not assume fourfold speedup. Raw `T_PS-A` is still unresolved; this prospective request does not resolve the G0/T1 historical resource gate.

## Measured computation and integrity

The shared `canonical_louvain_q_vector` runs exactly the original 200 observed seed values in their recorded order with `CANONICAL_SORTED_EDGE_V1`, unit weights, python-louvain 0.16, resolution 1.0, Qmax and first maximum. Full seed/Q/partition-hash vectors and finite-heuristic prefix diagnostics are saved privately. No signal preprocessing, neuron selection, correlation rule, graph rule, seed, statistic or threshold changes.

Per row measure wall, self CPU, native OS-attributed read/write bytes, block-I/O operation counters, RSS endpoints and lifetime process `ru_maxrss` for: private job/subset/seed identity, HDF5/window read, correlation + zero-variance diagnosis, inclusive historical graph construction, MST within that builder, independent graph identity/canonical representation, shared 200-Q path, serialization, file fsync and audit append. **MST and edge-selection residual are components of inclusive builder time, not extra additive stages.** The edge-selection residual is inclusive builder minus MST; it includes ranking/top-up/insertion and wrapper overhead. The shared 200-Q helper also constructs its canonical representation; that small cost is included and labeled. Use complete recorder-on end-to-end CPU/wall for prediction; do not blindly sum nested phases. Phase-log fsync totals are measured; terminal/control and metrology overhead remain in end-to-end residuals.

On macOS, `proc_pid_rusage(RUSAGE_INFO_V2)` supplies process-attributed disk bytes. Logical HDF5 array bytes are separate. OS caching and compression mean neither measures physical SSD throughput. `ru_inblock/oublock` are operation counts, never relabeled bytes. The existing Watchdog records tree RSS, system pressure/Swap/disk/power/thermal and current graph ID; recovery verification joins RSS samples by task ID. Zero samples for a short row means unknown peak, not zero memory. `ru_maxrss` is lifetime self-process high water, not a row/tree peak.

One compute worker means one scientific process, not a promise of one native BLAS thread. Record and bind the existing OMP/OpenBLAS/MKL/Accelerate/NumExpr thread environment without changing reduction semantics; native-library CPU is included in process-tree accounting. The OS file cache is not flushed or controlled: full source hashing before signal reads can warm it. Report observed native/logical I/O and cache hits, never label this a cold-SSD throughput test. A full-baseline forecast must match these setup/cache semantics or explicitly add the missing cost.

Raw caching requires the same MAT SHA, absolute nonredirected file identity, state, window index and exact frame-vector hash. On a hit, recheck device/inode/size/mtime/ctime. Cached arrays are read-only; selected-neuron extraction creates a fresh subset; no correlation, graph, partition or Q cache exists. Every source is SHA-256 checked before signal access. Production preflight checks all selected jobs and the complete seed-ledger file hash, and compares selected seed rows to the inherited recipe. Child admission rechecks authorization, HEAD, sample, sources and runtime under the Watchdog before reconstruction.

Zero-variance diagnostics preserve the historical `corrcoef → nan_to_num(0)` rule and never drop a neuron. Save raw nonfinite counts, exact constant IDs, zero-variance IDs and generated-nonfinite correlation counts privately. Aggregate affected graphs, unique source-window identities and unique original-neuron/window combinations without double-counting cache hits or shared subsets.

## Failure, audit and next decision

One fixed sample has at most one recorded attempt in the existing host activity ledger, irrespective of output directory. No automatic retry/resume is provided, including operational failures. Scientific identity/Q failures, resource stops, I/O faults and unknown exceptions retain the ordered completed prefix and failure record. Phase meters are persisted before the next phase, including aborted meters. Incomplete or damaged artifacts never count as success. Recovery is audit-only: verify every log chain, terminal/summary/host anchor, output hash, graph/seed/Q identity, phase record and exact ordered task list; refuse suffix truncation, unknown artifacts and overwrite. Inherited `h3-*` private transport filenames are explicitly reused, with observed-calibration event/result schemas.

Researcher approval is an explicit local accountable record, not third-party cryptographic authorization or external human peer review. Local hash chains and GitHub snapshots are verifiable copies, not immutable custody. The H3 legacy environment gaps and macOS transient-memory/OS-disruption risks remain disclosed.

The exact sample, cache/phase semantics, and finite loss envelope have received owner-relayed independent AI technical review and **separate explicit researcher resource approval** on 2026-10-26, as linked above. The AI review was not independently authenticated as human peer review; its private-hash and native-host-verification limitations remain disclosed. **The next step is preparation only:** freeze/recheck the final clean execution HEAD (which may change after this documentation-only approval record), generate a fresh UUID/unique private output directory, and produce a **PENDING** run-bound authorization draft only after a fresh current Mac/source/host preflight. Present the exact UUID/HEAD/sample/method/runtime/budget package and all live resource readings to the researcher, then **wait for the researcher's separate, personally entered exact confirmation line** before any approval JSON is marked `APPROVED_FOR_SINGLE_RUN` or any real task starts. No UUID, approved authorization package or biological calculation was created by this documentation-only approval update. Any host-induced early stop, even without a scientific error, exhausts the current fixed sample's single attempt: no automatic restart, replacement, UUID rotation or budget extension. Any prospective exception needs a wholly new scoped review and researcher decision, preserving original failure evidence. Full 4,900 baseline approval requires an independently reviewed model that separates reconstruction/Q/I/O, treats repeated source windows as clusters, covers unsupported tails and distinguishes model-conditional prediction limits from confidence bounds on a mean. G0's 49,000 nulls, 9.8 million null Q trials, 1,797,712,000 proposals and independent T1 admission remain separate.
