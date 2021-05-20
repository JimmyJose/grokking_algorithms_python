import pytest
from src.recursive_list_sum import *

def test_given_empty_list_then_returns_0():
    assert sum([]) == 0

def test_given_valid_list_then_sum_is_returned():
    assert sum([2, 4, 6]) == 12