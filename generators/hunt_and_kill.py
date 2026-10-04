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

        if current_row == next_row - 1:
            current_cell.set_south(False)
            next_cell.set_north(False)

        elif current_row == next_row + 1:
            current_cell.set_north(False)
            next_cell.set_south(False)

        elif current_column == next_column - 1:
            current_cell.set_east(False)
            next_cell.set_west(False)

        elif current_column == next_column + 1:
            current_cell.set_west(False)
            next_cell.set_east(False)

        current_cell.set_is_visited(True)
        next_cell.set_is_visited(True)

        current_cell.represent()
        next_cell.represent()

    def get_unvis_cell_with_vis_neighbour(
            self,
            maze: Maze,
            look_at: tuple[int, int] = (0, 0)
    ) -> Cell | None:
        """Find an unvisited cell with a visited neighbour.

        Args:
            maze: The maze to search.
            look_at: The row and column from which to start the search.

        Returns:
            An unvisited cell with a visited neighbour, or None if no
            suitable cell is found.
        """
        rows = maze.get_cells()

        for row in range(look_at[0], len(rows)):
            for column in range(look_at[1], len(rows[row])):
                current_cell = maze.get_cells()[row][column]

                if current_cell.is_visited() or current_cell._is_restricted():
                    continue

                neighbours = maze.get_all_neighbours(current_cell)
                visited_neighbours = maze.get_visited_neighbours(neighbours)

                if visited_neighbours:
                    return current_cell

        return None

    def generate_maze(self, maze: Maze) -> None:
        """Generate a maze using the Hunt and Kill algorithm.

        Args:
            maze: The maze to generate.
        """
        entry_row, entry_column = maze.get_entry()
        entry_cell = maze.get_cells()[entry_row][entry_column]
        entry_cell.set_is_visited(True)

        while True:
            if maze.get_unvisited_cell_count() == 18:
                break
            
            unvisited_cell = self.get_unvis_cell_with_vis_neighbour(maze)

            all_neighbours = maze.get_all_neighbours(unvisited_cell)
            visited_neighbours = maze.get_visited_neighbours(all_neighbours)

            visited_neighbour = self._random.choice(visited_neighbours)
            self.carve_path(visited_neighbour, unvisited_cell)

            current_cell = unvisited_cell

            while True:
                all_neighbours = maze.get_all_neighbours(current_cell)
                unvisited_neighbours = maze.get_unvisited_neighbours(
                    all_neighbours
                )

                if not unvisited_neighbours:
                    break

                next_cell = self._random.choice(unvisited_neighbours)
                self.carve_path(current_cell, next_cell)

                current_cell = next_cell
