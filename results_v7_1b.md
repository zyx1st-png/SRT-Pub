# v7.1b Results (friction-coupled sample generator)

数据：`data/unified_srt_mtor_v2.csv`（由 `prepare_sample_data_v2.py` 生成）
模型：`fit_real_pipeline_v7_1b.py`

- omega_hat = 0.100
- omega_mean = 0.094
- P(omega>0) = 0.960862
- alpha_hat = 0.800
- theta_hat = 0.400
- c_fric_hat = 1.000
- train LR = 27.868
- valid ΔNLL = -1.008
- test ΔNLL = +3.538

## 结论
这次 `c_fric_hat` 被显式激活（=1.0），证明摩擦项在“有摩擦耦合的数据生成机制”下可被识别。
但 valid/test 仍不均衡，说明 split 设计与生成机制之间有域偏移，需要做按 block/condition 的分层切分与重采样。
