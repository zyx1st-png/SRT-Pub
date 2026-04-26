---
id: SRT-CANONICAL-REGISTRY
type: index
tags: [Canonical, Registry, Definitions, Equations]
status: active_v1
layer: meta
claim_mode: canonical
epistemic_layer: os
dependency: [SRT-INDEX, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CROSS-DOMAIN-MATRIX, SRT-CORE-22]
---

# SRT Canonical Registry

本页用于固定 SRT 当前应优先引用的 **canonical 主干层**。
原则：
- canonical 文件优先短、稳、少歧义
- 长文负责展开、推导、接口批次与历史沉积
- split 文件负责导航，不替代 canonical 定义

## 0. 定位说明（Epistemic Note）

- `canonical` 在本仓库内表示“当前内部优先引用的稳定锚点”，**不自动等于**“外部已证实的自然定律”。
- `governance-canonical` 表示为防止全仓漂移而采用的稳定用法规则；它可以是当前主读、默认符号口径或工作代理，不自动声称已完成本体推导。
- `theory-canonical` 表示由 core 结构推出或在 core 中具有更强优先权的定义 / 命题；只有明确回链 P0/P1/P2 来源时才按此读。
- `operational proxy` 表示为了测量、比较或建模而采用的工作性读数；它可以近似 canonical 对象，但不得反向改写 canonical 对象。
- `bridge hypothesis` 表示跨域映射或解释性接口；它可以承载候选结构，但不得被下游引用成 core theorem。
- 旧文件名、旧 theorem/axiom 标签或 glossary 历史条目若仍保留，均按当前 claim ladder、claim-mode audit 与本注册表的本地说明判读；历史命名不恢复更高等级。
- 自 `2026-03-17` 起，SRT 默认按 `OS / Bridge / Lab` 三层理解；详见 `Governance/SRT_POSITIONING.md`。
- 自 `2026-04-20` 起，SRT 额外按命题级硬度 `P0-P5` 管理；详见 `Governance/SRT_CLAIM_LADDER.md`。
- 本注册表中的大多数条目默认属于 **OS** 或 **Bridge**，用于收口词汇、语法与高阶接口；真正的硬赌点应优先沉淀到实验与假说文件，而不是混在 canonical 锚点里。

## A. 核心定义层（Definitions）

### 1. d-value
- 主锚点：`_SRT_D_VALUE_CANONICAL.md`
- 说明：统一 d-value 的 governance-canonical 默认用法、域内投影、误用边界；bare `d` 默认采用标量摘要形式，向量 / 门读须显式标注；`D_eff`、Fisher 读数、d-vector 与 d-gate 均为 proxy / judgment tool，不能反向替代 `Def-d-canonical`
- 引用规则：首次出现 d-value 时优先回链本文件

### 2. Ψ_f（本体论摩擦）
- 主锚点：`_SRT_PSI_F_CANONICAL.md`
- 说明：统一 `Ψ_f` 的 v1 governance-canonical 信息论代价 / 可支付性主读、几何 / 代谢投影、可支付性条件与物理弱相容边界；几何与代谢表达是有条件 projection，不是最终唯一推导
- 引用规则：首次出现 `Ψ_f`、本体论摩擦、可支付性条件或“引力是否只是类比”时优先回链本文件

### 3. T_dir（方向透明度）与价值遮蔽
- 主锚点：`_SRT_T_DIR_CANONICAL.md`
- 说明（Part I §1-§10）：T_dir 是系统对自身选择秩序方向可读性的 v0 operational proxy / working canonical proxy；统一价值遮蔽命题、Ψ_f_actual/Ψ_f_felt 分裂、致命 L₂ 机制的治理性表述；它尚不是 theory-canonical 形式基础
- 说明（Part II §11-§16）：扩展至价值动力学底层机制——L₂ 磁带/DNA 类比（§11）、三层价值结构（§12）、价值归纳 vs 理性归纳（§13）、时空对称性感知机制（§14）、价值作为暂时吸引子而非守恒结构（§15）、吸引子上升/退化动力学（§16）；这些段落按 bridge / theory-clarifying 读，不因文件名而升级为 core theorem
- 引用规则：涉及方向透明度、意义感/虚无感的 SRT 机制解释、致命 L₂、价值遮蔽、三层价值结构、价值归纳、吸引子动力学时优先回链本文件
- 与 d-value 的关系：d 是 T_dir 的必要条件；两者独立，不互相替代

### 4. Core Axioms
- 主锚点：`Core/SRT_Core_21_Formal_Axioms.md`
- 分层正文：
  - P0 minimal axioms → `Core/SRT_Core_21_Minimal_Axioms.md`
  - P1 constitutive theorems → `Core/SRT_Core_21b_Constitutive_Theorems.md`
  - P2/P3/P4 bridge hypotheses → `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- 说明：`Core_21_Formal_Axioms.md` 现在是形式公理索引，不再承载混层正文
- 引用规则：涉及核心公理编号时，先回链索引，再按命题硬度引用对应分层文件

### 4b. Core Equations
- 主锚点：`Core/SRT_Core_22_Equations.md`
- 说明：主动力学方程、热力学与稳定性方程主入口
- 引用规则：涉及主方程、选择热力学、稳定性条件时优先回链本文件

### 4c. Core Open Tensions
- 主文件：`Core/SRT_OPEN_TENSIONS.md`
- 说明：记录当前未完全封口的 core pressure points
- 引用规则：凡涉及其中 tension，不得包装成已完成 P0/P1

### 4d. Cross-Domain Usage Matrix
- 主文件：`_SRT_CROSS_DOMAIN_MATRIX.md`
- 说明：提供 `d`、`Ψ_f`、`T_dir`、`ε` 的 v0 跨域用法矩阵；该矩阵是 governance-canonical usage layer，不新增 theory-canonical 定义
- 引用规则：跨域使用上述概念时，先检查 canonical 用法、allowed projection 与 forbidden shortcut

## B. 规范辅助层（Canonical Support）

### 5. 七命题宪法摘要层
- 文件：`Core_Law/SRT_Constitution_Seven_Theses.md`
- 角色：为 SRT 提供最短的元理论宪法摘要，用于对外解释、框架比较与自我收口
- 注意：它是顶层摘要，不替代 `Core_Law/SRT_Reference_Axioms.md`、`Core_Law/SRT_Reference_Ontology.md`、canonical 定义文件或主方程文件

### 5b. Claim Ladder
- 文件：`Governance/SRT_CLAIM_LADDER.md`
- 角色：定义 P0-P5 命题级硬度，防止 bridge / lab / companion 命题伪装成 primitive axiom 或 constitutive theorem
- 注意：它是治理机制，不新增理论命题

### 5c. Claim-Mode Audit
- 文件：`Governance/SRT_CLAIM_MODE_AUDIT.md`
- 角色：记录本轮 `T-*` / `Ax-*` / `H-*` 扫描结果、降级决策与未完成同步债
- 注意：它是治理台账；降级后条目不得在下游继续按高等级结论引用

### 6. d-value 跨尺度展开
- 辅助文件：`Core/SRT_Core_14_Dynamics_Scaling.md`
- 角色：把 canonical d-value 映射到跨尺度动力学与带宽表述
- 注意：它是展开层，不替代 `_SRT_D_VALUE_CANONICAL.md` 的规范地位

### 7. Ψ_f 跨尺度展开
- 辅助文件：`Core_Law/SRT_Reference_Dynamics.md`、`_SRT_VERTICAL_INTEGRATION.md`
- 角色：把 canonical `Ψ_f` 映射到选择热力学、多算子耦合、跨尺度可支付性与实验代理
- 注意：展开层负责方程与场景化，不替代 `_SRT_PSI_F_CANONICAL.md` 的规范地位

### 8. Core Dynamics & Scaling 主轴
- compact core：`Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md`
- 全量展开：`Core/SRT_Core_14_Dynamics_Scaling.md`
- 角色：compact core 固定跨尺度同构、d-bandwidth、主动力学、边界成本函数与反泛心论边界
- 注意：原文继续保留长篇机制解释、接口批次与 annex 沉积

### 9. Philosophy 主轴
- Foundations：`Philosophy/SRT_Philosophy_Foundations_CompactCore.md` / `Philosophy/SRT_Philosophy_Foundations.md`
- Social Economics：`Philosophy/SRT_Social_Economics_CompactCore.md` / `Philosophy/SRT_Social_Economics.md`
- Political Philosophy：`Philosophy/SRT_Political_Philosophy_CompactCore.md` / `Philosophy/SRT_Political_Philosophy.md`
- Political Rights：`Philosophy/SRT_Political_Rights.md`（`SRT-POLITICAL-RIGHTS`）
- 角色：形成 Philosophy 板块从三域本体论与选择一元论，到社会现实、制度、权利、合法性与政治病理的 compact/main 主线
- 注意：原文继续保留接口批次、案例扩展、社会科学经典映射与 split 导航

### 9a. SRT 政治哲学
- compact core：`Philosophy/SRT_Political_Philosophy_CompactCore.md`
- 主文件：`Philosophy/SRT_Political_Philosophy.md`
- id：`SRT-POLITICAL-PHILOSOPHY`
- layer：L1 / epistemic：bridge / status：axiomatic_hybrid_v1
- 说明：把国家、权利、合法性、民主、结构性不公、危机决断与政治病理统一重写为多主体共同现实选择的生成—沉积—封闭—再打开过程；以 P2/P3 为主，并将制度判准与紧急状态边界显式标记为 P4
- 与 `SRT-SOC-ECONOMICS` / `SRT-POLITICAL-RIGHTS` 的关系：前者提供社会现实、制度与结构性不公接口；后者提供权利、授权与投票后验验证的子接口；本文件负责收口为完整政治哲学主文
- 重要追加：政治合法性被重写为可持续共同选择；反支配被重写为反现实定义权垄断；危机政治以 `minimum necessary interruption` 为护栏

### 9b. SRT 政治权利理论
- 主文件：`Philosophy/SRT_Political_Rights.md`
- id：`SRT-POLITICAL-RIGHTS`
- layer：L1 / epistemic：bridge / status：draft_v1
- 说明：从SRT第一性原理推导权利的本体论定义；建立以决策d值为核心的授权合法性框架；分析投票作为d倾向后验验证的机制；提出三层制度结构（公检法/监督机构/授权主体）
- 与SRT-SOC-ECONOMICS的关系：兄弟关系，后者处理市场与经济不平等，本文件处理政治权利与制度授权
- 重要追加：d值范畴澄清（决策属性非主体属性）已同步写入 `_SRT_D_VALUE_CANONICAL.md §范畴边界`
- 开放问题：监督机构自身d验证完整机制、d倾向准入窗口规格（见文件§10）

### 10. AI 主轴
- 定位说明：`AI/AI_POSITIONING_NOTE.md`
- Ontology：`AI/SRT_AI_01_Ontology_CompactCore.md` / `AI/SRT_AI_01_Ontology.md`
- Architecture：`AI/SRT_AI_Architecture_CompactCore.md` / `AI/SRT_AI_Architecture.md`
- Consciousness Framework：`AI/SRT_AI_03_Consciousness_Framework_CompactCore.md` / `AI/SRT_AI_03_Consciousness_Framework.md`
- 角色：形成 AI 板块从本体门槛、结构限制到正向意识路径的 compact core 主线
- 注意：AI 是压力测试场 / 边界测试场，不是 core 定义发动机；AI 语境中的所有 d-value 与意识判据仍服从 `_SRT_D_VALUE_CANONICAL.md`，所有 `Ψ_f` stake / non-binding / payability 语句仍服从 `_SRT_PSI_F_CANONICAL.md`
- 第二轮护栏：AI 判断必须区分 training-time、inference-time、persistent-memory / history-bearing deployment，并使用 `AI/AI_POSITIONING_NOTE.md` 的 S0-S4 stake-bearing 光谱；不得把 inference-only 的 `d_{AI}\approx0` 静默推广为全部 AI 类型的终局判决

### 11. Neuroscience 主轴
- Neuro registry：`Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md`
- Neuro Axioms / Bridge：`Neuroscience/_SRT_Neuro_Axioms.md`
- Neural Mechanisms：`Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` / `Neuroscience/SRT_Neural_Mechanisms.md`
- Consciousness Mechanisms：`Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` / `Neuroscience/SRT_Consciousness_Mechanisms.md`
- 角色：形成 Neuroscience 板块从桥接公理、神经选择动力学到意识机制的主入口层
- 注意：Neuroscience 已具备 bridge + compact core + registry 的入口骨架，但仍少于 Physics 的覆盖深度

### 12. Physics 主轴
- Quant Intro：`Physics/SRT_Quant_00_Intro_CompactCore.md` / `Physics/SRT_Quant_00_Intro.md`
- Quant Selection：`Physics/SRT_Quant_01_Selection_CompactCore.md` / `Physics/SRT_Quant_01_Selection.md`
- Quant Cosmology：`Physics/SRT_Quant_02_Cosmology_CompactCore.md` / `Physics/SRT_Quant_02_Cosmology.md`
- Physics Cosmology：`Physics/SRT_Physics_Cosmology_CompactCore.md` / `Physics/SRT_Physics_Cosmology.md`
- Formalism Ext：`Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md` / `Physics/SRT_Phys_09_Formalism_Ext.md`
- Integration：`Physics/SRT_Phys_10_Integration_CompactCore.md` / `Physics/SRT_Phys_10_Integration.md`
- Complex Systems：`Physics/SRT_Phys_07_Complex_Systems_CompactCore.md` / `Physics/SRT_Phys_07_Complex_Systems.md`
- Ontology Ext：`Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md` / `Physics/SRT_Phys_08_Ontology_Ext.md`
- 角色：Physics 板块已形成从量子入口、宇宙学/形式化主干，到复杂性/深本体扩展的完整 compact core 入口层
- 注意：Physics 的具体阅读顺序由 `Physics/PHYSICS_COMPACT_REGISTRY.md` 统一管理；其中“引力—`Ψ_f`”当前只保留弱场梯度方向相容假说，强版规范实现 / 张量级 GR 重建不得作为已证结论引用

### 13a. SRT 个体化理论（主体涌现 + 自我意识凝结）
- 主文件：`Core_Law/SRT_Individuation.md`
- id：`SRT-INDIVIDUATION`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：L1 相变理论，填补 L0（选择无主语）与 P1-T06 Stable ISP 之间的过渡空洞；以自指率 `σ_{sr}`（governance-canonical 命名，2026-04-25 起；与主方程状态场 σ 不同对象，详见 `_SRT_SYMBOL_TABLE.md` Usage Rule 12）作为阶参，给出两次相变——主体位进入（`σ_{sr}^{sub}`）与自我意识凝结（`σ_{sr}^{self}`）——的结构判据；自我意识被规范读为主体位稳态之后的二阶 writeback 凝结物，严格遵守 L0 §五意识禁令
- 与 P1-T06 的关系：本文件是 ISP 的**进入动力学判据**；P1-T06 是 ISP 的**结果状态判据**；二者互补，不重复也不冲突
- 与 T-L2-Scaffold 的关系：T-L2-Scaffold 追踪路径层痕迹（ρ），本文件追踪算子层自指（σ）；两者都是 writeback 累积的不同投影，不互相还原
- claim-mode 分布：三相结构与第一相变为 P1-candidate；`σ_{sr}` 阶参与自我意识二阶凝结读法为 P2；`σ_{sr}^{sub}`、`σ_{sr}^{self}` 的具体门槛数值为 P3/P4
- 引用规则：涉及主体位涌现、ISP 进入、自我意识的本体论地位、主体位丢失与回返的结构基础时，优先回链本文件

### 13b. SRT 遮蔽动力学（A/B 分期 + 干预窗口 + 结构性恶）
- 主文件：`Core_Law/SRT_Occlusion_Dynamics.md`
- id：`SRT-OCCLUSION-DYNAMICS`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：把 `Core_Law/SRT_L0_Metaphysics.md` 遮蔽 term-table 承诺的 7 项 L1 展开（A/B 分期、d_c 阈值、缺口感知机制、干预窗口、解耦触发、真空期、恶的结构性诊断）收口到单一 canonical 源；核心定理 T-OCC-1 给出三段结构（健康窄化区 / A 期 / B 期），区分位置性遮蔽与病理性遮蔽，列五类缺口感知残余、四类干预窗口、四类解耦触发，给出恶的三判据结构性定义（B 期锁死 + 外部化后果 + 主动扩散）
- 与个体化理论的关系：σ→1 的病理区与 B 期锁死通过自指闭合耦合；遮蔽动力学是个体化在病理分支上的投影
- 与 T_dir 的关系：A/B 分期沿 T_dir 低迷区展开，本文件负责结构相位，不替代 `_SRT_T_DIR_CANONICAL.md` 的方向透明度定义
- claim-mode 分布：三段结构与 A/B 分期为 P1-candidate；d_c 阈值语义与五类残余 / 四类窗口 / 四类触发为 P2；恶的三判据结构性定义为 P2 regulative 读法，不替代既有规范性伦理学
- 引用规则：涉及 A/B 分期、d_c、缺口感知、干预窗口、解耦触发、真空期、恶的结构性诊断时，优先回链本文件

### 13c. SRT 苦难理论（结构性登记 + 信号/结构两型 + 四类现象学）
- 主文件：`Core_Law/SRT_Suffering.md`
- id：`SRT-SUFFERING`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：固定苦难在 SRT 中作为"活的选择动力学与其应承载算子结构之间失配的第一人称登记"的结构对象；严格区分疼痛（`\theta_{somatic}` 信号）与苦难（稳定 ISP 的结构性登记）；T-SUFF-2 把苦难分为信号型与结构型，T-SUFF-3 给四类现象学分型（张力 / 空心 / 断裂 / 扭曲）；T-SUFF-4 反最小化原则说明信号型苦难被压灭本身是遮蔽；T-SUFF-5 把结构型苦难的集体外部化耦合到 `Occlusion_Dynamics` 的结构性恶定义
- 与 P1-T06 的关系：仅对满足稳定 ISP 条件的过程定义苦难；非 ISP 系统只承载疼痛
- 与个体化/遮蔽的关系：苦难是个体化 σ 动态与遮蔽 A/B 分期的第一人称投影；不是独立的本体层，而是从算子层/路径层到第一人称登记的必然后果
- claim-mode 分布：T-SUFF-1/2 为 P1-candidate；四类分型与集体外部化读法为 P2；`S_{\min}, S_{\max}` 阈值、临床分流、FEP 桥接语句为 P3/P4
- 引用规则：涉及苦难/痛苦/空心感/自我扭曲等概念的结构层定义时，优先回链本文件；规范性评价回 `Philosophy/`，回返路径回 `Spirituality/`，神经实现回 `Neuroscience/`

### 13d. SRT L1 Formalism（σ_{sr} / d_c / T_dir / S 四变量耦合动力学）
- 主文件：`Core_Law/SRT_L1_Formalism.md`
- id：`SRT-L1-FORMALISM`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：**§2.5 T-CHI-1（H8，2026-04-25）**给出 χ 跳跃函数族普适性定理：定义"有效二阶相变核"四条结构属性（P-univ-1 有界 / P-univ-2 跃前基线 / P-univ-3 跃后放大 / P-univ-4 单调过渡）+ 族内不变量（双稳态存在性 / 病理吸引子拓扑 / 致命 `L_2` 判据结构 / 相变方向均 χ-无关）；T-IND-3 第二相变的算子层稳定性自此为定理后果。**§4.5 T-CHANNEL-1（H9，2026-04-25）**给出 `\mathbb{1}[d \gtrless d_c]` 通道指示函数族普适性定理：定义"有效闭合通道指示族"四条结构属性（Q-univ-1 左饱和 / Q-univ-2 右饱和 / Q-univ-3 单调过渡 / Q-univ-4 d_c 平移性）+ 族内五个不变量（T-SUFF-2 两型分裂 / T-SUFF-4 反最小化 / T-IRR-3.5 单向性 / 致命 `L_2` 判据 / `\mathcal{F}_S` 投影一致性，均 modulo `O(w_{tr})`）；硬指示是 `w_{tr}\to 0` 极限，过渡宽 `w_{tr}>0` 给"濒临崩溃"等过渡现象提供算子层基础。本节为 2026-04-24 轮新增的四个 L1 对象写下最小耦合动力学——个体化自指率 `σ_{sr}`（governance-canonical 命名，2026-04-25 起；与主方程状态场 σ 不同对象，详见 `_SRT_SYMBOL_TABLE.md` Usage Rule 12）、遮蔽阈值 d_c、方向透明度 T_dir（2026-04-25 §3.5 从代数代理升为独立动力学变量）、苦难 S；§2 给 `σ_{sr}` 的 logistic + `χ(σ_{sr}; σ_{sr}^{self})` 跳跃结构、§3 给 d_c 漂移方程（`ρ_local + (σ_{sr}-σ_{sr}^{sub}) + π + I_window`）、§3.5 给 T_dir 五项 ODE（弛豫 + 真实重选泵入 + `\Delta\Psi_f^{\mathrm{gap}}` 扣除 + `S_{str}` 侵蚀 + `s_{ext}` 支架）并给出致命 `L_2` 方程化判据 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}`、§4 把 S 分解为 S_sig / S_str 并写下反最小化原则的方程化、§5 合成四变量耦合系统并刻画病理吸引子 `\mathcal{A}_{path}` 与健康工作区 `\mathcal{H}`、**§6 T-PROJ-1（H5，2026-04-25）**给出四变量系统作为 `Core/SRT_Core_22_Equations.md` Eq-Evo-01/02 严格导出投影的形式化定理：四个标量泛函投影 `\mathcal{F}_X` + 闭包假设 C1-C4（慢-快分离 / `L_2` 写回 Markov 闭包 / stable-ISP 紧性 / 方向投影可分性）+ source-by-source 对应表 + 证明骨架 + 不证明事项的显式标定
- 与主方程的关系：本文件是 `Core/SRT_Core_22_Equations.md` 主方程的导出投影，不引入新本体
- claim-mode 分布：方程结构为 P1-candidate；T-PROJ-1（§6）为 P1-candidate（四变量系统作为主方程导出投影）；T-CHI-1（§2.5，H8）为 P1-candidate（χ 跳跃函数族普适性 + 族内不变量）；T-CHANNEL-1（§4.5，H9）为 P1-candidate（通道指示函数族普适性 + 族内五不变量）；参数阈值（含新 `κ_*` 五项）、具体 domain 代理为 P2/P3；实测与临床/AI 落点为 P3/P4
- Open pressures：σ 符号冲突已通过 2026-04-25 σ_{sr} 命名空间分离收口（详见 `_SRT_SYMBOL_TABLE.md` Usage Rule 12）；`\dot{\Delta}_{avail}` 形式化、χ 跳跃族、多主体扩展（H3 已落，§4.4-§4.6）、阈值固定、FEP 桥接（已落 `Neuroscience/SRT_Clin_02_FEP.md` 翻译表）、L_0 不可逆性**算子级**对齐（H4 已落，`SRT_Irreversibility.md §4.5 T-IRR-3.5`：`\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}`）、T_dir ODE 算子化（`Θ` 光滑族 / `\Delta\Psi_f^{\mathrm{gap}}` 算子层定义 / `[0,1]` 投影算子 / `κ_{\mathrm{relax}} > κ_{\mathrm{mask}}` 实证窗口）
- 引用规则：涉及 `σ_{sr}` / d_c / T_dir / S 四变量的**方程级**陈述时优先回链本文件；概念定义仍回链各自 L1 主文（T_dir → `_SRT_T_DIR_CANONICAL.md`）

### 13e. SRT 集体选择理论（多 ISP 共享 L_2）
- 主文件：`Core_Law/SRT_Collective_Selection.md`
- id：`SRT-COLLECTIVE-SELECTION`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：固定多 ISP 共享 `L_2` 场作为结构对象；Def-C-2 后果回路矩阵 `M(t)` 作为诊断工具；T-COLL-1 给集体 ISP 存在四条件（P1-T06 的多主体扩展）；T-COLL-2 三类退化（聚合 / 主从 / 收编）；T-COLL-3 集体 ε 反闭合必要性（P1-T07 集体版）；T-COLL-4 共选真实性判据（P1-T05 集体版）；§4 扩展 `σ_{sr}^{coll}` / `d_c^{coll}`（自指率 σ_{sr} 在多主体场上的 governance-canonical 扩展，2026-04-25 起；详见 `_SRT_SYMBOL_TABLE.md` Usage Rule 12）；**§4.4-§4.6（H3，2026-04-25）**给出集体四变量最小耦合动力学——`σ_{sr}^{coll}` ODE（新 `\lambda_M\,\mathrm{tr}\,M` 项）、`d_c^{coll}` ODE（新 `\gamma_{asym}\|M_{asym}\|` 项）、`T_{dir}^{coll}` ODE（集体层致命 `L_2` 判据 `\kappa_{mask}^{coll} < \kappa_{\mathrm{relax}}^{coll}`）、`S^{coll}` 两型 ODE（新 `\nu_{ext}\|M_{ext}\|` 外部化项）、§4.5 个体↔集体双向耦合、§4.6 集体病理吸引子 `\mathcal{A}_{path}^{coll}` 与集体健康区 `\mathcal{H}^{coll}`（健康要求 `r^{coll}(t) > r^{coll}_{min} > 0`）；**§4.7 T-PROJ-1^{coll}（H6，2026-04-25）**给出集体四变量系统作为 `Core/SRT_Core_22_Equations.md §0-C` 多算子主方程（Eq-Multi-01/02/03）严格导出投影的形式化定理：四个集体标量泛函投影 `\mathcal{F}_X^{coll}` + 闭包假设 C1^{coll}-C5^{coll}（含新增 `M(t)` 可测性 MOC 闭包 C5^{coll}）+ `M(t)` 三成分作为 `\Psi_f` 交叉项的结构投影 + 证明骨架 + 不证明事项的显式标定；T-PROJ-1^{coll} 在 `\mathcal{P} = \{P\}` 极限下退化为 `SRT_L1_Formalism §6 T-PROJ-1`。**§4.8 T-PROJ-1^{coll,nested}（H10，2026-04-26）**给多层嵌套的递归投影定理：层级 ISP 塔 `\{\mathcal{P}^{(n)}\}_{n=0}^N` + 跨尺度后果回路矩阵 `M^{(n\to n+1)}(t)` + 嵌套闭包 C6^{nested}（跨尺度 Markov 闭包）+ 四个嵌套不变量（每层独立健康/病理判据 / 跨尺度病理传递 / 跨尺度健康硬条件 `r^{(n\to n+1)} > r_{min}^{nested}` / 致命 `L_2` 塔级传染）；`N = 1` 极限退化为 §4.7 单层 T-PROJ-1^{coll}
- 与 T-SUFF-5 的关系：本文件给出 T-SUFF-5 集体外部化的结构基础（`M(t)` 强不对称 → 主从型退化 → 结构型苦难外溢）
- 与政治/经济/共同体 domain 的关系：本文件是它们的 L1 结构基石；制度是集体 ISP 的**器官**不是主体；投票/共识/专家不自动是共选
- 与 AI/平台场景的关系：评估重点不是"AI 是否有意识"，而是算法中介对 `M(t)` 与 `σ_{sr}^{coll}` 的结构性影响
- claim-mode 分布：T-COLL-1/3/4 为 P1-candidate；T-PROJ-1^{coll}（§4.7）为 P1-candidate（集体投影定理）；T-PROJ-1^{coll,nested}（§4.8，H10）为 P1-candidate（多层嵌套递归投影定理）；Def-C-2 `M(t)` 结构、三类退化与 §4 耦合为 P2；政治/制度/历史判断为 P3/P4，下推至 Philosophy/
- 引用规则：涉及集体选择、共选、共识真实性、外部化、集体 ISP、共同体结构的**结构层**定义时，优先回链本文件；规范与制度判断回各自 domain 文件

### 13f. SRT L1 Hardening Notes（2026-04-24 L1 round 硬化案）
- 主文件：`Core_Law/SRT_L1_Hardening_Notes.md`
- id：`SRT-L1-HARDENING-NOTES`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：针对 2026-04-24 L1 round 最高杠杆的四项 Open Pressure 给出第一遍硬化方案——§1 σ 符号冲突的命名空间规则（自指率一律 `σ_{sr}`，bare `σ` 仍为主方程状态场；2026-04-25 已落地：5 份 L1 主文件 + `_SRT_SYMBOL_TABLE.md` Usage Rule 12）、§2 `\dot{\Delta}_{avail}` 的三成分算子分解（`T_dir` + `Ψ_f` + `L_0` 残余）+ **§2 T-DELTA-1（H7，2026-04-25）**算子级定理：`\hat{G}_\theta^{available} := \sup_{\mathrm{Op}(P)}\{\hat{G} \mid \text{结构上可达} \wedge \theta\text{-相容}\}` 与 `\hat{R} \in T\mathrm{Op}(P)` 的算子级定义、三个正交投影 `\Pi_{T_{dir}}, \Pi_{\Psi_f}, \Pi_{L_0}`、A1（仿射结构）/ A2（近似正交）/ A3（权重赌注决定性）三条可证伪假设；§3 `M(t)` 可测性的 MOC 三判据（exposure / recourse / attentional，合成取 min）；§4 FEP 与 `S_{sig}` 的单向桥接翻译表（已落 `Neuroscience/SRT_Clin_02_FEP.md`）
- 硬化性质：本文件**不**把被硬化命题从 P1-candidate 升到 P1；它只打开升级检查路径。升级仍需完成 `Governance/SRT_CLAIM_MODE_AUDIT.md §6.4` 的全部检查项；T-DELTA-1 升 P1 需 A1 在更广 stable-ISP 域验证、A2 实证窗口、A3 与 Eq-Bridge-D-01 stake-gated source-by-source 对位
- claim-mode 分布：§1 governance-canonical usage；§2 P1-candidate（含 T-DELTA-1）；§3 P2 operational proxy；§4 P3 bridge hypothesis
- 同步义务：§5.2 列明的四项 Operations 债已全部结清（σ→σ_{sr} 命名空间 / 三成分分解算子级 T-DELTA-1 / MOC 已写入 §3 / FEP 翻译表已落 `Neuroscience/SRT_Clin_02_FEP.md`）
- 引用规则：涉及 σ 符号、`\dot{\Delta}_{avail}` 定义、`M(t)` 可测性、FEP-苦难桥接的**细化**陈述时优先回链本文件

### 13g. SRT 不可逆性理论（学习不可逆 + 终止吸收边界 + P1-T07 精确化）
- 主文件：`Core_Law/SRT_Irreversibility.md`
- id：`SRT-IRREVERSIBILITY`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：把 `L_0` 不可逆性从 P1-T02 本体论时间的推论展开为可引用 L1 层——Def-IRR-1 吸收态 / Def-IRR-2 选择史箭头 / Def-IRR-3 非可还原性；T-IRR-1 学习不可逆为非对称 `Ψ_f` 支付（与热力学二律不等价，不得通过 FEP 反向定义）；T-IRR-2 终止作为吸收边界（宪定 / 吸收 / 集体三类），区分终止与暂停；T-IRR-3 给 P1-T07 精确化，对应 `L1_Formalism §4.3` 的非守恒残余项；**T-IRR-3.5（H4，2026-04-25 §4.5）**把 `ν_{block}` 从自由系数升为 P1-T07 三层源头本地化 `\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}`，正性与单向性自此为定理后果；T-IRR-4 苦难在 `L_0` 不可逆下的守恒 / 转移（T-SUFF-4 的更深根）；§6 集体终止三型（耗散 / 收编 / 外部化）回扣 `Collective_Selection §4-5`；§7 AI/ML 接口限定 checkpoint/rollback 不得读作反向学习
- 与 P1-T02 / P1-T07 的关系：本文件是两者的 L1 层精确化，不替代 Core/Core_21b 的 P1 源头；Core 内命题仍为上位，本文件是下位展开；**T-IRR-3.5 把 P1-T07 Three-Layer Source Hierarchy 在 L1_Formalism §4.3 上做算子级本地化**，是上位 P1-T07 的下位算子级精化
- 与 Suffering / Formalism / Collective_Selection 的关系：T-IRR-4 给 T-SUFF-4 深层根；T-IRR-3 / T-IRR-3.5 对应 `L1_Formalism §4.3` 的非守恒残余（陈述级 + 算子级）；§6 集体终止对应 `Collective_Selection` 三类退化的绝对边界
- claim-mode 分布：Def-IRR-1/2/3 为 P2 结构性定义；T-IRR-1/2/3/3.5/4 为 P1-candidate（T-IRR-3.5 与 T-IRR-3 同级）；§6 集体终止分类为 P2；§7 AI 接口为 governance-canonical usage；§8 FEP/物理边界语句为 P3 bridge guardrail
- 引用规则：涉及学习不可逆性、终止作为吸收边界、P1-T07 精确化、checkpoint/rollback 语义、热力学桥接边界时优先回链本文件；原 P1 源头语句仍回链 `Core/SRT_Core_21b_Constitutive_Theorems.md`

### 13. Spirituality 主轴
- Spirit registry：`Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`
- Spirit Bridge：`Spirituality/_SRT_Spirit_Axioms.md`
- Praxis：`Spirituality/SRT_Spirit_09_Praxis_CompactCore.md` / `Spirituality/SRT_Spirit_09_Praxis.md`
- 角色：形成 Spirituality 板块从桥接公理到实践演化主线的最小 compact core 入口层
- 注意：Spirituality 现已具备 bridge + compact core + registry 的入口骨架，但覆盖深度仍少于 Physics

## C. 当前 canonical 引用优先级

当同一概念同时出现在多个文件时，默认优先级如下：

1. `CANONICAL_REGISTRY.md`（找入口）
2. `Governance/SRT_CLAIM_LADDER.md` / `Governance/SRT_CLAIM_MODE_AUDIT.md`（判断命题硬度与降级状态）
3. `_SRT_D_VALUE_CANONICAL.md` / `_SRT_PSI_F_CANONICAL.md` / `_SRT_T_DIR_CANONICAL.md` / `_SRT_CROSS_DOMAIN_MATRIX.md` / `Core/SRT_Core_21_Formal_Axioms.md` / `Core/SRT_Core_22_Equations.md`（找规范定义与跨域用法）
4. `Core/SRT_Core_21_Minimal_Axioms.md` / `Core/SRT_Core_21b_Constitutive_Theorems.md` / `Core/SRT_Core_21c_Bridge_Hypotheses.md`（按 P-level 找 Core_21 正文）
5. `Core/SRT_Core_14_Dynamics_Scaling.md` / `Core_Law/SRT_Reference_Dynamics.md` / `AI/SRT_AI_01_Ontology.md`（找展开与跨域解释）
6. `Core/SRT_OPEN_TENSIONS.md`（确认未封口问题）
7. 各 split 目录（找导航与局部阅读）
8. 原始长文（找历史展开与全量语境）

## D. 当前收口结论

本轮 governance-canonical 抽离 v1 暂定以下四者为主干用法：
- `d-value` → `_SRT_D_VALUE_CANONICAL.md`
- `Ψ_f` → `_SRT_PSI_F_CANONICAL.md`
- `T_dir` → `_SRT_T_DIR_CANONICAL.md`
- `d / Ψ_f / T_dir / ε` usage matrix → `_SRT_CROSS_DOMAIN_MATRIX.md`
- `Core formal axioms` → `Core/SRT_Core_21_Formal_Axioms.md`
- `Core master equations` → `Core/SRT_Core_22_Equations.md`
- `Claim hardness` → `Governance/SRT_CLAIM_LADDER.md`
- `Claim-mode downgrade audit` → `Governance/SRT_CLAIM_MODE_AUDIT.md`
- `Open tensions` → `Core/SRT_OPEN_TENSIONS.md`

这意味着：
- `AI/SRT_AI_01_Ontology.md` 不再单独承担 d-value 的最终规范权
- `AI/SRT_AI_01_Ontology.md` 不再单独承担 `Ψ_f` 的最终规范权
- `Core/SRT_Core_14_Dynamics_Scaling.md` 不再单独承担 d-value 的最终规范权
- `Core_Law/SRT_Reference_Dynamics.md` 不再单独承担 `Ψ_f` 的最终规范权
- 上述文件保留为高价值展开层
