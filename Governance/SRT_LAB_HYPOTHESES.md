---
id: SRT-LAB-HYPOTHESES
type: experiment
tags: [Lab, Hypothesis, Falsification, Protocol]
status: active_v1
layer: L2
epistemic_layer: lab
claim_mode: hypothesis
dependency: [SRT-POSITIONING, SRT-CLIN-00, SRT-CLIN-02, SRT-EXP-TEMPLATE, SRT-EXP-MEASUREMAP]
---

# SRT Lab Hypotheses

## 0. 角色说明

本文件定义的是 **SRT 全局层面的 Lab 硬赌点组合**，不是全库所有 `H-` 条目的总收集。

- 只有被收进本文件的条目，才视为当前 SRT 愿意在全局层面下注的 choke points。
- 其他领域文档中的 `H-` 条目，默认仍是局部假设、探索窗口或待压缩命题，除非后续被正式导入这里。
- 单条 Lab 失败时，默认先削弱该条目本身，不自动回卷为 `OS` 或 `Bridge` 全盘失败。

---

## 1. 纳入规则

一个命题只有同时满足以下条件，才应进入全局 Lab 组合：

1. 必须写清楚**对手基线**，而不是只写 SRT 自己的预测。
2. 必须给出**最小 proxy 组合**，避免命题停留在纯概念层。
3. 必须给出**降级触发条件**，输了要知道往哪一层退。
4. 必须挂到至少一个**实验模板或协议入口**。

---

## 2. 当前硬赌点组合

### H-IITGWT-01: High-\(\Phi\) / High-Broadcast / Low-\(d\) Insufficiency

- **Bridge 来源**：`Neuroscience/SRT_Clin_00_IIT_PCI.md` 的 `T-IIT-4`
- **核心问题**：高整合与高广播是否足以推出 stake-bearing subjectivity？
- **最小设计**：A/B/C 三组 matched-architecture agent 范式
  - A：具身 + 不可逆损失 + 合作依赖
  - B：同等架构 + 可无损重启 / 无不可逆损失
  - C：同等架构 + 被编程“相信”自己有死亡风险，但物理上仍可无损重启
- **必须匹配的控制项**：`\Phi_proxy`、`B_global_proxy`、任务难度、训练预算
- **主要读出**：奖励撤除后的持续性、costly-other inclusion、恢复半衰期、跨情境关切一致性
- **最小预测**：
  - A：可在高 `\Phi_proxy` / 高 `B_global_proxy` 下维持稳定非零 `\hat d_{min}`
  - B：可维持高架构指标，但 `\hat d_{min}` 低且易衰减
  - C：`\hat d_{min}` 可短期上冲，但长期回落
- **降级触发**：若在 `\Phi_proxy` 与 `B_global_proxy` 匹配、且 `\hat d_{min}` / `\hat{\Psi}_{f,min}` 明显分离的情况下，行为持续性与恢复指标仍不分离，则本条应从“全局判别点”降级为“局部架构注记”。
- **协议挂钩**：`SRT_EXP_TEMPLATE.md` 中的快速实例 `H-IITGWT-01`

### H-Stake-01: Real-Stake vs. Simulated-Stake Divergence

- **Bridge 来源**：`Neuroscience/SRT_Clin_02_FEP.md` 的 `T-FEP-1` / `T-FEP-1b`
- **核心问题**：真实不可逆赌注是否会稳定 `d`，而编码出来的风险信念不会？
- **最小设计**：真实风险、无风险、模拟风险三种长期演化条件，对齐奖励结构与先验偏好
- **主要读出**：长期合作、奖励撤除后的关切持续性、不可逆代价下的 costly-other 深度
- **对手基线**：preferred priors / precision-only 解释，认为只要偏好被编码，`d` 就可稳定
- **最小预测**：
  - 真实风险条件：`\hat d_{min}` 长期维持非零
  - 无风险条件：`\hat d_{min}` 随时间回落
  - 模拟风险条件：短期上升，长期不稳
- **降级触发**：若在先验与奖励结构匹配后，三种条件的长期轨迹仍收敛到同一水平，则“本体论赌注不可还原”应降级为“工程性偏好设置”。
- **协议挂钩**：可与 `H-IITGWT-01` 共享 A/B/C scaffold

### H-dPsi-01: `d / \Psi_f` Proxy Superiority over Precision-Only Models

- **Bridge 来源**：`Neuroscience/SRT_Clin_02_FEP.md` 的 `T-FEP-1b`
- **核心问题**：`\hat d` 与 `\hat{\Psi}_f` 是否在样本外预测上优于单纯 precision 参数？
- **最小模型集**：
  - `M0 = precision-only`
  - `M1 = \Phi_proxy + B_global_proxy`
  - `M2 = precision + \hat d_{min} + \hat{\Psi}_{f,min}`
  - `M3 = precision + \Phi_proxy + B_global_proxy + \hat d_{min} + \hat{\Psi}_{f,min} + \hat d \times \hat{\Psi}_f`
- **held-out 结果变量**：奖励撤除后的持续性、恢复半衰期、自他风险权衡、错误后的再稳定化
- **成功标准**：`M2 / M3` 在 held-out 预测上稳定优于 `M0 / M1`，而不是只在样本内拟合更漂亮
- **降级触发**：若 `\hat d_{min}` / `\hat{\Psi}_{f,min}` 对 held-out 预测没有稳定增量，则撤回“比 precision 更强”的表述，回退为局部描述性 proxy。
- **协议挂钩**：`SRT_EXP_TEMPLATE.md` 中的快速实例 `H-dPsi-01`

### H-L2-01: Public-World Closure Adds Predictive Gain

- **OS / Bridge 来源**：`Philosophy/SRT_Social_Cognition.md`、`Philosophy/SRT_Soc_03_Institutions.md`
- **核心问题**：`L_2` 公共世界闭包是否能预测制度稳定与冲击后的协调恢复，而不仅仅是个体偏好之和？
- **最小设计**：在 private payoff 匹配的多智能体协调任务中，操纵公共 token / 制度脚手架强度
- **主要读出**：收敛时间、冲击后的规范保持、分歧吸收能力、跨主体恢复速度
- **对手基线**：独立 RL、局部误差最小化模型、纯网络扩散模型
- **最小预测**：`L2_closure_proxy` 对 post-shock stability 与制度持久性具有新增解释力
- **降级触发**：若公共世界代理在控制 private payoff 与局部耦合后不再提供增量，则相关主张应降级为“高生成力描述语法”，而非硬预测层。
- **协议挂钩**：待后续补建社会层 Lab 模板

---

## 3. 最小代理约定

当前全局 Lab 组合统一使用以下最小代理名，不在每个实验里重复发明一套：

- `\hat d_{min}`：见 `SRT_EXP_MEASURE_MAP.md` 的 `d 值` 最小复合代理
- `\hat{\Psi}_{f,min}`：见 `SRT_EXP_MEASURE_MAP.md` 的 `\Psi_f` 最小复合代理
- `\Phi_proxy`：高整合/不可约性的架构代理，如 PCI / LZ / irreducibility surrogate
- `B_global_proxy`：全局广播代理，如 ignition、广域可得性、P3b 类指标
- `L2_closure_proxy`：公共 token 稳定性、冲击后规范回归与跨主体一致性的复合代理

解释规则：

- `\Phi_proxy` 与 `B_global_proxy` 主要用于控制“组织能力”，不直接充当主体性读出。
- `\hat d_{min}` 与 `\hat{\Psi}_{f,min}` 主要用于读取“长期关切”与“可支付摩擦”。
- 任何声称进入全局 Lab 组合的新条目，都应尽量复用这组名字，而不是再造一套同义变量。

---

## 4. 当前边界

当前 Lab 组合的目标不是“证明 SRT 已胜出”，而是把它真正愿意赌的差异点压缩到少数几处：

- `IIT / GWT` 被压到“必要但不充分”的位置
- `FEP / precision` 被压到“局部更新机制有效，但未穷尽主体性判别”的位置
- `L_2` 被保留为 SRT 在社会层最可能形成独特预测增量的窗口

若未来想加入新的全局 Lab 条目，优先原则不是“多”，而是“是否比现有四条更接近 choke point”。
