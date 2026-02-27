# Real Pipeline Results (v2, grouped split)

运行脚本：`fit_real_pipeline_v2.py`

## 指标说明
- `omega_hat`: 训练集最优 \(\omega\)
- `p_omega_gt_0`: 近似后验 \(P(\omega>0)\)
- `train_lr`: LRT 统计量（\(\omega=0\) vs \(\omega=\hat\omega\)）
- `valid_delta_nll`: \(\Delta NLL = NLL_{null}-NLL_{hat}\)（>0 为支持）
- `test_delta_nll`: 同上
- `perm_p`: 置换检验 p-value（越小越好）

## 解释模板
1. 若 `p_omega_gt_0 > 0.95` 且 `train_lr` 明显>0，说明训练集存在 SRT 观测权重信号。
2. 若 `valid_delta_nll` 与 `test_delta_nll` 均>0，说明可泛化；
   若一正一负，优先怀疑 U(t) 设计或分组切分不充分。
3. 若 `perm_p < 0.05`，说明 U(t) 的信息不是随机偶然。

## 本次运行结果（样例数据）
- omega_hat = 0.200
- omega_mean = 0.210
- P(omega>0) = 0.998931
- train LR = 10.586
- valid ΔNLL = +2.306
- test ΔNLL = -1.254
- permutation p = 0.0123

## v3 结果（session-block 标准化 + 层级 omega）
运行脚本：`fit_real_pipeline_v3.py`

- mu_omega_hat = 0.275
- mu_omega_mean = 0.286
- P(mu_omega>0) = 1.0000
- train LR = 31.816
- valid ΔNLL = +8.536
- test ΔNLL = +9.765

解释：相较 v2，v3 在 valid/test 同时转正，说明“U 的跨组可迁移性”明显改善。

## v4 结果（引入 theta/alpha 先验 + mTOR 联合项）
运行脚本：`fit_real_pipeline_v4.py`

- omics prior: theta~N(0.604,0.102), alpha~N(1.127,0.400)
- omega_hat = 0.175
- theta_hat = 0.600
- alpha_hat = 0.800
- P(omega>0) = 0.9982
- train LR = 31.239
- valid ΔNLL = +8.679
- test ΔNLL = +9.555

解释：在加入 mTOR 先验收缩后，omega 略降但仍显著为正，且泛化保持双正，说明“阈值参数解释力”与“SRT 权重解释力”被更干净地拆分。

## 下一步
- 用真实 Allen session/block 做分层切分（而非样例）
- 用真实 mTOR proxy 替代 latent x_hat(sigmoid(u_z))
- 在 v5 做完整层级贝叶斯（mu_omega, sigma_omega, theta_i, alpha_i 联合后验）
