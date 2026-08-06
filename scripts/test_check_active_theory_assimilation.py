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
        "assimilation_status": "effectively_assimilated",
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

        # 4. Bundled nowhere -> cannot claim the full bar.
        row = mod.check_node(base_node(), empty_bundles)
        expect("unbundled", row["problems"], "no context bundle loads it")

        # 5. A regression-test file that exists but contains no tests.
        write(root, "Tests.md", "# tests\n\nnothing here yet\n")
        row = mod.check_node(base_node(), good_bundles)
        expect("empty test file", row["problems"], "no `## T-NN` blocks")
        write(root, "Tests.md", "\n".join(f"## T-{i:02d} · case\n" for i in range(1, 13)))

        # 6. Too few tests for the full bar.
        write(root, "Tests.md", "\n".join(f"## T-{i:02d} · case\n" for i in range(1, 4)))
        row = mod.check_node(base_node(), good_bundles)
        expect("too few tests", row["problems"], f"minimum {mod.MIN_REGRESSION_TESTS}")
        write(root, "Tests.md", "\n".join(f"## T-{i:02d} · case\n" for i in range(1, 13)))

        # 7. `n/a` must not count as having handled the old formulation.
        row = mod.check_node(base_node(old_text_handled="n/a"), good_bundles)
        expect("old text n/a", row["problems"], "without recording old-text handling")

        # 8. A missing owner is reported even for a modest status claim.
        row = mod.check_node(
            base_node(active_owners=["Gone.md"], assimilation_status="partially_active"),
            good_bundles,
        )
        expect("missing owner", row["problems"], "missing active owner")

        # 9. Lower status claims are not held to the full bar: a partially_active
        #    node with no tests and no compact must stay clean, otherwise the
        #    checker would report the entire historical backlog as broken.
        row = mod.check_node(
            base_node(
                assimilation_status="partially_active",
                compact_layer=None,
                regression_tests=None,
                bundle=False,
                old_text_handled="n/a",
            ),
            empty_bundles,
        )
        expect("modest claim", row["problems"], None)

        # 10. But `bundle: true` is a claim in its own right and is checked.
        row = mod.check_node(
            base_node(assimilation_status="partially_active", regression_tests=None),
            empty_bundles,
        )
        expect("bundle claim", row["problems"], "manifest says bundle: true")

    if FAILURES:
        for failure in FAILURES:
            print(f"FAIL: {failure}")
        sys.exit(1)
    print("test_check_active_theory_assimilation: all cases pass")


if __name__ == "__main__":
    run()
