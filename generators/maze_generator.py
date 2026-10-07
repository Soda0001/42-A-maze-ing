from entities.maze import Maze
from generators.hunt_and_kill import HuntAndKill


class MazeGenerator:
    """Generate mazes using a selected generation algorithm."""

    def __init__(self, seed: int | None = None):
        self._seed = seed

    def generate_HandK_maze(
            self,
            maze: Maze,
            perfect: bool = True
    ) -> None:
        """Generate a maze using the Hunt and Kill algorithm.

        Args:
            maze: The maze to generate.
            perfect: Whether to generate a perfect maze.
        """
        hunt_and_kill = HuntAndKill(self._seed)
        hunt_and_kill.generate_maze(maze, perfect)
