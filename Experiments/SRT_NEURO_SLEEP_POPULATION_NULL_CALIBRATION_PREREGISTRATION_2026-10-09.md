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

Reprocessing all 49,049 original graphs for multiple null ensembles would substantially expand computation. This *revised draft* defines a new, **narrower 10-of-100 subset-repeats-per-recording-and-finite-N estimand**; it must not be mislabeled as recalibration of the original 100-repeat headline. This reduces the number of *original graphs selected*, but null graph construction and optimization add substantial work; see the explicit resource ledger in §6. The 10/100 choice is a computational design choice made **after PS-A but before any null Q inspection**, not an independently validated optimal sampling fraction.

For each recording and finite N, rank the 100 existing subset-repeat IDs by the unsigned numeric result of the inherited BLAKE2b stable_seed function applied to the *exact stringified parts*:

~~~text
stable_seed(20261009, "NC_SUBSET_SELECTION_V1", recording_id, "N" + decimal(N), repeat_id)
~~~

Take the 10 smallest ranks; break seed ties by ascending repeat_id. This uses no Q or state contrast to select repeats. The original selected neuron indices and hash for each chosen repeat are loaded from the saved realized-subset ledger, **not regenerated** by either the erroneous label seed or the earlier intended numeric-N seed. Every selected subset remains paired across NREM/Wake windows. Record selected repeat IDs and SHA-256 hashes in the compact execution manifest **before** reading any new null Q.

The first 5 of these rank-selected 10 repeats form the **nested secondary signal-surrogate panel**. The secondary panel is not chosen on observed effect sizes.

### 2.2 Identity gate before null analysis

Before generating a null, verify the six data hashes against the 2026-10-09 result, each subset's indices and hash against its ledger, finite N and state-window counts, and reconstructed original graph edge sets or graph fingerprints. Recompute the original Q for a deterministic, hash-selected identity panel from the selected graphs using the **pinned original runtime/seed semantics** (macOS arm64, Python 3.14.0, python-louvain 0.16, dependency lock to be captured). Require both exact labeled edge-set identity and absolute |Q_recomputed - Q_logged| <= 1e-6 for every identity-panel graph. Identity-panel size/selection rule, environment manifest, graph serialization and trial-seed ledger must be locked before null Q inspection. If exact runtime cannot be restored, the edge/Q check fails, or a required artifact is unavailable, **NC-INVALID; no unrecorded skip or substitute comparison**. A transparently dated amendment may be proposed **only before inspecting any biological null outcome**. Never rechoose selected subsets or alter the original graph rule.

## 3. Primary null G0: connected, exact-degree-preserving graph rewiring

**Unit of null randomization:** each original selected-subset × state-window graph separately. Preserve its exact labeled node set, number of undirected edges, per-node degree, absence of self loops/multi-edges, and connectedness. Randomize which nodes connect using degree-preserving double-edge swaps; do **not** preserve MST edge identities, community assignments or geometric wiring.

For each source graph, make **10 independently seeded graph-null replicates**, independently starting each from the original labeled graph. The proposed kernel is a **custom reject-and-stay simple connected double-edge swap chain**, **not** a call to NetworkX `connected_double_edge_swap`. For each proposal, select two distinct present undirected edges uniformly, choose an orientation uniformly from the two possible cross-pairings after canonically sorting their endpoints, and either (a) perform the swap if it is simple and leaves the graph connected, or (b) **leave the graph unchanged and count one rejected proposal**. Each replicate stops after **exactly 4 × E total attempted proposals**, whether accepted or rejected (E = original number of edges). The stopping rule must not depend on the number of accepted swaps. This is an explicitly **procedure-defined null ensemble**; **uniform mixing over all connected fixed-degree graphs is not asserted**.

Before freezing, the actual algorithm, graph adjacency representation, proposal probabilities, endpoint ordering, connectivity test and dependency versions must be committed and reviewed. NetworkX 3.6.1 may be used for invariant checks; silently substituting its windowed `connected_double_edge_swap` is prohibited. **Synthetic-only mixing diagnostics** must track number of attempted/accepted swaps, triangle counts, degree assortativity and overlap with the starting graph at E, 2E, 4E and 8E proposals across independently seeded chains and representative synthetic degree sequences/sizes. The 8E diagnostic is for deciding **before freeze** whether 4E is an adequate approximation; it is not an optional observed-data analysis branch. Any substantial failure of synthetic-chain stabilization, unreasonable connectivity-check cost, or invalid topology means **NC-0 not passed**, not a license to tune after reading the RIKEN null. Mixing remains a limitation even if these diagnostics look stable.

At execution each required null graph must pass labeled node, degree sequence, edge count, simplicity and connectivity checks. A missing/invalid required null graph or trial gives **NC-INVALID** (no replacement cherry-picking), and record all kernel attempts, acceptance rates, swaps and diagnostics.

For every rewired graph run the same 200-repeat Louvain/max-Q algorithm and modularity definition as the original analysis. There is no optional choice of a better-looking null. Stable seeds follow the inherited stable_seed hash function with explicit *string* label semantics:

~~~text
stable_seed(20261009, "NC_G0_GRAPH_V1", recording_id,
            "N" + decimal(N), repeat_id, state, window_id, null_repeat)
stable_seed(20261009, "NC_G0_LOUVAIN_V1", recording_id,
            "N" + decimal(N), repeat_id, state, window_id, null_repeat, louvain_repeat)
~~~

Here null_repeat = 0..9 and louvain_repeat = 0..199; all ID encodings, ordering, and graph-to-seed mapping must be documented and fixed in the execution manifest before the first new Q is calculated.

**Important scope:** G0 conditions on observed state-dependent degree sequences. Because the graph builder targets mean degree 16, the N-dependence of D_G0 may arise from differences in state-specific degree heterogeneity plus finite-size/max-Q optimizer behavior, even though mean degree is nearly fixed. G0 calibrates these factors only under the **specified rewiring procedure**; it does not isolate how the graph builder **produced** the sequences, prove mixing to a uniform connected-degree ensemble, or distinguish all finite-size sampling artifacts. The primary outcome is therefore not an SRT-specific mechanism discriminator.

## 4. Primary outcome and Gate NC-1

For a recording s, finite N and selected subset r:

~~~text
D_obs(s,N,r)  = mean_windows Qobs(NREM) - mean_windows Qobs(Wake)
Q_G0(s,N,r,w) = mean_{10 graph-null replicates} maxQ_200(null graph at window w)
D_G0(s,N,r)   = mean_NREM_windows Q_G0 - mean_Wake_windows Q_G0
D_excess(s,N,r) = D_obs(s,N,r) - D_G0(s,N,r)
~~~

First take the median over the preselected 10 repeats within each session at each N. For mouse04 average its two session medians at each N; other animals have one session. Fit ordinary least-squares D_excess_animal(N) on log10(N) over **exactly the ten finite targets**. Call the animal-specific slope beta_G0_excess. In parallel calculate beta_obs_10 and beta_G0_10 by the identical aggregation, making it explicit that beta_obs_10 can differ from the published 100-repeat beta_N. Verify by simple OLS arithmetic that beta_G0_excess = beta_obs_10 - beta_G0_10 at each animal's aggregated-curve slope level; the displayed equality is a reconciliation check, not an assumption used to replace curve-level aggregation.

Report for every animal and every N: D_obs, D_G0, D_excess, slope, Spearman rho, finite-N ranges, and the independent FULL original reference. Cross-animal report: all five slopes, number positive, median and mean. Descriptive percentile bootstrap: resample five **animals** with replacement 10,000 times using seed 98766; 95% percentile intervals for the **mean and median** of beta_G0_excess. Do not bootstrap windows, null graphs or subsets as biological replicates. Intervals are descriptive with n=5, not a calibrated confirmatory p-value.

**Proposed Gate NC-1 (subject to a further independent methodology review before freeze):**

Define `p = number of animals with beta_G0_excess > 0`; zero slopes count as nonpositive. Compute `R_med = median(beta_G0_excess) / median(beta_obs_10)` **only** when `median(beta_obs_10) > 0` and at least 4/5 `beta_obs_10` slopes are positive; otherwise set R_med = undefined and classify NC-B (selected observed panel does not directionally reproduce PS-A). Report all five `R_i = beta_G0_excess / beta_obs_10` only where the individual denominator is positive; otherwise show undefined, never set it to zero or exclude that animal from p. Also report the unnormalized median and mean slopes (observed, G0 and excess) to prevent misleading ratio-only interpretation.

- **NC-A-material (direction + operational magnitude):** observed-panel reproducibility holds, p >= 4, and R_med >= **0.25**. The 25% retention bar is a **provisional operational materiality convention**, not a known biological threshold, statistical significance threshold or evidence that a quarter of the *biological mechanism* survives. It is selected before inspecting any G0 outcomes; its rationale and sensitivity to 0.10/0.50 must be independently reviewed **before freezing**.
- **NC-A-directional-only:** observed-panel reproducibility holds and p >= 4, but R_med < 0.25. This means only the *sign* remains in most animals; **do not** describe the residual as substantively surviving.
- **NC-B:** p = 3; **or** the selected observed panel does not reproduce a positive 4/5 trend, or R_med is undefined. No ambiguous discretionary catch-all.
- **NC-C:** observed-panel reproducibility holds and p <= 2.
- **NC-INVALID:** required input provenance, original-graph/Q identity, null topology, algorithmic reproducibility, optimizer trials, or required null replicates fail. No biological classification or post-hoc rescue.

**Monte-Carlo fragility check, descriptive:** with 10 G0 replicates, recompute beta_G0_excess from the first five and last five G0 replicates separately using their *fixed assigned index order*. Report both slopes and classifications. If the directional sign criterion p >= 4 or R_med >= 0.25 is not stable across the two halves, report **NC-B (Monte-Carlo unstable)** instead of claiming NC-A-material; do not increase null repeats after looking at the effect. A larger confirmatory follow-up would need a new prospective plan.

This is a **conditional residual N-dependence classification against G0 only**, not a p-value, proof that the remaining effect is non-artifactual, or a statement about individual D_excess zero crossing. Do not choose a new N range, delete animals, change repeat counts or redefine null-Q based on the result.

## 5. Secondary null T1: within-window independent neuron circular shifts

This null examines whether the measured slope remains when zero-lag cross-neuron coordination is disrupted while preserving each neuron's within-window amplitude distribution and circular temporal structure. It is **secondary and diagnostic**, not another chance to replace a failed NC-A.

On the fixed first 5 of 10 selected subset repeats per recording × finite N, use **5 surrogates** per state-window input. Independently circularly shift **each selected neuron's** S3 sequence within the original state window by an integer offset chosen uniformly from [ceil(L/4), floor(3L/4)] inclusive (L = frames in that window). No cell is shifted as an intact population, no mixing between state windows and no state relabeling. Preserve the selected neuron IDs, window IDs and Wake/NREM status. Recompute correlations, original MST-plus-edges builder, the same 200-repeat Louvain max-Q and paired state contrast.

~~~text
stable_seed(20261009, "NC_T1_SHIFT_V1", recording_id,
            "N" + decimal(N), repeat_id, state, window_id, surrogate_repeat, neuron_id)
stable_seed(20261009, "NC_T1_LOUVAIN_V1", recording_id,
            "N" + decimal(N), repeat_id, state, window_id, surrogate_repeat, louvain_repeat)
~~~

surrogate_repeat = 0..4. Store offsets or their verifiable hashes. Use the same session-median → mouse04 session average → animal-slope pipeline for a T1-adjusted diagnostic, and show the raw observed curve for that **same five-repeat panel**. Report whether the diagnostic agrees, disagrees or cannot be determined. No gate classification, pooled p-value, or post-hoc primary substitution from T1.

Caveats: circular shifting introduces a boundary seam, may not faithfully preserve nonstationary event structure, and cannot by itself identify biological coupling, causal coordination or consciousness. It tests a particular zero-lag surrogate assumption, not all signal-level null hypotheses.

## 6. Process gates, resource and interpretation controls

**Resource ledger (design estimate, not a benchmark):** the previous job ledger contains 49,049 original state-window graphs and 9,809,800 Louvain trials (including FULL). Excluding the small FULL contribution, the proposed G0 uses approximately `(10/100) * 10 = 1.0` times the original graph/Louvain work: roughly **49,000 G0 null graphs / 9.8 million Louvain trials**. T1 uses approximately `(5/100) * 5 = 0.25` times: roughly **12,250 rebuilt signal-surrogate graphs / 2.45 million Louvain trials**, before expensive correlation reconstruction. Combined estimate: **~61,250 newly optimized graphs / ~12.25 million Louvain trials**, about **1.25× the previous Louvain-trial count**, *plus* potentially dominant connectivity-preserving edge swaps, graph copies, correlation re-estimation, I/O and integrity checks. These are **approximations**; the actual per-condition graph-window inventory, graph sizes, memory ceiling, wall-time and failure/retry overhead must be reconstructed and documented from manifests. Replacing the original 20×20 G0 proposal with 10×10 is a **pre-null, transparent design revision after Claude's review**, not outcome-driven tuning.

**Gate NC-0a — synthetic-only feasibility before freeze:** implement the proposed graph-null kernel and benchmark entirely on **synthetic connected graphs and synthetic time series**, covering node sizes 100–3900 and representative edge/degree patterns. Record seconds per swap proposal, per graph replicate and per 200-trial optimizer run; the full projected worker-hours, storage and error risk must be explicitly evaluated. Inspect only provenance metadata and prior runtime summaries from biological data, not new null outputs. Synthetic-chain E/2E/4E/8E mixing diagnostics and deterministic reruns must pass an independently reviewed specification **before** locking 4E and 10 replicates. If they fail, revise this **draft** and obtain re-review; do not freeze an infeasible or ill-mixed sampler.

**Gate NC-0 — preregistration lock:** after the synthetic-only feasibility/mixing checks and independent methods review, resolve any ambiguity in the custom rewiring implementation, exact string/ID serialization, subset ordering and data availability; freeze a runnable implementation commit, dependency versions, original Q identity panel, source/selected-ledger hashes, selection manifest, graph/optimizer settings, all endpoint definitions and classification rules. No biological null Q inspection before this gate; this current draft is **not** a freeze commit.

**Gate NC-1 — G0 primary execution:** only after NC-0, finish the entire 10-subset panel with 10 null graphs/window and 200 Louvain trials/null graph; validate every stored Q_max against trial maxima and each graph's topology invariants. Do not inspect/classify partial animal curves and then optimize parameters. If the locked design is infeasible or invalid during execution, **stop**, publish deviation/failure, and require a separately reviewed prospective amendment before any new outcome analysis.

**Gate NC-2 — T1 secondary execution:** only after NC-1 results are frozen, run the predefined 5-repeat nested panel with 5 surrogate inputs/window. Never use it to retune G0 or the previous PS-A finding; if secondary resources are unavailable, report it as **not executed** rather than dropping T1 silently.

**Publication/claim constraints:**
1. Only **NC-A-material** would clear a predeclared *operational residual-magnitude* bar under this specific degree-conditioned topology null. **NC-A-directional-only** indicates positive direction without magnitude sufficiency. Neither denotes statistical significance, robustness to all nulls, independence from the original seed deviation, or an SRT-specific mechanism.
2. NC-C (and some NC-B outcomes) would weaken the interpretation that the original slope reflects higher-order graph organization beyond the preserved constraints; it would **not** prove that all biological network differences are artifacts.
3. G0 and T1 answer different questions; cross-null disagreement is a reportable result, not a reason to choose one after inspection.
4. Five animals, one dataset family, lineage overlap and the unresolved Kiyooka anchor constrain generalization.
5. No new NEURAL number, Phase-8 reopening, canonical/CompactCore/STATUS promotion, mechanism attribution, SRT-specific validation, One/Bearer/Selection/consciousness inference or claim of novel generic network-size effects.

## 7. Minimum final deliverables (only after execution authorization)

- Frozen preregistration SHA, final executed code SHA, runtime/dependency record and immutable input hashes;
- predeclared repeat-selection manifest and discrepancy ledger against PS-A's original 100-repeat result;
- completed null graph / Louvain integrity audit, synthetic-only runtime/mixing benchmark and (if T1 is executed) surrogate-offset ledger;
- per-recording, per-animal and cross-animal observed/null/excess curves with all five animal slopes and uncertainty;
- Gate NC-1 verdict (NC-A-material / NC-A-directional-only / NC-B / NC-C / NC-INVALID), per-animal and cross-animal residual/observed slope ratios, split-replicate stability, and T1 separate diagnostic interpretation if executed;
- all deviations, failed null draws, resource limits and inconclusive results, including negative results.

Original PS-A files remain unchanged except an optional **display-only repair** of the Markdown figure's GitHub-relative link, if separately included in the proposal PR.

## 8. Methodological references (not proof of this design's validity)

- Váša F, Mišić B. *Null models in network neuroscience*. Nature Reviews Neuroscience (2022). https://www.nature.com/articles/s41583-022-00601-9
- Bullmore / graph-theoretic reviews: modularity can appear in randomized networks and requires properly matched controls; https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2010.00200/full
- Fosdick BL, Larremore DB, Nishimura J, Ugander J. *Configuring Random Graph Models with Fixed Degree Sequences*. SIAM Review (2018). https://doi.org/10.1137/16M1087175
- NetworkX `connected_double_edge_swap` documents a windowed connectivity strategy that must not be conflated with this draft's custom proposal-count chain: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.swap.connected_double_edge_swap.html
- Neuron/glia multicell imaging surrogate example using single-neuron circular shifts; https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003949
