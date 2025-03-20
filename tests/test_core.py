import pytest
from calculator.core import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5.0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3.0

def test_add_invalid_input_llyl():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.add("a", 3)

def test_subtract_invalid_input_eafp():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.subtract("b", 2)