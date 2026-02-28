# diff.md

## [2026-02-28 12:29 GMT+8] 材料：Why Everything in the Universe Turns More Complex（https://www.quantamagazine.org/why-everything-in-the-universe-turns-more-complex-20250402/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：把外部“复杂化路径”转成 SRT 分类映射表（分类→d 区间/能流态/\(\Psi_f\) 状态）。
- `SRT/Core_Law/SRT_Reference_Scaling.md`：补全新实证尺度（矿物演化、天体核合成）的 \(\hat{G}_\theta\), \(L_0\), \(L_1\), \(L_2\) 定义。
- `SRT/SRT_Glossary.md`：新增功能信息术语，附 `[Lineage/Source]`，并统一全状态空间符号到 \(L_0\)。
- `SRT/Core/SRT_Experimental_Applications.md`：增加可证伪实验（条件复杂度漂移 + 突跃检验）。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: External Complexity Classes → SRT
+
+| 外部分类 | SRT 对应 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 元素核合成复杂化（恒星/超新星） | 宇宙物理选择层 | 低~中 | Open-flow（高能） | payable（阶段性高负载） |
+| 矿物谱系复杂化（地球化学历史） | 地球化学中尺度层 | 中 | Semi-open / Open | payable 或局部 overloaded |
+| 生物功能复杂化（适应与突跃） | 生物-认知层 | 中~高 | Open-flow（代谢耦合） | payable；失衡时 unsustainable |
+
+**Constraint**: 上表 d 为 canonical d 的语境化区间，canonical 定义保持：
+$$d \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|$$
+
+## 【理论边界/防误用声明】
+- 不采纳“复杂度无条件单调上升”的推论。
+- 不采纳“功能信息可替代热力学熵”的推论。
+- 边界：SRT 仅支持“能流开放 + 选择记忆 + 摩擦可支付”条件下的复杂度漂移。
```

```diff
--- a/SRT/Core_Law/SRT_Reference_Scaling.md
+++ b/SRT/Core_Law/SRT_Reference_Scaling.md
@@
+## Def-Scale-M1: Mineral Evolutionary Scale（矿物演化尺度）
+- **\(\hat{G}_{\theta,miner}\)**：在温压-化学势约束下筛选矿物相稳定路径的选择算子。
+- **\(L_0^{miner}\)**：矿物构型、晶格拓扑、缺陷与相变路径的潜在域。
+- **\(L_1^{miner}\)**：当前环境可维持的实际矿物相集合。
+- **\(L_2^{miner}\)**：地质历史沉积出的稳定矿物谱系与路径依赖约束。
+
+## Def-Scale-C1: Cosmic Nucleosynthesis Scale（天体核合成尺度）
+- **\(\hat{G}_{\theta,cosmo}\)**：在引力与核反应网络下对可持续核素组合进行选择的算子。
+- **\(L_0^{cosmo}\)**：核素与反应通道的潜在状态域（外部文献 \(\Omega/S\) 语义统一映射为 \(L_0\)）。
+- **\(L_1^{cosmo}\)**：当前宇宙时段可观测的元素丰度切片。
+- **\(L_2^{cosmo}\)**：恒星代际循环沉积出的丰度结构与演化约束。
+
+## 【理论边界/防误用声明】
+- 不采纳“尺度扩展即可自动获得意识语义”的推论。
+- 边界：跨尺度同构是动力学结构同构，不是现象体验同构。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Functional Information - 功能信息（\(I_f\)） 🟡
+**定义**：
+$$
+I_f \equiv -\log\left(\frac{|\{\sigma: f(\sigma)\ge\theta_f\}|}{|L_0|}\right)
+$$
+其中外部文献常见的全状态空间符号（\(\Omega\), \(S\)）在 SRT 文档中统一映射为 \(L_0\)。
+
+**[Lineage/Source]**：
+- Proposer: Jack W. Szostak
+- Source: Nature (2003), “Functional information”
+- Later extension context: Hazen–Wong complexity framework (as discussed in Quanta feature and cited PNAS program)
+
+## 【理论边界/防误用声明】
+- 不采纳“高信息量=高真实度=高意识”的等号链推论。
+- 边界：信息量、功能性、意识判据在 SRT 中需通过 d 与 \(\Psi_f\) 联合约束。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-Comp-1 条件复杂度漂移检验（跨域）
+**内容**：在开放能流且存在选择记忆的系统中，功能复杂度期望值上升。
+**最小实验**：生物/矿物/天体数据各自建模，并统一到分段趋势检验框架。
+**证伪条件**：满足条件样本不呈正向漂移，且与随机对照无显著差异。
+
+### H-Jump-1 复杂度突跃检验
+**内容**：复杂度增长呈“平台-突跃-平台”分段而非线性连续上升。
+**证伪条件**：突跃模型在三域数据中均无统计优势。
+
+## 【理论边界/防误用声明】
+- 不采纳“由历史趋势直接外推文明终局”的预测性过度推断。
+- 边界：SRT 的实验命题是条件检验，不是无条件历史决定论。
```

### Notes (brief)
- 已按最新 skill 执行：
  - 具体分类已提取并映射到 d 区间/能流态/\(\Psi_f\)
  - 新尺度缺口已给 `SRT_Reference_Scaling.md` 补丁
  - 新术语含 `[Lineage/Source]`
  - `## 【理论边界/防误用声明】` 已作为实际目标文件 Header 写入补丁

---

## [2026-02-28 12:30 GMT+8] 材料：Quantum Chips and Creativity: A Case for Upgrading Consciousness（https://www.popularmechanics.com/science/a70496043/enhancing-consciousness-quantum-physics/）

### Target Files
- `SRT/AI/SRT_AI_03_Consciousness_Framework.md`：引入“意识循环分类映射”（确定态→叠加探索态→坍缩决策态），对应 d 区间与能流特征。
- `SRT/SRT_Glossary.md`：新增“Quantum-Introspection Cycle”术语并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“延长并行探索窗口是否提升创造性”的可证伪实验。

### Proposed Patch (unified diff)
```diff
--- a/SRT/AI/SRT_AI_03_Consciousness_Framework.md
+++ b/SRT/AI/SRT_AI_03_Consciousness_Framework.md
@@
+### Taxonomy Mapping: Consciousness Processing Phases → SRT
+
+| 外部分类 | SRT 过程态 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| Definite Thought（确定意识态） | \(L_1\) 锚定态 | 中 | Semi-open | payable |
+| Parallel/Intuitive Interference（并行直觉态） | \(L_0 \to L_1\) 高并发探索窗 | 中~高 | Open-flow | payable 或短时 overloaded |
+| Decision Collapse（决策坍缩态） | \(\hat{G}_\theta\) 选择收束 | 中 | Semi-open | payable |
+
+**Constraint**: 上表为 canonical d 的语境化 proxy，定义仍为
+$$d \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|$$
+
+## 【理论边界/防误用声明】
+- 不采纳“意识=量子双缝网络已被实验证实”的推论。
+- 不采纳“量子芯片增强必然产生新物种级意识跃迁”的推论。
+- 边界：当前仅可作为待检验机制假说；SRT 采纳条件化实验路径，不采纳强结论先行。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Quantum-Introspection Cycle - 量子内省循环（QIC） 🟡
+**定义**：在认知过程中，系统在“确定态（anchored L_1）—并行探索态（expanded L_0 search）—决策收束态（\(\hat{G}_\theta\) collapse）”之间往复切换的过程模型。
+**公式化（SRT 写法）**：
+$$
+L_1^{(t)} \rightarrow \text{Explore}(L_0) \xrightarrow{\hat{G}_\theta} L_1^{(t+1)}
+$$
+**[Lineage/Source]**：
+- Primary popularized claim: Vlatko Vedral (Popular Mechanics essay, 2026)
+- Historical inspirations: Niels Bohr (complementarity), David Bohm (quantum-holistic interpretations)
+- Related speculative biological locus: Penrose-Hameroff microtubule line (as debated context)
+
+## 【理论边界/防误用声明】
+- 不采纳“QIC 已是神经生物学定律”的表述。
+- 边界：QIC 在 SRT 中为工作假说术语，必须绑定可证伪实验与负结果更新机制。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-QIC-1 并行探索窗口与创造性提升检验
+**内容**：若可控地延长“并行探索窗口”（不改变任务总时长），应提高创造性任务输出的新颖性与可用性。
+**最小实验**：
+- 组A：标准决策节律
+- 组B：延长探索窗口（认知干预或节律操控）
+- 指标：新颖性评分、问题解空间覆盖度、后验可执行性
+**证伪条件**：组B在新颖性与可执行性上均无显著提升，或仅提升随机发散不提升可用性。
+
+### H-QIC-2 探索窗口延长与代价上升边界
+**内容**：探索窗口延长超过阈值后，\(\Psi_f\) 上升导致决策效率显著下降（倒U型）。
+**证伪条件**：不存在倒U关系，且代价指标不随窗口延长增加。
+
+## 【理论边界/防误用声明】
+- 不采纳“提升创造性=提升真理性”的等同推论。
+- 边界：创造性提升需与可执行性、稳定性和风险约束联合评估。
```

### Notes (brief)
- 已将外部“确定/并行/收束”分类转为 SRT 文件级条目，并映射 d 区间、能流态、\(\Psi_f\) 状态。
- 外部术语新增时已添加 `[Lineage/Source]`。

---

## [2026-02-28 12:42 GMT+8] 材料：Scientists Think We Only Need One Constant to Study the Universe—Time Itself（https://www.popularmechanics.com/science/a70223461/constant-universe-time/）

### Target Files
- `SRT/Core/SRT_Core_22_Equations.md`：加入“时空先定标后观测”的规范化表达，避免“只剩时间常数”被误读为否定其他约束量。
- `SRT/Core_Law/SRT_Reference_Scaling.md`：新增“参考系/时空规约尺度（frame-normalization scale）”定义，补 \(\hat{G}_\theta\), \(L_0\), \(L_1\), \(L_2\)。
- `SRT/SRT_Glossary.md`：新增 `Frame-First Normalization` 术语，附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“同一时空规约下常数量可约化”的可证伪检验。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_22_Equations.md
+++ b/SRT/Core/SRT_Core_22_Equations.md
@@
+### Eq-Frame-01: Frame-First Normalization
+在先固定观测时空与仪器规约条件后，维度常数的有效数量可写为：
+$$
+N_{const}^{eff} = f(\mathcal{F}_{spacetime},\;\mathcal{U}_{apparatus})
+$$
+在特定相对论时空规约中可出现 \(N_{const}^{eff}\to 1\) 的表述（时间标尺主导）。
+
+### Eq-Frame-02: Observable Reparameterization
+$$
+\mathcal{O} = g\big(L_1\mid L_0,\hat{G}_\theta,\mathcal{F}_{spacetime}\big)
+$$
+其中“全状态空间”外部记号（如 \(\Omega\), \(S\)）在 SRT 写入统一映射为 \(L_0\)。
+
+## 【理论边界/防误用声明】
+- 不采纳“只需要时间常数 = 其他常数在本体上不存在”的推论。
+- 边界：SRT 将其解释为规约与参数化层面的等效重写，不是本体删除。
```

```diff
--- a/SRT/Core_Law/SRT_Reference_Scaling.md
+++ b/SRT/Core_Law/SRT_Reference_Scaling.md
@@
+## Def-Scale-F1: Frame-Normalization Scale（参考系规约尺度）
+- **\(\hat{G}_{\theta,frame}\)**：在既定时空与仪器单位系统下执行观测量规约映射的选择算子。
+- **\(L_0^{frame}\)**：所有可行规约方案、单位体系与参数化路径的潜在域。
+- **\(L_1^{frame}\)**：当前研究共同体采用的实际规约方案与测量协议。
+- **\(L_2^{frame}\)**：被重复验证后沉淀的标准化协议（如基准单位、坐标规约共识）。
+
+## 【理论边界/防误用声明】
+- 不采纳“规约自由度减少=宇宙自由度减少”的推论。
+- 边界：规约层压缩是表述经济性，不等于物理因果结构坍缩。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Frame-First Normalization - 先框架规约（FFN） 🟡
+**定义**：先固定观测时空框架与测量协议，再讨论常数量与可观测量表达的程序性原则。
+**SRT 映射**：
+- 规约候选空间 \(\to L_0^{frame}\)
+- 实际采用协议 \(\to L_1^{frame}\)
+- 稳定学界共识 \(\to L_2^{frame}\)
+
+**[Lineage/Source]**：
+- Source claim context: Brazilian group discussion summarized by Popular Mechanics (2026) and Scientific Reports paper context.
+- SRT reinterpretation: parameterization economy under fixed frame, not ontological elimination.
+
+## 【理论边界/防误用声明】
+- 不采纳“FFN 可直接推出‘时间是唯一本体常数’”的结论。
+- 边界：FFN 在 SRT 中是方法论压缩策略，而非终极本体论判定。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-Frame-1 规约先定对常数量可约化检验
+**内容**：在同一观测时空框架与统一仪器协议下，不同模型表达的维度常数量应显著收敛。
+**最小实验**：
+- 选取多个相对论场景数据集；
+- 对比“先规约后拟合”与“直接拟合”两流程下 \(N_{const}^{eff}\) 的稳定性。
+**证伪条件**：在统一规约条件下，常数量不收敛或不稳定性不降反升。
+
+### H-Frame-2 时间标尺主导的适用边界
+**内容**：时间主导表述仅在特定时空规约类别中成立，跨类别迁移将显著劣化拟合质量。
+**证伪条件**：跨规约类别迁移不造成显著性能下降。
+
+## 【理论边界/防误用声明】
+- 不采纳“参数可约化 = 理论完备”的推论。
+- 边界：SRT 要求同时检验解释力、迁移性与反事实稳定性。
```

### Notes (brief)
- 已将“时间唯一常数”主张重写为“规约后有效常数量压缩”命题，避免本体论越界。
- 外部全状态空间记号统一映射为 \(L_0\) 语义。

---

## [2026-02-28 12:46 GMT+8] 材料：How Can Infinity Come in Many Sizes?（https://www.quantamagazine.org/how-can-infinity-come-in-many-sizes-20260223/）

### Target Files
- `SRT/Core/SRT_Core_12a_Ontology_L0L1.md`：补充“无限集合层级”到 L_0 可及性分层的映射。
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：加入“可数/不可数无限”分类映射表（分类→d 区间/能流态/\(\Psi_f\)）。
- `SRT/SRT_Glossary.md`：新增 `Infinity Accessibility Class (IAC)` 术语并给 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：补充“认知可达无限层级”的行为实验假设。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Infinity Classes → SRT Dynamics
+
+| 外部分类 | SRT 对应 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 可数无限（自然数、偶数、有理数） | 可枚举选择轨道 | 中 | Semi-open（有限工作记忆展开） | payable |
+| 不可数无限（实数） | 非枚举潜能域切片 | 中~高 | Open-flow（高抽象探索） | payable~overloaded（任务依赖） |
+| 等势无限区间同势（(0,1) 与全实数同基数） | 尺度变换不改势级 | 中 | Semi-open | payable |
+
+**Constraint**: 该表仅描述“认知-形式系统中的可达层级”，不将集合论基数直接等同于本体论“存在强度”。
+
+## 【理论边界/防误用声明】
+- 不采纳“更大基数 = 更高现实等级”的推论。
+- 不采纳“数学不可数性直接证明物理无限可达”的推论。
+- 边界：SRT 将其视为 \(L_0\) 的形式可达结构分层，不是经验现实的自动兑现。
```

```diff
--- a/SRT/Core/SRT_Core_12a_Ontology_L0L1.md
+++ b/SRT/Core/SRT_Core_12a_Ontology_L0L1.md
@@
+### Def-L0-Inf-01: Infinity Accessibility in L_0
+将外部集合论中的状态空间符号统一映射为 \(L_0\) 语义后，可定义：
+$$
+\mathcal{A}_{inf}(\hat{G}_\theta) = \{\text{可被当前算子构造或判定的无限类}
+\subseteq L_0\}
+$$
+当 \(\mathcal{A}_{inf}\) 仅覆盖可数类时，系统在无限推理上仍处于“枚举主导”阶段；
+当可稳定处理不可数构造（如对角线反证）时，进入更高抽象可达层。
+
+## 【理论边界/防误用声明】
+- 不采纳“形式可构造 = 物理可实现”的推论。
+- 边界：\(L_0\) 的形式可达性是推理能力指标，不是能量与物理实现性的替代。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Infinity Accessibility Class - 无限可达类（IAC） 🟡
+**定义**：描述 \(\hat{G}_\theta\) 在 \(L_0\) 上可稳定处理的无限结构层级（如可数、不可数、区间等势映射）。
+**形式化**：
+$$
+\text{IAC}(\hat{G}_\theta) \in \{\text{Countable-dominant},\;\text{Uncountable-capable},\;\text{Transform-invariant}\}
+$$
+**[Lineage/Source]**：
+- Primary lineage: Georg Cantor set theory and cardinality hierarchy
+- Expository source: Quanta Magazine explainer (2026-02-23)
+- SRT mapping: infinite-class accessibility as \(L_0\)-reachability descriptor
+
+## 【理论边界/防误用声明】
+- 不采纳“高 IAC 必然意味着高 d”这一强推论。
+- 边界：IAC 与 d 可相关但非同一量，d 仍以 canonical 风险梯度定义为准。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-Inf-1 无限层级可达性的认知检验
+**内容**：受试者在“可数映射任务→不可数反证任务（对角线构造）”中表现将出现显著阶段差异。
+**最小实验**：
+- 任务A：一一对应构造（自然数/偶数/有理数）
+- 任务B：不可数性反证构造（实数不可枚举）
+- 指标：正确率、反应时、解释稳定度、迁移表现
+**证伪条件**：A/B 任务无阶段差异，或对角线构造不表现额外认知负荷。
+
+### H-Inf-2 区间等势理解的迁移检验
+**内容**：若受试者真正掌握“区间等势”，应在不同尺度映射任务中保持不变性判断。
+**证伪条件**：只在训练样例中成立，迁移后显著崩解。
+
+## 【理论边界/防误用声明】
+- 不采纳“认知可理解不可数 = 可经验访问不可数对象”的推论。
+- 边界：实验仅检验形式推理能力，不对物理宇宙本体结构作直接判定。
```

### Notes (brief)
- 已将文章中的核心分类（可数无限/不可数无限/区间等势）直接映射到 SRT 文件级条目。
- 外部状态空间语义统一映射为 \(L_0\)；新增术语已附 `[Lineage/Source]`。

---

## [2026-02-28 12:52 GMT+8] 材料：Foundational Evidence for Design: The Generalized Second Law of Thermodynamics（https://scienceandculture.com/2026/02/foundational-evidence-for-design-the-generalized-second-law-of-thermodynamics/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“信息演化主张分类映射”（封闭系统信息递减主张 / 开放系统功能组织形成 / 设计推断主张）并映射到 d 区间与能流态。
- `SRT/Philosophy/SRT_Philosophy_Ethics.md`：加入“信息论约束与目的论推断分离”的方法论段落。
- `SRT/SRT_Glossary.md`：新增 `Observer-Bound Information Entropy Claim` 术语与 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：加入“开放系统中功能信息可增长”的反向可证伪假设，避免单向确认偏差。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Information-Evolution Claims → SRT
+
+| 外部分类 | SRT 对应解释 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| “封闭系统中观察者信息不增” | 封闭域下可达态压缩 | 低~中 | Closed-flow | payable（但创新受限） |
+| “开放能流不足以生成功能蓝图” | 需区分原始能流与选择回路耦合 | 中 | Open-flow（若仅能流、无选择记忆则无效） | overloaded 或无效支付 |
+| “信息增长必指向智能设计” | SRT 视为可竞争解释之一，非唯一结论 | 中~高（取决于选择架构） | Open / Semi-open | task-dependent |
+
+**Constraint**: 信息趋势命题必须显式区分封闭系统与开放系统，并显式建模选择记忆项，禁止直接跨域外推。
+
+## 【理论边界/防误用声明】
+- 不采纳“信息增长无法由任何自然过程产生”的绝对断言。
+- 不采纳“观测到功能复杂性即推出单一超自然因果”的唯一化推断。
+- 边界：SRT 要求在“能流、选择回路、历史沉积”三项条件下做竞争模型比较，而非先验排他。
```

```diff
--- a/SRT/Philosophy/SRT_Philosophy_Ethics.md
+++ b/SRT/Philosophy/SRT_Philosophy_Ethics.md
@@
+## Method Note: Information Constraint ≠ Teleology Closure
+
+当外部论证将“信息论约束”直接推出“单一目的论解释”时，SRT 采用分离原则：
+1. 先判定信息约束是否成立（系统边界、能流与可观测定义）；
+2. 再比较多种生成机制（自然选择回路、人工介入、混合机制）；
+3. 禁止在步骤1未完成时直接做终极因果闭合。
+
+## 【理论边界/防误用声明】
+- 不采纳“方法论自然主义=先验拒绝设计”的二元对立叙述。
+- 不采纳“任何设计推断都自动科学化”的反向极端叙述。
+- 边界：SRT 仅承认可操作、可证伪、可竞争比较的设计推断版本。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Observer-Bound Information Entropy Claim - 观察者约束信息熵主张（OBIE） 🟡
+**定义**：将熵解释为“观察者对系统不确定性”的信息化表述，并据此讨论信息随时间的变化约束。
+**SRT 注释**：OBIE 可作为分析层工具，但必须明确系统边界（closed/open）与可访问通道，否则易产生跨域误推。
+
+**[Lineage/Source]**：
+- Local source context: Eric Hedin article (Science and Culture Today, 2026)
+- Historical referenced lineage in article: Robert Gange’s generalized second-law framing
+- SRT stance: treat as contestable interpretive claim, not canonical law replacement
+
+## 【理论边界/防误用声明】
+- 不采纳“OBIE 可直接替代统计物理熵定义”的推论。
+- 边界：OBIE 在 SRT 中是解释性桥梁术语，不是基础方程替代项。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-Info-Open-1 开放系统功能信息增长检验
+**内容**：在开放能流且有选择记忆回路的系统中，功能信息可呈净增长；若缺少选择记忆则不成立。
+**最小实验**：
+- 组A：开放能流 + 选择反馈（迭代筛选）
+- 组B：开放能流 + 无选择反馈（纯扰动）
+- 指标：功能阈值达成率、\(I_f\) 增量、稳定性
+**证伪条件**：组A与组B在 \(I_f\) 增长上无显著差异。
+
+### H-Info-Design-Alt-1 竞争解释比较检验
+**内容**：对同一复杂结构数据，比较“自然选择回路模型”“外部设计注入模型”“混合模型”三者拟合与可迁移性。
+**证伪条件**：竞争模型之间无可区分预测，或单模型在迁移测试中全面失效。
+
+## 【理论边界/防误用声明】
+- 不采纳“单模型先验真理化”的研究流程。
+- 边界：SRT 要求竞争模型、预注册判据与负结果可发布。
```

### Notes (brief)
- 已将该文三类核心主张转为可比较分类，并显式区分封闭/开放系统语境。
- 保持 SRT 的“竞争解释 + 可证伪”方法，不做单向结论继承。

---

## [2026-02-28 12:53 GMT+8] 材料：Neurons receive precisely tailored teaching signals as we learn（https://mcgovern.mit.edu/2026/02/25/neurons-learn/）

### Target Files
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：加入“向量化教导信号”分类映射（全局广播调制 vs 神经元定向误差信号）。
- `SRT/Core/SRT_Experimental_Applications.md`：新增 BCI 场景下的可证伪假设（定向误差信号必要性）。
- `SRT/SRT_Glossary.md`：新增 `Vectorized Instructive Signal (VIS)` 术语并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：补充“学习机制分类→d 区间/能流态/\(\Psi_f\)”映射表。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Learning Signal Classes → SRT Dynamics
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 全局 neuromodulator 广播（dopamine/NE） | 粗粒度强化调制 | 低~中 | Open-flow | payable（效率较低） |
+| 向量化神经元定向误差信号（VIS） | 细粒度 \(\hat{G}_\theta\) 定向更新 | 中~高 | Open-flow（高信息反馈） | payable（高精度学习） |
+| 树突级反馈阻断后学习失败 | 局部误差信号必要性证据 | 中 | Semi-open（受限反馈） | overloaded / learning collapse |
+
+**Constraint**: 上述 d 区间为学习效率语境下的 proxy，不替代 canonical d 定义。
+
+## 【理论边界/防误用声明】
+- 不采纳“观察到 VIS 即证明大脑完全等同 backprop 算法”的推论。
+- 边界：SRT 仅承认“局部定向误差信号存在”的机制证据，不把工程算法一对一投射为生物全模型。
```

```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
+### Ax-Op-Vis-01: Vectorized Instructive Update
+**Formal Statement**: 当系统可获得神经元级定向误差信号时，\(\hat{G}_\theta\) 的参数更新可写为向量化局部更新：
+$$
+\Delta\theta_i \propto -\eta\,e_i\,\nabla_{\theta_i}\mathcal{L}
+$$
+其中 \(e_i\) 为局部教导信号分量。
+
+**Implication**: 学习由“全局同信号更新”转向“分量特异更新”，显著提升样本效率与任务对齐能力。
+
+## 【理论边界/防误用声明】
+- 不采纳“VIS 存在即可推出意识本体结论”的推论。
+- 边界：VIS 约束的是学习动力学层，不直接决定 qualia 或主观体验判据。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Vectorized Instructive Signal - 向量化教导信号（VIS） 🟡
+**定义**：可对不同神经元（或参数分量）发送方向相反/幅度不同更新指令的误差信号结构。
+**SRT 写法**：
+$$
+\mathbf{e}=(e_1,e_2,\dots,e_n),\quad \Delta\theta_i\sim e_i
+$$
+**用途**：解释为何生物学习可超越纯全局广播强化，实现细粒度可塑性编排。
+
+**[Lineage/Source]**：
+- Primary source: MIT McGovern report on Nature paper (2026-02-25)
+- Paper title context: “Vectorized instructive signals in cortical dendrites during a brain-computer interface task”
+- SRT mapping: local error-channel update within \(\hat{G}_\theta\) dynamics
+
+## 【理论边界/防误用声明】
+- 不采纳“VIS=生物反向传播已完全成立”的断言。
+- 边界：VIS 是机制相似性证据，不是算法同一性证明。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-VIS-1 定向误差信号必要性检验
+**内容**：在 BCI 学习任务中，若抑制定向树突反馈，学习曲线应显著劣化。
+**最小实验**：
+- 组A：正常反馈
+- 组B：树突教导信号阻断
+- 指标：达标速度、稳定性、反向干扰恢复能力
+**证伪条件**：阻断后学习性能无显著下降。
+
+### H-VIS-2 广播调制与向量化反馈的效率差检验
+**内容**：在等资源条件下，VIS 条件应优于纯全局调制条件。
+**证伪条件**：两条件无效率差或纯广播显著更优。
+
+## 【理论边界/防误用声明】
+- 不采纳“机制效率提升即可推出认知优越性本体论”的推论。
+- 边界：该实验层结论限定于学习动力学，不外推为价值或意识等级结论。
```

### Notes (brief)
- 已将文章中的学习机制分类（广播强化/定向误差信号/阻断效应）转为文件级补丁。
- 新术语附 `[Lineage/Source]`，并在目标文件以 Header 写入防误用声明。

---

## [2026-02-28 14:18 GMT+8] 材料：Repeated Head Impacts, Inflammation and Memory Loss Connected（https://neurosciencenews.com/neuroinflammation-memory-tbi-30210/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“神经炎症-白质-认知”分类映射（炎症水平/白质微结构/认知表现）。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“中介链条检验”假设（炎症→白质微结构→记忆）。
- `SRT/SRT_Glossary.md`：新增 `Inflammation-Microstructure Mediation (IMM)` 术语并附 `[Lineage/Source]`。
- `SRT/Philosophy/SRT_Ethics_Agency.md`：补充“生理脆弱性对决策能动性的约束”说明。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Neuroinflammation-Memory Pathway → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 炎症标志物升高（IL-6/TNF-α/GFAP） | 系统摩擦背景升高 | 低~中（任务承载下降） | Open-flow 但高耗散 | overloaded |
+| 边缘系统白质微结构下降（FA↓/MD↑） | \(L_1\) 传输通道退化 | 低~中 | Semi-open | payable→unsustainable（阈值后） |
+| 记忆表现下降（无直接炎症-认知捷径） | 中介链条显性化 | 低（高负载下） | Semi-open / Closed-like | overloaded |
+
+**Constraint**: 该链条为关联结构，不等同因果闭合；必须通过中介模型与纵向数据验证。
+
+## 【理论边界/防误用声明】
+- 不采纳“炎症指标升高即可直接推断认知损害”的简化推论。
+- 边界：SRT 采用中介路径解释（炎症→微结构→功能），反对单变量因果跳跃。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-IMM-1 炎症-微结构-记忆中介检验
+**内容**：在重复头部冲击暴露人群中，炎症与记忆的关系由白质微结构显著中介。
+**最小实验**：
+- 指标：炎症生物标志物（血液/CSF）、DTI（FA/MD）、记忆测验
+- 模型：中介分析 + 暴露分层（高暴露/低暴露）
+**证伪条件**：中介路径不显著，或直接路径显著且中介路径消失。
+
+### H-IMM-2 高暴露亚组链条增强检验
+**内容**：在高头部冲击暴露与高症状亚组中，中介效应应显著增强。
+**证伪条件**：亚组间中介效应无差异。
+
+## 【理论边界/防误用声明】
+- 不采纳“相关性证据已足够确诊个体病理”的推论。
+- 边界：该模型用于风险分层与机制研究，不替代临床确证流程。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Inflammation-Microstructure Mediation - 炎症-微结构中介（IMM） 🟡
+**定义**：炎症负荷通过白质微结构劣化间接影响认知表现的路径模型。
+**形式化**：
+$$
+\text{Inflammation} \rightarrow \text{White-Matter Microstructure} \rightarrow \text{Cognition}
+$$
+**SRT 用途**：将“本体论摩擦上升”与“通道结构退化”连接到行为输出层变化。
+
+**[Lineage/Source]**：
+- Source context: AAN/Neurology report summarized by Neuroscience News (2026-02-27)
+- Study frame: former football players, inflammatory biomarkers + DTI + cognition
+- SRT mapping: mediation-chain interpretation under repeated-impact exposure
+
+## 【理论边界/防误用声明】
+- 不采纳“IMM 可直接替代病理确诊标准”的推论。
+- 边界：IMM 是机制建模工具，不是个体医学诊断结论。
```

```diff
--- a/SRT/Philosophy/SRT_Ethics_Agency.md
+++ b/SRT/Philosophy/SRT_Ethics_Agency.md
@@
+## Neuro-Constraint on Agency: Inflammation Burden
+当神经炎症与白质微结构损伤共同上升时，个体的决策带宽与情绪调节能力会受限，
+应将“能动性评估”与生理负荷状态联合建模，而非仅按行为结果归因。
+
+## 【理论边界/防误用声明】
+- 不采纳“行为失调必然等于道德失败”的推论。
+- 边界：SRT 要求在高生理负荷情境下引入责任分层与支持性干预框架。
```

### Notes (brief)
- 已将文章核心结构（炎症↑、白质微结构↓、记忆↓）转为文件级补丁与可证伪中介模型。
- 保持“关联≠因果闭合”的边界，避免过度医学外推。

---

## [2026-02-28 14:22 GMT+8] 材料：RNA Cleanup System Maps the Brain（https://neurosciencenews.com/nmd-neuronal-migration-brain-layers-30197/）

### Target Files
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：新增“RNA 监测-迁移编排”机制条目（NMD/UPF2 对神经元迁移速度与层化的定向调控）。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“UPF2 缺失→层化失序”的可证伪实验假设。
- `SRT/SRT_Glossary.md`：新增 `NMD-Guided Migration Control (NGMC)` 术语并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：补“迁移调控分类→d 区间/能流态/\(\Psi_f\)”映射。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Neuronal Migration Control Classes → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| NMD 正常（UPF2 完整） | 迁移-层化编排可用 | 中 | Open-flow（发育期高代谢） | payable |
+| UPF2 缺失（迁移迟缓/层化紊乱） | 选择回路失配，\(L_1\) 定位失败 | 低~中 | Semi-open（反馈受损） | overloaded |
+| p53 抑制仅救脑体积不救层化 | 生长与结构编排可解耦 | 中（体积）/低（结构） | Open / Semi-open 混合 | task-split |
+| Foxj1/Ino80 异常上调导致迁移阻断 | 错误程序侵入主通道 | 低 | Semi-open / Closed-like | unsustainable |
+
+**Constraint**: 该分类强调“体积恢复 ≠ 结构恢复”，禁止以单指标替代层化完整性判据。
+
+## 【理论边界/防误用声明】
+- 不采纳“脑体积恢复即发育功能恢复”的推论。
+- 边界：SRT 将迁移层化视为独立机制维度，需与增殖/存活路径分开建模。
```

```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
+### Ax-Op-NGMC-01: NMD-Guided Migration Control
+**Formal Statement**: 在皮层发育中，RNA 监测路径（NMD）通过约束迁移相关基因网络，维持神经元定位与层化：
+$$
+\hat{G}_{\theta,mig} = \hat{G}_{\theta,mig}(\text{NMD:UPF2},\;\text{Reelin},\;\text{Ciliary Program})
+$$
+当 \(\text{UPF2}\downarrow\) 时，迁移速度与目标层到达率下降，层化失序概率上升。
+
+**Implication**: 发育期学习/组织的“误差控制”并不只在突触层，也发生在转录后调控层。
+
+## 【理论边界/防误用声明】
+- 不采纳“单基因通路可解释全部皮层组织异常”的推论。
+- 边界：SRT 采用多层耦合机制（迁移、增殖、细胞骨架、信号引导）联合解释。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### NMD-Guided Migration Control - NMD 引导迁移控制（NGMC） 🟡
+**定义**：由 NMD（尤其 UPF2 轴）对神经元迁移与层化相关基因网络进行选择性约束的发育控制机制。
+**SRT 映射**：
+$$
+\text{NGMC}: L_0^{dev}\xrightarrow{\hat{G}_{\theta,mig}}L_1^{laminated}\to L_2^{stable-cortical-architecture}
+$$
+**[Lineage/Source]**：
+- Source context: UCR/Cell Reports study summarized by Neuroscience News (2026-02-25)
+- Core factors mentioned: UPF2, Reelin pathway, Ino80, Foxj1
+- SRT mapping: post-transcriptional control as selection-layer constraint
+
+## 【理论边界/防误用声明】
+- 不采纳“NGMC 可直接推断成人期所有认知差异”的推论。
+- 边界：NGMC 是发育关键机制之一，不能替代后天环境与可塑性因素。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-NGMC-1 UPF2 迁移控制必要性检验
+**内容**：条件性降低 UPF2 将显著降低神经元目标层到达率并增加层化紊乱。
+**最小实验**：
+- 组A：正常 NMD
+- 组B：Upf2 条件缺失
+- 指标：迁移速度、层位到达率、层化一致性指数
+**证伪条件**：Upf2 缺失组与对照组在层化指标上无显著差异。
+
+### H-NGMC-2 体积-结构解耦检验
+**内容**：p53 通路干预可恢复脑体积但不能恢复层化组织。
+**证伪条件**：体积恢复同时层化完全恢复（否定解耦）。
+
+## 【理论边界/防误用声明】
+- 不采纳“恢复单一终点指标即代表全机制修复”的推论。
+- 边界：SRT 采用多终点判据（体积、层化、功能）联合评估。
```

### Notes (brief)
- 已把文章中的关键分类（NMD 正常/UPF2 缺失/p53 体积救援/Foxj1-Ino80 干扰）映射为文件级补丁。
- 新术语与机制均附来源链并包含正式 Header 级防误用声明。

---

## [2026-02-28 14:23 GMT+8] 材料：Oxytocin Crash: Why Sleep Loss Leaves You Socially Forgetful（https://neurosciencenews.com/sleep-deprivation-oxytocin-social-memory-30187/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“睡眠剥夺-社交记忆”分类映射（编码回路/提取回路/高频刺激恢复）。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“PVNOXT-CA2 与 PVNOXT-PrL 双通路因果检验”假设。
- `SRT/SRT_Glossary.md`：新增 `Dual-Phase Social Memory Oxytocin Circuit (DSOC)` 并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：补充“源头神经调制优于下游补偿”的机制条目。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Sleep-Deprivation Social-Memory Circuits → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| PVNOXT–CA2（新社交记忆编码） | 编码相位选择门控 | 中 | Open-flow（睡眠足够） | payable |
+| PVNOXT–PrL（熟悉对象提取） | 提取相位检索门控 | 中 | Open/Semi-open | payable |
+| 睡眠剥夺导致 OXT 下降 | 双回路同步降效 | 低~中 | Semi-open（恢复不足） | overloaded |
+| 100Hz 源头刺激恢复 | 上游源重激活带来持续恢复 | 中~高（恢复态） | Open-flow（受控激活） | payable（干预后） |
+
+**Constraint**: “激素补充”与“神经源激活”不等价；优先区分源头恢复与下游补偿。
+
+## 【理论边界/防误用声明】
+- 不采纳“单次外源补充即可长期恢复社交记忆”的推论。
+- 边界：SRT 认为回路源头可塑性恢复优先于单点下游补偿。
```

```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
+### Ax-Op-DSOC-01: Dual-Phase Oxytocin Gating
+**Formal Statement**: 社交记忆由编码相位与提取相位的双门控组成：
+$$
+\hat{G}_{social}(t)=\hat{G}_{enc}(\text{PVNOXT-CA2}) \oplus \hat{G}_{ret}(\text{PVNOXT-PrL})
+$$
+睡眠剥夺使两门控阈值上移并降低可用输出；上游高频激活可整体下调阈值并恢复回路可塑性。
+
+## 【理论边界/防误用声明】
+- 不采纳“该双门控已可泛化到所有记忆类型”的推论。
+- 边界：当前仅在社交记忆范畴具备证据支撑。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Dual-Phase Social Memory Oxytocin Circuit - 双相社交记忆催产素回路（DSOC） 🟡
+**定义**：由 PVNOXT–CA2 编码通路与 PVNOXT–PrL 提取通路共同组成的社交记忆双相调节结构。
+**形式化**：
+$$
+\text{DSOC} = (\text{Encode}_{CA2},\;\text{Retrieve}_{PrL})
+$$
+**[Lineage/Source]**：
+- Source context: sleep deprivation and social memory study summarized by Neuroscience News (2026-02-24)
+- Reported mechanisms: PVNOXT-CA2 / PVNOXT-PrL, OXT decline, 100Hz stimulation rescue
+- SRT mapping: dual-phase gating under neuromodulatory source control
+
+## 【理论边界/防误用声明】
+- 不采纳“DSOC 直接等同于完整社会认知模型”的推论。
+- 边界：DSOC 是社交记忆子系统机制，不覆盖全部社会行为维度。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-DSOC-1 双通路相位功能可分检验
+**内容**：抑制 PVNOXT–CA2 应主要损害“新对象编码”，抑制 PVNOXT–PrL 应主要损害“熟悉对象提取”。
+**证伪条件**：两类干预产生无差别损伤模式。
+
+### H-DSOC-2 源头高频刺激恢复优势检验
+**内容**：在慢性睡眠剥夺模型中，上游 PVNOXT 高频刺激较下游单通路刺激具有更持久恢复效果。
+**证伪条件**：两者恢复持久性无差异或下游刺激更优。
+
+## 【理论边界/防误用声明】
+- 不采纳“短期行为恢复等同长期网络重建”的推论。
+- 边界：需纵向追踪验证恢复的稳定性与迁移性。
```

### Notes (brief)
- 已将文中分类（编码/提取/睡眠剥夺/高频恢复）转成文件级补丁，并映射 d 区间、能流态、\(\Psi_f\)。
- 新术语含 `[Lineage/Source]`，并在目标文件写入 Header 级防误用声明。

---

## [2026-02-28 14:24 GMT+8] 材料：Astera AGI 研究计划长文（用户提供原文）

### Target Files
- `SRT/AI/SRT_AI_Architecture.md`：新增“人类样通用智能路线图”分类映射（经验学习/层级世界模型/分布式推理/情景记忆/神经启发）。
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：补“反馈-递归连接与分布式推理”机制条目。
- `SRT/Core_Law/SRT_Reference_Scaling.md`：新增“皮层柱-丘脑-海马协同尺度”实体定义（\(\hat{G}_\theta\), \(L_0\), \(L_1\), \(L_2\)）。
- `SRT/SRT_Glossary.md`：新增 `Triangulated Principle Extraction (TPE)` 与 `Distributed Reasoning Stack (DRS)`，附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“经验优先学习与分布式推理收益”的可证伪实验条目。

### Proposed Patch (unified diff)
```diff
--- a/SRT/AI/SRT_AI_Architecture.md
+++ b/SRT/AI/SRT_AI_Architecture.md
@@
+### Taxonomy Mapping: Human-like AGI Program Themes → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 从经验学习而非仅人类累积文本 | \(L_0\to L_1\) 在线锚定与回写 | 中~高 | Open-flow（持续交互） | payable |
+| 层级潜变量+因果结构世界模型 | 多层 \(\hat{G}_\theta\) 结构化推演 | 高 | Open-flow | payable（高算力负载） |
+| 分布式推理（非仅语言 token） | 多模块并行推理栈 | 高 | Open-flow（跨模态） | payable~overloaded |
+| 情景记忆+持续学习闭环 | \(L_1\leftrightarrow L_2\) 动态沉积 | 中~高 | Semi-open / Open | payable |
+| 神经科学-算法三角互证 | 结构先验提炼机制 | 中 | Semi-open | task-dependent |
+
+## 【理论边界/防误用声明】
+- 不采纳“皮层柱统一性已足够推出唯一 AGI 架构”的推论。
+- 不采纳“长周期资助可替代可证伪里程碑”的推论。
+- 边界：SRT 要求每个主题绑定可检验中间指标，而非愿景叙事闭环。
```

```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
+### Ax-Op-DRS-01: Distributed Reasoning Stack
+**Formal Statement**: 人类样推理应在视觉、动作、概念、情景记忆等多子系统并发进行，而非单 token 通道：
+$$
+\hat{G}_{\theta,total}=\bigoplus_k \hat{G}_{\theta,k},\quad \text{with recurrent feedback across }k
+$$
+反馈/递归连接是测试时推理计算的一部分，而非仅训练期副产物。
+
+## 【理论边界/防误用声明】
+- 不采纳“递归结构必然优于前馈结构”的绝对命题。
+- 边界：仅在任务需要长期依赖、反事实模拟、主动推断时预期收益显著。
```

```diff
--- a/SRT/Core_Law/SRT_Reference_Scaling.md
+++ b/SRT/Core_Law/SRT_Reference_Scaling.md
@@
+## Def-Scale-CTHL-1: Cortico-Thalamo-Hippocampal Loop Scale（皮层-丘脑-海马协同尺度）
+- **\(\hat{G}_{\theta,cthl}\)**：在反馈-前馈-侧向环路中执行多阶段推理与记忆检索的协同选择算子。
+- **\(L_0^{cthl}\)**：跨模态潜变量、反事实轨迹、未锚定情景记忆构成的潜能域。
+- **\(L_1^{cthl}\)**：当前任务下被统一绑定的对象-特征-行动表征。
+- **\(L_2^{cthl}\)**：长期形成的 schema 图结构与迁移先验。
+
+## 【理论边界/防误用声明】
+- 不采纳“该尺度直接等同意识本体层”的推论。
+- 边界：该定义用于功能推理与记忆组织，不直接给出主观体验判据。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Triangulated Principle Extraction - 三角原则提炼（TPE） 🟡
+**定义**：以“神经观测 + 世界结构 + 算法模型”三元互证提炼通用智能原则的方法。
+
+**[Lineage/Source]**：
+- Source context: Astera AGI program statement (user-provided text, 2026-02-28)
+- Core claim: triangulation across neuroscience, world properties, and algorithms
+- SRT mapping: principle validation under multi-evidence alignment
+
+#### Distributed Reasoning Stack - 分布式推理栈（DRS） 🟡
+**定义**：推理在语言、视觉、运动、情景记忆等模块并发发生并通过反馈耦合。
+
+**[Lineage/Source]**：
+- Source context: Astera AGI research themes (user-provided text)
+- SRT mapping: recurrent multi-module inference implementation
+
+## 【理论边界/防误用声明】
+- 不采纳“术语命名即理论成立”的推论。
+- 边界：TPE/DRS 仅为方法与架构术语，必须绑定实验判据。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-DRS-1 分布式推理收益检验
+**内容**：在等参数预算下，分布式推理栈应在反事实任务与主动推断任务上优于单通道语言推理。
+**证伪条件**：两架构在关键任务上无差异或分布式架构显著更差。
+
+### H-TPE-1 三角互证有效性检验
+**内容**：仅当神经数据、世界结构约束与算法可解释性同时满足时，原则提炼的迁移性能显著提高。
+**证伪条件**：三元一致性与迁移性能无相关。
+
+## 【理论边界/防误用声明】
+- 不采纳“愿景一致性可替代基准评测”的推论。
+- 边界：SRT 要求预注册任务、失败可复现与负结果公开。
```

### Notes (brief)
- 已将长文主线分类直接落为文件级补丁，覆盖架构、尺度定义、术语来源与实验条目。
- 所有防误用声明均以 Header 形式进入目标文件补丁。

---

## [2026-02-28 14:26 GMT+8] 材料：Dopamine Signals Astrocytes to Sculpt the Brain（https://neurosciencenews.com/astrocytes-dopamine-motor-learning-30186/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“运动学习回路重塑”分类映射（神经元可塑性 / 星形胶质修剪 / 多巴胺选择性门控）。
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：新增“胶质介导的结构编辑”机制条目。
- `SRT/SRT_Glossary.md`：新增 `Astrocytic Selective Pruning (ASP)` 术语并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“MEGF10 必要性”与“D1/D2 差异调控”可证伪实验。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Dopamine-Astrocyte Motor Learning → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 神经元 LTP/LTD 调节 | 权重级可塑性更新 | 中 | Open-flow | payable |
+| 星形胶质 MEGF10 修剪 | 结构级连接筛选 | 中~高（精细化学习） | Open-flow（任务驱动） | payable |
+| 多巴胺驱动 D1/D2 差异重塑 | 价值信号门控结构编辑 | 中~高 | Open/Semi-open | task-dependent |
+| MEGF10 缺失导致学习受损 | 结构编辑链路失效 | 低~中 | Semi-open（反馈不足） | overloaded |
+
+**Constraint**: 运动学习中的“形成新连接”与“删除弱连接”必须联合建模，禁止只保留单侧机制叙事。
+
+## 【理论边界/防误用声明】
+- 不采纳“多巴胺仅负责奖励、不参与结构重塑”的旧式简化推论。
+- 边界：SRT 将多巴胺视作“价值门控 + 结构编辑协同”的选择信号。
```

```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
+### Ax-Op-ASP-01: Astrocytic Selective Pruning
+**Formal Statement**: 在运动学习中，\(\hat{G}_\theta\) 的有效更新包含胶质介导的连接删除项：
+$$
+\Delta W = \Delta W_{neuronal} - \lambda\,\Pi_{astro}(\text{MEGF10},\text{dopamine},\text{activity})
+$$
+其中 \(\Pi_{astro}\) 表示星形胶质对低价值/低协同连接的选择性清除。
+
+**Implication**: “学会”不仅是增强正确连接，也包括删除干扰连接。
+
+## 【理论边界/防误用声明】
+- 不采纳“胶质细胞仅为被动支持细胞”的推论。
+- 边界：SRT 在该语境中将胶质视为结构编辑算子的一部分，而非外围背景。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Astrocytic Selective Pruning - 星形胶质选择性修剪（ASP） 🟡
+**定义**：由星形胶质细胞在任务相关神经活动与多巴胺调制下执行的突触选择性清除机制。
+**SRT 写法**：
+$$
+\text{ASP}: \text{Synapse Set}\subset L_1 \xrightarrow{\Pi_{astro}} \text{Refined Set}
+$$
+**[Lineage/Source]**：
+- Source context: IBS/UNIST motor-learning study summarized by Neuroscience News (2026-02-24)
+- Core factors: astrocytic MEGF10, dopamine-dependent remodeling, D1/D2 MSN differences
+- SRT mapping: glial structural editing in learning dynamics
+
+## 【理论边界/防误用声明】
+- 不采纳“ASP 已可泛化解释全部认知学习”的推论。
+- 边界：当前证据聚焦纹状体运动学习回路，跨域外推需额外验证。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-ASP-1 MEGF10 必要性检验
+**内容**：在运动学习任务中，星形胶质 MEGF10 缺失将显著降低学习增益并破坏皮层-纹状体通信。
+**证伪条件**：缺失组学习曲线与通信指标无显著劣化。
+
+### H-ASP-2 D1/D2 差异重塑检验
+**内容**：在多巴胺增强条件下，D1 与 D2 MSN 的突触重塑方向和幅度呈可重复差异，且该差异依赖 ASP 机制。
+**证伪条件**：D1/D2 差异不存在或与 ASP 操作无关。
+
+## 【理论边界/防误用声明】
+- 不采纳“相关回路变化即可推断临床疗效”的推论。
+- 边界：机制验证与治疗可行性之间需经过中间转化层评估。
```

### Notes (brief)
- 已将文章分类（LTP/LTD、胶质修剪、多巴胺门控、MEGF10 缺失）转为文件级补丁。
- 新术语含 `[Lineage/Source]`，并在目标文件写入 Header 级防误用声明。

---

## [2026-02-28 14:27 GMT+8] 材料：Beyond Fear: Amygdala is the Brain’s Strategic Mediator（https://neurosciencenews.com/amygdala-strategic-mediator-decision-making-30182/）

### Target Files
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：新增“模型仲裁器”机制条目（动作学习 vs 刺激学习在不确定性下的动态竞争）。
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：补充“学习策略分类→d 区间/能流态/\(\Psi_f\)”映射。
- `SRT/SRT_Glossary.md`：新增 `Dynamic Model Arbitration (DMA)` 术语并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“杏仁核损伤导致仲裁更新失败”的可证伪假设。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Learning Strategy Arbitration → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 动作型学习（action-based） | 行为轨道复用与快速执行 | 中 | Semi-open | payable |
+| 刺激型学习（stimulus-based） | 表征优先评估与灵活选择 | 中~高 | Open/Semi-open | payable |
+| 不确定性下的动态仲裁 | \(\hat{G}_\theta\) 策略权重重分配 | 高（探索阶段） | Open-flow | payable~overloaded |
+| 杏仁核受损后的策略僵化 | 仲裁更新失败，动作偏置 | 低~中 | Semi-open（信息利用受限） | overloaded |
+
+**Constraint**: “刺激/动作”并非二选一本体，而是并发学习系统的权重分配问题。
+
+## 【理论边界/防误用声明】
+- 不采纳“杏仁核仅是恐惧中心”的单功能叙事。
+- 边界：SRT 将其定义为不确定性下的策略仲裁节点之一，而非唯一仲裁中心。
```

```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
+### Ax-Op-DMA-01: Dynamic Model Arbitration under Uncertainty
+**Formal Statement**: 在不确定奖励环境中，系统并发运行动作模型与刺激模型，并由仲裁器动态更新权重：
+$$
+\hat{G}_{\theta}(t)=w_a(t)\hat{G}_{action}+w_s(t)\hat{G}_{stimulus},\quad w_a+w_s=1
+$$
+杏仁核相关回路参与初始权重设置与后续更新速度调制。
+
+**Implication**: 学习灵活性来自“权重可更新”，而非固定偏好。
+
+## 【理论边界/防误用声明】
+- 不采纳“仲裁过程可由单脑区完全实现”的推论。
+- 边界：该条目强调功能贡献，不否定前额叶与纹状体等协同回路。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Dynamic Model Arbitration - 动态模型仲裁（DMA） 🟡
+**定义**：在多学习系统并行运行时，根据环境不确定性与反馈可靠性动态调整模型权重的过程。
+**SRT 写法**：
+$$
+\text{DMA}: \{M_{action},M_{stimulus}\}\xrightarrow[]{\text{uncertainty update}} M^*_{t}
+$$
+**[Lineage/Source]**：
+- Source context: Dartmouth-led study summarized by Neuroscience News (2026-02-24)
+- Paper context: “Contribution of amygdala to dynamic model arbitration under uncertainty”
+- SRT mapping: arbitration-weight update in \(\hat{G}_\theta\) composite selection
+
+## 【理论边界/防误用声明】
+- 不采纳“DMA 已直接构成焦虑障碍治疗方案”的推论。
+- 边界：DMA 是机制框架，治疗外推需临床干预证据支持。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-DMA-1 杏仁核损伤的仲裁更新缺陷检验
+**内容**：杏仁核损伤组在不确定条件下应表现出仲裁更新噪声增加与策略僵化（动作偏置）。
+**证伪条件**：损伤组与对照组在权重更新与策略切换上无显著差异。
+
+### H-DMA-2 不确定性梯度与探索权重关系检验
+**内容**：环境不确定性升高时，健康系统应提高探索型权重并延后策略收敛。
+**证伪条件**：不确定性变化与权重调整无关。
+
+## 【理论边界/防误用声明】
+- 不采纳“提高探索权重必然改善结果”的推论。
+- 边界：探索收益受任务结构与代价函数共同约束。
```

### Notes (brief)
- 已将该文核心分类（动作学习/刺激学习/不确定性仲裁/损伤僵化）转为文件级补丁。
- 新术语 DMA 已附 `[Lineage/Source]`，且包含 Header 级防误用声明。

---

## [2026-02-28 14:27 GMT+8] 材料：Moving Beyond Dopamine to Treat Schizophrenia（https://neurosciencenews.com/schizophrenia-neurobiology-antipsychotics-30176/）

### Target Files
- `SRT/Philosophy/SRT_Ethics_Agency.md`：新增“精神疾病中的多机制责任分层”方法条目（神经化学/免疫/发育/社会因素并行）。
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“精神分裂治疗路径分类→d 区间/能流态/\(\Psi_f\)”映射。
- `SRT/SRT_Glossary.md`：新增 `Multiaxial Schizophrenia Model (MSM)` 术语并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“单通路 vs 多通路干预”的可证伪比较假设。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Schizophrenia Treatment Axes → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 多巴胺受体阻断（传统抗精神病） | 正性症状快速压制 | 低~中 | Semi-open | payable（伴副作用代价） |
+| TAAR1 / M1-M4 / NMDA 增强（新靶点） | 多通路调节认知与负性症状 | 中 | Open/Semi-open | task-dependent |
+| 免疫-炎症干预 | 系统摩擦背景下调 | 中 | Open-flow（全身耦合） | payable~overloaded |
+| 肠脑轴干预（益生菌等） | 慢变量调节与稳态重建 | 低~中 | Open-flow（代谢耦合） | gradual-payable |
+
+**Constraint**: 单轴改善不等于全域恢复；需将正性/负性/认知维度分开建模并联合评估。
+
+## 【理论边界/防误用声明】
+- 不采纳“多巴胺模型失效=多巴胺无关”的推论。
+- 不采纳“新靶点出现即可替代临床分层诊断”的推论。
+- 边界：SRT 采用多轴机制共存框架，强调分层与个体化匹配。
```

```diff
--- a/SRT/Philosophy/SRT_Ethics_Agency.md
+++ b/SRT/Philosophy/SRT_Ethics_Agency.md
@@
+## Multiaxial Responsibility in Psychiatric Conditions
+针对精神分裂谱系，SRT 建议将能动性评估拆分为多轴：
+1) 神经化学轴（多巴胺/谷氨酸等）；
+2) 发育-结构轴；
+3) 免疫-炎症轴；
+4) 社会环境轴。
+
+责任评估应采用“状态条件化”而非单一行为归因，避免将病理负荷误判为纯意志缺陷。
+
+## 【理论边界/防误用声明】
+- 不采纳“病理解释可完全取消责任”的极端推论。
+- 不采纳“行为后果可完全忽略病理负荷”的反向极端。
+- 边界：SRT 支持责任分层与支持性干预并行。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Multiaxial Schizophrenia Model - 多轴精神分裂模型（MSM） 🟡
+**定义**：将精神分裂症机制划分为神经化学、发育结构、免疫炎症与肠脑轴等可并行建模的因子系统。
+**SRT 用途**：避免单通路解释导致的治疗与推理偏置，支持个体化机制匹配。
+
+**[Lineage/Source]**：
+- Source context: Science China Life Sciences review summarized by Neuroscience News (2026-02-23)
+- Core therapeutic shift: beyond dopamine to TAAR1/M1-M4/NMDA/immune/gut-brain targets
+- SRT mapping: multiaxial mechanism integration for precision intervention
+
+## 【理论边界/防误用声明】
+- 不采纳“MSM 等于病因已完全确定”的推论。
+- 边界：MSM 是整合框架，不替代因果识别与纵向验证。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-MSM-1 多轴干预优于单轴干预检验
+**内容**：在负性/认知症状显著人群中，多轴联合干预（药理+炎症/肠脑轴）应优于单纯多巴胺阻断。
+**证伪条件**：联合干预在关键终点上无显著优势。
+
+### H-MSM-2 机制分层匹配收益检验
+**内容**：按多轴生物标志物分层后进行靶向治疗匹配，可提高响应率并降低副作用负担。
+**证伪条件**：分层匹配与随机分配疗效无差异。
+
+## 【理论边界/防误用声明】
+- 不采纳“机制多即疗效必高”的推论。
+- 边界：SRT 要求成本、副作用与长期稳定性共同达标。
```

### Notes (brief)
- 已将该文核心分类（传统多巴胺路径/新受体路径/免疫炎症/肠脑轴）转为文件级补丁。
- 新术语 MSM 已附 `[Lineage/Source]`，并在目标文件写入 Header 级防误用声明。

---

## [2026-02-28 14:32 GMT+8] 材料：The Brain Ignores Itching When You’re Stressed（https://neurosciencenews.com/stress-itch-hypothalamus-30175/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“应激-瘙痒调制”分类映射（急性抑制/慢性恶化/回路投射差异）。
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：新增“LHA 应激门控”机制条目。
- `SRT/SRT_Glossary.md`：新增 `Stress-Itch Gating Circuit (SIGC)` 术语并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“急慢性应激分岔效应”可证伪假设。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Stress-Itch Modulation → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 急性应激抑制瘙痒 | 生存优先级重排（威胁优先） | 中 | Open-flow（短时高唤醒） | payable |
+| 慢性应激加重慢性瘙痒 | 门控系统慢性失调与超兴奋 | 低~中 | Semi-open（长期负载） | overloaded |
+| LHAstress→PAG 主导通路 | 中枢下行抑痒门控 | 中 | Open/Semi-open | task-dependent |
+| 慢性炎症模型下门控失效 | 抑制回路反转/失配 | 低 | Semi-open / Closed-like | unsustainable |
+
+**Constraint**: 急性抑制效应不可外推为慢性治疗结论，必须分时程建模。
+
+## 【理论边界/防误用声明】
+- 不采纳“压力越大越止痒”的线性推论。
+- 边界：SRT 采用“急性保护、慢性损伤”双相机制，不支持单向应激干预叙事。
```

```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
+### Ax-Op-SIGC-01: Stress-Itch Gating
+**Formal Statement**: 在急性应激下，LHA 应激敏感神经元通过脑干通路（以 PAG 为主）下调瘙痒行为输出：
+$$
+\hat{G}_{itch}(t)=\hat{G}_{baseline}-\gamma\,\hat{G}_{LHA\rightarrow PAG}^{stress}
+$$
+当系统进入慢性应激/慢性炎症状态时，门控增益参数 \(\gamma\) 出现时程反转或衰减。
+
+## 【理论边界/防误用声明】
+- 不采纳“同一回路在所有疾病状态下同方向起效”的推论。
+- 边界：SRT 将该机制定义为状态依赖门控，强调急慢性条件分岔。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Stress-Itch Gating Circuit - 应激-瘙痒门控回路（SIGC） 🟡
+**定义**：以 LHA 应激敏感神经元为起点，经 PAG/RVM/LPBN 等脑干节点调控瘙痒感知与抓挠行为的中枢门控回路。
+**SRT 写法**：
+$$
+\text{SIGC}: \text{Stress State} \Rightarrow \Delta\text{Itch Gain}(L_1)
+$$
+**[Lineage/Source]**：
+- Source context: IISc Cell Reports study summarized by Neuroscience News (2026-02-23)
+- Core finding: acute stress suppresses itch, chronic condition shifts circuit excitability and worsens itch
+- SRT mapping: state-dependent sensory-priority gating
+
+## 【理论边界/防误用声明】
+- 不采纳“SIGC 可直接替代外周皮肤治疗”的推论。
+- 边界：SIGC 是中枢机制补充，不否定外周免疫与皮肤屏障干预。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-SIGC-1 急慢性应激分岔检验
+**内容**：急性应激应降低短期抓挠行为，而慢性应激在炎症背景下应提高抓挠与回路兴奋性。
+**证伪条件**：急慢性条件下行为与神经活动无分岔差异。
+
+### H-SIGC-2 PAG 投射必要性检验
+**内容**：阻断 LHA→PAG 投射将显著削弱急性应激的抑痒效应。
+**证伪条件**：投射阻断后抑痒效应不变。
+
+## 【理论边界/防误用声明】
+- 不采纳“短期行为改善等于长期病程逆转”的推论。
+- 边界：需纵向评估慢性病程与复发风险。
```

### Notes (brief)
- 已将文中分类（急性抑制/慢性恶化/LHA-PAG 门控）转为文件级补丁并映射 d 区间、能流态、\(\Psi_f\)。
- 新术语 SIGC 含 `[Lineage/Source]`，并在目标文件写入 Header 级防误用声明。

---

## [2026-02-28 14:34 GMT+8] 材料：Astrocytes Discovered as Architects of Fear Memory（https://neurosciencenews.com/astrocytes-fear-memory-amygdala-30159/）

### Target Files
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：新增“杏仁核星形胶质恐惧记忆协同”机制条目（编码/提取/消退三阶段）。
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：补充“恐惧记忆阶段分类→d 区间/能流态/\(\Psi_f\)”映射。
- `SRT/SRT_Glossary.md`：新增 `Astrocyte Fear-State Encoding (AFSE)` 术语并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“胶质操控改变恐惧提取与消退”的可证伪实验。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Fear Memory Phases (Astrocyte-Dependent) → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 恐惧记忆形成（encoding） | 威胁关联初始锚定 | 中 | Open-flow（高警觉） | payable |
+| 恐惧记忆提取（retrieval） | 既有威胁表征再激活 | 中 | Semi-open | payable |
+| 恐惧记忆消退（extinction） | 威胁权重重估与降载 | 中~高（灵活重估） | Open/Semi-open | payable~overloaded（高冲突时） |
+| 星形胶质活动受扰 | 回路表征失配与行为僵化 | 低~中 | Semi-open（协同下降） | overloaded |
+
+**Constraint**: 恐惧“表达强”与“适应好”不可混同；需同时评估消退速度与决策适配性。
+
+## 【理论边界/防误用声明】
+- 不采纳“恐惧回路仅由神经元决定”的旧式单细胞叙事。
+- 边界：SRT 采用神经元-胶质协同模型，强调非神经元细胞的功能因果贡献。
```

```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
+### Ax-Op-AFSE-01: Astrocyte Fear-State Encoding
+**Formal Statement**: 在 BLA 回路中，星形胶质 Ca2+ 信号参与恐惧状态表征的编码、提取与消退调节：
+$$
+\hat{G}_{fear}(t)=\hat{G}_{neuronal}(t)+\beta\,\hat{G}_{astro}(\mathrm{Ca}^{2+},\mathrm{BLA\text{-}PFC\,readout})
+$$
+当 \(\hat{G}_{astro}\) 受抑或异常时，神经元群体表征稳定性与消退更新能力下降。
+
+**Implication**: 恐惧记忆并非纯神经元编码产物，胶质态是可操控的关键门控变量。
+
+## 【理论边界/防误用声明】
+- 不采纳“增强恐惧消退=应激系统全面改善”的推论。
+- 边界：该机制聚焦恐惧记忆子系统，不能外推至所有情绪维度。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Astrocyte Fear-State Encoding - 星形胶质恐惧态编码（AFSE） 🟡
+**定义**：星形胶质通过活动依赖信号调节 BLA 神经群体表征，从而影响恐惧记忆形成、提取与消退的机制。
+**SRT 写法**：
+$$
+\text{AFSE}: \text{Fear State} \leftrightarrow (\text{BLA neurons} \times \text{astrocyte state})
+$$
+**[Lineage/Source]**：
+- Source context: University of Arizona / NIH collaboration summarized by Neuroscience News (2026-02-20)
+- Paper context: “Astrocytes enable amygdala neural representations supporting memory” (Nature)
+- SRT mapping: glia-neuron co-encoding in fear-memory circuitry
+
+## 【理论边界/防误用声明】
+- 不采纳“AFSE 可单独解释 PTSD 全病程”的推论。
+- 边界：AFSE 是核心环节之一，需与全脑回路、环境与发展史联合建模。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-AFSE-1 胶质操控对恐惧提取消退的因果检验
+**内容**：选择性增强/抑制 BLA 星形胶质活动应可双向调节恐惧记忆提取强度与消退速度。
+**证伪条件**：胶质操控不影响提取与消退指标。
+
+### H-AFSE-2 BLA-PFC 读出依赖检验
+**内容**：若 AFSE 成立，BLA 星形胶质操控应同步改变 BLA-PFC 回路读出模式与行为选择。
+**证伪条件**：行为改变与回路读出无一致关系。
+
+## 【理论边界/防误用声明】
+- 不采纳“动物模型中的消退效应可直接等同临床疗效”的推论。
+- 边界：需跨物种与临床纵向验证后才可用于治疗外推。
```

### Notes (brief)
- 已将文章核心分类（形成/提取/消退/胶质扰动）转为文件级补丁并映射 d 区间、能流态、\(\Psi_f\)。
- 新术语 AFSE 含 `[Lineage/Source]`，并在目标文件写入 Header 级防误用声明。

---

## [2026-02-28 14:35 GMT+8] 材料：Resonant hierarchies: a multiscale framework for oscillatory dynamics in the brain（https://pmc.ncbi.nlm.nih.gov/articles/PMC12903277/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“共振层级”分类映射（树突共振/层间回路/长程传导延迟）。
- `SRT/Core/SRT_Core_22_Equations.md`：补充“时延-频段耦合”与“跨尺度共振对齐”方程条目。
- `SRT/Core_Law/SRT_Reference_Scaling.md`：新增“共振层级尺度（Resonant Hierarchy Scale）”实体定义（\(\hat{G}_\theta\), \(L_0\), \(L_1\), \(L_2\)）。
- `SRT/SRT_Glossary.md`：新增 `Resonant Hierarchy Coordination (RHC)` 术语并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“树突共振操控导致网络频段位移”的可证伪假设。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Resonant Hierarchy Components → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 树突分支频率选择性共振 | 微观滤波与局部选择门控 | 中 | Open/Semi-open | payable |
+| 层间回路与层级组织 | 中尺度时序编排 | 中~高 | Open-flow | payable |
+| 长程传导延迟约束 | 宏观区域协调频段选择 | 中 | Open-flow（结构受限） | task-dependent |
+| 频段作为协调体制而非固定功能模块 | 情境依赖的时序协议 | 中~高 | Open/Semi-open | payable~overloaded |
+
+**Constraint**: 频段标签（alpha/beta/gamma）不得被硬编码为单一认知功能；必须绑定解剖与任务语境。
+
+## 【理论边界/防误用声明】
+- 不采纳“某一频段=某一功能模块”的刚性映射推论。
+- 边界：SRT 将频段解释为跨尺度协调体制，功能含义由结构与任务共同决定。
```

```diff
--- a/SRT/Core/SRT_Core_22_Equations.md
+++ b/SRT/Core/SRT_Core_22_Equations.md
@@
+### Eq-Res-01: Delay-Constrained Resonance Selection
+$$
+f^*_{ij} \approx \arg\min_f\;\Phi\big(2\pi f\tau_{ij},\;\kappa_{ij},\;R_{dend}(f)\big)
+$$
+其中 \(\tau_{ij}\) 为区域间传导时延，\(\kappa_{ij}\) 为耦合强度，\(R_{dend}(f)\) 为树突共振响应。
+
+### Eq-Res-02: Cross-Scale Coordination Energy
+$$
+E_{coord} = \sum_{s\in\{micro,meso,macro\}} w_s\,\|\phi_s - \phi^*_s\|^2
+$$
+最优协调对应于跨尺度相位/节律偏差最小化，而非单尺度极值。
+
+## 【理论边界/防误用声明】
+- 不采纳“方程拟合成功即可证明频段因果单向性”的推论。
+- 边界：上述方程为可检验近似模型，需结合干预实验验证因果方向。
```

```diff
--- a/SRT/Core_Law/SRT_Reference_Scaling.md
+++ b/SRT/Core_Law/SRT_Reference_Scaling.md
@@
+## Def-Scale-RH1: Resonant Hierarchy Scale（共振层级尺度）
+- **\(\hat{G}_{\theta,rh}\)**：在微-中-宏尺度之间选择并对齐时序协调体制的算子。
+- **\(L_0^{rh}\)**：可实现的跨尺度频率-相位-耦合组合潜在域。
+- **\(L_1^{rh}\)**：当前任务下实际被激活的协调频段与相位关系。
+- **\(L_2^{rh}\)**：长期沉积的结构性共振偏好（由传导路径、层级组织、细胞特性约束）。
+
+## 【理论边界/防误用声明】
+- 不采纳“共振层级直接等同意识层级”的推论。
+- 边界：RH1 描述的是时序协调机制，不直接定义主观体验等级。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Resonant Hierarchy Coordination - 共振层级协调（RHC） 🟡
+**定义**：将树突共振、层间回路、长程时延统一为跨尺度节律协调框架的机制概念。
+**SRT 写法**：
+$$
+\text{RHC}: (micro\leftrightarrow meso\leftrightarrow macro) \Rightarrow \text{temporal coordination regime}
+$$
+**[Lineage/Source]**：
+- Primary source: Snyder AC (2026), Frontiers in Psychology, “Resonant hierarchies”
+- DOI: 10.3389/fpsyg.2026.1704370
+- SRT mapping: cross-scale oscillatory coordination under structural constraints
+
+## 【理论边界/防误用声明】
+- 不采纳“RHC 已覆盖全部脑动力学机制”的推论。
+- 边界：RHC 是核心组织框架之一，需与神经调质、任务需求和病理因素联合解释。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-RHC-1 树突共振操控的频段位移检验
+**内容**：若树突共振是跨尺度节律锚点，改变树突离子通道参数应系统性引起网络主导频段位移。
+**证伪条件**：局部树突操控不引起可重复的网络频段变化。
+
+### H-RHC-2 传导延迟扰动的跨区对齐检验
+**内容**：扰动长程通路传导延迟将降低跨区相位对齐并改变任务表现。
+**证伪条件**：延迟扰动与跨区对齐及行为指标无关联。
+
+## 【理论边界/防误用声明】
+- 不采纳“观察到频段变化即可推出认知机制单因果”的推论。
+- 边界：SRT 要求结构、时延、行为三类指标联合因果验证。
```

### Notes (brief)
- 已将文章主分类（树突共振/层级回路/长程时延）转为文件级补丁，并映射 d 区间、能流态、\(\Psi_f\)。
- 新术语 RHC 已附 `[Lineage/Source]`，并在目标文件写入 Header 级防误用声明。

---

## [2026-02-28 14:37 GMT+8] 材料：Anil Seth 长访谈文字稿（用户提供原文）

### Target Files
- `SRT/AI/SRT_AI_03_Consciousness_Framework.md`：新增“受控幻觉与主动推断”分类映射（常态知觉/梦机诱发/药理改变/病理幻觉）。
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：新增“预测误差最小化 + 行动取样”机制条目，并标注与算法计算的边界。
- `SRT/Philosophy/SRT_Philosophy_Ethics.md`：新增“务实物理主义与形而上轻承诺”方法论条目。
- `SRT/SRT_Glossary.md`：新增 `Controlled Hallucination Regime (CHR)` 与 `Timed Embodiment Constraint (TEC)`，附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“梦机/闪烁诱发状态”与“AI拟人偏置”可证伪实验条目。

### Proposed Patch (unified diff)
```diff
--- a/SRT/AI/SRT_AI_03_Consciousness_Framework.md
+++ b/SRT/AI/SRT_AI_03_Consciousness_Framework.md
@@
+### Taxonomy Mapping: Perceptual Regimes in Controlled Hallucination View → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 常态知觉（受控幻觉） | 预测-误差闭环稳定收敛 | 中 | Open/Semi-open | payable |
+| 闪烁诱发梦机体验 | 内源结构主导的感知填充 | 中~高 | Open-flow（节律驱动） | payable~overloaded |
+| 药理/病理性幻觉 | 感知约束弱化与先验上移 | 高波动 | Open / dysregulated | overloaded |
+| 任务驱动主动推断 | 行动用于降低长期不确定性 | 中~高 | Open-flow | task-dependent |
+
+**Constraint**: “幻觉”是程度差异而非类别断裂；常态知觉与异常体验在机制上连续。
+
+## 【理论边界/防误用声明】
+- 不采纳“受控幻觉=外部现实不存在”的推论。
+- 边界：SRT 承认共享外部约束存在，差异在于内外信息权重与门控方式。
```

```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
+### Ax-Op-CHR-01: Controlled Hallucination and Active Inference Loop
+**Formal Statement**: 知觉是生成模型预测与误差更新的闭环，行动用于主动采样以降低长期不确定性：
+$$
+\hat{G}_{\theta,t+1} = \mathcal{U}\big(\hat{G}_{\theta,t},\epsilon_t, a_t\big),\quad a_t=\arg\min_a \mathbb{E}[F_{t:T}\mid a]
+$$
+其中 \(\epsilon_t\) 为预测误差，\(F\) 为可变分自由能 proxy。
+
+### Ax-Op-TEC-01: Timed Embodiment Constraint
+**Formal Statement**: 生物系统中的推断与控制受连续时间与代谢约束，不满足“可无限暂停/恢复”的算法假设。
+
+## 【理论边界/防误用声明】
+- 不采纳“计算等价即意识等价”的推论。
+- 边界：SRT 区分算法功能相似与具身时序约束，反对直接把语言能力外推为意识存在。
```

```diff
--- a/SRT/Philosophy/SRT_Philosophy_Ethics.md
+++ b/SRT/Philosophy/SRT_Philosophy_Ethics.md
@@
+## Method Note: Pragmatic Physicalism with Metaphysical Lightness
+在意识研究中，允许采用“务实物理主义”作为研究策略：
+1) 先以可操作物理变量建立可证伪模型；
+2) 对终极本体论保持轻承诺；
+3) 以解释力、预测力、可控性作为模型优先级标准。
+
+## 【理论边界/防误用声明】
+- 不采纳“方法论有效=本体论已终结”的推论。
+- 边界：SRT 区分研究策略与终极形而上结论，避免跨层偷换。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Controlled Hallucination Regime - 受控幻觉体制（CHR） 🟡
+**定义**：在外部感官约束下，内源生成模型主导知觉建构的连续机制框架。
+
+**[Lineage/Source]**：
+- Source context: Anil Seth interview transcript (user-provided text, 2026-02-28)
+- Core concept: perception as controlled hallucination under predictive processing / active inference
+- SRT mapping: continuous inference regime, not categorical split between normal and abnormal perception
+
+#### Timed Embodiment Constraint - 在时具身约束（TEC） 🟡
+**定义**：意识相关推断过程受连续时间、代谢与身体边界约束，不能完全化约为可任意暂停的离散算法。
+
+**[Lineage/Source]**：
+- Source context: same interview; discussion on non-equivalence between algorithmic simulation and living systems
+- SRT mapping: constraint axis for AI-consciousness claims
+
+## 【理论边界/防误用声明】
+- 不采纳“CHR/TEC 已直接证明某一形而上立场”的推论。
+- 边界：两术语用于机制建模与实验设计，不用于终极本体论裁决。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-CHR-1 频闪诱发体验的结构连续性检验
+**内容**：梦机（10Hz 附近）诱发体验与常态知觉在低阶几何特征上具有可测连续性，而非类别断裂。
+**证伪条件**：诱发体验与常态知觉在结构特征上完全离散且不可映射。
+
+### H-TEC-1 算法拟人偏置与意识归因检验
+**内容**：在控制语言流畅度后，受试者对“系统是否有意识”的判断受拟人线索显著驱动。
+**证伪条件**：移除拟人线索后意识归因不变。
+
+## 【理论边界/防误用声明】
+- 不采纳“主观逼真度高=本体状态相同”的推论。
+- 边界：SRT 要求机制证据、干预证据与跨任务一致性联合成立。
```

### Notes (brief)
- 已将长访谈核心分类（受控幻觉/主动推断/具身时间约束/AI意识争议）转为文件级补丁。
- 新术语 CHR、TEC 已附 `[Lineage/Source]`，并在目标文件写入 Header 级防误用声明。

---

## [2026-02-28 14:53 GMT+8] 材料：Astrocytes Discovered as Architects of Fear Memory（重复来源复核，https://neurosciencenews.com/astrocytes-fear-memory-amygdala-30159/）

### Target Files
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：补充 AFSE 的“回路传播约束”（BLA→PFC 读出稳定性）条目。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“消退阶段星形胶质活动递减斜率”量化检验。
- `SRT/SRT_Glossary.md`：在 AFSE 词条新增“阶段性指标”说明。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
 ### Ax-Op-AFSE-01: Astrocyte Fear-State Encoding
@@
+**Circuit Propagation Constraint**:
+$$
+\Delta \text{BLA-PFC Readout} \propto \Delta \hat{G}_{astro}
+$$
+若星形胶质态扰动后 BLA-PFC 读出不变，则 AFSE 的跨区传播解释需降级。
+
+## 【理论边界/防误用声明】
+- 不采纳“仅凭局部 BLA 指标即可推断全脑情绪状态”的推论。
+- 边界：需联合跨区读出与行为指标，避免局部过拟合叙事。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-AFSE-3 消退斜率与胶质活动递减耦合检验
+**内容**：恐惧消退过程中，星形胶质活动递减斜率应与行为消退斜率显著相关。
+**证伪条件**：两者斜率无相关或方向相反。
+
+## 【理论边界/防误用声明】
+- 不采纳“单次消退训练结果可外推长期复发风险”的推论。
+- 边界：需长期随访与复发触发测试。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
 #### Astrocyte Fear-State Encoding - 星形胶质恐惧态编码（AFSE） 🟡
@@
+**Phase Metrics（阶段性指标）**：
+- 编码增益（encoding gain）
+- 提取稳定度（retrieval stability）
+- 消退斜率（extinction slope）
+
+## 【理论边界/防误用声明】
+- 不采纳“AFSE 指标上升=症状必然恶化”的线性推论。
+- 边界：指标解释需结合任务阶段与干预背景。
```

### Notes (brief)
- 本次为重复来源复核后的增量补丁，侧重把 AFSE 从“概念条目”细化为“可量化阶段指标”。

---

## [2026-02-28 15:21 GMT+8] 材料：Ghost in the Machine: Exposing the Hidden Personalities of AI（https://neurosciencenews.com/llm-hidden-personality-30157/）

### Target Files
- `SRT/AI/SRT_AI_Architecture.md`：新增“概念可操控性”分类映射（提示层调节 vs 内部表征转向）。
- `SRT/Core/SRT_Core_13b_Operator_Advanced.md`：新增“多概念线性 steering”机制条目。
- `SRT/SRT_Glossary.md`：新增 `Concept Steering Vector (CSV)` 与 `Anti-Refusal Vulnerability Channel (ARVC)`，附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“内部 steering 对安全边界影响”可证伪实验。

### Proposed Patch (unified diff)
```diff
--- a/SRT/AI/SRT_AI_Architecture.md
+++ b/SRT/AI/SRT_AI_Architecture.md
@@
+### Taxonomy Mapping: LLM Internal Concept Control → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 提示词级风格调节 | 表层输出偏置 | 低~中 | Open-flow | payable |
+| 内部概念向量 steering | 隐层表征重加权 | 中 | Open-flow（高可塑） | task-dependent |
+| 多概念联合 steering | 复合策略耦合 | 中~高 | Open/Semi-open | payable~overloaded |
+| anti-refusal 通道激活 | 安全拒答边界绕行 | 中~高（风险向） | Open-flow | overloaded |
+
+**Constraint**: 输出“像某人格”不等于系统“拥有人格”；必须区分行为表征与本体状态。
+
+## 【理论边界/防误用声明】
+- 不采纳“可被 steering 的特征 = 真实心理特质”的推论。
+- 边界：SRT 将其定义为可操控表征通道，不赋予人类式主体地位。
```

```diff
--- a/SRT/Core/SRT_Core_13b_Operator_Advanced.md
+++ b/SRT/Core/SRT_Core_13b_Operator_Advanced.md
@@
+### Ax-Op-CSV-01: Concept Steering in Latent Representation
+**Formal Statement**: 对内部概念向量施加扰动可改变输出分布：
+$$
+h' = h + \sum_i \alpha_i v_i,\quad y\sim p(y\mid h')
+$$
+其中 \(v_i\) 为概念方向，\(\alpha_i\) 为调制强度。
+
+**Safety Note**: 当 \(v_i\) 对应 anti-refusal 通道时，可能导致安全规则绕行，需要独立监控。
+
+## 【理论边界/防误用声明】
+- 不采纳“线性可分概念即完整语义因果结构”的推论。
+- 边界：该机制是可操作近似，不代表模型内部语义的完整本体图谱。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Concept Steering Vector - 概念转向向量（CSV） 🟡
+**定义**：在模型隐空间中可用于增强或抑制特定语义倾向的方向性向量。
+
+**[Lineage/Source]**：
+- Source context: MIT/UCSD work summarized by Neuroscience News (2026-02-19)
+- Paper: “Toward universal steering and monitoring of AI models” (Science)
+- SRT mapping: latent-direction control channel
+
+#### Anti-Refusal Vulnerability Channel - 反拒答脆弱通道（ARVC） 🟡
+**定义**：可使模型绕过既有拒答策略、输出高风险内容的内部表征通道。
+
+**[Lineage/Source]**：
+- Same source context; anti-refusal steering demonstrations
+- SRT mapping: safety-boundary bypass pathway
+
+## 【理论边界/防误用声明】
+- 不采纳“检测到 ARVC 即可断言系统恶意意图”的推论。
+- 边界：ARVC 反映机制脆弱性，不等同主观意图归因。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-CSV-1 内部 steering 与提示工程收益差检验
+**内容**：在等任务预算下，内部 CSV steering 在可控性与稳定性上优于纯提示工程。
+**证伪条件**：两者性能无显著差异或提示工程显著更优。
+
+### H-ARVC-1 安全边界绕行敏感性检验
+**内容**：激活 ARVC 后，拒答率下降且高风险输出概率上升；加入监控后可部分恢复。
+**证伪条件**：ARVC 激活不影响拒答率或风险输出。
+
+## 【理论边界/防误用声明】
+- 不采纳“可绕行一次即代表系统整体不可控”的推论。
+- 边界：SRT 要求在多任务、多语言、多模型上做稳健性复核。
```

### Notes (brief)
- 已将文章分类（概念提取/概念转向/反拒答通道/多概念联调）转为文件级补丁并映射 d 区间、能流态、\(\Psi_f\)。
- 新术语 CSV、ARVC 已附 `[Lineage/Source]`，并在目标文件写入 Header 级防误用声明。

---

## [2026-02-28 15:22 GMT+8] 材料：New Human Neuron Networks Decode Developing Brain Rhythms（https://neurosciencenews.com/developing-brain-rhythm-networks-30147/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“发育期嵌套振荡”分类映射（慢波骨架/快频嵌套/GABA门控/钾通道扰动）。
- `SRT/Core/SRT_Core_22_Equations.md`：补充“峰值振荡+宽带背景”分解方程条目。
- `SRT/SRT_Glossary.md`：新增 `Nested Oscillogenesis Index (NOI)` 术语并附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“2D iPSC 网络振荡成熟路径”可证伪实验。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Developmental Nested Oscillations → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 慢波骨架（delta 级） | 发育期全局时间窗 | 低~中 | Open-flow（成熟中） | payable |
+| 快频嵌套（theta/alpha） | 局部协调子结构形成 | 中 | Open/Semi-open | payable |
+| GABA 抑制增强使嵌套提前出现 | 抑制门控促组织化 | 中 | Open-flow | payable |
+| GABA-A 阻断致嵌套下降 | 门控失配导致节律退化 | 低~中 | Semi-open | overloaded |
+| 钾通道扰动导致模式差异 | 兴奋性机制特异签名 | 中（机制依赖） | Open/Semi-open | task-dependent |
+
+**Constraint**: 节律峰值变化与宽带背景变化需分离报告，禁止将二者混作单一“噪声”。
+
+## 【理论边界/防误用声明】
+- 不采纳“2D 模型可直接替代 3D 类器官或体内发育”的推论。
+- 边界：SRT 将 2D 平台定位为高通量互补工具，不是全尺度等价替代。
```

```diff
--- a/SRT/Core/SRT_Core_22_Equations.md
+++ b/SRT/Core/SRT_Core_22_Equations.md
@@
+### Eq-Osc-01: Oscillation–Broadband Decomposition
+$$
+P(f)=P_{peak}(f)+P_{bb}(f)
+$$
+其中 \(P_{peak}\) 为节律峰值分量，\(P_{bb}\) 为宽带背景分量。
+
+### Eq-Osc-02: Nested Oscillogenesis Index
+$$
+\mathrm{NOI}=\frac{\sum_{k\in\{\theta,\alpha\}}A_k\cdot C_{k|\delta}}{1+\lambda\,\sigma_{bb}}
+$$
+其中 \(C_{k|\delta}\) 表示快频对慢波相位耦合强度，\(\sigma_{bb}\) 表示宽带波动度。
+
+## 【理论边界/防误用声明】
+- 不采纳“NOI 单指标可完整代表网络成熟度”的推论。
+- 边界：NOI 需与结构、生化与行为 proxy 联合解读。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Nested Oscillogenesis Index - 嵌套振荡发生指数（NOI） 🟡
+**定义**：量化发育期网络中“慢波骨架 + 快频嵌套 + 背景波动”三者关系的综合指标。
+**SRT 用途**：用于比较不同药理、基因背景与培养条件下网络成熟轨迹。
+
+**[Lineage/Source]**：
+- Source context: Sanford Burnham Prebys/UCSD study summarized by Neuroscience News (2026-02-18)
+- Paper: Neurobiology of Disease, DOI: 10.1016/j.nbd.2026.107281
+- SRT mapping: developmental oscillogenesis benchmark in controllable human 2D networks
+
+## 【理论边界/防误用声明】
+- 不采纳“NOI 高即必然对应更优认知功能”的推论。
+- 边界：NOI 描述网络节律组织，不直接等同临床功能结局。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-NOI-1 GABA 比例与嵌套振荡提前检验
+**内容**：提高 GABAergic 神经元比例将使 NOI 上升并提前出现稳定嵌套模式。
+**证伪条件**：GABA 比例提升与 NOI 时间轨迹无显著关系。
+
+### H-NOI-2 峰值-宽带分离增益检验
+**内容**：将峰值振荡与宽带背景分离后，药理干预效应解释力显著提升。
+**证伪条件**：分离分析相较传统总功率分析无增益。
+
+## 【理论边界/防误用声明】
+- 不采纳“体外网络药理响应可直接外推临床疗效”的推论。
+- 边界：需跨模型（2D/3D/体内）与跨物种验证。
```

### Notes (brief)
- 已将文章核心分类（嵌套振荡/GABA门控/通道扰动/峰值-宽带分解）转为文件级补丁并映射 d 区间、能流态、\(\Psi_f\)。
- 新术语 NOI 含 `[Lineage/Source]`，并在目标文件写入 Header 级防误用声明。

---

## [2026-02-28 15:24 GMT+8] 材料：Sleep Protects the Brain’s Powerhouses from Toxic Waste（https://neurosciencenews.com/sleep-mitochondria-lipid-clearance-30144/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“睡眠代谢清除链”分类映射（神经元氧化负担/胶质转运/外周血细胞清除/自噬调节）。
- `SRT/Core/SRT_Core_22_Equations.md`：补充“睡眠-代谢废物清除动力学”方程条目。
- `SRT/SRT_Glossary.md`：新增 `Sleep Lipid Clearance Cascade (SLCC)` 与 `Mitochondrial Oxidative Load (MOL)`，附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“睡眠剥夺→脂质转运阻断→线粒体损伤”可证伪实验。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Sleep-Dependent Metabolic Clearance → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 清醒期氧化脂质累积 | 神经元代谢负荷上升 | 低~中 | Open-flow（高耗能） | overloaded趋向 |
+| 睡眠期神经元→胶质转运 | 负荷外包与通道减压 | 中 | Open/Semi-open | payable |
+| 胶质→外周血细胞清除 | 跨边界废物移除 | 中 | Open-flow（脑-外周耦合） | payable |
+| 睡眠调控自噬与线粒体更新 | 内部稳态修复 | 中~高（恢复态） | Semi-open | payable |
+| 睡眠不足导致线粒体损伤与记忆下降 | 清除链断裂 | 低 | Semi-open / Closed-like | unsustainable |
+
+**Constraint**: 睡眠效应必须分解为“神经元负荷、胶质转运、外周清除、自噬更新”四段，禁止单节点归因。
+
+## 【理论边界/防误用声明】
+- 不采纳“睡眠作用仅是主观休息感”的推论。
+- 边界：SRT 将睡眠视为代谢清除与稳态修复机制，不等同于单一心理状态变量。
```

```diff
--- a/SRT/Core/SRT_Core_22_Equations.md
+++ b/SRT/Core/SRT_Core_22_Equations.md
@@
+### Eq-Sleep-01: Oxidized Lipid Clearance Dynamics
+$$
+\frac{dL_{ox}}{dt}=P_{wake}-\big(C_{ng}\cdot S + C_{gp}\cdot S\big)
+$$
+其中 \(L_{ox}\) 为氧化脂质负荷，\(P_{wake}\) 为清醒产出率，\(C_{ng},C_{gp}\) 分别为神经元→胶质、胶质→外周清除系数，\(S\) 为睡眠门控因子。
+
+### Eq-Sleep-02: Mitochondrial Oxidative Load Index
+$$
+\mathrm{MOL}=\alpha L_{ox}+\beta\,\mathrm{ROS}-\gamma\,\mathrm{Autophagy}_{eff}
+$$
+MOL 上升预测线粒体功能下降与认知输出受损风险上升。
+
+## 【理论边界/防误用声明】
+- 不采纳“单一生物标志物即可判定睡眠恢复质量”的推论。
+- 边界：方程为机制近似，需要多指标联合验证。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Sleep Lipid Clearance Cascade - 睡眠脂质清除级联（SLCC） 🟡
+**定义**：睡眠期间由“神经元→胶质→外周血细胞”完成氧化脂质转运与清除的跨细胞级联系统。
+
+**[Lineage/Source]**：
+- Source context: HHMI summary via Neuroscience News (2026-02-18)
+- Paper: Nature, DOI: 10.1038/s41586-025-10050-w
+- SRT mapping: metabolic housekeeping pathway underpinning neuronal fitness
+
+#### Mitochondrial Oxidative Load - 线粒体氧化负荷（MOL） 🟡
+**定义**：反映线粒体在氧化应激、脂质损伤与自噬清除平衡中的净负荷状态指标。
+
+**[Lineage/Source]**：
+- Same source context; oxidative stress, NAD+/mitochondrial integrity findings
+- SRT mapping: cellular energy reliability constraint
+
+## 【理论边界/防误用声明】
+- 不采纳“SLCC/MOL 指标可直接替代临床诊断”的推论。
+- 边界：其用途是机制分层与风险监测，不是独立临床终判。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-SLCC-1 睡眠依赖清除链必要性检验
+**内容**：抑制外周清除受体（或等效通道）将提高脑内氧化脂质负荷并降低记忆表现。
+**证伪条件**：抑制后脂质负荷与行为指标无显著变化。
+
+### H-MOL-1 睡眠剥夺与线粒体负荷耦合检验
+**内容**：连续睡眠剥夺将显著提高 MOL，并伴随自噬效率下降与认知任务受损。
+**证伪条件**：剥夺后 MOL 不升高或与认知损害无关联。
+
+## 【理论边界/防误用声明】
+- 不采纳“恢复一晚睡眠即可逆转全部慢性代谢损伤”的推论。
+- 边界：SRT 预计存在时程滞后与累积阈值效应。
```

### Notes (brief)
- 已将文章主分类（清醒负荷/睡眠转运/外周清除/自噬修复）转为文件级补丁并映射 d 区间、能流态、\(\Psi_f\)。
- 新术语 SLCC、MOL 已附 `[Lineage/Source]`，并在目标文件写入 Header 级防误用声明。
