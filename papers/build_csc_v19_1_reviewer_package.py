from __future__ import annotations

import hashlib
import lzma
import zipfile
from pathlib import Path

PAPERS = Path(__file__).resolve().parent
SUP = PAPERS / "costly_selective_closure_supplement"
OUT = PAPERS / "CostlySelectiveClosure_v19_1_REVIEWER_EVIDENCE_PACKAGE.zip"
FIXED_ZIP_TIME = (2026, 9, 16, 0, 0, 0)

E4_CHUNKS_REL = "artifacts/E4_first_confirmatory_chunks"
E4_XZ_ARCHIVE = "artifacts/E4_first_confirmatory_consequence_scope_results_2026-09-15.json.xz"
E4_RAW_ARCHIVE = "full_first_confirmatory/consequence_scope_results.json"
EXPECTED_E4_XZ_SIZE = 88872
EXPECTED_E4_XZ_SHA256 = "283fac7d641d77ea937ccc65f120d750c9b7740bc6b1f29857e84188df639a84"
EXPECTED_E4_JSON_SIZE = 10112971
EXPECTED_E4_JSON_SHA256 = "74b4452a90231dbefdac82fc18373cbecf346df75948092366cb49e6a23406b5"

E4_CHUNK_SPECS = [
    ("part00.bin", 8192, "f80da11a6a56d52d73cb381e59af4379ccec095a886ddcafad36670b2ff32a1c"),
    ("part01.bin", 8192, "789a0fe61bcee78390544747ee87e74f1a20ee055e944b0e7ef7d09075d24f22"),
    ("part02.bin", 8192, "526e5654876e7dcf2553f54422812dfd982daf2276a3d679ba9980ab960fb2f3"),
    ("part03.bin", 8192, "42d56d915e83ad87c7fac383b0ae0d2c37f40203a2d515cdedd95c62108e8a6a"),
    ("part04.bin", 8192, "c64baa6368e988856ef2075203d021524c7304a83d0f87b66865b606ce53bde8"),
    ("part05.bin", 8192, "545fc28354e49ecd2d93e62c6d6744e554df0c23f08822338e321f8ca1ae112b"),
    ("part06.bin", 8192, "80d72e218ae30ef0bae418f2d8c4a41ad9edd427307e7153add404394859e5c4"),
    ("part07.bin", 8192, "66388896cb37c57ea48729956241646388c3ba09d3277793d061ef4ea8a49b6e"),
    ("part08.bin", 8192, "9f6ab073b42f040b66594b88822501764632e3bd3cdd68bdf56ca3aa530f67c0"),
    ("part09.bin", 8192, "4166052843442708c2d3499e5e81d1c7383883de76436be7fe130075f58e3763"),
    ("part10.bin", 6952, "048c4c1e3f9277e39cc3f894ccf457189881b5210457cfb4d142bc8e6790fb30"),
]

WHITELIST = [
    "run_main.py",
    "run_zero_penalty.py",
    "run_lives_gradient.py",
    "run_payoff_sweep.py",
    "run_common_state_probe.py",
    "src/csc_experiment.py",
    "src/csc_robustness.py",
    "src/csc_probe.py",
    "results/main_results.json",
    "results/zero_penalty_results.json",
    "results/lives_gradient_results.json",
    "results/payoff_sweep_results.json",
    "results/common_state_probe.json",
    "EXPERIMENT2_RECOVERABILITY_PREREGISTRATION.md",
    "EXPERIMENT2_RECOVERABILITY_RESULT.md",
    "run_recoverability_gradient.py",
    "src/csc_recoverability.py",
    "results/recoverability_gradient_results.json",
    "EXPERIMENT3_CONSEQUENCE_RECOVERY_PREREGISTRATION.md",
    "EXPERIMENT3_CONSEQUENCE_RECOVERY_RESULT.md",
    "run_consequence_recovery.py",
    "src/csc_consequence_recovery.py",
    "results/consequence_recovery_results.json",
    "EXPERIMENT4_CONSEQUENCE_SCOPE_PREREGISTRATION.md",
    "EXPERIMENT4_CONSEQUENCE_SCOPE_ADJUDICATION.md",
    "run_consequence_scope.py",
    "src/csc_consequence_scope.py",
    "results/consequence_scope_results_E4_confirmatory_record.json",
    "analyze_e4_individual_latency_exploratory.py",
    "results/consequence_scope_E4_individual_latency_exploratory.json",
    "figures/figure1_experiment_architectures_v19.svg",
    "figures/figure2_evidence_summary_v19_1.svg",
    "generate_v19_1_evidence_summary.py",
    "requirements.txt",
    "requirements-probe-lock.txt",
    "LICENSE",
]

FORBIDDEN_ARCHIVE_NAMES = {
    "README.md",
    "CITATION.cff",
    "CONSEQUENCE_SCOPE_MECHANISM_AUDIT_2026-09-15.md",
    "CONSEQUENCE_SCOPE_MECHANISM_AUDIT_POST_E4_CLOSURE_2026-09-15.md",
    "EXPERIMENT2_POSTRESULT_THEORY_AUDIT.md",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    info.create_system = 3
    return info


def reconstruct_e4_xz() -> bytes:
    chunks_dir = SUP / E4_CHUNKS_REL
    pieces: list[bytes] = []
    for filename, expected_size, expected_hash in E4_CHUNK_SPECS:
        path = chunks_dir / filename
        if not path.is_file():
            raise RuntimeError(f"missing preserved E4 chunk: {filename}")
        data = path.read_bytes()
        if len(data) != expected_size:
            raise RuntimeError(f"E4 chunk size mismatch: {filename}")
        if sha256(data) != expected_hash:
            raise RuntimeError(f"E4 chunk hash mismatch: {filename}")
        pieces.append(data)

    xz_bytes = b"".join(pieces)
    if len(xz_bytes) != EXPECTED_E4_XZ_SIZE:
        raise RuntimeError("reconstructed E4 XZ size mismatch")
    if sha256(xz_bytes) != EXPECTED_E4_XZ_SHA256:
        raise RuntimeError("reconstructed E4 XZ hash mismatch")
    return xz_bytes


def load_payload() -> dict[str, bytes]:
    reviewer_readme = SUP / "REVIEWER_README_v19_1.txt"
    if not reviewer_readme.is_file():
        raise RuntimeError("missing v19.1 reviewer README")

    payload: dict[str, bytes] = {"README.txt": reviewer_readme.read_bytes()}

    for rel in WHITELIST:
        src = SUP / rel
        if not src.is_file():
            raise RuntimeError(f"missing reviewer-package source: {rel}")
        payload[rel] = src.read_bytes()

    xz_bytes = reconstruct_e4_xz()
    payload[E4_XZ_ARCHIVE] = xz_bytes

    raw_json = lzma.decompress(xz_bytes)
    if len(raw_json) != EXPECTED_E4_JSON_SIZE:
        raise RuntimeError("decompressed E4 first-confirmatory JSON size mismatch")
    if sha256(raw_json) != EXPECTED_E4_JSON_SHA256:
        raise RuntimeError("decompressed E4 first-confirmatory JSON hash mismatch")
    payload[E4_RAW_ARCHIVE] = raw_json

    return payload


def validate_payload(payload: dict[str, bytes]) -> None:
    names = set(payload)
    for forbidden in FORBIDDEN_ARCHIVE_NAMES:
        if forbidden in names:
            raise RuntimeError(f"forbidden historical/internal file entered package: {forbidden}")

    if any(name.startswith(".git/") or "/.git/" in name for name in names):
        raise RuntimeError("Git metadata entered reviewer package")

    readme = payload["README.txt"].decode("utf-8")
    required_readme = [
        "Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents",
        "post-hoc exploratory only",
        "does not claim that Experiment 4 quantitatively explains a fraction",
        "E4 first-confirmatory artifact",
    ]
    for phrase in required_readme:
        if phrase not in readme:
            raise RuntimeError(f"reviewer README missing required boundary: {phrase}")

    forbidden_readme = [
        "Anonymous author(s) (double-blind submission)",
        "isolates V",
        "four components are",
        "V — irreversible vulnerability",
    ]
    for phrase in forbidden_readme:
        if phrase in readme:
            raise RuntimeError(f"stale supplement framing in reviewer README: {phrase}")


def build_manifest(payload: dict[str, bytes]) -> bytes:
    lines = [
        "# SHA-256 manifest — CSC v19.1 reviewer evidence package",
        "# Generated from the exact bytes placed in the ZIP.",
        "",
    ]
    for name in sorted(payload):
        lines.append(f"{sha256(payload[name])}  {name}")
    lines.append("")
    return "\n".join(lines).encode("utf-8")


def build() -> tuple[str, int]:
    payload = load_payload()
    validate_payload(payload)
    payload["MANIFEST_SHA256.txt"] = build_manifest(payload)

    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for name in sorted(payload):
            zf.writestr(zip_info(name), payload[name])

    package_bytes = OUT.read_bytes()
    return sha256(package_bytes), len(package_bytes)


def main() -> None:
    package_hash, package_size = build()
    print(f"wrote {OUT.relative_to(PAPERS.parent)}")
    print(f"package_size_bytes={package_size}")
    print(f"package_sha256={package_hash}")
    print("journal_submission=NOT_PERFORMED")


if __name__ == "__main__":
    main()
