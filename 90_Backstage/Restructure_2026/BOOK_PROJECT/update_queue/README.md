---
id: SRT-BOOK-UPDATE-QUEUE
type: book_project_update_queue
status: active
canonical: false
scope: book_project_backstage
created: 2026-05-10
---

# Book Update Queue

This folder is an optional queue for tool-generated book updates that do not fit well as standalone chapter drafts.

Web / GitHub tools may also create standalone `*_vN*.md` chapter drafts directly under `01_Source_Intuition/BOOK/Part_*`. Use this queue mainly for section patches, merge notes, or non-chapter update material.

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

- Standalone `*_vN*.md` chapter drafts are allowed under `01_Source_Intuition/BOOK/Part_*` when that is easier for the tool.
- Put section patches, merge notes, or non-chapter update material here.
- A local git-capable agent should later merge queued updates or standalone draft files into the stable chapter file and commit the cleanup.
