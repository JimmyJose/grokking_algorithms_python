import pytest
from src.quick_sort import *

def test_given_empty_array_then_it_is_already_sorted():
    assert sort([]) == []

def test_given_array_with_single_element_then_it_is_already_sorted():
    assert sort([10]) == [10]

def test_given_array_with_two_elements_then_it_is_sorted():
    assert sort([10, 5]) == [5, 10]

def test_given_an_unsorted_list_then_list_is_sorted():
    assert sort([2, 1, 3, 5, 4]) == [1, 2, 3, 4, 5]