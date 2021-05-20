import pytest
from src.selection_sort import *


def test_given_no_array_is_provided_then_exception_raised():
    with pytest.raises(Exception):
        sort(None)

# def test_given_empty_array_provided_then_exception_raised():
#     with pytest.raises(Exception):
#         sort([])

def test_given_unsorted_array_then_array_is_sorted():
    unsorted = [1, 99, 88, 104, 23, 54, 17]
    sorted = sort(unsorted)
    print(sorted)

    assert sorted[0] == 1
    assert sorted[1] == 17
    assert sorted[2] == 23
    assert sorted[3] == 54
    assert sorted[4] == 88
    assert sorted[5] == 99
    assert sorted[6] == 104