---
id: SRT-NEURO-G0-RIKEN-SOURCE-IDENTITY-H3-READINESS-20261021
type: audit
status: draft
updated: 2026-10-23
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
  - Experiments/neuro_sleep_null_calibration/G0_T1_PROSPECTIVE_RESOURCE_BUDGET_AMENDMENT_DRAFT_2026-10-20.md
tags: [Neuroscience, G0, RIKEN, Identity, H3, Evidence]
---

# G0 RIKEN Source Identity and H3 Readiness

This record accompanies the public-safe inventory generated from the preserved
local PS-A artifacts. It does not change the preregistered graph rule, produce
any biological null graph or Q value, or authorize resource benchmarking.
Formal G0/T1 status remains **RESOURCE NO-GO**.

## Current status and prospective Q-order decision (2026-10-23)

This section updates the preparation-era execution status below. It does not
change the frozen graph/null/statistical protocol, authorize another biological
run, or make the resource amendment effective.

### Completed H3 pilot: 10 of the fixed 120 graphs

The fixed pilot completed under the report at
[PR #1127 comment #6358214859](https://github.com/zyx1st-png/SRT-Pub/pull/1127#issuecomment-6358214859): run UUID
`7f69d7bf-6454-4d78-8e72-43af5b8d63a7`, execution HEAD
`7be6d57cb4e55d0abfeb4b4491fe402b8c51beeb`, pilot SHA-256
`286fa084f125d205463218951e3ccf2640701dc7712a9a48cec62b323a49c36b`, and
identity-manifest SHA-256
`6a8357ac0b815c434421a31dc6c294c292b5c144713f49c52b5344038235ece2`.
All 10 fixed graphs passed source/edge identity and authoritative historical-
order replay: 2,000/2,000 trial Q values matched exactly, Qmax and first-max
index matched for all ten. The #1126 sorted-edge insertion diagnostic was
incompatible on all ten: 1,812/2,000 trial values exceeded the `1e-10`
absolute comparison, maximum per-graph absolute difference `0.02179`, Qmax
outside `1e-6` on 9/10, and first-max index differed on 9/10. This is a
representation-sensitive Louvain result, not a graph-identity failure.

The 10 completed IDs are members of both the fixed 120-graph H3 panel and the
4,900-row expected G0 source inventory. They are all `mouse01_sleep`, Wake,
one graph at each registered N. Thus 10/120 H3 graph reconstructions and
10/4,900 G0 edge sets are verified; the other 110 H3 panel edge sets and the
other 4,890 G0 edge sets remain un-reconstructed. The 4,900-row expected
source identity mapping itself remains verified; that mapping is not evidence
that the corresponding edge sets were built. The completed panel has not yet
covered the other five recorded sources, NREM, or the within-N repeat/window
variation. The full 120 replay has not run. The independent incremental audit
verified artifacts and identity/hash evidence but did not independently rerun
Louvain.

The run used 573.25 seconds wall, 606.34 process-tree CPU seconds, 1.832 GB
maximum sampled aggregate RSS, and 1.244 MB output; the runner executed one
compute worker. RSS is sampled monitoring, not a hard memory limit. These
measurements describe this fixed 10-graph pilot only.

### Prospective common observed/null Q policy — researcher decision pending

The comparison needs one graph-order policy because `python-louvain 0.16`
uses adjacency iteration order in seeded community moves and tie resolution.
Identical labeled topology and seed do not guarantee identical finite-run Q
when neighbor insertion order differs. The 10-graph result directly confirms
that the historical and #1126 sorted-edge paths do not produce the same
finite-200 Q statistic.

**Recommended candidate: one canonical representation for observed and null
graphs.** Add nodes in ascending saved original-neuron index; add each
undirected edge once as `(min(u,v), max(u,v))`, in lexicographic pair order,
with weight `1.0`. Apply this same builder to each reconstructed observation
and each final 4E null graph. Use the existing, hash-bound ordered 200-seed
vector for each observed source graph and the already fixed per-null seed
vector for each null task; do not regenerate or reorder seeds. For each seed,
call `best_partition(weight="weight", resolution=1.0, random_state=seed)` and
evaluate modularity on that same graph. The primary graph statistic remains
`Qmax_200 = max(Q[0:200])`; ties retain the first maximizing trial index.
Record all 200 trial Q values, seed-vector hash, topology hash, ordered
representation hash, environment, and first-max index. A candidate policy
identifier is `CANONICAL_SORTED_EDGE_V1`.

This gives observed and null graphs the same deterministic mapping from
labeled topology to Louvain input. It does **not** make Louvain an exact
optimizer, remove stochastic heuristic error, establish order invariance, or
prove that 200 trials find a global maximum. Retain the 200-trial maximum as
the primary statistic. As descriptive diagnostics, report Q maxima at the
fixed seed prefixes 50/100/150/200 and the number of distinct returned
partitions; these diagnostics do not change the 200-trial endpoint, create a
new pass threshold, or authorize extra result-dependent trials.

The alternative is to retain historical insertion order and define a
source-derived null order (for example, source edges that remain in the final
graph in their original historical order, followed by non-source edges in
lexicographic order). This could preserve the published historical Q baseline
and be deterministic if edge provenance is retained, but it leaves null Q
dependent on which source edges survive and gives the observed and null
topologies different adjacency sequences. Carrying each accepted swap's
insertion order instead would also make Q depend on the random proposal path.
Neither rule is currently implemented or validated. I do not recommend it as
the primary comparison because it retains an avoidable representation effect.

Adopting the canonical candidate is a **prospective method amendment**, not a
mechanical fix. Historical PS-A Q vectors remain immutable provenance, while
the primary observed baseline would need canonical recomputation for all
4,900 source graphs: 980,000 Louvain trials. The observed slopes, paired
`D_excess`, and downstream NC-A/NC-B/NC-C classifications can change because
the finite-heuristic Q values change. Graph construction, 4E kernel, fixed
seeds, 200-trial maximum, aggregation, inferential thresholds, and failure
rules remain unchanged; the amended protocol must explicitly distinguish
legacy historical replay from the new primary canonical Q baseline before any
biological null Q is inspected. No amendment is approved by this document.

### Fixed 120-graph H3 completion plan and candidate limits

Keep the exact Q-independent 120 IDs already frozen in the manifest: 6
recorded sources (5 animals, with mouse04 day1/day2 separately represented),
two states, ten N values, one fixed graph per source × state × N. This covers
60 Wake and 60 NREM graphs, with 12 per N. Do not reselect rows. Run the two
representations in fixed order and report source identity, historical-order
Q replay, and canonical-order Q comparison separately. A canonical-order
mismatch against historical Q is a compatibility result, not a reason to
invalidate an otherwise passing source identity or historical replay.

The current launcher is hard-wired to ten IDs and 4,000 Q trials; it is not a
120-graph production entry point. Before a separately authorized H3 run, the
minimum scoped preparation is a new hash-bound 120-row packet/schema, runner
support for exactly those 120 IDs and 48,000 graph-order/seed evaluations,
and private persistence of complete canonical Q vectors so verified results
can be reused by the 4,900-graph baseline. Use a new UUID and audit directory;
retain the completed 10-graph run as immutable history. Re-run live source,
environment, disk, memory-pressure, power, thermal, Watchdog, lock and output
preflight before execution.

Candidate stop ceilings for researcher review are **8 wall-hours, 8
process-tree CPU-hours, one compute worker, 4 GiB sampled aggregate RSS, and
1 GiB output**. The 10-graph run gives a naive ×12 reference of about 1.91
wall-hours and 2.02 CPU-hours, so the candidates are about four times those
linear estimates. This is not a U95 bound: all ten pilot rows were from one
recording and Wake, while the full panel includes other sources and NREM.
Observed output scaled linearly would be about 15 MB, also not a validated
output bound. The 4 GiB RSS ceiling is about 2.2 times the largest sampled
pilot value, not a hard limit. Retain the existing independent Data/VM free
space checks (40 GiB at start, 30 GiB reserve while running), free-memory
floor (at least 20% available memory), Swap-growth stop (>2 GiB increase), AC
power, normal thermal state, sleep-prevention and fail-stop Watchdog
conditions. These are candidate loss limits, not an authorization or a
completion guarantee; stop on the first identity, historical-Q, audit or
resource failure, with no sample replacement or outcome-directed retry.

### Canonical baseline and G0/T1 boundary

Only after the Q policy is prospectively approved, rebuild and hash-bind all
4,900 observed graphs and compute the canonical 200-seed Q vector for each.
The fixed 120 H3 canonical vectors may count toward this total only if their
source, edge-set, order-policy, seed-vector and environment hashes match the
baseline manifest exactly. The current 10-graph artifact contains comparisons,
not a reusable complete canonical Q-vector cache. Then complete the other
4,780 rows (956,000 trials); the aggregate remains 980,000 observed trials.
Keep raw signals private. Cache only validated graph/result artifacts under
keys that bind MAT hash, selected-neuron/frame hashes, graph-builder version,
edge-set/order hashes, seed-vector hash, and environment lock. Do not overwrite
historical PS-A jobs or H3 audit files.

Each of the 4,900 graph reconstructions requires source-window loading,
correlation construction, MST, and strongest-edge selection. At N=3,900 one
dense float64 correlation matrix alone is 116.1 MiB; correlation, absolute-
value, distance and MST temporaries can coexist, so this is not a peak-RAM
estimate. The 980,000 Louvain trials and graph rebuilds must be separately
timed on preapproved representative strata before a total budget can be
proposed. Do not scale the H3 pilot into a completion bound. Add the full
observed-baseline cost to PR #1124's resource model; G0's 9.8 million null
Louvain trials remain a separate additional workload. Neither this plan nor
the H3 result changes **G0/T1 RESOURCE NO-GO**.

## Evidence checked

The inventory generator verified the six source MAT files against the hashes
in `SRT_NEURO_POPULATION_SIZE_SCALING_RESULT_2026-10-09.json`, and checked the
two preserved runtime source files against the same result's code hashes. It
also cross-checked all 6,006 completed PS-A job records against 6,006 public
summary rows, the selected neuron-index vectors and hashes, the 49,049-row
Louvain seed ledger (49,000 finite-N plus 49 FULL window records), and the
saved 200-value Q vectors for every ledger window. Each ledger key and seed
vector was checked against its historical job and Q reference. The generator
read source-file bytes for SHA-256, HDF5 shapes and
`frame/used_frame` index arrays. It did not read `spike_smoothed` signal values,
construct a biological correlation matrix or graph, or run Louvain.

The generated manifest is
`G0_RIKEN_SOURCE_GRAPH_EXPECTED_MANIFEST_2026-10-21.json`, 9,379,060 bytes,
SHA-256 `6a8357ac0b815c434421a31dc6c294c292b5c144713f49c52b5344038235ece2`.
It includes the identity-tool hash and verification package/runtime versions.
It contains source and job hashes, graph coordinates and Q/seed hashes, but
not raw signals, saved Q values, private absolute paths or local job files.
An output scan found no absolute local paths or `.local` path fragments.

The historical code hashes are `multirecording_primary.py`
`2421e4e21655199378aad81242aa1d0a5a02ba94a39c5cb83e0942689faa55f5` and
`population_size_scaling.py`
`0e7af206456348b9eb91d5771d7cd4d18fe312ea4508b71a5772d7a47370b625`.

| Recording ID | Animal | Session label in recorded ID | Source MAT SHA-256 |
|---|---|---|---|
| `mouse01_sleep` | mouse01 | not separately encoded | `a73526ff842633816a7d03f2578eaeb398fd928c9c2b4a62a2496273dc3c59e6` |
| `mouse02_sleep` | mouse02 | not separately encoded | `e7f283390791c5fbeade9dc2f579d9e89c772a46afcb7f36636d8d081bf99934` |
| `mouse03_sleep` | mouse03 | not separately encoded | `dcac3d396edcb188e88a7e1ff91efe335c904e9defdf2d26c11c36281bcb4277` |
| `mouse04_day1_sleep` | mouse04 | day1 | `3d78be67a6a192c511a41520062f6621b898661d2a2bc127e3f13012fb24ace3` |
| `mouse04_day2_sleep` | mouse04 | day2 | `84c843c06006a283a9df7fc3e081c550500e52909bafc96533b91861130f02c7` |
| `mouse05_sleep` | mouse05 | not separately encoded | `973c27b3e27451d153c108b1ad38e447b749622ac58de2c6c0c0c01ccb380181` |

“Not separately encoded” is deliberate: for those four recordings, the
preserved inventory gives a recording and animal ID but no separate session
identifier. No session value has been inferred. The state tokens are exactly
`wake` and `NREM` as serialized in the historical jobs. Window IDs are the
zero-based, consecutive 1,500-frame windows within each state's saved source
frame vector.

The verified expected G0 inventory has **4,900 source-graph identities**,
**490 per registered N** (`100, 150, 225, 340, 510, 765, 1150, 1725, 2600,
3900`). Each identity binds recording/animal/session evidence, N, selected
repeat, state, window ID, source MAT hash, selected-neuron-index hash and
source-frame-index hash. The selected neuron IDs are the saved zero-based
indices in ascending order. The inventory also binds the existing Q-vector,
200-seed and job-file hashes for each selected source window. This validates
the *expected input identity mapping*; it does **not** establish any of the
4,900 edge sets. The manifest correctly leaves each edge-set hash null and
marks edge identity as pending reconstruction.

The fixed H3 panel contains **120 IDs**, one for each recording × finite N ×
state. It applies the preregistered hash selection across the ten already
selected subset repeats and the available windows, without consulting Q
values. Existing private job files contain the corresponding historical
200-element Q vectors and first-maximum index; their hashes and seed mappings
were verified. The maximizing partitions and original edge lists were not
archived, so partition comparison and a direct comparison to saved historical
edge fingerprints are unavailable.

The realized PS-A subset selection used the saved string target labels (`N100`,
etc.) when deriving subset seeds; the preregistered numeric-target recipe
differs. This deviation is already disclosed in the PS-A result. The manifest
preserves the realized indices and seed identities; it does not regenerate or
replace them.

## Reconstructed graph rule and implementation check

The historical source and the identity tool agree on the following rule:

1. Read the selected `spike_smoothed` rows for the saved S3/C1 source window;
   if HDF5 requires sorted frame access, restore the original frame order after
   reading. Select saved neuron indices in their archived ascending order.
2. Compute row-wise `numpy.corrcoef`; map non-finite values to zero, zero the
   diagonal, then take absolute correlations.
3. Build a SciPy minimum spanning tree on `1 - abs(correlation)` with infinite
   diagonal. Normalize and sort the undirected MST pairs.
4. Add the strongest non-MST edges to `round(N × 16 / 2)`. The historical
   `np.partition` threshold is retained; strict-above-threshold indices are
   emitted in upper-triangle row-major order, followed by the required
   boundary-tie indices in that same order. Edges are unweighted with weight
   1.0. The target is 8N edges for these registered N values.

The tool hash-checks the historical builder source before extracting only its
`upper_flat_index` and `connected_graph` function definitions, avoiding module
import side effects. A small synthetic tie-heavy N=20 fixture confirmed exact
edge-set and adjacency-iteration agreement between that historical function
and the independently written faithful builder. The specific test fixture is
not a RIKEN input and does not stand in for any real source graph.
The hash of those exact extracted historical functions is
`59ed4ea1537d3b104e8ff9903ce98c51f69bb58edc09854933886f637ad90866`.

The preparation-time reconstruction path separates three questions: (1)
whether source input and reconstructed historical graph match the identity
record, (2) whether a 200-seed replay on historical adjacency order reproduces
the archived Q vector, and (3) whether PR #1126's sorted-edge insertion order
is compatible. The third result is diagnostic: an executor-order mismatch
cannot invalidate a source graph or a passing historical-order replay. Under
the original PS-A protocol, historical insertion order is authoritative for
reproducing legacy observed Q. The prospective primary order for future G0
comparisons is a separate, unresolved researcher decision documented above.

The frozen historical insertion sequence is: add nodes `0..N-1`; add the
`N-1` minimum-spanning-tree edges sorted by normalized endpoint pair; add all
strict-above-threshold edges in `np.flatnonzero` upper-triangle row-major
order; then add only the required threshold ties in that same row-major order.
The PS-A wrapper imported this exact `connected_graph` function from the
hash-pinned `multirecording_primary.py`. NetworkX preserves the resulting
per-node neighbor insertion order, which can affect seeded Louvain tie
handling even when labeled edge sets are equal. The independent builder is
checked against the exact AST-extracted historical function and against
source-node and frame-index hashes.

The PS-A worker computes each saved trial with
`community_louvain.best_partition(graph, weight="weight", resolution=1.0,
random_state=seed)`, then evaluates
`community_louvain.modularity(partition, graph, weight="weight")`. The saved
seed recipe is `stable_seed(12345, recording_id, "sleep", "S3", "C1",
analysis_label, state_index*1000 + window_index, repeat_index)`. The runtime
used a `fork` process pool, `chunksize=1`, and checkpointed every ten Q values;
the environment record lists eight workers and 200 repeats. H3 replay reuses
the saved seed vector in order and performs no edge swaps. Worker count affects
the schedule, while each trial's graph, seed, Louvain call and Q definition
remain the comparison target.

The H3 pilot applied absolute trial-Q tolerance `1e-10`, relative tolerance
zero; Qmax tolerance `1e-6`; and exact first-maximum-index agreement. The
validator compares each finite trial using `abs(actual - reference) > 1e-10`;
equality at the threshold passes. Its Qmax comparison is independently
`abs(max(actual) - reference_max) > 1e-6`, plus exact equality of the first
maximizing index. The supervised synthetic regression checks the exact
`1e-10` boundary and the next value above it. These limits remain fixed for
the H3 historical-Q integrity check and are not a post-hoc acceptance
threshold for declaring the canonical-order Q vector equal to the historical
one. A canonical-vs-historical difference is reported as representation
compatibility, without loosening these checks. The historical run record
captures Python 3.14.0, macOS 15.7.4 arm64, NumPy 2.5.3, NetworkX 3.6.1 and
python-louvain 0.16, but does not record the SciPy version used by the
historical MST or h5py/HDF5 versions. The replay environment therefore uses a
candidate lock (including SciPy 1.18.1 and h5py 3.16.0) that matches the
recorded versions where known; it cannot prove exact historical floating-point
equivalence. No tolerance may be changed after seeing pilot Q differences. A
failure at `1e-10` remains a failure unless a prospective amendment is
reviewed before the affected replay.

The saved job loader verifies each selected source MAT hash, job-file hash,
coordinate, 200-seed vector hash, archived ordered Q-vector hash, Qmax and
first-max index. It does not copy signal values or the Q vector into the
public preparation packet. The validator requires all 200 seeds and finite Q
values and independently reports the three outcomes above.

## Synthetic Louvain-order difference

The PR #1126 executor normalizes the graph by sorting its edge list, then adds
those edges to NetworkX in sorted order before seeded Louvain. The historical
builder adds sorted MST edges first, then strict-above-threshold edges, then
boundary ties. These can produce identical labeled edge sets but different
neighbor iteration orders.

A synthetic-only test used a fixed NumPy generator seed `20261021` to create a
1,500 × 20 normal matrix, took absolute Pearson correlations rounded to 0.01
to exercise threshold ties, and built an N=20, E=160 graph. The historical
builder and faithful identity implementation had identical edge-set hash
`74681ec089e3eeacdb88e3796f8645e197620c49c539eb23c391868ec473b4db` and
identical adjacency order. Rebuilding the same edges in the executor's sorted
order changed the adjacency-order hash. Under python-louvain 0.16, the same
200 deterministic synthetic seeds then produced **18/200 unequal trial Q
values**; maximum Q matched, but the first-max index changed, and maximum
absolute trial-Q difference was `0.019921875000000117`. This is not a
biological finding. It demonstrates that edge-set equality alone does not
establish replay equivalence for the current Louvain call path.

At the time this preparation snapshot was written, no biological correlation
matrix or Louvain replay had run and real H3 compatibility was unresolved.
That historical status is superseded by the completed 10-graph result in the
current-status section above. The observed sorted-order mismatch remains a
compatibility finding, not a source-identity failure. Do not run biological
G0 null tasks until the identity and Q-order policy are resolved prospectively
before any null outcome is inspected.

The original PS-A runner used NetworkX `fork` multiprocessing; the current G0
path uses `spawn` and a fresh ProcessPool per task. The Q/seed algorithm is the
same `python-louvain 0.16` `best_partition(weight="weight", resolution=1.0,
random_state=seed)` followed by `modularity`, but historical execution
environments are not captured as one immutable lock across every run. The
identity scan itself ran in Python 3.14.0, macOS arm64, macOS 15.7.4, with
NumPy 2.5.3, SciPy 1.18.1, h5py 3.16.0, NetworkX 3.6.1 and python-louvain
0.16. The preregistered historical runtime requirements are therefore
available for the replay, but replaying in the matching current environment
cannot retroactively prove every historical process used identical binaries.

## Cost and storage consistency with PRs #1124 and #1126

The current activity runner is serial across null tasks. Each task creates a
supervised runner and a new `ProcessPoolExecutor` with up to four compute
workers for its 200 Louvain trials. At 49,000 tasks, this implies 49,000
task-level invocations and up to 196,000 short-lived compute-worker process
starts, plus repeated Watchdog/runner startup. A campaign cost model must time
this exact serial task schedule and include all process starts, pool
initialization, idle/recovery work, audit compression and disk writes. A
four-worker dispatcher that instead runs four null tasks concurrently is not
wall-time-equivalent to this executor. The two schedules cannot share one
prediction without a validated simulation of the actual executor.

The executor enforces up to four compute workers inside one activity. Its
activity lock is an in-memory lock on a single store object; separate
processes/store objects or run directories do not share that lock. There is
not yet a host-wide four-worker exclusion across simultaneous activities.
Before any representative benchmark or production run, the launcher needs a
host-level single-activity lock/registration that cannot be bypassed by a
second run directory, or must otherwise enforce and record a host-wide worker
semaphore. This is a resource-safety gap, not a scientific-protocol change.

The present executor streams a per-proposal gzip JSONL audit to the external
store. Every JSON record contains sequence, previous SHA-256, event and record
SHA-256; the draft budget's compact 3–5 byte zstd event encoding is not
implemented. A bounded synthetic N=100, E=800, 4E probe wrote 3,200 exact
executor-format proposals: 1,093,134 uncompressed bytes and 235,105 gzip bytes
(73.47 compressed bytes/proposal). A naive constant-rate sensitivity for the
registered **1,797,712,000** total proposals is about **123.0 GiB** for proposal
JSONL alone, versus the candidate 14-GiB total G0 output cap. That one-N,
3,200-record result is not a representative compression benchmark or a
formal prediction, but it shows the current implementation has no evidence
of meeting the cap and its observed rate overshoots it by about 8.8×. The
14-GiB cap permits only 8.36 bytes per proposal even before result artifacts.

PR #1124's packed lossless candidate is about 8.19 GB (7.63 GiB) *uncompressed*
before graph lists, results, manifests, metadata and temporary copies. It
could plausibly fit the 14-GiB cap, but is only a proposal: no encoder,
decoder/replay test, recovery test or compression-ratio/CPU measurement has
validated it, and removing per-record predecessor/digest fields must be
reviewed against the existing per-proposal audit obligation. The storage cap
therefore remains unvalidated and RESOURCE NO-GO remains in force.

## Fixed ten-graph H3 pilot packet (preparation record; subsequently executed)

The Q-independent first row of the already frozen H3 panel was selected for
each ascending N. This means the pilot intentionally uses the first registered
recording (`mouse01_sleep`) and `wake` state at each N; it is a fixed identity
diagnostic, not a representative sample of animals or states. The subset
repeat and window are inherited from the frozen H3 panel selection and were
not chosen after seeing Q values.

| Order | N | Fixed graph identity |
|---:|---:|---|
| 1 | 100 | `mouse01_sleep|N100|rep-055|wake|window-000` |
| 2 | 150 | `mouse01_sleep|N150|rep-070|wake|window-000` |
| 3 | 225 | `mouse01_sleep|N225|rep-033|wake|window-000` |
| 4 | 340 | `mouse01_sleep|N340|rep-083|wake|window-000` |
| 5 | 510 | `mouse01_sleep|N510|rep-067|wake|window-000` |
| 6 | 765 | `mouse01_sleep|N765|rep-021|wake|window-000` |
| 7 | 1,150 | `mouse01_sleep|N1150|rep-089|wake|window-000` |
| 8 | 1,725 | `mouse01_sleep|N1725|rep-014|wake|window-000` |
| 9 | 2,600 | `mouse01_sleep|N2600|rep-045|wake|window-000` |
| 10 | 3,900 | `mouse01_sleep|N3900|rep-070|wake|window-000` |

`G0_RIKEN_H3_CALIBRATION_PILOT_2026-10-21.json` records the complete source
MAT, selected-neuron-index, source-frame-index, historical job, 200-seed and
saved Q-vector SHA-256 values for these ten identities, plus Qmax and first
maximum index. The source MAT hash is
`a73526ff842633816a7d03f2578eaeb398fd928c9c2b4a62a2496273dc3c59e6`; each
pilot record says `HASHES_AND_200_SEEDS_VERIFIED; GRAPH_NOT_REBUILT`. The
packet SHA-256 is
`286fa084f125d205463218951e3ccf2640701dc7712a9a48cec62b323a49c36b` and the
identity manifest SHA-256 it binds is
`6a8357ac0b815c434421a31dc6c294c292b5c144713f49c52b5344038235ece2`. The
current preparation tool SHA-256 is
`ba7c855c1744fcfa1f94dc3d6ffe79cf4196695af1d6d5803beffc83d9c5d73e`. The
public packet contains no raw signal values, Q values, private paths or job
JSON; an output scan found none of `/Users/`, `.local/`, `q_values` or
`spike_smoothed`.

At packet creation its status was `PREPARED_NOT_APPROVED_NOT_EXECUTED`; the
later completed execution is documented above and in the linked PR comment.
The original 10-graph request proposed ceilings of 8 wall-hours, 32
process-tree CPU-hours, at most four compute workers, 4 GiB sampled aggregate
process-tree RSS, and 1 GiB output.
The workload is at most 10 graph reconstructions and 4,000 Louvain trials
(the 200 saved seeds on both authoritative historical and diagnostic sorted
edge orders). These are stop ceilings, not an estimate of completion time;
the RSS figure is sampling and is not a macOS hard memory limit.

The reproducible preparation commands (not a replay) are:

```sh
PHASE2_ROOT="/path/to/private/.local/phase2_multirecording"
PSA_ROOT="/path/to/private/.local/phase2_population_size_scaling"
IDENTITY_OUT="/tmp/G0_RIKEN_SOURCE_GRAPH_EXPECTED_MANIFEST_REPRODUCE.json"
PILOT_OUT="$PSA_ROOT/h3_identity_calibration_2026-10-21/prepared/G0_RIKEN_H3_CALIBRATION_PILOT.json"
uv run --python 3.14.0 --with numpy==2.5.3 --with scipy==1.18.1 \
  --with h5py==3.16.0 --with networkx==3.6.1 --with python-louvain==0.16 \
  python Experiments/neuro_sleep_null_calibration/riken_source_identity.py \
  --phase2-root "$PHASE2_ROOT" --psa-root "$PSA_ROOT" --output "$IDENTITY_OUT"
uv run --python 3.14.0 --with numpy==2.5.3 --with scipy==1.18.1 \
  --with h5py==3.16.0 --with networkx==3.6.1 --with python-louvain==0.16 \
  python Experiments/neuro_sleep_null_calibration/riken_source_identity.py \
  --phase2-root "$PHASE2_ROOT" --psa-root "$PSA_ROOT" \
  --manifest "$IDENTITY_OUT" --prepare-h3-pilot --output "$PILOT_OUT"
```

The second command intentionally refuses to overwrite its output; use a new
empty `prepared/` directory for a fresh packet. The committed manifest and
pilot packet were produced by the same two invocations with unique `/tmp`
output names, then copied into this Draft PR.

The first command verifies expected source identities and hashes without
reading signal values or constructing graphs. The second verifies the fixed
ten job/Q/seed references and writes the public-safe packet. They were run for
this update. The H3-specific launcher is now
`h3_supervised_pilot.py`. It verifies the fixed packet and manifest SHA-256,
exact ten-row order and source/job/subset/window/seed/reference-Q hashes, and
the locked Python/dependency environment before opening private source roots.
It then runs the historical graph-builder/order as the authority, reports
source identity, historical-order Q replay, and #1126 sorted-order
compatibility separately, and writes a bounded per-row evidence chain plus
Watchdog and control records. Any source identity, authoritative historical-Q,
resource, or audit failure stops the ordered pilot. A mismatch only in sorted
insertion compatibility is diagnostic and does not invalidate the historical
graph. Recovery inspection is audit-only; neither failed rows nor incomplete
activities are automatically retried.

The following was the launch template for the original 10-graph run; it is
retained as execution provenance and must not be reused for the 120-graph
panel:

```sh
export SRT_PHASE2_ROOT="<private Phase-2 root>"
export SRT_PSA_ROOT="<private PS-A root>"
RUN_ID="<new UUID>"
HEAD="<reviewed clean HEAD>"
PILOT_SHA="286fa084f125d205463218951e3ccf2640701dc7712a9a48cec62b323a49c36b"
uv run --python 3.14.0 python \
  Experiments/neuro_sleep_null_calibration/h3_supervised_pilot.py \
  --pilot "$SRT_PSA_ROOT/h3_identity_calibration_2026-10-21/prepared/G0_RIKEN_H3_CALIBRATION_PILOT.json" \
  --manifest Experiments/neuro_sleep_null_calibration/G0_RIKEN_SOURCE_GRAPH_EXPECTED_MANIFEST_2026-10-21.json \
  --run-directory "$SRT_PSA_ROOT/h3_identity_calibration_2026-10-21/$RUN_ID" \
  --run-id "$RUN_ID" --expected-head "$HEAD" \
  --researcher-confirmation "I AUTHORIZE H3 PILOT $RUN_ID $PILOT_SHA $HEAD"
```

For the original 10-graph execution, the approved stop ceilings and actual
use are in the linked completion report. The 120-graph candidate ceilings are
listed in the current-status section and require a separate researcher
decision. RSS remains sampled observation, not a hard cap. The Watchdog
serializes Watchdog-supervised activities through a persistent host-wide
advisory lock; activities that do not use it are outside that exclusion.
Parent-Watchdog failure triggers runner-side process-group termination, and
an unclosed activity ledger blocks a new launch pending audit-only inspection.

The completed 10-graph execution record is already in the linked top-level
PR #1127 comment. A future 120-graph report needs a new UUID and private,
empty audit directory; it must include the 120 packet hash, runtime-lock
result, source/edge/order hashes, separate per-graph source/historical-Q/
canonical-Q results, complete Q-vector hashes, Qmax/first-index checks,
resource accounting, Watchdog audit hash, and any stop reason. It must not
overwrite PS-A jobs or the completed 10-graph audit.

On a future run, stop immediately and preserve the partial audit on any source
MAT/job/subset/frame/seed identity mismatch, graph edge/node/degree invariant
failure, nonfinite or missing Q, authoritative historical-order trial-Q
delta exceeding `1e-10`, Qmax difference exceeding `1e-6`, or first-max-index
mismatch. A mismatch confined to the #1126 sorted-order diagnostic is recorded
as incompatibility but does not invalidate source identity or the authoritative
historical replay; it does not justify changing order, seeds, tolerance or
sample membership. The first fixed N=100 row is evaluated first; only if its
source and historical replay checks pass may the runner proceed to the next
preselected N. Resource ceiling, watchdog, output-integrity, or unknown failure
also stops the run; no row is replaced or retried.

## H3 cost evidence and remaining full-panel request

The fixed pilot has now run both graph orders for ten members: 10 source graph
rebuilds and 4,000 Louvain trials, with no edge swaps and no biological null
output. A full panel remains 120 graph rebuilds and 48,000 Louvain trials.
The largest panel matrix is 3,900 × 3,900 float64 (121,680,000 bytes / 116.1
MiB) for one dense matrix; the source window has 46.8 MB of float64 values
before correlation and MST temporaries. These are array-size calculations,
not peak-RAM or runtime measurements. T_PS-A remains unresolved, and the
single-recording/Wake pilot is not a defensible completion-time bound for the
full cross-recording/state panel.

A rough linear scaling of the measured 10-graph execution gives 1.91 wall-
hours and 2.02 CPU-hours for 120 graphs, but this is only an order-of-magnitude
reference: each N in the pilot came from the same Wake recording, and costs
can vary with source/session, state, correlation ties, and Louvain partition
trajectory. The candidate 8 wall-hours / 8 CPU-hours / one worker / 4 GiB
sampled RSS / 1 GiB output limits in the current-status section provide about
four times that simple scaling, but no validated upper prediction. Do not
start until the fixed 120 packet and launcher support, method decision,
resource review, and fresh live preflight are complete.

## Required next steps

1. Decide whether to prospectively amend the G0 observed/null Q representation
   to `CANONICAL_SORTED_EDGE_V1`. Keep the historic PS-A vectors immutable;
   if approved, update the relevant preregistration/resource documents before
   any biological null outcome is inspected.
2. If the policy is approved, make the minimal versioned 120-row H3 packet and
   runner extension, persist full canonical Q vectors, and obtain a separate
   researcher decision on the candidate 8h/8 CPU-hour/one-worker limits.
3. Execute the fixed 120 panel only after fresh identity, environment and
   resource preflight and explicit authorization. Stop on any source identity
   or historical-Q failure; record canonical-order differences without
   changing tolerance or sample membership.
4. Use the completed 120 panel to validate strata and reuse exact canonical
   Q vectors where hashes match. Then separately review and resource-plan the
   remaining observed baseline and G0 null workload. Do not use the H3 runtime
   as a G0 completion bound.
5. Resolve the proposed G0 audit encoding and validate the 14-GiB cap on
   representative synthetic tasks; preserve G0/T1 RESOURCE NO-GO until the
   full cost and storage model is independently reviewed.

Current verified state: **10/4,900 G0 source graphs have reconstructed edge
identities; 10/120 fixed H3 graphs have source identity and historical-Q
replay; 110 H3 panel and 4,890 other G0 edge sets remain pending.** All 4,900
expected source identity rows and all 120 frozen H3 selections are present in
the manifest. This is not a completed full-panel reconstruction, canonical
baseline, resource GO, or G0/T1 authorization.
