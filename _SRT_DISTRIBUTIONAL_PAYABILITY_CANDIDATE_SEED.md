---
id: SRT-DISTRIBUTIONAL-PAYABILITY-CANDIDATE-SEED
type: research_seed
tags: [PsiF, Externalization, Payability, MoralGenealogy, Direction2, Seed]
status: seed_v0
layer: meta
epistemic_layer: research_program
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
created: 2026-07-01
provenance: 从 `_SRT_DIRECTION2_PHASE_TRANSITION_DUEL.md` §8.3(第4轮,Ψ_f 多主体校正后的缺口重定位)提炼出的独立候选原则
candidate_promotion_target: none (残余可喂 Core/SRT_OPEN_TENSIONS.md §2/§5;定义不可)
dependency: [SRT-PSI-F-CANONICAL, SRT-T-DIR-CANONICAL, SRT-D-VALUE-CANONICAL, SRT-DIRECTION2-PHASE-TRANSITION-DUEL, SRT-CLOSURE-BOUNDARY-CONVERGENCE-RECORD, SRT-OPEN-TENSIONS, SRT-DIRECTION2-MORAL-GENEALOGY-SEED, SRT-D3-OPTION-SPACE-READOUT-NOTE]
---

# Distributional Payability —— 聚合可支付性之下的子位置外部化候选判据

> **文件地位(先读)**
> - **non-canonical research seed**。不修改 `Ψ_f` canonical 定义,不新增 core theorem,不自动写入 `Core/SRT_OPEN_TENSIONS.md`。
> - 目标**不是**证明这条原则,是把 `_SRT_DIRECTION2_PHASE_TRANSITION_DUEL.md` §8.3 里一句话级别的候选定义,展开成一个**可攻击**的独立单元:写清它假设了什么、它没有解决什么、它在哪些既有残余之上才成立。
> - **禁句表见 §9,起草前请先读。**

---

## 0. 一句话

> canon 的 `Ψ_f` 可支付性判据在**聚合/整体层面**评估("系统在承担这笔 Ψ_f 的同时,仍能维持自身闭包";`_SRT_PSI_F_CANONICAL.md:201`)。当"系统"是一个多主体现实切片时(canon 已允许此读法,line 206:"社会层:制度/改革摩擦不致使系统解体"),**整体可支付不蕴含内部各子位置都可支付**。这条缺口本身可以被写成一个候选判据——但它是一个**新结构**,不是 `Ψ_f` 既有定义的展开。

---

## 1. 缺口来源

`_SRT_DIRECTION2_PHASE_TRANSITION_DUEL.md` §7-§8 在第3-4轮攻防中确认:

1. canon 的 `Ψ_f` 从来不是单主体局部负荷,而是"现实切片"(可为多主体协作结构)的锚定/维持/协调负担(Def-Ψ-1,line 68-71;line 206)。
2. 可支付性判据(line 201)只问**整体**闭包撑没撑住,没有按子位置分解的判据。
3. 这给出一个精确、可核查的外部化(X)候选定义空间,但这个空间**canon 目前是空的**——没有任何条款规定"整体可支付、子位置不可支付"这种分布状态该如何被识别或该不该被算作外部化。

本文件把这个空间填成一条候选原则,并逐条列出它还欠什么。

---

## 2. 候选原则(正式表述,proposal)

> **Distributional Payability(候选,非 canonical)**
> 设多主体现实切片 `S` 由子位置集合 `{P_i}` 构成。`S` 的聚合可支付性(按 `_SRT_PSI_F_CANONICAL.md` Def-Ψ-1 / line 201)成立,是"`S` 的 `Ψ_f` 负担被公平承担"的**必要非充分**条件。
>
> 一个分布构成**外部化(X)**,当且仅当:
> 1. `S` 的聚合可支付性成立(`S` 整体闭包、身份连续性、后续选择能力撑住);且
> 2. 存在某个 `P_i`,其**局部承担份额**——若将 `P_i` 的闭包独立地拿出来评估——已越过 `P_i` **自身**的不可支付/闭包崩溃阈值。

直觉版:**"整体没事"不能免除"局部有没有事"这个追问;外部化正是靠聚合读数把这个追问挡住的那种分布。**

### 补充条件(候选,2026-07-01)

> 仅满足上述条件1、2(聚合可支付 + 某 `P_i` 局部越阈)尚**不足够**判定为外部化;还应要求两者之间存在**可证明的支撑/转嫁关系**——即 `P_i` 的局部压缩**正在支撑** `S` 的整体稳定或某受益位置的稳定,而不只是两个事实巧合并存。
>
> 此条件由 `_SRT_D3_OPTION_SPACE_READOUT_NOTE.md §5` 提出,**尚未形式化**(何时算"支撑"而非"巧合并存"没有给出可核查标准),暂列为候选补充,不改变上述条件1、2 的既有地位,不升级本文件的 canonical 状态。

---

## 3. 前提条件(本原则不解决的东西,建立在其上而非替代)

这条候选原则**依赖**、而不是**解决**两笔已知残余(继承自 `_SRT_DIRECTION2_PHASE_TRANSITION_DUEL.md` §10 债1/债2):

1. **哪些算 `P_i`(闭包边界)**:子位置的个体化本身就是 `_SRT_CLOSURE_BOUNDARY_CONVERGENCE_RECORD.md` 处理的不可约原子("算谁的场、算到多远")。本原则**不提供**新的个体化判据,只是在"`P_i` 已被承认为一个位置"之后才能被问。
2. **`P_i` 必须已是厚位置(d>0),不是薄 ε 地板**:一个零关切的构成性方向(ε 地板)没有"自身的不可支付阈值"可言——阈值预设了"有什么东西真的对 `P_i` 重要"(`_SRT_DIRECTION2_PHASE_TRANSITION_DUEL.md` §5 精度闸;L0 五条否定第5条)。所以本原则的适用域**从一开始就排除**债1(0→1,P0-04)尚未解决的位置——它不是债1的替代方案,是在债1被(在别处)还清之后才能启动的下一步判据。

**因此:本原则本身不新增"谁算数"的判据,只在"谁算数"已被给定的条件下,追问"聚合读数是否正在掩盖局部崩溃"。**

---

## 4. 未解决的技术缺口(不得跳过,不得默认已解决)

### 4.1 可分解性问题

`Ψ_f` 在 canon 里不是一个天然可加/可分解的量。Fisher-Rao 几何投影(`_SRT_PSI_F_CANONICAL.md §Def-Ψ-2`)是**整个**参数化路径上的局部二阶代价结构;把"整体 `Ψ_f`"拆成"`P_i` 的份额",需要假设某种可加性或边际结构——**canon 没有提供这个假设,也没有否定它**。在这个假设被给出并证明合理之前,"`P_i` 的局部份额"这个说法本身是**未定义的**,只是一个占位符。

**禁止**把这条原则读成"`Ψ_f` 已经支持按位置分解"——它**目前不支持**,分解规则是本候选原则额外需要、且尚未提供的部分。

### 4.2 阈值的反事实基线问题

判据第2条要求"若将 `P_i` 的闭包**独立地**拿出来评估",其阈值才有意义。但很多子位置(尤其是制度/角色性的位置)可能**不存在**一个有意义的"独立于协作结构的基线状态"——一个角色如果从来只作为协作结构的一部分而存在,"如果它独立存在,它的阈值会是多少"这个反事实可能是病态的。

这与 `Core/SRT_OPEN_TENSIONS.md §5`(Stable ISP Entry)、`Core_Law/SRT_Individuation.md` 处理的 **σ_sub 入场阈值**是同一类问题的镜像:那里问"一个过程何时算作一个稳定 ISP、有资格被个体化",这里问"一个已被承认的位置,其'独立基线'阈值该如何锚定"。**两者都未解**,本文件不新增解法,只指出结构同构。

### 4.3 检测问题(D-3 仍未解除)

即使 §2 的判据在概念上成立,**读出**"`P_i` 的局部份额是否已越阈"需要某种方向性/可见性读数——自然候选是 `T_dir`。但 `_SRT_T_DIR_CANONICAL.md` §1(line 42)的核心命题是"价值内嵌于选择本身,不是缺席,而是被遮蔽的";受益于某个分布的位置,其 `T_dir` 读数按 canon 自身定义最可能已经退化(闭包边界记录 D-3 killer)。

**本文件不提供检测机制**,也不得被引用为"检测问题已解决"。检测仍然是 `_SRT_CLOSURE_BOUNDARY_CONVERGENCE_RECORD.md` route-C(跨位置、经反遮蔽扰动检验的收敛)的适用范围,且 route-C 本身可错论、不终结(该记录 E-1/E-2)。

**2026-07-01 更新**:检测对象的进一步重定位(从主观/生理信号,重定位为 `P_i` 的可选空间轨迹)已被记录于独立文件 `_SRT_D3_OPTION_SPACE_READOUT_NOTE.md`。该文件把检测问题精确到"反事实基线构造 + 归因"这两个具体动作,但**同样未解除 D-3**——本节原有结论(检测仍是 route-C 的可错论适用范围)保持不变。

---

## 5. 与 d-value / RCI 的关系(防混淆)

- 本原则**不是** d-value 的重定义。`P_i` 是否有"自身阈值"这件事本身就预设了 `P_i` 的 d>0(见 §3.2);本原则在 d 已经存在之后才起作用。
- 与 `_SRT_DIRECTION2_MORAL_GENEALOGY_SEED.md` §6 的 RCI-X 分量(externalization,标注"无扩散对应项")相印证:本文件是对那个未覆盖分量的一次**独立**尝试性展开,不是它的证明或完成。RCI-X 仍然是未覆盖的。

---

## 6. 与既有文件关系

- 候选来源:`_SRT_DIRECTION2_PHASE_TRANSITION_DUEL.md §8.3`(第4轮)。
- 前提未解残余:`_SRT_CLOSURE_BOUNDARY_CONVERGENCE_RECORD.md`(闭包边界、D-3、route-C)、`Core/SRT_OPEN_TENSIONS.md §1`(d-proxy)、`§5`(ISP 入场阈值,反事实基线问题的镜像)、`§7`(P0-04,债1)。
- 与 `_SRT_DIRECTION2_MORAL_GENEALOGY_SEED.md §5/§6`(X-防火墙、RCI-X 无对应)一致,不得混说。
- `_SRT_D3_OPTION_SPACE_READOUT_NOTE.md`:D-3 检测对象重定位的独立后续笔记(§2 补充条件、§4.3 更新均来自该文件),两者互为印证,该文件不改写本 seed 的主判据。
- **不改写** `_SRT_PSI_F_CANONICAL.md`、`_SRT_T_DIR_CANONICAL.md`、`_SRT_D_VALUE_CANONICAL.md`。

---

## 7. 禁句表(Must Not Be Overstated)

- ❌ "`Ψ_f` 已经支持按位置分解"(§4.1 明确否定,分解假设本身未给出);
- ❌ "本原则解决了闭包边界问题"(§3.1——原则依赖闭包边界,不解决它);
- ❌ "本原则适用于薄 ε 地板位置"(§3.2——适用域从一开始排除零关切位置);
- ❌ "本原则提供了检测外部化的可靠机制"(§4.3——检测问题原样开放,D-3 未解除);
- ❌ "distributional payability = canonical `Ψ_f` 的一部分"(它是本文件提出的新结构,proposal);
- ❌ "本原则关闭了 `_SRT_DIRECTION2_PHASE_TRANSITION_DUEL.md` 的残余"(它把残余精确化,没有关闭);
- ❌ "支撑/转嫁关系(§2 补充条件)已被形式化或验证"(它目前只是文字描述,可核查标准未给出,见 §8.5)。

---

## 8. 开放残余

1. **可分解性假设**:`Ψ_f` 按子位置的分解规则(可加性?边际结构?)完全未给出,是本原则能否成立的前提性技术缺口。
2. **反事实基线**:角色性/制度性子位置"独立评估阈值"是否总是良定义,未知;与 ISP 入场阈值(σ_sub)结构同构但未合并处理。
3. **检测机制**:如何在不依赖既得利益位置自身 `T_dir` 读数的情况下,读出局部越阈——未解,继承 route-C 的可错论、不终结性质;检测对象已被重定位(见 `_SRT_D3_OPTION_SPACE_READOUT_NOTE.md`),但反事实基线构造、归因、第三方独立性仍开放。
4. **与 RCI-X 的关系**:本原则是否能成为 RCI-X 分量的操作化入口,还是应保持独立——未决定,留待下一轮。
5. **支撑/转嫁关系的形式化**:§2 补充条件目前只是文字描述,"何时算支撑而非巧合并存"没有可核查标准(见 `_SRT_D3_OPTION_SPACE_READOUT_NOTE.md §6.5`)。

---

## 9. 文件目标(防误用)

本文件把 `_SRT_DIRECTION2_PHASE_TRANSITION_DUEL.md` 第4轮产出的一句候选定义,展开成一个可被独立攻击的最小单元:一条判据(§2)+ 两条前提性依赖(§3)+ 两个未解技术缺口(§4)+ 一个未解检测问题(§4.3)。它不是 `Ψ_f` 的扩展定义,不是外部化的完成判据,不是道德执行问题的解决方案。任何"候选/proposal"措辞在被作者按 `Governance/SRT_EDIT_PROTOCOL.md` 采纳前,不得当 SRT 定论引用。
