from typing import Any

from parsing_utils.parsing_utils import parse_config
from generators.maze_generator import MazeGenerator
from entities.maze import Maze
from render.ascii import render
from pathfinding.breadth_first_search import BreadthFirstSearch


def create_maze(
        config: dict[str, Any],
        generator: MazeGenerator,
) -> Maze:
    """Create and generate a maze that follows the configuration."""
    entry_x, entry_y = config["ENTRY"]
    exit_x, exit_y = config["EXIT"]

    maze = Maze(
        config["HEIGHT"],
        config["WIDTH"],
        (entry_y, entry_x),
        (exit_y, exit_x),
    )
    generator.generate_HandK_maze(maze, config["PERFECT"])

    return maze


def main() -> None:
    """Run the interactive terminal loop of A-maze-ing."""
    config = parse_config()

    if not config:
        return

    generator = MazeGenerator(config.get("SEED"))
    bfs = BreadthFirstSearch()

    try:
        maze = create_maze(config, generator)
    except (ValueError, IndexError) as error:
        print(f"Invalid maze: {error}")
        return

    path = bfs.path_to_directions(bfs.find_shortest_path(maze))
    color_index = 0
    show_path = False

    while True:
        maze.write_to_file(config["OUTPUT_FILE"])
        bfs.write_to_file(config["OUTPUT_FILE"], path)
        print(render(maze, path, show_path, color_index))

        try:
            choice = input(
                "\n=== A-maze-ing ==="
                "\n1. Re-generate a new maze"
                "\n2. Show / Hide the shortest path"
                "\n3. Rotate the wall colours"
                "\n4. Quit"
                "\nChoice? (1-4): "
            )
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if choice == "1":
            maze = create_maze(config, generator)
            path = bfs.path_to_directions(bfs.find_shortest_path(maze))
        elif choice == "2":
            show_path = not show_path
        elif choice == "3":
            color_index += 1
        elif choice == "4":
            break
        else:
            print("Invalid choice, please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
