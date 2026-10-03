from parsing_utils.parsing_utils import parse_config


def main() -> None:
    config = parse_config()
    print(config)


if __name__ == "__main__":
    main()
