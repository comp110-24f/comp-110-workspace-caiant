"""Implementing my utility functions"""

__author__ = "730656115"


# a function that will create a new list with only the evens
def only_evens(a: list[int]) -> list[int]:
    evens: list[int] = list()
    for elem in a:
        if elem % 2 == 0:  # if divisible by 2, add the item to the list
            evens.append(elem)
    return evens


# a function that will generate a subset of the list
def sub(b: list[int], z: int, y: int) -> list[int]:
    new: list[int] = list()
    if len(b) == 0:  # if given an empty list, return an empty list
        return []
    if y > len(
        b
    ):  # if the ending index is out of bounds, then end the list with the last item of the list
        y = len(b)
    if (
        z < 0
    ):  # if the starting index is negative, start the list with the first item of the list
        z = 0
    for idx in range(
        z, y
    ):  # reiterate through each item of the list and add the items between the indexes given
        new.append(b[idx])
    return new


# a function that will add a number at the given index
def add_at_index(c: list[int], num1: int, num2: int) -> None:
    if num2 > len(c):  # if the index is out of bounds
        raise IndexError("Index is out of bounds for the input list")
    if num2 < 0:  # if the index is out of bounds because its negative
        raise IndexError("Index is out of bounds for the input list")
    if len(c) > 0:  # if the list already has items
        c.append(len(c) - 1)  # add the pre-existing last item
        index: int = len(c) - 1
        while (
            index > num2
        ):  # while the biggest index of the list is > than the replaced index
            c[index] = c[index - 1]
            index -= 1
        c[num2] = num1
    else:
        c.append(num1)
