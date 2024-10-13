"""Gaining familiary with the names and behaviors of commonly used functions"""

__author__ = "730656115"


# a function that will evaluate whether all the ints =  given int
def all(vals: list[int], given: int) -> bool:
    if len(vals) == 0:  # if empty list, return False
        return False
    for elem in vals:  # iterate through each element
        if elem != given:  # if elem does not equal given
            return False
    return True


# a function that will return the max number in the list
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
        return False
    max_value = input[0]  # first number to compare
    for num in input:  # iterate through each item in the list
        if num > max_value:  # compare every number to first number
            max_value = num  # if number is bigger than replace
    return max_value


# a function that will compare two lists to see if each respective index is equal to each other
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):  # need to be list of same lengths
        return False
    for i in range(len(list_1)):  # iterate through each index of the list
        if list_1[i] != list_2[i]:  # testing if values of the same index are equal
            return False  # if not, return False
    return True  # True if they are equal


# A function that will mutate the first list by appending the second lists values
def extend(a: list[int], b: list[int]) -> None:
    for elem in b:  # iterate through each value in list b
        a.append(elem)  # add each element of b to add
    return None
