import random

from entities.maze import Maze
from entities.cell import Cell


class MazeGenerator:
    def __init__(
            self,
            seed: int | None = None
    ):
        self._random = random.Random(seed)

    def carve_path(self, current_cell: Cell, next_cell: Cell) -> None:
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

    def get_unvisited_cell_with_visited_neighbour(
            self,
            maze: Maze,
            look_at: tuple[int, int] = (0, 0)
    ) -> Cell | None:
        
        rows = maze.get_cells()

        for row in range(look_at[0], len(rows)):
            for column in range(look_at[1], len(rows[row])):
                current_cell = maze.get_cells()[row][column]

                if current_cell.is_visited():
                    continue

                all_neighbours = maze.get_all_neighbours(current_cell)
                visited_neighbours = maze.get_visited_neighbours(all_neighbours)
                
                if visited_neighbours:
                    return current_cell

        return None

    def generate_maze(self, maze: Maze):
        """
        HUNT & KILL ALGORITHM

        * start from random cell (in our case entry)
        * visit random unvisited cells
        * after ran out of unvisited cells;
        - start from top left to look for an unvisited cell with visited neighbour
        * do it until all the cells are visited
        * be careful not to visit 42 cells
        """

        entry_row, entry_column = maze.get_entry()

        while True:

            if not maze.get_cells()[entry_row][entry_column].is_visited():
                current_cell = maze.get_cells()[entry_row][entry_column]

            else:
                unvisited_cell = self.get_unvisited_cell_with_visited_neighbour(maze)

                if not unvisited_cell:
                    break

                all_neighbours = maze.get_all_neighbours(unvisited_cell)
                visited_neighbours = maze.get_visited_neighbours(all_neighbours)

                visited_neighbour = self._random.choice(visited_neighbours)
                self.carve_path(visited_neighbour, unvisited_cell)

                current_cell = unvisited_cell

            while True:
                all_neighbours = maze.get_all_neighbours(current_cell)
                unvisited_neighbours = maze.get_unvisited_neighbours(all_neighbours)

                if not unvisited_neighbours:
                    break

                next_cell = self._random.choice(unvisited_neighbours)
                self.carve_path(current_cell, next_cell)

                current_cell = next_cell
