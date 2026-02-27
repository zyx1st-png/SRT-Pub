# Real Multi-session 10% Benchmark

Data: `data/unified_srt_mtor_real_multi_10pct.csv` (30,000 rows)

## v5
- mu_omega = 0.026
- P(mu_omega>0) = 0.629330
- train LR = 300.387
- valid ΔNLL = -132.317
- test ΔNLL = -113.656

## v7.1
- omega_hat = 0.000
- P(omega>0) = 0.047417
- c_fric_hat = 0.000
- train LR = 42.477
- valid ΔNLL = -57.978
- test ΔNLL = -40.600

## Readout
在多 session 10% 快速基准上，SRT 主项目前未表现出稳定正向泛化（valid/test均为负），且 Ψ_f 项仍未激活。
