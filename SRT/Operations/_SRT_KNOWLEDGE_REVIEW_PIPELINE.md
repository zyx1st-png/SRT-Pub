---
id: SRT-KNOWLEDGE-REVIEW-PIPELINE
type: framework
tags: [KnowledgeReview, RandomSample, QualityImprovement, Pipeline7]
status: active_v1
dependency: [SRT-OPERATIONS-README]
---

# SRT 知识点随机抽查与回写流水线（Pipeline 7）

> **目标**：每次随机抽取一个 SRT 理论知识点，深度展示后由创造者点评，Claude 基于点评优化并回写，再抽取下一个。
>
> **触发方式**：用户发送 `知识抽查`（抽取 1 个并展示）；点评后自动写回并抽取下一个。

---

## §1 流程总览

```
[触发]
  → [抽取 1 个知识点]
  → [Claude 深度展示：原文 + 通俗解释 + SRT关联 + 问题/张力/优化点 + 建议]
  → [用户点评]
  → [Claude 优化并写回源文件]
  → [git commit]
  → [自动抽取下一个，循环]
```

**阶段说明**

| 阶段 | 执行者 | 内容 |
|:-----|:-------|:-----|
| 1. 抽样 | Claude (脚本) | 从 SRT KB 所有理论文件中随机抽取 1 个知识块 |
| 2. 深度展示 | Claude | 原文全文 → 通俗解释 → 与SRT关联 → 问题/张力/优化点 → 具体建议 |
| 3. 点评 | 用户 | 接受建议 / 修改方向 / 补充意图 / `跳过` |
| 4. 优化 | Claude | 基于点评重写知识点，保持格式规范 |
| 5. 回写 | Claude (脚本) | 精确写回源文件对应行 |
| 6. 提交+循环 | Claude | `git commit` 后立即抽取下一个知识点 |

---

## §2 抽样范围

**纳入**：以下目录中所有 `.md` 文件的 `###` 级别知识块
- `Core/`（排除 Split/Annex 子目录）
- `Core_Law/`
- `Physics/`（排除 Split/Annex、CompactCore 文件）
- `Philosophy/`（排除 Split/Annex、CompactCore 文件）
- `Neuroscience/`（排除 CompactCore 文件）
- `Spirituality/`（排除 Split/Annex、Praxis_Split、CompactCore 文件）
- `AI/`（排除 Split/Annex、CompactCore 文件）

**排除**：
- `*_CompactCore.md`（派生文件）
- `*_Split/`、`*_Annex/` 目录
- `*Bridge.md`（元数据/桥接文件）
- `Operations/`、`Governance/`、`Glossary/` 目录
- 字数少于 30 字的知识块（占位内容）

---

## §3 展示格式（深度模式）

每个知识点按以下五层展示：

```
════════════════════════════════════════════
【知识点】ID · 来源文件 (行 N–M)
════════════════════════════════════════════

【原文】
[原文全文，含公式]

【通俗解释】
用日常语言解释这个知识点在说什么，给出生活类比。

【与 SRT 的关联】
说明此知识点在 SRT 体系中的位置：依赖哪些公理、
被哪些定理引用、在整体框架中起什么作用。

【问题 · 张力 · 优化点】
- 表述是否存在模糊或歧义？
- 与其他知识点是否存在概念张力？
- 缺少哪些必要内容（触发条件、分级、关联等）？
- 格式或符号问题？

【建议】
具体可操作的改写/补充建议，附示例。

════════════════════════════════════════════
```

---

## §4 点评规范

用户可对每个知识点提供以下类型的点评：

| 类型 | 标记 | 示例 |
|:-----|:-----|:-----|
| 表述优化 | 直接说明 | "这句话不够准确，应该强调..." |
| 补充内容 | `+补充：...` | "+补充：需要加入与 FEP 的对比" |
| 删减冗余 | `-删除：...` | "-删除：最后那句 Implication 重复了" |
| 跳过 | `跳过` / `skip` | 不做修改 |
| 撤销 | `撤销` | 放弃本次对该知识点的修改 |

---

## §5 回写规则

1. **格式保持**：保留原有的 Markdown 格式、ID 编号、数学公式格式
2. **最小修改**：只修改点评涉及的部分，不扩展范围
3. **符号规范**：写回内容必须符合 `_SRT_SYMBOL_TABLE.md` 的符号规范
4. **Core_Law 保护**：`Core_Law/` 目录中的文件修改需额外确认
5. **原子提交**：每次 pipeline 运行生成一个 commit，commit message 格式：
   ```
   review(p7): optimize N knowledge points [YYYY-MM-DD]
   ```

---

## §6 执行方式

### 手动触发（命令行）

```bash
cd /Users/zhangyuxin/.openclaw/workspace/SRT
python ../scripts/srt_knowledge_review.py --count 3
```

### Claude Code 内触发

用户发送 `知识抽查` 或 `知识抽查 5`（抽查 5 个）时，Claude 执行：

```bash
python /Users/zhangyuxin/.openclaw/workspace/scripts/srt_knowledge_review.py \
  --count 3 --output-json
```

Claude 读取 JSON 输出，展示知识点，接收用户点评，调用：

```bash
python /Users/zhangyuxin/.openclaw/workspace/scripts/srt_knowledge_review.py \
  --writeback --patch-file /tmp/srt_p7_patch.json
```

---

## §7 与其他 Pipeline 的关系

| Pipeline | 关系 |
|:---------|:-----|
| Pipeline 6（每日内审） | P6 扫描格式问题；P7 深入内容质量 |
| Pipeline 4（信号采集） | P4 引入外部材料；P7 优化内部知识点 |
| Pipeline 5（媒体选题） | P5 面向输出；P7 面向理论自身的完善 |
