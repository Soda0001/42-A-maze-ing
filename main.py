import random

from parsing_utils.parsing_utils import parse_config
from generators.maze_generator import MazeGenerator
from generators.maze_braider import make_pacman_maze
from entities.maze import Maze
from render.ascii import render


def create_random_maze(perfect: bool) -> Maze:
    """Create a random maze with valid entry and exit coordinates."""
    while True:
        width = random.randint(3, 50)
        height = random.randint(3, 50)

        entry = (
            random.randint(0, height - 1),
            random.randint(0, width - 1),
        )

        exit = (
            random.randint(0, height - 1),
            random.randint(0, width - 1),
        )

        if entry == exit:
            continue

        try:
            maze = Maze(
                height,
                width,
                entry,
                exit,
            )
            MazeGenerator().generate_maze(maze, perfect)

        except (IndexError, ValueError):
            continue

        return maze


def main() -> None:
    try:
        config = parse_config()
    except Exception as e:
        print(e)
        return None

    if not config:
        return None

    maze = Maze(
        config["HEIGHT"],
        config["WIDTH"],
        config["ENTRY"],
        config["EXIT"],
    )

    maze_generator = MazeGenerator()
    maze_generator.generate_maze(maze, config["PERFECT"])

    color_index = 0
    show_path = False

    while True:
        maze.write_to_file(config["OUTPUT_FILE"])
        print(render(maze, "a", show_path, color_index))

        try:
            choice = input(
                "\n=== A-maze-ing ==="
                "\n1. Regenerate a new random maze"
                "\n2. Turn into pacman maze"
                "\n3. Show / Hide the shortest path"
                "\n4. Rotate the wall colours"
                "\n5. Quit"
                "\nChoice? (1-5): "
            )
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if choice == "1":
            maze = create_random_maze(True)

        elif choice == "2":
            make_pacman_maze(maze)

        elif choice == "3":
            show_path = not show_path

        elif choice == "4":
            color_index += 1

        elif choice == "5":
            break

        else:
            print("Invalid choice, please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
