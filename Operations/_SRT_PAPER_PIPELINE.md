---
id: SRT-PAPER-PIPELINE
type: framework
status: active
claim_mode: governance
updated: 2026-08-05
version: v3
layer: meta
epistemic_layer: os
dependency: [SRT-EQ-HYP-MAP, SRT-QUALITY-SCORECARD, SRT-WEEKLY-THEORY-REVIEW]
---

# SRT 论文孵化与出版流程（Pipeline 2）

## 目标

把论文工作分成四种互不混淆的状态：

1. **候选孵化**：尚未进入当前施工；
2. **活跃主稿**：作者明确授权编辑；
3. **投稿／出版流程**：已提交、已接受或正在转投；
4. **触发式延期**：有明确复活条件，但不自动排队。

`STATUS.md` 是唯一事实状态面；Pipeline 2 的三件套只维护对象、动作和门控。

---

## 触发方式

### HEARTBEAT

每周只检查：

- 是否有出版状态变化尚未同步；
- 是否有作者明确要求复活候选；
- 是否有活跃主稿需要推进。

没有状态变化或作者授权时，不自动重排候选、不刷新分数、不改稿。

### 手动触发

- `论文候选`：重新审计候选对象、路径与复活条件；
- `推进主稿`：只处理 `_SRT_PAPER_DRAFT_ACTIVE.md` 指定的工作面；
- `投稿检查`：执行 `_SRT_PAPER_SUBMISSION_CHECKLIST.md`；
- `更新投稿状态`：先核验事实，再同步 `STATUS.md` 与对应 Issue。

---

## 阶段

1. **对象定位**：稿件路径、相关实验、补充材料和当前 owner；
2. **状态分类**：candidate / active draft / publication workflow / deferred；
3. **复活或施工门**：作者授权、材料收口、外部回复或协议条件；
4. **主稿迭代**：只对 active draft 执行；
5. **预投稿检查**：结构、图表、引文、边界、匿名与数据声明；
6. **投稿包生成**：按当时真实期刊规则生成；
7. **状态同步**：稿号、编辑阶段、外审、接受、proof、DOI 或终止路径。

---

## 候选池契约

`Operations/_SRT_PAPER_CANDIDATES.md` 中每个候选至少包含：

```markdown
| 候选 | 当前对象 | 复活条件 |
|---|---|---|
| 标题 | `repo/path/to/manuscript.md` | 具名触发条件 |
```

规则：

- 已投稿、已接受或已进入出版流程的稿件不参与候选评分；
- 不维护永久 `XX/100` 成熟度分数；
- 不在未实际复活时预填期刊、IF 或 APC；
- 选刊必须在真实提交前重新核验 scope、article type、费用、版权和匿名政策；
- 每个候选必须有可定位路径和复活条件；
- 历史评分如需保留，进入 `Operations/Archive_Records/`。

---

## 活跃主稿契约

`Operations/_SRT_PAPER_DRAFT_ACTIVE.md` 只回答：

- 当前允许编辑哪一篇稿件或哪一个转投包；
- 当前允许和禁止的动作；
- 是否存在第二 drafting queue。

没有作者明确授权时，不自动把候选提升为活跃主稿。

---

## 投稿清单契约

`Operations/_SRT_PAPER_SUBMISSION_CHECKLIST.md` 只列：

- 操作硬门；
- 核验动作；
- 完成条件；
- 措辞与重复投稿护栏。

完整状态叙述指回 `STATUS.md`，不在三件套之间复制维护。

---

## 期刊匹配规则

1. 先确定稿件的最强学科问题和 article type；
2. 使用当前官网、作者指南和费用政策重新核验；
3. 同时检查订阅出版、APC、减免与机构协议；
4. 不默认“预印本先行”，而是按目标期刊政策和作者策略决定；
5. 原投稿流程未终止前不转投；
6. 期刊推荐必须标注核验日期，过期后重新查证。

---

## 三件套输出

- `Operations/_SRT_PAPER_CANDIDATES.md`：候选对象、路径、复活条件；
- `Operations/_SRT_PAPER_DRAFT_ACTIVE.md`：当前允许编辑的主稿／出版工作面；
- `Operations/_SRT_PAPER_SUBMISSION_CHECKLIST.md`：操作门与完成条件；
- `STATUS.md`：唯一事实状态面。
