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

def test_repl_execute_subtract(monkeypatch, capsys):
    repl = REPL()
    monkeypatch.setattr("sys.stdin", StringIO("subtract 5 3\n"))
    repl.execute_command("subtract", ["5", "3"])
    captured = capsys.readouterr()
    assert "Result: 2.0" in captured.out

def test_repl_execute_multiply(monkeypatch, capsys):
    repl = REPL()
    monkeypatch.setattr("sys.stdin", StringIO("multiply 4 5\n"))
    repl.execute_command("multiply", ["4", "5"])
    captured = capsys.readouterr()
    assert "Result: 20.0" in captured.out

def test_repl_execute_divide(monkeypatch, capsys):
    repl = REPL()
    monkeypatch.setattr("sys.stdin", StringIO("divide 10 2\n"))
    repl.execute_command("divide", ["10", "2"])
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

def test_repl_unknown_command(capsys):
    repl = REPL()
    repl.execute_command("foo", [])
    captured = capsys.readouterr()
    assert "Unknown command" in captured.out

def test_repl_start_exit(monkeypatch, capsys):
    repl = REPL()
    monkeypatch.setattr("sys.stdin", StringIO("exit\n"))
    repl.start()
    captured = capsys.readouterr()
    assert "Welcome to the Advanced Calculator" in captured.out

def test_repl_error_handling(monkeypatch, capsys):
    repl = REPL()
    monkeypatch.setattr("sys.stdin", StringIO("add 1\nexit\n"))
    repl.start()
    captured = capsys.readouterr()
    assert "Error: Add requires 2 arguments" in captured.out