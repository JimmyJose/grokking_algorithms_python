import pytest
from src.breadth_first_search import *

def test_given_no_users_graph_then_an_exception_is_raised():
    with pytest.raises(Exception):
        search(None)

def test_given_mango_seller_among_friends_then_its_true():
    # Setup the test input(s) / condition(s)
    users_graph = {}
    users_graph["you"] = ["alice", "bob", "claire"]
    users_graph["alice"] = ["peggy"]
    users_graph["bob"] = ["anuj", "peggy"]
    users_graph["claire"] = ["jonny", "thom"]
    users_graph["peggy"] = []
    users_graph["anuj"] = []
    users_graph["jonny"] = []
    users_graph["thom"] = []

    # Execute the code
    found = search(users_graph)

    # Verify the test result(s) / condition(s)
    assert found == True

def test_given_no_mango_seller_among_friends_then_its_false():
    # Setup the test input(s) / condition(s)
    users_graph = {}
    users_graph["you"] = ["alice", "bob", "claire"]
    users_graph["alice"] = ["peggy"]
    users_graph["bob"] = ["anuj", "peggy"]
    users_graph["claire"] = ["jonny", "thon"]
    users_graph["peggy"] = []
    users_graph["anuj"] = []
    users_graph["jonny"] = []
    users_graph["thon"] = []

    # Execute the code
    found = search(users_graph)

    # Verify the test result(s) / condition(s)
    assert found == False