---
id: SRT-TEMPLATE-MATERIAL-REVIEW
type: template
tags: [Template, Material, Pipeline1]
status: active_v1
layer: operations
epistemic_layer: workflow
claim_mode: prompt
canonical: false
date: 2026-07-15
usage: 复制本块，逐格填写。精确门槛以 Operations/_SRT_MATERIAL_PIPELINE.md 为准。
---

# 材料融合审核模板（Pipeline 1）

## 输入
- 材料：<URL / DOI / PDF / 文本 / 摘要 / 截图>
- 输入类型与证据可得性：<读到一手？还是只有二手/媒体解释/截图？证据缺口=？>

## 6 项审核门
| 门 | 结论 | 依据 |
|---|---|---|
| 1 相关性（能映射到 L0/L1/L2/Ĝθ/Ψ_f/d/硬化/选择/主体性/实验？） | pass/fail | |
| 2 增量性（不是已有内容重复？新增接口/反修正/加固/反哺/残余压力？） | pass/fail | |
| 3 证据等级（primary/peer-reviewed/preprint/review/secondary/commentary） | <标注> | |
| 4 可对齐性（能压出 ≥1 条 surviving claim 或仅作类比？） | pass/fail | |
| 5 风险（过拟合/HARKing/偷换/伪背书？） | <边界声明> | |
| 6 落点清晰（主落点/备选/禁止落点） | 主:__ 备:__ 禁:__ | |

## 裁决
- 结论：**A / B / C**（B 再标子型 B1/B2/B3）
- surviving claim（最小可承重命题，一句话）：
- A 类去材料化主句（脱离材料可独立阅读的原生表述）：

## 产物清单（勾选实际创建的）
- [ ] SourceCard
- [ ] PatchNote
- [ ] Material Log 记录（`Operations/_SRT_MATERIAL_LOG.md`，正式状态以此为准）
- [ ] Index / Registry 更新
- [ ] IntegrationHook
- [ ] 正文轻量回写（A 类，已做去材料化改写）
- [ ] STATUS.md 今日状态更新

## 红线自查
- [ ] 媒体解释未被当作者结论
- [ ] 证据等级已标注、未混淆
- [ ] 未把 P3 桥接映射 / P4 实验假说写成已证定律（P 级判读以 `Governance/SRT_CLAIM_LADDER.md` 为准）
- [ ] 回写命题已对照 canonical 与符号表
