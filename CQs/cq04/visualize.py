"""Visualize and import concatenation function"""

__author__ = "730656115"

from CQs.cq04.concatenation import concat  # importing concat function

from CQs.cq04.coordinates import get_coords  # importing get_coords function


x: str = "123"  # global variables
y: str = "abc"  # globals

print(concat(x, y))  # print

get_coords(x, y)  # calling get_coords
