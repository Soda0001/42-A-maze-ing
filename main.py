import random

from parsing_utils.parsing_utils import parse_config
from generators.maze_generator import MazeGenerator
from entities.maze import Maze
from render.ascii import render 


def create_random_maze(perfect: bool) -> Maze:
    """Create a random maze with valid entry and exit coordinates."""
    width = random.randint(3, 50)
    height = random.randint(3, 50)

    entry = (
        random.randint(0, width - 1),
        random.randint(0, height - 1),
    )

    exit = (
        random.randint(0, width - 1),
        random.randint(0, height - 1),
    )

    maze = Maze(
        width,
        height,
        entry,
        exit,
    )

    MazeGenerator().generate_maze(maze, perfect)

    return maze


def main() -> None:
    try:
        config = parse_config()
    except Exception as e:
        print(e)
        return None

    maze = Maze(
        config["WIDTH"],
        config["HEIGHT"],
        config["ENTRY"],
        config["EXIT"],
    )

    maze_generator = MazeGenerator()
    maze_generator.generate_maze(maze, config["PERFECT"])

    while True:
        maze.write_to_file(config["OUTPUT_FILE"])
        print(render(maze, "a", True, 35))

        choice = input(
            "\n=== A-maze-ing ==="
            "\n1. Regenerate a new random maze"
            "\n2. Regenerate a new pacman maze"
            "\n3. Quit"
            "\nChoice? (1-3): "
        )

        if choice == "1":
            maze = create_random_maze(True)

        elif choice == "2":
            maze = create_random_maze(False)

        elif choice == "3":
            break

        
if __name__ == "__main__":
    main()
