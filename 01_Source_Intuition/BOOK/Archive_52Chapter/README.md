---
id: SRT-BOOK-ARCHIVE-52CHAPTER
type: archive_index
status: archived
canonical: false
active_construction: false
authority_level: historical_material
scope: book_project
layer: meta
epistemic_layer: os
claim_mode: navigation
archived_on: 2026-05-22
updated: 2026-07-12
reason: book direction changed from the old 52-chapter route to the current Q00-Q28 plus topic-chapter five-act route
active_replacement:
  - 01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md
  - 01_Source_Intuition/BOOK/BOOK_ACTIVE_MANIFEST.json
  - 01_Source_Intuition/BOOK/Drafts_26Q/
---

# 存档：52 章旧结构

本目录保存《从存在到秩序》旧 52 章、`Part_*`、旧 `Outline_Parts/` 与历史版本稿。

## 当前地位

- 本目录是**历史材料库**，不是当前书稿施工入口。
- 当前正文主线唯一位于 `../Drafts_26Q/`。
- 当前状态与机器路由分别以 `../BOOK_CURRENT_STATUS.md`、`../BOOK_ACTIVE_MANIFEST.json` 为准。
- 本目录中的版本号只表示旧路线内部版本，不得与当前 `Drafts_26Q/` 版本直接比较新旧。
- 旧结构文件不再作为书籍出版骨架，不得覆盖当前五幕结构与当前章节判断。

## Agent / AI 硬规则

涉及书稿阅读、修订、续写、回写或章节定位时：

1. 必须先读取 `../BOOK_CURRENT_STATUS.md`；
2. 必须再读取 `../BOOK_ACTIVE_MANIFEST.json` 指向的当前章节；
3. 当前章节尚未读取前，不得以本目录搜索结果回答书稿现状；
4. 本目录只可用于历史对照、来源追踪、旧表达回收与差异审计；
5. 引用本目录时，必须明确标注“历史稿 / 旧路线”；
6. 不得直接复制旧稿作为当前正文初稿或补丁母版；
7. 不得把关键词命中度、旧文件版本号或旧章节编号当作当前权威性。

## 允许用途

- 比较旧路线与当前五幕结构的概念迁移；
- 追踪某一表达、例子或术语的历史来源；
- 审计当前稿是否遗漏旧稿中的有效直觉；
- 在已经读取当前章节后，为当前写作提供受控的历史材料。

## 禁止用途

- 因旧稿术语密度更高而优先采用旧定义；
- 用旧章节编号、旧 Part 结构或旧版本号判断当前书稿状态；
- 让归档文本覆盖当前正文、当前状态文件或 canonical 锚点；
- 将旧稿未经去历史化、重新论证和当前章节适配就直接回填。

## 目录内容

```text
Archive_52Chapter/
├── Part_01_从存在到成为/       旧卷一章节
├── Part_02_选择的本性/         旧卷二章节
├── Part_03_从选择到主体与价值/ 旧卷三章节
├── Part_04_秩序的双面性/       旧卷四章节
├── Outline_Parts/              旧多卷结构概要文件
├── Future_Materials/           旧待用材料
├── Versioned_Drafts/           旧版本草稿及 copyedit 策略文件
└── 00_*                        旧概念图、章节概要、序言、术语与定位文件
```

## 当前入口

| 文件 | 角色 |
|---|---|
| `../BOOK_CURRENT_STATUS.md` | 当前唯一施工状态入口 |
| `../BOOK_ACTIVE_MANIFEST.json` | 当前机器路由与归档降权规则 |
| `../BOOK_ARCHITECTURE_MAP_5ACT_2026-06-24.md` | 当前五幕结构视图 |
| `../BOOK_VERSION_LOG.md` | 当前版本变更记录 |
| `../Drafts_26Q/` | 当前正文主线 |
