from pathlib import Path

p = Path("scripts/build_srt_context_bundles.py")
text = p.read_text(encoding="utf-8")
old = '''SPINE = [
    "SRT_AI_START.md",
    "CANONICAL_REGISTRY.md",
    "Governance/SRT_CLAIM_LADDER.md",'''
new = '''SPINE = [
    "SRT_AI_START.md",
    "CANONICAL_REGISTRY.md",
    # 2026-09-11: cross-owner generative order now has its own canonical spine.
    # It must be loaded before claim-ladder/local owners so older canonical text
    # cannot silently override current formation / bearing routing.
    "Core_Law/SRT_Generative_Ontology_Spine.md",
    "Governance/SRT_CLAIM_LADDER.md",'''
if text.count(old) != 1:
    raise SystemExit(f"SPINE insertion anchor count={text.count(old)}")
p.write_text(text.replace(old, new, 1), encoding="utf-8")
print("added generative ontology spine to canonical context bundle inputs")
