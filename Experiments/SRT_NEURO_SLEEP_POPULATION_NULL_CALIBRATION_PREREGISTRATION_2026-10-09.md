---
id: SRT-NEURO-SLEEP-POPULATION-NULL-CALIBRATION-PREREGISTRATION-20261009
type: experiment-preregistration
status: draft
record_stage: proposal_only_not_frozen_no_execution
date: 2026-10-09
programme: SRT Neuro Objectification–Scale Stability
layer: operations
epistemic_layer: experimental
claim_mode: protocol
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Experiments/SRT_NEURO_POPULATION_SIZE_SCALING_PREREGISTRATION_2026-09-24.md
  - Experiments/SRT_NEURO_POPULATION_SIZE_SCALING_RESULT_2026-10-09.md
  - Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
tags: [Neuroscience, RIKEN, Sleep, NullCalibration, PopulationSize, Modularity, Preregistration, NonCanonical]
---

# RIKEN Sleep population-size scaling — null-calibration preregistration candidate

> **Status: DRAFT FOR INDEPENDENT REVIEW; NOT FROZEN; NO EXECUTION AUTHORIZED.**
> This document is a prospective plan for **uncomputed null-calibrated endpoints**, written **after** the 2026-10-09 PS-A result was observed. It must never be described as a preregistration of the original positive population-size slope or as an independent biological replication. Following review, freeze its actual code, parameters, dataset/ledger identity, and commit SHA before running or inspecting any null outcome.

## 1. Motivation, question, and provenance

The completed RIKEN Sleep N-scaling holdout (PR #1113) reported positive finite-N slopes in all five eligible animals (median beta_N = 0.06729) but no observed finite-N sign reversal. Its Gate 1 = PS-A authorized **stopping**, followed by a **separately preregistered null-calibration**; it did not authorize an unregistered mechanism search.

**New question:** how much of the observed positive slope of the operational NREM-minus-Wake modularity contrast survives comparison with a null distribution that preserves, graph by graph, population size, edge count, connectedness and the exact degree sequence, but destroys higher-order graph topology?

The primary target is a **degree-conditioned topology excess slope**, not an SRT variable, consciousness measure, or proof of scale-specific ontology. The degree-preserving null does not test whether the original neuron-to-neuron correlations are causal, nor does it preserve the original correlation geometry, spanning-tree membership, spatial distances or triangles. A separate signal-level surrogate will address a different, narrower question.

**Disclosed antecedents and limitations:** this protocol was designed after observing PS-A, using the same five animal lineages and underlying Sleep recordings. Its success would not provide a wholly independent discovery. The earlier subset seed used a string label such as "N100" instead of the preregistered numeric N; this protocol deliberately consumes the **recorded realized subsets** and cannot repair original exact seed-recipe compliance. The Kiyooka session-specific anchor remains ANCHOR-UNRESOLVED. Mouse05 overlaps the Phase 1 lineage.

## 2. Inherited measurements and fixed audit unit

- Data: the **same** eligible six RIKEN Sleep recordings from five animals; mouse04 has two sessions and must contribute only one animal-level curve. No new recordings or outcome-based exclusions.
- Source signal: existing S3 smoothed_spike. State annotations, windows, accepted neuron sets, signal preprocessing and original graph builder remain exactly those of the completed run.
- Original graph builder: binary undirected connected network from an MST backbone plus highest-ranked absolute-correlation edges, target mean degree 16; original graph construction is *not* altered by this proposal.
- Graph-level Q: max of 200 Louvain trials with inherited settings; state-level Q: arithmetic mean over state windows; NREM minus Wake contrast.
- Finite N grid: 100, 150, 225, 340, 510, 765, 1150, 1725, 2600, 3900. FULL is reported descriptively, with no place in any primary finite-N slope.
- Biological uncertainty: five independent animals, not neurons, windows, graph null draws or session repeats. Report six nested recordings; combine mouse04's two session medians before fitting/cross-animal summaries.
- Raw data and job/seed/checkpoint ledgers remain in ignored local storage, not Git. Commit only compact aggregate result, code/manifests and checksums.

### 2.1 Fixed computational subset: reduced, paired follow-up

Reprocessing all 49,049 original graphs for multiple null ensembles would substantially expand computation. This proposal therefore defines a new, **narrower 20-of-100 subset-repeats-per-recording-and-finite-N estimand**; it must not be mislabeled as recalibration of the original 100-repeat headline.

For each recording and finite N, rank the 100 existing subset-repeat IDs by the unsigned numeric result of the inherited BLAKE2b stable_seed function applied to the *exact stringified parts*:

~~~text
stable_seed(20261009, "NC_SUBSET_SELECTION_V1", recording_id, "N" + decimal(N), repeat_id)
~~~

Take the 20 smallest ranks; break seed ties by ascending repeat_id. This uses no Q or state contrast to select repeats. The original selected neuron indices and hash for each chosen repeat are loaded from the saved realized-subset ledger, **not regenerated** by either the erroneous label seed or the earlier intended numeric-N seed. Every selected subset remains paired across NREM/Wake windows. Record selected repeat IDs and SHA-256 hashes in the compact execution manifest **before** reading any new null Q.

The first 10 of these rank-selected 20 repeats form the **nested secondary signal-surrogate panel**. The secondary panel is not chosen on observed effect sizes.

### 2.2 Identity gate before null analysis

Before generating a null, verify the six data hashes against the 2026-10-09 result, each subset's indices and hash against its ledger, finite N and state-window counts, and reconstructed original graph edge sets or graph fingerprints. Re-running the original Louvain max-Q pipeline must match the logged Q for the selected graph to the documented deterministic tolerance (absolute 1e-6) wherever identical software/seed semantics are available. If source graph/ledger identity or computational comparability fails, stop with NC-INVALID and document why; do not substitute a new graph rule or rechoose subsets.

## 3. Primary null G0: connected, exact-degree-preserving graph rewiring

**Unit of null randomization:** each original selected-subset × state-window graph separately. Preserve its exact labeled node set, number of undirected edges, per-node degree, absence of self loops/multi-edges, and connectedness. Randomize which nodes connect using degree-preserving double-edge swaps; do **not** preserve MST edge identities, community assignments or geometric wiring.

For each source graph, make **20 independently initialized rewired graph replicates**. Use a simple connected-graph double-edge-swap Markov procedure with exactly 2 × E **accepted** swaps per replicate (E = original number of edges). A proposal picks two distinct edges uniformly, chooses one of two orientations with equal probability, and is accepted only if its endpoints are valid, it introduces no self-loop/duplicate and the resulting graph remains connected. Cap attempted proposals at 100 × (2 × E) per replicate. Failure to reach the acceptance target is an **invalid replicate**, not permission to relax constraints or replace the graph; if any required replicate is missing, primary classification is NC-INVALID. Track attempts, acceptance rate, edge count, degrees, connectivity and triangle count as diagnostics. The swap count is a fixed algorithmic convention, **not a guaranteed proof of Markov-chain mixing**.

For every rewired graph run the same 200-repeat Louvain/max-Q algorithm and modularity definition as the original analysis. There is no optional choice of a better-looking null. Stable seeds follow the inherited stable_seed hash function with explicit *string* label semantics:

~~~text
stable_seed(20261009, "NC_G0_GRAPH_V1", recording_id,
            "N" + decimal(N), repeat_id, state, window_id, null_repeat)
stable_seed(20261009, "NC_G0_LOUVAIN_V1", recording_id,
            "N" + decimal(N), repeat_id, state, window_id, null_repeat, louvain_repeat)
~~~

Here null_repeat = 0..19 and louvain_repeat = 0..199; all ID encodings, ordering, and graph-to-seed mapping must be documented and fixed in the execution manifest before the first new Q is calculated.

**Important scope:** G0 conditions on observed state-dependent degree sequences. It controls modularity bias due to the given network size/edge count/degree sequence and optimizer under that graph null; it cannot isolate how the graph builder **produced** those sequences or distinguish all finite-size sampling artifacts.

## 4. Primary outcome and Gate NC-1

For a recording s, finite N and selected subset r:

~~~text
D_obs(s,N,r)  = mean_windows Qobs(NREM) - mean_windows Qobs(Wake)
Q_G0(s,N,r,w) = mean_{20 graph-null replicates} maxQ_200(null graph at window w)
D_G0(s,N,r)   = mean_NREM_windows Q_G0 - mean_Wake_windows Q_G0
D_excess(s,N,r) = D_obs(s,N,r) - D_G0(s,N,r)
~~~

First take the median over the preselected 20 repeats within each session at each N. For mouse04 average its two session medians at each N; other animals have one session. Fit ordinary least-squares D_excess_animal(N) on log10(N) over **exactly the ten finite targets**. Call the animal-specific slope beta_G0_excess. In parallel calculate beta_obs_20 and beta_G0_20 by the identical aggregation, making it explicit that beta_obs_20 can differ from the published 100-repeat beta_N.

Report for every animal and every N: D_obs, D_G0, D_excess, slope, Spearman rho, finite-N ranges, and the independent FULL original reference. Cross-animal report: all five slopes, number positive, median and mean. Descriptive percentile bootstrap: resample five **animals** with replacement 10,000 times using seed 98766; 95% percentile intervals for the **mean and median** of beta_G0_excess. Do not bootstrap windows, null graphs or subsets as biological replicates. Intervals are descriptive with n=5, not a calibrated confirmatory p-value.

**Frozen classification if and only if NC validity checks pass:**

- **NC-A (positive residual):** at least 4/5 animals have beta_G0_excess > 0 **and** cross-animal median beta_G0_excess > 0. Report interval width and effect sizes; do not interpret NC-A as evidence of a particular SRT mechanism.
- **NC-B (mixed/inconclusive):** 3/5 positive slopes or an otherwise inconclusive directional picture not satisfying NC-A or NC-C.
- **NC-C (no positive residual support):** at most 2/5 slopes are positive **or** cross-animal median beta_G0_excess <= 0.
- **NC-INVALID:** input provenance, topology invariants, optimizer trials or required replicates fail. No biological classification or post-hoc rescue.

The classification is about *residual N dependence against G0*, not whether any individual D_excess crosses zero. Do not choose a new N range, delete animals, change the number of repeats or redefine null-Q because the directional result is unhelpful.

## 5. Secondary null T1: within-window independent neuron circular shifts

This null examines whether the measured slope remains when zero-lag cross-neuron coordination is disrupted while preserving each neuron's within-window amplitude distribution and circular temporal structure. It is **secondary and diagnostic**, not another chance to replace a failed NC-A.

On the fixed first 10 of 20 selected subset repeats per recording × finite N, use **10 surrogates** per state-window input. Independently circularly shift **each selected neuron's** S3 sequence within the original state window by an integer offset chosen uniformly from [ceil(L/4), floor(3L/4)] inclusive (L = frames in that window). No cell is shifted as an intact population, no mixing between state windows and no state relabeling. Preserve the selected neuron IDs, window IDs and Wake/NREM status. Recompute correlations, original MST-plus-edges builder, the same 200-repeat Louvain max-Q and paired state contrast.

~~~text
stable_seed(20261009, "NC_T1_SHIFT_V1", recording_id,
            "N" + decimal(N), repeat_id, state, window_id, surrogate_repeat, neuron_id)
stable_seed(20261009, "NC_T1_LOUVAIN_V1", recording_id,
            "N" + decimal(N), repeat_id, state, window_id, surrogate_repeat, louvain_repeat)
~~~

surrogate_repeat = 0..9. Store offsets or their verifiable hashes. Use the same session-median → mouse04 session average → animal-slope pipeline for a T1-adjusted diagnostic, and show the raw observed curve for that **same ten-repeat panel**. Report whether the diagnostic agrees, disagrees or cannot be determined. No gate classification, pooled p-value, or post-hoc primary substitution from T1.

Caveats: circular shifting introduces a boundary seam, may not faithfully preserve nonstationary event structure, and cannot by itself identify biological coupling, causal coordination or consciousness. It tests a particular zero-lag surrogate assumption, not all signal-level null hypotheses.

## 6. Process gates, resource and interpretation controls

**Gate NC-0 — preregistration lock:** independent content/method review; explicitly resolve any ambiguity in graph-rewiring implementation, exact string/ID serialization and data availability; freeze implementation commit, dependency versions, source/selected-ledger hashes, selection manifest, null counts, graph/optimizer settings and all classification rules. No null Q inspection until this gate is approved. This current draft is **not** the freeze commit.

**Gate NC-0b — synthetic-only quality check:** run unit tests on synthetic connected graphs and synthetic time series, validating invariants, deterministic reruns, missing-data handling and runtime. Never tune null settings against any observed RIKEN Sleep null result. Record resource expectations. If the locked design is computationally infeasible, stop and issue a **new transparently dated amendment before biological null results**, never silently reduce repetitions mid-run.

**Gate NC-1 — G0 primary execution:** finish the entire prescribed selection panel, 20 null graphs/window and 200 finite Louvain Q trials/null graph; validate each recorded max-Q against its trial maximum and confirm topology invariants. Do not inspect/classify partial animal curves and then optimize parameters.

**Gate NC-2 — T1 secondary execution:** only after NC-1 is frozen, run the predefined 10-repeat nested panel and 10 surrogate inputs/window. Never use it to retune G0 or the previous PS-A finding.

**Publication/claim constraints:**
1. NC-A would mean the positive size trend survives this **specific degree-conditioned topology null** in the defined reduced panel, not all possible nulls and not the original strict seed-recipe preregistration.
2. NC-C would weaken the interpretation that the original slope reflects higher-order graph organization beyond the preserved constraints; it would **not** prove that all biological network differences are artifacts.
3. G0 and T1 answer different questions; cross-null disagreement is a reportable result, not a reason to choose one after inspection.
4. Five animals, one dataset family, lineage overlap and the unresolved Kiyooka anchor constrain generalization.
5. No new NEURAL number, Phase-8 reopening, canonical/CompactCore/STATUS promotion, mechanism attribution, SRT-specific validation, One/Bearer/Selection/consciousness inference or claim of novel generic network-size effects.

## 7. Minimum final deliverables (only after execution authorization)

- Frozen preregistration SHA, final executed code SHA, runtime/dependency record and immutable input hashes;
- predeclared repeat-selection manifest and discrepancy ledger against PS-A's original 100-repeat result;
- completed null graph / Louvain integrity audit and surrogate-offset ledger;
- per-recording, per-animal and cross-animal observed/null/excess curves with all five animal slopes and uncertainty;
- Gate NC-1 verdict (NC-A/B/C/INVALID) and T1 separate diagnostic interpretation;
- all deviations, failed null draws, resource limits and inconclusive results, including negative results.

Original PS-A files remain unchanged except an optional **display-only repair** of the Markdown figure's GitHub-relative link, if separately included in the proposal PR.

## 8. Methodological references (not proof of this design's validity)

- Váša F, Mišić B. *Null models in network neuroscience*. Nature Reviews Neuroscience (2022). https://www.nature.com/articles/s41583-022-00601-9
- Bullmore / graph-theoretic reviews: modularity can appear in randomized networks and requires properly matched controls; https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2010.00200/full
- Neuron/glia multicell imaging surrogate example using single-neuron circular shifts; https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003949
