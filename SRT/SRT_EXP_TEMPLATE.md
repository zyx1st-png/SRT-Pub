---
id: SRT-EXP-TEMPLATE
type: experiment
tags: [Experiment, Template]
status: v1
layer: L2
epistemic_layer: lab
claim_mode: canonical
dependency: [SRT-LAB-HYPOTHESES, SRT-EXP-MEASUREMAP]
---

# SRT 最小实验模板（P1-2）

更新时间：2026-03-17
用途：统一 H 系列假设的可复现实验设计

> **Lab 注记**
> 本文件属于 `Lab` 层的 canonical 模板。只有被 `Governance/SRT_LAB_HYPOTHESES.md` 正式收编的条目，才视为 SRT 当前的全局硬赌点；其余快速实例仍可作为局部试验口，但不自动获得全局地位。

---

## 0. 基本信息
- 假设编号：H__
- 关联公理：Ax-__
- 研究问题：
- 研究类型：行为 / 神经 / 生理 / 社会网络 / 混合

## 1. 可证伪陈述（必须）
- 主陈述（可被否定）：
- 反证条件（满足即判定不支持）：

## 2. 样本与分组
- 样本量目标（含功效依据）：
- 纳入/排除标准：
- 分组方式（随机/匹配/分层）：

## 3. 变量定义
- 自变量（IV）：
- 因变量（DV）：
- 协变量（Covariates）：
- 代理指标与理论变量映射（如 d, Ψ_f, ii）：

## 4. 协议（Procedure）
- 阶段 A（基线）：
- 阶段 B（干预/任务）：
- 阶段 C（追踪）：
- 质量控制（attention checks / 数据清洗规则）：

## 5. 统计计划（预注册）
- 主分析模型：
- 次分析模型：
- 多重比较校正：
- 缺失值处理：
- 稳健性检验：

## 6. 结果判定
- 支持阈值：
- 不支持阈值：
- 不确定区间与解释：

## 7. 风险与伦理
- 伦理风险级别：低 / 中 / 高
- 参与者保护措施：
- 数据隐私与去标识化：

## 8. 复现包
- 数据字典：
- 代码仓库：
- 预注册链接：
- 复现说明（README）：

---

## 附：Lab 快速实例（H-IITGWT-01）
- 假设编号：`H-IITGWT-01`
- 关联命题：`T-IIT-4`
- 研究问题：在 `\Phi_proxy` 与 `B_global_proxy` 匹配时，系统是否仍会因 `\hat d_{min}` / `\hat{\Psi}_{f,min}` 不同而出现主体性相关分离？
- 研究类型：agent simulation / 行为 / 混合

### 可证伪陈述
- 主陈述：A/B/C 三组在高 `\Phi_proxy` / 高 `B_global_proxy` 匹配后，A 组应在奖励撤除后的持续性、costly-other inclusion 与恢复半衰期上显著优于 B；C 可短期接近 A，但长期回落。
- 反证条件：若匹配架构指标后，A/B/C 在上述行为与恢复指标上不分离，或分离完全可由 `\Phi_proxy` / `B_global_proxy` 单独解释，则该条不支持。

### 最小变量映射
- IV：赌注结构（真实不可逆 / 无不可逆 / 模拟不可逆）
- DV：奖励撤除后持续性、错误后恢复半衰期、跨情境关切一致性、costly-other inclusion
- 协变量：任务难度、训练预算、模型容量、`\Phi_proxy`、`B_global_proxy`
- 代理映射：`\hat d_{min}`、`\hat{\Psi}_{f,min}` 见 `SRT_EXP_MEASURE_MAP.md`

### 最小协议
- 阶段 A：训练三个 matched-architecture agent 到相近任务表现
- 阶段 B：分别施加真实不可逆、无不可逆、模拟不可逆条件
- 阶段 C：关闭外显奖励并测量持续性、恢复与自他风险权衡

### 最小判定
- 支持：在控制 `\Phi_proxy` / `B_global_proxy` 后，`\hat d_{min}` / `\hat{\Psi}_{f,min}` 仍显著预测主体性相关读出
- 不支持：主体性相关读出全部被架构指标吸收，或 A/B/C 无稳定分离

---

## 附：Lab 快速实例（H-dPsi-01）
- 假设编号：`H-dPsi-01`
- 关联命题：`T-FEP-1b`
- 研究问题：`\hat d_{min}` / `\hat{\Psi}_{f,min}` 是否在 held-out 预测上优于单纯 precision 参数？
- 研究类型：模型比较 / agent simulation / 混合

### 可证伪陈述
- 主陈述：`M2` 或 `M3` 应在 held-out 数据上稳定优于 `M0`（precision-only）与 `M1`（结构控制-only）。
- 反证条件：若 `\hat d_{min}` / `\hat{\Psi}_{f,min}` 仅提高样本内拟合，或在 held-out 预测上无稳定增量，则该条不支持。

### 最小模型集
- `M0 = precision-only`
- `M1 = \Phi_proxy + B_global_proxy`
- `M2 = precision + \hat d_{min} + \hat{\Psi}_{f,min}`
- `M3 = precision + \Phi_proxy + B_global_proxy + \hat d_{min} + \hat{\Psi}_{f,min} + \hat d \times \hat{\Psi}_f`

### 最小变量映射
- DV：奖励撤除后持续性、恢复半衰期、自他风险权衡、post-error stabilization
- 代理映射：`\hat d_{min}` / `\hat{\Psi}_{f,min}` / `\Phi_proxy` / `B_global_proxy`
- 判定重点：只看 held-out 预测，不把拟合优美当成支持

---

## 附：快速实例（H22）
- 主陈述：d 值扩展训练提升合作行为。
- IV：是否接受 d 扩展训练（是/否）
- DV：公共品博弈贡献率、背叛率
- 反证条件：训练组在主要指标上与对照组无显著差异（且效应量接近 0）。

---

## 附：快速实例（G2-OpenData-01）
- 假设编号：G2-OpenData-01
- 关联方程：`Eq-LDP-01` / `Eq-LDP-02`
- 研究问题：公开事件流与注意流是否允许把 online collective 粗粒化为 `\rho(x,t)` / `J(x,t)`，并对路径频率做 rate-function 检验？
- 研究类型：开放数据 / 社会动力学 / 混合

### 最小数据源
- Wikimedia pageviews（长期聚合注意流）
- Wikimedia EventStreams `recentchange`（实时编辑事件流）

### 变量定义
- IV：外部冲击窗口（例如 breaking news、节日、灾害、选举日）
- DV1：主题箱密度 `\rho_k(t)`
- DV2：主题箱流量 `J_k(t)`
- DV3：路径类频率 `P(\Gamma_m)`
- 协变量：总流量、昼夜周期、周内周期、机器人编辑过滤
- 代理映射：
  - `\rho_k(t)` → 粗粒化密度场
  - `J_k(t)` → 局部流量/通量代理
  - `I_{SRT}^*(\Gamma_m)` → 候选作用量 surrogate

### 协议（Procedure）
- 阶段 A（建箱）：
  - 选定有限主题箱 `K`
  - 将页面标题映射到主题箱
- 阶段 B（采集）：
  - 用 pageviews 聚合每小时 `\rho_k(t)`
  - 用 recentchange 聚合每小时 `J_k(t)`
- 阶段 C（路径）：
  - 按冲击窗口切片 24h–72h 轨迹
  - 将轨迹聚类为路径类 `\Gamma_m`
  - 估计 `\log P(\Gamma_m)` 与 `I_{SRT}^*(\Gamma_m)` 的关系

### 主分析模型
- `Eq-LDP-01`：
  - 比较 coarse-grained `\rho/J` 模型与独立 AR 基线
  - 输出：传播时滞、相关长度、谱峰/主模态
- `Eq-LDP-02`：
  - 回归 `\log P(\Gamma_m) ~ -a I_{SRT}^*(\Gamma_m) + b`

### 反证条件
- coarse-graining 后预测力不优于独立基线
- 路径类频率与 `I_{SRT}^*` 不呈稳定负相关
- 结果完全由昼夜周期与总流量解释，加入 `\rho/J` 结构后无新增解释力

### 实现挂钩
- 脚本：`scripts/g2_wikimedia_open_data_mvp.py`
- 主题映射样例：`data/g2_open_data/topic_mapping.example.json`
- 首轮样本目录：`data/g2_open_data/sample_run/`

### MVP 经验注记
- 对 bounded sample run，优先使用 `fetch-recentchanges-api`，因为 `EventStreams` 更适合长连监听而非短窗口校准。
- 若 `rho` 与 `J` 时间粒度不一致，先用 `daily` 粗粒度打通整链，再扩展到更细时间窗。
