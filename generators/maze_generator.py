import random

from entities.maze import Maze
from entities.cell import Cell


class MazeGenerator:
    def __init__(
            self,
            seed: int | None = None
    ):
        self._random = random.Random(seed)

    def generate_maze(self, maze: Maze):
        ...

    def carve_path(self, current_cell: Cell, next_cell: Cell) -> None:

        current_row = current_cell.get_row()
        current_column = current_cell.get_column()

        next_row = next_cell.get_row()
        next_column = next_cell.get_column()

        current_cell.set_row(next_row)
        current_cell.set_column(next_column)

        if current_row == next_row - 1:
            current_cell.set_north(False)
            next_cell.set_north(False)

        elif current_row == next_row + 1:
            current_cell.set_south(False)
            next_cell.set_south(False)

        elif current_column == next_column - 1:
            current_cell.set_west(False)
            next_cell.set_west(False)

        elif current_column == next_column + 1:
            current_cell.set_east(False)
            next_cell.set_east(False)

        current_cell.set_is_visited(True)
        next_cell.set_is_visited(True)
