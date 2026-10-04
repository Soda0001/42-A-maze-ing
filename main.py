from parsing_utils.parsing_utils import parse_config
from generators.maze_generator import MazeGenerator
from entities.maze import Maze
from render.ascii import render 


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

    maze_generator = MazeGenerator(seed=4)
    maze_generator.generate_maze(maze, config["PERFECT"])

    maze.write_to_file(config["OUTPUT_FILE"])
    print(render(maze, "a", True, 35))


if __name__ == "__main__":
    main()
