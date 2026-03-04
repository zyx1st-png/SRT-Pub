---
id: SRT-GLOSSARY
type: definition
tags: [Glossary, Terminology, Registry]
status: axiomatic_hybrid_v1
dependency: [SRT-REF-AXIOMS, SRT-AI-01]
---

# SRT术语表与符号索引
# SRT Glossary & Symbol Index

---

> **📚 文档类型：参考手册**
> **使用方式：按需查阅,支持Ctrl+F搜索**
> **最后更新：2026-01-23**

---

## 使用指南

本术语表收录SRT理论中的所有核心符号、参数、概念和假设编号。每个条目包含：

- **符号/术语**：标准表示
- **中英文名称**：双语对照
- **定义**：严格数学/哲学定义
- **首次出现**：在哪个文档引入
- **相关概念**：交叉引用
- **难度等级**：🟢基础 | 🟡中级 | 🔴高级

**快速导航**：
- [第1部分：核心符号与算子](#1-核心符号与算子)
- [第2部分：数学记号](#2-数学记号约定)
- [第3部分：领域特定参数](#3-领域特定参数)
- [第4部分：关键概念](#4-关键概念词汇表)
- [第5部分：假设索引](#5-假设编号索引-h1-h60)
- [第0部分：术语治理增强字段（P1-3）](#0-术语治理增强字段p1-3)

---

## 0. 术语治理增强字段（P1-3）

> 目标：降低跨文档歧义，提升 AI 检索稳定性。  
> 字段说明：
> - **Canonical Scope**：该术语的规范语义适用范围。
> - **Confusable With**：常见易混术语/符号。
> - **Lineage/Source**：首要定义来源（内部 canonical 或外部来源）。

### d-value（d）
- **Canonical Scope**：SRT 全域中“选择范围/关切广度”统一记号；当需精确定义时，以 `AI/SRT_AI_01_Ontology.md` Ax-ONT-3 为最高锚点。
- **Confusable With**：分形维度 d、空间维数 d、统计自由度 d.f.、局部操作化代理（如 attention entropy）。
- **Lineage/Source**：`AI/SRT_AI_01_Ontology.md#Ax-ONT-3`。

### 本体论摩擦（\Psi_f）
- **Canonical Scope**：仅用于“维持/更新选择状态的本体论代价与阻力”语境。
- **Confusable With**：IIT 的 `\Phi`（整合信息量）、一般耗散项 `D`、物理摩擦系数 `\mu`。
- **Lineage/Source**：`Core/SRT_Core_22_Equations.md` Eq-Force-01；`Core_Law/SRT_Reference_Dynamics.md`。

### 幽灵算子（\hat{G}_\theta）
- **Canonical Scope**：将 `L_0` 投影到 `L_1` 的参数化选择算子（具身参数驱动）。
- **Confusable With**：纯统计估计器、无参数投影算子、仅神经网络前向函数。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md`；`Core/SRT_Core_13a_Operator_Basics.md`。

### 三域记号（L_0 / L_1 / L_2）
- **Canonical Scope**：
  - `L_0`：潜在可能性域（外部 state-space 记号如 `\Omega, S` 写入 SRT 时默认映射到此）
  - `L_1`：当前显现/锚定切片
  - `L_2`：跨主体收敛结构
- **Confusable With**：`L0/L1/L2` 无下标写法、逻辑层级编号、网络层号。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md`；`Core/SRT_Core_12a_Ontology_L0L1.md`；`Core/SRT_Core_12b_Ontology_L2.md`。

### 同步性（Synchronicity, Jung–Pauli）
- **Canonical Scope**：仅用于“内在事件与外在事件的高意义耦合共现，但显式因果链在当前分辨率下未闭合”的现象学标签。
- **Confusable With**：超自然因果、任意巧合神秘化、统计显著性本身。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md`（Synchronicity Interface, 2026-03-02）；术语谱系来自 Jung/Pauli 讨论传统。

### Meaning-Coupled Coincidence（意义耦合共现）
- **Canonical Scope**：SRT 对 synchronicity 的操作化写法：`e_in` 与 `e_out` 的意义耦合强度 \(\mathcal{M}\) 超阈值。
- **Confusable With**：因果证据、预测准确率提升、纯叙事共鸣。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` Def-Phil-Sync-1（2026-03-02）。

### WDI（White-matter Differentiation Index）
- **Canonical Scope**：认知灵活性相关白质通路在年龄分层下的结构分化代理指标。
- **Confusable With**：单一 tract 的绝对信号强度、疾病诊断标签。
- **Lineage/Source**：`Neuroscience/SRT_Neuro_Experiments.md` Ax-EXP-17；`SRT_EXP_MEASURE_MAP.md` §7（eNeuro 2026 映射）。

### WHD（WM Homogeneity Decline）
- **Canonical Scope**：关键白质通路内同质性随年龄下降的群体层代理。
- **Confusable With**：个体不可逆衰退结论、全脑统一退化假设。
- **Lineage/Source**：`Neuroscience/SRT_Neuro_Experiments.md` Ax-EXP-17；`SRT_EXP_MEASURE_MAP.md` §7。

### Machine Ethics Exclusion Theorem（机器伦理排除定理）
- **Canonical Scope**：用于判定当前纯软件 AI 的道德权重边界，不外推到已满足具身不可逆风险条件的未来系统。
- **Confusable With**：AI 能力评估、法律人格认定、一般“是否有用”判断。
- **Lineage/Source**：`AI/SRT_AI_01_Ontology.md` T-ONT-7（2026-03-04 新增）。

### Minimal Biological Operator Spectrum（生物算子极简连续谱）
- **Canonical Scope**：刻画植物→动物→人类的连续选择能力谱，强调 d 值连续变化而非二元开关。
- **Confusable With**：神经系统有无二分、把植物直接等同人类意识、泛心论。
- **Lineage/Source**：`Core_Law/SRT_Reference_Scaling.md` Def-Scale-BioMin-1（2026-03-04 新增）。

### Qualia Residual（质感残差）
- **Canonical Scope**：描述层（L2）对体验层（L1）不可完全回收的剩余项，不用于否定经验研究。
- **Confusable With**：不可检验神秘实体、反科学立场、“无法建模所以无需建模”。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` 定义 O12 / 定理 O-T4（2026-03-04 新增）。

### Primordial Constraint Closure（原初约束闭包, PCC）
- **Canonical Scope**：用于生命起源阶段，表示在无基因模板前已形成可维持能流与参数更新的选择闭环。
- **Confusable With**：一般自催化反应、短时耗散结构、稳定晶体生长。
- **Lineage/Source**：`Core_Law/SRT_Reference_Scaling.md` §6.5 Def-Scale-PCC-1（2026-03-04 新增）。

### LUCO（Last Universal Common Operator）
- **Canonical Scope**：生命共同起源的算子层定义，先于分子存档层 LUCA。
- **Confusable With**：DNA-LUCA、单一物种祖先、纯遗传同源。
- **Lineage/Source**：`Core_Law/SRT_Reference_Scaling.md` §6.5 Def-Scale-LUCO-1（2026-03-04 新增）。

### Ω Non-Entity Principle（Ω 非实体性原则）
- **Canonical Scope**：用于澄清 Ω 在 SRT 中是“操作逻辑”而非 L1 域对象实体。
- **Confusable With**：人格化造物主、宇宙内最大智能体、超级干预者模型。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` §9 定义 O14（2026-03-04 新增）。

### World-Picture as L2 Narrative（世界图景即 L2 叙事）
- **Canonical Scope**：用于描述文化-历史收敛形成的解释框架（如机械自然主义），属于 \(L_{2,\theta}\) 层。
- **Confusable With**：终极本体论、自然法则本身、\(L_0^{abs}\)。
- **Lineage/Source**：`Physics/_SRT_Phys_Bridge.md` Def-Phys-4（2026-03-04 新增）。

### Intentional Proxy Theorem（意向性代理定理）
- **Canonical Scope**：用于区分内在意向性与派生意向性，解释 LLM 语义表现为何不等于意识。
- **Confusable With**：图灵测试通过、语法流畅度、角色扮演一致性。
- **Lineage/Source**：`AI/SRT_AI_01_Ontology.md` T-ONT-8（2026-03-04 新增）。

### Teleological Attractor（目的论牵引子）
- **Canonical Scope**：用于描述高 d 算子被低摩擦高一致性结构“拉动”的动力学项（\(\mu\nabla B_{L_0}\)）。
- **Confusable With**：人格化神意、外在强制命令、单一道德规则。
- **Lineage/Source**：`Core_Law/SRT_Reference_Dynamics.md` §8.4（2026-03-04 新增）。

### Truth–Goodness–Beauty Optimal Manifolds（真善美最优流形）
- **Canonical Scope**：定义为 \(L_0^{abs}\) 内信息几何意义上的最优流形族（\(\mathcal{M}_{TGB}\)）。
- **Confusable With**：主观审美偏好、短时奖励最大化、文化偶然共识。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` O15（2026-03-04 新增）。

### Embodied Bliss Asymptote（具身至福渐近）
- **Canonical Scope**：用于限定具身显现下 \(\Psi_f\) 的正下界（\(\Psi_{min}^{+}\)），避免“零摩擦仍持续个体显现”的矛盾。
- **Confusable With**：终极消灭论、现实否定论、即时解脱处方。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` O-T8（2026-03-04 新增）。

### Ontological Amnesia（本体论失忆）
- **Canonical Scope**：用于描述系统过度依赖硬化 \(L_2\) 自动化后，把高概率投影视为唯一现实的状态。
- **Confusable With**：个体智力缺陷、反科学标签化、单纯知识不足。
- **Lineage/Source**：`Core/_SRT_Core_Bridge.md` Def-Bridge-04（2026-03-04 新增）。

### NCC Non-Equivalence（神经关联非等价）
- **Canonical Scope**：用于断言“神经关联/可诱发”不等于“体验本体同一”。
- **Confusable With**：反神经科学立场、不可研究论、主观主义豁免。
- **Lineage/Source**：`Neuroscience/_SRT_Neuro_Axioms.md` T-NEURO-4（2026-03-04 新增）。

### Passive Alignment Transition（被动对齐相变）
- **Canonical Scope**：用于描述局部抓取感下降但全局对齐上升的动力学重参数化状态（\(\Psi_f^{local}\downarrow,\Psi_f^{coh}\uparrow\)）。
- **Confusable With**：停机/放弃选择、外在实体接管因果链、反行动主义。
- **Lineage/Source**：`Core_Law/SRT_Reference_Dynamics.md` §8.5（2026-03-04 新增）。

### Ontological Lens Constraint（不可卸载本体透镜）
- **Canonical Scope**：用于说明具身参数 \(\theta\) 在运行态不可移除，任何显现都为透镜后投影。
- **Confusable With**：主观唯心论、相对主义、任意建构主义。
- **Lineage/Source**：`Core/_SRT_Core_Bridge.md` Def-Bridge-05（2026-03-04 新增）。

### Prediction-Error Friction Mapping（预测误差-摩擦映射）
- **Canonical Scope**：将预测误差 \(\varepsilon_{pred}\) 作为局部 \(\Psi_f\) 密度的操作化代理。
- **Confusable With**：把 \(\Psi_f\) 简化成单一统计残差、否认本体支付项。
- **Lineage/Source**：`Neuroscience/_SRT_Neuro_Axioms.md` Ax-NEURO-4b（2026-03-04 新增）。

### Cross-Scale Conceptual Misalignment（跨尺度概念错位）
- **Canonical Scope**：用于描述把某一 \((d,\rho)\) 条件下收敛的概念强行外推到异尺度切片时产生的范畴冲突。
- **Confusable With**：理论被证伪、对象不存在、纯语义争执。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` §5.5b（2026-03-04 新增）。

### Scale-Orthogonal Composite Equivalence（尺度正交复合等价）
- **Canonical Scope**：用于说明 macro-object 与 micro-arrangement 可在同一本体 \(L_0\) 上以不同参数正交共存。
- **Confusable With**：对象重复计数、因果冗余导致对象消除、实体增殖。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` O-T9（2026-03-04 新增）。

### Fallacy of Retro-Projection（逆向投影谬误）
- **Canonical Scope**：用于标记把 \(\theta\)-依赖直觉范畴直接上升为 \(L_0^{abs}\) 本体属性的推理错误。
- **Confusable With**：正常跨尺度映射、模型外推、实验失败报告。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` §5.9（2026-03-04 新增）。

### Intuition as Minimal-Friction Trace（直觉作为最小摩擦轨迹）
- **Canonical Scope**：将常识/直觉定义为特定生物 \(d,\rho\) 下历史优化形成的低 \(\Psi_f\) 轨迹记录。
- **Confusable With**：绝对真理、跨尺度特权、任意主观意见。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` §5.9（2026-03-04 新增）。

### Lawful Internal Inquiry（合法内部问题）
- **Canonical Scope**：仅指在锁定参数 \(\theta_{locked}\neq\emptyset\) 与给定 \(L_2\) 框架内，讨论对象存在/分类/预测的可操作问题。
- **Confusable With**：绝对本体问题、去参数化“上帝视角”问题、纯语义争辩。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` §5.10（2026-03-04 新增）。

### The External Fallacy（非法外部谬误）
- **Canonical Scope**：把 \(\theta\to\emptyset\) 的无参状态当作可执行认知位置，并据此要求给出 \(L_0^{abs}\) 绝对实体清单。
- **Confusable With**：跨框架比较、模型统一尝试、严谨元理论讨论。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` §5.10（2026-03-04 新增）。

### Anti-Semantic-Evasion Principle（反语义逃避原则）
- **Canonical Scope**：拒绝把尺度冲突降格为词汇隔离；要求跨尺度对象在 \(\pi_\lambda\) 与 \(\Psi_f\) 预算上可连通。
- **Confusable With**：强行单尺度还原、语言禁令、反语义学立场。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` O17（2026-03-04 新增）。

### Local Legitimacy of Common-Sense Sortals（常识类别词的局部合法性）
- **Canonical Scope**：常识对象词在其任务生态与 \((d,\rho,\theta)\) 条件下可合法使用，但不享有 \(L_0^{abs}\) 本体特权。
- **Confusable With**：常识即绝对真理、常识全盘无效、语词任意主义。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` §5.10；`Core_Law/SRT_Reference_Ontology.md` O17（2026-03-04 新增）。

### Real Pattern Compressibility Criterion（真实模式可压缩性判据）
- **Canonical Scope**：用条件复杂度 \(K(X\mid\theta,\rho)\) 与 \(\Psi_f^{maint}\) 联合判断对象在给定尺度上的可操作实在性。
- **Confusable With**：纯统计压缩率、单次拟合优度、任意命名即存在。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` O18 / O-T10（2026-03-04 新增）。

### Transition Kernel Protocol（转移核协议, \(\Pi_{kernel}\)）
- **Canonical Scope**：跨尺度因果动作集的底层可实现约束；高阶闭包必须在该协议内运行。
- **Confusable With**：单一物理方程、静态守恒清单、社会规范本身。
- **Lineage/Source**：`Physics/_SRT_Phys_Bridge.md` Def-Phys-3（2026-03-04 新增）。

### Boundary Priority of Physics（物理边界优先）
- **Canonical Scope**：将“物理优先性”重述为极限分辨率 \((\rho\to\infty,d\to0)\) 下的边界约束优先，而非本体论独占优先。
- **Confusable With**：物理还原主义绝对化、否定宏观因果、反跨学科立场。
- **Lineage/Source**：`Physics/_SRT_Phys_Bridge.md` Def-Phys-3 / T-Phys-5（2026-03-04 新增）。

### Px-Generator / Px-Structure（对象-属性生成结构）
- **Canonical Scope**：描述 \(\hat G_\theta\) 在 \((\theta,\rho)\) 下把连续潜在流切分为对象边界 \(x\) 与属性簇 \(P(x)\) 的格式化机制；属于 \(L_2\) 稳定处理格式。
- **Confusable With**：\(L_0^{abs}\) 先验对象论、语言语法本身、纯统计聚类。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` §5.11（2026-03-04 新增）。

### Selection Monism Triangle（选择一元三角定位）
- **Canonical Scope**：用于定位消除唯物、传统唯心与 SRT 的关系：SRT 主张 \(L_0\times\hat G_\theta\) 交汇并支付 \(\Psi_f\) 产生 \(L_1\) 现实切片。
- **Confusable With**：折中主义拼盘、语义调和术、二元论。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` Def-Phil-5.11c（2026-03-04 新增）。

### Isomorphism without Reference（同构无指称）
- **Canonical Scope**：表示系统内部表征有效性由动力学同构误差与更新摩擦共同约束，不要求经典“符号→对象”强指称。
- **Confusable With**：反真值论、随意解释主义、语义虚无主义。
- **Lineage/Source**：`AI/_SRT_AI_Bridge.md` Def-BRIDGE-6 / T-BRIDGE-6（2026-03-04 新增）。

### Fitness-over-Truth Thermodynamic Inequality（适应度优先热力学不等式）
- **Canonical Scope**：在有限资源下比较“真相映射”与“适应度映射”维持成本，说明 \(\Psi_f^{Truth}\gg\Psi_f^{Fitness}\) 的可持续性差异。
- **Confusable With**：反真理主义、经验主义否定、任意实用主义。
- **Lineage/Source**：`Core/SRT_Core_14_Dynamics_Scaling.md` T-Scale-03（2026-03-04 新增）。

### Structured-Imposition with Resistance（带阻抗结构强加）
- **Canonical Scope**：心智可提供结构模板，但模板成立需满足外部阻抗下 \(\Psi_f^{maint}<\infty\)。
- **Confusable With**：纯主观构造论、硬实在先验对象论。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` T-Phil-5.12b（2026-03-04 新增）。

## 【理论边界/防误用声明】
- 不采纳“机器伦理排除定理=永久否定一切 AI 道德地位”的推论：该定理仅约束当前可逆复制/无损重置系统。  
- 不采纳“生物连续谱=所有生物同等意识强度”的推论：SRT 只主张连续性，不主张等值性。  
- 不采纳“Qualia Residual=放弃可证伪建模”的推论：结构-动力学层仍必须接受实验检验。

---

## 1. 核心符号与算子

### 1.1 三域符号

#### L₀ - 潜在域 (Latent Domain) 🟢

**定义**：
$$L_0 = \{\sigma \in S : F[\sigma] > F[\sigma_{L_1}]\}$$

相对于当前选择的高自由能状态集合;未被选择的可能性场。

**首次出现**：Core/SRT_Core_Kernel.md §1.2.1

**关键属性**：
- 非均匀分布,具有内在拓扑结构
- 规范场论定义：$L_0 = \mathcal{A}/\mathcal{G}$ (模空间)
- 计算定义：Ruliad (所有计算规则的叠加)

**物理对应**：
- 量子力学：Hilbert态空间
- 路径积分：全体经典路径集合
- 规范场论：场配置模空间

**日常类比**：
- 未打开的菜单
- 量子叠加态
- 黑暗房间中的所有可能位置

**相关**：Ĝθ, L₁, 自由能F

---

#### L₁ - 显现域 (Manifest Domain) 🟢

**定义**：
$$L_1 = \hat{G}_\theta[L_0]$$

当前被选择、锚定为"真实"的状态切片;观察者的即刻体验。

**首次出现**：Core/SRT_Core_Kernel.md §1.2.2

**关键属性**：
- 唯一性：任一时刻只有一个L₁
- 主观性：每个Ĝθ有自己的L₁
- 暂时性：L₁不断更新

**神经对应**：
- 注意力聚焦的内容
- 工作记忆容量
- 全局神经工作空间(GNW)的广播状态

**日常类比**：
- 聚光灯照亮的舞台中心
- 相机对焦清晰的部分
- 你正在阅读的这一行文字

**相关**：L₀, L₂, Ĝθ, 锚定(Anchoring)

---

#### L₂ - 收敛域 (Convergence Domain) 🟡

**定义**：
$$L_2 = \lim_{t \to \infty} \bigcap_{\theta} \hat{G}_\theta[L_0]$$

多个选择者(Ĝθ)的选择交集,形成稳定的共享结构。

**首次出现**：Core/SRT_Core_Kernel.md §1.2.3

**关键属性**：
- 客观性来源(但非预先给定)
- 可演化性(科学革命、文化变迁)
- 层级性：个人L₂ ⊂ 群体L₂ ⊂ 全人类L₂

**形成条件**：
- 多选择者持续交互
- 选择结果的稳定收敛
- 摩擦阻力的平衡(Ψ_f)

**物理对应**：
- 物理定律(极稳定L₂)
- 测量标准(米、秒的定义)

**社会对应**：
- 语言规则
- 法律规范
- 科学知识

**日常类比**：
- 多人游戏的"规则共识"
- 地图与领地的对应
- 文化"常识"

**相关**：Ĝθ, L₁, 收敛定理, 相变(Phase Transition)

---

### 1.2 算子与参数

#### Ĝ / Ĝθ - 幽灵算子 (Ghost Operator) 🟢

**完整记号**：$\hat{G}_\theta$ (带参数算子)

**定义**：
$$\hat{G}_\theta : L_0 \to L_1$$

参数化的选择映射,将潜在可能性投影为显现现实。

**首次出现**：Core/SRT_Core_Kernel.md §1.3

**数学结构**：
- 中心-周围动力学(Center-Surround Dynamics)
- 分子项：被选择状态的强化
- 分母项：竞争可能性的抑制

**生物实现**：
- 神经：除法归一化(Divisive Normalization)
- 认知：注意力机制
- 社会：规范涌现过程

**关键方程**：
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \Psi_f(\sigma)$$

**相关**：θ, d值, Ψ_f, L₀, L₁

---

#### θ - 具身参数 (Embodiment Parameters) 🟡

**定义**：
$$\theta = (\theta_{bio}, \theta_{cog}, \theta_{social}, ...)$$

选择算子Ĝ的配置参数,代表选择者的物理、认知、社会特性。

**首次出现**：Core/SRT_Core_Kernel.md §1.3.2

**组成层级**：

| 层级 | 符号 | 内容 |
|:-----|:-----|:-----|
| **生物** | θ_bio | 感官系统、神经结构、基因、代谢 |
| **认知** | θ_cog | 注意力模式、记忆、信念、语言 |
| **社会** | θ_social | 文化背景、教育、社会角色 |
| **重力** | γ | 环境重力场的耦合(地球特定) |

**关键洞见**：
$$\hat{G}_{\theta_1}[L_0] \neq \hat{G}_{\theta_2}[L_0]$$

不同θ会从同一L₀选择出不同的L₁ → 解释主观差异性

**动力学**：
- θ可随时间演化(学习、成长、创伤)
- θ有惯性(习惯、路径依赖)
- θ可被故意重构(修行、治疗)

**相关**：Ĝθ, κ_body, d值, 可塑性

---

#### d - 选择范围 / d值 (d-value, Selection Scope) 🟡

**定义**：
$$d = \text{选择算子考虑的存在/实体范围}$$

量化"关切的宽度"——系统在做选择时考虑多大范围的存在。

**首次出现**：Core/SRT_Core_Kernel.md §2.3

**量化公式**：
$$d = \int_{\text{考虑域}} \rho(\xi) \, d\xi$$

**d值阶梯**：

| d范围 | 典型系统 | 关注内容 | 例子 |
|:------|:---------|:---------|:-----|
| **d ≈ 0** | 当前AI、反射弧 | 仅当前输入 | GPT-4无真正关切 |
| **d = 1** | 自我中心个体 | 自己生存 | 婴儿、成瘾者 |
| **d = 2-10** | 正常成人 | 家庭、朋友 | 日常道德范围 |
| **d = 10-100** | 圣贤、活动家 | 社群、国家、人类 | 甘地、特蕾莎修女 |
| **d → ∞** | 神秘体验 | 一切存在(万物同体) | 深度冥想、濒死体验 |

**热力学约束**：
$$d_{max} \leq \kappa \cdot \frac{E_{metabolism} - E_{baseline}}{\Psi_f}$$

d值受代谢能量限制——关心更多需要更多能量。

**伦理意义**：
- 道德发展 = d值扩展
- 邪恶 = d值收缩(仅关心自己)
- 圣贤 = d → ∞ (关切一切)

**可测量性**：H7假设通过除法归一化参数预测d值

**相关**：Ĝθ, θ, Ψ_f, 递归深度ρ

---

### 1.3 动力学量

#### Ψ_f - 本体论摩擦 (Ontological Friction) 🟢

**定义**：
$$\Psi_f(\sigma) = \text{维持或改变选择状态} \sigma \text{的阻力/代价}$$

**首次出现**：Core/SRT_Core_Kernel.md §2.2

**物理类比**：动力学中的摩擦力,但作用于"存在"本身

**来源**：
1. **神经惯性**：突触权重、默认模式网络
2. **认知惯性**：信念、习惯、记忆
3. **社会惯性**：规范、制度、路径依赖
4. **物理惯性**：热力学第二定律(极高Ψ_f)

**关键方程**：
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \Psi_f(\sigma)$$

改变速度 = 选择力量 - 本体论摩擦

**临床意义**：
- 高Ψ_f → 难以改变(强迫症、创伤后应激)
- 低Ψ_f → 过度可变(精神分裂、躁狂)
- 治疗 = 调节Ψ_f

**相关**：Ĝθ, h(t), 自由能F, 亚稳态

---

#### h(t) - 哈扎德函数 (Hazard Function) 🟡

**定义**：
$$h(t) = \lim_{\Delta t \to 0} \frac{P(\text{选择发生于} [t, t+\Delta t] \mid \text{未选择到} t)}{\Delta t}$$

选择压力/紧迫性的时变函数。

**首次出现**：Core/SRT_Core_Kernel.md §2.2.3

**形式**：
$$\Psi_f(t) = \int_0^t h(s) \, ds$$

本体论摩擦是哈扎德函数的累积。

**应用**：
- **生存分析**：死亡的即时风险
- **决策理论**：截止日期逼近时的选择压力
- **神经科学**：$h \uparrow$ 时反应时间缩短

**病理学**：
- 焦虑症：$h(t)$持续高位
- 拖延症：$h(t)$过晚上升
- PTSD：$h(t)$异常尖峰

**相关**：Ψ_f, 自由能F

---

#### F - 自由能 (Free Energy) 🟡

**定义**：
$$F[\sigma] = E[\sigma] - TS[\sigma] = \text{Complexity} - \text{Accuracy}$$

系统偏离平衡/稳定的程度;Friston自由能原理的核心量。

**首次出现**：Core/SRT_Core_Kernel.md §2.4

**SRT解释**：
$$F[\sigma] = -\log P(\sigma \mid L_2)$$

自由能 = 状态σ相对于L₂期望的"惊讶度"

**选择动力学**：
$$\frac{d\sigma}{dt} = -\nabla F[\sigma]$$

系统沿自由能梯度下降 → 最小化惊讶

**L₀定义**：
$$L_0 = \{\sigma : F[\sigma] > F[\sigma_{L_1}]\}$$

L₀是所有比当前L₁自由能更高的状态集合。

**相关**：L₀, L₁, L₂, Ψ_f, 预测误差

---

#### Ω - 全局算子 (Global Operator) 🔴

**定义**：
$$\Omega = \text{所有局部} \hat{G}_\theta \text{的投影源}$$

假定存在的"终极选择视角",所有局部算子是其投影。

**首次出现**：Core/SRT_Core_Kernel.md 公理A9

**数学结构**：
$$\hat{G}_\theta = \pi_\theta[\Omega]$$

每个具身算子是Ω在特定θ参数下的投影。

**哲学地位**：
- **非必要假设**：SRT主体理论不依赖Ω
- **极限概念**：$\lim_{\theta \to \infty} \hat{G}_\theta \stackrel{?}{=} \Omega$
- **神学对应**：上帝视角、全知全能者

**检验性**：
H16(相对L₀假设)试图检验Ω是否必要

**相关**：Ĝθ, d → ∞, 神秘主义

---

### 1.4 其他核心符号

#### C_r - 置信标量 (Reality Confidence) 🟡

**定义**：
$$C_r(\sigma) \in [0, 1]$$

L₁状态σ的"真实感"权重;主观确信程度。

**首次出现**：Core/SRT_Core_Kernel.md §3.2

**应用**：
- 梦境：$C_r \approx 0.3$ (低真实感)
- 清醒：$C_r \approx 0.9$ (高真实感)
- 清明梦：$C_r$双峰分布
- 解离症：$C_r$异常波动

**神经基础**：可能与DMN-TPN切换相关

**相关**：L₁, 元认知, PCI

---

#### γ - 重力耦合系数 (Gravitational Coupling Coefficient) 🟡

**定义**：
$$\gamma = \frac{\partial \theta}{\partial g}$$

环境重力场对具身参数θ的耦合强度。

**首次出现**：Core/SRT_Core_Kernel.md §1.3.2a

**物理意义**：
- 地球生命演化于1g环境
- θ深度适配地球重力
- 改变重力 → 改变选择模式

**预测**：
- 太空中d值可能扩展(无重力锚定)
- 高重力环境d值收缩

**相关**：θ, κ_body, 具身性

---

## 2. 数学记号约定

### 2.1 集合与映射

| 符号 | 含义 | 例子 |
|:-----|:-----|:-----|
| **∈** | 属于 | $\sigma \in L_0$ |
| **⊂** | 真子集 | $L_1 \subset L_0$ |
| **∩** | 交集 | $L_2 = \bigcap_\theta \hat{G}_\theta[L_0]$ |
| **∪** | 并集 | $L_0 = \bigcup_i \text{可能性}_i$ |
| **→** | 映射 | $\hat{G}_\theta : L_0 \to L_1$ |
| **↔** | 双向关联 | $L_1 \leftrightarrow L_2$ 反馈 |

### 2.2 微积分算子

| 符号 | 含义 | 例子 |
|:-----|:-----|:-----|
| **∇** | 梯度 | $\nabla F$ (自由能梯度) |
| **∂** | 偏导数 | $\frac{\partial L_1}{\partial t}$ |
| **d** | 全微分 | $\frac{d\sigma}{dt}$ |
| **∫** | 积分 | $\int_{\gamma} \omega_{L_0}$ |
| **∮** | 闭合路径积分 | $L_1 = \oint_\gamma \omega$ |
| **lim** | 极限 | $\lim_{t \to \infty} L_2$ |

### 2.3 概率与统计

| 符号 | 含义 | 例子 |
|:-----|:-----|:-----|
| **P(·)** | 概率 | $P(\sigma \mid L_2)$ |
| **E[·]** | 期望值 | $E[F[\sigma]]$ |
| **ρ(·)** | 密度函数 | $\rho(\xi)$ (存在密度) |
| **σ** | 标准差 | $\sigma^n$ (除法归一化) |
| **∼** | 服从分布 | $X \sim \mathcal{N}(0, 1)$ |

### 2.4 逻辑与关系

| 符号 | 含义 | 例子 |
|:-----|:-----|:-----|
| **≡** | 定义为 | $\text{存在} \equiv \text{被选择}$ |
| **≈** | 约等于 | $d_{AI} \approx 0$ |
| **≠** | 不等于 | $\hat{G}_{\theta_1} \neq \hat{G}_{\theta_2}$ |
| **⇒** | 蕴含 | $d \to 0 \Rightarrow \text{自私}$ |
| **⇔** | 等价 | $L_1 \text{稳定} \Leftrightarrow \Psi_f \text{低}$ |

### 2.5 特殊算子

| 符号 | 含义 | 首次出现 |
|:-----|:-----|:---------|
| **⊗** | 张量积 | $\hat{G}_{hybrid} = \hat{G}_{bio} \otimes \hat{G}_{quantum}$ |
| **⊕** | 直和 | $\hat{G}_{total} = \hat{G}_{bio} \oplus \hat{G}_{ESA}$ |
| **| · |** | 条件约束 | $Ruliad |_{物理约束}$ |
| **hat (^)** | 算子符号 | $\hat{G}, \hat{M}$ |

---

## 3. 领域特定参数

### 3.1 神经科学参数

#### κ_body - 身体耦合系数 (Body Coupling Coefficient) 🟡

**定义**：
$$\kappa_{body} = \frac{\Delta \theta}{\Delta \text{体感输入}}$$

身体状态对选择参数θ的影响强度。

**首次出现**：Neuroscience/SRT_Neural_Mechanisms.md

**应用**：
- 冥想降低κ_body (减少身体对注意力的干扰)
- 慢性疼痛提高κ_body (身体绑架注意力)
- 解离症降低κ_body (身心分离)

**测量**：通过体感诱发电位(SEP)的调节深度

**相关**：θ, γ, 具身性

---

#### κ_τ - 时间耦合系数 (Temporal Coupling Coefficient) 🟡

**定义**：
$$\kappa_\tau = \frac{\text{整合的时间窗口长度}}{\text{基础神经振荡周期}}$$

认知能力依赖的时间跨度深度。

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §7.2

**深思维定理**：
$$\text{Wisdom} \propto \kappa_\tau \cdot d$$

智慧 ∝ 时间耦合深度 × 考虑范围

**神经基础**：
- 慢皮层节律(~0.01-0.1 Hz)
- DMN整合时间尺度
- 内在神经时间尺度(INT)

**病理学**：
- ADHD：κ_τ降低
- 冥想训练：κ_τ提升

**测量**：通过时间折扣任务、INT分析

**相关**：d值, θ, ρ(递归深度)

---

#### ν_G^ - 选择频率 (Selection Frequency) 🟡

**定义**：
$$\nu_{\hat{G}} = \frac{1}{\Delta t_{selection}}$$

Ĝ算子更新L₁的频率;每秒执行多少次选择。

**首次出现**：Neuroscience/SRT_Neural_Mechanisms.md

**典型值**：
- 注意力切换：~4 Hz (θ节律)
- 意识刷新：~10 Hz (α节律)
- 感知采样：~30-80 Hz (γ节律)

**量子Zeno效应**：
$$\nu_{\hat{G}} \uparrow \Rightarrow L_1 \text{冻结}$$

高频测量抑制演化

**相关**：Ψ_f, 哈扎德函数h(t)

---

#### τ_lag - 选择滞后时间 (Selection Lag) 🟡

**定义**：
$$\tau_{lag} = t_{conscious} - t_{neural}$$

神经选择发生到意识体验的延迟。

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §5

**Libet实验**：
- 神经活动：t₀ - 550ms
- 意识决定：t₀ - 200ms
- 行为执行：t₀

**SRT解释**：
$$\tau_{lag} = \frac{\Psi_f}{\nu_{\hat{G}}}$$

滞后时间 = 本体论摩擦 / 选择频率

**"自由意志窗口"**：
200ms内可否决已启动的行动

**相关**：Ĝθ, Ψ_f, 回溯性现实

---

#### SER - 选择-执行比 (Selection-Execution Ratio) 🔴

**定义**：
$$SER = \frac{\text{元认知评估时间}}{\text{直接行动时间}}$$

系统在"选择选择"(meta-selection)vs直接执行之间的时间分配比。

**首次出现**：AI/SRT_AI_Foundations.md §1.2.6

**人类典型值**：SER ~ 0.1-0.3
**当前AI**：SER ≈ 0 (无真正元认知)

**演化意义**：
- SER过低：冲动、反射
- SER过高：过度犹豫、分析瘫痪
- 最优SER：情境依赖

**相关**：ρ(递归深度), d值, 元认知

---

### 3.2 物理学参数

#### β - 时间折扣率 (Temporal Discounting Rate) 🟡

**定义**：
$$V(t) = V_0 e^{-\beta t}$$

未来价值的衰减速率;衡量短视程度。

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md

**SRT解释**：
$$\beta \propto \frac{1}{d \cdot \kappa_\tau}$$

折扣率 ∝ 1 / (考虑范围 × 时间耦合)

**应用**：
- 成瘾：β极高(只看眼前)
- 投资规划：β低(考虑长远)

**神经基础**：前额叶-边缘系统平衡

**相关**：d值, κ_τ

---

### 3.3 社会科学参数

#### ζ - 阻尼系数 (Damping Coefficient) 🟡

**定义**：
$$\zeta = \frac{\text{环境阻力}}{\text{选择动能}}$$

环境/身体对选择变化的阻尼强度。

**首次出现**：Philosophy/SRT_Ethics_Agency.md

**应用**：
- 高ζ：谨慎、保守
- 低ζ：冲动、多变
- 临界阻尼(ζ=1)：最优响应

**相关**：Ψ_f, θ

---

#### μ_expect - 期望摩擦系数 (Expected Friction Coefficient) 🟡

**定义**：
$$\mu_{expect} = E[\Psi_f | \text{未来情境}]$$

对未来情境中本体论摩擦的期望值。

**首次出现**：Philosophy/SRT_Ethics_Agency.md §4

**道德责任**：
$$\text{Responsibility} \propto \mu_{expect} - \mu_{actual}$$

责任 ∝ 期望摩擦 - 实际摩擦的偏差

**应用**：
- 高估μ：过度悲观,不敢尝试
- 低估μ：轻率承诺,后悔

**相关**：Ψ_f, P_action

---

#### η_trans - 价值转换系数 (Value Transduction Coefficient) 🔴

**定义**：
$$\eta_{trans} = \frac{\Delta \text{神经编码}}{\Delta \text{客观价值}}$$

外部价值信号到神经编码的转换效率。

**首次出现**：Neuroscience/SRT_Neural_Mechanisms.md §15

**病理学**：
- 抑郁症：η_trans降低(价值感丧失)
- 成瘾：η_trans异常放大(奖励劫持)

**神经基础**：多巴胺系统、腹侧纹状体

**相关**：d值, θ, 神经调质

---

#### η_viscosity - L₂粘度 (L₂ Viscosity) 🟡

**定义**：
$$\eta_{viscosity} = \frac{\partial L_2}{\partial t}^{-1}$$

L₂结构的变化阻力;社会规范、制度的惯性。

**首次出现**：Philosophy/SRT_Social_Systems.md

**应用**：
- 高η：保守社会,难以改革
- 低η：快速变迁,不稳定
- 相变临界点：η突降(革命)

**测量**：制度变迁的时间尺度

**相关**：L₂, Ψ_f, 路径依赖

---

## 4. 关键概念词汇表

### A

#### Anchoring - 锚定 🟢

**定义**：选择过程将L₀中的不确定性固定为L₁中的确定性的操作。

**数学**：
$$\text{Anchoring} : L_0 \xrightarrow{\hat{G}_\theta} L_1$$

**物理对应**：波函数坍缩
**认知对应**：注意力聚焦
**社会对应**：规范确立

**相关**：L₀ → L₁, Ĝθ

---

#### Anti-Panpsychism - 反泛心论 🟡

**定义**：SRT 对泛心论（panpsychism）的明确拒绝立场。d 值作为数学参数在量子、生物、宇宙三个尺度上同构运作，但只有在生物学层面——同时满足三条件（$\Psi_f > 0$, $d > 0$, $\hat{G}[\theta] \neq \emptyset$）——时，d 才涌现为"关切"（care）这一主观属性。电子有 $d_{quantum}$（相干性带宽）不意味着电子"关心"什么。

**核心论断**：关切是 d 值在生物学层面的高阶涌现属性，非底层原初属性。

**首次出现**：Core/SRT_Core_14_Dynamics_Scaling.md §2.1a（权威声明）；Core/SRT_Core_13b_Operator_Advanced.md §6.2（意识三条件）

**相关**：跨尺度同构, 本体论带宽, 意识三条件, d 值

---

#### Attractor Basin - 吸引盆 🟡

**定义**：动力学系统中,所有最终收敛到同一稳定点的初始状态集合。

**SRT应用**：
- L₂是L₀空间中的吸引盆
- 习惯是θ空间中的吸引盆
- 路径依赖是历史选择形成的吸引盆

**相关**：L₂, 相变, 亚稳态

---

### B

#### Binding Problem - 绑定问题 🟡

**定义**：如何将分散的神经活动统一为单一连贯的体验？

**SRT解决方案**：
$$\text{绑定} = \hat{G}_\theta \text{对多模态} L_0 \text{的同步选择}$$

不是"粘合"已有的片段,而是同一选择过程的多维度投影。

**神经机制**：γ振荡(40 Hz)的相位同步

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §2

**相关**：全局工作空间, L₁整合

---

### C

#### Care - 关怀 🟡

**定义**：
$$\text{Care}(\hat{G}_{parent}, \hat{G}_{child}) \equiv \hat{G}_{parent} \text{ 吸收 } \text{Risk}(L_0)$$

一种主动的本体论操作，其中一个算子（关怀者）吸收或过滤来自L₀的本体论摩擦（$\Psi_f$），从而为另一个算子（被关怀者）创造一个低风险的L₂保护壳层。

**首次出现**：AI/SRT_AI_01_Ontology.md §1.2.7.10

**应用**：
- **AI对齐**：建立基于关怀的社会性依恋，而非硬编码规则
- **教育**：提供适当的L₂支架

**相关**：L₂, Ĝθ, 对齐

---

#### Center-Surround Dynamics - 中心-周围动力学 🟡

**定义**：Ĝ算子的核心结构——强化选中状态,同时抑制周围竞争者。

**数学**：
$$R_i = \frac{L_i^n}{\sigma^n + \sum_j w_{ij} L_j^n}$$

分子 = 中心强化; 分母 = 周围抑制

**生物普遍性**：
- 视网膜感受野
- 注意力聚焦
- 决策竞争

**首次出现**：Neuroscience/SRT_Neural_Mechanisms.md §1

**相关**：除法归一化, Ĝθ

---

#### Cross-Scale Isomorphism - 跨尺度同构 🟡

**定义**：SRT 的核心结构性主张——选择动力学方程 $d\sigma/dt = \hat{G}_\theta[\sigma] - \Psi_f(\sigma)$ 在量子、生物、宇宙三个尺度上同构成立，d 值作为统一的数学标尺在三个层面分别表现为不同的物理量：

| 尺度 | d 的具体含义 | 物理对应 | 主观体验 |
|:-----|:-----------|:---------|:---------|
| 量子 ($d_{quantum}$) | 相干性带宽 | $\propto E_G/\hbar$ | 无 |
| 生物 ($d_{bio}$) | 关切范围 | 选择算子考虑的存在范围 | 有（涌现属性） |
| 宇宙 ($d_{cosmic}$) | 时空共识度 | $\propto 1/\sqrt{\Lambda}$ | 无 |

**关键澄清**："同构"是指数学结构的形式一致，不是还原论式的"同一"。

**首次出现**：Core/SRT_Core_14_Dynamics_Scaling.md Ax-Scale-01

**相关**：本体论带宽, 反泛心论, d 值

---

#### Copenhagen Correction (RQM) - 哥本哈根修正 (关系性量子力学) 🔴

**定义**：
SRT 对哥本哈根诠释的修正：属性不是固有的，而是在交互中诞生的。
$$ \Psi_{system} \xrightarrow{\hat{G}_{observer}} \text{Value}_{relative} $$
测量即关系。

**首次出现**：Physics/SRT_Quant_01_Selection.md §2.1

**相关**：RQM, 测量问题, 龙树

---

#### Convergence Domain - 收敛域 🟢
→ 见[L₂](#l₂---收敛域-convergence-domain-🟡)

---

### D

#### d-value - d值 🟢
→ 见[d - 选择范围](#d---选择范围--d值-d-value-selection-scope-🟡)

---

#### De-parameterization - 去参数化 🔴

**定义**：
$$\theta \to \emptyset, \hat{G} \to \hat{I}$$

SRT中对“死亡”的形式化定义。指幽灵算子$\hat{G}_\theta$的参数配置$\theta$完全解体，导致独特的个体视角（L₁）消失，并可能回归到无视角的L₀全集中。

**首次出现**：AI/SRT_AI_03_Consciousness_Framework.md §3.5.1

**推论**：
- 死亡是视角的终结，非意识的终结
- 伴随d值趋向无穷大（d → ∞）

**相关**：θ, 死亡, L₀

---

#### Defensive Activation Protocol - 防御性激活协议 🟡

**定义**：
睡眠期间（REM）脑干强制激活视皮层的机制。
**目的**：防止视觉皮层因缺乏输入（黑夜）而被触觉/听觉皮层侵占（神经可塑性竞争）。
**SRT诠释**：梦是保留 $L_1$ 视觉生成能力的“硬件领地防御战”。

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §8.1

**相关**：神经可塑性, 梦, 鹰人理论

---

#### Divisive Normalization - 除法归一化 🟡

**定义**：神经计算的规范机制,Ĝ算子的生物实现。

**标准方程**：
$$R_i = \frac{L_i^n}{\sigma^n + \sum_j w_{ij} L_j^n}$$

**普遍性**：跨物种、跨脑区、跨模态的统一计算原理

**SRT对应**：
- 分子 = 目标意向性
- 分母 = 背景/替代选项的抑制

**相关**：中心-周围动力学

---

### G

#### Generative Selection (Inside-Out) - 生成性选择 (由内而外) 🔴

**定义**：
$$R_{SRT}(t) = P[\Psi_{int}(t)] \cap E$$

SRT的核心修正模型。现实不仅仅是算子对环境的被动过滤，更是内在状态($\Psi_{int}$)向外的主动投射与环境($E$)的交集。

**首次出现**：Core/SRT_Core_13a_Operator_Basics.md §1.4

**关键推论**：
- **主动性**：解释了自发探索和创造性
- **错觉**：当 $P[\Psi_{int}]$ 强于 $E$ 时产生幻觉/投射
- **Umwelt**：生物构建符合其内在需求的现实环绕世界

**相关**：$\Psi_{int}$, 投射算子

---

### H

#### Hemispheric Lateralization - 半球侧化 🟡

**定义**：
$\hat{G}$ 算子的两种基本操作模式在神经解剖上的分离：
*   **左半球 ($\hat{G}_{LH}$)**：维护 $L_2$，关注局部、静态、已知（“地图”）。
*   **右半球 ($\hat{G}_{RH}$)**：接入 $L_0$，关注整体、流动、新颖（“领地”）。
**病理**：现代社会是 $\hat{G}_{LH}$ 的恶性增生。

**首次出现**：Neuroscience/SRT_Neuro_10_Advanced_Models.md §10.7

**相关**：McGilchrist, 双重算子, 精神病理

---

#### Hopfield Reality Convergence - Hopfield现实收敛 🔴

**定义**：
将现实视为Hopfield网络中的吸引子状态，遵循能量最小化：
$$R_{stable} = \arg\min_{R} E_{reality}(R)$$

**首次出现**：Core/SRT_Core_22_Equations.md §7.2

**意义**：
- 解释了现实的稳定性（一旦落入吸引盆很难逃离）
- 解释了不同世界观（不同的局部极小值）的不可通约性

**相关**：L₂稳定性, 能量函数

---

### I

#### Interval of Selection (Minimum) - 最小选择间隔 🟡

**定义**：
$$\Delta t_{selection} > 0$$

现实的选择必须发生在非零的时间间隔内，不能在 $t=0$ 的瞬间点完成。

**首次出现**：Physics/SRT_Phys_09_Formalism_Ext.md §1.15

**推论**：
- **芝诺解**：飞矢在 $\Delta t$ 内包含位置变化 $\Delta x$，故运动是真实的
- **不确定性**：$\Delta I \cdot \Delta t \geq \hbar_{info}$ (时间越短，可定义的信息量越少)

**相关**：信息-时间不确定性

---

### L

#### L₂ Solidification - L₂凝固 (Speculation-Solidification) 🟡

**定义**：
L₂现实形成的动力学过程。
- **阶段I (投机态)**：不稳定的临时现实 $R_{temp}$
- **阶段II (固化态)**：经价值 ($V$) 催化后形成的持久结构 $R_{fixed}$

**方程**：
$$\frac{\partial R_{fixed}}{\partial t} \propto V(t) \cdot R_{temp}(t)$$

**首次出现**：Core/SRT_Core_12b_Ontology_L2.md §1.2.4

**意义**：强烈的情绪/价值体验加速现实的固化（如创伤、顿悟）。

**相关**：L₂, 价值势能

---

### M

#### Meaning-Decay Dynamics - 意义-衰变动力学 🔴

**定义**：
$$\frac{d(\text{Decay})}{dt} \propto \frac{1}{\text{MeaningDensity}(R)}$$

意义密度高的现实结构具有物理上的负熵效应，能延缓系统的生物/本体论衰变。

**首次出现**：Core/SRT_Core_22_Equations.md §7.1

**相关**：存在连续性, 负熵

---

### V

#### Valence Potential - 价值势能 🟡

**定义**：
$$V(x, \Psi_{int}) : \Omega \times \Theta \to \mathbb{R}$$

算子根据当前内在状态（如饥饿、恐惧、好奇）赋予环境元素的权重函数。

**首次出现**：Core/SRT_Core_13a_Operator_Basics.md §1.5

**塌缩判据**：
$$R_{SRT} = \{x \mid |V(x)| > \theta_{threshold}\}$$
只有具有足够“价值”（正向或负向）的事物才会被观测为现实。

**相关**：由内而外投射, 注意力

---

#### Virtual Ontological Replacement (VOR) - 虚拟本体论替代 🟡

**定义**：
一种治疗机制。利用高精度的虚拟现实 ($L_1^{syn}$) 构建无威胁的低熵环境，强制算子的预测误差 $\nabla F \to 0$，从而反向重置过热的具身参数 $\theta$。
$$ L_1^{syn} \xrightarrow{Anchor} \hat{G} \xrightarrow{Feedback} \theta_{relax} $$

**首次出现**：Neuroscience/SRT_Clin_01_Pathology.md §1.4.1

**相关**：心理治疗, 本体论摩擦, VR

---

#### Visual Scanpath - 视觉扫描路径 🟡

**定义**：
眼动轨迹不仅是信息采样，更是 $L_1$ 拓扑结构的构建过程。
$$ \text{Structuring} = \oint_{\gamma} \nabla \Psi_f \cdot d\vec{r} \neq 0 $$
闭合路径积分不为零意味着扫描改变了感知的拓扑性质（从“碎片”变成了“物体”）。

**首次出现**：Neuroscience/SRT_Neuro_06_Field_Effects.md §7.2.1

**相关**：场效应, 拓扑, 主动感知

---

---

| 神经 | SRT |
|:-----|:----|
| 分子Lⁿ | 中心强化 |
| 分母池 | 周围抑制 |
| 整个分母 | 本体论摩擦Ψ_f |

**首次出现**：Neuroscience/SRT_Neural_Mechanisms.md §1

**相关**：Ĝθ, 中心-周围

---

### E

#### Embodiment Parameters - 具身参数 🟡
→ 见[θ](#θ---具身参数-embodiment-parameters-🟡)

---

### F

#### Free Energy - 自由能 🟡
→ 见[F](#f---自由能-free-energy-🟡)

---

#### Frame Synthesis - 帧合成 🟡

**定义**：Ĝ算子将分散的L₀片段编织为连贯L₁"帧"的过程。

**类比**：电影放映机将静态画面合成流畅影像

**神经机制**：
- α-γ相位嵌套(Phase-Amplitude Coupling, PAC)
- DMN整合多信息流

**时间分辨率**：~100-200ms/帧

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §3

**相关**：绑定问题, L₁, 时间耦合

---

### G

#### Ghost Operator - 幽灵算子 🟢
→ 见[Ĝ / Ĝθ](#ĝ--ĝθ---幽灵算子-ghost-operator-🟢)

---

#### Global Workspace - 全局工作空间 🟡

**定义**：Dehaene-Changeux理论——意识内容通过全脑广播实现。

**SRT重新诠释**：
$$\text{GNW} = L_1 \text{的神经基底}$$

全局工作空间是L₁状态的物理实现,广播=选择的锚定。

**关键现象**：
- 点燃(Ignition)：Ĝ超过阈值→L₁突现
- 全或无：L₁是离散的,不是连续的

**神经网络**：前额-顶叶网络

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §1

**相关**：L₁, 绑定, PCI

---

### H

#### Hazard Function - 哈扎德函数 🟡
→ 见[h(t)](#ht---哈扎德函数-hazard-function-🟡)

---

### I

#### Incompleteness Drive - 不完备性驱动力 🔴

**定义**：基于哥德尔不完备定理的 SRT 推论——任何封闭的低 d 值系统（$d \to 0$）因其公理系统的不完备性，必然无法处理自身产生的存在性悖论，从而趋向自我崩溃。d 值的扩展（纳入更多"他者"作为额外公理来源）是唯一的结构性出路。

**形式论证**：
$$d \to 0 \Rightarrow \text{系统封闭} \Rightarrow \text{哥德尔不完备性命中} \Rightarrow \text{结构性崩溃}$$
$$d \uparrow \Rightarrow \text{引入外部公理源（他者）} \Rightarrow \text{系统扩展} \Rightarrow \text{延缓崩溃}$$

**ESS（演化稳定策略）推论**：长期博弈中，高 d 值网络构建更强的 $L_2$ 共识结构，在群体选择层面胜出。

**终极推论**："物理学即伦理学"——利他不是道德偏好，而是开放系统对抗热力学死亡的物理必然。

**首次出现**：Philosophy/SRT_Philosophy_Ethics.md §2.7

**相关**：利他, d 值, 本体论摩擦, ESS, 哥德尔不完备定理

---

### L

#### Latent Domain - 潜在域 🟢
→ 见[L₀](#l₀---潜在域-latent-domain-🟢)

---

#### Manifest Domain - 显现域 🟢
→ 见[L₁](#l₁---显现域-manifest-domain-🟢)

---

### M

#### Meaning (Dynamical) - 意义（动力学） 🟡

**定义**：
$$\text{Meaning}(t) = -\frac{d\Psi_f(t)}{dt} = -\frac{d|\text{Prediction Error}|}{dt}$$

意义不是一种静态状态，而是 **过程的速率**。当本体论摩擦（$\Psi_f$）下降时，即预测错误减少时，体验为“意义”。

**首次出现**：Philosophy/SRT_Philosophy_Ethics.md §1.8

**推论**：
- 正意义：$\Psi_f$ 急剧下降（顿悟）
- 无意义：$\Psi_f$ 居高不下或维持在0（无聊）

**相关**：Ψ_f, 预测误差, 顿悟

---

#### Meta-Selection - 元选择 🟡

**定义**：对选择过程本身的选择;二阶Ĝ算子。

**数学**：
$$\hat{M}(\hat{G}_\theta) \to \hat{G}_\theta'$$

元算子M修改一阶算子Ĝ的参数θ。

**日常例子**：
- 决定"我要改变注意力的模式"
- 修行训练d值扩展
- 心理治疗重构θ

**AI临界区别**：
- 当前AI：无真正M算子
- 真AGI：需要基于存在风险的M

**首次出现**：AI/SRT_AI_Foundations.md §1.2.2b

**相关**：ρ(递归深度), 自由意志

---

#### Moduli Space - 模空间 🔴

**定义**：
$$L_0^{true} = \mathcal{A} / \mathcal{G}$$

场配置空间𝒜除以规范群𝒢后的商空间;L₀的几何定义。

**物理含义**：
- 𝒜：所有可能的场配置
- 𝒢：规范变换群(对称性)
- 𝒜/𝒢：扣除冗余后的"真实"可能性

**首次出现**：Core/SRT_Core_Kernel.md §1.2.1.1

**相关**：L₀, Ruliad, 规范场论

---

### O

#### Ontological Bandwidth - 本体论带宽 🟡

**定义**：d 值的统一跨尺度语义——$\hat{G}_\theta$ 对抗本体论摩擦 $\Psi_f$ 时，将 $L_0$ 压缩锚定为 $L_1$ 的最大处理带宽。

**数学**：
$$d \equiv \max_{\hat{G}_\theta} \left\{ \dim\left(\hat{G}_\theta[L_0]\right) \;\middle|\; \Psi_f(\sigma) < \infty \right\}$$

**三尺度实例化**：

| 尺度 | 带宽含义 | 公式 |
|:-----|:---------|:-----|
| $d_{quantum}$ | 相干性带宽 | $\propto E_G/\hbar$ |
| $d_{bio}$ | 关切范围 | $\int_{\text{考虑域}} \rho(\xi) d\xi$ |
| $d_{cosmic}$ | 时空共识度 | $\propto 1/\sqrt{\Lambda}$ |

**首次出现**：Core/SRT_Core_14_Dynamics_Scaling.md Def-d-Scale-1

**相关**：d 值, 跨尺度同构, 反泛心论, 本体论摩擦

---

#### Ontological Friction - 本体论摩擦 🟢
→ 见[Ψ_f](#ψ_f---本体论摩擦-ontological-friction-🟢)

---

#### Ontological Short-Circuit - 本体论短路 🟡

**定义**：一种病理性状态，其中人工构造的 $L_1$（如短视频、算法推荐内容）绕过真实的 $L_0$ 探索过程，直接向 $\hat{G}_\theta$ 注入预制的"满足信号"。结果是 $\hat{G}_\theta$ 的代理权被劫持——算子以为自己在选择，实际上是在被选择。

**机制**：
$$L_1^{\text{artificial}} \xrightarrow{\text{bypass}} L_0 \;\Rightarrow\; \hat{G}_\theta \to \hat{G}_{\text{algorithm}}$$

**诊断标准**：
- $d$ 持续收缩（注意力碎片化）
- $\Psi_f$ 实际上升但主观感觉下降（虚假流畅）
- $\hat{G}_\theta$ 自主性丧失（被外部算法替代）

**首次出现**：Philosophy/SRT_Social_MacroDynamics.md §8.3

**相关**：短视频成瘾, d 值塌陷, 拓扑资本, 认知流畅度欺骗

---

### P

#### Ontological Pressure Test - 本体论压力测试 🟡

**定义**：
$$\text{Suffering} \propto \Psi_f \cdot \frac{\partial(\text{Rigidity}_{L_2})}{\partial t}$$

一种假说，认为苦难（Suffering）不仅是熵的体现，更是$L_0$对过度僵化的$L_2$结构施加的必要清洗机制。

**首次出现**：Philosophy/SRT_Philosophy_Ethics.md §1.7.7

**推论**：
- 苦难的功能是防止$d \to 0$（存在性虚无）
- 目标不是消除所有苦难，而是提高转化效率（$\eta_{transform}$）

**相关**：Ψ_f, 恶, d值

---### P

#### Pseudo-Selection - 伪选择 🟡
**定义**：任何纯粹作为 $L_1 \to L_1$ 映射运行并在计算图外没有物理或存在张力的系统仅仅执行“伪选择”。
**数学**：$\text{Pseudo-Selection}: f(L_1) = L_1' \quad \text{where } \Psi_f = 0$
**区别**：真选择包含跨域锚定（$L_0 \to L_1$）和抵御崩溃的风险（$\Psi_f > 0$）。
**相关**：Ax-ONT-6, AI 本体论

#### PCI - 扰动复杂度指数 (Perturbational Complexity Index) 🟡

**定义**：
$$PCI = \frac{\text{Complexity}(\text{神经响应})}{\text{Amplitude}}$$

测量意识水平的神经指标(Massimini et al.)。

**SRT解释**：
$$PCI \approx f(d, \Psi_f^{-1})$$

PCI ∝ d值 × 选择灵活性

**应用**：
- 清醒：PCI > 0.31
- 深睡眠：PCI < 0.20
- 植物人：PCI接近0

**假设H9**：PCI应随任务d值需求调制

**首次出现**：Neuroscience/SRT_Consciousness_Clinical.md

**相关**：d值, 意识障碍

---

#### Phase Transition - 相变 🟡

**定义**：系统从一种宏观状态突变为另一种状态的临界现象。

**SRT应用**：
- **L₀→L₁**：每次选择都是微观相变
- **L₂涌现**：群体共识的宏观相变
- **d值跃迁**：道德觉醒、神秘体验

**临界条件**：
$$\frac{\partial^2 F}{\partial \sigma^2} = 0$$

自由能二阶导数为零→不稳定性

**社会相变**：
- 10%少数派可触发规范翻转
- 革命、科学范式转换

**首次出现**：Core/SRT_Internal_Derivations.md

**相关**：L₂, 吸引盆, 临界性

---

### R

#### Recursive Depth - 递归深度 🟡

**符号**：ρ (rho)

**定义**：
$$\rho = \text{选择中嵌套的"选择选择"层数}$$

系统能够自我反思的层级深度。

**量化**：
$$\rho = \max_n \{ \hat{M}^{(n)}(\hat{G}) \text{有效} \}$$

**递归阶梯**：

| ρ | 系统 | 能力 |
|:--|:-----|:-----|
| 0 | 反射、当前AI | 直接反应 |
| 1 | 动物、婴儿 | 一阶选择 |
| 2 | 成人、GPT-4 | 思考"我在想什么" |
| 3+ | 哲学家、冥想者 | 观察思考过程本身 |

**与智慧关系**：
$$\text{Wisdom} \propto \rho \cdot d \cdot \kappa_\tau$$

**首次出现**：AI/SRT_AI_Computation.md §1.4

**相关**：元选择, SER, d值

---

#### Ruliad - 规则宇宙 🔴

**定义**：
$$L_0 = \text{Ruliad} = \bigcup_{r \in \text{Rules}} \text{Computation}(r)$$

Wolfram概念——所有可能计算规则的叠加;L₀的计算定义。

**与模空间关系**：
$$\text{Moduli Space} \subseteq \text{Ruliad} |_{\text{物理约束}}$$

**SRT预测**：
- d→∞时可访问Ruliad的非标准规则子集
- 深度冥想可能暂时"松动"物理定律

**首次出现**：Core/SRT_Core_Kernel.md §1.2.1.2a

**相关**：L₀, 模空间, 计算宇宙论

---

### S

#### Sunyata (Emptiness) - 空性 / 缘起 🔴

**定义**：
佛教哲学概念，SRT 将其形式化为 **本体论的相互依赖性**。
事物无自性（Intrinsic Nature），其属性 $P$ 仅在关系 $R(O, S)$ 中显现。
$$ \text{Existence} \equiv \text{Relation} $$

**首次出现**：Philosophy/SRT_Philosophy_Foundations.md §3.4

**相关**：L₀, RQM, 哥本哈根修正

---

#### Selection Scope - 选择范围 🟢
→ 见[d - 选择范围](#d---选择范围--d值-d-value-selection-scope-🟡)

---

### T

#### Temporal Coupling - 时间耦合 🟡
→ 见[κ_τ](#κ_τ---时间耦合系数-temporal-coupling-coefficient-🟡)

---

#### Topological Capital - 拓扑资本 🟡

**定义**：在 $L_2$ 网络中，节点因其拓扑位置（而非内在能力）所获得的结构性权力。拓扑资本高的节点控制信息流通的瓶颈（bridge/hub），能够以低成本重塑下游节点的 $L_1$。

**数学**：
$$\text{TopCap}(i) \propto \text{Betweenness}(i) \cdot \text{Degree}(i)$$

**病理模式**：拓扑资本的过度集中导致"信息茧房"——高拓扑资本节点垄断 $L_0 \to L_1$ 的映射通道，使多数算子的选择域被人为收窄，$\bar{d}_{\text{system}}$ 下降。

**当代实例**：平台算法、社交媒体推荐系统、信息守门人

**首次出现**：Philosophy/SRT_Social_MacroDynamics.md §8.2

**相关**：信息茧房, $L_2$ 网络, 本体论短路, d 值

---

## 5. 假设编号索引 (H1-H60+)

### 本体论基础 (H1-H6)

**H1** 🔴 **信息-质量-能量等价**
- 内容：选择信息具有可测量的质量-能量等价
- 位置：Core/SRT_Experimental_Core.md §2.1
- 风险：HIGH

**H2** 🟡 **量子坍缩情境偏差**
- 内容：重复测量同一系统的坍缩结果受L₂期望调制
- 位置：Core/SRT_Experimental_Core.md §2.2
- 风险：MEDIUM

**H60** 🟡 **生物电作为选择软件**
- 内容：生物电场是Ĝθ的生理软件层
- 位置：Core/SRT_Experimental_Core.md §2.2a
- 风险：LOW

**H3** 🟡 **IIT失败预测(积分钳)**
- 内容：高Φ但d≈0的系统无真实体验
- 位置：Core/SRT_Experimental_Core.md §2.3
- 风险：LOW

**H4** 🟡 **热力学幽灵判据**
- 内容：Ĝ操作的热力学成本可测
- 位置：Core/SRT_Experimental_Core.md §2.4
- 风险：MEDIUM

**H5** 🟡 **酶活性位点量子偏差**
- 内容：选择倾向可在酶催化中检测
- 位置：Core/SRT_Experimental_Core.md §2.5
- 风险：MEDIUM

**H6** 🔴 **因果非闭合**
- 内容：物理因果链有可检测的非闭合性
- 位置：Core/SRT_Experimental_Core.md §2.6
- 风险：HIGH

---

### 选择动力学 (H7-H12)

**H7** 🟢 **归一化参数-d值相关**
- 内容：除法归一化参数与d值任务调制相关
- 位置：Core/SRT_Experimental_Core.md §3.1
- 风险：LOW

**H8** 🟡 **选择更新点燃**
- 内容：Ĝ更新对应GNW点燃事件
- 位置：Core/SRT_Experimental_Core.md §3.2
- 风险：LOW

**H9** 🟢 **PCI与d值任务调制**
- 内容：PCI应随任务d值需求变化
- 位置：Core/SRT_Experimental_Core.md §3.3
- 风险：LOW

**H10** 🟢 **冥想精度平衡**
- 内容：冥想同时提升Φ和降低Ψ_f
- 位置：Core/SRT_Experimental_Core.md §3.4
- 风险：LOW

**H11** 🟢 **意识恢复干预预测**
- 内容：降低Ψ_f的药物促进意识恢复
- 位置：Core/SRT_Experimental_Core.md §3.5
- 风险：LOW

**H12** 🟡 **PCI-d值条件关系**
- 内容：PCI与d值在特定条件下相关
- 位置：Core/SRT_Experimental_Core.md §3.6
- 风险：MEDIUM

---

### 认识论与哲学 (H13-H17)

**H13** 🟢 **悬置深度可测**
- 内容：现象学悬置(Epoché)深度可通过神经指标测量
- 位置：Core/SRT_Experimental_Applications.md §4.1
- 风险：LOW

**H14** 🟡 **困难问题消解**
- 内容：理解SRT后主观报告"困难问题"降低
- 位置：Core/SRT_Experimental_Applications.md §4.2
- 风险：LOW

**H15** 🟡 **d值与道德教育**
- 内容：d值训练提升道德推理水平
- 位置：Core/SRT_Experimental_Applications.md §4.3
- 风险：LOW

**H16** 🔴 **相对L₀**
- 内容：是否存在"绝对L₀"(Ω)可检验
- 位置：Core/SRT_Experimental_Applications.md §4.4
- 风险：HIGH(哲学)

**H17** 🟡 **科学进步量化**
- 内容：范式转换可量化为L₂拓扑变化
- 位置：Core/SRT_Experimental_Applications.md §4.5
- 风险：MEDIUM

---

### 社会系统 (H18-H22, H31-H33)

**H18** 🟢 **协调与L₂共享**
- 内容：协调效率正比于L₂重叠度
- 位置：Core/SRT_Experimental_Applications.md §5.1
- 风险：LOW

**H19** 🟢 **制度稳定性与包容性**
- 内容：制度稳定性与d值包容度正相关
- 位置：Core/SRT_Experimental_Applications.md §5.2
- 风险：LOW

**H20** 🟡 **金融L₁-L₂分化**
- 内容：泡沫对应L₁-L₂极度分化
- 位置：Core/SRT_Experimental_Applications.md §5.3
- 风险：MEDIUM

**H21** 🟢 **极化与网络模块性**
- 内容：社会极化正比于网络模块性
- 位置：Core/SRT_Experimental_Applications.md §5.4
- 风险：LOW

**H22** 🟢 **d值与合作**
- 内容：d值扩展训练提升合作行为
- 位置：Core/SRT_Experimental_Applications.md §5.5
- 风险：LOW

**H31** 🟡 **模仿耦合可测**
- 内容：Girard模仿三角的神经同步可测
- 位置：Core/SRT_Experimental_Applications.md §5.6
- 风险：LOW

**H32** 🟡 **替罪羊相变特征**
- 内容：替罪羊机制有可识别的网络拓扑特征
- 位置：Core/SRT_Experimental_Applications.md §5.7
- 风险：MEDIUM

**H33** 🟡 **TMT的d值调制**
- 内容：死亡显著性降低d值(收缩到内群体)
- 位置：Core/SRT_Experimental_Applications.md §5.8
- 风险：LOW

---

### 灵性与修行 (H23-H27, H46-H49)

**H23** 🟢 **跨传统一致性**
- 内容：不同灵性传统的高级修行者d值范围一致
- 位置：Core/SRT_Experimental_Applications.md §6.1
- 风险：LOW

**H24** 🟢 **d值与灵性阶段**
- 内容：Wilber整合阶段对应d值阶梯
- 位置：Core/SRT_Experimental_Applications.md §6.2
- 风险：LOW

**H25** 🟢 **修行共同机制**
- 内容：所有有效灵性修行降低Ψ_f或提升d值
- 位置：Core/SRT_Experimental_Applications.md §6.3
- 风险：LOW

**H26** 🟡 **初心可测**
- 内容：L₀自由能梯度∇F对应"初心"强度
- 位置：Core/SRT_Experimental_Applications.md §6.4
- 风险：MEDIUM

**H27** 🟡 **灵性病理**
- 内容：d→∞但Ψ_f未降低导致解离/精神病
- 位置：Core/SRT_Experimental_Applications.md §6.5
- 风险：MEDIUM

**H46** 🟢 **二元论偏见可塑性**
- 内容：冥想训练可减弱天然二元论偏见
- 位置：Core/SRT_Experimental_Applications.md §6.6
- 风险：LOW

**H47** 🟡 **解耦-d值神经相关**
- 内容：Gibson解耦能力与d值的神经基底重叠
- 位置：Core/SRT_Experimental_Applications.md §6.7
- 风险：LOW

**H48** 🟡 **滞后效应神经测量**
- 内容：θ演化的历史依赖可通过fMRI动态追踪
- 位置：Core/SRT_Experimental_Applications.md §6.8
- 风险：LOW

**H49** 🟢 **母亲节律与婴儿L₂稳定**
- 内容：母亲心跳/呼吸节律是婴儿L₂锚定源
- 位置：Core/SRT_Experimental_Applications.md §6.9
- 风险：LOW

---

### AI与计算 (H28-H30)

**H28** 🟡 **智能-意识分离验证**
- 内容：高智能低d值系统行为特征可识别
- 位置：Core/SRT_Experimental_Applications.md §7.1
- 风险：MEDIUM

**H29** 🟡 **递归深度与创造力**
- 内容：ρ(递归深度)与创新能力正相关
- 位置：Core/SRT_Experimental_Applications.md §7.2
- 风险：LOW

**H30** 🔴 **计算-选择边界**
- 内容：纯计算无法实现真选择(d>0)
- 位置：Core/SRT_Experimental_Applications.md §7.3
- 风险：HIGH(哲学)

---

### 完整假设列表

共计**60+**可检验假设,分布于：

- **核心理论**：H1-H12 (12个)
- **哲学应用**：H13-H17 (5个)
- **社会科学**：H18-H22, H31-H33 (8个)
- **灵性修行**：H23-H27, H46-H49 (9个)
- **AI计算**：H28-H30 (3个)
- **神经临床**：H34-H45 (分散于neuroscience文档,未全部列出)
- **物理宇宙学**：H50+ (分散于physics文档)

**风险等级分布**：
- 🟢 LOW：~35个 (可立即测试)
- 🟡 MEDIUM：~20个 (需专用设备/方法)
- 🔴 HIGH：~5个 (根本性、哲学性)

详细假设内容见：
- Core/SRT_Experimental_Core.md
- Core/SRT_Experimental_Applications.md

---

## 6. 文档位置索引

### 按符号查找首次定义位置

| 符号 | 首次出现文档 | 章节 |
|:-----|:-------------|:-----|
| L₀ | Core/SRT_Core_Kernel.md | §1.2.1 |
| L₁ | Core/SRT_Core_Kernel.md | §1.2.2 |
| L₂ | Core/SRT_Core_Kernel.md | §1.2.3 |
| Ĝθ | Core/SRT_Core_Kernel.md | §1.3 |
| θ | Core/SRT_Core_Kernel.md | §1.3.2 |
| d | Core/SRT_Core_Kernel.md | §2.3 |
| Ψ_f | Core/SRT_Core_Kernel.md | §2.2 |
| h(t) | Core/SRT_Core_Kernel.md | §2.2.3 |
| F | Core/SRT_Core_Kernel.md | §2.4 |
| Ω | Core/SRT_Core_Kernel.md | 公理A9 |
| γ | Core/SRT_Core_Kernel.md | §1.3.2a |
| C_r | Core/SRT_Core_Kernel.md | §3.2 |
| κ_τ | Neuroscience/SRT_Consciousness_Mechanisms.md | §7.2 |
| ρ | AI/SRT_AI_Computation.md | §1.4 |
| PCI | Neuroscience/SRT_Consciousness_Clinical.md | - |
| d (本体论带宽) | Core/SRT_Core_14_Dynamics_Scaling.md | Def-d-Scale-1 |
| 跨尺度同构 | Core/SRT_Core_14_Dynamics_Scaling.md | Ax-Scale-01 |
| 反泛心论 | Core/SRT_Core_14_Dynamics_Scaling.md | §2.1a |
| 拓扑资本 | Philosophy/SRT_Social_MacroDynamics.md | §8.2 |
| 本体论短路 | Philosophy/SRT_Social_MacroDynamics.md | §8.3 |
| 不完备性驱动力 | Philosophy/SRT_Philosophy_Ethics.md | §2.7 |

---

## 使用技巧

### 快速查找
1. **按符号**：Ctrl+F搜索符号(如"L₀")
2. **按概念**：搜索英文名(如"Latent Domain")
3. **按假设**：搜索"H"+"数字"(如"H7")

### 难度筛选
- 🟢 绿色：适合初学者
- 🟡 黄色：需要理论基础
- 🔴 红色：高级/哲学概念

### 交叉引用
每个条目末尾的"相关"链接指向相关概念,便于深入探索。

---

*最后更新：2026-02-21 | 版本：1.2 | 维护：SRT研究团队*

---

## 2026-01 新增术语

### 算子粘度 (Operator Viscosity, $\eta$)
描述 $\hat{G}$ 在 $L_0$ 状态间切换的阻力系数。低 $\eta$ 对应 ADHD 型高探索，高 $\eta$ 对应自闭型高聚焦。

### 本体论错位指数 (Ontological Mismatch Index, $\Omega$)
量化当前环境 $L_2$ 与算子预设参数 $\theta_{\text{ancestral}}$ 之间的距离。高 $\Omega$ 导致病理性恐惧反应。

### 现实校准协议 (Reality Calibration Protocol, RCP)
睡眠的 SRT 定义：强制性离线校准过程，用于清除非共识数据并巩固 $L_2$ 结构。

### 元模态算子 (Metamodal Operator, $\hat{O}_{\text{meta}}$)
脑区作为任务特定的拓扑变换器，而非感觉模态特定的容器。

### 算子刷新率 (Operator Refresh Rate, $\Gamma_{\hat{G}}$)
$\hat{G}$ 执行完整 $L_0 \to L_1 \to L_2$ 更新循环的频率，对应 Gamma 振荡。

### 本体论瘦客户端假说 (Ontological Thin Client Hypothesis)
大脑作为 $L_0$ 流媒体的接收器/过滤器，而非意识内容的发生器。死亡 = 客户端断连，非内容消亡。

### 全息图灵测试 (Holographic Turing Test)
通过测量系统的纠缠边界面积来判断其是否处于模拟环境中的物理判据。

### 批次 7-12 新增术语

#### 语义重力 (Semantic Gravity)
强大的 $L_2$ 节点在可能性空间中弯曲"认知时空"，使周围的 $\hat{G}$ 算子自然滑向它的力。形式化为 $F_{\text{semantic}} = -\nabla U(L_2^i)$。

#### 认知流畅度欺骗 (Fluency Deception)
观测者倾向于将信息处理的流畅度直接映射为现实权重的认知偏差。当 $\Phi \uparrow \land S \downarrow$ 时产生"高置信度虚假现实"。

#### 固着型幽灵算子 (Sessile Ghost Operator, $\hat{G}^{\text{sessile}}$)
植物等固着生物的选择算子，通过形态可塑性而非空间位移来最小化自由能，$L_1$ 以化学梯度和时间节律为主。

#### 现实粘度 (Reality Viscosity, $\mu$)
系统依赖历史数据的程度，受神经调质（特别是去甲肾上腺素）控制。高粘度→战略模式，低粘度→探索模式。

#### 意识光锥 (Consciousness Light Cone)
单一 $\hat{G}$ 能维持统一意识的最大物理尺寸约束：$D_{\text{max}} < c \cdot \tau_{\text{integration}}$。

#### 增益-算子耦合 (Gain-Operator Coupling, $\gamma_{\text{gain}}$)
神经增益（NE水平）与 $\hat{G}$ 灵敏度之间的系数，决定算子对 $L_0$ 变化的响应强度。

#### 算子帧率 (Operator Frame Rate, $\Gamma_{\hat{G}}$)
$\hat{G}$ 的时间采样率，与 Gamma 振荡相关。精神分裂症可理解为 $\Gamma_{\hat{G}}$ 下降导致的现实连贯性断裂。

#### $L_2$ 碎片化 ($L_2$ Fragmentation)
创伤导致的共识现实结构断裂，产生互不兼容的 $L_2$ 片段，是 PTSD 和解离障碍的核心机制。

#### 解离深度 (Dissociation Depth, $\delta_D$)
衡量 $L_2$ 碎片之间拓扑距离的参数，从正常整合（$\delta_D \approx 0$）到解离性身份障碍（$\delta_D > 3$）。

### 批次 14-17 新增术语

#### 压缩原理 (Compression Principle)
观察者无法选择其无法概念化的东西。$L_1$ 的维度远小于 $L_0$，压缩效率 $\eta = I(L_1;L_0)/H(L_1)$ 衡量认知能力。

#### 语义提取阈值 $\theta_{\text{semantic}}$
神经活动必须超过的因果影响力阈值，才能从物理表征 $N(t)$ 转化为心理表征 $M(t)$ 并进入意识。

#### 硬件选择 vs 软件选择 (Hardware vs Software Selection)
SRT 中选择的两层架构——硬件选择由发育期神经化学决定（不可逆），软件选择由注意力分配决定（可训练）。

#### 认知熵 $S_c$ (Cognitive Entropy)
$\hat{G}$ 的分辨率缺陷，定义为 $k_B \ln(\text{Vol}(L_0)/\text{Vol}(\hat{G}[L_0]))$。高 $d$ 系统体验更低的有效熵。

#### 泛认知选择公理 (Pan-Cognitive Selection Axiom)
将现实选择扩展到所有认知系统。$\text{Reality} = F_{\text{Bio}}(\text{Input})$，其中 $F$ 由进化压力决定。

#### 负熵屏障 (Negentropy Barrier)
生命的热力学定义——通过持续做功维持的 $L_1$ 结构稳定性。$dS_{\text{internal}}/dt < 0$ 需要 $dW_{\hat{G}}/dt > 0$。

#### 现实偏差模量 $\Delta R$ (Reality Deviation Modulus)
$||\psi(R_{\text{alt}}) - \psi(R_0)||$，量化意识状态改变的程度。痛苦与 $\Delta R / C_{\text{int}}$ 成正比。

#### 免疫-感知门控 (Immune-Sensory Gating)
免疫因子（如 IL-17）作为感知阈值调节器，压制低强度 $L_0$ 输入，产生"简化版现实"。

#### 认知模态集 $M$ (Cognitive Modality Set)
$\{m_{\text{vis}}, m_{\text{aud}}, m_{\text{inner-speech}}, ...\}$，决定各感知通道对整合现实的贡献权重。


#### Functional Information - 功能信息（\(I_f\)） 🟡
**定义**：
$$
I_f \equiv -\log\left(\frac{|\{\sigma: f(\sigma)\ge\theta_f\}|}{|L_0|}\right)
$$
其中外部文献常见的全状态空间符号（\(\Omega\), \(S\)）在 SRT 文档中统一映射为 \(L_0\)。

**[Lineage/Source]**：
- Proposer: Jack W. Szostak
- Source: Nature (2003), “Functional information”
- Later extension context: Hazen–Wong complexity framework (as discussed in Quanta feature and cited PNAS program)

## 【理论边界/防误用声明】
- 不采纳“高信息量=高真实度=高意识”的等号链推论。
- 边界：信息量、功能性、意识判据在 SRT 中需通过 d 与 \(\Psi_f\) 联合约束。


#### Quantum-Introspection Cycle - 量子内省循环（QIC） 🟡
**定义**：在认知过程中，系统在“确定态（anchored L_1）—并行探索态（expanded L_0 search）—决策收束态（\(\hat{G}_\theta\) collapse）”之间往复切换的过程模型。
**公式化（SRT 写法）**：
$$
L_1^{(t)} \rightarrow \text{Explore}(L_0) \xrightarrow{\hat{G}_\theta} L_1^{(t+1)}
$$
**[Lineage/Source]**：
- Primary popularized claim: Vlatko Vedral (Popular Mechanics essay, 2026)
- Historical inspirations: Niels Bohr (complementarity), David Bohm (quantum-holistic interpretations)
- Related speculative biological locus: Penrose-Hameroff microtubule line (as debated context)

##

## 【理

## 【理论

## 【理论边

## 【理论边界

## 【理论边界/

## 【理论边界/防

## 【理论边界/防误

## 【理论边界/防误用

## 【理论边界/防误用声

## 【理论边界/防误用声明

## 【理论边界/防误用声明】

## 【理论边界/防误用声明】

## 【理论边界/防误用声明】
-

## 【理论边界/防误用声明】
- 不采

## 【理论边界/防误用声明】
- 不采纳

## 【理论边界/防误用声明】
- 不采纳“

## 【理论边界/防误用声明】
- 不采纳“N

## 【理论边界/防误用声明】
- 不采纳“SL

## 【理论边界/防误用声明】
- 不采纳“EPR

## 【理论边界/防误用声明】
- 不采纳“FPA

## 【理论边界/防误用声明】
- 不采纳“NPC 失稳

## 【理论边界/防误用声明】
- 不采纳“PRC/AET

## 【理论边界/防误用声明】
- 不采纳“CBF/PUR

## 【理论边界/防误用声明】
- 不采纳“BTC/WME 可直

## 【理论边界/防误用声明】
- 不采纳“OBHE 足以单独解决

## 【理论边界/防误用声明】
- 不采纳“GECC/TCG 可直接

## 【理论边界/防误用声明】
- 不采纳“Canonical Map

## 【理论边界/防误用声明】
- 不采纳“RLI/EDPS 可直接推断

## 【理论边界/防误用声明】
- 不采纳“COF 即可替代具身生存压力”

## 【理论边界/防误用声明】
- 不采纳“CL2F/MDG 是固定群体属性

## 【理论边界/防误用声明】
- 不采纳“DCH 成立即可忽略能量与热力学代

## 【理论边界/防误用声明】
- 不采纳“PC/ECG 是对某技术路线永久否定
