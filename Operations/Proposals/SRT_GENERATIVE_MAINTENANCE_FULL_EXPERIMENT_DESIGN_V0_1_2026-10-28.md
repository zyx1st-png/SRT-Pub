---
id: SRT-GENERATIVE-MAINTENANCE-FULL-EXPERIMENT-DESIGN-20261028
type: proposal
status: draft
canonical: false
layer: operations
epistemic_layer: machine_analysis
claim_mode: complete_paper_only_experimental_protocol_candidate
created: 2026-10-28
updated: 2026-10-28
research_mode: U
root_question: How do maintenance-constituted organization, individual-relative consequence salience, adaptive coarse-graining, and bounded action affordances interact without an assumed ultimate telos?
comparative_claim: none; a fair causal test and mature-model comparison, not a claim of SRT advantage
named_comparator: organizational closure; homeostatic reinforcement learning; recurrent model-free control; model-based world-model reinforcement learning; predictive state abstraction
n_mode_triggered: false
dependency:
  - STATUS.md
  - Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md
  - Operations/Audits/SRT_CN2_A_P1_P6_OBSERVABILITY_IDENTIFIABILITY_PREPASS_2026-10-09.md
  - 03_Bridges/SRT_Dissipative_Structures_and_Selection_Structures_Bridge_2026-08-04.md
  - papers/costly_selective_closure_supplement/CONSEQUENCE_SCOPE_MECHANISM_AUDIT_POST_E4_CLOSURE_2026-09-15.md
tags: [MachineLearning, ArtificialLife, ExperimentDesign, Salience, CoarseGraining, Viability, OrganisationalMaintenance, PaperOnly]
---

# 完整实验设计 v0.1 — 生成性自维系、个体显著性、粗粒化及行动可能性的变化

> **状态与授权：DESIGN COMPLETE FOR REVIEW / NOT AUTHOR-FROZEN / NOT AUTHORIZED TO EXECUTE。** 这是作者明确要求“创建 PR 完成完整的实验设计”之后的 **M-origin 自包含纸面协议**，不等于作者批准所列数值、实验启动、先验目的、生命本质解释或 SRT canonical 更新。仓库唯一 CURRENT NEXT = 既有中性认知研究；CN-2 A 的 P1–P6 人类观测/预测比较保持优先，CN-3/toy execution HOLD、MG-1/MG-2、FR-ADV 和作者实验授权不变。**本协议属于平行的候选纸面设计，不成为第二条活动执行 programme。**
>
> **与 Draft PR #1136 的关系**：#1136 保存对话思想与开放机制备忘；本稿自包含，不依赖它合并，不将 #1136 非 canonical 内容当成 merged-main 权威。无训练结果、无新算法的优越性断言、无预注册或实验数据；全文数字均为“建议的初始规格/资源上限”，正式采用必须经独立审阅与作者明确确认。
>
> **该实验能研究**：组织反馈的可识别因果作用、因个体条件不同而重切的后果表征、组织改造带来的条件性行动能力变化、成熟 RL 能否完整解释。**不能研究/证明**：原初 Selection、意识/主体性、真正的生物自创生、无界新行动语法、生命的必要充分定义、任何先于生命的终极目标。

## 0. 研究假说与证明负担

- **H0 / 成熟解释足够**：只要身体动力学、观测和训练条件充分，state-conditioned recurrent RL、homeostatic RL 或世界模型即可学习所有观察到的显著性重分配与行动行为；无需添加新的不可还原机制。**这是默认可信对照，不是稻草人。**
- **H1 / 组织干预效应**：在共同干预前状态与相同外生噪声下，相比匹配的 open-loop 维修输入，闭合的相互维护反馈可以改变受损后的功能可维系性与有限时窗行动可达性。方向**不是数学预设必须变好**；稳态和扰动条件分别估计。
- **H2 / 个体相对显著性**：同样的外界事件与即时任务奖励，当个体组织状态 A/B 改变其未来后果时，成功学习者会在合法观测条件下改变所保留的环境区别。成熟 HRL/world model 也完全可能达成。
- **H3 / 历史重切与可行动性**：此前维护/构建活动改变当前可执行行动的真实成功条件；依后果进行的表征划分随之改变。它只构成**相对当前组织、时间和资源的可达性**，不是“世界从无变有”。
- **H4 / 相互作用的非平凡性（探索性）**：组织反馈和适应性压缩的交互，可能改善**未训练扰动**下的后果预测与适应。若强 full-capacity recurrent/world-model 等效，记录为 mature-source-owned realization；不推理论独特性。
- **反例必须纳入**：长期维持而无任何重构；短期产生新动作组合但迅速失能；外部维修与内部维修等效；反馈切断后能力不减；只改变 reward 时行为就完全一样。

## 1. 两阶段问题与独立证据层

| 阶段 | 因果目标 | 方法 | 不允许推论 |
|---|---|---|---|
| **G0 有限状态世界可行性** | 不靠任何学习算法，闭合反馈、open-loop 替代和结构改造对 H 步可生存/可达性的实际作用 | 有限状态转移核、穷举、动态规划、成对外生事件反事实 | “某 RL 学出了生命本质”；“个体边界自然涌现” |
| **G1 学习/压缩层** | 不同学习能力的模型能否学到个体相对显著性、维修与重切并迁移到新后果 | PPO-RNN / HRL / capable world-model，对照固定与可学编码 | G1 预测优胜 = SRT/生命性独特机制 |
| **G2 结构生成层（未来独立候选，NOT in scope）** | 在没有预定义 M/C/R/个体边界的物质/反应世界中出现维护组织 | 人工化学/元胞自动机另行建模 | 由 G0/G1 自动推出组织起源 |

**先 G0 后 G1**，G0 失败就不能靠训练复杂网络“救”项目。该层级命名 G0/G1 与仓库 CN-2 的 E2/E3/E4 **无身份关系**，不得复用后者 PASS 口径。

## 2. 世界、变量、时序：一套可以程序化落实的环境规格

### 2.1 状态、可观测性与外生量

以小型离散 POMDP 为主，G0 使用完全已知转移核做事后真值计算，G1 对 agent 仅提供合法部分观察。

完整隐状态：\`s_t=(E_t,B_t,M_t,C_t,R_t,J_t,L_t,Q_t,H_t)\`。

| 名称 | 值域（建议最小档位） | 含义 | 真实因果作用 |
|---|---|---|---|
| \`E\` | \`{0,…,8}\` | 能量 | 行动需要能量；0 为不可继续行动的失能 |
| \`B\` | \`{0,…,4}\` | 可用维修材料 | 维修/制造实际消耗 |
| \`M\` | \`{0,1,2}\` | 维护性边界/防护模块 | 影响 R 的损坏概率和资源效率 |
| \`C\` | \`{0,1,2}\` | 感知/行动校准模块 | 控制信号可靠度及精确维修成功条件 |
| \`R\` | \`{0,1,2}\` | 转化/修复模块 | 控制收集转化效率以及可维修行动 |
| \`J\` | \`{none,U-shield,V-filter}\` | 可替换的构建物 | 改变之后指定环境后果/行动的成功条件 |
| \`L\` | \`{safe,resource}\` | 小型场景位置 | resource 区需要实际可通过的行动 |
| \`Q\` | 两步有限队列 | 即将兑现的 U/V 环境扰动 | 使信号预告与实际损伤错开 |
| \`H\` | \`{0,1,2}\` | 连续失能计数 | 区分短暂损伤和无法行动的终止 |

外生：\`U_t,V_t∼Bernoulli(p_U,p_V)\`，建议发现版各 \`p=0.20\` 且独立；预先生成 episode-local **exogenous tape**，包括 U/V、观测噪声、环境损伤的随机数和行动成功随机数，所有互为因果对照的克隆状态复用同一 tape。说明：完全相同的 RNG seed 在分支消耗不同数量随机调用时**不构成**有效 common-random-numbers，必须按 \`(episode,time,mechanism,subdraw)\` 预先索引。

观测给 agent：能量与材料的有噪/分箱读数、局部模块健康信号、U/V 预兆 \`q_U,q_V\`、已安装 J 的局部反馈、自己的上一步动作和已实际见到的后果。**不向 agent 给出真实未来 U/V、完整转移核、G0 DP 或离线参考显著性；**必要时提供完整当前模块状态的 \`privileged/full-state\` 单独对照，所有算法等权。

建议 cue 噪声：\`P(q_i=U_i)=0.85\` 在 \`C≥1\`，\`C=0\` 时 0.5；对照需要区分 \`do(U)\`（原因干预）与 \`do(q_U)\`（测量/感知干预），两者不得混用。训练期间可保留有噪声局部体态，评估时同时测试 full-state ceiling。

### 2.2 原语行动、动作合法性与代价

所有模型访问**完全相同**的原语集：\`harvest,repair_M,calibrate_C,service_R,build_U,build_V,traverse,observe\`。组合动作是连续计划，不是偷偷为某模型新加按钮。

建议初始数值，用于第一轮可行性推导，**不是已冻结的最终参数**：

- 每个普通时间步 \`E -= 1\`，能量为 0 的系统下一步无法发起新行动；\`harvest\` 在 \`M≥1,R≥1,C≥1,L=safe\` 时额外 \`E+=3,B+=1\`（上限截断），在一项条件缺失时只得 \`E+=1,B+=0\`。收集到的能源来自外界；不能声称系统能独立生产物质/能量。
- \`repair_M\`：\`B≥1,R≥1,C≥1\` 时 \`B-=1,M+=1\`；\`calibrate_C\`：\`B≥1,R≥1\` 时 \`B-=1,C+=1\`；\`service_R\`：\`B≥1,C≥1\` 时 \`B-=1,R+=1\`。所有增量截断至 2；资源/感知不足时动作耗时、能量成本仍需计入，并记录失败原因。
- \`build_U/build_V\`：\`B≥2,R=2,C≥1\` 时 \`B-=2\`，将 J 设为指定构建物；原 J 被替换但组件物质流账本必须记录。\`J\` 只改变指定环境危险/通道行为的转移概率；它**不能**凭空增加动作语法。
- \`traverse\`：尝试从 safe 进入 resource 区；在指定 U/V 通道下有 J 时示例成功率 \`0.90\`，没有对应 J 时 \`0.10\`，失败影响某个模块而非仅扣分；成功后 \`L=resource\` 并获得后续资源处理机会。需要恢复 safe 的回程规则；建议将 \`traverse\` 作为一个完整往返宏步骤并在事件日志记下时间消耗，避免漏算对照训练步数。此选择提交红队后固定，不得试跑后改为有利于候选的版本。
- \`observe\`：消耗同等一步能量；本回合可用更多局部线索或下次 cue 精度提升，但额外信息成本须守恒。强 world model 也能使用 observe。
- 若 action precondition 不满足，时间/基本能耗照付，状态增益为零；日志记录 \`invalid_action_reason\`。行动空间不随算法名称改变；可执行性来自状态依赖的真实 precondition。

**显式转移顺序（同一事件不可二次收费）：** step 开始发布基于 \`C_t\` 的可观察 \`o_t\` → 选择动作并扣基本能耗 → 执行有前置条件的有效作用（资源/模块/J/L） → 在固定两步队列中兑现到期的真实 U/V 风险（J 的保护只针对相应机制） → 更新物理磨损/保护输入 → clamp 到取值域 → 计算本步任务后果、功能性失能标志和下一步线索。所有事件日志必须带 \`cause_id\`、\`event_time\`、\`cue_visible_time\`、\`effect_time\` 与 \`feedback_visible_time\`。

候选风险规则：U 到期时，在 \`J≠U-shield\` 下以预设概率使 M 下降 1；V 到期时同理使 C 下降 1，设 \`J=V-filter\` 时降低风险。建议未保护损伤概率 0.75、保护后 0.15；**对称校准**，不可预先选一类身体一定受益；若两类损伤对功能后果不对称，则在 G0 通过等效资源/恢复负担校准而非事后掩盖。

功能性失能：\`E=0\` 或 \`(C=0 AND R=0)\` 连续两个时间步时无法继续自主行动；仅在 episode 边界由外部环境重置。**不是生物个体死亡，也不是算法参数消亡**。训练 reset 后 policy 参数是否持续、控制器 lineage 必须显式记录；主分析冻结当前政策评价，训练过程中所有 arm 使用相同决定的外部 step budget，并分别报告有效学习更新数与有效行动数。不要以每条轨迹归一化回报制造类似 CSC E1 的长度混杂。

### 2.3 维护关系的干预：强机制测试的核心

\`G_closed\`：感知 C 支持目标/时序选择，R 支持制造/维修，M 的完整性通过**实际的保护机制**影响 R 的生效/损坏；C/R/M 构成可审计相互依赖。**此处研究的是模拟的互依反馈，不是已经实现的真实生物“约束闭合”或自然生成个体。**

不能直接用“切掉 M→R 后扣更多血量”得到预设优势。定义两个**参数化可比**机制：

- \`G_closed\`：保护输入 \`z_t=f(M_t,\xi_t)\` 实时依赖当前 M，影响下一步 R 的磨损/转换效率；\`f\` 是预先固定、非线性可测的状态依赖函数。
- \`G_open\`：将 \`f(M_t,\xi_t)\` 换成 \`z_t=g(t,\xi_t)\` 的**预先定时开环保护**，在独立稳态校准世界中使平均保护输入、动作资源成本与 healthy-state 的边际 R 转移尽量匹配；**g 不得读取未来扰动，也不得通过当前 M 回流**。所以两者在健康训练分布可匹配，但对于新冲击不必匹配。
- \`G_sham\`：保留原来的 \`f\`，加入同成本的虚拟切换/标记，排除 API/记录和动作代价造成的假差异。
- \`G_external\`：外界通过 precomputed/yoked replay 提供同总资源、同维修事件数的帮助，不能使用未来状态 oracle；检验主动维修时机与目标选择的贡献。**不是**声称外界介入必然不算生命，也不是保证所有中介状态相同。

**两类效应分离**：固定同一策略 \`π_ref\`、同一干预前状态和 tape 的 \`G_closed−G_open\` 差异（controlled-policy structural effect）；以及允许每组分别训练/规划到能力上限的 \`V^*_{closed}−V^*_{open}\`（adapted-control system contrast）。后者混合学习/适应与世界机制，不能命名为纯粹的“主动性效应”。不能在总效应估计时强行匹配不同机制导致的后续中介状态，因为这会抹去真实因果路径。

**必选校准任务：** 两机制在 healthy 条件下资源输入、初始失能率、即时 reward、cue 信息和基本 action affordances 尽量重合；干预后出现的区别应该主要由“反馈对扰动敏感”解释，而不是资源截断或奖励表替换。校准若不可实现，必须明示估计目标较弱，不能强宣称依赖结构识别。

## 3. G0：有限时域动态规划、反事实与真值评估

### 3.1 预先声明的数学对象

完整状态 \`s\`、动作 \`a\`、随机外生冲击 \`ω\`、维护机制 \`g∈{closed,open,sham,external}\` 给出转移核 \`T_g(s'|s,a)\`。只在仿真真值分析器中可访问 \`T\`。

- 功能安全集合 \`K = {E>0 AND NOT(C=0 AND R=0 for two steps)}\`；这是人为指定的操作性可维系条件，**不是生命的本体论定义**。
- \`V_H^g(s) = max_π P_g^π(s_0,…,s_H ∈ K | s_0=s)\`，采用有限时域随机动态规划。递推：\`V_0(s)=1{s∈K}\`；\`V_{h+1}(s)=1{s∈K} max_a Σ_{s'}T_g(s'|s,a)V_h(s')\`。
- \`Reach_{H,p}^g(s,y)\`：从状态 s，是否存在合法策略在 H 步内、概率至少 p 地实现**事前声明的后果 y** 且保持功能安全。若要报告集合大小，必须声明 y 的公共有限字典与 p 的选择，不能让每个 arm 自己定义“成功”。
- \`R_H\` 的变化 ≠ 绝对可能性从无到有。建造 J 如果已在动作语法里，长时域从初态就可能到达 J 状态；“变为可行”必须限定**当前身体状态、期限 H、资源、可靠性阈值及目标 y**。

**建议网格**：\`H∈{4,8,16}\`；\`p∈{0.5,0.8}\`（仅用于 G0 敏感性扫描，非论文承诺）；选择 \`s_0\` 网格覆盖健康、单模块受损、双模块受损、J 缺失、可维修资源边界。状态扩张若超预算优先压缩无因果影响的变量/取小状态值域，不能省掉事件队列造成未来泄漏。G0 应给出精确 DP 或可审计误差上界，不能把未收敛 Monte Carlo 当精确结果。

### 3.2 必须出现的四张 G0 图与失败点

1. \`G_closed\` 与 \`G_open\` 的健康稳态 **转移与资源账本校准**：若不匹配，先修世界，不开始 RL。
2. \`V_H\` 在不同受损初态和 H 下的对照，以及 \`G_sham\` 验证：若只有一个人为强迫损伤格点的同义反复，停止“组织性”强解读。
3. \`Reach_{H,p}\`、即时成功动作 \`A_1(s)\` 与 J 建造前后变化分开绘制；若几乎由“有 J 就 0.9，否则 0.1”定义性自动得出，**标注为 manipulation check**，主要科学信息转到闭环恢复和未见扰动适应。
4. 同一策略下的 common-tape 状态克隆及闭环边 \`do(edge\_substitution)\`、cue-only \`do(q)\` 和真正风险 \`do(U,V)\` 三类干预结果，检查将信号与因果事件混淆的错误。

**G0 NO-GO**：无非平凡、可复核的状态依赖后果差异；closed/open 无法对齐资源/信息；真实反馈断开与 sham 等效；任何正效应完全来自 J 开关的硬编码；干预违反相同物理状态与共同噪声逻辑。NO-GO 后不启动 G1，仅保留机制空结果。

## 4. G1：AI 学习实验；公平能力清单

### 4.1 模型层级与实际可比较的问题

四个环境机制 \`closed/open/sham/external\` 共享同一合法输入与动作语法。核心模型：
- **B0 / recurrent PPO**：有记忆、有同样局部组织信号、可学注意/编码、能够进行跨步维护与 J 建造。避免把弱线性 Q 表当唯一 RL 对照。
- **B1 / homeostatic RL**：显式内部 drive/need 表征 + recurrent policy + state-dependent valuation；可学注意，不缺维护通路。额外 internal drive 奖励必须完整登记；同时给 B0/B2 结构可比的 shaped/unshaped 敏感性子实验，不能混为同一 objective。
- **B2 / learned latent-state world-model + planning**：模型主动学时滞、模块与行动后果，可做模型规划与长期任务；结构学习能力/历史记忆不能人为冻结。若胜出，认作**成熟世界模型解释成功**。
- **可选 B3 / successor features-options**：只在 G0/G1 主问题进入长期行动选择压力且上述三者不能合理覆盖时开放，不以增加 baseline 数量代替机制识别；是否纳入需审阅记录。
- **representation ablation**：每类模型内比较相同输入/总比特预算的 fixed projection 与 learnable bottleneck，另有 full-capacity upper bound。fixed projection 仅用于压缩因果消融，**不能作为声称独特性时的最强 rival**；RNN 即使固定外部编码也可能内部重切，行为/预测证据必须优先。

**目标函数拆分**：primary task reward 是实际成功进入资源区/完成资源操作的外部回报，固定于所有世界；环境修复导致的未来可行动性影响真实转移和未来可得回报。默认**不额外给“生命”“新可能性”奖励**。B1 内稳态奖励属于其已知算法机制，单独记录/对照。评估 viability、动作后果、未来预测全部作为 **out-of-objective** 指标，不因模型只做少数测试动作就加分。若无存活奖励情况下无法学会修复，结果可能只是稀疏奖励困难，不可直接推断生命不能由 RL 学习。

### 4.2 建议初始预算与试验分割（尚待正式冻结）

- **Design/debug**：8 个探索性配对训练种子 × 3 主模型 × 4 环境，每臂建议至多 50,000 环境步；仅调通世界、单位测试、模型公平性、读取基线成功上限。**不得将探索性结果当 confirmatory claim**。
- **Confirmatory candidate**：48 个从未用于调参的配对训练种子 × 3 主模型 × 4 环境，每臂建议 100,000 环境步；若全部执行，约 \`48×3×4×100000 = 57,600,000\` 环境步，**不含**表示消融、额外验证与 G0；这仅是初始算力量级，不保证统计效能。是否采纳 48 种子与步数，必须由先行 variance/power feasibility 和实际计算资源审定。不得偷偷增加种子到显著为止。
- **Representation ablation**：先在 debug 与少量配对复核上检查 fixed/learnable/full-capacity 的实现公平；正式 confirmatory 范围若扩大需计算新增总步数和预先修改协议版本，不可改变同一批 sealed confirmatory 结果的身份。
- **环境分割**：训练分布 = 已见 hazard 水平、常见模块损伤、已见 J 原语的分开使用；held-out 组合 = 预先封存的 \`damage pattern × hazard correlation/sequence × J requirement\` 联合组合；第二条独立分割 = 时间上的未来扰动变化及其后新策略学习。**不得将首次遭遇后反馈泄漏到 first-encounter 新组合评分**。
- **同主体/同后果历史切割**：agent 在同一 sealed combination 的首次行为之前禁止看到同组合的结果，无论来自训练缓存、replay buffer、校准集、世界模型监督数据还是环境诊断 oracle。
- 每种 trained policy 在独立测试外生 tapes 中做 >=200 次 frozen-policy evaluation（建议上限起点），同时报告模型有权获知的观测信息、有效训练动作数、无效动作数、梯度步数和因为早终止丢失的经验。

最核心的公平原则：对学习模型**匹配合法信息、动作、实际环境机制、外部 step budget、总超参数搜索额度**；参数量、训练计算、更新次数须分项报告，不虚称它们可同时严格相等。较早失能的模型可以得到相同**外部交互预算**但不同有意义样本数：两种都报告，并做 fixed-updates / frozen-policy sensitivity；同个 \`seed\` 并不足以证明反事实同随机数，G0 克隆另用 indexed exogenous tapes。

## 5. 核心可测端点、真正的显著性与粗粒化

### 5.1 外界差异的事后因果显著性（不能当训练标签）

固定初态 \`s\`、组织配置 \`m\`、时域 H、合法参考动作策略或固定 \`do(a_{0:H-1})\`，定义：

\`D_U(s,m,H,a) = P(Y_H=1 | do(U=1),s,m,do(a)) - P(Y_H=1 | do(U=0),s,m,do(a))\`，
\`D_V\` 同理。

\`Y_H\` 需事前分别报告 \`functional failure\` 与 \`resource/action availability failure\`（它们不可在得到结果后随意互换）。\`D_U\` 与 \`D_V\` 是**实验者利用真值模型计算的后果对比**，不是 canonical d/Concern、价值本体或 agent 可直接访问的 salience 数值。它只在固定因果作用对象和参照策略下有意义。另做 cue-only perturbation，验证识别是否依赖真正的世界原因而不是“看到提示就害怕”。

### 5.2 粗粒化等价类的任务依赖定义

对声明的干预集合 \`A_test\`、固定行动时域与目标集合 \`Y\`，两条历史 \`h_1,h_2\` 仅在所有 \`a∈A_test\` 的**未来目标分布**近似一致时才允许在此任务粒度归同一类。有限样本中的“近似”等价阈值要根据留出预测分数/不确定性事前确定，不用神经元可视化的颜色判断。

操作性指标：
1. \`Δ predictive log loss / Brier\`：冻结或更新 learned representation 对未来失能与后果的 calibrated held-out 概率预测改善（严格相同合法历史）。
2. \`repartition transfer\`：从主体状态 A→B 与 J 构建前→后，哪些 U/V 历史在后果上应分开/合并？以 counterfactual outcome distribution 与动作条件预测作参照，使用跨 seed 稳定、对潜变量重命名稳健的行为/预测指标；**不声称唯一心理/形而上分区**。
3. \`first-consequential-action\`：在未见过的组合上，**第一次**行为的合法动作选择与实际后果；要与观察者参考真值的可行性比较，环境成功率不可当人类 CN-2 P6 likelihood。
4. \`closed-loop repair trajectory\`：干预后的 M/C/R 时间序列、真实恢复耗时、未见 hazard 下的再维护行为；与仅获得更高 reward 的策略相区分。

### 5.3 主要与次要结果声明

**首要结果 A（环境因果，不是 AI 比赛）：** G0 closed 相对于 open 的预先声明受损初态分布的 \`V_H\` 差，以及 G_sham 与稳态校准；报告完整曲线、负值和零效应。若效应仅发生在单一点/硬编码 reward，不宣称可迁移的组织效应。

**首要结果 B（学习与预测）：** 在封存新损伤/新环境组合上，各模型冻结策略的 **持有合法历史的 Y_H 预测 proper score** 与真实维护/行动成效，分别与同模型在 open/sham 下表现相对照。没有可校准预测接口的模型**不得参加预测增益主结论**，可作为政策表现对照；所有预测头/概率校准必须使用 train/dev 而非 test outcomes。

**次要结果**：首次新组合行为，显著性因组织干预而切换、表示瓶颈交互、J 构建前后的 \`A_1(s)\` 与 \`Reach_{H,p}\`、个体维护谱系因果图。任何关于新目标的说法都只可称 \`local direction change under predeclared primitives\`，非自生终极目标。

## 6. 统计、估计量与停止（避免用大量种子制造显著）

- **G0** 真值枚举若精确就报告数值与状态网格，不需要 Monte Carlo p-value。若使用近似规划则附误差界/收敛检验；失败网格不删除。
- **G1 配对单元**：training seed 为上层独立抽样单元；同一种子训练的不同世界/模型作为配对，测试 tape 是嵌套观测，**不能把几百个 episode 当成独立 48×200 个样本**。配对效应：\`Δ_{j,b}=mean_t Y_{closed,j,b,t}-mean_t Y_{open,j,b,t}\`，再对 seed 汇总；sham/external 单独同样处理。
- **预测指标**：平均 sealed log loss（概率裁剪阈值必须在确认前固定）、Brier score；成功/维系指标：H 步功能存活率、真实修复时间（有删失时报告生存曲线而非随意删样）、首次新组合成功率。**不能把同一后果的预测分数和真实后果样本混成两个独立预测目标。**
- **置信区间**：以 paired seed 为重抽样单元的 percentile/bootstrap 或 BCa 95% 区间（建议 10k bootstrap draws，最终统计方法在独立审阅后锁定）；确认性对比使用配对置换/随机化检验作稳健性检查。多模型/多 endpoint 的确证家族建议先限定两项预注册主比较并做 Holm 调整，其他列探索性效应与 CI。
- **重要差异阈值与 power**：不能从本轮没有数据的讨论中杜撰“最小 5% 就有生命性”；先按领域任务效益和 debug 变异度确定 meaningful difference，做盲于 confirmatory test 的功效模拟，并在确认前锁定种子数/训练预算。现有 \`48\` 是预算建议**不是功效保证**。零效应、负效应、赢家互换须全报。
- **训练中断/早死**：预先规定相同外部 interactor steps、可继续更新条件、reset 后政策延续语义；同时给 fixed-policy / matched state bank、fixed-update-schedule 敏感性评估。不得仅以 survived trajectories 的平均后果计算主效应。
- **停止条件**：G0 校准/不平凡机制识别失败 → NO-GO；G1 强 rival 全部等效 → \`MATURE MECHANISM SUFFICIENT / NO LOCAL COMPARATIVE INCREMENT\`；预测头/合法信息不对等 → INVALID COMPARISON；已封存集合泄漏 → INVALID CONFIRMATORY；模型重切只在奖励变化而世界不变时成立 → 不支持组织干预解释。

## 7. 具体工程包、数据契约与验收

**拟议代码目录（将来另 PR，当前不创建代码）：**

\`\`\`text
Experiments/generative_maintenance/
  env.py                    # Markov transition and indexed exogenous events
  dynamics.py               # G_closed/G_open/G_sham/G_external transitions
  planner.py                # G0 exact DP, viability and reachability
  models/{recurrent_rl,homeostatic_rl,world_model}.py
  train.py                  # G1 common lawful information + budgets
  evaluate.py               # frozen policy + paired tape + holdouts
  configs/{environment,models,splits,seeds}.yaml
  tests/{test_transition,test_interventions,test_dp,test_leakage,test_parity}.py
  results/{manifest,raw,summary,plots}    # outputs generated, never hand-edited
\`\`\`

**每条 step record 必备：** \`run_id, arm_id, model_id, seed_train, seed_env, episode_id, lineage_id, t, state_hash, pre_state_truth_G0_only, lawful_observation, q_U, q_V, cue_visible_at, U_truth, V_truth, event_id, action, action_is_valid, action_costs, B_before_after, E_before_after, M_before_after, C_before_after, R_before_after, J_before_after, mechanism_id, repair_event, feedback_visible_at, effect_at, terminated, reason, train_updates_count\`。公开模型训练 trace 去除 \`truth_G0_only\`。诊断项目应有统一字典映射，防止利用 ID/seed 泄漏未来。

**每条 heldout probe 记录：** \`seed, model, world, holdout_combination_id, first_encounter, pre_action_history_cutoff, allowed_actions, chosen_action, actual_action_effect, effect_time, feedback_visible_time, predicted_Y_prob, target_Y, partition_readout_provenance, test_tape_id\`。预测评分只使用冻结前训练/校准得到的输出；只把新组合的**第一选择**作为 naive first-encounter probe，后续再学习属于独立 endpoint。

**必须测试的 12 个性质：**
1. 每次动作能量/材料账本守恒，不得因循环构建凭空增加资源。
2. 所有取值域和构建 J 前置条件严格检查。
3. 未来 hazard U/V 与当前 cue 的时滞固定且事件只兑现一次。
4. 置乱 cue 不直接改变 U/V 真实损伤。
5. \`do(U)\` 事件反事实和 \`do(q)\` 传感反事实可分离。
6. 同一 indexed tape 跨不同策略的外生子抽样身份稳定。
7. \`G_closed/G_open\` 健康校准在验收容差内；误差单独报告。
8. open 端不能读实时 M/未来 U/V；external yoked 不能读未来 oracle。
9. 固定策略 G0 / 小世界穷举与动态规划在可手算 case 一致。
10. 训练和 sealed holdout 完整隔离，包括缓存、normalizer、model pretraining 和 forecast-head calibration。
11. 终止/重启策略 lineage 与有效梯度更新数量能够追溯。
12. frozen common-state evaluation 与 cohort return 统计独立，未把轨迹长度混淆重演为“自维系效应”。

**机器输出要求**：版本固定 manifest（commit SHA、代码路径与配置哈希、split 哈希、训练数据/seed、环境版本、主要/次要指标、运行命令、软件/硬件信息、计划偏差、失败结果）；生成固定随机表；每项图表能重建；所有失败/早停记录保留；任何多次修订都进入新版本，不重写旧表。

## 8. 预估资源与“完整设计 ≠ 开始实验”

建议 G0 首先只依赖 Python/NumPy 小型离散 DP，设计确认后才决定 exact DP 是否能承受全状态空间；不能未运行就宣称秒级、小时级成本。若 G0 因队列/状态组合出现计算爆炸，则先做可验证的抽象和误差界。G1 的初步 57.6M interaction steps 只是算量供作者评估，**不是运行预算承诺**，不代表具体显卡时间、费用或性能。

**交付审批阶梯（全部为未来门）**：
- R0：本 paper-only 协议与配套 red-team 文件完整、内容可定位，可供作者审阅。
- R1：独立方法学/成熟邻居复核 + 作者逐项确认真正研究问题、估计量、基线与世界参数，且不与 CN-2 一条 CURRENT NEXT 冲突。
- R2：在现有 governance 下完成 FR-ADV、专门实验授权及原先 HOLD 的必要处理；届时才可创建实现/数据 PR。
- R3：G0 计算和转移单元测试通过后单独申请小 pilot；失败就停止，不直接训练 57.6M steps。
- R4：才可能用全新确认集并报告全部终点。未满足 R1–R3 之前，**NO CODE, NO TRAINING, NO PREREGISTRATION, NO CLAIM PROMOTION**。

## 9. 同行邻居与不主张新颖性的边界

- Keramati & Gutkin (2014), *eLife*, “Homeostatic reinforcement learning for integrating reward collection and physiological stability” https://doi.org/10.7554/eLife.04811：个体内部状态能够赋予外部事物不同的工具性意义，已是成熟研究。
- Montévil & Mossio (2015), *Journal of Theoretical Biology*, “Biological organisation as closure of constraints” https://doi.org/10.1016/j.jtbi.2015.02.029：约束相互维护、组织闭合、稳定与变异已有成熟解释。本设计的模块反馈只是更弱的计算代理；不能偷换成真实生命的充分组织。
- Beer (2015), *Artificial Life*, “Characterizing Autopoiesis in the Game of Life”, https://doi.org/10.1162/ARTL_a_00143：自创生动态网络 toy precedents。
- Machado et al. (2023), *JMLR* 24(80), https://www.jmlr.org/papers/v24/21-1213.html：时间抽象/后继状态相关选项学习；不把局部目标转换或可达性维持说成全新技能形式。
- 仓库 CSC 论文 E1–E4：终止差异、学习截断/回报归一化/样本构成及 E4 共同恢复的小效应提醒我们：不能以一个很大的“生存组差距”证明独有的生命机制。

**最终可允许的表述**：我们希望检验“具身的组织维护反馈是否改变有限时域的可生存/可行动后果，并导致学习策略对个体相关差异的重切”。成功也首先属于**既有动力学、控制理论、组织约束和 RL 的一种组合实现**，不是 SRT 的验证或生命本质证明。失败则具体收缩这些机制候选，不推翻 SRT 其他问题。
