"""EX02 - Chardle - Our version of Wordle"""

__author__ = 730656115


# Prompting for a 5-character word
def input_word() -> str:
    """Asking the user for a word"""
    user_word: str = input("Enter a 5-character word: ")  # storing the user's input
    if len(user_word) != 5:  # testing if there are 5 characters in the word
        print("Error: Word must contain 5 characters")
        exit()  # exits the program if the word > 5 characters long
    return user_word


# Prompting for a character
def input_letter() -> str:
    """Asking for a single character"""
    user_letter = input(
        "Enter a single character: "
    )  # storing the user's input for a single character
    if len(user_letter) != 1:  # seeing if it truly is a single character
        print("Error: Character must be a single character")
        exit()  # exits the program if it is not a single character
    return user_letter


# Finding character matches and recording their position
def contains_char(user_word: str, user_letter: str) -> None:
    """Checks if the character is present in the word and if the counts match"""
    print("searching for " + user_letter + " in " + user_word)
    count = 0
    i = 0
    while i < len(user_word):
        if user_word[i] == user_letter:
            print(user_letter + " found at index " + str(i))
            count += 1  # increasing count by 1 each time
        i += 1
    if count == 0:  # if there are no matches at all
        print("no instances of " + user_letter + " found in " + user_word)
    elif count == 1:  # For 1 match
        print("1 instance of " + user_letter + " found in " + user_word)
    else:  # For multiple matches
        print(str(count) + " instances of " + user_letter + " found in " + user_word)


# Putting all the functions under one function
def main() -> None:
    user_word = input_word()
    user_letter = input_letter()
    contains_char(user_word, user_letter)


# Calling the main function
if __name__ == "__main__":
    main()
