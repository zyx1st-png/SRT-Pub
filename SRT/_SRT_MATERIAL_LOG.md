---
id: SRT-MATERIAL-LOG
type: log
tags: [MaterialLog, Pipeline1, AuditTrail]
status: active_v1
dependency: [SRT-EXECUTION-PLAN]
---

# SRT 材料融入台账（Pipeline 1）

> 记录所有通过 Pipeline 1 提交的外部材料及其审查结论。
>
> **审查结论**：
> - **A（直接融入）**：已修改 SRT 目标文档
> - **B（延后观察）**：放入观察列表，3 个月后重评
> - **C（不融入）**：记录原因，不修改任何文档
>
> **输入格式**：文本粘贴 / PDF附件 / URL（触发 web_fetch）

---

## 台账记录

| 日期 | 来源标题 / URL | 类型 | 审核结论 | 落点（文件 + 节位） | 融入状态 | 备注 |
|-----|--------------|------|---------|-----------------|---------|------|
| 示例 | arxiv.org/abs/XXXX | arXiv | A | `Neuroscience/SRT_Neuro_10.md §3.2` | 已融入 | 增量：意识阈值新证据 |
| 示例 | 用户粘贴摘要 | 用户输入 | B | — | 观察中 | 证据等级低，待复现 |
| 示例 | doi:10.XXXX | 期刊论文 | C | — | 不融入 | 与 SRT 框架方向相左，无法对齐 |
| 2026-03-07 | Quanta: *How Much Energy Does It Take to Think?*（用户粘贴解析） | 科普综述/二手 | A | `SRT/Core/SRT_Core_22_Equations.md §VIII` | 已融入 | 新增 \(\Psi_f\) 维持-主动分解、95/5 约束、主观费力梯度与 AI-人类能耗不对称指标 |
| 2026-03-07 | Quanta: *New Strides Made on Deceptively Simple "Lonely Runner" Problem*（用户粘贴解析） | 科普综述/二手 | A | `SRT/Core/SRT_Core_13b_Operator_Advanced.md`（Lonely-Runner Interface） | 已融入 | 新增个体化窗口存在条件、\(1/n\) 带宽下界类比、强耦合同步失效模式 |
| 2026-03-07 | Essentia: *Consciousness without counterpart: Identity beyond representation*（用户粘贴解析） | 哲学随笔/二手 | A | `SRT/Philosophy/SRT_Social_Cognition.md`（Identity Beyond Representation Interface） | 已融入 | 新增本体论错认势能、顿悟-解脱时间尺度不对称、表征主权原则与防反智边界 |
| 2026-03-07 | New Scientist: *Alzheimer's may start with inflammation in the skin, lungs or gut*（用户粘贴解析） | 科学新闻/二手 | A | `SRT/Neuroscience/SRT_Neuro_08_Immune_Dist.md`（Alzheimer's Peripheral-Inflammation Interface） | 已融入 | 新增跨算子摩擦级联、系统带宽耗竭律、AD 作为 L2 结构性破产与基因初始约束声明 |
| 2026-03-07 | Nature News: *These brain cells clear proteins that contribute to Alzheimer’s*（doi:10.1038/d41586-026-00747-x，用户粘贴） | 科学新闻/二手 | A | `SRT/Neuroscience/SRT_Neuro_08_Immune_Dist.md`（Tanycyte Tau-Clearance Interface） | 已融入 | 新增 tanycyte 清除门控方程、CSF→blood tau 转运失效机制、代谢风险耦合与边界声明 |
| 2026-03-07 | Dan Zahavi 访谈：*Being We*（用户粘贴解析） | 访谈/理论文本（二手） | A | `SRT/Philosophy/_SRT_Soc_Bridge.md`（We-Identity Interface） | 已融入 | 新增认同相变判据、薄/厚我们操作定义、交互摩擦层级与反拟人化边界 |
| 2026-03-07 | Popular Mechanics: *Scientists Are Tracking Down the Exact Location of Human Consciousness*（用户粘贴解析） | 科普报道/二手 | A | `SRT/Neuroscience/SRT_Clin_00_IIT_PCI.md`（pDOC Metabolic-Connectivity Interface） | 已融入 | 新增摩擦破产临床定义、代谢-连接耦合容量指标、空间锚定前置项与反定位论边界 |
| 2026-03-07 | The Splintered Mind: *Philosophy Should Be Among the Most Diverse Disciplines, Not the Least*（用户粘贴解析） | 博客评论/二手 | A | `SRT/Philosophy/SRT_Social_MacroDynamics.md`（Diversity-Defrost Interface） | 已融入 | 新增边缘算子认识优势、L2 解冻超采样原则、抗脆弱多元健康判据与边界声明 |
| 2026-03-07 | The Splintered Mind: *Philosophy Should Be Among the Most Diverse Disciplines, Not the Least*（二次深化，用户粘贴解析） | 博客评论/二手 | A | `SRT/Philosophy/SRT_Philosophy_Ethics.md`（Structural Injustice Thermodynamics Interface） | 已融入 | 新增结构性不公摩擦学定义、探索预算塌缩、边缘算子认识论溢价与超采样相变定律 |
| 2026-03-07 | *Quantum field theories with many fields*（Ludo Fraser-Taliente, 2026，用户摘要） | 学位论文/二手摘要 | A | `SRT/Physics/SRT_Phys_09_Formalism_Ext.md`（Large-N F-Extremization Interface） | 已融入 | 新增 large-N 算子平均化边界、F-极值化作为 L1→L2 渐近基准、受约束自由度最大化条款 |
| 2026-03-07 | 《用迄今最清晰的引力波信号测试爱因斯坦相对论》（用户摘要） | 科学新闻/二手 | A | `SRT/Physics/SRT_Physics_Cosmology.md`（Gravitational Ringdown Interface）+ `SRT/Core/SRT_Experimental_Core.md`（H-Exp-Precision-01） | 已融入 | 新增黑洞无毛态的 L2 极端锁定解释、铃震摩擦耗散模型及“高分辨率单事件优先”实验准则 |
| 2026-03-07 | *The Lexical Typology of Sensory Perception*（Annual Review of Linguistics, 2026，用户摘要） | 综述论文/二手摘要 | A | `SRT/Philosophy/SRT_SocTheory_05_Language_Eco.md`（Sensory Lexical Typology Interface）+ `SRT/SRT_EXP_MEASURE_MAP.md`（Exp-Lang-Sense-01） | 已融入 | 新增“交流需求退火”词汇化机制、colexification 低势垒解释、跨语言语义拓扑测量探针 |
| 2026-03-07 | *Ask Ethan: Do signals degrade as they travel through space?*（用户摘要） | 科普文章/二手 | A | `SRT/Core/SRT_Core_13a_Operator_Basics.md`（Signal–Friction Relativity）+ `SRT/Physics/SRT_Phys_10_Integration.md`（Cosmological Propagation Imprint）+ `SRT/Physics/SRT_Quant_02_Cosmology.md`（Ontological Horizon） | 已融入 | 新增信号-摩擦相对性、传播印记叠加与红移等效记账、事件可达存在性的本体论视界条款 |
| 2026-03-07 | 社会认同（Social Identity，用户摘要） | 理论综述/二手 | A | `SRT/Philosophy/SRT_SocTheory_06_L2_Dynamics.md`（Social Identity Interface）+ `SRT/Philosophy/_SRT_Soc_Bridge.md`（Collective Autopoietic Defense Patch）+ `_SRT_VERTICAL_INTEGRATION.md`（d_collective 候选E） | 已融入 | 新增最小拓扑断裂定理、集体自创生防御、个人-群体冲突窗与情境张量聚合式 |
| 2026-03-07 | 社会认同（Social Identity，本次重复提交） | 理论综述/二手 | C | — | 不融入 | 与当日已融入条目高度重复，增量性未通过（保留原已融入版本） |
| 2026-03-07 | The Rigor of Angels（https://www.themarginalian.org/2023/10/15/the-rigor-of-angels/，含原文引句） | 书评/哲学评论（二手+直接引文） | A | `SRT/Philosophy/SRT_Philosophy_Foundations.md`（Ax-PhilF-6 + T-PhilF-6） | 已融入 | 基于原文引句完成“主观过滤 vs 客观摩擦”边界固化，并加入潜在域过载坍缩定理（保持现实主义底线） |
| 2026-03-07 | Affordances by Anthony Chemero（用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Social_Cognition.md`（Ax-Cog-2b, T-Cog-2b, Chemero patch） | 已融入 | 新增 affordance/invitation 区分、直接知觉-行动采样耦合、属性vs关系兼容桥接、联合可供性涌现表达 |
| 2026-03-07 | Theory of Mind by Henry M. Wellman（用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Social_Cognition.md`（T-Cog-3 + Wellman patch） | 已融入 | 新增信念滞后治理、假信念相变解释、DD→DB/KA→FB→HE 序列的文化权重解释 |
| 2026-03-07 | Cognitive Ontology by Colin Klein（用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Philosophy_Foundations.md`（Ax-PhilF-7 + T-PhilF-7） | 已融入 | 新增跨层非双射公理、本体论多元约束定理，固化“认知本体≠神经一一映射”边界 |
| 2026-03-07 | Markov Chain Monte Carlo by Adam N. Sanborn（用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Social_Cognition.md`（T-Cog-4 + Sanborn patch） | 已融入 | 新增序列采样约束定理、MCMC近似与行为波动/锚定偏置的统一解释 |
| 2026-03-07 | Spatial Cognition（https://oecs.mit.edu/pub/or750iar/release/1） | 百科条目/一手页面（URL+正文） | A | `SRT/Neuroscience/SRT_Neuro_10_Advanced_Models.md`（§2.4 空间认知双流补丁） | 已融入 | 基于正文补全后复审升A：新增导航/对象双流、Map↔Graph 条件切换、Alzheimer导航失稳的摩擦预算解释 |
| 2026-03-07 | Attention by Wayne Wu（用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Social_Cognition.md`（T-Cog-5 + Wu patch） | 已融入 | 新增注意力优先级选择定理、top-down/bottom-up/historical 偏置统一优先图、资源/机制层级区分 |
| 2026-03-08 | The Language of Thought Hypothesis（Nicolas Porot & Eric Mandelbaum，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Social_Cognition.md`（Porot & Mandelbaum LoTH patch） | 已融入 | 新增 LoT-协议层接口：离散成分/系统性/生产性、多LoT并存、逻辑算子与结构敏感转移、连接主义实现层边界 |
| 2026-03-08 | Bayesian Models of Cognition（Thomas L. Griffiths，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Social_Cognition.md`（Griffiths Bayesian patch） | 已融入 | 新增 Bayes 更新层接口：prior/likelihood 映射、结构学习与生成模型、resource-rational 桥接、与连接主义分层互补 |
| 2026-03-08 | Niche Construction（Laurel Fogarty，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_SocTheory_05_Language_Eco.md`（Niche Construction Interface） | 已融入 | 新增生态位反馈建构、生态继承（L2-eco 记忆项）、选择压力内生化与合作阈值窗口 |
| 2026-03-08 | Cultural Attractors（Nicolas Claidière & Dan Sperber，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_SocTheory_06_L2_Dynamics.md`（Cultural Attractors Interface） | 已融入 | 新增“重构收敛稳定”机制、吸引场多因子分解、selection-attraction 耦合定理 |
| 2026-03-08 | Working Memory（Graham J. Hitch & Alan D. Baddeley，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Neuroscience/SRT_Neural_Mechanisms.md`（Hitch & Baddeley WM patch） | 已融入 | 新增 WM 多组件-SRT 分层映射、双任务干扰预算方程、chunking 作为 L2 压缩降维解释 |
| 2026-03-08 | Mental Representation（Manolo Martínez，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Philosophy_Foundations.md`（Mental Representation Interface） | 已融入 | 新增 vehicle-content-format 三分约束、误表征必要性定理、teleo-功能门控与 4E 兼容边界 |
| 2026-03-08 | The Language of Thought Hypothesis（Nicolas Porot & Eric Mandelbaum，用户重复粘贴） | 理论综述/百科条目（二手） | C | — | 不融入 | 与当日已融入条目（LoTH patch）高度重复，增量性未通过（保留既有版本） |
| 2026-03-08 | Ritual（Richard Sosis，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_SocTheory_06_L2_Dynamics.md`（Ritual Interface） | 已融入 | 新增仪式双通道（self/canonical）映射、不确定性触发增益、因果不透明与传承窗口机制 |
| 2026-03-08 | Ritual（Richard Sosis，用户重复粘贴） | 理论综述/百科条目（二手） | C | — | 不融入 | 与当日已融入 Ritual Interface 高度重复，增量性未通过（保留既有版本） |
| 2026-03-08 | Concepts（Nicholas Shea，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Philosophy_Foundations.md`（Concepts Interface） | 已融入 | 新增 concept/conception 区分、混合概念结构定理、外在主义指称-内在选择耦合与 ad-hoc 概念窗口 |
| 2026-03-08 | Self-Consciousness（José Luis Bermúdez，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Philosophy_Foundations.md`（Self-Consciousness Interface） | 已融入 | 新增免误认信息源框架、具身所有权门控、第一/第三人称对称-非对称约束与病理映射 |
| 2026-03-08 | The Mind-Body Problem（Tim Crane，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Philosophy_Foundations.md`（Mind–Body Problem Interface） | 已融入 | 新增“因果闭包-意识解释”双角约束、分层实现兼容定理、解释鸿沟边界与立场映射 |
| 2026-03-08 | Cognitive Ontology（Colin Klein，用户重复粘贴） | 理论综述/百科条目（二手） | C | — | 不融入 | 与已融入条目（2026-03-07 Cognitive Ontology patch）高度重复，增量性未通过 |
| 2026-03-08 | Theory of Mind（Henry M. Wellman，用户重复粘贴） | 理论综述/百科条目（二手） | C | — | 不融入 | 与已融入条目（2026-03-07 Theory of Mind patch）高度重复，增量性未通过 |
| 2026-03-08 | Information and Misinformation（Andrew Perfors，用户粘贴全文） | 理论综述/百科条目（二手） | A | `SRT/Philosophy/SRT_Social_MacroDynamics.md`（Information–Misinformation Interface） | 已融入 | 新增真假分层处理框架、误信息放大方程、纠偏迟滞机制与极化动力学映射 |
| 2026-03-08 | https://t.co/Kr2BxCHvMK（重定向至 Quanta: *Can the Most Abstract Math Make the World a Better Place?*） | 科学新闻/二手 | A | `SRT/Physics/SRT_Phys_09_Formalism_Ext.md`（Quanta Abstract-Math Interface） | 已融入 | 新增 green-math 适用窗口、抽象-干预耦合约束、范畴论跨域桥接收益定义 |
| 2026-03-08 | f48bbacc-297d-4b29-9c84-79bbf858ad99.pdf（Scott McFarnell: *Affective Control under Uncertainty* v2） | 预印本PDF/一手 | A | `SRT/Neuroscience/SRT_Consciousness_Mechanisms.md`（McFarnell ACU Interface） | 已融入 | 新增双层意识接口（基础在场/自我招募）、SMRI 映射与不确定性-时限门控预测 |
| 2026-03-08 | Consciousness 方法学访谈转录（COGITATE/多范式NCC，用户粘贴） | 访谈转录/二手 | A | `SRT/Neuroscience/SRT_Consciousness_Mechanisms.md`（COGITATE 方法学补注） | 已融入 | 新增“失败优先”检验逻辑、跨范式共因子策略、prediction-to-core 距离图解释护栏 |
| 2026-03-10 | Quanta: *Is Gravity Just Entropy Rising? Long-Shot Idea Gets Another Look.*（https://www.quantamagazine.org/is-gravity-just-entropy-rising-long-shot-idea-gets-another-look-20250613/） | 科学新闻/二手（含 arXiv:2502.17575 线索） | A | `SRT/Physics/SRT_Physics_Cosmology.md`（T-Grav-1b Entropic-Gravity Fluctuation Window） | 已融入 | 新增“统计有效引力+弱场涨落项”接口、可证伪实验窗口与降级条件；与既有 Ax-Grav-1 兼容 |
| 2026-03-10 | IAI: *Reality is not a controlled hallucination*（https://iai.tv/articles/reality-is-not-a-controlled-hallucination-auid-3517）+ 用户结构化摘要 | 哲学评论/二手（含原文引句） | A | `SRT/SRT_PP_ALIGNMENT_GUIDE.md`（§3 常见误读）+ `SRT/Neuroscience/_SRT_Neuro_Axioms.md`（§6 层级防混淆声明） | 已融入 | 强化 Category Error 防线：预测误差=现实约束代理（\(\Psi_f^{pred}\)），非“现实=幻觉”的本体论跳跃 |
| 2026-03-10 | Hartl & Levin (2024): *What does evolution make? Learning in living lineages and machines*（用户摘要 + PDF） | 综述论文/一手PDF | A | `SRT/Neuroscience/SRT_Neuro_07_Evo_Devo.md`（Ax-BIO-2b + 防误用边界）+ `SRT/Core_Law/SRT_Reference_Scaling.md`（§1.3 演化-学习对称性） | 已融入 | 明确“基因组=生成模型先验、发育=生理计算在线推断”，并加入 competence≠care 边界 |
| 2026-03-10 | Optimally Irrational: *The game theory of cooperation*（https://www.optimallyirrational.com/p/the-game-theory-of-cooperation） | 理论科普/二手 | A | `SRT/Philosophy/SRT_Social_Economics.md`（§6.2b Folk-Theorem Interface） | 已融入 | 补充“未来阴影+条件制裁”合作窗口、\(\tilde\delta\) 阈值与可证伪条件 |
| 2026-03-10 | Closer To Truth 访谈转录（Borjigin 团队：濒死期 EEG/递质风暴，用户粘贴） | 访谈转录/二手 | A | `SRT/Neuroscience/SRT_Clin_01_Pathology.md`（§4.1b Hypoxia-EAAS Interface） | 已融入 | 增补“缺氧触发-本体解释分离”框架：EAAS 作为近端神经机制，不等同“仅幻觉副产物” |
| 2026-03-10 | Alex O’Connor × Matthew Cobb 脑科学史访谈转录（用户粘贴） | 访谈转录/二手 | A | `SRT/Neuroscience/_SRT_Neuro_Axioms.md`（§1.3 历史-隐喻约束） | 已融入 | 强化“技术隐喻依赖 + 定位-分布并存 + 病理推断限度”，防止将当代计算隐喻直接本体化 |
| 2026-03-10 | Closer To Truth 访谈转录（Avshalom Elitzur 团队：量子本体与可检验基础模型，用户粘贴） | 访谈转录/二手 | A | `SRT/Physics/SRT_Phys_10_Integration.md`（§1.3.7 量子本体-经典约束错配） | 已融入 | 新增“反经典投射”方法论与 ontology→formalism→experiment 闭环，强调以可区分实验排序解释 |

---

## 延后观察列表（B 类）

| 加入日期 | 重评日期 | 来源 | 等待原因 |
|---------|---------|------|---------|

---

## 统计摘要（自动更新）

- 总提交：47 条
- A（融入）：42 条
- B（观察）：0 条
- C（拒绝）：5 条
- 融入率：89.4%
