---
id: SRT-DIRECTION2-WEDGE1-SIM-RESULTS
type: pilot_result
tags: [Direction2, DynamicsHalf, Simulation, Reselectability, Pilot, NotValidation, Seed]
status: pilot_result_v0
layer: meta
epistemic_layer: research_program
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
scope: dynamics-half-only
validation_status: not_validation
created: 2026-06-30
provenance: Direction 2 动力学半第一颗经验楔子(受控仿真)的留痕
dependency: [SRT-DIRECTION2-MORAL-GENEALOGY-SEED, SRT-OBJECTHOOD-AS-RESELECTABILITY-META-STANDARD, SRT-OPEN-TENSIONS]
---

# Direction 2 · Wedge 1 仿真结果(pilot,dynamics-half-only,not validation)

> **文件地位(先读)**
> - **non-canonical / pilot_result / dynamics-half-only / not validation**。
> - 不修改 L0 / d-value / T_dir;不创建定义、不升级 theorem。
> - 它**只**记录一个受控 toy 仿真的结果,用来探测 Direction 2 seed §7 的一个动力学半预测候选。**它不证明 Direction 2,也不触碰道德半。**
> - 主张已**压窄**(见 §4);禁句表见 §8。

---

## 0. 这是什么

Direction 2 seed §8 把"第一颗干净经验楔子"定为**受控仿真**:隔离 re-sampling 序参量,测"option-diversity 是否在结果指标_之前/之外_携带 robustness 信息"。本文件是这颗楔子的第一次运行留痕。

**模型(最小、可复跑,代码见 §9)**:一个 K=8 模式的多峰"选项场";一个 agent 以 softmax(inverse-temperature `g` = 引导/foreclosure 强度)在估值上采样、用运行均值学习各模式价值;在 t=2000 处发生一次 **regime shift**(一个原本低值的模式变为最优)——这是"未来 ≠ 当下"、即再选择之所以要紧的原因。
- **outcome 指标** = 平均 reward(效率);
- **序参量** = option-diversity = 最近窗口采样分布的有效模式数 `exp(entropy)`(= re-sampling capacity 的操作化);
- 度量:shift 前 reward / diversity、shift 后 reward、shift 后恢复比例。

---

## 1. 结果 A:参数扫描(突变 swap,100 trials/点)

| g (引导) | pre-reward | pre-diversity | post-reward | recovery frac |
|---|---|---|---|---|
| 4 | 0.789 | 4.63 | 0.638 | 0.00\* |
| 6 | 0.886 | 2.91 | 0.771 | 0.00\* |
| 8 | 0.938 | 2.03 | 0.841 | **0.86** |
| 11 | 0.974 | 1.46 | **0.851** | 0.85 |
| 16 | 0.995 | 1.08 | 0.784 | 0.63 |
| **22** | **0.999** | **1.01** | 0.753 | 0.56 |
| 32 | 0.906 | 1.12 | 0.763 | 0.50 |
| 64 | 0.844 | 1.00 | 0.596 | 0.25 |

\* 低 g 的 recovery=0 **不是锁死**,是"太探索、永远 exploit 不到 0.85 的门"——recovery 对照只在 g≥8 apples-to-apples。

**观察**:pre-reward 的 optimum(g=22,0.999)落在 **diversity 已坍缩(1.01)** 的区域,且其 post-shift reward(0.753)与存活(0.56)**劣于** g=8–11(post 0.84–0.85,存活 0.85–0.86)。

---

## 2. 结果 B:两策略对照(都在 shift _之前_选运营点)

| 策略 | 选中 g | pre-reward | pre-diversity | → post-reward | 存活 |
|---|---|---|---|---|---|
| reward-only(取 pre-reward 最大) | 22 | 0.999 | 1.01 | 0.753 | 0.56 |
| diversity-aware(diversity≥2 下取最大 reward) | 8 | 0.938 | 2.03 | **0.841** | **0.86** |

代价:diversity-aware 的 pre-reward −0.061(约 6%);收益:post-reward +0.088,存活 +30 个百分点。**reward-only 在决策时刻看不到这个差别——脆点(g=22)恰是 reward 最大点。**

---

## 3. 结果 C:稳健性 —— 渐变漂移(600 步,80 trials/点)

把扰动从突变 swap 换成 600 步线性漂移:

| g | pre-reward | pre-diversity | post-reward |
|---|---|---|---|
| 8 | 0.937 | 2.05 | **0.822** |
| 16 | 0.996 | 1.10 | 0.733 |
| **22** | **0.999** | **1.01** | 0.764 |
| 64 | 0.830 | 1.00 | 0.568 |

reward-峰 g=22(post 0.764,div 1.01)= 脆;robustness-峰 g=8(post 0.822,div 2.05)。**结构对扰动类型稳健(swap 与 gradual 都成立)。**

---

## 4. 主张(已压窄)

> **在该 toy landscape 的参数扫描中,pre-reward optimum 位于 low-diversity fragile region;这支持一个 target-level 的 reward–reselectability dissociation。**

也就是说:**在这个受控玩具里,"使 outcome/reward 最大化"的运营点,与"使 robustness / 再选择能力最大化"的运营点,是_可分离_的——而且 reward 信号在决策时刻不携带这种可分离性。** diversity(re-sampling capacity)序参量携带它。

**注意主张的窄度**:这是 **target-level**(优化_目标点_的位置)的陈述,**不是** dynamics-level(真实优化_过程_会怎样)的陈述。后者见 §5、§6。

---

## 5. 已支持 vs 未支持(必须分清)

| | 陈述 | 本楔子 |
|---|---|---|
| **已支持(在此 toy 内)** | reward optimum 与 reselectability / robustness optimum **可分离**;reward 在决策时刻对此分离性盲 | §1–§3,跨两种扰动复现 |
| **未支持** | **真实训练动态会自动导致 endogenous diversity collapse**(即"任何 reward optimizer 会内生爬到脆点") | **未达成,见 §6** |

> **禁止**把"已支持"读成"未支持":本楔子**没有**证明任何 reward 优化过程会自毁 diversity;它只证明了脆点_就是_ reward 最大点(target-level)。

---

## 6. 失败的 Experiment A(单独成节,标为未达成,不 spin)

**意图**:用一个_自适应、追逐 reward_ 的控制器,演示它**内生地**把自己的 diversity 压垮、爬进脆点(dynamics-level 的 endogenous collapse)。

**结果:未达成。** 两次尝试(1-步噪声爬山;加长评估窗 + margin 的爬山)中,reward 优化器都**没能爬到 reward-峰**(分别停在 g≈6.7、g≈4.7),因此**无法**测试"它到峰后是否自毁 diversity"。

**诚实归因**:这是**优化器工具的失败**(toy 1-D 噪声爬山在 reward landscape 上 stall),**不是**对 endogenous-collapse 主张的证据(无论支持还是反对)。要做成它需要一个_真正会爬到 reward-峰_的优化器(g-bandit / policy-gradient meta-controller),那是真实 ML 工程,超出本 scratch wedge。

**地位**:**endogenous diversity collapse 在 dynamics-level 仍是_未测_的开放工程项**,不得当已立。target-level 的可分离性(§4)**不**依赖它。

---

## 7. 诚实残余 / caveats

1. **窄度**:这是 explore/exploit-under-nonstationarity——RL 知道探索重要。本楔子的窄贡献只是"**diversity 是决策时刻的可测判别序参量,与 reward 背离**",不是"探索很重要"。
2. **endogenous 演示未达成**(§6)。
3. **recovery 指标在低 g 处混淆**(§1 注\*)。
4. **单 toy 家族、单 K / 单 landscape 结构 / 单 shift 幅度**;**一次仿真 ≠ validation**。
5. **dynamics-half-only**:对道德半 / X(外部化、他者损失)**零信息**(承 Direction 2 seed §5 防火墙)。

---

## 8. 禁句表(Forbidden / Must Not Be Overstated)

- ❌ "任何 reward optimizer 都会内生爬到脆点 / 真实训练动态会自动导致 diversity collapse"(§6 未支持)。
- ❌ "本仿真验证了 Direction 2 / 验证了道德相位"(它只触动力学半,且非 validation)。
- ❌ "diversity 序参量 = canonical d-value / RCI = canonical d-value"(回链 OPEN_TENSIONS §1,proxy gate)。
- ❌ "本结果区别于 RL,因为 RL 不懂探索"(RL 懂;窄主张是序参量的_决策时刻判别力_)。
- ❌ "扩散 / re-sampling 类比覆盖了外部化 / 他者损失"(X-失明防火墙)。
- ❌ "动力学结果支持道德命题"(动力学被证实 ≠ 道德命题被证实)。

---

## 9. 回链 + 复跑

**回链**:
- `_SRT_DIRECTION2_MORAL_GENEALOGY_SEED.md`(§7 预测候选 / §8 第一楔子 / §5 X-防火墙);
- `_SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md`(再选择能力作为对象性元标准——本楔子是它的"再选择 > 表现"主张的一个动力学侧探针);
- `Core/SRT_OPEN_TENSIONS.md §1`(d / d_stakes / D_eff proxy gate,卡住序参量操作化)、`§3`(T_dir v0 proxy)、`§8`(cross-scale loop failure,未兑现前为类比)、`§9`(closure-boundary fallibilist foundation,道德半边界承担)。

**复跑(核心仿真,pure stdlib Python,无依赖)**:

```python
import math, random
K=8; T=4000; T_SHIFT=2000; W=200; NOISE=0.15; TRIALS=100
def softmax(qs,g):
    m=max(qs); ex=[math.exp(g*(q-m)) for q in qs]; s=sum(ex); return [e/s for e in ex]
def eff_modes(c):
    tot=sum(c)
    if tot==0: return 0.0
    h=0.0
    for x in c:
        if x>0: p=x/tot; h-=p*math.log(p)
    return math.exp(h)
def sample(p,rnd):
    r=rnd.random(); cum=0.0
    for j,x in enumerate(p):
        cum+=x
        if r<=cum: return j
    return len(p)-1
def run(g,seed,gradual=False,DRIFT=600):
    rnd=random.Random(seed)
    base=[1.0,0.75,0.7,0.45,0.4,0.35,0.3,0.25]; rnd.shuffle(base); val=base[:]
    ob=max(range(K),key=lambda i:val[i]); lows=sorted(range(K),key=lambda i:val[i])[:3]; nb=rnd.choice(lows)
    q=[0.5]*K; n=[0]*K; recent=[]; rew=[]; div=[]
    for t in range(T):
        if not gradual and t==T_SHIFT:
            val=[0.3]*K; val[nb]=1.0
            for i in rnd.sample([j for j in range(K) if j!=nb],2): val[i]=0.6
        if gradual and T_SHIFT<=t<T_SHIFT+DRIFT:
            f=(t-T_SHIFT)/DRIFT; val[ob]=1.0-0.7*f; val[nb]=0.3+0.7*f
        i=sample(softmax(q,g),rnd); obs=val[i]+rnd.gauss(0,NOISE)
        n[i]+=1; q[i]+=(obs-q[i])/n[i]; recent.append(i)
        if len(recent)>W: recent.pop(0)
        rew.append(val[i]); c=[0]*K
        for m in recent: c[m]+=1
        div.append(eff_modes(c))
    return (sum(rew[T_SHIFT-W:T_SHIFT])/W, sum(div[T_SHIFT-W:T_SHIFT])/W, sum(rew[T-W:T])/W)
for g in [4,6,8,11,16,22,32,64]:
    a=b=c=0.0
    for s in range(TRIALS):
        x,y,z=run(g,1000*s+int(g*7)); a+=x; b+=y; c+=z
    print(f"g={g:>3}  pre_rew={a/TRIALS:.3f}  pre_div={b/TRIALS:.2f}  post_rew={c/TRIALS:.3f}")
```

> 随机种子 / trial 数不同会有数值波动;报告的是**结构**(reward-峰落在 diversity-坍缩区),不是精确数值。Experiment A 的失败优化器代码不附(它失败了,不作复跑基准);如需复现失败,见 §6 描述的 1-D 噪声爬山。

---

## 10. 文件目标

记录 Direction 2 动力学半的第一颗楔子:**target-level 的 reward–reselectability 可分离性,在此 toy 内被支持、跨两种扰动复现;dynamics-level 的 endogenous collapse 未达成、留作工程。** 非 validation,非道德半,非 canonical。
