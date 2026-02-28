#!/usr/bin/env bash
set -euo pipefail

python3 scripts/srt_lint_frontmatter.py
python3 scripts/srt_check_links.py
python3 scripts/srt_check_symbols.py

echo "All SRT checks passed."
