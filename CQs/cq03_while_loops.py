"""Practice using a while loop to iterate over a string"""

__author__ = 730656115


# This is a function that will count and return how many times a certain character occurs in a phrase
# FYI "e" and "E" are two separate characters and not seen as one
def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count += 1
            index += 1

        else:
            index += 1
    return count


print(num_instances(phrase="HelloHelloHello", search_char="e"))
