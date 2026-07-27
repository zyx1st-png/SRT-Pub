#!/usr/bin/env python3
"""Tests for `build_srt_context_bundles.py`.

These assert the *substance* of the extracted guardrails, not merely that some
regex still fires. Two review findings motivate that distinction:

- G1 once carried a hand-written "the only unconditional claim is `if τ<∞`
  then not a stable ISP", which dropped the audit's S1/pathwise qualifier and
  reintroduced exactly the semantic promotion the audit warns against.
- G3 once summarised all three `partial` hooks as blocked on `T_dir`, when the
  source table shows two on `T_dir` and one on `Occlusion_Dynamics`.

Both were shaped correctly enough to pass an anchor-exists check, so the tests
below pin counts, grouping, and the presence of the limiting clause.

Run: `uv run python scripts/test_build_context_bundles.py`
"""

from __future__ import annotations

import os
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_srt_context_bundles as B  # noqa: E402

FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    if not condition:
        FAILURES.append(f"{label}{': ' + detail if detail else ''}")


# --------------------------------------------------------------------------
# G3 — grouping must come from the table, not a hand-written summary
# --------------------------------------------------------------------------

def test_hook_grouping() -> None:
    rows, groups = B.parse_open_hooks()

    check("G3 row count", len(rows) == 6, f"got {len(rows)}")
    check("G3 group count", len(groups) == 3, f"got {sorted(groups)}")

    by_target = {k: sorted(v) for k, v in groups.items()}
    t_dir = [k for k in by_target if "T_dir" in k]
    occl = [k for k in by_target if "Occlusion_Dynamics" in k]
    planned = [k for k in by_target if "planned target" in k]

    check("G3 has a T_dir group", len(t_dir) == 1, f"got {t_dir}")
    check("G3 has an Occlusion_Dynamics group", len(occl) == 1, f"got {occl}")
    check("G3 has a planned-target group", len(planned) == 1, f"got {planned}")
    if not (t_dir and occl and planned):
        return

    # The exact miscount the review caught: T_dir must be 2, never 3.
    check("G3 T_dir count is 2", len(by_target[t_dir[0]]) == 2, f"got {by_target[t_dir[0]]}")
    check("G3 Occlusion_Dynamics count is 1", len(by_target[occl[0]]) == 1,
          f"got {by_target[occl[0]]}")
    check("G3 planned-target count is 3", len(by_target[planned[0]]) == 3,
          f"got {by_target[planned[0]]}")

    check("G3 T_dir hooks are AG02/AG03",
          by_target[t_dir[0]] == ["PH_AG02_Reasoning_Bias", "PH_AG03_Constitutive_Commitment"],
          f"got {by_target[t_dir[0]]}")
    check("G3 Occlusion hook is SEM01",
          by_target[occl[0]] == ["PH_SEM01_Bilateral_Incompatibility"],
          f"got {by_target[occl[0]]}")

    rendered = B.render_guardrail(B.guard_hooks())
    check("G3 does not claim all three partials share one blocker",
          "三张 partial 的共同阻塞点" not in rendered)
    check("G3 names Occlusion_Dynamics in the grouping", "Occlusion_Dynamics" in rendered)


# --------------------------------------------------------------------------
# G1 — the S1/pathwise qualifier must survive into the usage policy
# --------------------------------------------------------------------------

def test_p1_t07_semantics() -> None:
    g = B.guard_p1_t07()
    rendered = B.render_guardrail(g)

    check("G1 keeps the S1/pathwise qualifier in policy",
          "S1 / pathwise" in g.policy or "S1/pathwise" in g.policy)
    check("G1 policy names the S2 condition", "P(τ<∞)>0" in g.policy)
    check("G1 policy names the S3 condition", "P(τ=∞)=0" in g.policy)
    check("G1 policy forbids the unqualified process-level verdict",
          "process-level" in g.policy and "不得" in g.policy)

    # The regression itself: an unqualified "τ<∞ ⇒ not a stable ISP" must not
    # appear as a standalone licensed claim.
    check("G1 does not license the unqualified claim",
          "唯一可无条件陈述的是" not in rendered)

    # The 1.3 stratification clause must be among the verbatim extracts, since
    # dropping it as "revision noise" is what allowed the regression.
    extracts = " ".join(text for _, text in g.extracts)
    check("G1 extracts include the stratification clause",
          "stratified by semantics" in extracts)
    check("G1 extracts include the S1 pathwise wording",
          "S1 pathwise" in extracts)

    check("G1 flags that OPEN_TENSIONS does not register the gap",
          "OPEN_TENSIONS" in g.interpretation or "OPEN_TENSIONS" in g.policy)


# --------------------------------------------------------------------------
# Provenance labelling — extract vs interpretation must stay separable
# --------------------------------------------------------------------------

def test_guardrail_sections() -> None:
    for factory in (B.guard_p1_t07, B.guard_dqo, B.guard_hooks, B.guard_shorthands):
        g = factory()
        rendered = B.render_guardrail(g)
        check(f"{g.gid} labels its interpretation as generated",
              "GENERATED INTERPRETATION" in rendered)
        check(f"{g.gid} labels its usage policy", "USAGE POLICY" in rendered)
        check(f"{g.gid} cites a policy source", bool(g.policy_source.strip()))
        if g.extracts:
            check(f"{g.gid} labels its source extract", "SOURCE EXTRACT" in rendered)


# --------------------------------------------------------------------------
# fail-loud — a missing anchor must abort, never degrade silently
# --------------------------------------------------------------------------

def test_fail_loud() -> None:
    real = B.read_text
    cases = [
        ("audit status block", "Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md",
         B.guard_p1_t07),
        ("theorem body", "Core/SRT_Core_21b_Constitutive_Theorems.md", B.guard_p1_t07),
        ("STATUS embargo", "STATUS.md", B.guard_dqo),
        ("hook audit table", "Operations/Audits/Hook_Closure_Audit_2026-07-25.md",
         B.guard_hooks),
        ("claim ladder section", "SRT_AI_START.md", B.build_claim_discipline),
    ]
    for label, target, fn in cases:
        B.read_text = lambda rel, _t=target: ("" if rel == _t else real(rel))
        stderr, sys.stderr = sys.stderr, open(os.devnull, "w")  # expected aborts are noisy
        try:
            fn()
            FAILURES.append(f"fail-loud {label}: did not abort on a missing anchor")
        except SystemExit as exc:
            if not exc.code:
                FAILURES.append(f"fail-loud {label}: exited 0")
        finally:
            sys.stderr.close()
            sys.stderr = stderr
            B.read_text = real


# --------------------------------------------------------------------------
# determinism — same provenance + same sources must give identical bytes
# --------------------------------------------------------------------------

def test_determinism() -> None:
    prov = B.Provenance(sha="deadbee", branch="test-branch",
                        generated="2026-01-01", dirty=False)
    with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
        B.generate(prov, Path(a))
        B.generate(prov, Path(b))
        names_a = sorted(p.name for p in Path(a).glob("*.md"))
        names_b = sorted(p.name for p in Path(b).glob("*.md"))
        check("determinism: same file set", names_a == names_b)
        for name in names_a:
            same = (Path(a) / name).read_bytes() == (Path(b) / name).read_bytes()
            check(f"determinism: {name} byte-identical", same)

        # Every bundle in one run must record the same provenance. This is the
        # bug where a per-bundle `git status` let bundle 1 say clean and the
        # rest say dirty, because writing bundle 1 dirtied the tree.
        for name in names_a:
            fm, _ = B.split_frontmatter((Path(a) / name).read_text(encoding="utf-8"))
            check(f"provenance sha in {name}", fm.get("source_commit") == "deadbee",
                  f"got {fm.get('source_commit')}")
            check(f"provenance date in {name}", fm.get("generated") == "2026-01-01",
                  f"got {fm.get('generated')}")
            check(f"provenance dirty in {name}", fm.get("source_dirty") == "false",
                  f"got {fm.get('source_dirty')}")


def test_porcelain_path() -> None:
    """`git()` strips stdout, so the first porcelain line loses its leading
    space and fixed-width slicing eats a character off the path. That bug hid
    behind a fake whose payload was never strip()ed."""
    cases = [
        ("M Operations/Context_Bundles/README.md",  # first line, already stripped
         "Operations/Context_Bundles/README.md"),
        (" M Operations/Context_Bundles/SPINE.md",
         "Operations/Context_Bundles/SPINE.md"),
        ("?? scripts/new_file.py", "scripts/new_file.py"),
        ("MM Core/SRT_Core_22_Equations.md", "Core/SRT_Core_22_Equations.md"),
        ("R  Core/old.md -> Core/new.md", "Core/new.md"),
        ("", ""),
    ]
    for line, want in cases:
        got = B.porcelain_path(line)
        check(f"porcelain_path({line!r})", got == want, f"got {got!r}, want {want!r}")


def test_dirty_excludes_bundle_dir() -> None:
    """The bundles' own churn must not count as a dirty source tree."""
    real = B.git

    def with_status(payload: str):
        def fake(*args: str) -> str:
            # Mirror git(): the real helper strips the whole stdout, which is
            # exactly what removed the first line's leading space.
            return payload.strip() if args[:2] == ("status", "--porcelain") else real(*args)
        return fake

    bundle_only = (
        " M Operations/Context_Bundles/README.md\n"
        " M Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_SPINE.md"
    )
    B.git = with_status(bundle_only)
    try:
        check("dirty check ignores the bundle dir", B.working_tree_dirty() is False)
    finally:
        B.git = real

    B.git = with_status(" M Core/SRT_Core_22_Equations.md")
    try:
        check("dirty check still catches source edits", B.working_tree_dirty() is True)
    finally:
        B.git = real

    # A source edit listed after bundle churn must still register.
    B.git = with_status(bundle_only + "\n M STATUS.md")
    try:
        check("dirty check catches a source edit among bundle churn",
              B.working_tree_dirty() is True)
    finally:
        B.git = real


def test_shallow_repo_guard() -> None:
    """A shallow clone makes `git log -1 -- <file>` return the graft commit's
    date for every file, so the bundles would report the entire canonical spine
    as changed today. That is silently plausible and completely wrong, so the
    builder must abort rather than emit it."""
    real = B.git

    def shallow(*args: str) -> str:
        if args[:2] == ("rev-parse", "--is-shallow-repository"):
            return "true"
        return real(*args)

    B.git = shallow
    stderr, sys.stderr = sys.stderr, open(os.devnull, "w")
    try:
        B.require_full_history()
        FAILURES.append("shallow guard: did not abort on a shallow clone")
    except SystemExit as exc:
        if not exc.code:
            FAILURES.append("shallow guard: exited 0")
    finally:
        sys.stderr.close()
        sys.stderr = stderr
        B.git = real

    # generate() must be gated by the same guard, not just the helper.
    B.git = shallow
    stderr, sys.stderr = sys.stderr, open(os.devnull, "w")
    try:
        with tempfile.TemporaryDirectory() as td:
            B.generate(B.Provenance("x", "y", "2026-01-01", False), Path(td))
        FAILURES.append("shallow guard: generate() ran on a shallow clone")
    except SystemExit as exc:
        if not exc.code:
            FAILURES.append("shallow guard: generate() exited 0")
    finally:
        sys.stderr.close()
        sys.stderr = stderr
        B.git = real

    check("shallow guard: real repo is not shallow", B.is_shallow_repo() is False)


# --------------------------------------------------------------------------
# 交付契约：上下文预算与 manifest 完备性（旧版被驳回的两点）
# --------------------------------------------------------------------------

def test_context_budget() -> None:
    """推荐组合必须留出余量；禁止组合必须确实超预算。

    旧版把 `SPINE + COMPACTCORE`（约 199K）推荐为 200K 窗口的跨域方案，等于不给
    系统提示、问题和输出留位置。预算现在是显式常量并在构建时强制。"""
    check("预算上限 = 窗口 − 余量",
          B.MAX_RECOMMENDED_LOAD == B.CONTEXT_WINDOW - B.HEADROOM_RESERVE)
    check("余量至少 25K", B.HEADROOM_RESERVE >= 25_000,
          f"got {B.HEADROOM_RESERVE}")

    prov = B.Provenance("budget", "test", "2026-01-01", False)
    with tempfile.TemporaryDirectory() as td:
        out = Path(td)
        B.generate(prov, out)   # generate() 内部已跑 check_budgets，失败会 SystemExit
        problems = B.check_budgets(out)
        for p in problems:
            FAILURES.append(f"budget: {p}")

        def tok(key: str) -> int:
            return B.estimate_tokens(
                (out / B.bundle_filename(key)).read_text(encoding="utf-8"))

        spine, compact = tok("SPINE"), tok("COMPACTCORE")
        check("SPINE 单包在预算内", spine <= B.MAX_RECOMMENDED_LOAD,
              f"{spine:,} > {B.MAX_RECOMMENDED_LOAD:,}")
        # 被驳回的那个组合必须仍然是超的——否则禁令没有数字依据。
        check("SPINE+COMPACTCORE 确实超预算",
              spine + compact > B.MAX_RECOMMENDED_LOAD,
              f"{spine + compact:,}")

        readme = (out / "README.md").read_text(encoding="utf-8")
        check("README 不把 SPINE+COMPACTCORE 列为推荐",
              "| 骨架路线" in readme and
              not re.search(r"^\|[^|]*推荐[^|]*\|.*`SPINE`.*`COMPACTCORE`", readme, re.M))
        check("README 声明了预算上限", f"{B.MAX_RECOMMENDED_LOAD:,}" in readme)


def test_manifest_completeness() -> None:
    """manifest 差异报告必须把「未收录」讲清楚，且不得声称自己是完备闭包。"""
    first_sources = B.parse_first_sources()
    mentioned, _broken = B.registry_mentions()
    check("First Sources 解析非空", len(first_sources) >= 10, f"got {len(first_sources)}")
    check("registry 提及解析非空", len(mentioned) >= 50, f"got {len(mentioned)}")

    # 每个骨架文件都要有分类依据，不能落进兜底。
    for path in B.SPINE:
        check(f"SPINE_BUCKETS 覆盖 {path}", path in B.SPINE_BUCKETS)

    # 旧版的实质缺口：收了七命题摘要，却漏掉它自己声明不能替代的两个文件。
    for path in ("Core_Law/SRT_Reference_Axioms.md",
                 "Core_Law/SRT_Reference_Ontology.md",
                 "Governance/SRT_CLAIM_MODE_AUDIT.md"):
        check(f"SPINE 已补入 {path}", path in B.SPINE)

    missing_fs = [p for p in first_sources
                  if p not in B.SPINE and (B.REPO_ROOT / p).is_file()]
    check("AI_START §2 First Sources 全部落入 SPINE", not missing_fs, f"缺 {missing_fs}")

    report = B.build_manifest_report(B.SPINE)
    check("报告声明本包不是完备闭包",
          "完备闭包" in report and "人工选择的高优先级 spine" in report)
    check("报告标明分类是生成器判断", "生成器的判断" in report)
    check("报告含未收录小节", "### 未收录支持文件" in report)
    check("报告列出 registry 未收数量", "文件存在、但本包未收" in report)


# --------------------------------------------------------------------------
# 装载协议自洽：领域包不得把用户引回被禁止的叠加方案
# --------------------------------------------------------------------------

def test_no_conflicting_load_instructions() -> None:
    """领域包曾写"请同时加载 SPINE"，而 README 同时禁止叠加——用户照领域包做就会
    掉回本 PR 要禁止的高负载组合。两处必须口径一致：切换，不是叠加。"""
    prov = B.Provenance("loadout", "test", "2026-01-01", False)
    with tempfile.TemporaryDirectory() as td:
        out = Path(td)
        B.generate(prov, out)
        for path in sorted(out.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            check(f"{path.name} 不含「同时加载」表述", "同时加载" not in text)
            check(f"{path.name} 不含「一并加载」表述", "一并加载" not in text)
        pointer = (out / "SRT_CONTEXT_BUNDLE_DOMAIN_AI.md").read_text(encoding="utf-8")
        check("领域包指示改用骨架路线", "改用骨架路线" in pointer)
        check("领域包明确禁止叠加骨架", "不要在本包之上再叠加骨架包" in pointer)


def test_loadouts_have_no_duplicate_sources() -> None:
    """推荐组合不得把同一来源文件装两遍。

    `COMPACTCORE + DOMAIN_X` 就是这种情况：COMPACTCORE 已含全部领域的 CompactCore，
    领域包又装一遍同样的 cores。即便仍在预算内，也是白费上下文。"""
    contents = {"SPINE": list(B.SPINE),
                "COMPACTCORE": [f for c in B.DOMAINS.values() for f in c["cores"]]}
    for key, cfg in B.DOMAINS.items():
        contents[f"DOMAIN_{key.upper()}"] = [*cfg["guards"], *cfg["nav"], *cfg["cores"]]

    for label, keys, _ in B.RECOMMENDED_LOADOUTS:
        seen: dict[str, int] = {}
        for k in keys:
            for f in contents[k]:
                seen[f] = seen.get(f, 0) + 1
        dupes = sorted(f for f, n in seen.items() if n > 1)
        check(f"推荐组合「{label}」无重复来源文件", not dupes, f"重复 {dupes}")


# --------------------------------------------------------------------------
# provenance 真实性：source_commit 必须能对应上内容
# --------------------------------------------------------------------------

def test_provenance_cannot_be_forged() -> None:
    """伪造 / 过期的 source_commit 必须被拒。

    此前 `--check` 只做逐字比对，而比对用的是当前工作树，所以任意 SHA 都能"通过"。
    现在还要求：该 commit 存在、是 HEAD 的祖先、且此后来源文件未变。"""
    sources = B.all_source_files()
    real_head = B.git("rev-parse", "--short", "HEAD")
    check("all_source_files 非空", len(sources) > 20, f"got {len(sources)}")

    cases = [
        ("不存在的 SHA", B.Provenance("deadbee", "b", "2026-01-01", False)),
        ("占位值", B.Provenance("unknown", "b", "2026-01-01", False)),
        ("生成时工作树是脏的", B.Provenance(real_head, "b", "2026-01-01", True)),
    ]
    for label, prov in cases:
        stderr, sys.stderr = sys.stderr, open(os.devnull, "w")
        try:
            B.verify_provenance(prov, sources)
            FAILURES.append(f"provenance 伪造未被拒：{label}")
        except SystemExit as exc:
            if not exc.code:
                FAILURES.append(f"provenance 伪造检查 exit=0：{label}")
        finally:
            sys.stderr.close()
            sys.stderr = stderr

    # 真实 HEAD + 干净树必须通过。
    try:
        B.verify_provenance(B.Provenance(real_head, "b", "2026-01-01", False), sources)
    except SystemExit:
        FAILURES.append("真实 HEAD 的 provenance 被误拒")

    # 不能再有一个可以把任意字符串写进 provenance 的开关（注释里提到它是可以的）。
    src = (B.REPO_ROOT / "scripts" / "build_srt_context_bundles.py").read_text(encoding="utf-8")
    check("已移除 --source-ref 开关", 'add_argument("--source-ref"' not in src)
    check("capture_provenance 不再接受来源 SHA 参数",
          "def capture_provenance(generated_date" in src)


# --------------------------------------------------------------------------
# manifest 不得静默隐藏 registry 的失效路径
# --------------------------------------------------------------------------

def test_broken_registry_paths_surface() -> None:
    """registry 指向不存在文件的条目，必须出现在报告里而不是被 is_file() 过滤掉。"""
    exists, broken = B.registry_mentions()
    check("registry 存在路径集非空", len(exists) >= 50, f"got {len(exists)}")
    check("registry_mentions 返回失效集合", isinstance(broken, set))

    report = B.build_manifest_report(B.SPINE)
    if broken:
        check("报告含失效路径小节", "registry 提及但文件不存在" in report)
        for p in broken:
            check(f"报告点名失效路径 {p}", f"`{p}`" in report)
    check("报告区分「文件存在但未收」", "文件存在、但本包未收" in report)

    # 失效的 First Source 不得被算作「已全部收录」。
    real = B.parse_first_sources
    B.parse_first_sources = lambda: real() + ["Core_Law/__does_not_exist__.md"]
    try:
        r2 = B.build_manifest_report(B.SPINE)
        check("失效 First Source 不被算作已全部收录", "已全部收录" not in r2)
        check("失效 First Source 被点名", "__does_not_exist__" in r2)
    finally:
        B.parse_first_sources = real


def run() -> None:
    test_hook_grouping()
    test_p1_t07_semantics()
    test_guardrail_sections()
    test_fail_loud()
    test_determinism()
    test_porcelain_path()
    test_shallow_repo_guard()
    test_context_budget()
    test_manifest_completeness()
    test_no_conflicting_load_instructions()
    test_loadouts_have_no_duplicate_sources()
    test_provenance_cannot_be_forged()
    test_broken_registry_paths_surface()
    test_dirty_excludes_bundle_dir()

    if FAILURES:
        for failure in FAILURES:
            print(f"FAIL: {failure}")
        raise SystemExit(1)
    print("test_build_context_bundles: all cases pass")


if __name__ == "__main__":
    run()
