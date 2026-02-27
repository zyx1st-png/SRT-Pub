# Methods + Results (ready-to-paste draft)

## Methods (core model)
We modeled spike counts in bins \(\Delta t\) as:
\[
N(t) \sim \text{Poisson}(\mu(t)),\quad
\mu(t)=\lambda^{(0)}(t)\exp(\omega U(t))\Delta t.
\]
The baseline intensity was mTOR-threshold gated:
\[
\lambda^{(0)}(t)=\lambda_{base}+\alpha\,\sigma(k(x(t)-\theta)),
\]
where \(\sigma\) is logistic, \(x(t)\) is an mTOR proxy state, \(\theta\) threshold, and \(\alpha\) gain.

We estimated parameters with progressively stronger constraints:
- v2: grouped split + circuit-specific baseline effects.
- v3: block-wise observer normalization + hierarchical \(\omega\).
- v4: omics-informed priors on \(\theta,\alpha\) with joint modulation.
- v5: empirical-Bayes hierarchical MAP over block/circuit parameters.
- v6: posterior sampling for \(\omega\) (MCMC fallback in current environment).

Primary readouts:
1) likelihood-ratio statistic against \(\omega=0\),
2) out-of-sample \(\Delta\mathrm{NLL}=\mathrm{NLL}_{null}-\mathrm{NLL}_{model}\),
3) posterior probability \(P(\omega>0)\),
4) permutation control on observer \(U\).

## Results (current sandbox run)
- v3: train LR=31.816, valid \(\Delta\mathrm{NLL}=+8.536\), test \(\Delta\mathrm{NLL}=+9.765\), \(P(\mu_\omega>0)\approx1\).
- v4 (with omics priors): train LR=31.239, valid \(+8.679\), test \(+9.555\), \(P(\omega>0)=0.9982\).
- v5 (hierarchical shrinkage): train LR=32.036, valid \(+8.056\), test \(+8.991\), \(P(\mu_\omega>0)=0.9409\).
- v6 posterior sampling: \(\omega\) mean=0.2921, 95% CI=[0.2217, 0.3618], \(P(\omega>0)=1.000\), ESS≈4241.5.

Interpretation: selective weighting remains positive under increasingly conservative parameterizations, with stable out-of-sample gains after v3, supporting a non-zero SRT weighting effect.

## Limitations
- Current \(x(t)\) still uses a bridge proxy in the neural stream.
- Full NUTS/HMC diagnostics (R-hat, rank plots) require PyMC/ArviZ stack installation.
- Cross-dataset integration is currently weakly-coupled (not yet fully time-aligned multimodal recording).

## Next technical step
Run full Bayesian inference (NUTS) with real aligned \(x(t)\), session/block metadata, and multimodal priors to quantify posterior coupling among \(\omega,\theta,\alpha\).
