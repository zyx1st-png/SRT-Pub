from pathlib import Path

p = Path("scripts/build_srt_context_bundles.py")
text = p.read_text(encoding="utf-8")
old = '''SPINE_BUCKETS: dict[str, tuple[str, str]] = {
    "_SRT_D_VALUE_CANONICAL.md": ("定义源", "registry §A.1 主锚点"),'''
new = '''SPINE_BUCKETS: dict[str, tuple[str, str]] = {
    "Core_Law/SRT_Generative_Ontology_Spine.md": ("定义源", "registry §A.0 跨 owner 生成主轴"),
    "_SRT_D_VALUE_CANONICAL.md": ("定义源", "registry §A.1 主锚点"),'''
if text.count(old) != 1:
    raise SystemExit(f"SPINE_BUCKETS anchor count={text.count(old)}")
p.write_text(text.replace(old, new, 1), encoding="utf-8")
print("registered generative ontology spine in SPINE_BUCKETS")
