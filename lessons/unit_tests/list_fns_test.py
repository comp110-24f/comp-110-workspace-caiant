from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    fruits: list[str] = ["apples", "oranges", "lime"]
    assert get_first(fruits) == "apples"


def test_remove_first_ret_value() -> None:
    """Test that removes first, returns none"""
    fruits: list[str] = ["apples", "oranges", "lime"]
    assert remove_first(fruits) == None


def test_remove_first_behavior() -> None:
    """Test that remove first removes first element"""
    fruits: list[str] = ["apples", "oranges", "lime"]
    remove_first(fruits)
    assert fruits == ["oranges", "lime"]


def test_get_first_edge_case() -> None:
    """Test that get_first works with empty lists"""
    input: list[str] = []
    assert get_first([]) == ""
