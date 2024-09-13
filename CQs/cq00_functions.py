"""Challenge Question000- Writing functions"""

___author___ = 730656115


def mimic(message: str) -> str:
    """Repeat input back."""
    return message


def main() -> None:
    """Return mimic message"""
    return print(mimic(message=input("what is your message?")))


if __name__ == "__main__":
    main()
