"""Getting some practice with dictionary functions"""

__author__ = "730656115"


# a function that will invert the keys and values of the function
def invert(given: dict[str, str]) -> dict[str, str]:
    new_dict: dict[str, str] = {}  # creating a new dict of the inverted elements
    key: str = ""  # making a key variable to store the key variable
    value: str = ""  # making a value variable to store the value variable

    for elem in given:
        key = elem  # making the key equal to the elem
        value = given[key]  # setting the value equal to the value of the given
        if value in new_dict:  # making sure there are no duplicate values
            raise KeyError("error message of your choice here!")
        new_dict[value] = (
            key  # the new key is the old value, the new value is the old key
        )

    return new_dict  # return the new list


# a function that returns the most popular color
def favorite_color(input: dict[str, str]) -> str:
    color_name: str = ""
    result: dict[str, int] = {}  # create a dictionary with color and frequency
    for elem in input:
        if input[elem] in result:  # if the color is in new dict
            result[input[elem]] += 1
        else:  # if this is first time the color returns
            result[input[elem]] = 1
        if color_name == "":  # for the first color, assign the color to color_name
            color_name = input[elem]
        if (
            result[input[elem]] > result[color_name]
        ):  # if this color appears more often the the previous color, than replace most popular
            color_name = input[elem]
    return color_name


# find the count of each value in a list
def count(given_list: list[str]) -> dict[str, int]:
    value_count: dict[str, int] = (
        {}
    )  # Creating a new dict with the key as the value in the list and the value as the count
    for item in given_list:  # iterate through each item in the list
        if item in value_count:  # if already in dict, add 1
            value_count[item] += 1
        else:  # if not in dict, put the key as appearing once
            value_count[item] = 1
    return value_count  # return the resulting dict


# sort words of a list by their first letter
def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    alpha_dict: dict[str, list[str]] = {}  # creating a new dict
    for elem in input_list:  # iterate through each element
        first_letter = elem[
            0
        ].lower()  # find the lowercase value of the first letter of the word
        if first_letter in alpha_dict:  # if this letter is a key already in the dict
            alpha_dict[first_letter].append(elem)  # add this letter to the list
        else:
            alpha_dict[first_letter] = [elem]  # make a new list for the value
    return alpha_dict  # return the dictionary


# Update the attendance
def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    if (
        day in attendance_log
    ):  # if the day is already in dict, add the student to that list
        if student in attendance_log:
            return None
        else:
            attendance_log[day].append(student)
    else:  # if new day, create a key for that day and start a list of students
        attendance_log[day] = [student]
    return None
