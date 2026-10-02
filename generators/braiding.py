from entities.maze import Maze


def find_dead_ends(maze: Maze) -> list[tuple[int, int ]]:
    """Return the coordinates of every dead-end cell (exactly 3 closed walls)."""
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
