from entities.maze import Maze
from generators.hunt_and_kill import HuntAndKill
from generators.maze_braider import MazeBraider


class MazeGenerator:
    """Generate mazes using a selected generation algorithm."""

    def __init__(
            self,
            seed: int | None = None
    ):
        """Initialize the maze generator.

        Args:
            seed: Optional seed for reproducible maze generation.
        """
        self._hunt_and_kill = HuntAndKill(seed)
        self._pacman = MazeBraider(seed)

    def generate_maze(
            self,
            maze: Maze,
            algorithm: bool
    ) -> None:
        """Generate a maze using the selected algorithm.

        Args:
            maze: The maze to generate.
            algorithm: The algorithm to use.
        """
        if algorithm == True:
            self._hunt_and_kill.generate_maze(maze)

        elif algorithm == False:
            self._pacman.generate_maze(maze)

        else:
            raise ValueError(f"Unknown maze generation algorithm: {algorithm}")
