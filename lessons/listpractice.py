"""Practicing making lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor


print(my_numbers)
my_numbers.append(1.5)
my_numbers.append(2.3)
print(my_numbers)


game_points: list[int] = [102, 86, 94]

game_points[1] = 72

print(game_points)

game_points.append(102)

# Write a function called display
# input: list[int]
# Return Value: None
# Loop over the input and print every value
# Try calling it on game_points


def display(Input: list[int]) -> None:
    index: int = 0
    while index < len(Input):
        print(Input[index])
        index + 1


display(Input=game_points)
