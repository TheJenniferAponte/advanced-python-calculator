import pytest
from calculator.plugins import load_plugins
from calculator.plugins.basic_operations import (
    AddCommand,
    SubtractCommand,
    MultiplyCommand,
    DivideCommand
)

def test_load_plugins():
    plugins = load_plugins()
    assert "addcommand" in plugins
    assert "subtractcommand" in plugins
    assert "multiplycommand" in plugins
    assert "dividecommand" in plugins
    assert isinstance(plugins["addcommand"], AddCommand)
    assert isinstance(plugins["subtractcommand"], SubtractCommand)
    assert isinstance(plugins["multiplycommand"], MultiplyCommand)
    assert isinstance(plugins["dividecommand"], DivideCommand)

def test_add_command():
    from calculator.core import Calculator
    cmd = AddCommand()
    calc = Calculator()
    cmd.execute(calc, "4", "5")
    assert calc.history.df.iloc[-1]["result"] == 9.0

def test_add_command_invalid_args():
    from calculator.core import Calculator
    cmd = AddCommand()
    calc = Calculator()
    with pytest.raises(ValueError):
        cmd.execute(calc, "1")

def test_subtract_command():
    from calculator.core import Calculator
    cmd = SubtractCommand()
    calc = Calculator()
    cmd.execute(calc, "5", "3")
    assert calc.history.df.iloc[-1]["result"] == 2.0

def test_subtract_command_invalid_args():
    from calculator.core import Calculator
    cmd = SubtractCommand()
    calc = Calculator()
    with pytest.raises(ValueError):
        cmd.execute(calc, "5")

def test_multiply_command():
    from calculator.core import Calculator
    cmd = MultiplyCommand()
    calc = Calculator()
    cmd.execute(calc, "4", "5")
    assert calc.history.df.iloc[-1]["result"] == 20.0

def test_multiply_command_invalid_args():
    from calculator.core import Calculator
    cmd = MultiplyCommand()
    calc = Calculator()
    with pytest.raises(ValueError):
        cmd.execute(calc, "4")

def test_divide_command():
    from calculator.core import Calculator
    cmd = DivideCommand()
    calc = Calculator()
    cmd.execute(calc, "10", "2")
    assert calc.history.df.iloc[-1]["result"] == 5.0

def test_divide_command_invalid_args():
    from calculator.core import Calculator
    cmd = DivideCommand()
    calc = Calculator()
    with pytest.raises(ValueError):
        cmd.execute(calc, "10")