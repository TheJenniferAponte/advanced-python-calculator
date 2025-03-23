import pytest
from calculator.core import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5.0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3.0

def test_multiply():
    calc = Calculator()
    assert calc.multiply(4, 5) == 20.0

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0

def test_add_invalid_input_llyl():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.add("a", 3)

def test_subtract_invalid_input_eafp():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.subtract("b", 2)

def test_multiply_invalid_input():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.multiply("x", 5)

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

def test_add_logging(caplog):
    calc = Calculator()
    with caplog.at_level("INFO"):
        calc.add(1, 2)
    assert "Adding 1 + 2 = 3.0" in caplog.text


def test_divide_invalid_input():
    from calculator.core import Calculator
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide("a", "b")