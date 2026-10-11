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

## Small-unit-test verification

In the directory containing both files:

~~~sh
python -m unittest -v test_connected_swap.py
~~~

The five tests were run successfully on **Python 3.13.5 in an isolated non-biological environment** when initially authored. This is not the original PS-A macOS arm64 / Python 3.14 / python-louvain environment and is **not evidence of reproducibility of the original Louvain Q**.

## Not yet implemented / not authorized

1. No exact inherited `stable_seed` bridge, source-graph serialization/identity mapping, or version-locked runtime.
2. No G0 10×10 selected-subset orchestration, Louvain Q trials, observed-minus-null aggregation, statistical classifications, or T1 surrogate runner.
3. No 12-case synthetic generator / 8-chain 32E diagnostic, 12,000-proposal equivalence battery, mixing measurements, or resource extrapolation.
4. No NC-0a results; **do not execute NC-0a until the acceptance standards in the preregistration are independently reviewed and frozen**.
5. No inference that a 4E chain has mixed or targets a uniform connected fixed-degree graph distribution.

**Next gate:** independent source review of the code/protocol equivalence and synthetic-only NC-0a validation specification. Any changes are prospective to new null outputs. Do not merge or call the protocol frozen merely because the unit tests pass.
