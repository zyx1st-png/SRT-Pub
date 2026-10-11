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
- `test_anomaly_screen.py`: **three additional statistics-only tests**, including a deterministic 2,500-family iid-normal toy rehearsal of the revised **48-test paired-t/Bonferroni** anomaly rule. This is *not a graph-chain convergence or mixing test*. The toy rehearsal was independently replicated with a 4.48% familywise rejection rate under the ideal null, close to the nominal 5%.

## Small-unit-test verification

In the directory containing both files:

~~~sh
python -m unittest -v test_connected_swap.py test_anomaly_screen.py
~~~

The original five swap tests passed on **Python 3.13.5 in an isolated non-biological environment** when initially authored. Separately, the statistical toy calibration formula was exercised using a 2,500-repetition iid-normal rehearsal (familywise rejection ~4.48%); the new automated test file is provided for subsequent reruns. Neither check is the prospective NC-0a **synthetic graph** battery, the original PS-A macOS arm64 / Python 3.14 / python-louvain runtime, or evidence that 4E graph rewiring has mixed.

## Not yet implemented / not authorized

1. No exact inherited `stable_seed` bridge, source-graph serialization/identity mapping, or version-locked runtime.
2. No G0 10×10 selected-subset orchestration, Louvain Q trials, observed-minus-null aggregation, statistical classifications, or T1 surrogate runner.
3. No **16-case** synthetic generator (4 node sizes × ER / WS / BA / synthetic-correlation MST-plus-top-edges), 8-chain × 32E graph diagnostic, **16,000-proposal** connectivity equivalence battery, actual graph-mixing evidence, or resource extrapolation.
4. No NC-0a graph results; **do not execute NC-0a until the revised 48-comparison rule, synthetic generators, and separate G0/T1 resource gates have independent review and prospective approval**. The paired-t screen is a drift flag only; even a passing result does not prove uniform sampling or adequate mixing.
5. No inference that a 4E chain has mixed or generated near-uniform connected fixed-degree graphs. The graph-swap implementation remains a **procedure-defined finite-length null**, not a demonstrated stationary sampler.

**Next gate:** independent source review of the code/protocol equivalence and synthetic-only NC-0a validation specification. Any changes are prospective to new null outputs. Do not merge or call the protocol frozen merely because the unit tests pass.
