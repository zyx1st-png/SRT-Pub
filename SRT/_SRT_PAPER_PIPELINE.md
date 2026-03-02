---
id: SRT-PAPER-PIPELINE
type: framework
tags: [Paper, Submission, Research, JournalMatch]
status: active_v2
dependency: [SRT-EQ-HYP-MAP, SRT-QUALITY-SCORECARD, SRT-WEEKLY-THEORY-REVIEW]
---

# SRT 论文孵化流水线（Pipeline 2）

> **变更（2026-03-02）**：在成熟度评分中添加期刊匹配环节，规范候选条目输出格式（含期刊推荐）。

---

## 目标

将内部理论资产持续提炼为可投稿论文，形成"候选池 → 主稿 → 预投稿包"的闭环。

---

## 触发方式

**自动提醒（HEARTBEAT，每周一）**：
- 检查 `memory/heartbeat-state.json` 中 `paper_pipeline_week`
- 若本周未执行 → 提醒用户并等待授权
- 执行后更新 `paper_pipeline_week` 为本周 ISO 周号（如 `2026-W10`）

**手动触发**：
- 用户发送 `论文候选` → 立即执行候选池更新与评分

---

## 周期

- **每周**：候选筛选 + 评分更新 + 期刊匹配
- **每两周**：主稿迭代 + 投稿就绪评估

---

## 阶段

1. **候选池构建**（3-5 题）
2. **成熟度评分**（理论完整、证伪性、证据等级、引用密度）+ **期刊匹配**
3. **主稿迭代**（单篇优先）
4. **预投稿检查**（结构、图表、引文、边界声明）
5. **投稿包生成**（cover letter + target journal fit）

---

## 候选条目标准格式

每个候选题目在 `_SRT_PAPER_CANDIDATES.md` 中使用以下格式：

```markdown
### [P-ID] 论文候选标题

**成熟度评分**：XX/100
**理论完整度**：X/25 | **证伪性**：X/25 | **证据等级**：X/25 | **引用密度**：X/25

**选题原因**：
...（为什么这个题目现在适合发表？时机、空白点、SRT 独特贡献）

**核心论点**：
...（一段话概括论文的主张）

**关联 SRT 内容**：
- 主要文件/章节：`SRT/路径#章节`
- 关键方程：Eq-XX-XX
- 实验钩：H-ID（若已有实验数据）

**推荐期刊（按优先级）**：
1. [期刊名] | IF 估算：~X.X | 匹配原因：...
2. [期刊名] | IF 估算：~X.X | 匹配原因：...
3. 预印本：arXiv（分区：q-bio.NC / nlin.AO / cs.NE）

**投稿前缺口**：
- 缺口 1：...
- 缺口 2：...
```

---

## 期刊匹配逻辑

根据论文主题选择匹配期刊：

| 主题方向 | 推荐期刊（第一梯队） | 推荐期刊（第二梯队） |
|---------|-----------------|-----------------|
| 跨学科/意识理论 | *Entropy*、*PLOS ONE* | *Frontiers in Psychology* |
| 神经科学 | *Neural Computation*、*NeuroImage* | *Frontiers in Neuroscience* |
| 哲学/认知科学 | *Synthese*、*Mind & Language* | *Phenomenology and the Cognitive Sciences* |
| 物理/复杂系统 | *Physical Review E*、*Chaos* | *Journal of Statistical Physics* |
| AI/计算 | *Neural Networks*、*Cognitive Computation* | *Frontiers in AI* |
| 预印本先行（所有方向） | arXiv (q-bio.NC, nlin.AO) | bioRxiv |

**选刊原则**：
1. 优先匹配论文最强的一个维度（避免"跨学科导致无家可归"）
2. 预印本先行：正式投稿前先发 arXiv，建立优先权并获得早期反馈
3. 开放获取优先（*Entropy*、*PLOS ONE*）有利于传播

---

## 交付物

- `SRT/_SRT_PAPER_CANDIDATES.md`（候选池，含期刊匹配）
- `SRT/_SRT_PAPER_DRAFT_ACTIVE.md`（当前主稿）
- `SRT/_SRT_PAPER_SUBMISSION_CHECKLIST.md`（预投稿清单）
