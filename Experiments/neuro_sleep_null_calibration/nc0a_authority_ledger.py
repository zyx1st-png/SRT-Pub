"""Cross-directory authorization and cumulative-cost ledger.

The launcher never creates this store. An independent operator initializes the
ledger and its separately located tip anchor before signing the resource policy.
An absent or inconsistent store is an audit stop, not a new-run opportunity.
"""

from __future__ import annotations

from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import stat
import tempfile


ZERO_SHA256 = "0" * 64


class AuthorityLedgerError(RuntimeError):
    pass


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _check_paths(ledger_path: Path, anchor_path: Path) -> None:
    if not ledger_path.is_absolute() or not anchor_path.is_absolute():
        raise AuthorityLedgerError("Authority paths must be absolute")
    if ledger_path.is_symlink() or anchor_path.is_symlink():
        raise AuthorityLedgerError("Authority files may not be symlinks")
    ledger_path, anchor_path = ledger_path.resolve(), anchor_path.resolve()
    if ledger_path == anchor_path or ledger_path.parent == anchor_path.parent:
        raise AuthorityLedgerError(
            "Authority log and tip anchor must be absolute and separately located")


def _verify_records(raw: bytes) -> tuple[list[dict], str]:
    if raw and not raw.endswith(b"\n"):
        raise AuthorityLedgerError("Partial authority ledger tail; manual audit required")
    previous = ZERO_SHA256
    records = []
    for sequence, line in enumerate(raw.splitlines()):
        try:
            item = json.loads(line)
            digest = item.pop("record_sha256")
        except (ValueError, KeyError, TypeError) as exc:
            raise AuthorityLedgerError("Malformed authority ledger") from exc
        if item.get("sequence") != sequence or item.get("previous_sha256") != previous:
            raise AuthorityLedgerError("Authority ledger sequence or predecessor mismatch")
        expected = hashlib.sha256(_canonical(item)).hexdigest()
        if digest != expected:
            raise AuthorityLedgerError("Authority ledger digest mismatch")
        previous = digest
        records.append(item)
    return records, previous


def initialize_authority_store(ledger_path: str | Path,
                               anchor_path: str | Path) -> None:
    """Provision an empty store out of band; never called by a run launcher."""
    ledger, anchor = Path(ledger_path), Path(anchor_path)
    _check_paths(ledger, anchor)
    if ledger.exists() or anchor.exists():
        raise AuthorityLedgerError("Authority store already exists; it cannot be reset")
    ledger.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    anchor.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    for directory in (ledger.parent, anchor.parent):
        mode = stat.S_IMODE(directory.stat().st_mode)
        if mode & 0o022:
            raise AuthorityLedgerError(
                "Authority log and anchor directories may not be group/world writable")
    fd = os.open(ledger, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
    payload = _canonical({"format": "NC0A_AUTHORITY_TIP_V1",
                          "sequence": 0, "tip_sha256": ZERO_SHA256}) + b"\n"
    fd = os.open(anchor, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(fd, payload)
        os.fsync(fd)
    finally:
        os.close(fd)
    for directory in (ledger.parent, anchor.parent):
        dfd = os.open(directory, os.O_RDONLY)
        try:
            os.fsync(dfd)
        finally:
            os.close(dfd)


class AuthorityLedger:
    def __init__(self, ledger_path: str | Path, anchor_path: str | Path):
        self.path = Path(ledger_path).resolve()
        self.anchor_path = Path(anchor_path).resolve()
        _check_paths(self.path, self.anchor_path)
        if not self.path.is_file() or not self.anchor_path.is_file():
            raise AuthorityLedgerError(
                "Authority ledger or independent tip anchor is missing; refusing authorization")
        self.fd = os.open(self.path, os.O_WRONLY | os.O_APPEND)
        try:
            fcntl.flock(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            ledger_stat = os.fstat(self.fd)
            anchor_stat = self.anchor_path.stat()
            if ledger_stat.st_nlink != 1:
                raise AuthorityLedgerError("Authority ledger hard links are prohibited")
            if anchor_stat.st_nlink != 1:
                raise AuthorityLedgerError("Authority tip hard links are prohibited")
            if (stat.S_IMODE(ledger_stat.st_mode) & 0o022 or
                stat.S_IMODE(anchor_stat.st_mode) & 0o022):
                raise AuthorityLedgerError(
                    "Authority ledger and anchor files may not be group/world writable")
            for directory in (self.path.parent, self.anchor_path.parent):
                if stat.S_IMODE(directory.stat().st_mode) & 0o022:
                    raise AuthorityLedgerError(
                        "Authority log and anchor directories may not be group/world writable")
            self.records, self.tip = _verify_records(self.path.read_bytes())
            anchor = json.loads(self.anchor_path.read_text(encoding="utf-8"))
            if (anchor.get("format") != "NC0A_AUTHORITY_TIP_V1" or
                anchor.get("sequence") != len(self.records) or
                anchor.get("tip_sha256") != self.tip):
                raise AuthorityLedgerError(
                    "Authority log differs from its independent tip anchor")
            self.sequence = len(self.records)
        except BaseException:
            os.close(self.fd)
            raise

    def append(self, event: dict) -> str:
        record = {"sequence": self.sequence, "previous_sha256": self.tip,
                  "event": event}
        digest = hashlib.sha256(_canonical(record)).hexdigest()
        line = _canonical({**record, "record_sha256": digest}) + b"\n"
        view = memoryview(line)
        while view:
            written = os.write(self.fd, view)
            if written <= 0:
                raise AuthorityLedgerError("Short write to authority ledger")
            view = view[written:]
        os.fsync(self.fd)
        new_sequence = self.sequence + 1
        payload = _canonical({"format": "NC0A_AUTHORITY_TIP_V1",
                              "sequence": new_sequence,
                              "tip_sha256": digest}) + b"\n"
        fd, tmp_name = tempfile.mkstemp(prefix=".nc0a-tip-",
                                        dir=self.anchor_path.parent)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(tmp_name, self.anchor_path)
            dfd = os.open(self.anchor_path.parent, os.O_RDONLY)
            try:
                os.fsync(dfd)
            finally:
                os.close(dfd)
        finally:
            if os.path.exists(tmp_name):
                os.unlink(tmp_name)
        self.records.append({"sequence": self.sequence,
                             "previous_sha256": self.tip,
                             "event": event})
        self.sequence, self.tip = new_sequence, digest
        return digest

    def begin(self, *, experiment_id: str, run_dir: str | Path,
              policy_sha256: str, approval_sha256: str,
              wall_budget_seconds: float,
              cpu_budget_seconds: float, max_invocations: int,
              pre_start_check=None) -> dict:
        if max_invocations not in (1, 2):
            raise AuthorityLedgerError("Only one or two signed operational invocations are allowed")
        resolved_run = str(Path(run_dir).resolve())
        events = [row["event"] for row in self.records]
        registrations = [e for e in events if e.get("event") == "run_registered" and
                         e.get("experiment_id") == experiment_id]
        if len(registrations) > 1:
            raise AuthorityLedgerError("Duplicate experiment registration in authority log")
        is_resume = bool(registrations)
        if registrations:
            registration = registrations[0]
            if (registration.get("run_dir") != resolved_run or
                registration.get("policy_sha256") != policy_sha256 or
                registration.get("approval_sha256") != approval_sha256):
                raise AuthorityLedgerError(
                    "This signed experiment identity is already bound to another run or approval")
        else:
            self.append({"event": "run_registered", "experiment_id": experiment_id,
                         "run_dir": resolved_run, "policy_sha256": policy_sha256,
                         "approval_sha256": approval_sha256,
                         "utc": datetime.now(timezone.utc).isoformat()})
            events.append(self.records[-1]["event"])

        starts = [e for e in events if e.get("event") == "invocation_started" and
                  e.get("experiment_id") == experiment_id]
        finishes = [e for e in events if e.get("event") == "invocation_finished" and
                    e.get("experiment_id") == experiment_id]
        start_ids = [e.get("invocation") for e in starts]
        finish_ids = [e.get("invocation") for e in finishes]
        if (len(set(start_ids)) != len(start_ids) or
            len(set(finish_ids)) != len(finish_ids) or
            any(item not in start_ids for item in finish_ids)):
            raise AuthorityLedgerError("Invocation accounting is inconsistent; manual audit required")
        finished_ids = {e.get("invocation") for e in finishes}
        pending = [e for e in starts if e.get("invocation") not in finished_ids]
        if pending:
            raise AuthorityLedgerError(
                "Prior invocation has unknown resource cost; independent reconciliation is required")
        if any(e.get("event") == "run_completed" and
               e.get("experiment_id") == experiment_id for e in events):
            raise AuthorityLedgerError("Signed experiment is already complete")
        if any(e.get("status") == "completed" for e in finishes):
            raise AuthorityLedgerError("A completed invocation cannot be restarted")
        if len(starts) >= max_invocations:
            raise AuthorityLedgerError("Signed operational invocation allowance is exhausted")
        if [e.get("invocation") for e in starts] != list(range(1, len(starts) + 1)):
            raise AuthorityLedgerError("Invocation sequence is inconsistent; manual audit required")
        if len(finishes) != len(starts):
            raise AuthorityLedgerError("Invocation accounting is inconsistent; manual audit required")
        wall_used = sum(float(e["usage"]["wall_seconds"]) for e in finishes)
        cpu_used = sum(float(e["usage"]["cpu_seconds"]) for e in finishes)
        if wall_used >= wall_budget_seconds or cpu_used >= cpu_budget_seconds:
            raise AuthorityLedgerError("Cumulative signed resource budget is exhausted")
        invocation = len(starts) + 1
        if pre_start_check is not None:
            pre_start_check(is_resume)
        self.append({"event": "invocation_started", "experiment_id": experiment_id,
                     "invocation": invocation, "utc": datetime.now(timezone.utc).isoformat(),
                     "prior_wall_seconds": wall_used, "prior_cpu_seconds": cpu_used})
        return {"invocation": invocation, "wall_seconds": wall_used,
                "cpu_seconds": cpu_used, "is_resume": is_resume}

    def audit_anchors(self, experiment_id: str) -> list[str]:
        return [e.get("watchdog_audit_sha256") for row in self.records
                if (e := row["event"]).get("event") == "invocation_finished" and
                e.get("experiment_id") == experiment_id]

    def finish(self, *, experiment_id: str, invocation: int,
               status: str, usage: dict, audit_sha256: str | None,
               completed: bool = False) -> None:
        wall = float(usage.get("wall_seconds", -1))
        cpu = float(usage.get("cpu_seconds", -1))
        if not (0 <= wall < float("inf") and 0 <= cpu < float("inf")):
            raise AuthorityLedgerError("Terminal resource cost is missing or invalid")
        if (status not in ("completed", "failed", "stopped") or
            not isinstance(audit_sha256, str) or
            len(audit_sha256) != 64 or
            any(c not in "0123456789abcdef" for c in audit_sha256)):
            raise AuthorityLedgerError("Terminal status or watchdog audit anchor is invalid")
        if completed != (status == "completed"):
            raise AuthorityLedgerError("Completion marker disagrees with the terminal status")
        events = [row["event"] for row in self.records]
        starts = [e for e in events if e.get("event") == "invocation_started" and
                  e.get("experiment_id") == experiment_id and e.get("invocation") == invocation]
        finishes = [e for e in events if e.get("event") == "invocation_finished" and
                    e.get("experiment_id") == experiment_id and e.get("invocation") == invocation]
        if len(starts) != 1 or finishes:
            raise AuthorityLedgerError("No unique pending invocation to finish")
        self.append({"event": "invocation_finished", "experiment_id": experiment_id,
                     "invocation": invocation, "status": status,
                     "usage": {"wall_seconds": wall, "cpu_seconds": cpu},
                     "watchdog_audit_sha256": audit_sha256,
                     "utc": datetime.now(timezone.utc).isoformat()})
        if completed:
            self.append({"event": "run_completed", "experiment_id": experiment_id,
                         "invocation": invocation,
                         "utc": datetime.now(timezone.utc).isoformat()})

    def close(self) -> None:
        fcntl.flock(self.fd, fcntl.LOCK_UN)
        os.close(self.fd)

    def __enter__(self) -> "AuthorityLedger":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
