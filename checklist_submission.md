# checklist_submission

## Data
- [ ] Replace sample unified CSV with real aligned datasets
- [ ] Verify session/block metadata integrity
- [ ] Document preprocessing and exclusion criteria

## Model
- [ ] Run v3/v4/v5/v6 on real data
- [ ] Confirm valid/test ΔNLL remain > 0
- [ ] Re-check permutation significance
- [ ] Sensitivity analysis for bin size (10/50/100ms)

## Bayesian Diagnostics
- [ ] Upgrade v6 to PyMC NUTS
- [ ] Report R-hat, ESS, trace plots
- [ ] Inspect posterior correlations (omega-theta-alpha)

## Figures/Tables
- [ ] Regenerate all figures with real data
- [ ] Add table of priors and posterior summaries
- [ ] Add model comparison table (null vs v3/v4/v5/v6)

## Writing
- [ ] Finalize methods with dataset accession details
- [ ] Add limitations and falsifiability section
- [ ] Add reproducibility statement (code + environment)

## Final QA
- [ ] One-command reproduction script succeeds
- [ ] All referenced files exist
- [ ] Git clean state + tagged release
