---
id: SRT-EXP-MEASUREMAP
type: experiment
tags: [Experiment, Measure, Proxy]
status: v1
dependency: []
---

# SRT 核心变量—观测指标映射（P1-3）

更新时间：2026-02-28
目标：将核心理论变量映射到可测 proxy

---

## 1) d 值（关切梯度）

Canonical：\(d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|\)

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

## 【理论边界/防误用声明】
- 不采纳“ROS 是选择失败第一因”的还原论：ROS 在 SRT 中是**摩擦历史痕迹 + 反向耦合变量**，不是本体起点。  
- 不采纳“单一生化指标即可定义疾病”的推论：必须联合行为、神经、生理三层 proxy。  
- 不采纳“检测到高维拓扑=意识存在”的推论：拓扑仅是动力学几何特征，不等同本体论判据。  
- 本节为桥接假设，不构成临床诊断或治疗建议。
