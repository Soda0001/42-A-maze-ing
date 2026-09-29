import sys


def validate_argument_count() -> bool:
    """Check whether there are 2 arguments, including program name"""

    if len(sys.argv) != 2:
        print("Invalid usage, expected usage is:")
        print("./a-maze-ing config.txt")
        return False

    return True


def read_config(file_name: str) -> dict:
    """Read the configuration file and store its values in a dictionary.

    Args:
        file_name: Name of the configuration file to read.

    Returns:
        A dictionary containing the configuration keys and values.
    """

    maze_config = {}

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=")
            maze_config[key] = value

    return maze_config
