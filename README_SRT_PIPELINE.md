# README_SRT_PIPELINE

## Overview
This workspace implements an end-to-end SRT-mTOR modeling pipeline:
- Generative modeling (Poisson + mTOR threshold + SRT weighting)
- Simulation and recovery checks
- Progressive real-pipeline fitting (v1 → v6)
- Posterior diagnostics
- Publication-ready figures and draft text

## File Map
- `srt_mtor_sim.py` — baseline simulation sweep over omega
- `fit_srt_mtor.py` — MLE recovery + LRT
- `bayes_srt_mtor.py` — two-condition Bayesian grid posterior
- `run_experiments.py` — omega/theta/sigma sweep + MI diagnostics
- `prepare_sample_data.py` — unified sample-data builder
- `fit_real_pipeline.py` — initial fitting pipeline
- `fit_real_pipeline_v2.py` — grouped split + baseline random effect proxy
- `fit_real_pipeline_v3.py` — block-normalized U + hierarchical omega
- `fit_real_pipeline_v4.py` — omics-informed priors for theta/alpha
- `fit_real_pipeline_v5.py` — hierarchical empirical-Bayes MAP
- `fit_real_pipeline_v6.py` — posterior sampling fallback (MCMC)
- `paper_figures.py` — generate manuscript figures
- `methods_ready.md` — methods/results draft

## Quick Start
```bash
uv run python srt_mtor_sim.py
uv run python fit_srt_mtor.py
uv run python bayes_srt_mtor.py
uv run python run_experiments.py
uv run python prepare_sample_data.py
uv run python fit_real_pipeline_v3.py
uv run python fit_real_pipeline_v4.py
uv run python fit_real_pipeline_v5.py
uv run python fit_real_pipeline_v6.py
uv run --with matplotlib python paper_figures.py
```

## Main Outputs
- `experiments_srt_mtor.csv`
- `data/unified_srt_mtor.csv`
- `results_real_pipeline.md`
- `results_v6.md`
- `figures/*.png`

## Repro Notes
- Current dataset is sample/unified schema mockup.
- For real deployment, replace sample data with aligned Allen + GEO/omics inputs.
- v6 currently uses RW-MH fallback; replace with PyMC NUTS when available.
