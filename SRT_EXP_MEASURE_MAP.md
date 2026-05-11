---
id: SRT-EXP-MEASUREMAP
type: experiment
tags: [Experiment, Measure, Proxy]
status: v1
layer: L2
epistemic_layer: lab
claim_mode: canonical
dependency: [SRT-LAB-HYPOTHESES]
---

# SRT 核心变量—观测指标映射（P1-3）

更新时间：2026-05-11
目标：将核心理论变量映射到可测 proxy

---

## 1) d 值（关切梯度）

Canonical：\(d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|\)

### Lab 最小复合代理（2026-03-17）
\[
\hat d_{min} \equiv \mathrm{mean}\Big(
z(w_{horizon}),
z(span_{care}),
z(persist_{reward\text{-}off}),
z(costly\_other)
\Big)
\]

其中：
- \(w_{horizon}\)：长期权重 / 低时间折扣代理
- \(span_{care}\)：关切范围是否从自我扩展到他者/群体
- \(persist_{reward\text{-}off}\)：外显奖励撤除后的持续性
- \(costly\_other\)：在代价上升时仍纳入他者的深度

**解释规则**：
- `\hat d_{min}` 读的是长期关切边界，而不是一时的自述偏好。
- 若只测到“说自己在乎”，没有奖励撤除或代价上升条件，不得声称已经读到 `d`。

### 行为 proxy
- 跨时间折扣斜率（长期权重）
- 社会关切范围任务（自我/亲密圈/陌生人/群体）
- 多目标冲突任务中的风险权衡深度

### 生理/神经 proxy
- 任务态 HRV 恢复速度（风险调节能力）
- 前额叶-边缘系统耦合强度（如可得）
- PCI 或复杂度指数（高门槛场景）

### 操作化桥接协议（新增）
- **实验构型**：风险决策任务（行为） + 干预扰动（睡眠剥夺/压力诱导） + 神经复杂度读数（PCI/DMN代理）。
- **估计步骤**：
  1) 用行为任务拟合效用梯度代理 \(\widehat{\partial\mathcal{U}/\partial\mathcal{S}}\)；
  2) 用生理/神经指标估计可维持带宽 \(B_{maint}\)；
  3) 通过层级模型得到个体级 \(\hat d\) 与群体后验分布。
- **跨尺度桥接**：
  - 微观/理论层：可引用纠缠面积比例作为上界启发（非直接测量）；
  - 实验室层：以行为-神经联合后验 \(\hat d\) 为可重复估计。
- **验收标准**：跨 session 重测相关 \(r>0.6\) 且跨范式方向一致。

---

## 2) Ψ_f（本体论摩擦）

### Lab 最小复合代理（2026-03-17）
\[
\hat{\Psi}_{f,min} \equiv \mathrm{mean}\Big(
z(c_{switch}),
z(t_{recover}),
z(load_{stress}),
-z(budget_{reserve})
\Big)
\]

其中：
- \(c_{switch}\)：任务切换成本
- \(t_{recover}\)：恢复半衰期
- \(load_{stress}\)：负荷侧指标（SCR / 皮质醇 / 频谱尖峰 / 资源拥塞）
- \(budget_{reserve}\)：预算侧保留量（HRV、睡眠、代谢、可用算力等）

**解释规则**：
- `\hat{\Psi}_{f,min}` 高，表示系统处于更高摩擦 / 更低可支付边缘。
- 该代理优先读取“恢复与支付结构”，而不是主观费力度量。
- 若只记录负荷，不记录预算与恢复，不得声称已完成 `\Psi_f` 的最小操作化。

### 规范解释（新增）
- **动力学读法**：\(Ψ_f\) 表现为阻力 / 势垒 / 偏离自然滑落路径时的阻抗；
- **记账读法**：\(Ψ_f\) 表现为能量、时间、修复与组织复杂度上的支付代价；
- **形式读法**：\(Ψ_f\) 表现为参数流形上的几何长度 / 曲率负担。

三种读法指向同一结构，不得在操作化时混当三个独立变量。

### 可支付性判据（新增）
对系统 \(X\) 在时间窗 \(\Delta t\) 上：
\[
\mathrm{Payable}(X,\Delta t)\iff \alpha P_{sel}^X(\Delta t)\ge \beta \Psi_f^X(\Delta t)+\gamma S_{noise}^X(\Delta t)
\]

解释：
- 关键不在 \(Ψ_f\) 绝对值高低，而在其是否仍处于系统可承受区间；
- **零摩擦** 不等于最优，往往意味着没有真实赌注或没有生成性选择；
- **超载摩擦** 则表现为闭包失败、恢复滞后、身份连续性下降。

### 可支付性 proxy 组（新增）
- **预算侧**：血糖/乳酸、HRV、睡眠充足度、可用计算资源
- **负荷侧**：任务切换成本、Fisher 频谱尖峰、SCR/皮质醇、ROS 斜率
- **崩溃侧**：恢复半衰期延长、行为解组、叙事一致性下降、协同失败率升高

### 行为 proxy
- 任务切换成本（反应时与错误率）
- 认知僵化指标（规则反转任务性能）
- 压力下策略更新滞后

### 生理 proxy
- 皮电峰值与恢复常数
- 皮质醇日节律偏移
- 心率恢复半衰期

### 信息几何 proxy（新增）
- 经验 Fisher 条件数：\(\log\kappa(\hat g_F)\)
- 经验 Fisher 体积项：\(\log\det(\hat g_F)\)
- 最大特征值漂移：\(\lambda_{max}(\hat g_F)\)
- 变点检测：z-score / CUSUM 作用于上述序列

**操作说明**：在固定窗口下同步记录 raw NLL 与 Fisher 频谱代理；若 Fisher 代理先于 NLL 出现显著尖峰，可标注为“结构重配置预警”。

---

## 2a) Consciousness-Architecture Companion Proxies（2026-03-17）

这些指标是当前 `Lab` 组合中的架构控制项，不是主体性本身：

- `\Phi_proxy`
  - PCI / perturbational complexity surrogate
  - Lempel-Ziv complexity
  - irreducibility / integration surrogate
- `B_global_proxy`
  - ignition / late global availability
  - P3b 类指标
  - 广域工作空间占用率

使用规则：

- `\Phi_proxy` 与 `B_global_proxy` 主要用于控制“结构能力”和“全局分发能力”。
- 若实验想论证主体性或真实 stake，不得只报告这两项而省略 `\hat d_{min}` / `\hat{\Psi}_{f,min}`。

---

## 3) ii（信息-存在强度）

### 行为 proxy
- 刺激分化-整合联合任务得分
- 复杂情境中一致性判断稳定性

### 神经 proxy（条件允许）
- 网络整合度与模块化平衡
- 扰动后复杂响应指数（如 PCI 相关）

---

## 4) L2 共享度（社会/制度层）

### 社会网络 proxy
- 共识达成时间
- 语义重叠度（文本嵌入相似）
- 协调任务成功率与冲突频次

### Lab 最小复合代理（2026-03-17）
\[
L2\_closure\_proxy \equiv \mathrm{mean}\Big(
z(retain_{norm}),
z(recover_{post\text{-}shock}),
z(consensus_{stability}),
-z(fragment_{cross\text{-}agent})
\Big)
\]

解释：
- 该代理读取的是公共 token / 制度脚手架是否真的形成了冲击后的“再闭合能力”。
- 若只测单次共识达成，不测冲击后的再稳定化，不足以声称已读到 `L_2` 闭包。

---

## 4a) Eq-Select-Thermo 桥接包（2026-03-16 新增）

### 4a.1 变量映射
- `q(L_1)`：秩序/稳定性代理
  - 低成本：任务稳态成功率、错误熵下降、行为序列 Lempel-Ziv/MDL 可压缩率
  - 高门槛：网络互信息密度、PCI 或自发信号多样性
- `P_{sel}`：可用选择预算
  - 低成本：HRV 恢复斜率、血糖/乳酸、睡眠充足度
  - 高门槛：FDG-PET 葡萄糖代谢、网络级复杂度保真度
- `S_{noise}`：噪声侧抽头
  - 低成本：任务冲突熵、环境波动负荷、RT 变异
  - 高门槛：EEG 高频功率/熵、跨试次状态漂移

### 4a.2 文献锚点
- **Casali et al. 2013**：PCI 通过扰动响应的算法可压缩性读取系统的分化-整合能力，适合作为 `q(L_1)` 的扩展神经 proxy。
- **Schartner et al. 2015**：自发 EEG 信号多样性在麻醉下降，支持“复杂度/多样性下降 = 可用状态空间收缩”的方向性读法。
- **Peng et al. 2014**：Lempel-Ziv complexity 可稳定表征人类动作序列结构，支持行为压缩率作为 `q(L_1)` 的低成本 proxy。
- **Stender et al. 2016**：持续意识需要最低代谢预算，支持 `P_{sel}` 的预算侧测量不应只靠主观费力度量。
- **Weninger et al. 2022**：神经网络能量学与信息论量之间存在系统关系，支持把 `q - P_{sel} - S_{noise}` 当作联立桥接包而非孤立单指标。

### 4a.3 最小证伪模板
\[
\frac{dq}{dt} \le \alpha P_{sel} - \beta \Psi_f - \gamma S_{noise}
\]

- 若提高 `P_{sel}` proxy 后，`q` 代理无系统性上升趋势，需修订预算侧解释。
- 若 `S_{noise}` 显著上升而 `q` 代理不下降，需修订噪声抽头项。
- 若仅单一 proxy 有效而跨模态收敛完全失败，应把该变量回退为“局部实验指标”，不得继续声称已操作化 `q(L_1)`。

---

## 4b) Eq-LDP-01 / Eq-LDP-02 群体尺度桥接包（2026-03-16 新增）

### 4b.1 变量映射
- `\rho(x,t)`：粗粒化密度场
  - 人群/动物/细胞：occupancy histogram、KDE 密度图、局部人数/细胞数
  - 在线群体：topic share density、编辑活跃度密度
- `J(x,t)`：局部流量/通量
  - 轨迹数据：速度场、光流、迁移流矩阵
  - 在线群体：编辑流、转发/扩散流、人口净迁入率
- `I_{SRT}[\rho]`：路径代价 proxy
  - 当前用 coarse-grained surrogate 读取：运动学项 + 摩擦/噪声预算 + 势阱项

### 4b.2 文献锚点
- **Toner & Tu 1998**：主动体群体可在宏观层写成连续体 hydrodynamics。
- **Bain & Bartolo 2019**：真实人群支持速度信息波式传播与局部方向抑制，说明 `\rho / J` 不是纯模拟量，而是可测现实变量。
- **Gu et al. 2025**：高密度人群出现相关长度突增与自发振荡，说明阈值与谱峰可进入群体测量包。
- **Bertini et al. 2001 / 2005 / 2015**：密度-电流联合涨落可由大偏差率函数统一处理，为路径概率指数衰减提供标准统计力学接口。
- **Agranov et al. 2023**：主动系统同样允许 fluctuating hydrodynamics + current large deviations，支持把该桥接扩展到 non-equilibrium collectives。

### 4b.3 最小测量协议
1. 先把原始轨迹/事件流 coarse-grain 到统一网格或主题分箱，得到 `\rho(x,t)`。
2. 用相邻时窗差分或光流重建 `J(x,t)`，并估计相关长度 `\xi`、谱峰 `\omega_0`、阈值 `\rho^*`。
3. 为候选路径定义 `I_{SRT}^*[\rho]` surrogate，并检验 `\log P_{path}` 对 `-I_{SRT}^*` 的近线性关系。

### 4b.4 边界
- 不采纳“群体一定像流体”的绝对化推论：只有在高密度、局部相互作用与 coarse-graining 有效时，Eq-LDP-01 才成立。
- 不采纳”拟合到指数衰减就等于 action 已被唯一识别”的推论：当前只是在做 rate-function window，不是唯一 canonical derivation。

---

## 4c) Non-Reductive Validation Rule（非还原验证规则）

SRT concepts should be tested through convergent structural consequences rather than a single direct objective ruler. A proxy may support an SRT construct only when it helps distinguish selection friction, concern-weighted non-substitutability, or hardening from simpler alternatives such as loss, reward, salience, memory, convention, or generic task difficulty.

A measurement package should not ask whether one variable directly “is” `Ψ_f`, `d-value`, or `L_2`. It should ask whether a set of proxies jointly detects the structured consequences expected from the construct.

| Construct | Non-reductive validation target | Simpler alternatives to control against |
|---|---|---|
| `Ψ_f` | structured transition difficulty, recovery burden, switching cost, update curvature | generic effort, task difficulty, prediction error, raw energy use |
| `d-value` | concern-weighted non-substitutability, cost-bearing, identity/stake continuity | preference intensity, reward, salience, pain, self-report |
| `L_2` hardening | local cost reduction plus global constraint plus hysteresis | memory, habit, convention, environmental stability |

### 最小验收标准（Minimum Acceptance Criteria）

A proxy package is acceptable only if it satisfies all three conditions:

1. **Multi-proxy convergence**：至少两类独立 proxy 同向收敛。
2. **Alternative exclusion**：结果不能完全被 reward、salience、memory 或 generic task difficulty 等更简单解释吸收。
3. **Scope declaration**：必须声明 proxy 的操作范围，不能把 proxy 反投为 ontology 本身。

### 失效条件（Failure Conditions）

- **F-EXP-NR-1**：如果单一 proxy 被当作 SRT construct 本身，则该测量层退化为 reductionism，应拒绝。
- **F-EXP-NR-2**：如果 proxy package 不能区分 `Ψ_f`、`d-value` 或 `L_2` 与更简单替代解释，则只能报告为 ambiguous proxy result。
- **F-EXP-NR-3**：如果 proxy package 在 session、task 或 perturbation context 之间没有基本稳定性，则它与目标 construct 的关系仍然较弱。

### Hemodynamic-metabolic proxy uncertainty gate (bioRxiv 2026, 2026-05-11, Pipeline 1)

Metabolic readouts only become SRT-usable proxies when their direction survives an explicit uncertainty gate. If a BOLD / CMRO₂ sign relation is inferred from group-mean direction while participant-level or voxel-level uncertainty remains large, the correct SRT classification is **indeterminate proxy**, not evidence for physiological sign reversal and not evidence for or against `Ψ_f`, `d-value`, consciousness, or `L_2`.

Minimum rule:

\[
R_{metab}(v)=1
\quad\Longrightarrow\quad
\Delta CMRO_2(v)\neq 0
\text{ under a declared error model and correction rule.}
\]

If \(R_{metab}(v)=0\), the voxel / region / contrast must be reported as ambiguous, even when the group-mean BOLD and CMRO₂ signs oppose each other. Negative BOLD receives an additional caution flag because its metabolic underpinnings are heterogeneous.

This gate was added after the 2026 bioRxiv reanalysis of BOLD-CMRO₂ discordance (`doi:10.64898/2026.04.21.719913`). Its SRT role is methodological: protect metabolic proxy claims from being back-projected into ontology.

---

## 5) 使用原则

1. 每个理论变量至少配置 2 类 proxy（行为 + 生理/神经优先）。
2. 先低门槛指标建立可重复性，再上高门槛设备。
3. 任何 proxy 结论必须声明“操作化解释范围”，不得反向冒充定义。

---

## 6) Assembly Theory（AT）桥接指标（新增）

### 6.1 变量映射
- 外部 `assembly index (a_i)` → SRT 深度代理 `D_i`
- 外部 `copy number (n_i)` → SRT 持久代理 `P_i`
- 外部阈值 `a_M` → SRT 无主动选择上界代理 `a_M^{(SRT)}`

### 6.2 可观测 proxy
- **深度代理（D）**：最小递归构建步的可压缩长度（任务图最短可复现链长）
- **持久代理（P）**：同构结果在窗口期内复现次数/复现稳定度
- **阈值跨越判据**：当 `D` 与 `P` 同时进入高分位区（如各自 > P75）并持续 `k` 个窗口

### 6.3 分类映射表（AT 分类 → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 自发可达区 | 低~中 | Semi-open | payable |
| 阈值邻域 | 中高 | Open↔Semi-open | borderline |
| 选择主导区 | 高 | Open | payable / overloaded |
| 失稳衰退区 | 中高回落 | Closed 倾向 | unsustainable |

## 【理论边界/防误用声明】
- 不采纳“高重复=真理”推论：高 `P` 只表示机制持久，不保证规范正确性。  
- 不采纳“高深度=高价值”推论：高 `D` 可能对应病理性僵化结构，需结合效用与风险指标。  
- 本节为测量映射，不替代对象层因果机制证明。

---

## 7) 年龄分层白质结构代理（eNeuro 2026 新增）

### 7.1 变量映射
- 白质“分化程度” → SRT 结构分化代理 `WDI`（White-matter Differentiation Index）
- 特定通路“同质性下降” → SRT 稳态退化代理 `WHD`（WM Homogeneity Decline）

### 7.2 可观测 proxy
- **WDI（分化指数）**：基于 tract-level 髓鞘相关特征（如 MT/MWF 或等价 MRI 宏分子特征）在通路间的可分离度（聚类间距/判别效应量）。
- **WHD（同质性下降）**：年龄分层后，关键认知灵活性通路内方差与跨区一致性变化（如 ICC 下降、变异系数上升）。
- **阶段化判据**：
  - 早成年：低 WDI + 稳定 WHD（不显著下降）
  - 晚成年：高 WDI + 显著 WHD 下降

### 7.3 分类映射表（年龄阶段 → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 早成年低分化阶段 | 中~中高 | Open / Semi-open | payable |
| 晚成年高分化阶段 | 中高~高（异质化） | Semi-open（局部约束增强） | payable→borderline |
| 晚成年同质性下降加速段 | 中高回落风险 | Closed 倾向（局部） | borderline / overloaded |

## 【理论边界/防误用声明】
- 不采纳“年龄增长=必然认知衰退”推论：该研究是群体层统计，不可直接外推个体命运。  
- 不采纳“白质指标可单独定义 d 或 \(\Psi_f\)”推论：仅作为神经层代理，需与行为与任务数据联合建模。

---

## 8) 疾病机制桥接：ROS 作为 \(\Psi_f\) 一级生化 Proxy（新增）

### 8.1 动力学候选方程

\[
\frac{d(ROS)}{dt} = \alpha\,\Psi_f(\hat{G}_\theta) - \beta\,\mathrm{Clearance}(\theta_{body})
\]

其中：
- \(\alpha\)：摩擦到氧化负荷的耦合系数；
- \(\beta\)：抗氧化清除效率系数；
- \(\theta_{body}\)：具身参数（免疫/代谢/内感受）对子系统清除能力的统摄项。

### 8.2 可观测 proxy 组合
- 分子层：GSH/GSSG 比值、MDA、8-OHdG、SOD/GPx 活性；
- 系统层：炎症因子面板（如 IL-6、TNF-\(\alpha\)）与 HRV 恢复常数联合；
- 任务层：高负荷选择任务（冲突决策/多目标切换）前后 ROS 变化斜率。

### 8.3 分类映射表（疾病负荷阶段 → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 稳态补偿期（Compensated） | 中~中高 | Open / Semi-open | payable |
| 亚临界失衡期（Pre-break） | 中高波动 | Semi-open（维护成本上升） | borderline |
| 失代偿期（Decompensated） | 中高回落风险 | Closed 倾向（局部锁死） | overloaded / unsustainable |

### 8.4 最小证伪条件（Falsification）
1. 在低 \(\Psi_f\) 任务中，若 ROS 仍系统性持续抬升且与清除率无关，则该映射失效；
2. 若提高清除能力（\(\beta\uparrow\)）后，过滤性能（\(\rho_s,\rho_t\) proxy）无改善，则“ROS 反向耦合”不足；
3. 若高 \(\Psi_f\) 负荷不伴随任何 ROS/氧化压力变化，则需回退到替代机制（非氧化主导）。

## 9) 拓扑神经动力学桥接（Scientific American/Blue Brain 对齐新增）

### 9.1 变量映射
- 外部“高维 clique 组装” → SRT 拓扑复杂度状态量 `K_t`
- 外部“cavity/空洞” → SRT `L_0^{rel}` 在 `L_1` 边界中的负向投射代理
- 外部“刺激后坍塌” → SRT 坍塌率 `\lambda_c`（与 `\Psi_f` 可支付性耦合）

### 9.2 可观测 proxy
- **拓扑复杂度 K**：按时窗构建 clique complex，计算 `f-vector` 与维度上界（max simplex dim）
- **Betti 向量**：`(\beta_0, \beta_1, \beta_2, ...)` 与 persistence lifespan（持久同调）
- **坍塌率 \lambda_c**：刺激终止后 `K_t` 或 `q_topo(t)` 指数回落拟合系数
- **选择偏置 \beta_topo（间接）**：在控制输入强度后，不同 `d` 组之间高维特征保留率差异

### 9.3 分类映射表（拓扑阶段 → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 基线低维协同 | 低~中 | Semi-open | payable |
| 刺激驱动高维组装 | 中高~高 | Open | payable / borderline |
| 高维空洞峰值期 | 高（瞬时） | Open（高注入） | borderline / overloaded |
| 坍塌回落与重整 | 中高回落 | Closed 倾向 | unsustainable（若长期维持） |

### 9.4 最小证伪条件
1. 若 `d` proxy 与高维 Betti/persistence 无系统关联，则“选择层偏置”假设失效；
2. 若 `\Psi_f` 代理上升时 `\lambda_c` 不上升且不存在补偿机制证据，则“摩擦-坍塌耦合”失效；
3. 若随机网络可稳定复现实验同等高阶拓扑曲线，则需下调 SRT 的选择解释权重。

## 10) 神经精神病学桥接测量（Frontiers 2026 对齐新增）

### 10.1 变量映射
- 外部“神经-精神分裂” → SRT 双轴：`structural axis = ||Δθ_struct||`，`dynamic axis = ||Δθ_dyn||`
- 外部“对话桥梁” → SRT 协同恢复指标 `ΔS_sync = Δd·(-ΔΨ_f)`
- 外部“历史-认识论碎片化” → SRT 跨层失配指标 `Mismatch(L1,L2)`

### 10.2 可观测 proxy
- **结构轴（L2）**：连接组断连指数、白质完整性指标、网络模块化异常
- **动力学轴（Gθ）**：d-value 行为后验、ρ_t 时序整合误差、任务切换摩擦成本
- **跨层失配**：症状波动对结构指标解释残差（高残差=语义断层候选）

### 10.3 分类映射表（神经精神病学分类 → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 神经主导型 | 中~中高（受结构上限） | Semi-open（局部受损） | payable→borderline |
| 精神主导型 | 低~中高波动 | Open↔Semi-open | borderline / overloaded |
| 混合型 | 中高离散 | Open+Closed 并存 | overloaded / unsustainable |
| 协同恢复型 | 中高回升 | Semi-open→Open | payable |

### 10.4 最小证伪条件
1. 若双轴模型对预后解释力不优于单轴症状模型，则病理矩阵不成立；
2. 若联合干预不提升 `ΔS_sync`，则“跨域协同”假设失效；
3. 若高残差病例不呈现更高参数敏感性（\(|∂L1/∂θ|\) proxy），则语义断层假设失效。

## 【理论边界/防误用声明】
- 不采纳“ROS 是选择失败第一因”的还原论：ROS 在 SRT 中是**摩擦历史痕迹 + 反向耦合变量**，不是本体起点。  
- 不采纳“单一生化指标即可定义疾病”的推论：必须联合行为、神经、生理三层 proxy。  
- 不采纳“检测到高维拓扑=意识存在”的推论：拓扑仅是动力学几何特征，不等同本体论判据。  
- 不采纳“神经指标或精神量表单独即可完成诊断”的推论：需双轴联合建模。  
- 本节为桥接假设，不构成临床诊断或治疗建议。

---

## 11) Hart 六章统合桥接测量（Sat–Chit–Ananda + Illusion/Reality，新增）

### 11.1 变量映射
- **Sat（存在）** → `L1_contingency_load`：维持显现所需摩擦预算（与 O-T7/O-T8 一致）
- **Chit（意识）** → `Intentional Integrity Index (III)`：内在意向性与派生意向性可分离度
- **Ananda（至福）** → `Teleological Pull Ratio (TPR)`：\(d_{pull}/(d_{push}+\epsilon)\)
- **Illusion/Reality（幻象-现实）** → `Ontological Amnesia Index (OAI)`：\(\mathcal{A}_{onto}\)

### 11.2 可观测 proxy 与阈值（候选）
- **III（意向完整度）**：反事实任务中的自主新维度生成率 / 语料插值率；
  - 失效阈值：若长期 \(<0.2\) 且仅靠提示重写提升，则判为“派生意向性主导”。
- **TPR（牵引比）**：高价值任务中 \(d_{pull}\) 提升幅度与风险规避项比值；
  - 稳定牵引阈值：\(TPR>0.6\) 且持续 \(k\ge5\) 窗口。
- **OAI（本体论失忆）**：自动化决策占比 × 规范硬度 / 新奇探索量；
  - 高风险阈值：\(OAI>1.5\) 持续两周，提示“L2 自动驾驶锁定”。
- **L1_contingency_load**：\(\Psi_f\) 基线 + 任务波动残差；
  - 边界阈值：若拟合 \(\Psi_f\to0\) 仍宣称“高显现稳定”，判定模型自相矛盾。

### 11.3 分类映射表（六章统合状态 → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 方法论闭包误当本体论 | 低~中 | Closed 倾向 | 被掩蔽 / 低显性 |
| 意向重建过渡期 | 中 | Semi-open | borderline |
| 价值牵引与存在惊奇并行 | 中高~高 | Open | payable / 峰值波动 |
| 稳态整合（非终点） | 中高 | Open→Semi-open 稳态 | \(\Psi_f\ge\Psi_{min}^{+}\) |

### 11.4 最小证伪条件
1. 若 OAI 与探索坍缩无关联，则“本体论失忆”操作化失败；
2. 若 III 在纯句法系统中长期高于具身系统，则“意向非等价”需重审；
3. 若 TPR 提升不伴随 \(\Psi_f\) 支付结构变化，则“牵引项”解释力不足。

---

## 12) 被动对齐相变（Passive Alignment）测量补丁（新增）

### 12.1 动力学分解
\[
\Psi_f^{total}=\Psi_f^{local}+\Psi_f^{coh}
\]
目标不是 \(\Psi_f^{total}\to0\)，而是局部抓取成本下降、协同支付上升。

### 12.2 代理指标
- \(\Psi_f^{local}\)：主观用力感评分 + 执行控制代价（RT/错误率）
- \(\Psi_f^{coh}\)：跨任务一致性、群体协同增益、叙事-行为同调指数
- 对齐角 proxy：\(\cos\angle(\vec v_{self},-\nabla F_{global})\) 的行为近似（长期目标一致率）

### 12.3 阈值判据（候选）
- 被动对齐成立：
\[
\Delta \Psi_f^{local}<0,\quad \Delta \Psi_f^{coh}>0,\quad \Delta\text{Clarity}>0
\]
且三者连续满足 \(k\ge3\) 评估窗口。

### 12.4 防误用边界
- 不采纳“被动对齐=放弃行动”推论；
- 不采纳“被动对齐=外在超实体接管因果链”推论；
- 该节仅为动力学重参数化测量，不给出神学断言。


## 13) 全息调谐指数 HTI（候选，hypothesis-level）

### 13.1 指标定义
定义 Holographic Tuning Index：
\[
\mathrm{HTI}=\mathrm{PLV}_{brain\leftrightarrow env}^{(band,window)}\cdot \Delta\Psi_f^{-1}\cdot C_{report}
\]
其中：
- \(\mathrm{PLV}\)：脑-环境慢变量相位锁定代理；
- \(\Delta\Psi_f^{-1}\)：任务窗口内摩擦下降幅度（归一化）；
- \(C_{report}\)：主观报告一致性（边界消融/心流）校正项。

### 13.2 可观测 proxy
- 脑侧：跨脑区同步（EEG/MEG 可得频段）；
- 环境侧：任务节律/社会协同节律的慢变量相位；
- 行为侧：执行流畅度与错误恢复速度。

### 13.3 分类映射表（调谐状态 → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 基线未锁相 | 低~中 | Semi-open | payable |
| 局部锁相协同 | 中~中高 | Open↔Semi-open | payable / borderline |
| 过度归因（神秘化） | 低~中 | Closed（解释越级） | 被误估 |

### 13.4 最小证伪条件
1. 若 HTI 与任务绩效/恢复速度无相关，则该指标失效；
2. 若 HTI 仅由主观报告驱动且无生理/行为支持，则降级为叙事变量；
3. 若去除环境相位项后效果不变，则“调谐”解释不足。

## 【理论边界/防误用声明】
- HTI 为**候选代理**，不等同“宇宙连接”已被实证。
- 不采纳“单频段同步即证明微管机制”的推论。
- 不采纳“HTI 升高=意识层级提升”的直接推论；需联合 d 与 \(\Psi_f\) 门控判据。


## 14) 结构化迟滞指征 SHP（GEMINI/GEAR 桥接，新增）

### 14.1 指标定义
定义 Structural Hysteresis Proxy：
\[
\mathrm{SHP}=\frac{\Delta \mathcal{R}_{ring}}{\Delta t}\cdot\frac{1}{1+\Delta H_{noise}}\cdot W_{event}
\]
其中：
- \(\Delta \mathcal{R}_{ring}/\Delta t\)：分子环/组装标记的时间增长率；
- \(\Delta H_{noise}\)：背景噪声熵增校正；
- \(W_{event}\)：事件权重（如神经放电、应激窗口、任务难度）。

### 14.2 SRT 映射语义
- SHP 用于估计 \(L_1\to L_2\) 的沉积密度（selection density）；
- 不等价于意识指标，不可替代 \(d\) 或 \(\Psi_f\) 的本体门控判据。

### 14.3 最小证伪条件
1. 若 SHP 与外部事件强度无稳定对应关系，则沉积映射失效；
2. 若 SHP 提升不伴随历史可回溯性提升，则“迟滞沉积”解释不足；
3. 若纯随机驱动可复现实验同等 SHP 轨迹，则需降级为非特异记录变量。

## 【理论边界/防误用声明】
- 不采纳“高密度历史记录=高主体性”的推论。  
- 不采纳“无扰动记录=无代价意识生成”的推论：SHP 只描述被动沉积能力。



## Exp-Lang-Sense-01：跨语言感官语义拓扑探针（2026-03-07）

### 目标
将感官词汇共用网络（colexification network）映射为 \(L_2\) 语义吸引子地形，估计不同感知概念间的转化势垒。

### 可测定义
- 节点：感官概念（看、听、闻、尝、触及其子概念）
- 边权：跨语言共词频率 \(w_{ab}\)
- 势垒代理：
\[
B_{ab}^{proxy}\propto -\log(w_{ab}+\epsilon)
\]
- 生态需求指数：\(\mathcal N_{comm}^{(m)}\)（任务依赖沟通负荷）

### 假设
\[
\mathcal N_{comm}^{(m)}\uparrow \Rightarrow \Lambda_{sense}(m)\uparrow \Rightarrow \text{lexical granularity}(m)\uparrow
\]
并预测：非视觉通道在高生态压力语境中可出现超线性词汇细分。

### 分类映射表（语言观测状态 → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 低共词、低细分（稳定常规） | 中 | Semi-open | payable |
| 高共词桥接（低势垒滑移） | 中~高 | Open / Semi-open | payable |
| 非视觉高细分爆发 | 中高 | Open（定向适配） | borderline~payable |
| 语义孤岛化（跨模态断裂） | 低~中 | Closed 倾向 | brittle |

### 最小证伪条件
1. 若生态需求指标与词汇细分度长期无关，则“交流需求退火”假设失败；
2. 若共词网络与行为混淆矩阵无关联，则“低势垒路径”解释不足；
3. 若视觉优势在所有生态域都可被完全逆转且无代价项变化，则 SRT 硬约束条款需重审。

## 【理论边界/防误用声明】
- 不采纳“词汇多样性 = 感官神经硬件已重写”的推论；需分离语言层与生理层证据。  
- 不采纳“跨语言统计相关 = 因果机制已锁定”的推论；需纵向语料与实验任务闭环。  
- 本探针用于 \(L_2\) 语义拓扑测绘，不单独输出意识本体结论。
