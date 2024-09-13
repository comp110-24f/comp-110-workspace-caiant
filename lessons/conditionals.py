"""practicing my conditionals"""


def less_than_10(num: int) -> bool:
    """Tell us if num < 10."""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("This is the end of the function!")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping. You deserve it. :)"


def check_first_letter(word: str, letter: str) -> bool:
    """Tell us if the first character of the word matches the letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match"


def get_weather_report() -> str:
    """Docstring."""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather
