from constants.config_contents import CONFIG_CONTENTS
import typing
import sys


def validate_argument_count() -> None:
    """Check whether there are 2 arguments, including program name"""

    if len(sys.argv) != 2:
        raise ValueError(
            "Invalid usage - Expected usage is:"
            "./a-maze-ing config.txt"
        )


def read_config() -> dict[str, str]:
    """Read the configuration file and store its values in a dictionary.

    Args:
        file_name: Name of the configuration file to read.

    Returns:
        A dictionary containing the configuration keys and values.
    """

    maze_config = {}

    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)

            if key in maze_config:
                raise ValueError(f"Duplicate item in config: {key}")
            
            maze_config[key] = value

    return maze_config


def validate_config_keys(contents: dict[str, typing.Any]) -> None:
    """Validate that all configuration keys are recognized."""

    for key in contents:
        if key not in CONFIG_CONTENTS:
            raise ValueError(f"Invalid key in config: {key}")


def validate_config_values(contents: dict[str, typing.Any]) -> None:
    for key, value in contents.items():
        if not isinstance(value, CONFIG_CONTENTS[key]):
            raise ValueError(f"Invalid value")


def convert_values(contents: dict[str, typing.Any]) -> dict[str, typing.Any]:
    converted_config = {}

    for key, value in contents.items():
        if key == "WIDTH" or key == "HEIGHT":
            converted_config[key] = int(value)

        if key == "ENTRY" or key == "EXIT":
            converted_config[key] = tuple(int(x) for x in value.split(","))

        if key == "OUTPUT_FILE":            
            converted_config[key] = value
        
        if key == "PERFECT":
            if value.lower() == "true":
                converted_config[key] = True

            elif value.lower() == "false":
                converted_config[key] = False

            else:
                raise ValueError(
                    "Invalid value in config - invalid type for boolean"
                ) 

    return converted_config


def parse_config() -> dict[str, typing.Any]:
    try:
        validate_argument_count()
        config = read_config()
        validate_config_keys(config)
        config = convert_values(config)
        validate_config_values(config)

        return config
    
    except ValueError as e:
        print(e)
        return {}
