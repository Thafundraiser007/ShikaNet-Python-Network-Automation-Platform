import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "ShikaNet_V9.py"


def load_app_module():
    spec = importlib.util.spec_from_file_location("shikanet_v9_credentials", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_missing_device_credentials_rejects_unconfigured_device():
    module = load_app_module()

    assert module.missing_device_credentials({
        "host": "lab.example",
        "username": "",
        "password": "",
    })


def test_missing_device_credentials_allows_password_or_key_auth():
    module = load_app_module()

    assert not module.missing_device_credentials({
        "host": "lab.example",
        "username": "test-user",
        "password": "test-password",
    })
    assert not module.missing_device_credentials({
        "host": "lab.example",
        "username": "test-user",
        "password": "",
        "key_file": "test-key",
    })


def test_missing_device_credentials_requires_jump_host_credentials():
    module = load_app_module()

    message = module.missing_device_credentials({
        "host": "lab.example",
        "username": "test-user",
        "password": "test-password",
        "jump_host": "jump.example",
        "jump_username": "",
        "jump_password": "",
    })

    assert "Jump-host username" in message


def test_auto_discovery_defaults_are_unconfigured_in_source():
    source = SOURCE.read_text(encoding="utf-8")
    discovery = source[source.index("    def _add_discovered(self):"):]
    discovery = discovery[:discovery.index("    def _import_csv(self):")]

    assert '"username":"admin"' not in discovery
    assert '"username":""' in discovery
    assert '"password":""' in discovery
