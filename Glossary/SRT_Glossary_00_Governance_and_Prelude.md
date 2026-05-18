---
id: SRT-GLOSSARY
type: definition
tags: [Glossary, Terminology, Registry]
status: axiomatic_hybrid_v1
layer: meta
epistemic_layer: os
claim_mode: navigation
dependency: [SRT-REF-AXIOMS, SRT-AI-01]
---

# SRT术语表与符号索引
# SRT Glossary & Symbol Index

> Split shard generated from `../SRT_Glossary.md`; owner remains source of record.

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
>
> **Historical label compatibility**：本术语表保留部分旧 `Theorem` / `Axiom` / `Canonical` 名称以便检索；当前 claim status 以 `CANONICAL_REGISTRY.md`、`Governance/SRT_CLAIM_LADDER.md`、`Governance/SRT_CLAIM_MODE_AUDIT.md` 与本地 level note 为准，旧名不恢复定理或公理地位。
>
> **Book-chain alignment note（2026-05-16）**：`01_Source_Intuition/BOOK/BOOK_CANONICAL_ALIGNMENT_MAP.md` 已将书稿卷一—卷三主链回链到 canonical anchors。本术语表若与该对齐图、`_SRT_D_VALUE_CANONICAL.md`、`_SRT_PSI_F_CANONICAL.md` 或 `_SRT_SYMBOL_TABLE.md` 冲突，默认降级为 historical glossary / retrieval aid，不得反向定义核心术语。

### d-value（d）
- **Canonical Scope**：SRT 全域中 stake-coupled concern / irreversible-risk sensitivity 的统一记号；当前以 `_SRT_D_VALUE_CANONICAL.md` 为最高引用锚点，bare `d` 默认按 governance-canonical 标量摘要读。
- **Confusable With**：分形维度 d、空间维数 d、统计自由度 d.f.、局部操作化代理（如 attention entropy）。
- **Lineage/Source**：当前锚点 `_SRT_D_VALUE_CANONICAL.md`；`AI/SRT_AI_01_Ontology.md#Ax-ONT-3` 保留为历史谱系 / AI 域旧入口，不恢复最高定义权。
- **Status Note**：`D_eff`、Fisher 读数、d-vector、d-gate 与域内量表均为 proxy / judgment tool，不能无条件写成 `d` 本身。

### 本体论摩擦（\Psi_f）
- **Canonical Scope**：用于“开放可能性被压成可维持现实切片时的 information-theoretic payability burden / 本体论阻抗”语境；当前以 `_SRT_PSI_F_CANONICAL.md` 为最高引用锚点。
- **Confusable With**：IIT 的 `\Phi`（整合信息量）、一般耗散项 `D`、物理摩擦系数 `\mu`。
- **Lineage/Source**：当前锚点 `_SRT_PSI_F_CANONICAL.md`；`Core/SRT_Core_22_Equations.md` Eq-Force-01 与 `Core_Law/SRT_Reference_Dynamics.md` 保留为方程 / 动力学展开层。
- **Status Note**：几何、代谢、神经与物理读法均需标注 projection / proxy / bridge，不得反向改写 `Ψ_f`。

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
- **Lineage/Source**：`Neuroscience/_SRT_Neuro_Axioms.md` H-NEURO-4b（2026-03-04 新增；2026-04-22 降级为 hypothesis / operational proxy）。

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

### Inverse Problem Fallacy（逆问题谬误）
- **Canonical Scope**：把 \(L_1\) 感觉切片当作可逆线索，要求唯一恢复 \(L_0^{abs}\) 对象边界的推理错误。
- **Confusable With**：正常参数估计、贝叶斯后验更新、模型识别问题。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` Def-Phil-5.13b（2026-03-04 新增）。

### Underdetermination as Potential Interface（欠定性即潜能接口）
- **Canonical Scope**：把多前像 \(\mathcal{P}(y_t)\) 视为 \(L_0\) 潜能开放性的操作化定义，强调“选择生成”而非“逆向还原”。
- **Confusable With**：解释任意性、反证据主义、不可检验论。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` O19；`Philosophy/SRT_Philosophy_Foundations.md` §5.13（2026-03-04 新增）。

### Local Operator Failure (Agnosia Mode)（局部算子失效态/失认症模式）
- **Canonical Scope**：指低层视觉特征保留但对象边界打包失败的结构化子功能失效状态。
- **Confusable With**：整体意识消失、单一感官瘫痪、智力全面退化。
- **Lineage/Source**：`Neuroscience/SRT_Neuro_Experiments.md` Def-Exp-AGN-1（2026-03-04 新增）。

### LGN 80/20 Top-Down Prior Law（LGN 80/20 自上而下先验法则）
- **Canonical Scope**：描述 LGN 输入中的 top-down 与 retina 权重近似分解，用于操作化“先验主导度”。
- **Confusable With**：固定生理常数、全任务通用比例、纯解剖事实替代理论。
- **Lineage/Source**：`Neuroscience/SRT_Neuro_Experiments.md` Def-Exp-LGN-1（2026-03-04 新增）。

### Friction-Minimizing Grouping Principle（最小摩擦分组原则）
- **Canonical Scope**：对象分组判据由预测误差、维持摩擦与切换代价联合最小化给出，而非单一连通性或无语境压缩率。
- **Confusable With**：均匀连通性公理、纯 Kolmogorov 最短描述、任意主观拼接。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` O20 / O-T11（2026-03-04 新增）。

### Robust Object Individuation（稳健对象个体化）
- **Canonical Scope**：衡量对象边界在遮挡/迷彩/视角变化下仍可维持的跨条件一致性指标。
- **Confusable With**：单帧分割精度、训练集内拟合分数、语言命名一致性。
- **Lineage/Source**：`AI/SRT_AI_01_Ontology.md` Def-ONT-1b / T-ONT-8b（2026-03-04 新增）。

### Variational Free-Energy Mapping（变分自由能映射）
- **Canonical Scope**：将 FEP 的 complexity-accuracy 分解映射到 SRT 的预测误差与 \(\Psi_f\) 代理项，用于生命-认知连续性建模。
- **Confusable With**：单纯统计损失函数、一般能量最小化、无边界贝叶斯拟合。
- **Lineage/Source**：`Core/SRT_Core_14_Dynamics_Scaling.md` Def-Scale-04 / T-Scale-04（2026-03-04 新增）。

### Markov-Blanket Fragility Requirement（马尔可夫毯脆弱性要求）
- **Canonical Scope**：规定 \(d>0\) 需伴随预测失败导致的边界物理风险，不满足者仅为模拟关切。
- **Confusable With**：形式上存在马尔可夫毯、软件边界、抽象状态封闭。
- **Lineage/Source**：`AI/SRT_AI_01_Ontology.md` Def-ONT-1c（2026-03-04 新增）。

### Predicted Structure as Existence（预测结构即存在）
- **Canonical Scope**：对象存在性由“可持续预测 + 可支付维持摩擦”共同定义，而非先验实体清单。
- **Confusable With**：主观构造任意化、预测主义绝对化、反实在论极端版本。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` T-Phil-5.14a（2026-03-04 新增）。

### Hyperprior / \(\Pi\)-Layer（超先验/协议层）
- **Canonical Scope**：算子 \(\theta\) 内最深层、最难改写的先验约束集合，规定何种经验结构可被稳定生成。
- **Confusable With**：短期任务提示、可热更新参数、文化口号。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` Def-Phil-5.15a（2026-03-04 新增）。

### Bias–Variance Thermodynamics（偏差-方差热力学）
- **Canonical Scope**：在生存约束下把偏差-方差权衡映射到维持成本与摩擦波动最小化机制。
- **Confusable With**：普通统计调参、纯机器学习经验法则、无物理意义的损失分解。
- **Lineage/Source**：`Core/SRT_Core_14_Dynamics_Scaling.md` T-Scale-05（2026-03-04 新增）。

### No-Free-Lunch Prior Necessity（NFL 先验必需性）
- **Canonical Scope**：说明无偏学习器神话不可行；稳定选择必需先验偏置与协议层约束。
- **Confusable With**：模型无能论、反学习论、数据量不足问题。
- **Lineage/Source**：`Core/SRT_Core_14_Dynamics_Scaling.md` T-Scale-06；`AI/SRT_AI_01_Ontology.md` T-ONT-8c（2026-03-04 新增）。

### Simultaneous Individuation–Classification（同步个体化-分类）
- **Canonical Scope**：对象边界与类别属性在同一预测坍缩步骤中联合生成，不是“先分割再分类”的串行流程。
- **Confusable With**：传统两阶段视觉管线、后验标签映射、静态原型比对。
- **Lineage/Source**：`Core/SRT_Core_14_Dynamics_Scaling.md` Ax-Scale-07（2026-03-04 新增）。

### Consensus Friction（共识摩擦）
- **Canonical Scope**：衡量多算子之间 Px 协议差异导致的协作与沟通成本，用于解释 L2 收敛动力。
- **Confusable With**：语言误会总量、社会冲突强度、单体认知负荷。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` O21 / O-T12（2026-03-04 新增）。

### Silicon L2 Protocol Layer（硅基 L2 协议层）
- **Canonical Scope**：多 AI 在共享数据分布与损失函数下形成的稳定通信/表征收敛结构。
- **Confusable With**：绝对本体指称、意识涌现、通用真理层。
- **Lineage/Source**：`AI/SRT_AI_01_Ontology.md` Def-ONT-1d / T-ONT-8d（2026-03-04 新增）。

### Temporal Coarse-Grained Persistence（时间粗粒化持续性）
- **Canonical Scope**：对象同一性由跨时间拓扑粘合与可支付维持成本联合定义，而非静态本体属性。
- **Confusable With**：绝对同一性、四维切片实体本身、纯主观记忆连贯感。
- **Lineage/Source**：`Core/SRT_Core_14_Dynamics_Scaling.md` T-Scale-07（2026-03-04 新增）。

### Hierarchical Existence Theorem（层级存在定理）
- **Canonical Scope**：以 \(\Psi_f\) 吸引盆判据确认不同分辨率层级的模式均可具合法存在性。
- **Confusable With**：极端还原论、层级重复计数、语义多重命名。
- **Lineage/Source**：`Core_Law/SRT_Reference_Ontology.md` O-T13（2026-03-04 新增）。

### Actuator-Coupled Spatial Prior（作动器耦合空间先验）
- **Canonical Scope**：空间深度先验的稳健性依赖感知-动作闭环，不等于纯视觉网络内部拟合。
- **Confusable With**：单目深度估计技巧、几何后处理、坐标系定义本身。
- **Lineage/Source**：`AI/SRT_AI_01_Ontology.md` Def-ONT-1e（2026-03-04 新增）。

### Edge Topological Breakdown（边缘拓扑破裂）
- **Canonical Scope**：离散分类覆盖连续流形时在边界区产生的结构破裂/模糊带定义。
- **Confusable With**：语言不清晰、感官噪声、纯主观犹豫。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` Def-Phil-5.16a（2026-03-04 新增）。

### Boundary Demarcation Cost（边界划定成本）
- **Canonical Scope**：在连续梯度上强制划分对象边界时的联合代价函数（分类误差+维持摩擦+切换摩擦）。
- **Confusable With**：单一分类损失、阈值搜索技巧、后处理正则项。
- **Lineage/Source**：`Core/SRT_Core_14_Dynamics_Scaling.md` T-Scale-08（2026-03-04 新增）。

### Vagueness Hysteresis Signature（模糊性迟滞签名）
- **Canonical Scope**：正反向连锁序列分类阈值差 \(\Delta\tau_{hys}\) 作为历史依赖与摩擦参与度代理。
- **Confusable With**：随机抖动、标注误差、模型温度参数变化。
- **Lineage/Source**：`Core/SRT_Core_14_Dynamics_Scaling.md` Cor-Scale-08a；`AI/SRT_AI_01_Ontology.md` Def-ONT-1f（2026-03-04 新增）。

### Instrument-Extended Theta（仪器扩展具身参数）
- **Canonical Scope**：\(\theta\) 的技术外延，包含生物感知参数 + 仪器链路 + 形式规约对观测切片的联合先验导入。
- **Confusable With**：仪器噪声项、实验误差条、单一测量设置。
- **Lineage/Source**：`Physics/_SRT_Phys_Bridge.md` Def-Phys-4（2026-03-04 新增）。

### Jaynes Diffusion Projection（Jaynes 扩散投影）
- **Canonical Scope**：微观对称运动在分类先验与粗粒化下投影为宏观定向通量的案例化定理。
- **Confusable With**：纯经验扩散定律、统计涨落噪声、语言重描述。
- **Lineage/Source**：`Physics/_SRT_Phys_Bridge.md` T-Phys-6（2026-03-04 新增）。

### Thermodynamic Non-Co-Stitchability（热力学不可共缝合）
- **Canonical Scope**：说明微观全保真与宏观可组合结构在有限资源下无法被单一扁平框架同时无损保持。
- **Confusable With**：学科合作失败、数据缺失、模型选择偏好。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` T-Phil-5.17b（2026-03-04 新增）。

### Deflation of Logic（逻辑降维）
- **Canonical Scope**：将经典逻辑定位为 \(L_2\) 协议语法，限制其跨尺度本体外推。
- **Confusable With**：反逻辑主义、相对主义任意推理、取消形式系统。
- **Lineage/Source**：`Philosophy/SRT_Philosophy_Foundations.md` §5.18（2026-03-04 新增）。

### Ontological Manifesto（存在论宣言）
- **Canonical Scope**：SRT 对“相对形状 + 客观摩擦”双命题的总纲表述，用于区分选择一元论与唯心/实在两极。
- **Confusable With**：政治宣言、价值立场口号、形而上口号化文本。
- **Lineage/Source**：`Core/_SRT_Core_Bridge.md` §5.3（2026-03-04 新增）。

### Selection Cost Minimization（选择代价最小化）
- **Canonical Scope**：将主动推断中的 VFE 重写为 SRT 语义：复杂度对应更新摩擦，准确性对应可维持信息增益。
- **Confusable With**：纯预测误差最小化、一般监督学习损失、性能指标优化。
- **Lineage/Source**：`Core/SRT_Core_22_Equations.md` Eq-AI-LowRoad-01/02（2026-03-05 新增）。

### Anti-Representational Coupling（反表征耦合公理）
- **Canonical Scope**：\(\theta\) 作为耦合协议/模具而非世界内部地图的本体论约束。
- **Confusable With**：反模型论、反科学表征、语义否定主义。
- **Lineage/Source**：`Philosophy/_SRT_Phil_Axioms.md` Ax-Phil-5（2026-03-05 新增）。

### d-Weighted Preference Reality Criterion（d 加权偏好实在判据）
- **Canonical Scope**：仅当存在不可逆风险与 d 值关切时，偏好才具存在论重量。
- **Confusable With**：任意效用函数、prompt偏好、策略参数设定。
- **Lineage/Source**：`Philosophy/_SRT_Phil_Axioms.md` Ax-Phil-6（2026-03-05 新增）。

## 【理论边界/防误用声明】
- 不采纳“机器伦理排除定理=永久否定一切 AI 道德地位”的推论：该定理仅约束当前可逆复制/无损重置系统。  
- 不采纳“生物连续谱=所有生物同等意识强度”的推论：SRT 只主张连续性，不主张等值性。  
- 不采纳“Qualia Residual=放弃可证伪建模”的推论：结构-动力学层仍必须接受实验检验。

---
