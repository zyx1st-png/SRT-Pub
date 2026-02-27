# v7.1 Results (hazard-like Ψ_f)

脚本：`fit_real_pipeline_v7_1.py`

- omega_hat = 0.225
- omega_mean = 0.226
- P(omega>0) = 0.999981
- alpha_hat = 0.400
- theta_hat = 0.600
- c_fric_hat = 0.000
- train LR = 31.447
- valid ΔNLL = +9.052
- test ΔNLL = +9.901

结论：hazard-like Ψ_f 代理在当前样例数据上仍未被激活（c_fric=0）。说明数据生成机制未包含可辨识摩擦动态，而非 SRT 主项消失。
