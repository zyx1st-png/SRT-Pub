# Minimal Costly-Selection Pilot

Symmetric two-agent environment with shared-policy REINFORCE, 700 training episodes with mutual-cooperation bonus, followed by 120 online adaptation episodes after bonus withdrawal.

| Regime | d_eff | Baseline mutual cooperation | Post-withdrawal mutual cooperation | Persistence episodes |
|---|---:|---:|---:|---:|
| real | 1.90 ± 0.23 | 0.58 ± 0.27 | 0.62 ± 0.28 | 100.2 ± 44.3 |
| resettable | 1.83 ± 0.34 | 0.51 ± 0.25 | 0.54 ± 0.29 | 100.2 ± 44.3 |
| simulated | 1.57 ± 0.16 | 0.28 ± 0.40 | 0.29 ± 0.41 | 42.3 ± 55.0 |
