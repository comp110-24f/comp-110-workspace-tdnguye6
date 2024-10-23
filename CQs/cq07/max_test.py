"""Test module for find_and_remove_max function from find_max"""

from CQs.cq07.find_max import find_and_remove_max

__author__: str = "730766559"


def test_find_and_remove_max_use_case1() -> None:
    assert find_and_remove_max([1, 2, 5, 4, 5]) == 5


def test_find_and_remove_max_use_case2() -> None:
    assert find_and_remove_max([1, 2, 10, 10, 5]) == 10


def test_find_and_remove_max_edge_case1() -> None:
    assert find_and_remove_max([]) == -1
