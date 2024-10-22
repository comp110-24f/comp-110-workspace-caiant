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
    if len(b) == 0:  # if given an empyt list, return an empty list
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
    prev: int = c[len(c) - 1]  # storing the last digit
    if len(c) == 1:  # if length of the list is 1, all you have to do is append
        c.append(num1)
    else:  # if length is > 1
        initial: int = c[num2]  # the initial number at that index
        c.append(initial)  # adding the initial number
        for i in range(num2, len(c) - 1):  # shifting each item to the right
            c[i] = c[i + 1]
        c[num2] = num1
        c[len(c) - 1] = prev
