"""Credential protection and authorization primitives for the desktop app."""
from __future__ import annotations

import base64
import getpass
import hashlib
import json
import os
import secrets
import stat
import threading
from functools import wraps
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken

_LOCK = threading.RLock()
ARTIFACT_MARKER = b"SHIKANET-ENC1\n"
_SECRET_FIELDS = frozenset({
    "password", "enable_secret", "jump_password", "console_ap_pass",
    "console_dev_pass", "api_key", "smtp_password",
})


def secret_fields():
    return _SECRET_FIELDS


def _key_path() -> Path:
    override = os.environ.get("SHIKANET_KEY_FILE")
    if override:
        return Path(override)
    root = Path(os.environ.get("APPDATA", Path.home())) / "ShikaNet"
    root.mkdir(parents=True, exist_ok=True)
    return root / "credential.key"


def _read_or_create_key() -> bytes:
    path = _key_path()
    with _LOCK:
        if path.exists():
            key = path.read_bytes().strip()
            Fernet(key)
            return key
        key = Fernet.generate_key()
        path.write_bytes(key)
        try:
            os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)
        except OSError:
            pass
        return key


def cipher() -> Fernet:
    return Fernet(_read_or_create_key())


def encrypt(value: object) -> str:
    if value is None:
        return ""
    return cipher().encrypt(str(value).encode("utf-8")).decode("ascii")


def decrypt(value: object) -> str:
    if value in (None, ""):
        return ""
    try:
        return cipher().decrypt(str(value).encode("ascii")).decode("utf-8")
    except (InvalidToken, ValueError, TypeError):
        return ""


def is_encrypted(value: object) -> bool:
    if value in (None, ""):
        return False
    try:
        cipher().decrypt(str(value).encode("ascii"))
        return True
    except (InvalidToken, ValueError, TypeError):
        return False


def encrypt_artifact(data: bytes) -> bytes:
    """Encrypt sensitive at-rest application data with the credential key."""
    if not isinstance(data, bytes):
        raise TypeError("artifact data must be bytes")
    return ARTIFACT_MARKER + cipher().encrypt(data)


def decrypt_artifact(data: bytes) -> bytes:
    if not data.startswith(ARTIFACT_MARKER):
        raise InvalidToken
    return cipher().decrypt(data[len(ARTIFACT_MARKER):])


def write_artifact(path: str | os.PathLike, data: bytes) -> str:
    """Atomically write encrypted data and restrict permissions where supported."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    encoded = encrypt_artifact(data)
    temp = target.with_name(target.name + ".writing")
    try:
        temp.write_bytes(encoded)
        try:
            os.chmod(temp, stat.S_IRUSR | stat.S_IWUSR)
        except OSError:
            pass
        os.replace(temp, target)
        try:
            os.chmod(target, stat.S_IRUSR | stat.S_IWUSR)
        except OSError:
            pass
    except Exception:
        try:
            temp.unlink()
        except OSError:
            pass
        raise
    return str(target)


def read_artifact(path: str | os.PathLike, migrate: bool = True) -> bytes:
    """Read an encrypted artifact, safely migrating a legacy plaintext file."""
    target = Path(path)
    raw = target.read_bytes()
    try:
        return decrypt_artifact(raw)
    except (InvalidToken, ValueError, TypeError):
        # Never replace a legacy file until encryption and the atomic write
        # have both succeeded.  A failure leaves the original untouched.
        if not migrate:
            return raw
        encoded = encrypt_artifact(raw)
        temp = target.with_name(target.name + ".migration")
        try:
            temp.write_bytes(encoded)
            try:
                os.chmod(temp, stat.S_IRUSR | stat.S_IWUSR)
            except OSError:
                pass
            os.replace(temp, target)
            try:
                os.chmod(target, stat.S_IRUSR | stat.S_IWUSR)
            except OSError:
                pass
        except Exception:
            try:
                temp.unlink()
            except OSError:
                pass
            raise
        return raw
def protect_record(record: dict) -> dict:
    result = dict(record)
    for field in _SECRET_FIELDS:
        if field in result and result[field]:
            result[field] = encrypt(result[field])
    return result


def reveal_record(record: dict) -> dict:
    result = dict(record)
    for field in _SECRET_FIELDS:
        if field in result:
            result[field] = decrypt(result[field])
    return result


def password_hash(password: str) -> str:
    # PBKDF2 keeps the existing schema compatible while avoiding fast hashes.
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 240_000)
    return "pbkdf2$240000$%s$%s" % (
        base64.urlsafe_b64encode(salt).decode(),
        base64.urlsafe_b64encode(digest).decode(),
    )


def password_matches(password: str, stored: str) -> bool:
    try:
        scheme, rounds, salt, digest = stored.split("$", 3)
        if scheme != "pbkdf2":
            return False
        actual = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), base64.urlsafe_b64decode(salt),
            int(rounds),
        )
        return secrets.compare_digest(
            actual, base64.urlsafe_b64decode(digest)
        )
    except (ValueError, TypeError):
        return False


ROLE_ORDER = {"viewer": 0, "operator": 1, "admin": 2}


def authorize(role: str | None, minimum: str = "operator") -> bool:
    return ROLE_ORDER.get((role or "").lower(), -1) >= ROLE_ORDER[minimum]


def require_role(minimum: str = "operator"):
    def decorator(func):
        @wraps(func)
        def wrapped(self, *args, **kwargs):
            role = getattr(self, "role", None) or getattr(self, "user_role", None)
            if not authorize(role, minimum):
                raise PermissionError(
                    f"{minimum} role required for {func.__name__}"
                )
            return func(self, *args, **kwargs)
        return wrapped
    return decorator


def migrate_json(path: str | os.PathLike) -> tuple[dict, bool]:
    """Load encrypted JSON, or safely migrate a legacy plaintext JSON file.

    The legacy file is replaced atomically with encrypted content after a
    successful parse.  Invalid files are never overwritten.
    """
    source = Path(path)
    if not source.exists():
        return {}, False
    raw = source.read_bytes()
    try:
        data = json.loads(cipher().decrypt(raw).decode())
        return data, False
    except Exception:
        data = json.loads(raw.decode("utf-8"))
        encoded = cipher().encrypt(json.dumps(data, indent=2).encode())
        temp = source.with_suffix(source.suffix + ".migration")
        temp.write_bytes(encoded)
        os.replace(temp, source)
        return data, True
