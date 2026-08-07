#!/usr/bin/env python3
"""Fixture tests for `check_active_theory_assimilation.py`.

The checker's whole point is to refuse to count engineering artifacts as
assimilation, so the tests concentrate on the ways a node can *look* assimilated
while not being reachable: a route heading that exists but names none of the
node's files, a compact layer nobody bundles, a regression-test file with no
tests, and a dangling open-tension anchor.

Run: `uv run python scripts/test_check_active_theory_assimilation.py`
"""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_active_theory_assimilation as mod  # noqa: E402

FAILURES: list[str] = []


def write(root: Path, rel: str, body: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def expect(label: str, problems: str, substring: str | None) -> None:
    """substring=None means: expect no problems at all."""
    if substring is None:
        if problems:
            FAILURES.append(f"{label}: expected clean, got {problems!r}")
        return
    if substring not in problems:
        FAILURES.append(f"{label}: expected {substring!r}, got {problems!r}")


def base_node(**overrides: object) -> dict:
    node = {
        "node_id": "NODE-TEST",
        "title": "test node",
        "active_owners": ["Owner.md"],
        "compact_layer": "Compact.md",
        "router_anchor": "Router.md#7",
        "deep_map_anchor": None,
        "bundle": True,
        "regression_tests": "Tests.md",
        "open_tension": "Tensions.md#3",
        "old_text_handled": "rewrote the old pointer",
        "author_gates": [],
        "structural_assimilation": "active_complete",
        "active_complete_blockers": [],
        "behavioral_availability": "untested",
        "behavior_evidence": None,
        "behavior_observation_mode": None,
        "interventions": [],
    }
    node.update(overrides)
    return node


def run() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        mod.ROOT = root

        write(root, "Owner.md", "# owner\n")
        write(root, "Compact.md", "# compact\n")
        write(root, "Router.md", "## 7. Route: test\n\n- `Compact.md`\n- `Owner.md`\n")
        write(root, "Tensions.md", "## 3. A tension\n")
        write(root, "Tests.md", "\n".join(f"## T-{i:02d} · case\n" for i in range(1, 13)))

        good_bundles = {"B.md": "... Compact.md ..."}
        empty_bundles: dict[str, str] = {}

        # 1. Everything present -> clean, and the full bar is met.
        row = mod.check_node(base_node(), good_bundles)
        expect("complete node", row["problems"], None)
        if row["regression_tests_count"] != 12:
            FAILURES.append(f"complete node: expected 12 tests, got {row['regression_tests_count']}")

        # 2. The central case: a real heading that does not name the node's files.
        #    Without this check a route is satisfied by any heading with the
        #    right number, which is how a node stays unreachable while looking routed.
        write(root, "Router.md", "## 7. Route: something else\n\n- `Unrelated.md`\n")
        row = mod.check_node(base_node(), good_bundles)
        expect("route names nothing", row["problems"], "names none of the node's files")
        write(root, "Router.md", "## 7. Route: test\n\n- `Compact.md`\n- `Owner.md`\n")

        # 3. Anchor number must match exactly: `#3` must not be satisfied by `## 31`.
        write(root, "Tensions.md", "## 31. Another tension\n")
        row = mod.check_node(base_node(), good_bundles)
        expect("anchor prefix collision", row["problems"], "open tension anchor not found")
        write(root, "Tensions.md", "## 3. A tension\n")

        # 4. Bundled nowhere -> cannot claim the structural bar.
        row = mod.check_node(base_node(), empty_bundles)
        expect("unbundled", row["problems"], "no default load path reads it")

        # 5. THE LOAD-BEARING CASE. A written suite is not a result: claiming a
        #    behavior verdict without recorded evidence must be rejected, even
        #    when the suite exists and is large. This is the error the 2026-08-07
        #    pass exists to correct.
        row = mod.check_node(base_node(behavioral_availability="observed"), good_bundles)
        expect("observed without evidence", row["problems"], "is not a recorded run")

        # 5b. ...and it stays rejected for `mixed` and `failed` too.
        row = mod.check_node(base_node(behavioral_availability="failed"), good_bundles)
        expect("failed without evidence", row["problems"], "is not a recorded run")

        # 5c. Evidence must actually exist.
        row = mod.check_node(
            base_node(behavioral_availability="observed", behavior_evidence="Gone.md"), good_bundles
        )
        expect("evidence missing", row["problems"], "behavior_evidence points at a missing file")

        # 5d. With real evidence it is accepted, and only then is the derived
        #     label allowed to be yes.
        write(root, "Evidence.md", "# run record\n")
        row = mod.check_node(
            base_node(behavioral_availability="observed", behavior_evidence="Evidence.md"), good_bundles
        )
        expect("observed with evidence", row["problems"], None)
        if row["effectively_assimilated"] != "yes":
            FAILURES.append("derived label should be yes for active_complete + observed")

        # 5e. active_complete alone must NOT produce the derived label.
        row = mod.check_node(base_node(), good_bundles)
        if row["effectively_assimilated"] != "no":
            FAILURES.append("derived label must be no while behavioral_availability is untested")

        # 6. A regression-test file that exists but contains no tests.
        write(root, "Tests.md", "# tests\n\nnothing here yet\n")
        row = mod.check_node(base_node(), good_bundles)
        expect("empty test file", row["problems"], "regression suite has no `## T-NN` blocks")
        write(root, "Tests.md", "\n".join(f"## T-{i:02d} · case\n" for i in range(1, 13)))

        # 7. Too few tests to support a behavior verdict (an Axis B concern, so
        #    it is only raised when a verdict is actually claimed).
        write(root, "Tests.md", "\n".join(f"## T-{i:02d} · case\n" for i in range(1, 4)))
        row = mod.check_node(
            base_node(behavioral_availability="observed", behavior_evidence="Evidence.md"), good_bundles
        )
        expect("too few tests", row["problems"], f"minimum {mod.MIN_REGRESSION_TESTS}")
        row = mod.check_node(base_node(), good_bundles)
        expect("few tests, no verdict claimed", row["problems"], None)
        write(root, "Tests.md", "\n".join(f"## T-{i:02d} · case\n" for i in range(1, 13)))

        # 8. `n/a` is ambiguous and must not count as old-text handling.
        row = mod.check_node(base_node(old_text_handled="n/a"), good_bundles)
        expect("old text n/a", row["problems"], "without recording old-text handling")

        # 9. A missing owner is reported even for a modest status claim.
        row = mod.check_node(
            base_node(
                active_owners=["Gone.md"],
                structural_assimilation="partially_active",
                active_complete_blockers=["EA-2: owner absorbed nothing"],
            ),
            good_bundles,
        )
        expect("missing owner", row["problems"], "missing active owner")

        # 9b. A node below the bar must say what holds it there.
        row = mod.check_node(
            base_node(structural_assimilation="partially_active", active_complete_blockers=[]),
            good_bundles,
        )
        expect("silent downgrade", row["problems"], "no active_complete_blockers recorded")

        # 10. Lower status claims are not held to the structural bar: a
        #     partially_active node with no tests and no compact must stay clean,
        #     otherwise the checker would report the whole historical backlog as
        #     broken and violate the Anti-Blocking Gate.
        row = mod.check_node(
            base_node(
                structural_assimilation="partially_active",
                active_complete_blockers=["EA-4: not in any bundle"],
                compact_layer=None,
                regression_tests=None,
                bundle=False,
                old_text_handled="n/a",
            ),
            empty_bundles,
        )
        expect("modest claim", row["problems"], None)

        # 11. But `bundle: true` is a claim in its own right and is checked.
        row = mod.check_node(
            base_node(
                structural_assimilation="partially_active",
                active_complete_blockers=["EA-4: pending"],
                regression_tests=None,
            ),
            empty_bundles,
        )
        expect("bundle claim", row["problems"], "manifest says bundle: true")

        # 12. `robustly_observed` carries a reliability claim, so it is gated on
        #     bounded retrieval; an unconstrained deep dive must not be recorded
        #     as a fast-layer result.
        row = mod.check_node(
            base_node(
                behavioral_availability="robustly_observed",
                behavior_evidence="Evidence.md",
                behavior_observation_mode="unconstrained",
            ),
            good_bundles,
        )
        expect("robust needs bounded", row["problems"], "requires behavior_observation_mode=bounded")
        row = mod.check_node(
            base_node(
                behavioral_availability="robustly_observed",
                behavior_evidence="Evidence.md",
                behavior_observation_mode="bounded",
            ),
            good_bundles,
        )
        expect("robust with bounded", row["problems"], None)

        # 13. Axis C records are validated but never inferred.
        row = mod.check_node(
            base_node(interventions=[{"intervention": "PR", "intervention_effect": "wishful",
                                      "ref": "Evidence.md"}]),
            good_bundles,
        )
        expect("bad axis C value", row["problems"], "intervention_effect not in the allowed set")
        row = mod.check_node(
            base_node(interventions=[{"intervention": "PR", "intervention_effect": "none"}]),
            good_bundles,
        )
        expect("intervention without ref", row["problems"], "without a `ref`")

        # 14. THE SEMANTIC FIX. A node whose baseline already retrieves and uses
        #     it is available (B) even though the PR added nothing (C). These must
        #     not collapse: recording that as "not assimilated" was the 2026-08-07
        #     error this axis split exists to prevent.
        row = mod.check_node(
            base_node(
                behavioral_availability="observed",
                behavior_evidence="Evidence.md",
                interventions=[{"intervention": "PR", "intervention_effect": "none",
                                "ref": "Evidence.md"}],
            ),
            good_bundles,
        )
        expect("zero-effect PR, available node", row["problems"], None)
        if row["effectively_assimilated"] != "yes":
            FAILURES.append("a node with a zero-effect PR but observed availability must still derive yes")

        # 15. An unknown Axis B value is rejected rather than silently accepted.
        row = mod.check_node(base_node(behavioral_availability="probably_fine"), good_bundles)
        expect("bad axis B value", row["problems"], "behavioral_availability not in the allowed set")

    if FAILURES:
        for failure in FAILURES:
            print(f"FAIL: {failure}")
        sys.exit(1)
    print("test_check_active_theory_assimilation: all cases pass")


if __name__ == "__main__":
    run()
