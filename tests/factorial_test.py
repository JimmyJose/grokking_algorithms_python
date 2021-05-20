import pytest
from src.factorial import *

def test_given_negative_input_then_exception_raised():
    with pytest.raises(Exception):
        compute(-1)

def test_given_zero_then_factorial_is_1():
    assert compute(0) == 1

def test_given_positive_number_then_factorial_is_computed():
    assert compute(5) == 120
