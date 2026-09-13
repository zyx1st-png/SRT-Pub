---
name: srt-structure-extraction
description: 将 SRT 长文件中的内容拆为 split/annex 或抽取接口，执行风险盘点、裁决与落地核验。普通 typo、断链或 frontmatter 修复使用 edit protocol，不自动开启抽取流程。
argument-hint: "[目标领域/文件 | pre-audit | 裁决 | closure]"
---

# SRT Structure Extraction

使用根 AGENTS.md、`Operations/README.md` 的 Structure Governance Stop Rule、`Governance/_SRT_DOC_ENGINEERING_GUIDE.md` 及 freeze/edit protocol。先核对现有工作包的范围与裁决；不要重新请求已具备的授权。

## 三阶段

1. **Pre-audit**：只读盘点目标正文、公式、阈值、claim、元数据与导航，标出抽取风险。结果记入工作包；明确只读审计时在回复交付，不因本步骤自动创建记录。
2. **Adjudication**：确定主/备/禁止落点、可抽/暂缓/不抽及其理由。无新 pre-audit/adjudication 不做机会主义抽取。普通结构选择由 AI 在授权范围内完成；高风险公式、阈值、subjecthood、collapse 等须有对应明确裁决，不能由 AI 自批。
3. **Extraction / closure**：仅实施已裁决且已授权的块，更新实际受影响的导航、注册表和 split 元数据，按主流程留 extraction/closure 记录。大文件使用局部补丁，保持 owner 内容与论证完整。

阶段顺序保留；已有记录可复用，简单工作包可在一个记录中分节，不为形式齐全新造多个台账。只有 pre-audit 请求时，完成审计即结束，不推进抽取。

验证受影响的 split freshness、frontmatter、registry/links；集成前执行 required governance preflight。前置检查已经覆盖的项目不单独重复跑。保留既有失败归因，不扩 warning baseline。

split/annex/companion 不获得定义权；元数据归一化不改变 claim level；本流程不夹带新理论。
