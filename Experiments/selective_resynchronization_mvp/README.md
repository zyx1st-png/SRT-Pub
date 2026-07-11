# Selective Resynchronization Fashion-MNIST MVP

This directory implements the locked `A -> B -> C` experiment specified in
`papers/selective_resynchronization/06_mvp_spec_lock.md`.

The scientific target is narrow: test whether an A/B-only `SR_preC` score adds
prediction of C-stage retained adaptability after controlling B-stage current
performance. Fisher burden is a candidate predictor, not the construct.

## Environment

```bash
uv venv .venv --python 3.12
uv pip install --python .venv/bin/python -r requirements.txt
```

The runtime selects CUDA, MPS, or CPU in that order when `device: auto`; every
script also accepts `--device cpu|mps|cuda|auto`.

## Locked order

```bash
uv run --python .venv/bin/python scripts/run_smoke.py
uv run --python .venv/bin/python -m pytest tests -q
uv run --python .venv/bin/python scripts/run_pilot.py --stage all
uv run --python .venv/bin/python scripts/run_locked_mvp.py
uv run --python .venv/bin/python scripts/analyze_locked_mvp.py
```

`run_pilot.py` computes standardization constants from pilot A/B artifacts
before it runs pilot C. `run_locked_mvp.py` refuses to start unless the spec,
configuration, A/B standardizers, state thresholds, split IDs, and code tree
are hashed in a formal manifest.

## Leakage boundary

Each formal run is split into two operations:

1. train/evaluate A and B, write `preC_features.parquet`, hash it, and make it
   read-only;
2. verify that hash, construct C loaders, and run C.

The primary pre-C function accepts an `ABArtifacts` schema with no C field.
The analysis re-verifies the frozen hash and timestamps before merging with
`C_outcomes`.

## Outputs

Run-level data live under `outputs/raw/`. Collated data, figures, manifests,
and analysis tables live in their corresponding output subdirectories. Smoke
and pilot artifacts are never included in confirmatory inference.
