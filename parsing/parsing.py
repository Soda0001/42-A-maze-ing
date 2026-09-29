import sys


def validate_argument_count() -> bool:
    """Check whether there are 2 arguments, including program name"""

    if len(sys.argv) != 2:
        print("Invalid usage, expected usage is:")
        print("./a-maze-ing config.txt")
        return False

    return True
