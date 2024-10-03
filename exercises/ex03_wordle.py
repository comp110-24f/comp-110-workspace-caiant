"""Making a Wordle File"""

__author__ = "730656115"


# A function that takes user input for a guess
def input_guess(secret_word_len: int) -> str:  # Enter a guess
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while (
        len(guess) != secret_word_len
    ):  # testing if the length of the guess is correct
        guess: str = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


# A function that checks if any of the characters of the guess is in the secret word
def contains_char(
    secret_word: str, char_guess: str
) -> bool:  # Will return a True or False value
    """Searching for a character in the secret word"""
    assert (
        len(char_guess) == 1
    )  # the length of char_guess must be 1 for this function to run
    count: int = 0
    i = 0
    while i < len(
        secret_word
    ):  # reiterate through the different index of the secret_word
        if secret_word[i] == char_guess:
            count += 1
        i += 1
    if count != 0:  # when the char_guess is found in the word
        return True
    else:  # char_guess is not in the word
        return False


# A function that uses emojis to visually represent the accuracy of a guess in relation to a secret word
def emojified(guess: str, secret_word: str) -> str:
    assert len(guess) == len(
        secret_word
    )  # the lengths of the guess and secret_word must be equal for this to run
    # The emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    index = 0
    # This will loop throughout the guess and see if any of the characters of the same index match
    while index < len(secret_word):
        if (
            guess[index] == secret_word[index]
        ):  # if the characters in the same index match
            emoji += GREEN_BOX
        elif (
            contains_char(secret_word, guess[index]) == True
        ):  # if the character is in the word but not in that index
            emoji += YELLOW_BOX
        else:  # the character is not in the word
            emoji += WHITE_BOX
        index += 1
    return emoji  # returns the concatenated string


# A main function that brings everything together
def main(secret_word: str) -> None:
    turn: int = 0
    # A player is given 6 turns to guess the word
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess_word = input_guess(len(secret_word))
        print(emojified(guess_word, secret_word))
        # The player guesses the correct secret_word
        if guess_word == secret_word:
            print(f"You won in {turn}/6 turns!")
            quit()
        turn += 1
    # The player ran out of turns
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
