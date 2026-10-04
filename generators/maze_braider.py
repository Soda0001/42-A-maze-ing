import random

from entities.cell import Cell
from entities.maze import Maze


def find_dead_ends(maze: Maze) -> list[tuple[int, int]]:
    """Return the coordinates of every dead-end cell."""
    dead_ends: list[tuple[int, int]] = []

    for row in maze.get_cells():
        for cell in row:
            closed = (
                cell.get_north()
                + cell.get_east()
                + cell.get_south()
                + cell.get_west()
            )

            if closed == 3:
                dead_ends.append(cell.get_coordinates())

    return dead_ends


def open_wall(cell: Cell, neighbour: Cell) -> None:
    """Open the wall between two adjacent cells."""
    row = cell.get_row()
    column = cell.get_column()

    neighbour_row = neighbour.get_row()
    neighbour_column = neighbour.get_column()

    if neighbour_row == row - 1:
        cell.set_north(False)
        neighbour.set_south(False)

    elif neighbour_row == row + 1:
        cell.set_south(False)
        neighbour.set_north(False)

    elif neighbour_column == column - 1:
        cell.set_west(False)
        neighbour.set_east(False)

    elif neighbour_column == column + 1:
        cell.set_east(False)
        neighbour.set_west(False)


def get_closed_neighbours(
        maze: Maze,
        cell: Cell
) -> list[Cell]:
    """Return neighbours separated by a closed wall."""
    closed_neighbours: list[Cell] = []

    for neighbour in maze.get_all_neighbours(cell):
        row_diff = neighbour.get_row() - cell.get_row()
        column_diff = neighbour.get_column() - cell.get_column()

        if row_diff == -1 and cell.get_north():
            closed_neighbours.append(neighbour)

        elif row_diff == 1 and cell.get_south():
            closed_neighbours.append(neighbour)

        elif column_diff == -1 and cell.get_west():
            closed_neighbours.append(neighbour)

        elif column_diff == 1 and cell.get_east():
            closed_neighbours.append(neighbour)

    return closed_neighbours


def close_wall(cell: Cell, neighbour: Cell) -> None:
    """Close the wall between two adjacent cells."""
    row = cell.get_row()
    column = cell.get_column()

    neighbour_row = neighbour.get_row()
    neighbour_column = neighbour.get_column()

    if neighbour_row == row - 1:
        cell.set_north(True)
        neighbour.set_south(True)

    elif neighbour_row == row + 1:
        cell.set_south(True)
        neighbour.set_north(True)

    elif neighbour_column == column - 1:
        cell.set_west(True)
        neighbour.set_east(True)

    elif neighbour_column == column + 1:
        cell.set_east(True)
        neighbour.set_west(True)


def would_create_3x3(
        maze: Maze,
        cell: Cell,
        neighbour: Cell
) -> bool:
    """Check if opening the wall creates a 3x3 open area."""
    row = cell.get_row()
    column = cell.get_column()

    open_wall(cell, neighbour)

    for start_row in range(row - 2, row + 1):
        for start_column in range(column - 2, column + 1):

            if start_row < 0 or start_column < 0:
                continue

            if start_row + 2 >= maze.get_row():
                continue

            if start_column + 2 >= maze.get_column():
                continue

            open_area = True

            for r in range(start_row, start_row + 3):
                for c in range(start_column, start_column + 2):
                    if maze.get_cells()[r][c].get_east():
                        open_area = False
                        break

                if not open_area:
                    break

            if not open_area:
                continue

            for r in range(start_row, start_row + 2):
                for c in range(start_column, start_column + 3):
                    if maze.get_cells()[r][c].get_south():
                        open_area = False
                        break

                if not open_area:
                    break

            if open_area:
                close_wall(cell, neighbour)
                return True

    close_wall(cell, neighbour)
    return False


def make_pacman_maze(
        maze: Maze,
        seed: int | None = None
) -> None:
    """Create loops by removing walls from a perfect maze."""
    rng = random.Random(seed)

    dead_ends = find_dead_ends(maze)
    rng.shuffle(dead_ends)

    for coordinates in dead_ends:
        row, column = coordinates
        cell = maze.get_cells()[row][column]

        candidates = get_closed_neighbours(maze, cell)
        rng.shuffle(candidates)

        for neighbour in candidates:
            closed = (
                neighbour.get_north()
                + neighbour.get_east()
                + neighbour.get_south()
                + neighbour.get_west()
            )

            if closed == 4:
                continue

            if would_create_3x3(maze, cell, neighbour):
                continue

            open_wall(cell, neighbour)
            break

    for cells in maze.get_cells():
        for cell in cells:
            cell.represent()
