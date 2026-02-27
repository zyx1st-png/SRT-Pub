# Dataset Manifest for SRT-mTOR Pipeline

## 目标
把多源数据统一成可直接喂给 `fit_real_pipeline.py` 的表结构。

---

## A. Unified Schema (`data/unified_srt_mtor.csv`)

每行对应一个时间 bin（建议 50ms）。

- `dataset_id`：数据来源标识（allen_vcnp / GSE286175 / GSE247367）
- `subject_id`：受试体/样本 id
- `session_id`：记录会话 id（分子组学可用 batch id）
- `circuit_id`：神经元/回路标识（组学样本可填 `bulk`）
- `t_sec`：时间（秒）
- `dt_sec`：bin 宽度（秒）
- `spike_count`：该 bin 放电计数（无时序组学可置空）
- `x_mtor_proxy`：mTOR 状态代理（0~1 归一化）
- `u_observer`：SRT 观测算子值 U(t)
- `condition`：实验条件（baseline/stim/tsc2_variant 等）
- `split`：train/valid/test

---

## B. 数据源到字段映射

### 1) Allen Neuropixels
- 原始：spike times / units / stimulus
- 映射：
  - `spike_count` <- spike times 按 bin 计数
  - `u_observer` <- 由任务块/刺激标签映射（如 preferred stimulus = 1, else 0）
  - `x_mtor_proxy` <- 暂缺时可用 NaN（后续由组学先验补充）

### 2) GSE286175（mTOR/TOP mRNA）
- 原始：表达矩阵（样本级）
- 映射：
  - `x_mtor_proxy` <- mTOR/TOP 基因集打分（ssGSEA 或 z-score 聚合）
  - `u_observer` <- 样本标签导出（synaptic localization 指标可映射）
  - `spike_count` <- NaN

### 3) GSE247367（TSC2 bulk RNA-seq）
- 原始：bulk RNA-seq
- 映射：
  - `x_mtor_proxy` <- TSC/mTOR 通路签名分数
  - `condition` <- WT vs TSC2_variant
  - `spike_count` <- NaN

---

## C. 最小融合策略（当前阶段）

1. 用 Allen 建立时序放电主模型（N(t), U(t)）
2. 用 GSE286175/GSE247367 给 `theta/alpha` 设置先验范围
3. 在拟合中做：
   - `theta ~ N(mu_theta_from_omics, sigma_theta)`
   - `alpha ~ N(mu_alpha_from_omics, sigma_alpha)`

这能避免把阈值参数错误吸收进 omega。

---

## D. 目录约定

- `data/raw/allen/`
- `data/raw/GSE286175/`
- `data/raw/GSE247367/`
- `data/processed/`
- 输出：`data/unified_srt_mtor.csv`

---

## E. 版本说明

v0：先用样例数据跑通结构与代码。
v1：接入真实下载与解析。
