# 如何给 Pro / Deep Research 上传《从存在到秩序》书稿

你现在遇到的问题是：Pro 模型或 Deep Research 对 GitHub 仓库调用不稳定，所以不要让它临时访问仓库，而是给它一个本地合并后的 Markdown 文件。

## 最推荐流程

1. 下载这个脚本：`build_srt_deep_research_full_bundle.py`
2. 把脚本放到本地仓库 `SRT-Pub` 根目录。
3. 在终端运行：

```bash
cd /path/to/SRT-Pub
python3 build_srt_deep_research_full_bundle.py
```

4. 打开生成目录：

```text
01_Source_Intuition/BOOK/_DeepResearch_Pack/
```

5. 上传这个文件给 Pro / Deep Research：

```text
SRT_BOOK_FULL_CONTEXT_FOR_DEEP_RESEARCH_YYYY-MM-DD.md
```

6. 同时复制 `SRT_PRO_DEEP_RESEARCH_BOOT_FILE_2026-06-05.md` 里的提示词给模型。

## 如果模型仍然说没有文档

直接告诉它：

```text
我已经上传了本地合并版 Markdown。请读取当前会话附件，不要调用 GitHub。如果你看不到文件，请说明你看不到附件，而不是说仓库不可检索。
```
