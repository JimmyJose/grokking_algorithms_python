import pytest
from src.recursive_problems import *

def test_given_empty_list_then_sum_is_0():
    assert sumList([]) == 0

def test_given_valid_list_then_sum_is_returned():
    assert sumList([2, 4, 6]) == 12

def test_given_empty_list_then_size_is_0():
    assert sizeList([]) == 0

def test_given_valid_list_then_size_is_returned():
    assert sizeList([2, 4, 6]) == 3