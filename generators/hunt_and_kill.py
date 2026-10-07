import random

from entities.maze import Maze
from entities.cell import Cell
from generators.maze_braider import make_pacman_maze


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

                if current_cell.is_visited() or current_cell.is_restricted():
                    continue

                visited_neighbours = maze.get_visited_neighbours(current_cell)

                if visited_neighbours:
                    return current_cell

        return None

    def kill(self, maze: Maze, current_cell: Cell) -> None:
        """Run the kill phase from the given cell.

        Args:
            maze: The maze to generate.
            current_cell: The cell to start from.
        """
        current_cell.set_is_visited(True)

        while True:
            unvisited_neighbours = maze.get_unvisited_neighbours(current_cell)

            if not unvisited_neighbours:
                break

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

        while True:
            next_cell = self.get_unvis_cell_with_vis_neighbour(maze)

            if not next_cell:
                break

            visited_neighbours = maze.get_visited_neighbours(next_cell)

            current_cell = self._random.choice(visited_neighbours)

            self.carve_path(current_cell, next_cell)

            self.kill(maze, next_cell)

    def generate_maze(self, maze: Maze, perfect: bool = True) -> None:
        """Generate a maze using the Hunt and Kill algorithm.

        Args:
            maze: The maze to generate.
        """
        while True:
            unvisited_cells = maze.get_unvisited_cells()

            if not unvisited_cells:
                break

            current_cell = self._random.choice(unvisited_cells)

            self.hunt_and_kill(maze, current_cell)

        if not perfect:
            make_pacman_maze(maze, self._seed)
