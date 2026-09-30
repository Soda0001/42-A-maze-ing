from constants.config_contents import CONFIG_CONTENTS
import sys
import typing


def validate_file():
    if not sys.argv[1].endswith(".txt"):
        raise OSError("[Errno 2] No such file or directory:")


def validate_argument_count() -> None:
    """Validate that exactly one command-line argument is provided.

    Raises:
        ValueError: If the number of command-line arguments is incorrect.
    """

    if len(sys.argv) != 2:
        raise ValueError(
            "Invalid usage - Expected usage is: "
            "python3 a-maze-ing config.txt"
        )


def read_config() -> dict[str, str]:
    """Read the configuration file and store its values in a dictionary.

    Returns:
        A dictionary containing the configuration keys and values.

    Raises:
        ValueError: If a configuration key is duplicated.
    """

    maze_config = {}
    try:
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
    
    except OSError as e:
        print(f"Invalid file - {e}")


def validate_mandatory_keys(contents: dict[str, str]) -> None:
    """Validate that all required configuration keys are present.

    Args:
        contents: Configuration data containing string values.

    Raises:
        ValueError: If a required configuration key is missing.
    """

    for key in CONFIG_CONTENTS:
        if key not in contents:
            raise ValueError(f"Missing mandatory item {key}")


def validate_config_keys(contents: dict[str, str]) -> None:
    """Validate that all configuration keys are recognized.

    Args:
        contents: Configuration data containing string values.

    Raises:
        ValueError: If an unrecognized configuration key is found.
    """

    for key in contents:
        if key not in CONFIG_CONTENTS:
            raise ValueError(f"Invalid key in config: {key}")


def validate_config_values(contents: dict[str, typing.Any]) -> None:
    """Validate that configuration values have the expected types.

    Args:
        contents: Configuration data containing converted values.

    Raises:
        ValueError: If a configuration value has an unexpected type.
    """

    for key, value in contents.items():
        if not isinstance(value, CONFIG_CONTENTS[key]):
            raise ValueError(f"Invalid value for {key}")


def convert_values(contents: dict[str, str]) -> dict[str, typing.Any]:
    """Convert configuration values to their expected Python types.

    Args:
        contents: Configuration data containing string values.

    Returns:
        A dictionary containing converted configuration values.

    Raises:
        ValueError: If a boolean value is invalid.
    """

    converted_config: dict[str, typing.Any] = {}

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
    """Read, validate, and convert the maze configuration.

    Returns:
        A dictionary containing the validated configuration.

    Raises:
        ValueError: If the configuration contains invalid values.
    """

    try:
        validate_file()
        validate_argument_count()
        config = read_config()
        validate_config_keys(config)
        validate_mandatory_keys(config)
        config = convert_values(config)
        validate_config_values(config)

        return config

    except (ValueError, OSError) as e:
        print(e)
        return {}

