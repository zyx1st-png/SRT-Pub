---
id: SRT-NEURO-G0-CANONICAL-Q-ORDER-AMENDMENT-20261023
type: proposal
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
date: 2026-10-23
scope: prospective common observed/null Louvain-Q representation and resource-plan amendment
dependency:
  - Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
  - Experiments/neuro_sleep_null_calibration/G0_RIKEN_SOURCE_IDENTITY_AND_H3_READINESS_2026-10-21.md
  - Experiments/neuro_sleep_null_calibration/G0_T1_PROSPECTIVE_RESOURCE_BUDGET_AMENDMENT_DRAFT_2026-10-20.md
tags: [Neuroscience, RIKEN, G0, Louvain, Q, ProspectiveAmendment, Draft]
---

# G0 common observed/null Q-order amendment

**DRAFT / NOT EFFECTIVE.** This is a prospective method change for independent review and researcher decision. It is not a routine code fix, result claim, NC-0 freeze, or authorization to run H3, a canonical observed baseline, G0, or T1. Until an explicit dated amendment is accepted and the relevant execution package is frozen, G0/T1 remain **RESOURCE NO-GO**.

## Decision proposed

Adopt **CANONICAL_SORTED_EDGE_V1** as the single graph-to-Louvain representation for both selected observed graphs used by the G0 analysis and every final 4E null graph.

For each graph, obtain each vertex's stable original-neuron integer index from the verified realized-subset ledger. Insert vertices in ascending original index. Map every edge to those original indices, normalize it to (min(i,j), max(i,j)), reject duplicates, and insert edges once in lexicographic pair order with weight exactly 1.0. Require the expected labeled node set, simple connected topology, and E=8N where the source manifest requires it. Do not use temporary array positions, historical NetworkX node iteration, swap proposal order, or scheduler order as ordering keys.

The resulting weighted NetworkX graph is the common input to the observed and null Q routines. Use python-louvain 0.16, best_partition(weight="weight", resolution=1.0, random_state=seed), then modularity(partition, graph, weight="weight"). The 200 seed values and their order are fixed inputs, not chosen by the graph builder:

- For each observed source graph, retain the exact 200-value PS-A seed vector and its recorded order: stable_seed(12345, recording_id, "sleep", "S3", "C1", analysis_label, state_index*1000 + window_index, repeat_index). Verify it against the historical seed ledger before canonical replay; never regenerate it under a new namespace.
- For each G0 null graph, retain the preregistered 200-value vector: stable_seed(20261009, "NC_G0_LOUVAIN_V1", recording_id, "N" + decimal(N), repeat_id, state, window_id, null_repeat, louvain_repeat), with the registered string labels and indices. Do not change or reorder this recipe.

The primary graph statistic remains Qmax_200 = max(Q[0], …, Q[199]); record the zero-based index of the first maximum in the frozen seed order. Save the complete ordered Q vector. Each result identity must bind the source/job and selected-neuron hashes, original node-index vector hash, labeled edge-set hash, CANONICAL_SORTED_EDGE_V1, ordered node/edge/adjacency representation hash, 200-seed vector hash, Python/package/runtime-lock and implementation hashes, complete Q-vector hash, Qmax and first-max index. Missing/nonfinite trials or identity disagreement are NC-INVALID; no replacement trial, graph, seed or sample is allowed.

This rule changes how a fixed labeled graph is presented to an order-sensitive heuristic. It does not alter the historical correlation/MST/top-edge graph topology, 4E swap kernel, number or identity of selected source graphs, null replicate count, Q definition, or seed values.

## Why this is a prospective scientific change

The fixed 10-graph H3 pilot verified source identity and replayed 2,000/2,000 historical-order Q values exactly. Its sorted-edge compatibility diagnostic differed from historical order on all 10 graphs. That establishes that adjacency order affects the finite Louvain result and that edge-set identity alone is insufficient.

The existing H3 diagnostic and #1126 executor sort edges using their current local node positions while preserving the supplied node list. The proposed contract instead keys node order to stable original-neuron indices from the realized-subset ledger. Therefore the 10/10 diagnostic is evidence of order sensitivity, **not a direct validation or rejection of this exact original-index policy**. The pilot remains unchanged and is retained as historical evidence. The fixed 120-graph H3 panel must separately report (1) source/edge identity, (2) historical-order replay, and (3) the new canonical representation result.

Historical PS-A Q vectors, jobs, seeds and original reported slopes remain immutable provenance. Before any new biological null Q is inspected, recompute and hash the canonical 200-Q vector for every one of the 4,900 fixed G0 observed source graphs (980,000 observed Louvain trials). Recompute the G0-sample observed state contrasts/slopes, paired excess slopes, and every downstream NC-A / NC-B / NC-C / NC-INVALID determination that uses those observed values. The published 100-repeat PS-A result remains the historical result; the selected 10/100 G0 estimand and its historical-vs-canonical differences must be reported separately. Do not overwrite old Q values or silently relabel them canonical.

Keep unchanged: selected-repeat identities and pairing; 49 finite-N windows and exclusion of FULL from primary inference; 10 null replicates per source graph; exactly 4E proposals and registered graph invariants; all graph and Louvain seed recipes; 200 trials; session-to-animal aggregation and paired D_excess order; five-animal unit; existing regression, inference, Bonferroni, materiality, direction, invalidity, and failure thresholds; no outcome-directed retries or sample changes; and MIXING-UNRESOLVED for the finite swap procedure. Only the graph-to-Louvain ordering policy and the observed Q baseline values change. Any altered downstream classification is a reportable consequence of this prospective amendment, not evidence that the old values were erroneous.

## Finite-heuristic interpretation

Qmax_200 is the maximum found in exactly 200 seeded Louvain heuristic runs. It is not the global modularity optimum, proof of optimizer convergence, or an order-invariant graph property. Canonical order removes one avoidable implementation degree of freedom and makes observed/null calls reproducible under the locked environment; it does not remove dependence on the heuristic, seed vector, finite restart count, or software/runtime.

Retain all 200 values and the first-max index. As descriptive diagnostics only, report prefix maxima at fixed prefixes 50/100/150/200 and the number of distinct returned partitions (with a stable partition encoding). These diagnostics do not change the endpoint, add thresholds, authorize more runs, or support outcome-selected extension. Synthetic tests must show that changing input enumeration while preserving original neuron IDs leaves the canonical graph and Q vector unchanged, while arbitrary relabeling is not treated as identity: labels must be mapped back through the frozen source-ID map before comparison.

## Minimal implementation and verification

PR #1126 already sorts normalized edge pairs and inserts unit-weight edges, then runs the registered python-louvain calls. It is reusable for edge-policy mechanics, but it currently retains the input node sequence and sorts positional endpoint indices. It is not by itself a complete implementation of this amendment unless the input node sequence is first mapped to ascending original-neuron indices and the exact ordered-representation hash is persisted.

The scoped implementation adds one shared canonical graph/Q contract used by the null worker and the observed replay adapter. It validates original IDs, sorts node and labeled-edge sequences, builds unit-weight edges, and produces separately verifiable topology and ordered-representation hashes. The old historical replay remains available and is not redirected through the new helper. Synthetic regressions cover scrambled node/edge input order, source-label remapping, deterministic 200-seed Q vectors, first-max ties, malformed identities, observed/null adapter equivalence, and current G0 spawn-worker integration. No biological source signal, Q vector, or null graph is read or generated by these tests.

## Resource scope and fixed 120-graph H3 reuse

The resource model must add the canonical observed baseline as a distinct stage: 4,900 graph builds/identity checks and 980,000 observed Louvain trials. The 4,900 source reconstructions overlap the G0 source-build/cache stage and may be counted once only when the exact builder, source-window identity and cache hashes match. The 980,000 observed trials are additional to the 9,800,000 G0-null trials; they must not be hidden in null-task cost. T1 remains separate and T1-GO requires G0-GO.

Complete the already frozen 120-graph H3 panel with a fresh UUID and audit directory. For every graph retain full historical-order and canonical Q vectors as separate results (48,000 trials total, subject to exact reuse of already completed pilot artifacts). The 24,000 canonical H3 trials are a subset of, not an addition to, the 980,000 canonical observed baseline trials. Reuse them only when all of the following match: source MAT/job/subset/window identity; absolute source-neuron-index vector; labeled edge set; canonical topology and ordered-representation hashes; exact 200-seed vector and order; algorithm and Python/dependency/runtime-lock hashes; execution implementation/commit; Q-vector file hash and complete trial count. A matching Qmax alone is insufficient. Historical-order H3 replay (24,000 trials) is a separate identity/reproducibility cost and is not reusable as canonical baseline output. The completed 10-graph pilot is likewise reusable only to the extent its private full canonical vectors satisfy the same complete predicate.

The existing candidate 120-H3 limits (8 wall-hours, 8 process-tree CPU-hours, one worker, 4 GiB sampled RSS, 1 GiB output, and established disk/power/thermal/swap/Watchdog conditions) remain unapproved and must be re-evaluated against the expanded two-order work. The 10-graph pilot's 573.25 wall seconds and 606.34 process-tree CPU seconds are descriptive evidence from one recording and Wake only, not a reliable 120-graph upper bound. The 4-GiB RSS limit remains sampled, not hard.

## More efficient synthetic resource-calibration candidate

The current #1124 candidate can require 12,000 core null tasks (100 strata × 12 parent clusters × 10 child tasks) and up to 19,600 additional full structural-tail tasks: as many as 31,600/49,000 G0-sized tasks and 6.32 million Louvain trials, before source builds, recorder pairs and H3. That is up to 64.5% of the null workload and should not be the default resource-gate design without a demonstrated need.

A more economical candidate, still pending review and researcher selection before any timing, is:

1. Preserve the full frozen source-feature census and exact weights W_s=10M_s for the 100 (N, profile-medoid) workload strata. Keep the four synthetic graph families, all ten N values, exact registered 4E, and all 200 Louvain trials on every timed task. No task-count or seed reduction is proposed.
2. Use 4 training parent clusters plus 2 sealed holdout parent clusters per stratum initially. A parent cluster remains one independently seeded source fixture with its ten intact child null-task cost vectors. This is 400 training and 200 holdout clusters, or 6,000 fully timed null tasks / 1.2 million Louvain trials. Bootstrap parent blocks, never their ten children independently; aggregate with exact W_s, not balanced fixture counts. Freeze every fixture ID, seed, family assignment, split, bootstrap and holdout before the first timing.
3. Expand training only by exactly 2 clusters/stratum at m=6 and then m=8 if any frozen training-only CV error, N-specific underprediction, U95/median, or prediction-support rule fails. Keep two holdout blocks sealed. At m=8, any remaining instability, failed holdout, unsupported feature, or uncaptured tail is RESOURCE NO-GO; no post-holdout refit. Maximum core is 10,000 tasks / 2.0 million Louvain trials.
4. Replace the full four-family cross-product on every low/high-decile source ID with a fixed balanced tail panel: take the union of registered 10% low/high IDs for all seven predeclared descriptors within each N; give each selected source ID exactly one synthetic family by a hash-bound cyclic assignment balanced across N, descriptor and family. Add a fixed full four-family crossing only for the predeclared minimum/maximum source ID of each descriptor at each N (deduplicate IDs before counting). Maximum tail work is 4,900 tasks + 560 crossings / 1.092 million Louvain trials, rather than 19,600/3.92 million. All selected tail identities and assignments are fixed before timing and never weighted as extra biological tasks.
5. Retain every current acceptance condition or a stricter one: independent holdout evaluated once; full task and stage measurements; 4-worker production-DAG simulation; at least 95% bootstrap predictive U95 with the same failure-to-NO-GO rules; training-only predictive stability; source-build census; feature-support checks after 4E; no stress task or optimizer-work-counter exceedance beyond the predeclared tolerance; exact audit-writer overhead test. The proposal cannot pass if a high-cost tail cannot be bounded. U95 remains conditional on matched synthetic support, not a distribution-free guarantee. Do not decide that 4/2/8 is adequate from counts alone; independent review may reject it or require a larger sample before timing.
6. Stage costs separately: (a) graph reconstruction/cache, (b) 4E rewiring/connectivity/audit, (c) the full 200-trial Louvain, (d) compression/I/O/checkpoint/final verification, and (e) coordinator/worker startup and queue costs. Use recorder-on end-to-end timings for prediction. Instrument identical production executor/scheduler semantics, a global maximum of four workers across activities, and the same task dependency/order rules. Do not approximate wall time by CPU-hours divided by four. Include 4,900 observed Q trials and 9.8 million null Q trials separately in the synthetic weighted prediction; count shared graph builds once.
7. Publish two prospective outputs: resource distributions for the 980,000-observed-trial stage and the complete 10.78-million-trial G0 campaign (980,000 + 9,800,000), with separate process-tree CPU and end-to-end scheduled wall distributions, U95, medians, maxima, recovery reserve, source-build time, H3 prerequisite and benchmark expenditure. Existing G0 outer ceilings and the 1.5×U95 margin remain candidate values only; they are not approved by this amendment.

This alternative reduces maximum timed null-task sampling from 31,600 to 15,460 tasks (10,000 core + 4,900 tail + at most 560 crossings), 3.092 million Louvain trials, about 31.6% of the 49,000 null workload. Initial core plus the fixed maximum tail is 11,460 tasks / 2.292 million trials (23.4%). Compared with the current maximum 31,600 tasks, the proposed maximum is 51.1% fewer timed tasks. Source reconstruction census, H3, observed canonical baseline, paired recorder tests and full final prediction remain additional work and must be included in the cumulative benchmark cap. Actual deduplicated tail IDs may reduce these ceilings. If coverage fails at the fixed cap, report NO-GO rather than expanding opportunistically.

## Exchange-count correction and gate status

For 4,900 source graphs with E=8N, ten null repeats and 4E attempts per repeat, the verified arithmetic is 4,900 × 10 × 4 × (8N), summed over the registered graph-size distribution. Under the current inventory of 490 graphs at each of the ten N values, this is **1,797,712,000** proposals, about **1.798 billion** (not 17.98 billion). The source manifest must still verify E=8N for every graph before freezing this total.

The underlying 2026-10-09 preregistration remains unchanged until a separately dated revision is accepted. No canonical observed Q, new biological null Q, full H3 replay, G0, or T1 was run to prepare this proposal. The 10-graph historical H3 audit, old PS-A outputs, and all existing hashes remain untouched. T_PS-A remains unresolved; no new resource estimate is an accepted historical baseline. This proposal does not change RESOURCE NO-GO.

## Decisions still required

Before this amendment can become effective, the researcher and independent methods reviewer must decide whether to accept the common order policy, node-ID definition, unchanged seed vectors, finite-Q interpretation, reanalysis scope, H3 reuse predicate and more economical benchmark design. They must also resolve the revised two-order H3 budget and freeze the benchmark's sample counts, expansion/stop rules, synthetic-family assignments, U95 method, holdout acceptance, and aggregate resource/storage limits. A selected or rejected candidate must be documented before any new canonical biological Q or biological G0 null output is inspected.
