"""Transactional device deletion and narrowly-scoped artifact cleanup."""

from __future__ import annotations

import json
import os
import re
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable


ARTIFACT_SUFFIXES = (
    ".txt.enc", ".json.enc", ".csv.enc", ".html.enc", ".pdf.enc",
    ".txt", ".json", ".csv", ".html", ".pdf",
)
_NAME_RE = re.compile(r"^[^\x00-\x1f\x7f]+$")


@dataclass
class DeletionResult:
    device: str
    status: str
    db_committed: bool = False
    removed_files: list[str] = field(default_factory=list)
    failed_files: list[str] = field(default_factory=list)
    error: str | None = None

    @property
    def complete(self) -> bool:
        return self.status == "success"


def _sanitized(name: str) -> str:
    return re.sub(r"[^\w\-]", "_", name)


def _contained(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def _artifact_paths(device: str, names: list[str], root: Path,
                    backup_dir: Path, known: list[str]) -> list[Path]:
    prefix = _sanitized(device) + "_"
    # A sanitization collision cannot be safely disambiguated from a filename.
    if sum(_sanitized(n) == _sanitized(device) for n in names) > 1:
        prefix = None
    paths: list[Path] = []
    for raw in known:
        p = Path(raw)
        if not p.is_absolute():
            p = root / p
        if _contained(p, root) or _contained(p, backup_dir):
            paths.append(p)
    if prefix:
        for folder in (root, backup_dir):
            if not folder.is_dir():
                continue
            for entry in folder.iterdir():
                if (entry.is_file() and entry.name.startswith(prefix)
                        and entry.name.endswith(ARTIFACT_SUFFIXES)):
                    paths.append(entry)
    return list(dict.fromkeys(paths))


def _schedule_references(path: Path, device: str) -> tuple[list[Path], bool]:
    if not path.is_file():
        return [], False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return [], False
    changed = False
    if isinstance(data, list):
        kept = []
        for item in data:
            target = item.get("device") if isinstance(item, dict) else None
            if target == device:
                changed = True
            else:
                kept.append(item)
        new_data = kept
    elif isinstance(data, dict):
        new_data = dict(data)
        for key in ("device", "device_name", "target"):
            if new_data.get(key) == device:
                new_data.pop(key)
                changed = True
        for key, value in list(new_data.items()):
            if isinstance(value, dict) and value.get("device") == device:
                new_data.pop(key)
                changed = True
    else:
        return [], False
    if not changed:
        return [], False
    temp = path.with_name(path.name + ".delete")
    temp.write_text(json.dumps(new_data, indent=2), encoding="utf-8")
    os.replace(temp, path)
    return [path], True


def delete_device(
    name: str,
    *,
    db_path: str | os.PathLike,
    root_dir: str | os.PathLike = ".",
    backup_dir: str | os.PathLike = "config_backups",
    scheduled_file: str | os.PathLike = "scheduled_backups.json",
    unlink: Callable[[str | os.PathLike], None] = os.unlink,
) -> DeletionResult:
    """Delete one device's DB records, then its exact app-owned artifacts."""
    result = DeletionResult(name, "failed")
    if not isinstance(name, str) or not name or not _NAME_RE.match(name):
        result.error = "invalid device name"
        return result
    root = Path(root_dir).resolve()
    backup = (root / backup_dir).resolve() if not Path(backup_dir).is_absolute() else Path(backup_dir).resolve()
    schedule = (root / scheduled_file).resolve() if not Path(scheduled_file).is_absolute() else Path(scheduled_file).resolve()
    if not _contained(backup, root) or not _contained(schedule, root):
        result.error = "invalid cleanup path"
        return result

    known: list[str] = []
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS device_cleanup_pending "
                         "(device TEXT PRIMARY KEY, paths TEXT, updated TEXT)")
            names = [r[0] for r in conn.execute("SELECT name FROM devices").fetchall()]
            known.extend(r[0] for r in conn.execute(
                "SELECT filepath FROM backups WHERE device=?", (name,)).fetchall()
                if r[0])
            conn.execute("DELETE FROM logs WHERE device=?", (name,))
            conn.execute("DELETE FROM backups WHERE device=?", (name,))
            conn.execute("DELETE FROM alerts WHERE device=?", (name,))
            conn.execute("DELETE FROM devices WHERE name=?", (name,))
    except Exception as exc:
        result.error = "database deletion failed"
        return result
    result.db_committed = True

    try:
        _schedule_references(schedule, name)
    except Exception:
        result.failed_files.append(str(schedule))
    for path in _artifact_paths(name, names, root, backup, known):
        try:
            if path.exists():
                unlink(path)
                result.removed_files.append(str(path))
        except OSError:
            result.failed_files.append(str(path))

    if result.failed_files:
        result.status = "partial"
        with sqlite3.connect(db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO device_cleanup_pending(device,paths,updated) "
                "VALUES (?,?,datetime('now'))",
                (name, json.dumps(result.failed_files)),
            )
    else:
        result.status = "success"
        with sqlite3.connect(db_path) as conn:
            conn.execute("DELETE FROM device_cleanup_pending WHERE device=?", (name,))
    return result
