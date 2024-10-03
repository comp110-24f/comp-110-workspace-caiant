"""Print formatted pairs of each character"""

__author__ = "730656115"


def get_coords(xs: str, ys: str) -> None:
    i = 0
    count = 0
    while i < len(xs):  # reiterate through the xs coordinate
        while count < len(ys):
            print("(" + xs[i] + "," + ys[count] + ")")
            count += 1
        i += 1
        count = 0  # setting it back to 0 so the ys loop runs again


get_coords("12", "34")
