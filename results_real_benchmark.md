# Real Benchmark (Allen session 715093703)

Data: `data/unified_srt_mtor_real.csv` (~60k neural rows)
Runner: `run_real_benchmark.py`

## v4
- omega_hat = -0.050
- P(omega>0) = 0.000000
- train LR = 1.427
- valid ΔNLL = -0.701
- test ΔNLL = -9.273

## v5
- mu_omega = -0.122
- P(mu_omega>0) = 0.062854
- train LR = 205.128
- valid ΔNLL = +52.179
- test ΔNLL = +29.570

## v7.1
- omega_hat = +0.025
- P(omega>0) = 0.701354
- c_fric_hat = 0.000
- train LR = 1.708
- valid ΔNLL = -0.439
- test ΔNLL = -9.055

## Readout
- 在真实 Allen 最小数据上，v4/v7.1 的 SRT 主项目前不稳（接近 0 或偏负）。
- 仅 v5（层级收缩）表现出明显泛化增益，但其 `mu_omega` 仍偏负，说明目前 `u_observer` 构造与真实刺激结构尚未对齐。
- `c_fric_hat=0` 说明这批真实数据+当前代理下，Ψ_f 仍不可识别。

## Priority fix
1. 用真实 stimulus table 重构 `u_observer`（不要用时间占位）
2. 按 stimulus condition + block 分层切分
3. 再做 v5/v7.1 对比验证
