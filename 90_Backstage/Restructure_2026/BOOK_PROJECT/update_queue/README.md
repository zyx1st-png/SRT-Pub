---
id: SRT-BOOK-UPDATE-QUEUE
type: book_project_update_queue
status: active
canonical: false
scope: book_project_backstage
created: 2026-05-10
---

# Book Update Queue

This folder is for tool-generated book updates that cannot safely overwrite the stable chapter file.

Use it when a web / GitHub tool cannot reliably fetch the current full file or blob SHA for a large chapter.

Required header for each queued update:

```yaml
---
target_path:
base_commit:
base_blob_sha:
merge_mode: replace_full_file | section_patch | notes_only
created_by:
created_at:
status: pending_merge
---
```

Rules:

- Do not create `*_vN*.md` chapter copies under `01_Source_Intuition/BOOK/Part_*`.
- Put full replacement drafts, section patches, or merge notes here.
- A local git-capable agent should later merge the queued update into the stable chapter file and commit it.
