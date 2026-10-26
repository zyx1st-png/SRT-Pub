---
id: SRT-H3-120-SCIENTIFIC-CLOSURE-20261026
type: experiment-result
status: draft
record_stage: verified-result-archive-awaiting-review
date: 2026-10-26
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/neuro_sleep_null_calibration/H3_120_PUBLIC_CLOSURE_2026-10-26.json
  - Experiments/neuro_sleep_null_calibration/G0_CANONICAL_Q_ORDER_PROSPECTIVE_AMENDMENT_DRAFT_2026-10-23.md
tags: [RIKEN, H3, Closure, Reproducibility, CanonicalQ]
---

# Fixed H3-120 scientific closure

**H3 SCIENTIFIC CLOSURE: PASS. CORRCOEF WARNING: IMPACT-BOUNDED.** This is an archive of the completed fixed-panel experiment, not a new experiment authorization. The JSON projection contains aggregate statistics, input/result identity hashes and audit anchors only. The original signal, jobs, authorization package, full Q vectors and audit files remain in their existing private locations and were not rewritten.

## Identity and verification

| Identity | Value |
|---|---|
| Run UUID | `e6abc8fd-831f-4076-b412-e5a7481a027b` |
| Executed HEAD | `147d5ca268ef0c579c41f314a6f5e5ec8cafc6d2` (#1130) |
| Packet SHA-256 | `669cc9148cb92e1d6bd57dce5276fe8ecdbda04bb7b35c2c9dbeef32a1875a4a` |
| Source inventory SHA-256 | `6a8357ac0b815c434421a31dc6c294c292b5c144713f49c52b5344038235ece2` |
| Effective method SHA-256 | `c0cf7f85a18bad844e190deefbe83e8ab55f0dbe194299be0ef94e2c828e38c3` |
| Summary SHA-256 | `201cd095b87462a8f74f743a54c59733c229725ff184f27cb94fef830939e6c8` |
| Public closure JSON SHA-256 | `f3079612e1e7946cd000ec9c73c085371b7544e6a47d452ca82e0de244fe18d7` |

The official recovery verifier was run read-only against the completed private directory and host ledger: `VERIFIED_TERMINAL`, 120/120 row artifacts verified, full ordered panel completed, `resume_allowed=false`. The public projection preserves the three verified hash-chain tips and hashes of the manifest, summary, runner terminal, stdout, evidence, control and Watchdog files, plus each row artifact hash. The closure script independently checks recorded Q vectors/maxima/first-maximum indices through the official verifier and computes the aggregate statistics. It does **not** independently rerun Louvain.

All 120 source identities and historical-order Q replays pass. All 24,000 archived historical Q values are exactly reproduced; the maximum absolute difference is zero, and all 120 Qmax values and first-maximum indices agree. All 24,000 canonical trials were newly computed in the H3 run: no legacy sorted-edge diagnostic or prior ten-graph trial was credited as canonical cache. The graph identity reference is faithfully reconstructed from hash-bound sources/code/subsets; historical edge lists were not archived. Historical SciPy and h5py/HDF5 versions remain incompletely documented even though these 120 historical Q vectors replay exactly in the locked candidate environment.

The six recordings are five animal lineages, including both mouse04 sessions. The fixed panel has one graph per recording × state × finite N: 60 Wake, 60 NREM, twelve graphs at each of ten N values. This is fixed-panel verification, not a population-level replication or biological hypothesis test.

## Canonical versus historical Q

Define ΔQmax = canonical Qmax_200 − historical Qmax_200. Positive/negative/zero counts are 60/48/12; mean +0.0001254502, median +0.0000002836, range −0.0027588397 to +0.0036177083. Qmax differs for 108/120 graphs; the first-max index matches in 21/120. Of 24,000 paired trial values, 19,675 differ; median absolute difference is 0.0005328064 and maximum absolute difference 0.0380954861.

| N | ΔQmax mean | ΔQmax median | + / − / zero |
|---:|---:|---:|---:|
| 100 | +0.00019355 | 0 | 5 / 1 / 6 |
| 150 | +0.00058533 | +0.00013438 | 7 / 2 / 3 |
| 225 | +0.00041142 | +0.00013835 | 9 / 3 / 0 |
| 340 | −0.00057755 | −0.00025820 | 1 / 8 / 3 |
| 510 | +0.00046667 | +0.00027438 | 7 / 5 / 0 |
| 765 | +0.00016506 | +0.00019364 | 8 / 4 / 0 |
| 1150 | +0.00000089 | −0.00000254 | 6 / 6 / 0 |
| 1725 | +0.00003318 | −0.00002570 | 5 / 7 / 0 |
| 2600 | +0.00000944 | +0.00003640 | 8 / 4 / 0 |
| 3900 | −0.00003350 | −0.00002726 | 4 / 8 / 0 |

Wake mean/median are +0.00005456 / 0 (26/28/6); NREM +0.00019634 / +0.00003087 (34/20/6). The JSON includes signed distributions by all six recordings, states and N. These are descriptive diagnostics of a finite, order-sensitive optimizer. No additional significance test, result-based threshold, seed selection or sample substitution was performed. Canonical order makes the representation fixed; it does not establish a global modularity optimum or eliminate all heuristic sensitivity.

## corrcoef warning

Stdout contains four NumPy divide-warning lines; warning filtering means these are not a count of affected graphs. A read-only constant-signal audit of the fixed inputs, without correlation reconstruction, graph building or Louvain, confirms 97 affected graphs and 997 graph-neuron zero-variance instances. Deduplication by source, state, exact frame-vector identity and original neuron gives **859 unique neuron-window combinations**, across **37 affected windows** of the 40 distinct source windows represented in H3. Raw selected inputs contain no NaN/Inf. Counts and hashes are public; no raw values or neuron IDs are exported.

Zero variance produces undefined Pearson correlations. Both historical PS-A and H3 use the same `corrcoef → nan_to_num(nan=0, posinf=0, neginf=0) → diagonal=0 → abs` rule. Replacing undefined correlations with zero is an inherited modeling choice that can affect tied MST/top-edge decisions. Exact historical replay bounds its impact on this reproducibility result; it does not prove the choice is biologically innocuous. No channel was excluded and no completed artifact was changed.

## Resource observations and limits

Recorded wall: 6,269.350 seconds; accounted process-tree/controller CPU: 6,479.524 seconds. One compute worker; sampled RSS maximum 2,033,582,080 bytes (1.89 GiB), not a true peak or hard limit. The Watchdog exit storage sample is 5,135,178 bytes, including its 1-MiB emergency scratch reserve. After reserve cleanup and terminal/control writes, the actual closed-directory file-byte total is 4,091,123 bytes; row artifacts are 2,646,611 bytes; 1,148 resource samples. Data/VM minimum sampled free space was about 44.56 GiB each (shared APFS capacity, not additive); free-memory percentage minimum 33%; Swap growth about 0.617 GiB, with current-pool free Swap as low as about 275 MiB. AC, thermal and sleep-assertion conditions remained acceptable under the adopted policy.

H3 row times combine source loading, reconstruction, both 200-Q orders, checks and recording. Per-phase read bytes and per-row true RSS peaks were not measured. They cannot supply a validated total-cost upper bound for 4,900 observed graphs. The historical `T_PS-A` remains unresolved. NC-0a retains `MIXING-UNRESOLVED`; G0/T1 remain RESOURCE NO-GO.

## Archive reproduction

`h3_120_closure.py` requires explicit private run/source roots and a new output file outside the old run. It calls the existing recovery verifier, reads existing result vectors and performs only a constant/variance/nonfinite source audit. It never writes to the completed run and contains no Louvain execution call. This public JSON is a hashable projection, not an independent backup or tamper-proof custody service.
