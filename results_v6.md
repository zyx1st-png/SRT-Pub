# v6 Posterior Sampling Notes

脚本：`fit_real_pipeline_v6.py`

当前实现为轻量 MCMC（RW-MH）后验采样（PyMC 不可用时的 fallback）：
- n_obs = 1600
- omega mean = 0.2921
- 95% CI = [0.2217, 0.3618]
- P(omega>0) = 1.0000
- acceptance = 0.427
- ESS ≈ 4241.5

结论：后验明显支持 `omega>0`，且链混合质量在该近似设置下可接受。

后续若安装 PyMC，可替换为 NUTS 并增加 R-hat/ESS（ArviZ）。
