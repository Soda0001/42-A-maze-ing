from ..constants.config_contents import CONFIG_CONTENTS
import typing
import sys


def validate_config_contents(contents: dict[str, typing.Any]) -> None:
    #check duplicate
    #check whether keys match
    #chheck whether values match

    for key, value in contents.items():
        if key not in CONFIG_CONTENTS:
            raise ValueError(f"Invalid key in config {key}")

        if not isinstance(value, CONFIG_CONTENTS[key]):
            raise ValueError(f"Invalid value for {key}")



    

    

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

            key, value = line.split("=", 1)
            maze_config[key] = value

    return maze_config
