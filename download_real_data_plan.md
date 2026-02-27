# Download Plan (Real Data for SRT Pipeline)

## 目标
拉取最小可运行的真实数据子集，替换当前模拟数据。

- 神经放电主线：Allen Neuropixels → `N(t)`
- mTOR组学先验：GEO GSE286175 / GSE247367 → `x_mtor_proxy` 先验

---

## A. Allen Neuropixels（优先）

### 入口
- Docs: https://allensdk.readthedocs.io/en/latest/visual_coding_neuropixels.html

### 最小下载策略
1. 安装依赖（临时）
   - `uv run --with allensdk python -c "import allensdk; print('ok')"`
2. 拉一个 session 的 unit + spike_times + stimulus table
3. 输出 `data/raw/allen/session_<id>/...`

### 目标字段
- `unit_id`
- `spike_times`
- `stimulus_id / block / trial`
- `session_id`

### 转换
- bin=50ms，得到 `spike_count`
- 用 stimulus block 构建 `u_observer`

---

## B. GEO（mTOR）

### 1) GSE286175
- URL: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286175
- 目标：提取表达矩阵中 mTOR/TOP 基因集分数

### 2) GSE247367
- URL: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE247367
- 目标：提取 WT vs TSC2_variant 条件下 mTOR proxy 分布

### 最小下载策略
1. 先下 series matrix / supplemental csv
2. 提取样本注释 +表达矩阵关键列
3. 计算 proxy：基因集 z-score（后续可换 ssGSEA）

---

## C. 统一落地目录

- `data/raw/allen/`
- `data/raw/GSE286175/`
- `data/raw/GSE247367/`
- `data/processed/`
- 输出：`data/unified_srt_mtor_real.csv`

---

## D. 质量门槛（必须满足）

1. `spike_count` 非空行 > 50k
2. 至少 2 个 session / block 条件
3. mTOR proxy 有明确条件差异（effect size > 0.3）
4. `u_observer` 不与 split 泄漏

---

## E. 执行顺序

1. 先 Allen 拉最小 session 跑通 pipeline
2. 再并入 GEO 先验
3. 最后跑 v4/v5/v7.1 比较（是否激活 `c_fric`）
