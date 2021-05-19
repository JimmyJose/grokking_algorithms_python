import pytest
from src.binary_search import *

def test_given_no_search_item_provided_then_exception_raised():
    with pytest.raises(Exception):
        search(None, [ 1, 3, 5, 7, 9])


def test_given_no_array_is_provided_then_exception_raised():
    with pytest.raises(Exception):
        search(3)

def test_given_empty_array_provided_then_exception_raised():
    with pytest.raises(Exception):
        search(3, [])

def test_given_item_not_found_then_none_is_returned():
    assert search(2, [ 1, 3, 5, 7, 9]) == None

def test_given_item_is_found_then_items_index_in_array_is_returned():
    assert search(3, [ 1, 3, 5, 7, 9]) == 1