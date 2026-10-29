from entities.maze import Maze
from generators.hunt_and_kill import HuntAndKill
from generators.maze_braider import transform_to_pacman_maze


class MazeGenerator:
    """Generate mazes using a selected generation algorithm."""

    def __init__(self, seed: int | None = None):
        self._seed = seed
        self._hunt_and_kill = HuntAndKill(seed)

    def generate_HandK_maze(
            self,
            maze: Maze,
            perfect: bool = True
    ) -> None:
        """Generate a maze using the Hunt and Kill algorithm."""
        self._hunt_and_kill.generate_maze(maze, perfect)
        if not perfect:
            transform_to_pacman_maze(maze, self._seed)
