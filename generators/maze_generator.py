from entities.maze import Maze
from generators.hunt_and_kill import HuntAndKill
from generators.maze_braider import make_pacman_maze


class MazeGenerator:
    """Generate mazes using a selected generation algorithm."""

    def __init__(self, seed: int | None = None):
        self._hunt_and_kill = HuntAndKill(seed)
        self._seed = seed

    def generate_maze(
            self,
            maze: Maze,
            algorithm: bool
    ) -> None:
        """Generate a maze using the selected algorithm."""
        if algorithm:
            self._hunt_and_kill.generate_maze(maze)
        else:
            self._hunt_and_kill.generate_maze(maze)
            make_pacman_maze(maze, self._seed)
