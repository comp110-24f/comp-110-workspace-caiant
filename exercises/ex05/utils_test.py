"""Testing my utility function files"""

__author__ = "730656115"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest


def test_only_evens_no() -> None:
    """Checking if a list only contains odd numbers"""
    a: list[int] = [1, 1]
    assert only_evens(a) == []


def test_only_evens_regular() -> None:
    """Checking if it will work properly with a list of odds and evens"""
    a: list[int] = [1, 2, 3, 4]
    assert only_evens(a) == [2, 4]


def test_only_evens_all() -> None:
    """Checking it it will work with a list of only evens"""
    a: list[int] = [2, 4, 6]
    assert only_evens(a) == [2, 4, 6]


def test_sub_neg() -> None:
    """Checking if it'll work with the start index as a negative"""
    b: list[int] = [1, 3, 5, 7]
    z = -2
    y = 3
    assert sub(b, z, y) == [1, 3, 5]


def test_sub_none() -> None:
    """Checking if it'll work with an empty list"""
    b: list[int] = []
    z = 3
    y = 4
    assert sub(b, z, y) == []


def test_sub_greater() -> None:
    """Checking if it'll work accurately with a larger ending index"""
    b: list[int] = [10, 25, 30]
    z = 1
    y = 8
    assert sub(b, z, y) == [25, 30]


def test_sub_regular() -> None:
    """Checking if it'll work with a normal set of index"""
    b: list[int] = [2, 8, 7, 8, 9]
    z = 1
    y = 3
    assert sub(b, z, y) == [8, 7]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    c: list[int] = [1, 3, 5]
    num1 = 8
    num2 = 7
    with pytest.raises(IndexError):
        add_at_index(c, num1, num2)
        # an IndexError is raised for the case when the add_at_index is given an index number > 2


def test_add_at_index_reg() -> None:
    """Test that the function properly mutates the list"""
    c: list[int] = [1, 2, 3]
    num1 = 9
    num2 = 1
    add_at_index(c, num1, num2)
    assert c == [1, 9, 2, 3]


def test_add_at_index_one() -> None:
    """Test that the function properly mutates the list if length == 1"""
    c: list[int] = [8]
    num1 = 20
    num2 = 1
    add_at_index(c, num1, num2)
    assert c == [8, 20]
