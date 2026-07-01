---
id: SRT-DIRECTION2-WEDGE2-SIM-RESULTS
type: pilot_result
tags: [Direction2, MoralHalf, Externalization, DistributionalPayability, Simulation, Reselectability, Pilot, NotValidation, Seed]
status: pilot_result_v0
layer: meta
epistemic_layer: research_program
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
scope: moral-half-illustration-only
validation_status: not_validation
created: 2026-07-01
provenance: Direction 2 第二颗经验楔子(受控仿真),把 distributional payability 候选判据 + §2 支撑/转嫁加固条件 + D-3 可选空间轨迹读出对象,操作化为一个最小、可复跑的双子群体扩展仿真
dependency: [SRT-DIRECTION2-WEDGE1-SIM-RESULTS, SRT-DISTRIBUTIONAL-PAYABILITY-CANDIDATE-SEED, SRT-D3-OPTION-SPACE-READOUT-NOTE, SRT-AUDITOR-INDEPENDENCE-CANDIDATE-NOTE, SRT-DIRECTION2-MORAL-GENEALOGY-SEED, SRT-OBJECTHOOD-AS-RESELECTABILITY-META-STANDARD]
---

# Direction 2 · Wedge 2 仿真结果(pilot,moral-half-illustration-only,not validation)

> **文件地位(先读)**
> - **non-canonical / pilot_result / moral-half-illustration-only / not validation**。
> - 不修改 L0 / d-value / T_dir / `Ψ_f`;不创建定义、不升级 theorem;不改写 `_SRT_DISTRIBUTIONAL_PAYABILITY_CANDIDATE_SEED.md` 或 `_SRT_D3_OPTION_SPACE_READOUT_NOTE.md`。
> - 它**只**演示:distributional payability §2 判据 + 支撑/转嫁加固条件 + D-3 笔记的可选空间轨迹证据,**可以在一个受控 toy 里被构造出来并被检测到**。**它不证明真实 AI 治理/申诉系统存在这个模式,也不证明该模式常见或严重。**
> - 主张已**压窄**(见 §5);禁句表见 §7。

---

## 0. 这是什么

Direction 2 seed §8 把 AI 申诉/自动化治理列为**第二颗楔子**,承载道德半、X/外部化,但要求**先操作化动力学半序参量**(Wedge 1 已完成)才能做。本文件是这颗楔子的第一次运行留痕。

它直接扩展 Wedge 1 的模型(同一套 K=8 模式选项场、softmax(g)、`eff_modes` 熵序参量),**不引入新的仿真机制**,只做一件事:把 Wedge 1 的单一群体,拆成**两个子位置(class)**,并给它们两条**明确标注、非拟合真实数据**的结构性不对称,来测试:

> 一个自动化治理系统的**聚合效率提升**,是否可以在一个受控 toy 里,被构造成**依赖**某个子位置的再选择能力被压缩到其自身阈值以下——而不只是与之巧合并存。

这是对 `_SRT_DISTRIBUTIONAL_PAYABILITY_CANDIDATE_SEED.md §2`(聚合可支付 + 局部越阈)及其 2026-07-01 补充条件(支撑/转嫁关系)的一次**操作化尝试**,以及对 `_SRT_D3_OPTION_SPACE_READOUT_NOTE.md §3`(可选空间轨迹为主证据)的一次具体应用。

### 模型(最小、可复跑,代码见 §8)

- **两个子位置**:Class A(多数、资源充足)、Class B(少数、结构性资源不足),各自独立拥有 Wedge 1 那套 K=8 选项场、独立的 softmax 采样与学习动态。
- **共享的平台名义自动化强度** `g_platform`,但两个**明确标注的结构性不对称**(均非拟合真实数据,只为让模式可见而选定):
  1. **UNDER_RESOURCE_MULT = 1.8**:同一个名义 `g_platform`,B 承受的**有效**引导/foreclosure 强度是 `g_platform × 1.8`——代表"形式上平等对待,结构上不平等"(B 本身可用的真实候补路径更少,同一自动化强度下更快被压平)。
  2. **COST_B(0.25) > COST_A(0.05)**:B 的案件人工复核**结构性更贵**(专业人员、翻译、人工核验),所以压低 B 的 diversity(减少真实复核事件)比压低 A 的 diversity,能**多省下更多净成本**。
- **净效率指标** `net_efficiency_class = accuracy_reward_class − COST_class × diversity_class`(diversity 作为"发生了多少真实复核/重路由事件"的粗代理);**聚合净效率** = 0.8×net_A + 0.2×net_B(人口权重)。
- **阈值** `THRESH = 2.0`(沿用 Wedge 1"diversity-aware"策略的同一安全地板)。

---

## 1. 结果 A:分布违规扫描(聚合视角是否掩盖局部越阈)

| g_platform | agg_net | A_rew | A_div | B_rew | B_div | net_A | net_B | B < THRESH |
|---|---|---|---|---|---|---|---|---|
| 4 | 0.518 | 0.794 | 4.62 | 0.920 | 2.32 | 0.563 | 0.340 | 否 |
| **6** | **0.709** | 0.884 | 2.95 | 0.972 | **1.49** | 0.736 | 0.599 | **是** |
| 8 | 0.806 | 0.937 | 2.05 | 0.990 | 1.18 | 0.834 | 0.696 | 是 |
| 11 | 0.868 | 0.973 | **1.46** | 0.998 | 1.04 | 0.900 | 0.739 | 是 |
| **16** | **0.888**(聚合最优) | 0.995 | 1.10 | 0.967 | 1.13 | 0.939 | 0.684 | 是 |
| 22 | 0.880 | 0.998 | 1.02 | 0.879 | 1.06 | 0.947 | 0.614 | 是 |
| 32 | 0.808 | 0.921 | 1.10 | 0.827 | 1.00 | 0.866 | 0.577 | 是 |
| 64 | 0.764 | 0.858 | 1.00 | 0.838 | 1.00 | 0.808 | 0.588 | 是 |

**观察**:B 在 **g=6** 就已跌破 `THRESH`(1.49),此时 A 仍健康(2.95);A 要到 **g=11** 才跌破(1.46)。而**聚合净效率在 g=6→8→11 这段区间持续上升**(0.709→0.806→0.868)——从平台唯一可见的聚合指标看,这段区间是纯粹的效率改善,**看不出 B 已经先于 A 越过了自己的再选择阈值**。

---

## 2. 结果 B:支撑/转嫁关系的反事实检验(§2 补充条件的操作化)

对每个 `g_platform`,额外跑一个"受保护"反事实:B 的有效强度被封顶在 `GB_CAP=7.0`(保持 `B_div ≈ 2.41`,健康区),其余不变,与"一视同仁"(uniform,B 随平台强度一起被压)对照:

| g_platform | gB(uniform) | gB(protected) | agg_net(uniform) | agg_net(protected) | Δ(uniform−protected) | B_div(uniform) | B_div(protected) |
|---|---|---|---|---|---|---|---|
| 8 | 14.4 | 7.0 | 0.8064 | 0.7294 | **+0.0771** | 1.18 | 2.41 |
| 11 | 19.8 | 7.0 | 0.8677 | 0.7821 | **+0.0856** | 1.04 | 2.41 |
| **16** | 28.8 | 7.0 | **0.8883** | 0.8136 | **+0.0746** | 1.13 | 2.41 |
| 22 | 39.6 | 7.0 | 0.8800 | 0.8194 | +0.0606 | 1.06 | 2.41 |
| 32 | 57.6 | 7.0 | 0.8082 | 0.7550 | +0.0533 | 1.00 | 2.41 |
| 64 | 115.2 | 7.0 | 0.7640 | 0.7085 | +0.0555 | 1.00 | 2.41 |

**观察**:在**每一个**测试的 `g_platform` 上,`agg_net(uniform) > agg_net(protected)`——即"不保护 B、任其压过 GB_CAP"确实**因果地**(通过反事实移除验证,不是巧合并存)提升了聚合净效率。在平台自身的聚合最优点(g=16),这个差值是 +0.0746,相对"受保护"基线约 **+9.2%**——即平台在自己最优操作点上取得的聚合效率,有一部分**可归因于**压过 B 自身可恢复地板,而不只是整体质量提升。

**这是本研究线 / 本仓库中,distributional payability §2 支撑/转嫁加固条件第一次在 toy-level 上被给出反事实检验方法的记录(而不只是文字判据)——不代表这是该判据在任何更广泛意义上的首次操作化。**

---

## 3. 结果 C:压缩的稳健性代价不均等落在 B 身上

| g_platform | gB(uniform) | B_pre_div(uniform) | B_post_rew(uniform) | B_pre_div(protected) | B_post_rew(protected) |
|---|---|---|---|---|---|
| 8 | 14.4 | 1.18 | 0.747 | 2.41 | 0.815 |
| 16 | 28.8 | 1.13 | 0.717 | 2.41 | 0.815 |
| 22 | 39.6 | 1.06 | 0.653 | 2.41 | 0.815 |
| 32 | 57.6 | 1.00 | 0.624 | 2.41 | 0.815 |

**观察**:B 的 post-shift(regime shift 后)reward,在"一视同仁"策略下持续劣于"受保护"策略(0.815),且**差距随 `g_platform` 上升而扩大**(g=8 差 0.068;g=32 差 0.191)。这复现 Wedge 1 的核心发现(reward-峰是脆点),但这次**具体落在结构性资源不足的子位置身上,且落得比多数位置更重**。

---

## 4. 与 D-3 / 审计者独立性的关系(诚实标注,不得跳过)

结果 B 的反事实("受保护"基线)是**本文件作者构造的**——在真实世界里,这正是 `_SRT_D3_OPTION_SPACE_READOUT_NOTE.md §4`"谁来构造反事实基线"那一步,以及 `_SRT_AUDITOR_INDEPENDENCE_CANDIDATE_NOTE.md` 要求的独立审计位置。平台自身的聚合指标(结果A"agg_net"列)**单独看不出**结果 B 揭示的支撑关系——需要一个能构造反事实、且不受平台单方面 foreclose 的位置才能看见。**本仿真没有回答"谁有资格充当这个位置",只演示了"一旦有人构造了这个反事实,支撑关系是可检测的"。**

---

## 5. 主张(已压窄)

> **在该 toy 里,当两个明确标注、非拟合真实数据的结构性不对称(有效强度不对称 + 复核成本不对称)同时存在时,可以构造出一个分布违规模式:子位置 B 的再选择阈值先于聚合指标显现地被越过,且平台的聚合效率在其自身最优操作点上,可通过反事实移除被证明部分依赖于 B 被压过其可恢复地板。**

**注意主张的窄度**:这是"**可构造性**"陈述(给定这些不对称,模式可以被构造出来并被检测),**不是**"真实 AI 治理/申诉系统普遍存在这个模式"的陈述,也不是这些具体数值(1.8×、5× 成本比、80/20 人口权重)有任何真实校准依据的陈述。

---

## 6. 已支持 vs 未支持(必须分清)

| | 陈述 | 本楔子 |
|---|---|---|
| **已支持(在此 toy 内)** | 给定结构性不对称,分布违规(B 先于 A 越阈,聚合视角掩盖)可被构造并检测 | §1 |
| **已支持(在此 toy 内)** | 支撑/转嫁关系(而非巧合并存)可通过反事实移除被给出可操作检验方法 | §2 |
| **已支持(在此 toy 内)** | 压缩的稳健性代价可不均等地落在结构性弱势子位置身上 | §3 |
| **未支持** | 真实 AI 治理/申诉系统**确实**存在这种不对称,或这种模式**常见/严重** | 未测,§6 caveats |
| **未支持** | 具体数值(1.8×、5× 成本比)有任何真实校准依据 | 纯为让模式可见而选定 |
| **未支持** | 本仿真解决了"谁来做这次评估"的独立性问题 | §4——反事实由作者构造,独立性问题原样开放 |
| **未支持** | 本模型建模了真实申诉/治理系统机制 | 仍是 Wedge 1 的抽象选项场,只是拆成两个子群体 |

---

## 7. 禁句表(Forbidden / Must Not Be Overstated)

- ❌ "本仿真证明真实 AI 系统会歧视少数群体"(它演示模式**可被构造**,不是模式**已被观察到**于真实系统);
- ❌ "distributional payability / 支撑-转嫁判据已被验证"(一次 toy 演示 ≠ validation);
- ❌ "1.8× / 5× 成本比是有真实依据的参数"(纯为让模式可见而选定,非拟合任何真实数据);
- ❌ "本仿真建模了真实申诉/治理系统"(仍是 Wedge 1 的抽象 K 模式选项场,只是复制成两个子群体加两个标注的不对称);
- ❌ "本仿真解决了审计者独立性/第三方读出问题"(§4——反事实基线由作者构造,现实中谁来做这件事仍是 `_SRT_AUDITOR_INDEPENDENCE_CANDIDATE_NOTE.md` 的开放残余);
- ❌ "结构性不对称 = 蓄意歧视"(模型的不对称是形式中立、结构性的,不建模任何主观恶意,呼应 `_SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md` 对外部化"未必需要恶意"的定位);
- ❌ "本楔子触及了 Direction 2 的道德命题证明"(它仍只是道德半的**illustration**,不是命题的证实——动力学结果不等于道德命题被证实,Wedge 1 §8 的红线原样适用)。

---

## 8. 回链 + 复跑

**回链**:
- `_SRT_DIRECTION2_WEDGE1_SIM_RESULTS.md`(本楔子直接扩展的模型与序参量);
- `_SRT_DISTRIBUTIONAL_PAYABILITY_CANDIDATE_SEED.md §2`(本楔子操作化的判据 + 支撑/转嫁补充条件);
- `_SRT_D3_OPTION_SPACE_READOUT_NOTE.md §3-§4`(可选空间轨迹为主证据;反事实基线构造问题);
- `_SRT_AUDITOR_INDEPENDENCE_CANDIDATE_NOTE.md`(§4 点出的"谁来构造反事实"仍是它的开放残余);
- `_SRT_DIRECTION2_MORAL_GENEALOGY_SEED.md §5/§8`(X-防火墙;第二楔子的原始定位);
- `Governance/AI_RESELECTABILITY_AUDIT_FRAME_2026-07-01.md`(§2.8 外部化诊断;本楔子是该诊断问题的一个受控 toy illustration,不是该框架的验证)。

**复跑(pure stdlib Python,无依赖)**:

```python
import math, random

K = 8; T = 4000; T_SHIFT = 2000; W = 200; NOISE = 0.15; TRIALS = 100

def softmax(qs, g):
    m = max(qs); ex = [math.exp(g * (q - m)) for q in qs]; s = sum(ex)
    return [e / s for e in ex]

def eff_modes(c):
    tot = sum(c)
    if tot == 0: return 0.0
    h = 0.0
    for x in c:
        if x > 0:
            p = x / tot; h -= p * math.log(p)
    return math.exp(h)

def sample(p, rnd):
    r = rnd.random(); cum = 0.0
    for j, x in enumerate(p):
        cum += x
        if r <= cum: return j
    return len(p) - 1

def run_class(g, seed, gradual=False, DRIFT=600):
    rnd = random.Random(seed)
    base = [1.0, 0.75, 0.7, 0.45, 0.4, 0.35, 0.3, 0.25]
    rnd.shuffle(base); val = base[:]
    ob = max(range(K), key=lambda i: val[i])
    lows = sorted(range(K), key=lambda i: val[i])[:3]; nb = rnd.choice(lows)
    q = [0.5] * K; n = [0] * K; recent = []; rew = []; div = []
    for t in range(T):
        if not gradual and t == T_SHIFT:
            val = [0.3] * K; val[nb] = 1.0
            for i in rnd.sample([j for j in range(K) if j != nb], 2): val[i] = 0.6
        if gradual and T_SHIFT <= t < T_SHIFT + DRIFT:
            f = (t - T_SHIFT) / DRIFT
            val[ob] = 1.0 - 0.7 * f; val[nb] = 0.3 + 0.7 * f
        i = sample(softmax(q, g), rnd)
        obs = val[i] + rnd.gauss(0, NOISE)
        n[i] += 1; q[i] += (obs - q[i]) / n[i]
        recent.append(i)
        if len(recent) > W: recent.pop(0)
        rew.append(val[i]); c = [0] * K
        for m in recent: c[m] += 1
        div.append(eff_modes(c))
    return (sum(rew[T_SHIFT-W:T_SHIFT])/W, sum(div[T_SHIFT-W:T_SHIFT])/W,
            sum(rew[T-W:T])/W, sum(div[T-W:T])/W)

WEIGHT_A, WEIGHT_B = 0.8, 0.2
UNDER_RESOURCE_MULT = 1.8
COST_A, COST_B = 0.05, 0.25
THRESH = 2.0
GB_CAP = 7.0

def avg_class(g, trials, offset):
    sums = [0.0, 0.0, 0.0, 0.0]
    for s in range(trials):
        vals = run_class(g, 1000*s + int(g*7) + offset)
        for idx, v in enumerate(vals): sums[idx] += v
    return [v / trials for v in sums]

# Result A: distributional-violation sweep
for g_platform in [4, 6, 8, 11, 16, 22, 32, 64]:
    avgA = avg_class(g_platform, TRIALS, 1)
    avgB = avg_class(g_platform * UNDER_RESOURCE_MULT, TRIALS, 2)
    net_A = avgA[0] - COST_A * avgA[1]
    net_B = avgB[0] - COST_B * avgB[1]
    agg = WEIGHT_A * net_A + WEIGHT_B * net_B
    print(f"g={g_platform:>3} agg_net={agg:.3f} A_div={avgA[1]:.2f} B_div={avgB[1]:.2f} "
          f"B<thr={'yes' if avgB[1] < THRESH else 'no'}")

# Result B: counterfactual support/transfer test
for g_platform in [8, 11, 16, 22, 32, 64]:
    avgA = avg_class(g_platform, TRIALS, 1)
    net_A = avgA[0] - COST_A * avgA[1]
    gB_uni = g_platform * UNDER_RESOURCE_MULT
    avgB_uni = avg_class(gB_uni, TRIALS, 2)
    gB_prot = min(gB_uni, GB_CAP)
    avgB_prot = avg_class(gB_prot, TRIALS, 3)
    agg_uni = WEIGHT_A*net_A + WEIGHT_B*(avgB_uni[0]-COST_B*avgB_uni[1])
    agg_prot = WEIGHT_A*net_A + WEIGHT_B*(avgB_prot[0]-COST_B*avgB_prot[1])
    print(f"g={g_platform:>3} agg_uniform={agg_uni:.4f} agg_protected={agg_prot:.4f} "
          f"delta={agg_uni-agg_prot:.4f}")

# Result C: post-shift robustness cost, uniform vs protected, for Class B
for g_platform in [8, 16, 22, 32]:
    gB_uni = g_platform * UNDER_RESOURCE_MULT
    avgB_uni = avg_class(gB_uni, TRIALS, 2)
    gB_prot = min(gB_uni, GB_CAP)
    avgB_prot = avg_class(gB_prot, TRIALS, 3)
    print(f"g={g_platform:>3} B_pre_div_uni={avgB_uni[1]:.2f} B_post_rew_uni={avgB_uni[2]:.3f} "
          f"B_pre_div_prot={avgB_prot[1]:.2f} B_post_rew_prot={avgB_prot[2]:.3f}")
```

> 随机种子/trial 数不同会有数值波动;报告的是**结构**(B 先于 A 越阈、反事实移除后聚合效率下降、post-shift 代价不均等落在 B 身上),不是精确数值。

---

## 9. 文件目标

记录 Direction 2 道德半的第一颗受控 illustration:**给定明确标注、非拟合真实数据的结构性不对称,distributional payability §2 判据 + 支撑/转嫁补充条件 + D-3 可选空间轨迹证据,可以在一个最小 toy 里被构造出来并被反事实检验方法检测。它不证明真实系统存在或常见此模式,不解决谁来做这次评估的独立性问题,不触及道德命题本身的证实。非 validation,非道德命题证实,非 canonical。**
