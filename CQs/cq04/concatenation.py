"""We will be concatenating 2 strings together"""

__author__ = "730656115"


def concat(string_1: str, string_2: str) -> str:  # defining the concat function
    return string_1 + string_2


word1: str = "happy"
word2: str = "tuesday"


if __name__ == "__main__":  # supressing the concat function once its imported
    concat(word1, word2)
