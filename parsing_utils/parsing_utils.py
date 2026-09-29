import sys


def validate_argument_count() -> bool:
    """Check whether there are 2 arguments, including program name"""

    if len(sys.argv) != 2:
        print("Invalid usage, expected usage is:")
        print("./a-maze-ing config.txt")
        return False

    return True


def read_config(file_name: str) -> dict:
    """
    Reads the config.txt and gathers required information
    inside a dict
    """

    maze_config = {}

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            maze_config[key] = value

    return maze_config
            