#!/usr/bin/env python3
"""Fail when `STATUS.md` drifts back into recording a PR's own lifecycle as repository state.

Twice in a row (#959, then #961) the dashboard was edited inside a landing PR to
describe that PR as in flight — `#961 ... = DRAFT / ACTIVE OWNER CYCLE`,
`CURRENT BOUNDED LANDING = #961` — so merging the PR made the panel false on the
merge commit itself. A written rule alone did not prevent the second occurrence;
this checker is its enforcement.

What is banned is narrow: a PR's transient lifecycle, and a PR number standing in
as the identity of a current-state key. Current programme state stays in scope —
`AGENTS.md` and `Governance/SRT_EDIT_PROTOCOL.md` both assign it to this page — so
an in-flight owner cycle is recorded by owner file or bounded work package instead.

`scan()` is importable so `test_check_status_recording_rule.py` can pin the
behaviour; this file is a governance gate in `governance_preflight.py`, and a gate
whose exact boundary is unpinned drifts.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STATUS = "STATUS.md"

# A line may opt out explicitly. Keep such markers rare — each one is a hole in
# the check. The rule statement itself needs one: it quotes the banned shape.
ALLOW = "status-lint:allow"

# `#961 ... = MERGED / <sha>` is fine; `= DRAFT` is not.
IN_FLIGHT = re.compile(
    r"=\s*(DRAFT|ACTIVE OWNER CYCLE|ACTIVE BOUNDED LANDING|WAITING|IN REVIEW|OPEN PR|UNMERGED)\b"
)
PR_REF = re.compile(r"#\d{2,}")

# A current-state key whose value carries a PR number at all — including the
# `owner-file / #964` shape the old dashboard actually used
# (`CURRENT TARGET OWNER = Core_Law/SRT_L0_Metaphysics.md / #961`). Current state
# already has an identity carrier (owner file, bounded work package); a transient
# PR number appended to it is exactly the coupling this rule cuts.
PR_AS_OWNER = re.compile(r"^(CURRENT|ACTIVE|NEXT)[A-Z0-9 _/()-]*=.*#\d{2,}")

# The same claim as prose — the shape the #961 Immediate routing override used:
# "The active owner cycle is now **#961 L0 targeted thinning**".
PROSE_CYCLE = re.compile(
    r"(active|current)[^\n]{0,40}(owner cycle|bounded landing)[^\n]{0,40}#\d{2,}",
    re.I,
)

# The rule text itself must stay on the page.
REQUIRED_RULE_TEXT = ("记录口径", "未合并 PR 号不得充当状态 owner")

# `build_srt_context_bundles.py` guard_dqo() extracts the d/q/o embargo sentence
# from between these markers. The anchor was already lost twice (ed20ccf, 156c4db).
REQUIRED_ANCHORS = ("SRT-GUARDRAIL:DQO-BEGIN", "SRT-GUARDRAIL:DQO-END")

# Section numbers are cited from outside and must not be renumbered:
# `Operations/Audits/SRT_CANONICAL_RETYPE_LEDGER.md` rows R2C-001..006 cite
# `STATUS.md §10` / `§11` by number.
CITED_SECTIONS = (
    "### 10. What is demoted / retyped",
    "### 11. What is retired as current admission logic",
)


def scan(text: str) -> list[str]:
    """Return every recording-rule violation in `text`, most specific first."""
    problems: list[str] = []

    for i, line in enumerate(text.splitlines(), 1):
        if ALLOW in line:
            continue
        if PR_REF.search(line) and IN_FLIGHT.search(line):
            problems.append(
                f"{STATUS}:{i}: a PR's own lifecycle is not repository state: {line.strip()}"
            )
        if PR_AS_OWNER.match(line.strip()):
            problems.append(
                f"{STATUS}:{i}: name the owner file or work package, not a PR number: "
                f"{line.strip()}"
            )
        if PROSE_CYCLE.search(line):
            problems.append(
                f"{STATUS}:{i}: an in-flight cycle is named by PR number in prose: {line.strip()}"
            )

    for needle in REQUIRED_RULE_TEXT:
        if needle not in text:
            problems.append(f"{STATUS}: the recording rule was dropped: missing {needle!r}")

    for marker in REQUIRED_ANCHORS:
        if marker not in text:
            problems.append(f"{STATUS}: generator anchor removed: missing {marker}")

    for heading in CITED_SECTIONS:
        if heading not in text:
            problems.append(
                f"{STATUS}: externally cited section heading changed or renumbered: {heading!r} "
                "(cited by Operations/Audits/SRT_CANONICAL_RETYPE_LEDGER.md)"
            )

    return problems


def main() -> None:
    problems = scan((ROOT / STATUS).read_text(encoding="utf-8"))
    if problems:
        print("status recording rule: FAIL")
        for item in problems:
            print(f"- {item}")
        raise SystemExit(1)
    print("status recording rule: PASS")


if __name__ == "__main__":
    main()
