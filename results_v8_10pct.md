# v8 Results (condition-id observer, 10% multi-session)

Data: `data/unified_srt_mtor_real_multi_condid_10pct.csv`
Model: `fit_real_pipeline_v8.py`

- omega_m1 = 0.2000
- omega_m2 = 0.2000
- c_fric_m2 = 0.000
- train_LR_M1 = 491.905
- train_LR_M2 = 491.905
- train_LR_M2vsM1 = 0.000
- valid dNLL_M1 = +156.080
- test  dNLL_M1 = +117.124
- valid dNLL_M2vsM1 = 0.000
- test  dNLL_M2vsM1 = 0.000

## Readout
在 condition-id 精细化后，M1（含 omega）在 valid/test 均显著优于 M0，方向恢复为稳定正向。
M2 未优于 M1，说明当前 Ψ_f 代理仍未提供额外信息。
