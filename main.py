from parsing_utils.parsing_utils import parse_config
from generators.maze_generator import MazeGenerator
from entities.maze import Maze


def main() -> None:
    config = parse_config()
    if not config:
        return None

    maze = Maze(
        config["WIDTH"],
        config["HEIGHT"],
        config["ENTRY"],
        config["EXIT"],
    )

    maze_generator = MazeGenerator(seed=42)
    maze_generator.generate_maze(maze, config["PERFECT"])

    with open(config["OUTPUT_FILE"], "w") as file:
        for row in maze.get_cells():
            for cell in row:
                file.write(cell.get_representation())
            file.write("\n")


if __name__ == "__main__":
    main()
