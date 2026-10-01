import random

from entities.maze import Maze
from entities.cell import Cell


class MazeGenerator:
    def __init__(
            self,
            seed: int | None = None
    ):
        self._random = random.Random(seed)
