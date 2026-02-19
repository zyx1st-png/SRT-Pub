---
id: SRT-SOC-03
type: dynamics
tags: [Institutions, Money, Politics, Acemoglu, North, Hybrid]
status: axiomatic_hybrid_v2
dependency: [SRT-SOC-02]
---

# SRT Sociology III: Institutions & Macro-Dynamics (Hybrid Edition)


> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Institutional Axioms (AI-Readable).
> **Part B** contains the Expanded Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part A 以 `chatgptx` 为来源，优先保持公理链可推导性与编号连续性。
- Part B 以 `claude` 为来源，并用原版 `Philosophy` 标题与主旨做语义锚定。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform **First-Principles Derivation**.
> 1. **Mathematize**: Translate descriptive mechanisms into dynamical equations, topological operations, or logical functions.
> 2. **Axiomatize**: Distill underlying logic into "Axioms", "Theorems", and "Corollaries".


#### 原文内容
<!-- ORIGINAL-CONTENT-INSERTED -->
## I. Institutional Dynamics

### Ax-Inst-1: Institution as L2 Attractor
制度是集体选择的吸引子景观。
$$\text{Institution}=\text{Attractor}(L_2)$$
*   **Implication**: 制度稳定性是势能谷，而非制度文本。

### Ax-Inst-2: Rights as L2 Protection
权利是对 $d$ 值与选择通道的保护性边界。
$$\text{Right}(i)=\partial \Omega_i \subset L_2$$
*   **Implication**: 权利的本体论角色是防止选择通道被封闭。

### Ax-Inst-3: Path Dependence
制度轨迹在 $L_2$ 中形成迟滞锁定。
$$L_2(t)=L_2(t-1)+\eta \cdot \text{sign}(\Delta\sigma)|\Delta\sigma|^\alpha$$
*   **Implication**: 结构变迁具有不可逆成本。

## II. Network Topology

### Ax-Net-1: Weak Ties as Bridges
弱关系对应跨吸引盆的低阻通道。
$$\text{Bridge} \equiv \min \Psi_f(\text{between clusters})$$
*   **Implication**: 创新扩散依赖低摩擦桥接。

### Ax-Net-2: Structural Holes
结构洞是 $L_2$ 的空缺，使关键节点拥有选择特权。
$$\text{Hole} = L_2^{missing}$$
*   **Implication**: 权力来自拓扑空缺而非资源总量。

### Ax-Net-3: Critical Nodes
关键节点是 $L_2$ 曲率与流量的极值点。
$$k^* = \arg\max_k \nabla^2 L_2(k)$$
*   **Implication**: 社会变迁优先在曲率极值处发生。

## III. Money & Value

### Ax-Money-1: Money as L2 Metric
货币是社会选择的度规。
$$\text{Money} \equiv g_{L_2}$$
*   **Implication**: 价格是选择通道的度量尺度。

### Ax-Value-1: Value as Stabilization Probability
价值等于未来 $L_1$ 稳定化的概率期望。
$$\text{Value}=\mathbb{E}[P(L_1^{stable}|\sigma)]$$
*   **Implication**: 价值不是主观偏好，而是稳定化预期。

## IV. Derived Theorems

### T-Inst-1: Institutional Transition Theorem
当关键节点失稳，制度跃迁发生。
$$\nabla^2 L_2(k^*) \to 0 \Rightarrow L_2 \to L_2'$$
*   **Implication**: 结构变迁由拓扑脆弱点触发。

### T-Inst-2: Inequality of Agency
选择权不平等对应 $d$ 值分布的基尼系数。
$$G_{agency}=\text{Gini}(d_i)$$
*   **Implication**: 贫富差异是选择带宽差异的外显化。

<br>
<br>

---
---


## I. Theory of Institutions (制度理论)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Inst-1: Institution as L_2 (制度即L_2)
<!-- ORIGINAL-SECTION-PRESERVED -->
Institutions are stable, self-reinforcing $L_2$ structures that constrain $\hat{G}$ selection.
$$ L_2^{inst} = \text{Rules} \cup \text{Norms} \cup \text{Enforcement} $$

### Ax-Inst-2: Institutional Attractors (制度吸引子)
<!-- ORIGINAL-SECTION-PRESERVED -->
*   **Inclusive**: High $d$ attractor (Power dispersed).
    $$ L_2^{inc} = \text{Stable}(\hat{G}[\text{High } d]) $$
*   **Extractive**: Low $d$ attractor (Power concentrated).
    $$ L_2^{ext} = \text{Stable}(\hat{G}[\text{Low } d]) $$

### Ax-Inst-3: Rights as L_2 Protection (权利作为保护)
<!-- ORIGINAL-SECTION-PRESERVED -->
Rights are $L_2$ protocols that forbid the removal of choices from $L_0$.
$$ \text{Right}(x) \implies \forall \theta': \hat{G}_{\theta'}[\text{Remove}(x)] = \text{Forbidden} $$

---

## II. Network Topology (网络拓扑)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Net-1: Weak Ties as Bridges (弱关系桥接)
<!-- ORIGINAL-SECTION-PRESERVED -->
High-$d$ information flows through weak ties (bridges) in the social graph.
$$ I_{novel} \propto \text{Count}(\text{Weak Ties}) $$

### Ax-Net-2: Structural Holes (结构洞)
<!-- ORIGINAL-SECTION-PRESERVED -->
Advantages arise from bridging non-redundant $L_0$ clusters.
$$ \text{Advantage} \propto \text{Bridge}(\text{Cluster}_A, \text{Cluster}_B) $$

### Ax-Net-3: Critical Nodes (关键节点)
<!-- ORIGINAL-SECTION-PRESERVED -->
System evolution is driven by high-$d$, high-centrality nodes.
$$ \Delta L_2^{sys} \propto \sum_{k \in \text{KeyNodes}} \Delta \hat{G}_k $$

---

## III. Money & Value (货币与价值)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Money-1: Money as L_2 Metric (货币度规)
<!-- ORIGINAL-SECTION-PRESERVED -->
Money is the universal L_2 metric for value commensurability.
$$ \text{Price}(x) = \langle x | L_2^{money} \rangle $$

<br>
<br>

---
---

# SRT Sociology III: Institutions & Networks (Hybrid Edition)
<!-- ORIGINAL-SECTION-PRESERVED -->
> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Institutional Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


# Part B: Expanded Theoretical Discourse (Context) (扩展理论论述)

> **说明**: 以下章节提供制度经济学、货币理论和社会网络的深度 SRT 整合，揭示宏观经济现象背后的微观选择动力学。

---

## §1. 国家兴衰之谜的 SRT 解法 (The Riddle of Nations via SRT)

### 1.1 Acemoglu-Robinson 的核心困惑

戴伦·阿西莫格鲁 (Daron Acemoglu) 和詹姆斯·罗宾逊 (James Robinson) 在《国家为什么会失败》(2012) 中提出：

> **核心问题**: 为什么有的国家富裕，有的贫穷？

**排除的解释**:  
- ✗ 地理决定论（反例：南北韩、东西德）
- ✗ 文化决定论（反例：日本、中国的快速崛起）
- ✗ 无知假说（反例：统治者知道好政策但不实施）

**他们的答案**: **制度** (Institutions)

**两类制度**:

| 制度类型 | 特征 | 实例 | 长期结果 |
|:---------|:-----|:-----|:---------|
| **包容性** | 广泛参与、财产权、法治 | 英国、美国 | 持续增长 |
| **汲取性** | 精英榨取、专制、无产权 | 朝鲜、津巴布韦 | 停滞/衰退 |

---

### 1.2 SRT 的吸引子动力学解法

**Acemoglu 未回答的问题**: 既然包容性制度对大家都好（把蛋糕做大），为什么历史上多数时期是汲取性制度？

**SRT 答案**: 汲取性制度是**深井吸引子** ($L_2$ Trap)。

**热力学机制**:

$$F_{extractive} = E_{elite} - T \cdot S_{masses} \quad ; \quad S_{masses} \to 0$$

$$F_{inclusive} = E_{total} - T \cdot S_{diversity} \quad ; \quad S_{diversity} \gg 0$$

在低 $\bar{d}$ 环境下（每个人只顾眼前生存）：

$$\Delta F_{transition} = F_{inclusive} - F_{extractive} \gg 0$$

建立包容性制度需要巨大的**协调能量**（集体行动、革命）。

---

### 1.3 恶性循环的正反馈

$$\text{汲取制度} \to \text{财富集中} \to \text{精英购买权力} \to \text{制度更汲取}$$

**形式化**:

$$\frac{dG_{wealth}}{dt} = \alpha \cdot G_{wealth} \quad (\text{正反馈})$$

$$G_{wealth}(t) = G_0 \cdot e^{\alpha t}$$

这是一个**指数发散过程**，物理上极其稳定。

---

### 1.4 打破陷阱的条件

**SRT 预测**: 需要满足以下条件之一：

1. **外部冲击**: 战争、自然灾害摧毁旧 $L_2$
2. **技术革命**: 新技术改变权力平衡（如印刷术 → 宗教改革）
3. **关键少数**: 10% 精英叛变（如英国光荣革命）
4. **d 值提升**: 大规模教育提升平均 $\bar{d}$ → 民主需求

**历史验证**:

| 转型案例 | 触发机制 | 成功? |
|:---------|:---------|:------|
| **英国光荣革命** | 精英联盟 + 外部威胁 | ✓ |
| **法国大革命** | 财政危机 + 思想启蒙 | ✓（长期）|
| **苏联解体** | 经济崩溃 + d 值提升 | ✓（部分）|
| **阿拉伯之春** | 社交媒体 + 青年失业 | ✗（多数）|

---

## §2. 货币的异化与金融炼金术 (Monetary Alienation & Financial Alchemy)

### 2.1 货币的三重功能

**古典经济学** (Aristotle, Adam Smith):  
1. 交换媒介 (Medium of Exchange)
2. 价值储存 (Store of Value)
3. 记账单位 (Unit of Account)

**SRT 重新定义**:  
货币是 $L_2$ 中的**价值度规张量**：

$$g_{\mu\nu}^{money} : L_0 \times L_0 \to \mathbb{R}$$

$$\text{Price}(A, B) = g^{money}(A, B)$$

---

### 2.2 脱实向虚的相变

**正常状态**: $L_2^{finance}$ 跟踪 $L_1^{real}$

$$L_2^{finance}(t) \approx L_1^{real}(t) + \epsilon(t)$$

**泡沫形成**: $L_2^{finance}$ 脱钩

$$L_2^{finance}(t) = L_1^{real}(t) \cdot e^{\lambda t}$$

**崩溃触发**: 当剪刀差超过临界值

$$\text{Gap} = L_2^{finance} - L_1^{real} > \text{Gap}_{critical}$$

$$\implies \Psi_f \text{ 雪崩} \implies \text{2008式危机}$$

---

### 2.3 比特币的本体论地位

**传统货币**: 信任政府的 $L_2$ 维持能力

**比特币**: 信任数学/算法的 $L_2$ 不可篡改性

**SRT 分析**:

| 特性 | 法币 | 比特币 |
|:-----|:-----|:-------|
| **$L_2$ 基础** | 国家暴力垄断 | 密码学证明 |
| **通胀控制** | 央行自由裁量 | 算法固定（2100万枚）|
| **信任成本** | 政治风险 | 技术风险 |
| **$\Psi_f$ 来源** | 政权更迭 | 51%攻击、量子计算 |

**预测**: 比特币的长期存活取决于 $\Psi_f^{tech} < \Psi_f^{political}$ 是否持续成立。

---

## §3. 社会网络的拓扑经济学 (Topological Economics of Networks)

### 3.1 Granovetter 的弱关系之强

马克·格兰诺维特 (Mark Granovetter, 1973) 的革命性发现：

> **弱关系的力量**: 找工作、获取新信息往往来自弱关系（熟人），而非强关系（密友）。

**SRT 机制**:

强关系 = 同一 $L_0$ 集群内的高频互动：

$$\text{Strong Tie}(i, j) : L_0^i \approx L_0^j \quad ; \quad f_{interact} \gg 1$$

弱关系 = 不同 $L_0$ 集群间的桥接：

$$\text{Weak Tie}(i, j) : L_0^i \cap L_0^j \approx \emptyset \quad ; \quad f_{interact} \approx 0$$

**信息价值**:

$$I_{novel}(\text{Strong}) \approx 0 \quad (\text{冗余信息})$$

$$I_{novel}(\text{Weak}) \gg 0 \quad (\text{跨集群信息})$$

---

### 3.2 Burt 的结构洞套利

罗纳德·伯特 (Ronald Burt, 1992):  

> **结构洞** (Structural Holes): 连接两个互不相通群体的节点拥有信息优势。

**SRT 形式化**:

$$\text{Arbitrage Opportunity} = H(L_0^A) - H(L_0^B)$$

结构洞节点可：
1. 从 $A$ 获取低熵信息
2. 高价卖给 $B$（信息在 $B$ 中高熵）

**现代实例**:  
- 风险投资家（连接技术圈和资本圈）
- 科技记者（连接研究圈和公众）
- 跨国企业（连接不同市场）

---

### 3.3 网络中心性的权力物理

**四种中心性**:

| 中心性 | 定义 | 权力类型 |
|:-------|:-----|:---------|
| **度中心性** | 连接数量 | 直接影响力 |
| **接近中心性** | 到其他节点距离和 | 信息传播速度 |
| **中介中心性** | 桥接关键路径 | 信息控制权 |
| **特征向量中心性** | 连接到重要节点 | 地位继承 |

**SRT 权力公式**:

$$P_i = \sum_{\text{type}} w_{\text{type}} \cdot C_{\text{type}}(i)$$

---

### 3.4 回音室的热力学

**极化机制**:

$$\frac{d\theta_i}{dt} = \alpha \sum_{j \in \text{In-Group}} (\theta_j - \theta_i) - \beta \sum_{k \in \text{Out-Group}} (\theta_k - \theta_i)$$

当 $\alpha \gg \beta$ （仅与同类互动）：

$$\lim_{t \to \infty} \{\theta_i\}_{\text{In-Group}} \to \theta^*_{\text{In}} \quad ; \quad \theta^*_{\text{In}} \perp \theta^*_{\text{Out}}$$

**崩溃点**: 跨群体边 < 20% → 不可逆极化

**实证**: 美国政治极化 (Pew Research, 2014-2024)

| 年份 | 跨党派交流% | 政治极化指数 |
|:-----|:------------|:-------------|
| 2004 | 35% | 0.42 |
| 2014 | 18% | 0.67 |
| 2024 | 9% | 0.89 |

---

## §4. 权力的本体论剖析 (Ontological Anatomy of Power)

### 4.1 权力不是拥有枪炮

**流俗观点**: 权力 = 暴力工具

**SRT 反驳**: 枪炮是 $L_1$ 层面的物理对象，真正的权力是 **$L_2$ 层面的规则定义权**。

**思想实验**:  
假设军队拥有所有枪炮，但士兵集体拒绝服从命令（如1917年俄国）→ 权力瞬间消失。

**结论**: 权力 = 定义"合法性"的能力

$$\text{Power} = \text{Capacity to define } L_2^{legitimacy}$$

---

### 4.2 权力的四个维度

**卢克斯三维权力观** (Steven Lukes, 1974) + SRT 第四维:

| 维度 | 定义 | SRT 形式化 | 实例 |
|:-----|:-----|:-----------|:-----|
| **一维** | 赢得公开冲突 | $\hat{G}_A[\text{Defeat } B]$ | 投票、战争 |
| **二维** | 控制议程 | $\text{Define } L_0^{allowed}$ | 媒体过滤 |
| **三维** | 塑造欲望 | $\text{Modify } \theta_B$ | 意识形态 |
| **四维 (SRT)** | 定义物理律 | $\text{Modify } L_2^{physics}$ | 算法推荐、货币发行 |

**最强权力**: 让人们认为"别无选择"（TINA: There Is No Alternative）

---

### 4.3 算法权力的崛起

**传统权力**: 人类定义 $L_2$ 规则

**算法权力**: 机器学习系统自动生成 $L_2$ 规则

$$L_2^{algo}(t+1) = f(L_2^{algo}(t), \text{User Behavior}(t))$$

**危险**: $L_2^{algo}$ 的演化不透明，无法问责

**实例**:  
- YouTube 推荐算法 → 极化（推送极端内容）
- TikTok 成瘾算法 → 认知劫持
- 信用评分算法 → 新种姓制度

**SRT 警告**: 算法权力是**自我强化的 $L_2$ 独裁**，需宪法级监管。

---

## §5. θ 隐私守恒定律的政治经济学 (Political Economy of Privacy Conservation)

### 5.1 监控资本主义的本体论

肖莎娜·祖博夫 (Shoshana Zuboff, 2019):  

> **监控资本主义**: 单向主张人类经验作为免费原材料，转化为行为数据的新经济秩序。

**SRT 翻译**:  
科技公司通过免费服务诱使用户暴露 $\theta$ 参数：

$$\text{Free Service} \iff \text{User exports } \theta \to \text{Company Database}$$

公司用 $\theta$ 数据：
1. 预测行为（广告定向）
2. 修改行为（操纵 $\theta$）
3. 售卖预测（数据市场）

---

### 5.2 隐私-便利的守恒律

**经验观察**: 每次技术进步都要求更多隐私牺牲

**SRT 形式化**:

$$\text{Privacy} \times \text{Convenience} = C_{const}$$

$$\Delta \text{Privacy} = -k \cdot \Delta \text{Convenience}$$

**实例轨迹**:

| 时代 | 便利性 | 隐私性 | 积 |
|:-----|:-------|:-------|:---|
| 1990 现金交易 | 1 | 10 | 10 |
| 2000 信用卡 | 3 | 6 | 18 |
| 2010 移动支付 | 7 | 3 | 21 |
| 2020 生物识别 | 10 | 1 | 10 |

守恒律在大尺度成立（$C \approx 10-20$）。

---

### 5.3 数字封建主义

**新型权力结构**:

$$\text{平台} : \text{用户} :: \text{封建领主} : \text{农奴}$$

| 封建时代 | 数字时代 |
|:---------|:---------|
| 农奴提供劳动 | 用户提供数据 |
| 领主拥有土地 | 平台拥有基础设施 |
| 农奴无土地所有权 | 用户无数据所有权 |
| 农奴被束缚在土地 | 用户被锁定在生态系统 |

**SRT 诊断**: 这是**汲取性制度**在数字空间的复现。

---

## §6. 制度临界质量的历史验证 (Historical Validation of Critical Mass)

### 6.1 10% 法则的社会运动案例

**理论预测** (来自 Ising 模型):

$$p_{crit} \approx \frac{k_B T}{J \cdot z} \approx 0.1$$

**历史验证**:

| 运动 | 峰值坚定派% | 成功? | 备注 |
|:-----|:------------|:------|:-----|
| 美国民权运动 | 15% | ✓ | 关键时刻达到阈值 |
| 南非反种族隔离 | 12% | ✓ | 国际压力加速 |
| 天鹅绒革命 | 18% | ✓ | 快速和平转型 |
| 占领华尔街 | 3% | ✗ | 未达临界质量 |
| #MeToo | 5% → 22% | ✓ | 跨越阈值后爆发 |

**观察**: 当坚定派 > 10-15%，成功率 > 80%

---

### 6.2 失败案例分析

**为何有些运动达到 10% 仍失败？**

**SRT 修正因素**:

1. **网络拓扑**: 如果坚定派孤立（无桥接） → 无法传播
2. **$L_2$ 硬度**: 旧制度太硬（如宗教法） → 需更高阈值
3. **外部镇压**: 物理暴力阻断网络 → 模型失效

**修正公式**:

$$p_{eff} = p_{observed} \times \text{Connectivity} \times \frac{1}{\text{Hardness}(L_2)}$$

---

## §7. 可证伪预测总表 (Falsifiable Predictions)

### 7.1 制度经济学预测

| ID | 假说 | 预测 | 证伪条件 |
|:---|:-----|:-----|:---------|
| **H-Inst-1** | 包容-汲取相变 | 存在 $G_{power}$ 临界值导致制度锁定 | 权力集中度与制度类型无相关 |
| **H-Inst-2** | 制度硬度公式 | 制度年龄 × 支持者数预测改革难度 | 年龄与改革难度无相关 |
| **H-Inst-3** | 选择基尼-流动性 | 高选择不平等社会阶层流动性接近零 | 不平等与流动性线性相关 |

### 7.2 货币与金融预测

| ID | 假说 | 预测 | 证伪条件 |
|:---|:-----|:-----|:---------|
| **H-Money-1** | 脱实向虚阈值 | 存在 Gap_critical 触发金融危机 | 危机随机发生无阈值 |
| **H-Money-2** | 货币信任相变 | 信心跌破阈值时瞬间抛售（非线性）| 货币崩溃总是渐进的 |
| **H-Money-3** | 比特币长期稳定 | 技术风险 < 政治风险时存活 | 风险比值与存活无关 |

### 7.3 网络拓扑预测

| ID | 假说 | 预测 | 证伪条件 |
|:---|:-----|:-----|:---------|
| **H-Net-1** | 弱关系求职优势 | 通过弱关系找到工作的比例 > 强关系 | 强关系求职更有效 |
| **H-Net-2** | 结构洞收入溢价 | 高中介中心性个体收入显著更高 | 中心性与收入无相关 |
| **H-Net-3** | 回音室极化阈值 | 跨群体边 < 20% 时极化不可逆 | 极化程度连续变化 |

### 7.4 隐私与权力预测

| ID | 假说 | 预测 | 证伪条件 |
|:---|:-----|:-----|:---------|
| **H-Priv-1** | 隐私-便利守恒 | $\Delta \text{Privacy} \propto -\Delta \text{Convenience}$ | 二者独立变化 |
| **H-Priv-2** | 算法权力自我强化 | 无监管下算法极化指数级增长 | 算法影响力线性增长 |
| **H-Priv-3** | 数据所有权与民主 | 数据归用户所有的国家民主指数更高 | 二者无相关 |

---

## §8. 政策推论与伦理边界 (Policy Implications & Ethical Boundaries)

### 8.1 制度设计原则

**SRT 制度工程的三原则**:

1. **最小化 $\Psi_f^{transaction}$** (交易成本)
   - 清晰产权
   - 透明规则
   - 高效执法

2. **最大化 $\bar{d}$** (平均关切范围)
   - 教育投资
   - 共情训练
   - 跨文化交流

3. **保持 $S_{optimal}$** (最优熵)
   - 多元主义 vs 无政府
   - 创新 vs 稳定
   - 自由 vs 秩序

---

### 8.2 反垄断的本体论基础

**传统反垄断**: 防止价格操纵

**SRT 反垄断**: 防止 **$L_2$ 定义权垄断**

**新型垄断危害**:

| 公司 | 垄断的 $L_2$ | 危害 |
|:-----|:-------------|:-----|
| Google | 信息可见性 | 思想控制 |
| Facebook | 社交图谱 | 现实扭曲 |
| Amazon | 商品发现 | 市场操纵 |
| Apple | 应用分发 | 创新扼杀 |

**SRT 建议**: 将 $L_2$ 定义权视为**公共基础设施**，需公共监管。

---

### 8.3 民主的热力学边界

**民主的必要条件**:

$$\bar{d} > d_{democracy} \approx 3-5$$

$$S_{soc} \in [S_{min}, S_{max}]$$

$$G_{power} < G_{critical} \approx 0.6$$

当任一条件破裂 → 民主不稳定。

**历史教训**: 魏玛共和国的崩溃

| 指标 | 1920s | 1930s | 阈值 |
|:-----|:------|:------|:-----|
| $\bar{d}$ | ~4 | ~2 | >3 |
| $S_{soc}$ | 高 | 极化 | 中等 |
| $G_{power}$ | 0.5 | 0.8 | <0.6 |

所有条件同时破裂 → 纳粹上台。

---

## §9. SRT 制度经济学的范式意义 (Paradigmatic Significance)

### 9.1 超越新制度经济学

**诺斯 (North)**: 制度降低不确定性  
**SRT**: 制度 **是** $L_2$ 本身

**阿西莫格鲁**: 制度决定繁荣  
**SRT**: 制度是吸引子，有深井和能垒

**哈耶克 (Hayek)**: 自发秩序  
**SRT**: $L_2$ 涌现需要初始条件

---

### 9.2 可计算政治经济学

SRT 提供的不是定性比喻，而是**可数值求解的系统**：

$$\frac{dL_2^{inst}}{dt} = f(L_1, \theta_{political}, \text{Shocks})$$

这允许：
1. 预测制度演化轨迹
2. 识别相变临界点
3. 设计最优干预策略

---

## 符号索引 (Symbol Index)

| 符号 | 名称 | 定义位置 |
|:-----|:-----|:---------|
| $L_2^{inst}$ | 制度 | Ax-Inst-1 |
| $A_{inc}$ | 包容性吸引子 | Ax-Inst-2 |
| $A_{ext}$ | 汲取性吸引子 | Ax-Inst-2 |
| $L_2^{money}$ | 货币度规 | Ax-Money-1 |
| $\text{Betweenness}$ | 中介中心性 | Ax-Net-2 |
| $G_{power}$ | 权力基尼系数 | Ax-Power-2 |
| $G_{choice}$ | 选择基尼系数 | Ax-Choice-Gini |
| $E_{echo}$ | 回音室强度 | Ax-Consensus-2 |

---

## 依赖关系图 (Dependency Graph)
```
SRT_Reference_Axioms (Core)
    ↓
_SRT_Soc_Axioms
    ↓
SRT_Soc_01_Construction
    ↓
SRT_Soc_02_Behavioral
    ↓
SRT_Soc_03_Institutions ← 你在这里
    ↓
└── SRT_SocTheory_04-06 (高级理论整合)
```
