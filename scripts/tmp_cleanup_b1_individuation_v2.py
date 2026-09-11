from pathlib import Path

src_path = Path("scripts/tmp_cleanup_b1_individuation.py")
src = src_path.read_text(encoding="utf-8")
old = '''def replace_line_regex(path: str, pattern: str, replacement: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    out, n = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if n != 1:
        raise SystemExit(f"expected one regex line match in {path}: {pattern}; got {n}")
    p.write_text(out, encoding="utf-8")
'''
new = '''def replace_line_regex(path: str, pattern: str, replacement: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    rx = re.compile(pattern, re.MULTILINE)
    out, n = rx.subn(lambda _m: replacement, text, count=1)
    if n != 1:
        raise SystemExit(f"expected one regex line match in {path}: {pattern}; got {n}")
    p.write_text(out, encoding="utf-8")
'''
if old not in src:
    raise SystemExit("target helper not found in original B1 script")
src = src.replace(old, new, 1)
exec(compile(src, str(src_path), "exec"), {"__name__": "__main__"})
