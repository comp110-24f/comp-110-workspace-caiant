"""Practicing list functions"""


def get_first(a: list[str]) -> str:
    if len(a) == 0:
        return ""
    return a[0]


def remove_first(a: list[str]) -> None:
    """Remove first element."""
    a.pop(0)


def get_and_remove_first(a: list[str]) -> str:
    """Remove and return first element"""
    b = a[0]
    a.pop(0)
    return b
