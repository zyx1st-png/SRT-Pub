# Real Benchmark (stimulus-informed u_observer)

Data: `data/unified_srt_mtor_real_stim.csv` (Allen session 715093703)
Builder: `rebuild_real_with_stimulus_u.py`

## v4
- omega_hat = 0.000
- P(omega>0) = 0.000000
- train LR = 189.199
- valid ΔNLL = -245.259
- test ΔNLL = +267.738

## v5
- mu_omega = -0.084
- P(mu_omega>0) = 0.148180
- train LR = 829.686
- valid ΔNLL = +162.911
- test ΔNLL = +2990.185

## v7.1
- omega_hat = 0.000
- P(omega>0) = 0.000000
- c_fric_hat = 0.000
- valid ΔNLL = -245.259
- test ΔNLL = +267.738

## Readout
- 用 stimulus table 重构 `u_observer` 后，模型表现出现更强的分割不稳定（valid/test 方向冲突）。
- v5 仍给出高增益，但 `mu_omega` 偏负，说明层级项在吸收结构性变异而非支持正向 SRT 权重。
- 当前单 session + 少量 unit 设置下，结论依赖分割方式，不可用于理论定论。

## Next action
1. 扩展到多 session（>=5）并按 session 分层切分
2. 使用真实 stimulus condition 编码 + cross-session standardization
3. 再评估 omega / Psi_f 的方向稳定性
