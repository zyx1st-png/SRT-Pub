---
id: SRT-EXP-CYCLE1-SHUFFLED-WRITEBACK-V2
type: experiment
status: active
date: 2026-09-05
layer: meta
epistemic_layer: lab
claim_mode: experiment
canonical: false
ai_do_not_use_for_definition: true
---

# Cycle 1 shuffled-writeback formation-time test

Specification and preregistered verdicts:
`Operations/Proposals/SRT_AUTHOR_REENTRY_CYCLE1_SHUFFLED_WRITEBACK_MODEL_V2_2026-09-05.md`.
One treatment contrast only: stable versus shuffled source-to-locus writeback
through matched recurrent dynamics. A common erasure of fast action bias is the
measurement challenge. Stored history reconstructs that bias without new evidence.

Run from repository root with Python 3.10+ (standard library only):

```bash
uv run python Experiments/cycle1_shuffled_writeback_v2/run_shuffled_writeback.py --output /tmp/cycle1-shuffle-results.json
```

After the reference run is committed:

```bash
uv run python Experiments/cycle1_shuffled_writeback_v2/run_shuffled_writeback.py --check Experiments/cycle1_shuffled_writeback_v2/reference_results.json
```

The runner checks bijective evidence delivery, equal per-locus write counts,
matched recurrent state graphs, no new probe evidence, analytical recovery,
and state-by-state equivalence to an independently implemented ordinary
delta-rule recurrent predictor. A baseline mismatch aborts as an implementation
error. No metric or seed selection is exposed as a command-line option.

`config.json` fixes the sole primary readout, 64 seeds, parameters, bootstrap
and decision threshold. Reference JSON retains per-seed scores and descriptive
curves, input/routing hashes, config/runner hashes and numerical control checks.
Curves cannot rescue a null primary result. The supplied loci and action-bias
recovery do not establish S2/S3 Bearer genesis or biological self-reconstitution.
