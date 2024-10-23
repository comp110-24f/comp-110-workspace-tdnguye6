import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""Unit tests for list utility functions for EX05"""

__author__: str = "730766559"


def test_only_evens_use_case1():
    assert only_evens([3, 6, 9, 12]) == [6, 12]


def test_only_evens_use_case2():
    assert only_evens([10, 20, 30, 40, 47]) == [10, 20, 30, 40]


def test_only_evens_edge_case1():
    assert only_evens([]) == []


def test_only_evens_edge_case2():
    assert only_evens([1, 3, 5, 7, 9, 11]) == []


def test_sub_use_case1():
    assert sub([0, 1, 0, 1, 0], 1, 4) == [1, 0, 1]


def test_sub_use_case2():
    assert sub([9, 18, 27, 36, 45, 54, 63], -1, 7) == [9, 18, 27, 36, 45, 54, 63]


def test_sub_edge_case1():
    assert sub([], 0, 5) == []


def test_add_at_index_use_case1():
    input: list[int] = [2, 4, 6, 8, 12]
    add_at_index(input, 10, 4)
    assert input == [2, 4, 6, 8, 10, 12]


def test_add_at_index_use_case2():
    input: list[int] = [6, 36, 1296, 7776]
    add_at_index(input, 216, 2)
    assert input == [6, 36, 216, 1296, 7776]


def test_add_at_index_raises_indexerror():
    """Check if add_at_index raises an IndexError for an invalid index."""
    with pytest.raises(IndexError):
        # Throw an expected IndexError after indexing out of the range of given list
        add_at_index([1, 8, 12, 16, 2], 20, 6)
