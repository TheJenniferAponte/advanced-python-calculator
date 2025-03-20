from calculator.plugins import load_plugins
from calculator.plugins.basic_operations import AddCommand

def test_load_plugins():
    plugins = load_plugins()
    assert "addcommand" in plugins
    assert "subtractcommand" in plugins
    assert isinstance(plugins["addcommand"], AddCommand)

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