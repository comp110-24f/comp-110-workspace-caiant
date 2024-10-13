"""Mutating functions."""

__author__ = "730656115"

# Global Variables
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


# A function that will add a new value to a pre-existing list
def manual_append(vals: list[int], new: int) -> None:
    vals.append(new)


# A function that will double each value of the list
def double(b: list[int]) -> None:
    index = 0
    while index < len(b):  # Iterating through each value of the list
        b[index] = b[index] * 2  # Double each value
        index += 1


# Double list_2
double(list_2)

# Print both lists
print(list_1)
print(list_2)
