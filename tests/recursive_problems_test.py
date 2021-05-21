import pytest
from src.recursive_problems import *

def test_given_empty_list_then_sum_is_0():
    assert sum_list([]) == 0

def test_given_valid_list_then_sum_is_returned():
    assert sum_list([2, 4, 6]) == 12

def test_given_empty_list_then_size_is_0():
    assert size_list([]) == 0

def test_given_valid_list_then_size_is_returned():
    assert size_list([2, 4, 6]) == 3

def test_given_empty_list_then_exception_raised():
    with pytest.raises(Exception):
        max_list([])

def test_given_single_value_in_list_then_max_is_itself():
    assert max_list([10]) == 10

def test_given_valid_list_then_max_is_determined():
    assert max_list([10, 88, 55, 220, 11]) == 220