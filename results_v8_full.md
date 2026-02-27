# v8 Results (condition-id observer, FULL multi-session)

Data: `data/unified_srt_mtor_real_multi_condid.csv` (300,000 rows)
Model: `fit_real_pipeline_v8.py`

- omega_m1 = 0.2000
- omega_m2 = 0.2000
- c_fric_m2 = 0.000
- train_LR_M1 = 4049.643
- train_LR_M2 = 4049.643
- train_LR_M2vsM1 = 0.000
- valid dNLL_M1 = +1956.734
- test  dNLL_M1 = +1184.516
- valid dNLL_M2vsM1 = 0.000
- test  dNLL_M2vsM1 = 0.000

## Readout
在全量 5-session 真实数据上，M1（含 omega）相对 M0 持续稳定正向提升（train/valid/test 全正，且量级显著）。
M2 不优于 M1，说明当前 Ψ_f 代理在该数据与建模尺度下仍未提供额外解释力。
