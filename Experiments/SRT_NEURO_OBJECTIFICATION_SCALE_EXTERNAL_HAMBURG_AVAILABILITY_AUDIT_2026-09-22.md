---
id: SRT-NEURO-OBJECTIFICATION-SCALE-EXTERNAL-HAMBURG-AVAILABILITY-AUDIT-20260922
type: experiment_audit
status: frozen
version: v0_1
record_stage: phase3a_result_blind_external_feasibility
date: 2026-09-22
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, ExternalReplication, HamburgCA1, AvailabilityAudit, ResultBlind]
---

# Phase 3A — result-blind external Hamburg availability audit

## PHASE 3A EXTERNAL HAMBURG AUDIT

This is a feasibility and availability audit only. It does not calculate correlation matrices, graphs, Louvain partitions, modularity, `Q`, `DeltaQ`, or any external network effect. No recording was excluded using a network outcome.

The audit inspected the processed G-Node repository at the repository/tree level, the published metadata CSVs, the Suite2p object inventory, the small `iscell.npy` objects, and one small pupillometry feature object. The large processed archive was not downloaded, and the 2.3-TiB raw imaging archive was not accessed.

## DATA SOURCE

- **Dataset:** Formozov A, Chini M, Dieter A, Yang W, Pöpplau JA, Hanganu-Opatz IL, Wiegert JS (2022), *Calcium Imaging and Electrophysiology of hippocampal Activity under Anesthesia and natural Sleep in Mice*.
- **Processed DOI:** [`10.12751/g-node.lkx6kk`](https://doi.gin.g-node.org/10.12751/g-node.lkx6kk/).
- **Processed repository:** [`doi/Anesthesia_CA1`](https://gin.g-node.org/doi/Anesthesia_CA1), live `master` at audit time `8a784cc0177eaa8d66970363b76b84ff1a7cf662`.
- **Raw DOI:** `10.12751/g-node.s549qk`; not downloaded.
- **license:** `CC0 1.0 Public Domain Dedication` for the processed G-Node dataset.
- **processed availability:** available and browsable. The DOI landing page advertises a 123-GiB processed ZIP; metadata CSVs, processed Suite2p directory listings, 54 calcium pupillometry feature pairs, and the required primary objects were reachable without materializing that archive.

The Scientific Data descriptor reports CA1 two-photon imaging at 30 frames/s, with an Anesthesia dataset of 189 five-minute recordings, a Transition State dataset, and a Natural Sleep dataset of 54 recordings lasting 2.1–14.8 minutes. The repository metadata and tree were treated as the operational source for file-level availability.

## ANIMALS / RECORDINGS / DATASET INVENTORY

| dataset | operational animal IDs | metadata rows / recordings | duration | status in this audit |
|---|---|---:|---|---|
| Anesthesia | `37527, 37528, 37529, 37530, 48, 51, 53` | 189 | 5.0 min fixed | primary candidate source |
| Natural Sleep | `8235, 8237, 8238` | 54 | 2.13–14.80 min from metadata | primary candidate source; epoch-label adaptation required |
| Transition State | `8235, 8237, 8238, F0, F1, M0, M3` in the CSV; `M0 (M3)` is combined in the paper | 199 CSV rows across 23 concatenated series | 2.8–18.9 min in the paper | separate inventory; not primary |

### Anesthesia conditions

The processed metadata uses `awa`, `iso`, `keta`, and `fenta`. `fenta` is the repository label for the MMF condition; it is not silently treated as Isoflurane.

| metadata condition | interpretation | recordings | animals |
|---|---|---:|---:|
| `awa` | awake | 39 | 7 |
| `iso` | Isoflurane | 49 | 7 |
| `keta` | Ketamine/Xylazine | 50 | 7 |
| `fenta` | MMF | 51 | 7 |

The primary Anesthesia contrast therefore has an animal-level overlap of all 7 animals, with 39 awake and 49 Isoflurane recordings. These are condition-specific recordings nested within animal; they are not same-recording paired observations.

### Natural Sleep conditions and state metadata

The 54 calcium recordings are distributed as `8235:22`, `8237:15`, and `8238:17`. The repository contains 54 paired calcium pupillometry videos, 54 DLC CSV feature files, and 54 `Matlab_2PM` feature files. The processed calcium tree does not contain a discrete Wake/NREM state vector for these 54 recordings. The separate `Sleep/sleep_scoring/*.mat` objects are the electrophysiology sleep scores for 4 animals and 7 ephys sessions, not an unambiguous state-vector mapping for the 54 calcium files.

The published method says that calcium sleep states can be recovered from pupil/eyelid dynamics using electrophysiology-grounded classification, but the ready-to-use calcium state labels were not found in the processed tree. This is an availability fact, not an outcome-dependent exclusion.

### Transition State separation

The Transition State CSV has 199 rows and 23 `Multiindex` series, including awake, Isoflurane, Keta/Xyl, MMF, recovery/post-anesthesia, and awake-control entries. This differs from the paper's summary of 172 transition recordings plus 37 awake controls. In the processed tree, 18 of the 23 concatenated series had reachable `F/Fneu/iscell/stat/ops` listings, while 5 metadata-derived paths were not directly resolvable (including shorthand `iso` paths and M0/M3 replacement paths). The accessible Transition State listings did not expose `spks.npy`. This dataset remains outside the primary Sleep and Anesthesia contrasts.

## REQUIRED DATA OBJECTS

For the 243 primary Anesthesia + Natural Sleep recording directories (189 + 54), the following objects were present in all 243 directory listings:

| object | primary availability | interpretation |
|---|---:|---|
| `F.npy` | 243/243 | per-ROI fluorescence traces |
| `Fneu.npy` | 243/243 | per-ROI neuropil traces |
| `spks.npy` | 243/243 | Suite2p deconvolved trace output |
| `iscell.npy` | 243/243 | ROI/cell inclusion object |
| `stat.npy` | 243/243 | ROI spatial-statistics object |
| `ops.npy` | 243/243 | Suite2p acquisition/processing metadata |

The 243 `iscell.npy` files were readable. Primary accepted-ROI counts were:

- Awake: `85–486` accepted ROIs per recording;
- Isoflurane: `151–652` accepted ROIs per recording;
- Natural Sleep: `267–1298` accepted ROIs per recording.

The Suite2p output convention documents `spks.npy` as deconvolved traces, `iscell.npy` column 1 as the cell/non-cell assignment, and `stat.npy` as one ROI-statistics dictionary per ROI, including `xpix`, `ypix`, and `med` ROI geometry. The repository's own validation code also uses `iscell[:,0]` to select accepted ROIs.

## RESULT-BLIND ELIGIBILITY

Eligibility was restricted to required objects, duration, usable accepted-ROI signal, spatial-object availability, metadata identity, and non-corrupt directory access.

| target | ELIGIBLE | INELIGIBLE | UNCERTAIN | reason |
|---|---:|---:|---:|---|
| Anesthesia all processed recordings | 189 | 0 | 0 | all metadata rows map to complete primary Suite2p object sets; all have positive accepted-ROI counts |
| Anesthesia awake primary cell | 39 | 0 | 0 | 5 min, awake metadata, complete objects, all 7 animals represented |
| Anesthesia Isoflurane primary cell | 49 | 0 | 0 | 5 min, Isoflurane metadata, complete objects, all 7 animals represented |
| Natural Sleep object-level candidates | 54 | 0 | 0 | complete objects, positive accepted-ROI counts, 2.13–14.80 min |
| Natural Sleep Wake↔sleep contrast | 0 final / 54 candidates | 0 | 54 | calcium-state epoch labels are not delivered as a ready discrete vector; recovery from paired pupil features must be frozen first |
| Transition State | 0 primary | 0 outcome-based | 199 rows / 23 series uncertain | metadata/tree naming discrepancy and no `spks.npy` in accessible processed series |

No recording is marked scientifically unusable because of a Q, correlation, modularity, or grain result. The Natural Sleep `UNCERTAIN` status is a protocol-object status only.

## CANDIDATE CONTRASTS

### External Sleep

`Wake ↔ Natural Sleep` is feasible in principle for 54 calcium recordings from 3 animals, using within-recording epoch labels reconstructed from the paired calcium pupillometry features. The biological unit must remain animal, with recordings and windows nested within animal. Same-session/state pairing is not yet frozen at the epoch level.

### External Anesthesia

`Wake ↔ Isoflurane` is feasible as an animal-level between-condition contrast: all 7 Anesthesia animals have both awake and Isoflurane recordings. It is not a same-session paired contrast. Keta/Xyl and MMF are retained as future secondary contrasts and are not promoted to primary.

## SIGNAL

- **S3-equivalent available:** the closest processed analogue is available. `spks.npy` is present for all 189 Anesthesia and all 54 Natural Sleep primary recording directories, and the descriptor identifies Suite2p/OASIS deconvolution.
- **adaptation required:** `spks.npy` is not asserted to be byte-for-byte identical to Kiyooka's S3 smoothed deconvolved activity. A single Gaussian smoothing rule, frame alignment rule, and sleep-state window rule must be frozen before any external network calculation. If the primary Sleep state labels are reconstructed from pupil features, that reconstruction must be result-blind and frozen before signal-window extraction.

## SPATIAL GEOMETRY

- **available:** yes for the primary 243 recordings. `stat.npy` and `ops.npy` are present; Suite2p `stat` provides ROI masks/pixel coordinates and the `med` center, so ROI centroids can be recovered without using a network outcome.
- **source:** Suite2p `stat.npy` / `ops.npy`, with inclusion from `iscell.npy`. The published imaging geometry is 512×512 pixels at 30 frames/s.

## GRAIN FEASIBILITY

No grain construction was run. The following is a candidate rule only, to be frozen before any external `DeltaQ`:

- `G1 = single neuron`: all accepted Suite2p ROIs (`iscell[:,0] == 1`).
- `G2 = intermediate local aggregation`: deterministic spatial clusters formed from ROI centroids, with cluster size `m2 = max(2, ceil(0.02 N))`.
- `G3 = coarser local aggregation`: the same deterministic local-clustering rule, with `m3 = max(4, ceil(0.04 N))`.
- For both grains, seed order is lexicographic by centroid `(y, x)` with ROI index as the deterministic tie-break; each seed takes its nearest currently unassigned centroids until the frozen cluster size is reached. The same rule is applied to every state and recording. This is dataset-size-aware, spatially local, deterministic, and independent of network outcomes.

Using the observed accepted-ROI minima in the primary candidates, the conservative minimum node counts are:

| primary cell | accepted-ROI minimum `N` | G1 minimum nodes | G2 minimum nodes | G3 minimum nodes |
|---|---:|---:|---:|---:|
| Awake | 85 | 85 | 43 | 22 |
| Isoflurane | 151 | 151 | 38 | 22 |
| Natural Sleep | 267 | 267 | 45 | 25 |
| minimum across primary cells | 85 | 85 | 38 | 22 |

The node counts are the deterministic partition lower bounds `ceil(N / m_g)` for the proposed fixed fractions; they are not observed network outputs.

## GRAPH RULE

- **Frozen candidate rule:** connected MST backbone plus strongest ranked absolute-correlation edges, with target mean degree `k̄ = 16`.
- **k̄=16 feasible:** yes for the proposed primary grain minima. A simple undirected graph with mean degree 16 requires at least `N = 17` nodes; the conservative proposed G3 minimum is 22.
- **adaptation required:** no graph-degree adaptation is required at the availability stage. The graph itself was not constructed and no modularity was calculated. If a later pre-processing audit finds a state-specific accepted-ROI count below the frozen grain lower bound, the protocol must stop and be amended before any result is inspected; it must not silently lower `k̄`.

## BIOLOGICAL HIERARCHY

- **animals:** 7 in the primary Anesthesia dataset; 3 in the primary Natural Sleep dataset.
- **sessions/recordings:** Anesthesia recordings are repeated condition-specific recordings nested within animal; Natural Sleep recordings are repeated sessions nested within animal.
- **epochs/windows:** state epochs and analysis windows are nested within recordings and are not biological replicates.
- **primary biological unit:** animal.

## BLOCKERS

1. Natural Sleep calcium files have paired pupil/DLC features and videos, but a ready discrete Wake/NREM annotation vector was not found in the processed tree. A result-blind state-recovery rule and minimum per-state epoch-duration rule must be frozen before preregistration.
2. The Hamburg `spks.npy` output is the appropriate nearest processed analogue, but exact S3 equivalence is not established. The smoothing and frame/window mapping are protocol adaptations that must be declared, not hidden.
3. The Transition State metadata/tree discrepancy and absence of accessible `spks.npy` in its processed series make it unsuitable for the primary contrast in this audit. It remains a future secondary/transition-specific dataset.
4. The processed DOI advertises a 123-GiB ZIP; only metadata and small object-level audit files were fetched. Full archive materialization remains a later execution step, after protocol freeze.

## VERDICT

**PROTOCOL-ADAPTATION-REQUIRED**

There are enough independent Hamburg CA1 calcium recordings and enough spatially resolved accepted ROIs to support a result-blind external replication design. The design is not yet ready for preregistration as a direct execution protocol because Natural Sleep state epochs and the Hamburg-to-S3 signal/window mapping require explicit frozen adaptations.

This verdict is strictly about external-data availability and protocol feasibility. It makes no claim about any network effect, SRT, objectification, Bearer, One, consciousness, or mechanism.

## NEXT

**freeze external replication protocol before any `DeltaQ`**

Required next design decisions are the result-blind sleep-state recovery rule, minimum usable state-window duration, fixed Hamburg smoothing/window mapping, and final confirmation of the candidate spatial clustering rule. No external modularity or network-effect computation was started in Phase 3A.

## AUDIT EVIDENCE

- Official processed DOI: <https://doi.gin.g-node.org/10.12751/g-node.lkx6kk/>
- GIN repository tree: <https://gin.g-node.org/doi/Anesthesia_CA1>
- Scientific Data descriptor: <https://pmc.ncbi.nlm.nih.gov/articles/PMC8964694/>
- Suite2p output schema used for the object audit: <https://suite2p.readthedocs.io/en/latest/outputs/>
- Local machine-readable inventory: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_AVAILABILITY_AUDIT_2026-09-22.json`
