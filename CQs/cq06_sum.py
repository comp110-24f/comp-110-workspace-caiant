"""Summing the elements of a list using different loops"""

__author__ = "730656115"


# Using a while loop to iterate through a list and add elements together
def w_sum(vals: list[float]) -> float:
    indx = 0
    sum: float = 0.0
    while indx < len(vals):
        sum += vals[indx]  # adding each element to the sum as the list is reiterated
        indx += 1
    return sum


# Using a for loop to add elements
def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for elem in vals:
        sum += elem  # adding each element to sum
    return sum


# Using a for-in-range loop to sum elements
def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0  # starting value for sum
    idx = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]  # Adding each element to sum
    return sum  # return each sum


# Testing out my code
print(w_sum([1.1, 0.9, 1.0]))
print(f_sum([1.1, 0.9, 1.0]))
print(f_range_sum([1.0, -3.0, 4.0]))
