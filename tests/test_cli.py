"""Tests for the camel2snake CLI."""

from camel2snake.cli import main


def test_cli_args(capsys):
    """Arguments are converted and printed one per line."""
    rc = main(["camelCase", "myVariableName"])
    out = capsys.readouterr().out
    assert rc == 0
    assert out == "camel_case\nmy_variable_name\n"


def test_cli_stdin(capsys, monkeypatch):
    """With no args, strings are read from stdin (one per line)."""
    import io

    monkeypatch.setattr("sys.stdin", io.StringIO("fooBar\nBazQux\n"))
    rc = main([])
    out = capsys.readouterr().out
    assert rc == 0
    assert out == "foo_bar\nbaz_qux\n"


def test_cli_version(capsys):
    """--version prints the version and exits 0."""
    import pytest

    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    assert "camel2snake" in capsys.readouterr().out
