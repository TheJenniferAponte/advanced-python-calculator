import pytest
from calculator.repl import REPL
from io import StringIO
import sys

def test_repl_menu(capsys):
    repl = REPL()
    repl.show_menu()
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "add" in captured.out
    assert "exit" in captured.out

def test_repl_execute_command(monkeypatch, capsys):
    repl = REPL()
    monkeypatch.setattr("sys.stdin", StringIO("add 2 3\n"))
    repl.execute_command("add", ["2", "3"])
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

def test_repl_unknown_command(capsys):
    repl = REPL()
    repl.execute_command("foo", [])
    captured = capsys.readouterr()
    assert "Unknown command" in captured.out
    