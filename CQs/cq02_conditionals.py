"""This is Challenge Question 2. I am writing a simple number guessing game"""

__author__ = 730656115


def guess_a_number() -> None:
    secret: int = 7
    x: str = input("Guess a number: ")
    print("Your guess was " + x)
    if int(x) == secret:
        print("You got it!")
    else:
        if int(x) < secret:
            print("Your guess was too low! The secret number is 7")
        else:
            print("Your guess was too high! The secret number is 7")

    return None


if __name__ == "__main__":
    guess_a_number()
