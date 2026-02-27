# RESULTS_SUMMARY

## Core Claim Check
SRT weighting parameter omega remains positive under progressively stricter models.

## Key Numbers
- v3: train LR=31.816, valid ΔNLL=+8.536, test ΔNLL=+9.765
- v4: train LR=31.239, valid ΔNLL=+8.679, test ΔNLL=+9.555, P(omega>0)=0.9982
- v5: train LR=32.036, valid ΔNLL=+8.056, test ΔNLL=+8.991, P(mu_omega>0)=0.9409
- v6 posterior sampling: omega mean=0.2921, 95% CI=[0.2217, 0.3618], P(omega>0)=1.0000, ESS≈4241.5

## Interpretation
- Generalization is consistently positive from v3 onward.
- Hierarchical shrinkage reduces overconfidence but does not eliminate omega>0 signal.
- Posterior interval in v6 excludes 0 by a clear margin.

## Current Limitation
- Neural stream still uses proxy bridge for x(t), not fully time-aligned multimodal mTOR measurements.
