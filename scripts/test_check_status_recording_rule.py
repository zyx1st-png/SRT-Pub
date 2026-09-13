#!/usr/bin/env python3
"""Tests for `check_status_recording_rule.py`.

The checker is a governance gate: it fails the whole preflight, so its exact
boundary has to be pinned. The banned shapes below are not hypothetical — each
FAIL case is a line that was actually committed to `STATUS.md` and made the
dashboard false on a merge commit:

- `#961 ... = DRAFT / ACTIVE OWNER CYCLE` and `CURRENT BOUNDED LANDING = #961`
  stood on `main` at 5591c793 after #961 had merged.
- `CURRENT TARGET OWNER = ... / #961` is the `owner-file / PR-number` shape; the
  first version of the checker let it through, which is why it is pinned here.
- "The active owner cycle is now **#961 ...**" is the prose form the Immediate
  routing override used.

The PASS cases matter just as much: a merged fact with its sha, and an owner
cycle named by owner file, must stay expressible. Over-banning would push the
page into the opposite failure — unable to record current programme state, which
`AGENTS.md` and `Governance/SRT_EDIT_PROTOCOL.md` both assign to it.

Run: `uv run python scripts/test_check_status_recording_rule.py`
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_status_recording_rule as C  # noqa: E402

FAILURES: list[str] = []

# A frame carrying everything the whole-file requirements need, so a case only
# ever fails on the line under test.
FRAME = """记录口径 ... 未合并 PR 号不得充当状态 owner
d/q/o 护栏 owner = Governance/SRT_DOWNSTREAM_GUARDRAILS.md
### 10. What is demoted / retyped
### 11. What is retired as current admission logic
"""

OWNER = """<!-- SRT-GUARDRAIL:DQO-BEGIN -->
已加下游护栏：...
<!-- SRT-GUARDRAIL:DQO-END -->
"""


def case(label: str, line: str, should_fail: bool) -> None:
    problems = C.scan(FRAME + line + "\n", OWNER)  # FRAME/OWNER satisfy every whole-file rule
    failed = bool(problems)
    if failed != should_fail:
        want = "FAIL" if should_fail else "PASS"
        got = "FAIL" if failed else "PASS"
        FAILURES.append(f"{label}: expected {want}, got {got} ({problems})")


# -- banned: a PR's own lifecycle -------------------------------------------
case("in-flight lifecycle token",
     "#964 One Formation thinning = DRAFT / ACTIVE OWNER CYCLE", True)
case("PR number as the value of a current-state key",
     "CURRENT BOUNDED LANDING = #964 / ONE FORMATION", True)
case("owner file with a PR number appended",
     "CURRENT TARGET OWNER = `Core_Law/SRT_One_Formation.md` / #964", True)
case("next-owner key with a PR number appended",
     "NEXT TARGET OWNER = `Core_Law/SRT_One_Formation.md` / #964", True)
case("in-flight cycle named by PR number in prose",
     "The active owner cycle is now **#964 One Formation thinning**.", True)
case("next cycle named by PR number in prose",
     "The next owner cycle is **#964 One Formation**.", True)
case("waiting-on-CI lifecycle",
     "#964 = WAITING CI", True)

# -- allowed: landed facts and owner-named state ----------------------------
case("merged fact with sha",
     "#961 post-#959 L0 targeted thinning = MERGED / 5591c793cd985729a228a2", False)
case("owner cycle named by owner file",
     "NEXT TARGET OWNER = `Core_Law/SRT_One_Formation.md` / OWNER CYCLE NOT YET OPEN", False)
case("no active cycle",
     "ACTIVE OWNER CYCLE = NONE", False)
case("completed landing referencing the PR that did it",
     "SECOND BOUNDED OWNER LANDING = COMPLETE IN #961 / L0 METAPHYSICS", False)
case("explicit opt-out marker",
     "CURRENT TARGET OWNER = #964 <!-- status-lint:allow -->", False)

# -- whole-file requirements -------------------------------------------------
if not C.scan(FRAME, OWNER.replace("SRT-GUARDRAIL:DQO-BEGIN", "gone")):
    FAILURES.append("a removed generator anchor in the guardrail owner did not fail")
if not C.scan(FRAME.replace("Governance/SRT_DOWNSTREAM_GUARDRAILS.md", "gone"), OWNER):
    FAILURES.append("a dropped guardrail pointer in STATUS did not fail")
if not C.scan(FRAME.replace("记录口径", "gone"), OWNER):
    FAILURES.append("a dropped recording rule did not fail")
if not C.scan(FRAME.replace("### 10. What is demoted / retyped", "### 9. Demoted"), OWNER):
    FAILURES.append("a renumbered externally cited section did not fail")
if C.scan(FRAME, OWNER):
    FAILURES.append(f"the clean frame should pass: {C.scan(FRAME, OWNER)}")

if FAILURES:
    print("test_check_status_recording_rule: FAIL")
    for item in FAILURES:
        print(f"- {item}")
    raise SystemExit(1)

print("test_check_status_recording_rule: all cases pass")
