import ast

import pytest

from ShikaNet_V9 import _PluginContext, _PluginValidator, PluginSecurityError
from security import authorize


def run_plugin(source, plugin):
    tree = ast.parse(source, filename="<test-plugin>", mode="exec")
    _PluginValidator().visit(tree)
    exec(compile(tree, "<test-plugin>", "exec"),
         {"__builtins__": {}}, {"plugin": plugin})


def test_authorized_plugin_can_use_approved_read_operation():
    calls = []
    plugin = _PluginContext(
        send=lambda command: calls.append(command) or "version",
        write=lambda text: calls.append(text),
        push=lambda lines: calls.append(lines) or "pushed",
        role="operator",
        names=["router"],
        current="router",
    )

    run_plugin("result = plugin.send('show version')\nplugin.write(result)", plugin)

    assert calls == ["show version", "version"]


def test_readonly_plugin_cannot_push_configuration():
    plugin = _PluginContext(
        send=lambda command: "",
        write=lambda text: None,
        push=lambda lines: pytest.fail("push must not be called"),
        role="readonly",
        names=[],
        current=None,
    )

    with pytest.raises(PluginSecurityError):
        run_plugin("plugin.push_config(['hostname blocked'])", plugin)


def test_plugin_cannot_access_raw_connection_or_application_state():
    plugin = _PluginContext(
        send=lambda command: "",
        write=lambda text: None,
        push=lambda lines: "",
        role="admin",
        names=["router"],
        current="router",
    )

    for source in (
        "conn.send_config_set(['hostname blocked'])",
        "plugin._send('show version')",
        "plugin.__class__",
        "__import__('os')",
    ):
        with pytest.raises(PluginSecurityError):
            run_plugin(source, plugin)


def test_plugin_read_api_rejects_mutating_commands():
    plugin = _PluginContext(
        send=lambda command: pytest.fail("mutating command must not be sent"),
        write=lambda text: None,
        push=lambda lines: "",
        role="operator",
        names=[],
        current=None,
    )

    with pytest.raises(PluginSecurityError):
        plugin.send("write memory")


@pytest.mark.parametrize(
    "role",
    ["viewer", "readonly", "", None],
)
def test_custom_cli_requires_operator_role(role):
    class Cli:
        _current_role = role
        denied = False

        def _ensure_role(self, minimum):
            self.denied = not authorize(self._current_role, minimum)
            return not self.denied

        def _req(self):
            pytest.fail("connection check must not run before authorization")

    cli = Cli()
    from ShikaNet_V9 import AppV9

    AppV9._run_cli(cli)

    assert cli.denied is True


def test_custom_cli_allows_operator_after_authorization():
    calls = []

    class Input:
        def get(self, *_):
            return "show version\nshow ip interface brief"

    class Cli:
        _current_role = "operator"
        cli_in = Input()
        cli_out = object()
        _hist = []
        _hidx = -1

        def _ensure_role(self, minimum):
            return authorize(self._current_role, minimum)

        def _req(self):
            return True

        def _run_q(self, cmds, box, label):
            calls.append((cmds, label))

    from ShikaNet_V9 import AppV9

    AppV9._run_cli(Cli())

    assert calls == [(["show version", "show ip interface brief"], "Custom CLI")]
