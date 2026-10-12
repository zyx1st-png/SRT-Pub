---
id: SRT-NEURO-SLEEP-NULL-CALIBRATION-IMPLEMENTATION-DRAFT-20261011
type: readme
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: protocol
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
tags: [Neuroscience, NullCalibration, Synthetic, ReviewOnly]
---

# G0 graph-swap implementation — code review only

**Status:** review-only implementation candidate. **Not NC-0 frozen; not a validated null sampler; no RIKEN real-data integration, no biological null analysis, and no completed NC-0a mixing test.**

## Scope

- `connected_swap.py`: a standard-library-only, simple-graph **degree-preserving connected double-edge swap** candidate. Each proposal picks two distinct edge slots uniformly, chooses one cross-pairing uniformly, accepts only if simple and connected, and otherwise **rejects with a stay-put step**. It does not silently use NetworkX's windowed swap implementation.
- Local connectivity checking after a two-edge replacement stops when the four touched endpoints are mutually reachable. When `oracle=True`, the candidate checks this decision against a full-graph BFS at each tentative proposal; **only use the expensive oracle for synthetic validation**.
- Edge slots are initially sorted, and the implementation expects labeled nodes `0..n-1`. This is a **provisional internal relabeling interface**. The real-data execution contract must preserve the external neuron-ID mapping and hashes; **no relabeling to biological data is approved at this stage**.
- `test_connected_swap.py`: five small synthetic-only unit tests for rejected malformed graphs, deterministic seed replay, topology invariants, proposal accounting, and local-vs-full connectivity checking.
- `test_anomaly_screen.py`: **three additional statistics-only tests**, including a deterministic 2,500-family iid-normal toy rehearsal of the revised **48-test paired-t/Bonferroni** anomaly rule. This is *not a graph-chain convergence or mixing test*.
- `synthetic_graphs.py`: **review-only** constructors for connected ER-like, ring-preserving WS-like, BA-like and six-factor synthetic-correlation MST-plus-top-edges graphs; also computes triangles, Pearson degree assortativity and source-edge overlap. The generation algorithms are procedural approximations, **not** exact distributions of the named model families or biological correlations. Factor MST uses NumPy `Generator(PCG64)` and resolves exact equal-weight MST frontiers by canonical edge-pair lexicographic order. Generator, 8 chain streams and 16 BFS identity streams share the **synthetic-only** SHA-256 first-eight-byte seed contract in `synthetic_graphs.synthetic_seed`; the inherited **biological** `stable_seed` is not replaced.
- `test_synthetic_graphs.py`: **eight small synthetic-only tests** (five original plus three new checks for synthetic seed serialization/index rejection and canonical MST tie behavior), with N=40/48 (below the formal NC-0a sizes) testing four input families, connectivity, degree-16 edge counts where defined, deterministic fingerprints and metric edge cases. The toy rehearsal was independently replicated with a 4.48% familywise rejection rate under the ideal null, close to the nominal 5%.

- `nc0a_contract_runner.py`: review-only **case/audit/report candidate**, with O(local) audit on each accepted swap, full connectivity at declared checkpoints, all three graph metrics, paired t screening reports, independent BFS oracle trace, fixed SHA seed manifest and non-overwriting atomic JSON output. It has **no automatic full experiment launch**. No drift-screen PASS is promoted to a mixing certificate.
- `test_nc0a_contract_runner.py`: small contract-level tests for replay, strict limits, audit completeness, seed manifest, atomic output and an example of **stagnant chains passing the drift screen while remaining MIXING-UNRESOLVED**.
- [NC-0a readiness and resource evidence ledger](NC0A_READINESS_AND_RESOURCE_LEDGER_2026-10-12.md): explicitly **NO-GO** until auditable historical PS-A active-time baseline, absolute 16-case synthetic-run caps, complete runner reviews and separate NC-0 graph-reference identity prerequisites are resolved.
- `.github/workflows/neuro-null-synthetic-unit-tests.yml`: CI runs **only** the four small Python unit-test modules; it does not invoke any full synthetic battery or biological data.

## Small-unit-test verification

In the directory containing both files:

~~~sh
python -m unittest -v test_connected_swap.py test_anomaly_screen.py test_synthetic_graphs.py test_nc0a_contract_runner.py
~~~

The original five swap tests passed on **Python 3.13.5 in an isolated non-biological environment** when initially authored. Separately, the statistical toy calibration formula was exercised using a 2,500-repetition iid-normal rehearsal (familywise rejection ~4.48%). The five fixture/metrics tests passed on small synthetic N=40/48 inputs in an environment with NumPy 2.3.5. These checks are **unit tests**, not the prospective NC-0a 16-case synthetic graph battery, the original PS-A macOS arm64 / Python 3.14 / python-louvain runtime, or evidence that 4E graph rewiring has mixed. Claude R4 reported **13/13 tests passing on the previous head**; the three new seed/MST tests still need a fresh run.

## Not yet implemented / not authorized

1. No exact inherited `stable_seed` bridge, source-graph serialization/identity mapping, or version-locked runtime.
2. No G0 10×10 selected-subset orchestration, Louvain Q trials, observed-minus-null aggregation, statistical classifications, or T1 surrogate runner.
3. Four synthetic fixture generators and an **auditable single-case contract candidate** now exist, but no **authorized, budget-gated full 16-case orchestration**; no formal 8-chain × 32E graph diagnostic or 16,000-proposal BFS/full-BFS equivalence battery, no actual graph-mixing evidence, and no validated resource extrapolation. Previous small MST unit fixtures used N=40/48; **formal N=100/340/1150/3900 acceptance is not established**.
4. No formal NC-0a graph results; **do not execute NC-0a until the R5 code audit, 48-comparison and fixture contracts, archival `T_PS-A`, absolute synthetic-run caps and separate G0/T1 resource gates have independent review and prospective approval**. The paired-t screen is a drift flag only; even a passing result does not prove uniform sampling or adequate mixing.
5. No inference that a 4E chain has mixed or generated near-uniform connected fixed-degree graphs. The graph-swap implementation remains a **procedure-defined finite-length null**, not a demonstrated stationary sampler. With eight chains, the paired t screen's observed-SD-dependent detection cutoff is **1.8985 × the paired-difference SD**, not a guaranteed minimum detectable effect at a stated power.
6. Claude R4 disclosed informal synthetic trials of **4/16** cases with separate reviewer-chosen seeds; all passed. This is *prior review exposure*, **not** formal NC-0a. See prereg §6.1 for provenance; no thresholds or chain counts were adjusted after those results.

**Next gate:** independent source review of the code/protocol equivalence and synthetic-only NC-0a validation specification. Any changes are prospective to new null outputs. Do not merge or call the protocol frozen merely because the unit tests pass.
