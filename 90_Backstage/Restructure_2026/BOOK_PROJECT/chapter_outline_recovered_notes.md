---
id: SRT-BOOK-CHAPTER-OUTLINE-RECOVERY-NOTES
type: backstage_recovery_notes
status: active_draft
canonical: false
scope: book_project
layer: meta
epistemic_layer: os
claim_mode: navigation
---

# Chapter Outline Recovery Notes

> Purpose: record why `01_Source_Intuition/BOOK/00_全书章节写作概要.md` was added and how it should be used.
>
> 2026-05-08 update: the outline was split into `01_Source_Intuition/BOOK/Outline_Parts/`; the root outline file now acts as a connector-safe index.

---

## 1. Diagnosis

The repository had strong local writing assets:

- written chapters;
- single-chapter recovered notes;
- style guides;
- philosophical style rules;
- review-driven PR notes.

But it lacked a middle-level whole-book writing outline that tells future writers:

- what each chapter must do;
- what each chapter should not prematurely include;
- how chapters depend on one another;
- which concepts first enter where;
- which lines are candidate load-bearing sentences;
- which chapters are already drafted or still missing.

This absence made the project rely too much on step-by-step local review rather than a stable whole-book construction map.

---

## 2. File added

Added:

```text
01_Source_Intuition/BOOK/00_全书章节写作概要.md
```

Current split layout:

```text
01_Source_Intuition/BOOK/00_全书章节写作概要.md
01_Source_Intuition/BOOK/Outline_Parts/
```

The root file provides the entry index. The split files provide:

- whole-book movement;
- 7-volume / 52-chapter structure;
- per-chapter task;
- core question;
- chapter summary;
- required concepts;
- do-not-prematurely-expand constraints;
- relation to previous / next chapter;
- candidate sharp sentences;
- chapter status table;
- maintenance rules.

---

## 3. Intended use

Before drafting a chapter:

1. Open `00_全书章节写作概要.md`, then read the corresponding `Outline_Parts/` chapter brief.
2. Check what must be introduced.
3. Check what must be deferred.
4. Draft the chapter in book voice.
5. Update chapter status and candidate nochange lines after founder pass.

This document should be updated whenever:

- chapter order changes;
- chapter title changes;
- a chapter gets merged;
- a major concept moves to a different chapter;
- a deferred material becomes accepted into main prose.

---

## 4. Important guardrail

The outline is not canonical.

It is a writing scaffold, not a theory authority. If future chapter writing discovers a better structure, the outline should be revised.

Do not let the outline become a new L2 that prevents the book from finding its better shape.

---

## 5. Candidate nochange / quasi-nochange lines

1. “本文件不替代正文，不替代 style guide，不替代 canonical；它只负责全书写作施工。”
2. “存在，是这条链上较晚出现的稳定标注；秩序，是许多稳定标注彼此继承之后形成的背景结构。”
3. “不要信 SRT。使用它，拆它，让它在新的选择中继续变形。”
4. “不要让 outline 成为新的 L2。”

---

## 6. Deferred improvements

Future improvements may include:

- a separate chapter dependency graph;
- a chapter concept index;
- a chapter status tracker table with PR/commit links;
- mapping from each chapter to canonical / bridge / public-layer anchors;
- a load-bearing sentence pool by chapter.
