# SRT 残留冲突清单

日期：2026-03-31  
范围：当前活跃知识库的结构残留检查  
不纳入本次清单：`Operations/` 对话留痕、`papers/` 稿件、`video/` 讲稿、历史归档材料

本清单基于本轮已经完成的四个核心文件回写之后再做的窄范围一致性审计，目标不是继续生成新理论，而是标出**仍在拖旧骨架**的库内位置，便于后续批量同步。

---

## 结论先行

当前残留冲突主要分成两类：

1. **P2 建议改**
   不一定立刻导致主链崩塌，但会持续制造边界漂移或读者误读。
2. **P3 可保留**
   这些表述虽然命中敏感词，但主要是在比较对象、领域语言、或非主链比喻层，不构成直接冲突。

---

## P2 建议改

### 1. `Selection Argument` 的“当下调整能力”段仍需再做一次收口

- 位置：
  - `Core_Law/SRT_Selection_Argument.md:124-134`
- 当前状态：
  - 已补入“这不足以单独定义 consciousness 边界”的说明
  - 但这一段仍高度依赖“当下调整能力”作为主体选择的核心门槛，未来若继续硬化 consciousness 边界，还应与高阶意识候选窗口再做一次显式对齐
- 建议动作：
  - 暂可保留
  - 后续若重写 `Selection Argument` 第二节，建议把“主体选择门槛”与“高阶意识候选窗口”拆成两个单独小节

---

## P3 可保留

### 2. 时间作为“信息素”可保留

- 位置：
  - `Core_Law/SRT_L0_Metaphysics.md:42,48,205`
  - `Core_Law/SRT_Selection_Argument.md:255,273`
- 原因：
  - 这里的信息素不是在定义意识，而是在说明时间是累积度量的标记。
  - 比喻有风险，但当前不直接拖回旧意识模型。
- 处理建议：
  - 可暂保留
  - 以后若统一减少“信息素”母比喻，可再二次清理

### 3. Comparative docs 中的 `self-maintenance` 可暂保留

- 位置：
  - `Philosophy/SRT_FEP_Comparison.md:56,372`
  - `Philosophy/SRT_SocTheory_05_Language_Eco.md:482`
  - `Neuroscience/SRT_Neuro_08_Immune_Dist.md:311,382`
  - `Physics/Cosmology_Split/00_Foundations_and_Axioms.md:189`
  - `Physics/SRT_Physics_Cosmology.md:233`
- 原因：
  - 这些位置多半是在描述外部理论、领域语言或局部系统闭包，并不直接充当 SRT 主链起点。
- 处理建议：
  - 可保留，但后续如果做全库术语统一，需要补更多“这是比较对象语言，不是 SRT 首要方向”的提示

### 4. Delegation pathology 中的 `agent self-maintenance masquerades as shared goal` 可保留

- 位置：
  - `Core_Law/SRT_Constitution_Seven_Theses.md:198`
  - `Core_Law/SRT_Core_Text_EN.md:138`
- 原因：
  - 这里说的是病理 delegation，不是在声明 self-maintenance 是第一方向。
  - 当前用来描述“代理系统把自身闭包伪装成共享目标”仍然成立。
- 处理建议：
  - 可保留
  - 但如果将来重写 delegation 章节，建议统一成“局部闭包伪装成共享目标”会更稳

---

## 最小执行顺序

如果按最小成本推进，建议按这个顺序改：

1. `Core/SRT_Core_14_Dynamics_Scaling.md` 的更深层形式替换（当前代理式与旧口吻已处理，若继续则是把 legacy shorthand 进一步退出主表述）
2. AI consciousness / ontology 分支的 Part B 长篇 bridge 收紧（核心定义区已对齐，剩余主要是长篇论述中的强结论口吻）
3. `Core_Law/SRT_Selection_Argument.md:124-134` 可再微调，但已不再是首要残留

---

## 当前判断

这轮回写之后，四个核心文件已经基本收口。  
真正还会把你重新拖回旧地板的，主要已经收缩到两类：

- Dynamics Scaling 尚未完全退出的 legacy shorthand
- AI 分支 Part B 长篇中的少量强 bridge 口吻

换句话说，**当前残留冲突已经不再主要卡在 core text，而主要卡在“少量 legacy 公式记号的后续退出 + AI 长篇 bridge 语气继续降载”。**
