from CQs.cq07.find_max import find_and_remove_max

"""Testing the max function"""

__author__ = "730656115"


# returns expected value
def test_find_and_remove_max_return() -> None:
    b: list[int] = [1, 10]
    assert find_and_remove_max(b) == 10  # if true, this should pass


# mutates the input
def test_find_and_remove_max_mutate() -> None:
    c: list[int] = [1, 8, 8, 2]
    find_and_remove_max(c)
    assert c == [1, 2]  # if true, this should pass


# returns correct value in the case of unconventional input
def test_find_and_remove_max_odd() -> None:
    d: list[int] = []
    assert find_and_remove_max(d) == -1  # if true, this should pass
