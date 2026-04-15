# Translation Style Guide

## Scope
This guide standardizes CN->EN translation for SRT repository documents.

## Document Structure
- Preserve original section order and heading depth.
- Preserve front matter keys and append:
  - `source_path`
  - `source_commit`
  - `translation_status`
  - `last_sync`

## Formula Rendering (GitHub Compatible)
- Inline math: use `$...$`
- Block math: use `$$...$$`
- Do NOT use `\(...\)` or `\[...\]` in Markdown docs.

## Terminology
- Follow `i18n/glossary.md` strictly for core terms.
- Keep notation exactly as source for symbols and equation IDs.

## Quality Bar
- `pending`: no translation yet
- `in_progress`: partial sections translated, meaning verified
- `done`: full translation + notation + dependency references checked
