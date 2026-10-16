import random

from entities.maze import Maze
from entities.cell import Cell


class HuntAndKill:
    """Generate mazes using the Hunt and Kill algorithm."""

    def __init__(
            self,
            seed: int | None = None
    ):
        """Initialize the Hunt and Kill generator.

        Args:
            seed: Optional seed for reproducible maze generation.
        """
        self._random = random.Random(seed)
        self._seed = seed

    def carve_path(self, current_cell: Cell, next_cell: Cell) -> None:
        """Carve a passage between two adjacent cells.

        Args:
            current_cell: The current cell.
            next_cell: The adjacent cell to connect to the current cell.
        """
        current_row = current_cell.get_row()
        current_column = current_cell.get_column()

        next_row = next_cell.get_row()
        next_column = next_cell.get_column()

        match (current_row - next_row, current_column - next_column):
            case (-1, 0):
                current_cell.set_south()
                next_cell.set_north()
            case (1, 0):
                current_cell.set_north()
                next_cell.set_south()
            case (0, -1):
                current_cell.set_east()
                next_cell.set_west()
            case (0, 1):
                current_cell.set_west()
                next_cell.set_east()

        current_cell.set_is_visited(True)
        next_cell.set_is_visited(True)

        current_cell.represent()
        next_cell.represent()

    def get_unvis_cell_with_vis_neighbour(
            self,
            maze: Maze,
    ) -> Cell | None:
        """Find an unvisited cell with a visited neighbour.

        Args:
            maze: The maze to search.

        Returns:
            An unvisited cell with a visited neighbour, or None if no
            suitable cell is found.
        """
        rows = maze.get_cells()

        for row in range(len(rows)):
            for column in range(len(rows[row])):
                current_cell = rows[row][column]

                if (
                    not current_cell.is_visited()
                    and not current_cell.is_restricted()
                ):
                    if maze.get_visited_neighbours(current_cell):
                        return current_cell

        return None

    def kill(self, maze: Maze, current_cell: Cell) -> None:
        """Run the kill phase from the given cell.

        Args:
            maze: The maze to generate.
            current_cell: The cell to start from.
        """
        current_cell.set_is_visited(True)

        while unvisited_neighbours := maze.get_unvisited_neighbours(
            current_cell
        ):
            next_cell = self._random.choice(unvisited_neighbours)

            self.carve_path(current_cell, next_cell)

            current_cell = next_cell

    def hunt_and_kill(self, maze: Maze, current_cell: Cell) -> None:
        """Run the Hunt and Kill algorithm from a starting cell.

        Args:
            maze: The maze to generate.
            current_cell: The cell to start from.
        """
        self.kill(maze, current_cell)

        while unvisited_cell := self.get_unvis_cell_with_vis_neighbour(maze):
            next_cell = unvisited_cell

            visited_neighbours = maze.get_visited_neighbours(next_cell)

            current_cell = self._random.choice(visited_neighbours)

            self.carve_path(current_cell, next_cell)

            self.kill(maze, next_cell)

    def generate_maze(self, maze: Maze, perfect: bool = True) -> None:
        """Generate a maze using the Hunt and Kill algorithm.

        Args:
            maze: The maze to generate.
        """
        while unvisited_cells := maze.get_unvisited_cells():
            current_cell = self._random.choice(unvisited_cells)

            self.hunt_and_kill(maze, current_cell)
