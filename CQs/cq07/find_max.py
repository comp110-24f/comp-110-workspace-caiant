"""Writing a function that will find and remove max"""

__author__ = "730656115"


# a function that will find and remove max of the list
def find_and_remove_max(a: list[int]) -> int:
    if len(a) == 0:
        return -1  # return value if empty string
    max = a[0]  # first number to compare
    for num in a:  # iterate through each num in the list
        if num > max:  # compare every number to first number
            max = num  # if number is bigger than replace max w num
    i = 0
    while i < len(a):  # iterate through each value of list a
        if max == a[i]:  # if the value is the max
            a.pop(i)  # remove the max
            i = i
        else:
            i += 1  # since you are removing the value, you must make sure to count each index
    return max
