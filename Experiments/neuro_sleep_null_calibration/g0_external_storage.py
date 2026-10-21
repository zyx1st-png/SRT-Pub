"""Fail-closed external-volume storage adapter for prospective G0 work.

This module is an integration boundary, not a G0 executor or authorization.
The removable volume holds immutable task artifacts; the control ledger and
its local tip anchor stay on the internal APFS volume. ExFAT mode bits and a
single local hash chain are integrity aids, not access control or an
independent backup.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import plistlib
import re
import shutil
import stat
import subprocess
import threading
import time
import uuid
from contextlib import contextmanager
from typing import Callable, Iterable, Mapping

from nc0a_watchdog import (HashChainLog, WatchdogError, WatchdogLimits,
                           supervise, verify_hash_chain)


EXPECTED_KIOXIA_VOLUME_UUID = "0E5DC84B-1E22-3C9B-9E3B-220EBA8607C1"
GIB = 1024 ** 3
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,119}$")
_STREAM_WRITE_CHUNK_BYTES = 1 << 20
_OPERATIONAL_STORAGE_CODES = frozenset({
    "G0_EXTERNAL_MOUNT_UNAVAILABLE",
    "G0_EXTERNAL_VOLUME_IDENTITY_MISMATCH",
    "G0_EXTERNAL_FILESYSTEM_MISMATCH",
    "G0_EXTERNAL_SPACE_LIMIT",
    "G0_INTERNAL_SPACE_LIMIT",
    "G0_EXTERNAL_IO_FAILURE",
    "G0_EXTERNAL_POSTWRITE_IDENTITY_FAILURE",
    "WALL_LIMIT", "CPU_LIMIT_WITH_TERMINATION_MARGIN",
    "AGGREGATE_RSS_LIMIT", "RUN_DISK_ALLOCATION_LIMIT",
    "FREE_DISK_RESERVE_BREACH", "CASE_WALL_LIMIT", "ORACLE_WALL_LIMIT",
    "HOST_MEMORY_PRESSURE_LIMIT", "SWAP_GROWTH_LIMIT",
    "SWAP_FREE_RESERVE_BREACH", "BOOT_VOLUME_FREE_DISK_RESERVE_BREACH",
    "VM_VOLUME_FREE_DISK_RESERVE_BREACH", "SLEEP_ASSERTION_LOST",
    "AC_POWER_LOST", "THERMAL_WARNING",
    # This exact typed reason may be used only when an independent supervisor
    # has established an operational interruption. The G0 executor records an
    # unexplained BrokenProcessPool/worker exit as UNKNOWN and never retries it.
    "G0_WORKER_PROCESS_EXIT",
})


class G0StorageError(RuntimeError):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


class RecoveryRefused(G0StorageError):
    pass


@dataclass(frozen=True)
class VolumeInfo:
    mount_point: str
    volume_uuid: str
    filesystem: str
    device_identifier: str
    st_dev: int
    st_ino: int
    free_bytes: int


class DiskUtilVolumeProbe:
    """Read volume identity from macOS diskutil and the live mount table."""

    def inspect(self, mount_point: str | Path) -> VolumeInfo:
        path = Path(mount_point)
        try:
            if path.is_symlink() or not path.is_dir():
                raise G0StorageError("G0_EXTERNAL_MOUNT_UNAVAILABLE",
                                     f"Expected mount is absent: {path}")
            completed = subprocess.run(
                ["diskutil", "info", "-plist", str(path)], check=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
            payload = plistlib.loads(completed.stdout)
            if str(payload.get("MountPoint", "")) != str(path):
                raise G0StorageError("G0_EXTERNAL_MOUNT_UNAVAILABLE",
                                     f"diskutil does not report the requested path as a mount: {path}")
            current = path.stat()
            return VolumeInfo(
                mount_point=str(payload.get("MountPoint", "")),
                volume_uuid=str(payload.get("VolumeUUID", "")).upper(),
                filesystem=str(payload.get("FilesystemType", "")).lower(),
                device_identifier=str(payload.get("DeviceIdentifier", "")),
                st_dev=current.st_dev, st_ino=current.st_ino,
                free_bytes=shutil.disk_usage(path).free)
        except G0StorageError:
            raise
        except (OSError, subprocess.SubprocessError, ValueError, KeyError,
                TypeError, plistlib.InvalidFileException) as exc:
            raise G0StorageError("G0_EXTERNAL_MOUNT_UNAVAILABLE",
                                 f"Cannot verify volume at {path}: {exc}") from exc


@dataclass(frozen=True)
class ExternalStoragePolicy:
    """Candidate storage constraints from the draft resource amendment."""

    external_mount: Path = Path("/Volumes/KIOXIA")
    internal_mount: Path = Path("/System/Volumes/Data")
    expected_external_uuid: str = EXPECTED_KIOXIA_VOLUME_UUID
    expected_external_filesystem: str = "exfat"
    expected_internal_filesystem: str = "apfs"
    minimum_external_start_free_bytes: int = 54 * GIB
    minimum_external_reserve_free_bytes: int = 30 * GIB
    maximum_run_bytes: int = 24 * GIB
    minimum_internal_start_free_bytes: int = 30 * GIB
    minimum_internal_reserve_free_bytes: int = 30 * GIB
    maximum_projected_use_fraction: float = 0.70
    run_root_relative: str = "SRT-G0/RUNS"

    def __post_init__(self) -> None:
        for name in ("minimum_external_start_free_bytes",
                     "minimum_external_reserve_free_bytes", "maximum_run_bytes",
                     "minimum_internal_start_free_bytes",
                     "minimum_internal_reserve_free_bytes"):
            if type(getattr(self, name)) is not int or getattr(self, name) <= 0:
                raise ValueError(f"{name} must be a positive integer")
        if not (0 < self.maximum_projected_use_fraction < 1):
            raise ValueError("maximum_projected_use_fraction must be between zero and one")
        if self.expected_external_uuid.upper() != EXPECTED_KIOXIA_VOLUME_UUID:
            raise ValueError("This adapter is bound to the reviewed KIOXIA volume UUID")
        _safe_relative(self.run_root_relative)


@dataclass(frozen=True)
class RecoveryReport:
    completed_task_ids: tuple[str, ...]
    retryable_task_ids: tuple[str, ...]
    not_started_task_ids: tuple[str, ...]
    exhausted_task_ids: tuple[str, ...]


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _sha256_path(path: Path) -> str:
    if path.is_symlink() or not path.is_file():
        raise RecoveryRefused("G0_CONTROL_ARTIFACT_MISSING", f"Expected control artifact is absent or unsafe: {path.name}")
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _safe_relative(value: str) -> tuple[str, ...]:
    if not isinstance(value, str) or not value or "\\" in value:
        raise G0StorageError("G0_EXTERNAL_PATH_INVALID", "Storage path must be relative POSIX text")
    path = PurePosixPath(value)
    parts = path.parts
    if path.is_absolute() or not parts or any(p in ("", ".", "..") for p in parts):
        raise G0StorageError("G0_EXTERNAL_PATH_INVALID", "Absolute and escaping paths are forbidden")
    if any("\x00" in part for part in parts):
        raise G0StorageError("G0_EXTERNAL_PATH_INVALID", "NUL is not valid in a storage path")
    return tuple(parts)


def _open_absolute_directory(path: Path) -> int:
    """Open the requested directory without following a symlink at that path.

    macOS exposes stable system aliases such as /var -> /private/var in
    ancestors of temporary test directories. The mountpoint itself and every
    managed child are still checked with O_NOFOLLOW; diskutil supplies the
    authoritative mount identity for production paths.
    """
    absolute = Path(os.path.abspath(path))
    if not absolute.is_absolute():
        raise G0StorageError("G0_PATH_INVALID", "Directory must be absolute")
    try:
        info = absolute.lstat()
    except OSError:
        raise
    if stat.S_ISLNK(info.st_mode) or not stat.S_ISDIR(info.st_mode):
        raise G0StorageError("G0_PATH_SYMLINK", "Requested mount root must be a real directory")
    flags = os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(absolute, flags)
    if os.fstat(fd).st_dev != info.st_dev or os.fstat(fd).st_ino != info.st_ino:
        os.close(fd)
        raise G0StorageError("G0_PATH_CHANGED", "Directory changed while opening")
    return fd


def _open_or_create_dir(parent_fd: int, name: str, *, create: bool,
                        expected_dev: int) -> int:
    flags = os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)
    try:
        fd = os.open(name, flags, dir_fd=parent_fd)
    except FileNotFoundError:
        if not create:
            raise
        try:
            os.mkdir(name, 0o700, dir_fd=parent_fd)
        except FileExistsError:
            # Another supervised task may have created the same namespace
            # directory after our initial open failed. Re-open below with
            # O_NOFOLLOW and verify the device exactly as for an existing dir.
            pass
        # Sync the parent after either our mkdir or a racing creator's mkdir,
        # so a task result cannot become durable before this entry is.
        os.fsync(parent_fd)
        fd = os.open(name, flags, dir_fd=parent_fd)
        os.fsync(fd)
    info = os.fstat(fd)
    if info.st_dev != expected_dev:
        os.close(fd)
        raise G0StorageError("G0_PATH_CROSSES_VOLUME", "Directory crossed a volume boundary")
    return fd


def _open_or_create_beneath(root_fd: int, parts: tuple[str, ...],
                            expected_dev: int, *, create: bool) -> int:
    current = os.dup(root_fd)
    try:
        for part in parts:
            next_fd = _open_or_create_dir(current, part, create=create,
                                          expected_dev=expected_dev)
            os.close(current)
            current = next_fd
        return current
    except BaseException:
        os.close(current)
        raise


def _validate_existing_parent_beneath(root_fd: int, parts: tuple[str, ...],
                                      expected_dev: int) -> None:
    """Walk existing parent components without creating directories or following links."""
    current = os.dup(root_fd)
    try:
        for part in parts:
            try:
                next_fd = _open_or_create_dir(current, part, create=False,
                                              expected_dev=expected_dev)
            except FileNotFoundError:
                return
            except OSError as exc:
                raise G0StorageError("G0_EXTERNAL_PATH_UNSAFE",
                                     f"Unsafe existing path component: {part}") from exc
            os.close(current)
            current = next_fd
    finally:
        os.close(current)


def _tree_bytes(fd: int, expected_dev: int) -> int:
    total = 0
    for name in os.listdir(fd):
        info = os.stat(name, dir_fd=fd, follow_symlinks=False)
        if info.st_dev != expected_dev:
            raise G0StorageError("G0_PATH_CROSSES_VOLUME", "Found entry on another volume")
        if stat.S_ISLNK(info.st_mode):
            raise G0StorageError("G0_EXTERNAL_SYMLINK", f"Symlink in managed tree: {name}")
        if stat.S_ISDIR(info.st_mode):
            child = _open_or_create_dir(fd, name, create=False, expected_dev=expected_dev)
            try:
                total += _tree_bytes(child, expected_dev)
            finally:
                os.close(child)
        elif stat.S_ISREG(info.st_mode):
            total += info.st_size
        else:
            raise G0StorageError("G0_EXTERNAL_ENTRY_TYPE", f"Unsupported entry in managed tree: {name}")
    return total


def _hash_open_file(parent_fd: int, name: str, expected_dev: int) -> tuple[str, int]:
    fd = os.open(name, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0), dir_fd=parent_fd)
    digest = hashlib.sha256()
    size = 0
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_dev != expected_dev:
            raise G0StorageError("G0_EXTERNAL_ENTRY_TYPE", "Artifact is not a regular file on the expected volume")
        while True:
            block = os.read(fd, 1 << 20)
            if not block:
                break
            digest.update(block)
            size += len(block)
    finally:
        os.close(fd)
    return digest.hexdigest(), size


class G0ExternalStore:
    """Stores immutable task results on KIOXIA with APFS control accounting.

    The adapter is deliberately not a G0 scheduler. The caller supplies the
    frozen run UUID, expected task/seed inventory and attempt IDs. It never
    falls back to a path on the internal disk.
    """

    def __init__(self, *, run_uuid: str, internal_ledger_dir: str | Path,
                 policy: ExternalStoragePolicy = ExternalStoragePolicy(),
                 probe: object | None = None,
                 usage_provider: Callable[[str | Path], object] = shutil.disk_usage):
        try:
            parsed_uuid = uuid.UUID(run_uuid)
        except (ValueError, TypeError, AttributeError) as exc:
            raise G0StorageError("G0_RUN_UUID_INVALID", "run_uuid must be a UUID") from exc
        self.run_uuid = str(parsed_uuid)
        self.policy = policy
        self.probe = probe or DiskUtilVolumeProbe()
        self._require_os_mount = isinstance(self.probe, DiskUtilVolumeProbe)
        if (self._require_os_mount and
                Path(policy.external_mount) != Path("/Volumes/KIOXIA")):
            raise G0StorageError("G0_EXTERNAL_MOUNT_PATH_INVALID",
                                 "Production policy must use the reviewed KIOXIA mount path")
        self.usage_provider = usage_provider
        self.control_dir = Path(os.path.abspath(internal_ledger_dir))
        self._closed = False
        self._poisoned = False
        self._ledger_lock = threading.RLock()
        self._inflight_result_paths: set[str] = set()
        self._inflight_artifact_paths: set[str] = set()
        self._task_event_index: dict[str, dict[str, list[dict]]] = {}
        self._active_task_ids: set[str] = set()
        self._activity_manifest: dict | None = None
        self._activity_task_seeds: dict[str, str] | None = None
        self._activity_task_order: tuple[str, ...] | None = None
        self._activity_verified = False
        self._activity_execution_lock = threading.Lock()
        self._used_external_paths: set[str] = set()
        self._expected_external_paths: set[str] = set()
        self._committed_external_files: dict[str, dict] = {}
        self._watchdog_invocation_ids: set[int] = set()
        self._watchdog_invocations: dict[int, dict[str, dict | None]] = {}
        self._external_run_bytes = 0
        self._external_reserved_bytes = 0
        self._ledger_bytes = 0
        self._ledger_stat_signature: tuple[int, int, int, int, int] | None = None
        self._indexed_sequence = 0
        self._indexed_tip = "0" * 64
        self._has_prior_work = False
        self._recovery_verified = True
        self._mount_fd: int | None = None
        self._run_fd: int | None = None
        self._ledger_fd: int | None = None
        self._ledger: HashChainLog | None = None

        self._external_initial = self._inspect(policy.external_mount)
        self._internal_initial = self._inspect(policy.internal_mount)
        self._validate_initial_identities()
        self._validate_start_space()
        try:
            self._mount_fd = _open_absolute_directory(Path(self._external_initial.mount_point))
            if os.fstat(self._mount_fd).st_dev != self._external_initial.st_dev:
                raise G0StorageError("G0_EXTERNAL_MOUNT_UNAVAILABLE", "Mount changed during open")
            self._ledger_fd = self._prepare_internal_ledger(self.control_dir)
            ledger_path = self.control_dir / "storage-ledger.jsonl"
            anchor_path = self.control_dir / "storage-ledger.anchor.json"
            self._open_control_ledger(ledger_path, anchor_path)
            self._run_fd = _open_or_create_beneath(
                self._mount_fd,
                _safe_relative(policy.run_root_relative) + (self.run_uuid,),
                self._external_initial.st_dev, create=True)
            self._rebuild_incremental_indexes()
            self._append({"event": "g0_external_store_opened",
                          "run_uuid": self.run_uuid,
                          "external_volume_uuid": self._external_initial.volume_uuid,
                          "external_filesystem": self._external_initial.filesystem,
                          "external_device_identifier_observed": self._external_initial.device_identifier,
                          "internal_volume_uuid": self._internal_initial.volume_uuid,
                          "internal_filesystem": self._internal_initial.filesystem,
                          "policy": self._policy_record()})
            self.check_health()
        except BaseException:
            self.close()
            raise

    def _inspect(self, path: Path) -> VolumeInfo:
        try:
            result = self.probe.inspect(path)
        except G0StorageError as exc:
            if Path(path) == Path(self.policy.internal_mount):
                raise G0StorageError("G0_INTERNAL_VOLUME_IDENTITY_MISMATCH",
                                     f"Cannot verify internal APFS control volume: {path}") from exc
            raise
        except BaseException as exc:
            code = ("G0_INTERNAL_VOLUME_IDENTITY_MISMATCH"
                    if Path(path) == Path(self.policy.internal_mount)
                    else "G0_EXTERNAL_MOUNT_UNAVAILABLE")
            raise G0StorageError(code,
                                 f"Volume probe failed for {path}: {exc}") from exc
        return result

    def _validate_initial_identities(self) -> None:
        ext, internal = self._external_initial, self._internal_initial
        if self._require_os_mount and not os.path.ismount(self.policy.external_mount):
            raise G0StorageError("G0_EXTERNAL_MOUNT_UNAVAILABLE",
                                 "External data path is not an active mountpoint")
        if (ext.mount_point != str(self.policy.external_mount) or
                ext.volume_uuid.upper() != self.policy.expected_external_uuid.upper()):
            raise G0StorageError("G0_EXTERNAL_VOLUME_IDENTITY_MISMATCH",
                                 "Mounted external volume UUID or mount point does not match policy")
        if ext.filesystem.lower() != self.policy.expected_external_filesystem.lower():
            raise G0StorageError("G0_EXTERNAL_FILESYSTEM_MISMATCH",
                                 f"Expected {self.policy.expected_external_filesystem} on external volume")
        if (internal.mount_point != str(self.policy.internal_mount) or
                internal.filesystem.lower() != self.policy.expected_internal_filesystem.lower()):
            raise G0StorageError("G0_INTERNAL_VOLUME_IDENTITY_MISMATCH",
                                 "Control volume is not the expected internal APFS mount")
        if internal.volume_uuid.upper() == ext.volume_uuid.upper():
            raise G0StorageError("G0_VOLUMES_NOT_SEPARATE",
                                 "Control ledger and external data volume must be distinct")

    def _validate_start_space(self) -> None:
        ext_free = self.usage_provider(self.policy.external_mount).free
        internal_free = self.usage_provider(self.policy.internal_mount).free
        if ext_free < self.policy.minimum_external_start_free_bytes:
            raise G0StorageError("G0_EXTERNAL_SPACE_LIMIT",
                                 "External volume is below its independent startup free-space floor")
        if internal_free < self.policy.minimum_internal_start_free_bytes:
            raise G0StorageError("G0_INTERNAL_SPACE_LIMIT",
                                 "Internal APFS volume is below its independent startup free-space floor")
        self._external_start_free = ext_free
        self._internal_start_free = internal_free

    def _prepare_internal_ledger(self, ledger_dir: Path) -> int:
        if not ledger_dir.is_absolute():
            raise G0StorageError("G0_INTERNAL_LEDGER_PATH_INVALID", "Internal ledger path must be absolute")
        normalized = Path(os.path.abspath(ledger_dir))
        try:
            relative = normalized.relative_to(Path(self.policy.internal_mount))
        except ValueError as exc:
            raise G0StorageError("G0_INTERNAL_LEDGER_PATH_INVALID",
                                 "Control ledger must remain on the configured internal volume") from exc
        internal_fd = _open_absolute_directory(Path(self.policy.internal_mount))
        try:
            if not relative.parts:
                raise G0StorageError("G0_INTERNAL_LEDGER_PATH_INVALID",
                                     "Control ledger cannot be placed at the volume root")
            self._internal_root_dev = os.fstat(internal_fd).st_dev
            if self._internal_root_dev != self._internal_initial.st_dev:
                raise G0StorageError("G0_INTERNAL_VOLUME_IDENTITY_MISMATCH",
                                     "Internal mount changed while opening the ledger")
            internal_ledger_fd = _open_or_create_beneath(
                internal_fd, tuple(relative.parts), self._internal_root_dev, create=True)
            try:
                return os.dup(internal_ledger_fd)
            finally:
                os.close(internal_ledger_fd)
        finally:
            os.close(internal_fd)

    def _open_control_ledger(self, ledger_path: Path, anchor_path: Path) -> None:
        log_exists = ledger_path.exists() or ledger_path.is_symlink()
        anchor_exists = anchor_path.exists() or anchor_path.is_symlink()
        if ledger_path.is_symlink() or anchor_path.is_symlink():
            raise RecoveryRefused("G0_LEDGER_SYMLINK", "Control ledger files cannot be symlinks")
        if log_exists != anchor_exists:
            raise RecoveryRefused("G0_LEDGER_ANCHOR_MISSING", "Ledger and tip anchor must exist together")
        if log_exists:
            sequence, tip = verify_hash_chain(ledger_path)
            anchor = self._read_anchor(anchor_path)
            if anchor != {"sequence": sequence, "tip_sha256": tip,
                          "run_uuid": self.run_uuid}:
                raise RecoveryRefused("G0_LEDGER_ANCHOR_MISMATCH",
                                      "Local anchor does not match complete ledger tip")
        self._ledger = HashChainLog(ledger_path)
        if log_exists:
            anchor = self._read_anchor(anchor_path)
            if anchor != {"sequence": self._ledger.sequence,
                          "tip_sha256": self._ledger.previous,
                          "run_uuid": self.run_uuid}:
                self._ledger.close()
                self._ledger = None
                raise RecoveryRefused("G0_LEDGER_CHANGED_DURING_OPEN",
                                      "Ledger changed between verification and locked open")
        else:
            self._write_anchor(anchor_path, self._ledger.sequence, self._ledger.previous)
        self._anchor_path = anchor_path
        self._ledger_bytes = os.fstat(self._ledger.fd).st_size
        self._ledger_stat_signature = self._ledger_file_signature()
        self._indexed_sequence = self._ledger.sequence
        self._indexed_tip = self._ledger.previous

    def _ledger_file_signature(self) -> tuple[int, int, int, int, int]:
        """Return APFS file identity and change metadata for cheap drift detection."""
        assert self._ledger is not None
        info = os.fstat(self._ledger.fd)
        return (info.st_dev, info.st_ino, info.st_size,
                info.st_mtime_ns, info.st_ctime_ns)

    def _read_anchor(self, path: Path) -> dict:
        try:
            item = json.loads(path.read_text(encoding="utf-8"))
            if (set(item) != {"sequence", "tip_sha256", "run_uuid"} or
                    type(item["sequence"]) is not int or item["sequence"] < 0 or
                    not isinstance(item["tip_sha256"], str) or
                    not _HEX64.fullmatch(item["tip_sha256"]) or
                    item["run_uuid"] != self.run_uuid):
                raise ValueError("invalid anchor fields")
            return item
        except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
            raise RecoveryRefused("G0_LEDGER_ANCHOR_INVALID",
                                  f"Cannot validate local ledger anchor: {exc}") from exc

    def _write_anchor(self, path: Path, sequence: int, tip: str) -> None:
        record = {"sequence": sequence, "tip_sha256": tip, "run_uuid": self.run_uuid}
        temp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(temp, flags, 0o600)
        try:
            payload = _canonical(record) + b"\n"
            view = memoryview(payload)
            while view:
                size = os.write(fd, view)
                if size <= 0:
                    raise OSError("short anchor write")
                view = view[size:]
            os.fsync(fd)
        finally:
            os.close(fd)
        try:
            os.replace(temp, path)
            dir_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY |
                             getattr(os, "O_NOFOLLOW", 0))
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        except BaseException:
            temp.unlink(missing_ok=True)
            raise

    def _append(self, event: dict) -> str:
        with self._ledger_lock:
            self._assert_index_current()
            assert self._ledger is not None
            sequence = self._indexed_sequence
            payload = {"run_uuid": self.run_uuid, **event}
            digest = self._ledger.append(payload)
            try:
                self._write_anchor(self._anchor_path, self._ledger.sequence, self._ledger.previous)
                self._index_event(payload)
                self._indexed_sequence = self._ledger.sequence
                self._indexed_tip = self._ledger.previous
                self._ledger_bytes = os.fstat(self._ledger.fd).st_size
                self._ledger_stat_signature = self._ledger_file_signature()
            except BaseException:
                self._poisoned = True
                raise RecoveryRefused("G0_LEDGER_ANCHOR_WRITE_FAILED",
                                      f"Ledger/index commit failed after sequence {sequence}; stop and reconcile")
            return digest

    def _policy_record(self) -> dict:
        return {
            "expected_external_uuid": self.policy.expected_external_uuid,
            "expected_external_filesystem": self.policy.expected_external_filesystem,
            "expected_internal_filesystem": self.policy.expected_internal_filesystem,
            "minimum_external_start_free_bytes": self.policy.minimum_external_start_free_bytes,
            "minimum_external_reserve_free_bytes": self.policy.minimum_external_reserve_free_bytes,
            "maximum_run_bytes": self.policy.maximum_run_bytes,
            "minimum_internal_start_free_bytes": self.policy.minimum_internal_start_free_bytes,
            "minimum_internal_reserve_free_bytes": self.policy.minimum_internal_reserve_free_bytes,
            "maximum_projected_use_fraction": self.policy.maximum_projected_use_fraction,
            "run_root_relative": self.policy.run_root_relative,
            "external_start_free_bytes": self._external_start_free,
            "internal_start_free_bytes": self._internal_start_free,
        }

    def _index_event(self, event: dict) -> None:
        """Update rebuildable hot-path indexes after an authoritative append."""
        kind = event.get("event")
        if kind == "g0_activity_manifest_started":
            if self._activity_manifest is not None:
                raise RecoveryRefused("G0_ACTIVITY_MANIFEST_DUPLICATE",
                                      "A run may contain only one frozen activity manifest")
            activity_id = event.get("activity_id")
            tasks = event.get("expected_tasks")
            task_order = event.get("task_order")
            manifest_sha256 = event.get("manifest_sha256")
            try:
                canonical_activity_id = str(uuid.UUID(activity_id))
            except (ValueError, TypeError, AttributeError):
                canonical_activity_id = None
            if (not isinstance(activity_id, str) or not _SAFE_ID.fullmatch(activity_id) or
                    canonical_activity_id != activity_id.lower() or
                    not isinstance(tasks, dict) or not tasks or
                    not isinstance(task_order, list) or
                    not isinstance(manifest_sha256, str) or not _HEX64.fullmatch(manifest_sha256)):
                raise RecoveryRefused("G0_ACTIVITY_MANIFEST_INVALID",
                                      "Activity manifest identity or task map is malformed")
            if any(not isinstance(task_id, str) or not _SAFE_ID.fullmatch(task_id) or
                   not isinstance(seed, str) or not _HEX64.fullmatch(seed)
                   for task_id, seed in tasks.items()):
                raise RecoveryRefused("G0_ACTIVITY_MANIFEST_INVALID",
                                      "Activity manifest contains an invalid task or seed")
            canonical_tasks = dict(sorted(tasks.items()))
            if (any(not isinstance(task_id, str) or not _SAFE_ID.fullmatch(task_id)
                    for task_id in task_order) or len(task_order) != len(tasks) or
                    len(set(task_order)) != len(task_order) or set(task_order) != set(tasks)):
                raise RecoveryRefused("G0_ACTIVITY_MANIFEST_INVALID",
                                      "Activity task order is malformed or incomplete")
            expected_digest = hashlib.sha256(_canonical({
                "activity_id": activity_id,
                "expected_tasks": canonical_tasks,
                "task_order": task_order})).hexdigest()
            if canonical_tasks != tasks or manifest_sha256 != expected_digest:
                raise RecoveryRefused("G0_ACTIVITY_MANIFEST_HASH_MISMATCH",
                                      "Activity manifest digest or order is invalid")
            self._activity_manifest = dict(event)
            self._activity_task_seeds = canonical_tasks
            self._activity_task_order = tuple(task_order)
            self._activity_verified = False
            self._has_prior_work = True
            return
        task_kinds = {
            "g0_task_started": "starts",
            "g0_task_completed": "completions",
            "g0_task_failed": "failures",
        }
        if kind in task_kinds:
            self._has_prior_work = True
            task_id = event.get("task_id")
            if not isinstance(task_id, str) or not _SAFE_ID.fullmatch(task_id):
                raise RecoveryRefused("G0_TASK_ID_INVALID", "Task audit contains invalid identity")
            state = self._task_event_index.setdefault(
                task_id, {"starts": [], "completions": [], "failures": []})
            state[task_kinds[kind]].append(dict(event))
            if kind == "g0_task_started":
                path = event.get("result_path")
                if not isinstance(path, str):
                    raise RecoveryRefused("G0_TASK_PATH_MISMATCH", "Task start lacks a result path")
                _safe_relative(path)
                self._used_external_paths.add(path)
                self._expected_external_paths.add(path)
                self._active_task_ids.add(task_id)
            elif kind == "g0_task_completed":
                path = event.get("result_path")
                if not isinstance(path, str):
                    raise RecoveryRefused("G0_TASK_PATH_MISMATCH", "Task completion lacks a result path")
                _safe_relative(path)
                self._committed_external_files[path] = {
                    "sha256": event.get("sha256"),
                    "size_bytes": event.get("size_bytes"),
                    "event": kind,
                }
                self._active_task_ids.discard(task_id)
            elif kind == "g0_task_failed":
                self._active_task_ids.discard(task_id)
            return
        artifact_kinds = {
            "g0_external_artifact_started",
            "g0_external_artifact_written",
            "g0_external_artifact_failed",
        }
        if kind in artifact_kinds:
            self._has_prior_work = True
            path = event.get("relative_path")
            if not isinstance(path, str):
                raise RecoveryRefused("G0_ARTIFACT_HISTORY_INVALID", "Artifact audit lacks a path")
            _safe_relative(path)
            if kind == "g0_external_artifact_started":
                self._used_external_paths.add(path)
                self._expected_external_paths.add(path)
            elif kind == "g0_external_artifact_written":
                self._committed_external_files[path] = {
                    "sha256": event.get("sha256"),
                    "size_bytes": event.get("size_bytes"),
                    "event": kind,
                }
            return
        if kind in ("g0_watchdog_invocation_started",
                    "g0_watchdog_invocation_finished"):
            self._has_prior_work = True
            invocation_id = event.get("invocation_id")
            if type(invocation_id) is not int or invocation_id < 1:
                raise RecoveryRefused("G0_WATCHDOG_RECORD_INVALID",
                                      "Invalid watchdog invocation ID")
            records = self._watchdog_invocations.setdefault(
                invocation_id, {"started": None, "finished": None})
            slot = ("started" if kind == "g0_watchdog_invocation_started"
                    else "finished")
            if records[slot] is not None:
                raise RecoveryRefused("G0_WATCHDOG_RECORD_DUPLICATE",
                                      f"Duplicate watchdog {slot} record: {invocation_id}")
            if slot == "finished" and records["started"] is None:
                raise RecoveryRefused("G0_WATCHDOG_RECORD_ORDER_INVALID",
                                      f"Watchdog terminal record precedes start: {invocation_id}")
            if slot == "finished" and any(
                    records["started"].get(name) != event.get(name)
                    for name in ("task_id", "attempt_id", "activity_id")):
                raise RecoveryRefused("G0_WATCHDOG_TASK_IDENTITY_MISMATCH",
                                      f"Watchdog task identity changed: {invocation_id}")
            records[slot] = dict(event)
            self._watchdog_invocation_ids.add(invocation_id)
            return

    def _rebuild_incremental_indexes(self) -> None:
        """Rebuild hot-path state and committed-byte totals on open or resume."""
        assert self._ledger is not None and self._run_fd is not None
        events = self._task_events()
        for event in events:
            self._index_event(event)
        self._indexed_sequence = self._ledger.sequence
        self._indexed_tip = self._ledger.previous
        self._ledger_bytes = os.fstat(self._ledger.fd).st_size
        anchor = self._read_anchor(self._anchor_path)
        if anchor != {"sequence": self._indexed_sequence,
                      "tip_sha256": self._indexed_tip,
                      "run_uuid": self.run_uuid}:
            raise RecoveryRefused("G0_LEDGER_ANCHOR_MISMATCH",
                                  "Ledger changed while its incremental index was rebuilt")

        actual_files, run_bytes = self._scan_managed_tree(
            self._run_fd, self._external_initial.st_dev)
        unexpected = actual_files - self._expected_external_paths
        if unexpected:
            raise RecoveryRefused("G0_EXTERNAL_FILE_INVENTORY_MISMATCH",
                                  f"Untracked external files exist: {sorted(unexpected)[:20]}")
        for path, commitment in self._committed_external_files.items():
            if path not in actual_files:
                raise RecoveryRefused("G0_EXTERNAL_FILE_INVENTORY_MISMATCH",
                                      f"Committed file is absent: {path}")
            parent, name = self._open_parent(path, create=False)
            try:
                digest, size = _hash_open_file(parent, name,
                                               self._external_initial.st_dev)
            finally:
                os.close(parent)
            if digest != commitment.get("sha256") or size != commitment.get("size_bytes"):
                raise RecoveryRefused("G0_EXTERNAL_ARTIFACT_CORRUPT",
                                      f"Committed file changed: {path}")
        self._external_run_bytes = run_bytes
        self._recovery_verified = not self._has_prior_work

    def _assert_index_current(self) -> None:
        """Reject stale in-memory state after a partial or external ledger change."""
        if self._poisoned or self._ledger is None:
            raise RecoveryRefused("G0_LEDGER_UNAVAILABLE", "Control ledger is unavailable")
        if (os.fstat(self._ledger.fd).st_size != self._ledger_bytes or
                self._ledger_file_signature() != self._ledger_stat_signature or
                self._ledger.sequence != self._indexed_sequence or
                self._ledger.previous != self._indexed_tip):
            self._poisoned = True
            raise RecoveryRefused("G0_LEDGER_INDEX_STALE",
                                  "Ledger identity, size, change metadata or tip changed")
        anchor = self._read_anchor(self._anchor_path)
        if anchor != {"sequence": self._indexed_sequence,
                      "tip_sha256": self._indexed_tip,
                      "run_uuid": self.run_uuid}:
            self._poisoned = True
            raise RecoveryRefused("G0_LEDGER_INDEX_STALE",
                                  "Ledger tip anchor differs from the in-memory index")

    def _require_recovery_verified(self) -> None:
        if not self._recovery_verified:
            raise RecoveryRefused("G0_RECOVERY_VALIDATION_REQUIRED",
                                  "Existing run state must pass full recovery validation before writes")

    @property
    def activity_task_seeds(self) -> dict[str, str] | None:
        with self._ledger_lock:
            self._assert_index_current()
            return (dict(self._activity_task_seeds)
                    if self._activity_task_seeds is not None else None)

    @property
    def activity_id(self) -> str | None:
        with self._ledger_lock:
            self._assert_index_current()
            return (str(self._activity_manifest["activity_id"])
                    if self._activity_manifest is not None else None)

    def next_watchdog_invocation_id(self) -> int:
        """Return the next unused invocation ID from the verified in-memory index."""
        with self._ledger_lock:
            self._assert_index_current()
            return max(self._watchdog_invocation_ids, default=0) + 1

    @contextmanager
    def activity_execution(self):
        """Serialize schedulers sharing this store before they create artifacts."""
        if not self._activity_execution_lock.acquire(blocking=False):
            raise RecoveryRefused("G0_ACTIVITY_ALREADY_RUNNING",
                                  "Another scheduler is already using this activity store")
        try:
            yield
        finally:
            self._activity_execution_lock.release()

    def activity_resource_accounting(self, activity_id: str) -> dict:
        """Return cumulative supervised usage from all attempts in one activity."""
        self._require_recovery_verified()
        with self._ledger_lock:
            self._assert_index_current()
            if (self._activity_manifest is None or
                    self._activity_manifest.get("activity_id") != activity_id):
                raise RecoveryRefused("G0_ACTIVITY_IDENTITY_MISMATCH",
                                      "Resource accounting activity does not match frozen manifest")
            selected = [record for record in self._watchdog_invocations.values()
                        if isinstance(record.get("started"), dict) and
                        record["started"].get("activity_id") == activity_id]
            total_wall = 0.0
            total_cpu = 0.0
            peak_workers = 0
            unaccounted = []
            for record in selected:
                started, finished = record["started"], record["finished"]
                invocation_id = started.get("invocation_id")
                result = finished.get("result") if isinstance(finished, dict) else None
                usage = result.get("usage") if isinstance(result, dict) else None
                if not isinstance(usage, dict):
                    unaccounted.append(invocation_id)
                    continue
                wall, cpu, workers = (usage.get("wall_seconds"),
                                      usage.get("cpu_seconds"),
                                      usage.get("peak_compute_workers"))
                if (type(wall) not in (int, float) or not math.isfinite(wall) or wall < 0 or
                        type(cpu) not in (int, float) or not math.isfinite(cpu) or cpu < 0 or
                        type(workers) is not int or workers < 0):
                    unaccounted.append(invocation_id)
                    continue
                total_wall += float(wall)
                total_cpu += float(cpu)
                peak_workers = max(peak_workers, workers)
            return {"watchdog_invocation_count": len(selected),
                    "accounted_invocation_count": len(selected) - len(unaccounted),
                    "resource_accounting_complete": not unaccounted,
                    "unaccounted_invocation_ids": sorted(unaccounted),
                    "summed_watchdog_wall_seconds": total_wall,
                    "summed_watchdog_cpu_seconds": total_cpu,
                    "peak_compute_workers": peak_workers,
                    "wall_semantics": "sum_of_supervised_invocation_wall_seconds_not_calendar_elapsed"}

    def prepare_activity(self, *, activity_id: str,
                         expected_tasks: Mapping[str, str]) -> RecoveryReport:
        """Freeze one complete task/seed inventory and validate it once.

        A newly opened store with prior records performs the full recovery
        scan. While the same verified store remains open, calls for the
        identical manifest use append-validated indexes.
        """
        try:
            if str(uuid.UUID(activity_id)) != activity_id.lower():
                raise ValueError("noncanonical activity UUID")
        except (ValueError, TypeError, AttributeError) as exc:
            raise G0StorageError("G0_ACTIVITY_ID_INVALID",
                                 "activity_id must be a canonical UUID") from exc
        if not isinstance(expected_tasks, Mapping) or not expected_tasks:
            raise G0StorageError("G0_ACTIVITY_MANIFEST_INVALID",
                                 "An activity requires a nonempty task/seed inventory")
        tasks = dict(expected_tasks)
        if any(not isinstance(task_id, str) or not _SAFE_ID.fullmatch(task_id) or
               not isinstance(seed, str) or not _HEX64.fullmatch(seed)
               for task_id, seed in tasks.items()):
            raise G0StorageError("G0_ACTIVITY_MANIFEST_INVALID",
                                 "Activity inventory contains an invalid task or seed")
        task_order = list(tasks)
        canonical_tasks = dict(sorted(tasks.items()))
        manifest_sha256 = hashlib.sha256(_canonical({
            "activity_id": activity_id, "expected_tasks": canonical_tasks,
            "task_order": task_order})).hexdigest()
        with self._ledger_lock:
            self._assert_index_current()
            if self._activity_manifest is None:
                if self._has_prior_work:
                    raise RecoveryRefused("G0_ACTIVITY_MANIFEST_MISSING",
                                          "Existing run work cannot be retrofitted with a new inventory")
                self._append({"event": "g0_activity_manifest_started",
                              "activity_id": activity_id,
                              "expected_tasks": canonical_tasks,
                              "task_order": task_order,
                              "manifest_sha256": manifest_sha256,
                              "utc_epoch": time.time()})
            else:
                current = self._activity_manifest
                if (current.get("activity_id") != activity_id or
                        current.get("expected_tasks") != canonical_tasks or
                        current.get("task_order") != task_order or
                        current.get("manifest_sha256") != manifest_sha256):
                    raise RecoveryRefused("G0_ACTIVITY_MANIFEST_CHANGED",
                                          "Activity ID and full task/seed inventory are immutable")
                if self._activity_verified and self._recovery_verified:
                    return self._incremental_recovery_report(tasks)
        return self.verify_recovery(tasks)

    def assert_activity_task(self, *, task_id: str, seed_fingerprint: str) -> None:
        """O(1) admission check for one task in the verified frozen inventory."""
        self._require_recovery_verified()
        with self._ledger_lock:
            self._assert_index_current()
            if (not self._activity_verified or self._activity_task_seeds is None or
                    self._activity_task_seeds.get(task_id) != seed_fingerprint):
                raise RecoveryRefused("G0_TASK_OUTSIDE_VERIFIED_ACTIVITY",
                                      "Task/seed is not in the full verified activity manifest")

    def task_recovery_state(self, *, task_id: str,
                            seed_fingerprint: str) -> str:
        """Read one task's verified indexed state without rescanning the ledger."""
        self.assert_activity_task(task_id=task_id, seed_fingerprint=seed_fingerprint)
        state = self._task_state(task_id)
        starts = state["starts"]
        completions = state["completions"]
        failures = state["failures"]
        if len(completions) > 1 or len(starts) > 2:
            raise RecoveryRefused("G0_TASK_HISTORY_INVALID", f"Task history invalid: {task_id}")
        attempts = [item.get("attempt_id") for item in starts]
        if (any(not isinstance(value, str) for value in attempts) or
                len(set(attempts)) != len(attempts)):
            raise RecoveryRefused("G0_ATTEMPT_DUPLICATE", f"Task attempts are invalid: {task_id}")
        if any(item.get("seed_fingerprint") != seed_fingerprint for item in starts):
            raise RecoveryRefused("G0_TASK_SEED_CHANGED", f"Task seed changed: {task_id}")
        failure_by_attempt: dict[str, list[dict]] = {}
        for failure in failures:
            failure_by_attempt.setdefault(str(failure.get("attempt_id")), []).append(failure)
        if set(failure_by_attempt) - set(attempts):
            raise RecoveryRefused("G0_TASK_HISTORY_INVALID",
                                  f"Failure exists without a matching attempt: {task_id}")
        prior_attempts = set(attempts[:-1])
        for prior_attempt in prior_attempts:
            prior = failure_by_attempt.get(prior_attempt, [])
            if (len(prior) != 1 or prior[0].get("failure_class") != "OPERATIONAL" or
                    prior[0].get("reason_code") not in _OPERATIONAL_STORAGE_CODES or
                    not prior[0].get("recovery_allowed")):
                raise RecoveryRefused("G0_TASK_RETRY_FORBIDDEN",
                                      f"Prior task attempt is not a verified retryable operation: {task_id}")
        if completions:
            if (not starts or completions[0].get("attempt_id") != attempts[-1] or
                    completions[0].get("seed_fingerprint") != seed_fingerprint or
                    set(failure_by_attempt) != prior_attempts or
                    len(failures) != len(prior_attempts)):
                raise RecoveryRefused("G0_TASK_COMPLETION_CONFLICT",
                                      f"Completed task history is inconsistent: {task_id}")
            return "completed"
        if not starts:
            if failures:
                raise RecoveryRefused("G0_TASK_HISTORY_INVALID",
                                      f"Failure exists without a start: {task_id}")
            return "not_started"
        terminal = failure_by_attempt.get(attempts[-1], [])
        if len(terminal) != 1 or len(failures) != len(attempts):
            raise RecoveryRefused("G0_TASK_INTERRUPTION_UNCLASSIFIED",
                                  f"Task has incomplete or ambiguous prior state: {task_id}")
        failure = terminal[0]
        if (failure.get("failure_class") == "OPERATIONAL" and
                failure.get("reason_code") in _OPERATIONAL_STORAGE_CODES and
                failure.get("recovery_allowed")):
            return "attempts_exhausted" if len(starts) >= 2 else "retryable"
        return "blocked"

    def _incremental_recovery_report(self, expected_tasks: Mapping[str, str]) -> RecoveryReport:
        completed, retryable, not_started, exhausted = [], [], [], []
        for task_id, seed in expected_tasks.items():
            state = self.task_recovery_state(task_id=task_id, seed_fingerprint=seed)
            if state == "completed":
                completed.append(task_id)
            elif state == "retryable":
                retryable.append(task_id)
            elif state == "not_started":
                not_started.append(task_id)
            elif state == "attempts_exhausted":
                exhausted.append(task_id)
            elif state == "blocked":
                raise RecoveryRefused("G0_TASK_RETRY_FORBIDDEN",
                                      f"Task failure is not eligible for automatic recovery: {task_id}")
        return RecoveryReport(tuple(sorted(completed)), tuple(sorted(retryable)),
                              tuple(sorted(not_started)), tuple(sorted(exhausted)))

    def _reserve_external_write(self, size: int) -> None:
        """Reserve a bounded write against run and independent volume limits."""
        if type(size) is not int or size <= 0 or size > _STREAM_WRITE_CHUNK_BYTES:
            raise ValueError("External writes must use positive bounded chunks")
        try:
            if self._require_os_mount and not os.path.ismount(self.policy.external_mount):
                raise G0StorageError("G0_EXTERNAL_MOUNT_UNAVAILABLE",
                                     "External data path is no longer a mountpoint")
            current = Path(self.policy.external_mount).stat()
            if (current.st_dev != self._external_initial.st_dev or
                    current.st_ino != self._external_initial.st_ino or
                    self._mount_fd is None or
                    os.fstat(self._mount_fd).st_dev != self._external_initial.st_dev):
                raise G0StorageError("G0_EXTERNAL_VOLUME_IDENTITY_MISMATCH",
                                     "External mount root changed before a bounded write")
            with self._ledger_lock:
                self._assert_index_current()
                ext_free = self.usage_provider(self.policy.external_mount).free
                internal_free = self.usage_provider(self.policy.internal_mount).free
                reserved = self._external_reserved_bytes
                next_run_bytes = self._external_run_bytes + reserved + size
                if (next_run_bytes > self.policy.maximum_run_bytes or
                        ext_free - reserved - size < self.policy.minimum_external_reserve_free_bytes or
                        max(0, self._external_start_free - ext_free) + reserved + size >
                        int(self._external_start_free * self.policy.maximum_projected_use_fraction)):
                    raise G0StorageError("G0_EXTERNAL_SPACE_LIMIT",
                                         "Bounded external write would breach run or volume limits")
                if (internal_free < self.policy.minimum_internal_reserve_free_bytes or
                        max(0, self._internal_start_free - internal_free) >
                        int(self._internal_start_free * self.policy.maximum_projected_use_fraction)):
                    raise G0StorageError("G0_INTERNAL_SPACE_LIMIT",
                                         "Internal APFS reserve would be breached during external write")
                self._external_reserved_bytes += size
        except G0StorageError:
            raise
        except OSError as exc:
            raise G0StorageError("G0_EXTERNAL_IO_FAILURE",
                                 f"Cannot reserve external write capacity: {exc}") from exc

    def _finish_external_write(self, reserved: int, written: int) -> None:
        with self._ledger_lock:
            self._external_reserved_bytes -= reserved
            if self._external_reserved_bytes < 0:
                self._poisoned = True
                raise RecoveryRefused("G0_EXTERNAL_COUNTER_INVALID",
                                      "External write reservation underflow")
            self._external_run_bytes += written

    def _write_bounded_payload(self, fd: int, payload: bytes | memoryview,
                               digest: object) -> int:
        view = memoryview(payload)
        total = 0
        while view:
            chunk = view[:_STREAM_WRITE_CHUNK_BYTES]
            reserved = len(chunk)
            self._reserve_external_write(reserved)
            try:
                written = os.write(fd, chunk)
            except BaseException:
                self._finish_external_write(reserved, 0)
                raise
            self._finish_external_write(reserved, written)
            if written <= 0:
                raise OSError("short external artifact write")
            digest.update(chunk[:written])
            total += written
            view = view[written:]
        return total

    def _validate_current_mounts(self) -> None:
        if self._require_os_mount and not os.path.ismount(self.policy.external_mount):
            raise G0StorageError("G0_EXTERNAL_MOUNT_UNAVAILABLE",
                                 "External data path is no longer an active mountpoint")
        ext = self._inspect(self.policy.external_mount)
        internal = self._inspect(self.policy.internal_mount)
        if (ext.mount_point != str(self.policy.external_mount) or
                ext.volume_uuid.upper() != self._external_initial.volume_uuid.upper() or
                ext.filesystem.lower() != self._external_initial.filesystem.lower() or
                ext.st_dev != self._external_initial.st_dev):
            raise G0StorageError("G0_EXTERNAL_VOLUME_IDENTITY_MISMATCH",
                                 "External mount identity changed during the run")
        if (internal.volume_uuid.upper() != self._internal_initial.volume_uuid.upper() or
                internal.filesystem.lower() != self._internal_initial.filesystem.lower() or
                internal.st_dev != self._internal_initial.st_dev):
            raise G0StorageError("G0_INTERNAL_VOLUME_IDENTITY_MISMATCH",
                                 "Internal control volume identity changed during the run")
        if self._mount_fd is None or os.fstat(self._mount_fd).st_dev != ext.st_dev:
            raise G0StorageError("G0_EXTERNAL_VOLUME_IDENTITY_MISMATCH",
                                 "Anchored external directory descriptor is invalid")
        now = Path(self.policy.external_mount).stat()
        if now.st_dev != ext.st_dev or now.st_ino != ext.st_ino:
            raise G0StorageError("G0_EXTERNAL_VOLUME_IDENTITY_MISMATCH",
                                 "External mount root was replaced")

    def check_health(self) -> dict:
        """Recheck volume identity and O(1) counters without walking prior outputs."""
        try:
            self._validate_current_mounts()
            ext_free = self.usage_provider(self.policy.external_mount).free
            internal_free = self.usage_provider(self.policy.internal_mount).free
            with self._ledger_lock:
                self._assert_index_current()
                run_bytes = self._external_run_bytes + self._external_reserved_bytes
                ledger_bytes = os.fstat(self._ledger.fd).st_size
            ext_use = max(0, self._external_start_free - ext_free)
            internal_use = max(0, self._internal_start_free - internal_free)
            if (ext_free < self.policy.minimum_external_reserve_free_bytes or
                    run_bytes > self.policy.maximum_run_bytes or
                    ext_use > int(self._external_start_free *
                                  self.policy.maximum_projected_use_fraction)):
                raise G0StorageError("G0_EXTERNAL_SPACE_LIMIT",
                                     "External reserve, run allocation, or projected-use limit breached")
            if (internal_free < self.policy.minimum_internal_reserve_free_bytes or
                    internal_use > int(self._internal_start_free *
                                       self.policy.maximum_projected_use_fraction)):
                raise G0StorageError("G0_INTERNAL_SPACE_LIMIT",
                                     "Internal APFS reserve or projected-use limit breached")
            return {"external_volume_uuid": self._external_initial.volume_uuid,
                    "external_filesystem": self._external_initial.filesystem,
                    "external_free_bytes": ext_free,
                    "external_run_bytes": run_bytes,
                    "external_projected_use_bytes": ext_use,
                    "internal_volume_uuid": self._internal_initial.volume_uuid,
                    "internal_filesystem": self._internal_initial.filesystem,
                    "internal_free_bytes": internal_free,
                    "internal_ledger_bytes": ledger_bytes,
                    "internal_projected_use_bytes": internal_use}
        except G0StorageError:
            raise
        except (OSError, ValueError, AssertionError, WatchdogError) as exc:
            raise G0StorageError("G0_EXTERNAL_IO_FAILURE",
                                 f"Storage health check failed: {exc}") from exc

    def watchdog_stop_guard(self) -> str | None:
        """Return a stable fail-closed stop code for nc0a_watchdog.supervise."""
        try:
            self.check_health()
            return None
        except G0StorageError as exc:
            return exc.code if re.fullmatch(r"[A-Z][A-Z0-9_]{2,119}", exc.code) else "G0_STORAGE_GUARD_FAILED"

    def supervise_worker(self, command: list[str], *, limits: WatchdogLimits,
                         invocation_id: int,
                         task_id: str | None = None,
                         attempt_id: str | None = None,
                         activity_id: str | None = None,
                         inherited_fds: tuple[int, ...] = (),
                         additional_stop_guard: Callable[[], str | None] | None = None,
                         **watchdog_options) -> dict:
        """Run one bounded worker under the internal-disk watchdog and guard.

        A G0 executor calls this boundary instead of invoking the watchdog
        directly. Watchdog control audit and small protocol stdout stay on
        APFS; proposal traces must be passed separately through a bounded pipe
        to write_immutable_artifact. This adapter does not schedule tasks.
        """
        if type(invocation_id) is not int or invocation_id < 1:
            raise ValueError("invocation_id must be a positive integer")
        task_identity = (task_id, attempt_id, activity_id)
        if any(value is not None for value in task_identity):
            try:
                valid_attempt = (isinstance(attempt_id, str) and
                                 str(uuid.UUID(attempt_id)) == attempt_id.lower())
                valid_activity = (isinstance(activity_id, str) and
                                  str(uuid.UUID(activity_id)) == activity_id.lower())
            except (ValueError, TypeError, AttributeError):
                valid_attempt = valid_activity = False
            if (not isinstance(task_id, str) or not _SAFE_ID.fullmatch(task_id) or
                    not valid_attempt or not valid_activity):
                raise G0StorageError("G0_WATCHDOG_TASK_IDENTITY_INVALID",
                                     "Watchdog task, attempt and activity identities must be supplied together")
            task_state = self._task_state(task_id)
            if not any(event.get("attempt_id") == attempt_id and
                       event.get("invocation_id") == invocation_id
                       for event in task_state["starts"]):
                raise RecoveryRefused("G0_WATCHDOG_TASK_START_MISMATCH",
                                      "Watchdog invocation has no matching task-start record")
        self._require_recovery_verified()
        controlled_options = {"run_dir", "stop_guard", "audit_name", "stdout_name",
                             "invocation_id"}
        if controlled_options.intersection(watchdog_options):
            raise ValueError("Watchdog run directory, audit names, ID and guard are fixed by the adapter")
        self.check_health()
        info = self.control_dir.lstat()
        if stat.S_ISLNK(info.st_mode) or not stat.S_ISDIR(info.st_mode):
            raise G0StorageError("G0_INTERNAL_LEDGER_PATH_INVALID",
                                 "Watchdog control directory is not a real directory")
        if info.st_dev != self._internal_root_dev:
            raise G0StorageError("G0_INTERNAL_VOLUME_IDENTITY_MISMATCH",
                                 "Watchdog control directory left the internal volume")
        audit_name = f"watchdog.g0.{invocation_id}.jsonl"
        stdout_name = f"runner.g0.{invocation_id}.stdout.log"
        with self._ledger_lock:
            self._assert_index_current()
            if invocation_id in self._watchdog_invocation_ids:
                raise RecoveryRefused("G0_WATCHDOG_INVOCATION_REUSED",
                                      "Watchdog invocation IDs are single-use")
            self._append({"event": "g0_watchdog_invocation_started",
                          "invocation_id": invocation_id,
                          "task_id": task_id, "attempt_id": attempt_id,
                          "activity_id": activity_id,
                          "audit_name": audit_name, "stdout_name": stdout_name,
                          "utc_epoch": time.time()})
        if additional_stop_guard is not None and not callable(additional_stop_guard):
            raise TypeError("additional_stop_guard must be callable")

        def combined_stop_guard() -> str | None:
            storage_reason = self.watchdog_stop_guard()
            if storage_reason is not None:
                return storage_reason
            return additional_stop_guard() if additional_stop_guard is not None else None

        try:
            result = supervise(command, run_dir=self.control_dir, limits=limits,
                               invocation_id=invocation_id,
                               audit_name=audit_name, stdout_name=stdout_name,
                               stop_guard=combined_stop_guard,
                               inherited_fds=inherited_fds,
                               **watchdog_options)
        except BaseException as exc:
            self._record_watchdog_terminal(invocation_id, audit_name, stdout_name,
                                           status="watchdog_exception",
                                           task_id=task_id, attempt_id=attempt_id,
                                           activity_id=activity_id,
                                           exception_type=type(exc).__name__,
                                           exception_message=str(exc)[:500])
            raise
        terminal = self._record_watchdog_terminal(
            invocation_id, audit_name, stdout_name,
            status=str(result.get("status", "unknown")), result=result,
            task_id=task_id, attempt_id=attempt_id, activity_id=activity_id)
        if result.get("audit_sha256") and result["audit_sha256"] != terminal.get("audit_tip_sha256"):
            raise RecoveryRefused("G0_WATCHDOG_AUDIT_TIP_MISMATCH",
                                  "Watchdog result tip differs from the persisted log")
        return {**result, "control_ledger_tip_sha256": self._ledger.previous}

    def _record_watchdog_terminal(self, invocation_id: int, audit_name: str,
                                  stdout_name: str, *, status: str,
                                  task_id: str | None = None,
                                  attempt_id: str | None = None,
                                  activity_id: str | None = None,
                                  result: dict | None = None,
                                  exception_type: str | None = None,
                                  exception_message: str | None = None) -> dict:
        audit_path = self.control_dir / audit_name
        stdout_path = self.control_dir / stdout_name
        audit_sequence = None
        audit_tip = None
        audit_file_sha = None
        stdout_sha = None
        audit_error = None
        try:
            audit_sequence, audit_tip = verify_hash_chain(audit_path)
            audit_file_sha = _sha256_path(audit_path)
        except BaseException as exc:
            audit_error = f"{type(exc).__name__}: {exc}"[:500]
        try:
            stdout_sha = _sha256_path(stdout_path)
        except BaseException as exc:
            audit_error = (audit_error + "; " if audit_error else "") + f"stdout {type(exc).__name__}: {exc}"[:500]
        terminal = {"event": "g0_watchdog_invocation_finished",
                    "invocation_id": invocation_id, "status": status,
                    "task_id": task_id, "attempt_id": attempt_id,
                    "activity_id": activity_id,
                    "audit_name": audit_name, "stdout_name": stdout_name,
                    "audit_sequence": audit_sequence, "audit_tip_sha256": audit_tip,
                    "audit_file_sha256": audit_file_sha, "stdout_sha256": stdout_sha,
                    "result": result, "exception_type": exception_type,
                    "exception_message": exception_message,
                    "artifact_error": audit_error, "utc_epoch": time.time()}
        self._append(terminal)
        return terminal

    def _task_events(self) -> list[dict]:
        """Read and verify the complete authoritative ledger for open/recovery only."""
        with self._ledger_lock:
            assert self._ledger is not None
            events = []
            previous = "0" * 64
            sequence = 0
            read_fd = os.open(self._ledger.path, os.O_RDONLY |
                              getattr(os, "O_NOFOLLOW", 0))
            handle = None
            try:
                read_info = os.fstat(read_fd)
                write_info = os.fstat(self._ledger.fd)
                if (read_info.st_dev, read_info.st_ino) != (write_info.st_dev,
                                                            write_info.st_ino):
                    raise RecoveryRefused("G0_LEDGER_IDENTITY_CHANGED",
                                          "Ledger path no longer names the locked file")
                read_signature = (read_info.st_dev, read_info.st_ino, read_info.st_size,
                                  read_info.st_mtime_ns, read_info.st_ctime_ns)
                if read_signature != self._ledger_stat_signature:
                    raise RecoveryRefused("G0_LEDGER_CHANGED_DURING_SCAN",
                                          "Ledger metadata differs from the indexed version")
                handle = os.fdopen(read_fd, "rb", closefd=False)
                while True:
                    offset = handle.tell()
                    line = handle.readline()
                    if not line:
                        break
                    if not line.endswith(b"\n"):
                        raise RecoveryRefused("G0_LEDGER_PARTIAL_TAIL",
                                              "Control audit has an incomplete tail")
                    try:
                        item = json.loads(line)
                        digest = item.pop("record_sha256")
                        if (set(item) != {"sequence", "previous_sha256", "event"} or
                                item.get("sequence") != sequence or
                                item.get("previous_sha256") != previous or
                                not isinstance(digest, str) or not _HEX64.fullmatch(digest) or
                                hashlib.sha256(_canonical(item)).hexdigest() != digest):
                            raise ValueError("hash-chain fields or digest mismatch")
                        event = item["event"]
                        if not isinstance(event, dict):
                            raise ValueError("event must be an object")
                    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
                        raise RecoveryRefused("G0_LEDGER_INVALID",
                                              f"Control audit is invalid at byte {offset}: {exc}") from exc
                    if event.get("run_uuid") != self.run_uuid:
                        raise RecoveryRefused("G0_LEDGER_RUN_ID_MISMATCH",
                                              "Ledger contains another run UUID")
                    events.append(event)
                    previous = digest
                    sequence += 1
            finally:
                if handle is not None:
                    handle.close()
                os.close(read_fd)
            if (sequence != self._ledger.sequence or previous != self._ledger.previous or
                    self._ledger_file_signature() != read_signature or
                    read_signature != self._ledger_stat_signature):
                raise RecoveryRefused("G0_LEDGER_CHANGED_DURING_SCAN",
                                      "Ledger differs from the locked in-memory tip")
            anchor = self._read_anchor(self._anchor_path)
            if anchor != {"sequence": sequence, "tip_sha256": previous,
                          "run_uuid": self.run_uuid}:
                raise RecoveryRefused("G0_LEDGER_ANCHOR_MISMATCH",
                                      "Audit records do not match the local tip anchor")
            return events

    def _task_state(self, task_id: str) -> dict[str, list[dict]]:
        """Return one task's indexed event state without rescanning old records."""
        with self._ledger_lock:
            self._assert_index_current()
            if not isinstance(task_id, str) or not _SAFE_ID.fullmatch(task_id):
                raise RecoveryRefused("G0_TASK_ID_INVALID", "Task ID is malformed")
            state = self._task_event_index.get(
                task_id, {"starts": [], "completions": [], "failures": []})
            return {kind: [dict(event) for event in events]
                    for kind, events in state.items()}

    def _expected_result_path(self, task_id: str, attempt_id: str) -> str:
        if not _SAFE_ID.fullmatch(task_id):
            raise G0StorageError("G0_TASK_ID_INVALID", "Task ID contains unsafe characters")
        try:
            if str(uuid.UUID(attempt_id)) != attempt_id.lower():
                raise ValueError("noncanonical UUID")
        except (ValueError, TypeError, AttributeError) as exc:
            raise G0StorageError("G0_ATTEMPT_ID_INVALID", "attempt_id must be a UUID") from exc
        return f"tasks/{task_id}/attempts/{attempt_id}/result.bin"

    def _open_parent(self, relative_path: str, *, create: bool) -> tuple[int, str]:
        parts = _safe_relative(relative_path)
        if self._run_fd is None:
            raise G0StorageError("G0_EXTERNAL_STORE_CLOSED", "External store is closed")
        parent = _open_or_create_beneath(self._run_fd, parts[:-1],
                                         self._external_initial.st_dev, create=create)
        return parent, parts[-1]

    def begin_task(self, *, task_id: str, attempt_id: str,
                   seed_fingerprint: str, invocation_id: int | None = None) -> str:
        """Record a task attempt before work begins and return its fixed path."""
        self._require_recovery_verified()
        if not _HEX64.fullmatch(seed_fingerprint):
            raise G0StorageError("G0_SEED_FINGERPRINT_INVALID", "Seed fingerprint must be SHA-256 hex")
        relative = self._expected_result_path(task_id, attempt_id)
        self.check_health()
        assert self._run_fd is not None
        _validate_existing_parent_beneath(
            self._run_fd, _safe_relative(relative)[:-1],
            self._external_initial.st_dev)
        with self._ledger_lock:
            self._assert_index_current()
            if (self._activity_task_seeds is not None and
                    self._activity_task_seeds.get(task_id) != seed_fingerprint):
                raise RecoveryRefused("G0_TASK_OUTSIDE_ACTIVITY_MANIFEST",
                                      "Task/seed is not in the frozen activity inventory")
            if self._activity_task_seeds is not None and (
                    type(invocation_id) is not int or invocation_id < 1):
                raise RecoveryRefused("G0_TASK_WATCHDOG_MAPPING_INVALID",
                                      "Every activity task must bind a positive Watchdog invocation ID")
            if self._activity_task_seeds is not None and self._active_task_ids:
                raise RecoveryRefused("G0_ACTIVITY_TASK_ALREADY_ACTIVE",
                                      "The activity scheduler permits only one active task at a time")
            prior = self._task_state(task_id)
            if prior["completions"]:
                raise RecoveryRefused("G0_TASK_ALREADY_COMPLETE", "Completed task cannot be recomputed")
            if len(prior["starts"]) >= 2:
                raise RecoveryRefused("G0_TASK_ATTEMPT_LIMIT", "Task attempt limit of two is exhausted")
            if prior["starts"]:
                last = prior["starts"][-1]
                failures = [x for x in prior["failures"] if x.get("attempt_id") == last.get("attempt_id")]
                if len(failures) != 1 or not failures[0].get("recovery_allowed"):
                    raise RecoveryRefused("G0_TASK_RECOVERY_NOT_AUTHORIZED",
                                          "Prior attempt lacks one explicit retryable operational failure")
                if last.get("seed_fingerprint") != seed_fingerprint:
                    raise RecoveryRefused("G0_TASK_SEED_CHANGED", "Recovery must retain the original seed fingerprint")
            elif prior["failures"]:
                raise RecoveryRefused("G0_TASK_HISTORY_INVALID", "Failure record has no preceding task attempt")
            if attempt_id in {x.get("attempt_id") for x in prior["starts"]}:
                raise RecoveryRefused("G0_ATTEMPT_DUPLICATE", "Attempt ID has already been used")
            self._append({"event": "g0_task_started", "task_id": task_id,
                          "attempt_id": attempt_id, "seed_fingerprint": seed_fingerprint,
                          "invocation_id": invocation_id,
                          "result_path": relative, "utc_epoch": time.time()})
        return relative

    def write_task_result(self, *, task_id: str, attempt_id: str,
                          seed_fingerprint: str, payload: bytes) -> dict:
        """Convenience method that begins and then commits one immutable result."""
        self.begin_task(task_id=task_id, attempt_id=attempt_id,
                        seed_fingerprint=seed_fingerprint)
        return self.complete_task_result(task_id=task_id, attempt_id=attempt_id,
                                         seed_fingerprint=seed_fingerprint, payload=payload)

    def read_completed_task_result(self, *, task_id: str,
                                   seed_fingerprint: str) -> bytes:
        """Read a previously verified immutable task result without recompute.

        Callers must first run ``verify_recovery`` for the frozen inventory.
        This method checks the indexed completion identity again and verifies
        the bytes against the authoritative completion record before return.
        """
        self._require_recovery_verified()
        if not _HEX64.fullmatch(seed_fingerprint):
            raise G0StorageError("G0_SEED_FINGERPRINT_INVALID",
                                 "Seed fingerprint must be SHA-256 hex")
        with self._ledger_lock:
            state = self._task_state(task_id)
            if len(state["completions"]) != 1 or not state["starts"]:
                raise RecoveryRefused("G0_TASK_RESULT_NOT_COMPLETE",
                                      "Task has no uniquely completed result")
            completion = state["completions"][0]
            start = state["starts"][-1]
            relative = self._expected_result_path(task_id, start["attempt_id"])
            if (start.get("seed_fingerprint") != seed_fingerprint or
                    completion.get("seed_fingerprint") != seed_fingerprint or
                    completion.get("attempt_id") != start.get("attempt_id") or
                    completion.get("result_path") != relative):
                raise RecoveryRefused("G0_TASK_RESULT_IDENTITY_MISMATCH",
                                      "Completed task result does not match task/seed identity")
            expected_digest = completion.get("sha256")
            expected_size = completion.get("size_bytes")
            if (not isinstance(expected_digest, str) or
                    not _HEX64.fullmatch(expected_digest) or
                    type(expected_size) is not int or expected_size < 0):
                raise RecoveryRefused("G0_TASK_RESULT_RECORD_INVALID",
                                      "Completion record has invalid result hash or size")
        self.check_health()
        parent_fd, name = self._open_parent(relative, create=False)
        fd = -1
        try:
            flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
            fd = os.open(name, flags, dir_fd=parent_fd)
            info = os.fstat(fd)
            if (not stat.S_ISREG(info.st_mode) or
                    info.st_dev != self._external_initial.st_dev or
                    info.st_size != expected_size):
                raise RecoveryRefused("G0_TASK_ARTIFACT_IDENTITY_MISMATCH",
                                      "Completed result is not the recorded regular file")
            digest = hashlib.sha256()
            chunks = []
            remaining = expected_size
            while remaining:
                block = os.read(fd, min(1 << 20, remaining))
                if not block:
                    raise RecoveryRefused("G0_TASK_ARTIFACT_TRUNCATED",
                                          "Completed result ended before recorded size")
                digest.update(block)
                chunks.append(block)
                remaining -= len(block)
            if os.read(fd, 1):
                raise RecoveryRefused("G0_TASK_ARTIFACT_SIZE_CHANGED",
                                      "Completed result exceeds recorded size")
            if digest.hexdigest() != expected_digest:
                raise RecoveryRefused("G0_TASK_ARTIFACT_CORRUPT",
                                      "Completed result hash differs from its ledger record")
            return b"".join(chunks)
        except OSError as exc:
            raise RecoveryRefused("G0_TASK_ARTIFACT_UNAVAILABLE",
                                  f"Cannot safely read completed result: {exc}") from exc
        finally:
            if fd >= 0:
                os.close(fd)
            os.close(parent_fd)

    def write_immutable_artifact(self, *, relative_path: str,
                                 artifact_kind: str, identity: Mapping[str, object],
                                 chunks: bytes | Iterable[bytes],
                                 stream_metadata: dict | None = None) -> dict:
        """Stream an immutable cache/checkpoint/audit/source-graph/diagnostic artifact.

        The namespace is constrained by kind, the content is hashed while
        writing and read back before the internal ledger marks it committed.
        This keeps large audit payloads out of memory when callers provide an
        iterator of bounded chunks.
        """
        parts = _safe_relative(relative_path)
        expected_namespace = {
            "cache": "cache", "checkpoint": "checkpoints",
            "audit": "audit", "source_graph": "source-graphs",
            "diagnostic_log": "diagnostic-logs",
        }.get(artifact_kind)
        if expected_namespace is None or parts[0] != expected_namespace:
            raise G0StorageError("G0_ARTIFACT_NAMESPACE_INVALID",
                                 "Artifact kind must use its fixed external namespace")
        if not isinstance(identity, Mapping):
            raise G0StorageError("G0_ARTIFACT_IDENTITY_INVALID", "Artifact identity must be a mapping")
        identity_record = dict(identity)
        if stream_metadata is not None and not isinstance(stream_metadata, dict):
            raise G0StorageError("G0_ARTIFACT_STREAM_METADATA_INVALID",
                                 "stream_metadata must be a dict populated by the stream producer")
        try:
            _canonical(identity_record)
        except (TypeError, ValueError) as exc:
            raise G0StorageError("G0_ARTIFACT_IDENTITY_INVALID",
                                 "Artifact identity must be canonical JSON data") from exc
        self._require_recovery_verified()
        iterator = iter((chunks,)) if isinstance(chunks, bytes) else iter(chunks)
        self.check_health()
        parent_fd = -1
        fd = -1
        digest = hashlib.sha256()
        size = 0
        with self._ledger_lock:
            self._assert_index_current()
            if (relative_path in self._used_external_paths or
                    relative_path in self._inflight_artifact_paths):
                raise RecoveryRefused("G0_ARTIFACT_PATH_REUSED",
                                      "External artifact paths are immutable and single-use")
            self._inflight_artifact_paths.add(relative_path)
            self._append({"event": "g0_external_artifact_started",
                          "relative_path": relative_path,
                          "artifact_kind": artifact_kind,
                          "identity": identity_record,
                          "utc_epoch": time.time()})
        try:
            self.check_health()
            parent_fd, name = self._open_parent(relative_path, create=True)
            fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL |
                         getattr(os, "O_NOFOLLOW", 0), 0o600, dir_fd=parent_fd)
            for block in iterator:
                if not isinstance(block, bytes):
                    raise TypeError("artifact chunks must be bytes")
                size += self._write_bounded_payload(fd, block, digest)
            os.fsync(fd)
            os.close(fd)
            fd = -1
            os.fsync(parent_fd)
            self._validate_current_mounts()
            actual_digest, actual_size = _hash_open_file(parent_fd, name,
                                                          self._external_initial.st_dev)
            if actual_digest != digest.hexdigest() or actual_size != size:
                raise G0StorageError("G0_EXTERNAL_IO_FAILURE",
                                     "Artifact readback hash or size mismatch")
            if stream_metadata is not None:
                try:
                    _canonical(stream_metadata)
                except (TypeError, ValueError) as exc:
                    raise G0StorageError("G0_ARTIFACT_STREAM_METADATA_INVALID",
                                         "Stream metadata is not canonical JSON") from exc
            health = self.check_health()
            self._append({"event": "g0_external_artifact_written",
                          "relative_path": relative_path,
                          "artifact_kind": artifact_kind,
                          "identity": identity_record,
                          "stream_metadata": stream_metadata,
                          "size_bytes": size, "sha256": actual_digest,
                          "external_volume_uuid": self._external_initial.volume_uuid,
                          "utc_epoch": time.time()})
            return {"relative_path": relative_path, "artifact_kind": artifact_kind,
                    "size_bytes": size, "sha256": actual_digest,
                    "stream_metadata": stream_metadata, "health": health}
        except BaseException as exc:
            code = exc.code if isinstance(exc, G0StorageError) else "G0_EXTERNAL_IO_FAILURE" if isinstance(exc, OSError) else "G0_UNKNOWN_STORAGE_FAILURE"
            try:
                self._append({"event": "g0_external_artifact_failed",
                              "relative_path": relative_path,
                              "artifact_kind": artifact_kind,
                              "reason_code": code, "reason": str(exc)[:500],
                              "automatic_recovery_allowed": False,
                              "utc_epoch": time.time()})
            except BaseException as ledger_exc:
                self._poisoned = True
                raise RecoveryRefused("G0_FAILURE_LEDGER_UNAVAILABLE",
                                      f"Artifact write failed and APFS ledger also failed: {ledger_exc}") from exc
            raise
        finally:
            if fd >= 0:
                os.close(fd)
            if parent_fd >= 0:
                os.close(parent_fd)
            with self._ledger_lock:
                self._inflight_artifact_paths.discard(relative_path)

    def complete_task_result(self, *, task_id: str, attempt_id: str,
                             seed_fingerprint: str, payload: bytes) -> dict:
        """Persist one immutable result for a previously started task attempt."""
        if not isinstance(payload, bytes):
            raise TypeError("payload must be bytes")
        self._require_recovery_verified()
        if not _HEX64.fullmatch(seed_fingerprint):
            raise G0StorageError("G0_SEED_FINGERPRINT_INVALID", "Seed fingerprint must be SHA-256 hex")
        relative = self._expected_result_path(task_id, attempt_id)
        with self._ledger_lock:
            state = self._task_state(task_id)
            if (state is None or not any(x.get("attempt_id") == attempt_id and
                                         x.get("seed_fingerprint") == seed_fingerprint and
                                         x.get("result_path") == relative
                                         for x in state["starts"])):
                raise RecoveryRefused("G0_TASK_START_MISSING", "Result has no matching task-start record")
            if any(x.get("attempt_id") == attempt_id for x in state["completions"] + state["failures"]):
                raise RecoveryRefused("G0_ATTEMPT_ALREADY_TERMINAL", "Attempt already has a terminal record")
            if relative in self._inflight_result_paths:
                raise RecoveryRefused("G0_ATTEMPT_ALREADY_WRITING", "Result path is already being written")
            self._inflight_result_paths.add(relative)
        parent_fd = -1
        fd = -1
        try:
            self.check_health()
            parent_fd, name = self._open_parent(relative, create=True)
            flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
            fd = os.open(name, flags, 0o600, dir_fd=parent_fd)
            write_digest = hashlib.sha256()
            written_size = self._write_bounded_payload(
                fd, payload, write_digest)
            digest = write_digest.hexdigest()
            if written_size != len(payload):
                raise OSError("short task result write")
            os.fsync(fd)
            os.close(fd)
            fd = -1
            os.fsync(parent_fd)
            self._validate_current_mounts()
            actual_digest, actual_size = _hash_open_file(parent_fd, name,
                                                          self._external_initial.st_dev)
            if actual_digest != digest or actual_size != len(payload):
                raise G0StorageError("G0_EXTERNAL_IO_FAILURE", "Readback hash or size mismatch")
            health = self.check_health()
            self._append({"event": "g0_task_completed", "task_id": task_id,
                          "attempt_id": attempt_id, "seed_fingerprint": seed_fingerprint,
                          "result_path": relative, "size_bytes": actual_size,
                          "sha256": actual_digest, "external_volume_uuid":
                          self._external_initial.volume_uuid,
                          "internal_volume_uuid": self._internal_initial.volume_uuid,
                          "utc_epoch": time.time()})
            return {"task_id": task_id, "attempt_id": attempt_id,
                    "result_path": relative, "size_bytes": actual_size,
                    "sha256": actual_digest, "health": health}
        except BaseException as exc:
            code = exc.code if isinstance(exc, G0StorageError) else "G0_EXTERNAL_IO_FAILURE" if isinstance(exc, OSError) else "G0_UNKNOWN_STORAGE_FAILURE"
            recovery_allowed = code in _OPERATIONAL_STORAGE_CODES
            try:
                self._append({"event": "g0_task_failed", "task_id": task_id,
                              "attempt_id": attempt_id,
                              "failure_class": "OPERATIONAL" if recovery_allowed else "UNKNOWN",
                              "reason_code": code, "reason": str(exc)[:500],
                              "recovery_allowed": recovery_allowed,
                              "utc_epoch": time.time()})
            except BaseException as ledger_exc:
                self._poisoned = True
                raise RecoveryRefused("G0_FAILURE_LEDGER_UNAVAILABLE",
                                      f"Storage failed and internal failure record also failed: {ledger_exc}") from exc
            raise
        finally:
            if fd >= 0:
                os.close(fd)
            if parent_fd >= 0:
                os.close(parent_fd)
            with self._ledger_lock:
                self._inflight_result_paths.discard(relative)

    def record_task_failure(self, *, task_id: str, attempt_id: str,
                            failure_class: str, reason_code: str,
                            reason: str) -> None:
        """Persist executor classification; only known operational codes permit retry."""
        self._require_recovery_verified()
        with self._ledger_lock:
            state = self._task_state(task_id)
            if not state or not any(x.get("attempt_id") == attempt_id for x in state["starts"]):
                raise RecoveryRefused("G0_FAILURE_WITHOUT_START", "Failure has no matching started attempt")
            if any(x.get("attempt_id") == attempt_id for x in state["completions"] + state["failures"]):
                raise RecoveryRefused("G0_ATTEMPT_ALREADY_TERMINAL", "Attempt already has a terminal record")
            if failure_class not in ("SCIENTIFIC", "OPERATIONAL", "UNKNOWN"):
                raise G0StorageError("G0_FAILURE_CLASS_INVALID", "Unknown failure class")
            recovery_allowed = failure_class == "OPERATIONAL" and reason_code in _OPERATIONAL_STORAGE_CODES
            if failure_class in ("SCIENTIFIC", "UNKNOWN"):
                recovery_allowed = False
            self._append({"event": "g0_task_failed", "task_id": task_id,
                          "attempt_id": attempt_id, "failure_class": failure_class,
                          "reason_code": reason_code, "reason": str(reason)[:500],
                          "recovery_allowed": recovery_allowed, "utc_epoch": time.time()})

    def verify_recovery(self, expected_tasks: Mapping[str, str]) -> RecoveryReport:
        """Verify UUID-bound ledger continuity, completed hashes and retry states."""
        self.check_health()
        with self._ledger_lock:
            if self._inflight_result_paths or self._inflight_artifact_paths:
                raise RecoveryRefused("G0_RECOVERY_DURING_WRITE",
                                      "Recovery verification requires all storage writes to stop")
        if self._ledger is None or self._ledger_fd is None:
            raise RecoveryRefused("G0_LEDGER_UNAVAILABLE", "Cannot inspect recovery ledger")
        ledger_events = self._task_events()
        manifest_events = [event for event in ledger_events
                           if event.get("event") == "g0_activity_manifest_started"]
        if len(manifest_events) > 1:
            raise RecoveryRefused("G0_ACTIVITY_MANIFEST_DUPLICATE",
                                  "Run contains multiple activity manifests")
        if manifest_events:
            manifest = manifest_events[0]
            manifest_tasks = manifest.get("expected_tasks")
            manifest_hash = hashlib.sha256(_canonical({
                "activity_id": manifest.get("activity_id"),
                "expected_tasks": manifest_tasks,
                "task_order": manifest.get("task_order")})).hexdigest()
            if (not isinstance(manifest_tasks, dict) or
                    manifest_tasks != dict(sorted(expected_tasks.items())) or
                    manifest.get("task_order") != list(expected_tasks) or
                    manifest.get("manifest_sha256") != manifest_hash):
                raise RecoveryRefused("G0_ACTIVITY_MANIFEST_MISMATCH",
                                      "Recovery inventory differs from the frozen activity manifest")
        states: dict[str, dict[str, list[dict]]] = {}
        for event in ledger_events:
            bucket = {"g0_task_started": "starts",
                      "g0_task_completed": "completions",
                      "g0_task_failed": "failures"}.get(event.get("event"))
            if bucket is None:
                continue
            task_id = event.get("task_id")
            if not isinstance(task_id, str) or not _SAFE_ID.fullmatch(task_id):
                raise RecoveryRefused("G0_TASK_ID_INVALID", "Task audit contains invalid identity")
            state = states.setdefault(task_id, {"starts": [], "completions": [], "failures": []})
            state[bucket].append(event)
        unknown_tasks = set(states) - set(expected_tasks)
        if unknown_tasks:
            raise RecoveryRefused("G0_UNEXPECTED_TASK", f"Unexpected task records: {sorted(unknown_tasks)}")
        completed, retryable, exhausted = [], [], []
        expected_files: set[str] = set()
        completed_files: set[str] = set()
        artifact_started: dict[str, dict] = {}
        artifact_written: dict[str, dict] = {}
        artifact_failed: set[str] = set()
        for event in ledger_events:
            kind = event.get("event")
            if kind == "g0_external_artifact_started":
                path = event.get("relative_path")
                if not isinstance(path, str) or path in artifact_started:
                    raise RecoveryRefused("G0_ARTIFACT_HISTORY_INVALID", "Duplicate or invalid artifact start")
                _safe_relative(path)
                artifact_started[path] = event
                expected_files.add(path)
            elif kind == "g0_external_artifact_written":
                path = event.get("relative_path")
                if not isinstance(path, str) or path in artifact_written:
                    raise RecoveryRefused("G0_ARTIFACT_HISTORY_INVALID", "Duplicate or invalid artifact commit")
                artifact_written[path] = event
            elif kind == "g0_external_artifact_failed":
                path = event.get("relative_path")
                if not isinstance(path, str) or path in artifact_failed:
                    raise RecoveryRefused("G0_ARTIFACT_HISTORY_INVALID", "Duplicate or invalid artifact failure")
                artifact_failed.add(path)
        if (set(artifact_written) - set(artifact_started) or
                artifact_failed - set(artifact_started) or
                set(artifact_written) & artifact_failed):
            raise RecoveryRefused("G0_ARTIFACT_HISTORY_INVALID", "Artifact terminal record lacks a unique start")
        if set(artifact_started) != set(artifact_written) or artifact_failed:
            raise RecoveryRefused("G0_ARTIFACT_INCOMPLETE",
                                  "Incomplete or failed external artifact requires manual reconciliation")
        for path, started in artifact_started.items():
            committed = artifact_written[path]
            namespace_by_kind = {"cache": "cache", "checkpoint": "checkpoints",
                                 "audit": "audit", "source_graph": "source-graphs",
                                 "diagnostic_log": "diagnostic-logs"}
            kind = started.get("artifact_kind")
            if (kind not in namespace_by_kind or _safe_relative(path)[0] != namespace_by_kind[kind] or
                    not isinstance(started.get("identity"), dict) or
                    started.get("artifact_kind") != committed.get("artifact_kind") or
                    started.get("identity") != committed.get("identity") or
                    committed.get("external_volume_uuid") != self._external_initial.volume_uuid):
                raise RecoveryRefused("G0_ARTIFACT_IDENTITY_MISMATCH", f"Artifact identity changed: {path}")
            identity = started["identity"]
            if (kind == "audit" and
                    identity.get("stream_format") == "G0_GZIP_CANONICAL_JSONL_AUDIT_V1"):
                metadata = committed.get("stream_metadata")
                expected_count = identity.get("expected_record_count")
                actual_count = metadata.get("record_count") if isinstance(metadata, dict) else None
                complete = metadata.get("complete") if isinstance(metadata, dict) else None
                tip = metadata.get("chain_tip_sha256") if isinstance(metadata, dict) else None
                if (type(expected_count) is not int or expected_count < 0 or
                        type(actual_count) is not int or not 0 <= actual_count <= expected_count or
                        type(complete) is not bool or not isinstance(tip, str) or
                        not _HEX64.fullmatch(tip) or
                        (complete and actual_count != expected_count) or
                        (not complete and actual_count >= expected_count)):
                    raise RecoveryRefused("G0_AUDIT_STREAM_METADATA_INVALID",
                                          f"Audit record-count metadata is invalid: {path}")
                if not complete:
                    task_id = identity.get("task_id")
                    attempt_id = identity.get("attempt_id")
                    task_state = states.get(task_id, {})
                    failures = [failure for failure in task_state.get("failures", [])
                                if failure.get("attempt_id") == attempt_id]
                    if len(failures) != 1:
                        raise RecoveryRefused("G0_PARTIAL_AUDIT_UNCLASSIFIED",
                                              f"Partial audit has no unique terminal task failure: {path}")
            parent, name = self._open_parent(path, create=False)
            try:
                digest, size = _hash_open_file(parent, name, self._external_initial.st_dev)
            finally:
                os.close(parent)
            if digest != committed.get("sha256") or size != committed.get("size_bytes"):
                raise RecoveryRefused("G0_ARTIFACT_CORRUPT", f"Artifact changed after commit: {path}")
            completed_files.add(path)
        watchdog_events = [event for event in ledger_events
                           if event.get("event") in (
                               "g0_watchdog_invocation_started",
                               "g0_watchdog_invocation_finished")]
        watchdog_starts: dict[int, dict] = {}
        watchdog_finishes: dict[int, dict] = {}
        for event in watchdog_events:
            invocation_id = event.get("invocation_id")
            if type(invocation_id) is not int or invocation_id < 1:
                raise RecoveryRefused("G0_WATCHDOG_RECORD_INVALID", "Invalid watchdog invocation ID")
            target = watchdog_starts if event["event"] == "g0_watchdog_invocation_started" else watchdog_finishes
            if invocation_id in target:
                raise RecoveryRefused("G0_WATCHDOG_RECORD_DUPLICATE", "Duplicate watchdog invocation record")
            target[invocation_id] = event
        if set(watchdog_starts) != set(watchdog_finishes):
            raise RecoveryRefused("G0_WATCHDOG_INVOCATION_INCOMPLETE",
                                  "Watchdog start/terminal records are not paired")
        for invocation_id, started in watchdog_starts.items():
            finished = watchdog_finishes[invocation_id]
            audit_name = f"watchdog.g0.{invocation_id}.jsonl"
            stdout_name = f"runner.g0.{invocation_id}.stdout.log"
            if (started.get("audit_name") != audit_name or
                    started.get("stdout_name") != stdout_name or
                    finished.get("audit_name") != audit_name or
                    finished.get("stdout_name") != stdout_name or
                    any(started.get(name) != finished.get(name)
                        for name in ("task_id", "attempt_id", "activity_id")) or
                    finished.get("artifact_error") or
                    finished.get("status") not in ("completed", "failed", "stopped")):
                raise RecoveryRefused("G0_WATCHDOG_ARTIFACT_INVALID",
                                      f"Watchdog evidence is incomplete or invalid: {invocation_id}")
            audit_path = self.control_dir / audit_name
            stdout_path = self.control_dir / stdout_name
            audit_sequence, audit_tip = verify_hash_chain(audit_path)
            if (audit_sequence != finished.get("audit_sequence") or
                    audit_tip != finished.get("audit_tip_sha256") or
                    _sha256_path(audit_path) != finished.get("audit_file_sha256") or
                    _sha256_path(stdout_path) != finished.get("stdout_sha256")):
                raise RecoveryRefused("G0_WATCHDOG_ARTIFACT_HASH_MISMATCH",
                                      f"Watchdog audit or stdout changed: {invocation_id}")
        if manifest_events:
            manifest_activity_id = manifest_events[0].get("activity_id")
            if any(
                    any(event.get(name) is None for name in
                        ("task_id", "attempt_id", "activity_id"))
                    for event in watchdog_starts.values()):
                raise RecoveryRefused("G0_TASK_WATCHDOG_MAPPING_INVALID",
                                      "Every Watchdog invocation in a frozen activity must bind a task")
            mapped_invocations: set[int] = set()
            for task_id, state in states.items():
                for started in state["starts"]:
                    invocation_id = started.get("invocation_id")
                    if (type(invocation_id) is not int or invocation_id < 1 or
                            invocation_id in mapped_invocations):
                        raise RecoveryRefused("G0_TASK_WATCHDOG_MAPPING_INVALID",
                                              f"Task start has invalid or duplicate invocation: {task_id}")
                    watchdog_start = watchdog_starts.get(invocation_id)
                    watchdog_finish = watchdog_finishes.get(invocation_id)
                    if (watchdog_start is None or watchdog_finish is None or
                            watchdog_start.get("task_id") != task_id or
                            watchdog_start.get("attempt_id") != started.get("attempt_id") or
                            watchdog_start.get("activity_id") != manifest_activity_id):
                        raise RecoveryRefused("G0_TASK_WATCHDOG_MAPPING_INVALID",
                                              f"Task start does not match its Watchdog invocation: {task_id}")
                    mapped_invocations.add(invocation_id)
            task_bound_invocations = {
                invocation_id for invocation_id, event in watchdog_starts.items()
                if event.get("task_id") is not None or event.get("attempt_id") is not None or
                event.get("activity_id") is not None}
            if task_bound_invocations != mapped_invocations:
                raise RecoveryRefused("G0_TASK_WATCHDOG_MAPPING_INVALID",
                                      "Task and Watchdog invocation inventories differ")
        for task_id, seed_fingerprint in expected_tasks.items():
            if not _SAFE_ID.fullmatch(task_id) or not _HEX64.fullmatch(seed_fingerprint):
                raise RecoveryRefused("G0_EXPECTED_INVENTORY_INVALID", "Task/seed inventory is malformed")
            state = states.get(task_id)
            if not state:
                continue
            starts = state["starts"]
            completions = state["completions"]
            failures = state["failures"]
            if len(starts) > 2 or len(completions) > 1:
                raise RecoveryRefused("G0_TASK_HISTORY_INVALID", f"Task history invalid: {task_id}")
            attempts = [x.get("attempt_id") for x in starts]
            if len(set(attempts)) != len(attempts):
                raise RecoveryRefused("G0_ATTEMPT_DUPLICATE", f"Repeated attempt ID: {task_id}")
            if any(x.get("seed_fingerprint") != seed_fingerprint for x in starts):
                raise RecoveryRefused("G0_TASK_SEED_CHANGED", f"Seed fingerprint changed: {task_id}")
            for started in starts:
                result_path = started.get("result_path")
                if result_path != self._expected_result_path(task_id, started["attempt_id"]):
                    raise RecoveryRefused("G0_TASK_PATH_MISMATCH", f"Result path changed: {task_id}")
                expected_files.add(result_path)
            if completions:
                completion = completions[0]
                prior_attempts = attempts[:-1]
                prior_failures = [x for x in failures if x.get("attempt_id") in prior_attempts]
                if (completion.get("attempt_id") != attempts[-1] or
                        completion.get("seed_fingerprint") != seed_fingerprint or
                        completion.get("result_path") != starts[-1].get("result_path") or
                        completion.get("external_volume_uuid") != self._external_initial.volume_uuid or
                        completion.get("internal_volume_uuid") != self._internal_initial.volume_uuid or
                        len(prior_failures) != len(prior_attempts) or
                        {x.get("attempt_id") for x in prior_failures} != set(prior_attempts) or
                        len(failures) != len(prior_attempts) or
                        any(x.get("failure_class") != "OPERATIONAL" or
                            x.get("reason_code") not in _OPERATIONAL_STORAGE_CODES or
                            not x.get("recovery_allowed") for x in prior_failures)):
                    raise RecoveryRefused("G0_TASK_COMPLETION_CONFLICT", f"Completion identity conflict: {task_id}")
                completed_files.add(completion["result_path"])
                parent, name = self._open_parent(completion["result_path"], create=False)
                try:
                    digest, size = _hash_open_file(parent, name, self._external_initial.st_dev)
                finally:
                    os.close(parent)
                if digest != completion.get("sha256") or size != completion.get("size_bytes"):
                    raise RecoveryRefused("G0_TASK_ARTIFACT_CORRUPT", f"Completed artifact changed: {task_id}")
                completed.append(task_id)
                continue
            if not starts:
                if failures:
                    raise RecoveryRefused("G0_TASK_HISTORY_INVALID", f"Failure without start: {task_id}")
                continue
            last = starts[-1]
            terminal = [x for x in failures if x.get("attempt_id") == last["attempt_id"]]
            prior_attempts = attempts[:-1]
            prior_failures = [x for x in failures if x.get("attempt_id") in prior_attempts]
            if (len(terminal) != 1 or len(prior_failures) != len(prior_attempts) or
                    {x.get("attempt_id") for x in prior_failures} != set(prior_attempts) or
                    len(failures) != len(prior_attempts) + 1):
                raise RecoveryRefused("G0_TASK_INTERRUPTION_UNCLASSIFIED",
                                      f"Incomplete/ambiguous attempt requires manual classification: {task_id}")
            if any(x.get("failure_class") != "OPERATIONAL" or
                   x.get("reason_code") not in _OPERATIONAL_STORAGE_CODES or
                   not x.get("recovery_allowed") for x in prior_failures):
                raise RecoveryRefused("G0_TASK_RETRY_FORBIDDEN",
                                      f"Earlier scientific or non-retryable failure blocks recovery: {task_id}")
            failure = terminal[0]
            if failure.get("failure_class") == "SCIENTIFIC" or not failure.get("recovery_allowed"):
                raise RecoveryRefused("G0_TASK_RETRY_FORBIDDEN",
                                      f"Scientific or non-retryable failure blocks recovery: {task_id}")
            if (failure.get("failure_class") != "OPERATIONAL" or
                    failure.get("reason_code") not in _OPERATIONAL_STORAGE_CODES):
                raise RecoveryRefused("G0_TASK_FAILURE_UNCLASSIFIED",
                                      f"Failure is not an approved operational storage event: {task_id}")
            if len(starts) >= 2:
                exhausted.append(task_id)
            else:
                retryable.append(task_id)
        actual_files, run_bytes = self._scan_managed_tree(
            self._run_fd, self._external_initial.st_dev)
        if not actual_files.issubset(expected_files) or not completed_files.issubset(actual_files):
            raise RecoveryRefused("G0_EXTERNAL_FILE_INVENTORY_MISMATCH",
                                  f"Managed file set differs from ledger; unexpected={sorted(actual_files-expected_files)}, missing_completed={sorted(completed_files-actual_files)}")
        with self._ledger_lock:
            self._task_event_index.clear()
            self._active_task_ids.clear()
            self._used_external_paths.clear()
            self._expected_external_paths.clear()
            self._committed_external_files.clear()
            self._watchdog_invocation_ids.clear()
            self._watchdog_invocations.clear()
            self._activity_manifest = None
            self._activity_task_seeds = None
            self._activity_task_order = None
            self._activity_verified = False
            self._has_prior_work = False
            for event in ledger_events:
                self._index_event(event)
            self._external_run_bytes = run_bytes
            self._recovery_verified = True
            self._activity_verified = bool(manifest_events)
        return RecoveryReport(tuple(sorted(completed)), tuple(sorted(retryable)),
                              tuple(sorted(set(expected_tasks) - set(states))),
                              tuple(sorted(exhausted)))

    def _managed_files(self, root_fd: int | None, expected_dev: int) -> set[str]:
        return self._scan_managed_tree(root_fd, expected_dev)[0]

    def _scan_managed_tree(self, root_fd: int | None,
                           expected_dev: int) -> tuple[set[str], int]:
        if root_fd is None:
            raise G0StorageError("G0_EXTERNAL_STORE_CLOSED", "External store is closed")
        files: set[str] = set()
        total_bytes = 0

        def visit(fd: int, prefix: tuple[str, ...]) -> None:
            nonlocal total_bytes
            for name in os.listdir(fd):
                info = os.stat(name, dir_fd=fd, follow_symlinks=False)
                if info.st_dev != expected_dev or stat.S_ISLNK(info.st_mode):
                    raise RecoveryRefused("G0_EXTERNAL_UNSAFE_ENTRY", "Cross-volume or symlink entry found")
                path = prefix + (name,)
                if stat.S_ISDIR(info.st_mode):
                    child = _open_or_create_dir(fd, name, create=False, expected_dev=expected_dev)
                    try:
                        visit(child, path)
                    finally:
                        os.close(child)
                elif stat.S_ISREG(info.st_mode):
                    files.add("/".join(path))
                    total_bytes += info.st_size
                else:
                    raise RecoveryRefused("G0_EXTERNAL_UNSAFE_ENTRY", "Unsupported filesystem entry found")

        visit(root_fd, ())
        return files, total_bytes

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        if self._ledger is not None:
            self._ledger.close()
            self._ledger = None
        for name in ("_run_fd", "_mount_fd", "_ledger_fd"):
            fd = getattr(self, name, None)
            if fd is not None:
                try:
                    os.close(fd)
                except OSError:
                    pass
                setattr(self, name, None)
    def __enter__(self) -> "G0ExternalStore":
        if self._closed:
            raise G0StorageError("G0_EXTERNAL_STORE_CLOSED", "External store is closed")
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
