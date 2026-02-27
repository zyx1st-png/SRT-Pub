# v7 Results (explicit Ψ_f + L2 state proxy)

脚本：`fit_real_pipeline_v7.py`

## Result
- omega_hat = 0.225
- omega_mean = 0.226
- P(omega>0) = 0.999981
- alpha_hat = 0.400
- theta_hat = 0.600
- c_fric_hat = 0.000  (Ψ_f coefficient)
- train LR = 31.447
- valid ΔNLL = +9.052
- test ΔNLL = +9.901

## Interpretation
- 泛化依然稳定（valid/test 双正）。
- 但 `c_fric_hat=0` 说明当前 Ψ_f 代理（|u_z - L2_rigidity|）没有提供额外解释力。
- 下一步要更换 Ψ_f 的构造（建议：预测误差导数或跨步能量耗散代理）。
