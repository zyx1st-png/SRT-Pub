from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[1]
SRC = ROOT / "paper_ontological_friction.md"
OUT = ROOT / "paper_ontological_friction_preprint.md"

# One-shot PR #961 maintenance helper. This file is intentionally outside the
# context-bundle input closure. The helper updates STATUS routing first, then
# runs the repository's canonical bundle generator on that final input tree and
# commits STATUS + generated outputs back to the PR branch. It is removed as
# soon as the generated commit lands.
TARGET_BRANCH = "theory/post959-l0-thinning-clean-20260913"
if os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_HEAD_REF") == TARGET_BRANCH:
    subprocess.run(["git", "fetch", "--unshallow"], cwd=REPO_ROOT, check=False)
    subprocess.run(["git", "fetch", "origin", TARGET_BRANCH], cwd=REPO_ROOT, check=True)
    subprocess.run(
        ["git", "checkout", "-B", TARGET_BRANCH, f"origin/{TARGET_BRANCH}"],
        cwd=REPO_ROOT,
        check=True,
    )

    status_path = REPO_ROOT / "STATUS.md"
    status = status_path.read_text(encoding="utf-8")
    count = status.count("#960")
    if count != 8:
        raise RuntimeError(f"Expected exactly 8 live #960 STATUS routes, found {count}")
    status_path.write_text(status.replace("#960", "#961"), encoding="utf-8")

    subprocess.run(
        [sys.executable, "scripts/build_srt_context_bundles.py", "--generated-date", "2026-09-13"],
        cwd=REPO_ROOT,
        check=True,
    )
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=REPO_ROOT, check=True)
    subprocess.run(
        ["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"],
        cwd=REPO_ROOT,
        check=True,
    )
    subprocess.run(
        ["git", "add", "STATUS.md", "Operations/Context_Bundles"],
        cwd=REPO_ROOT,
        check=True,
    )
    staged = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=REPO_ROOT, check=False
    ).returncode
    if staged:
        subprocess.run(
            ["git", "commit", "-m", "chore: route L0 landing through #961 and refresh context bundles"],
            cwd=REPO_ROOT,
            check=True,
        )
        subprocess.run(
            ["git", "push", "origin", f"HEAD:{TARGET_BRANCH}"],
            cwd=REPO_ROOT,
            check=True,
        )


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Could not find expected {label} block in {SRC.name}")
    return text.replace(old, new, 1)


text = SRC.read_text(encoding="utf-8")

text = replace_once(
    text,
    "**Article type**: Hypothesis and Theory  \n"
    "**Target journal**: Frontiers in Neuroscience  \n",
    "**Manuscript status**: Preprint; not a peer-reviewed version of record  \n"
    "**Article type**: Theoretical Article  \n"
    "**Version**: 1.0 (19 July 2026)  \n"
    "**Author**: Yuxin Zhang  \n"
    "**Affiliation**: Independent Researcher, Kaili, Guizhou, China  \n"
    "**Correspondence**: zyx1st@gmail.com  \n"
    "**ORCID**: https://orcid.org/0009-0007-6659-8518  \n",
    "journal-specific front matter",
)

text = replace_once(
    text,
    "This is a theoretical and computational contribution aimed at empirical translation. No new data are reported. Consistent with the *Frontiers in Neuroscience* Hypothesis and Theory format, the paper advances a testable model within a specific area of investigation — the knowing-doing gap in executive dysfunction — and provides measurement strategy, falsification rules, and clinically tractable protocols for future adjudication.",
    "This is a theoretical and computational contribution aimed at empirical translation. No new data are reported. As a theoretical framework paper, the manuscript advances a testable model of the knowing-doing gap in executive dysfunction and provides measurement strategies, falsification rules, and clinically tractable protocols for future adjudication.",
    "journal-specific scope sentence",
)

if "Frontiers in Neuroscience" in text:
    raise RuntimeError("Journal-specific Frontiers wording remains in the generated preprint")
if "**Target journal**" in text:
    raise RuntimeError("Target-journal metadata remains in the generated preprint")

OUT.write_text(text, encoding="utf-8")
print(f"Wrote {OUT.name}")
