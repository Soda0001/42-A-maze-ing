"""Terminal renderer: draws the maze with coloured blocks (ANSI colours)."""

from entities.cell import Cell
from entities.maze import Maze


RESET = "\033[0m"

WALL_COLORS = [250, 214, 46, 51, 201, 33]
ENTRY_COLOR = 13
EXIT_COLOR = 196
PATH_COLOR = 45
PATTERN_COLOR = 244

# Letter -> (row change, column change)
STEP = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

MENU = (
    "=== A-Maze-ing ===\n"
    "1. Re-generate a new maze\n"
    "2. Show / Hide the shortest path\n"
    "3. Rotate the wall colours\n"
    "4. Quit\n"
    "Choice? (1-4): "
)


def block(color: int | None) -> str:
    """Return one square block (2 characters wide)."""
    if color is None:
        return "  "
    return f"\033[48;5;{color}m  {RESET}"


def _closed_count(cell: Cell) -> int:
    """Count how many walls of a cell are closed."""
    return (
        cell.get_north()
        + cell.get_east()
        + cell.get_south()
        + cell.get_west()
    )


def build_tiles(
    maze: Maze,
    wall_color: int,
    path: str,
    show_path: bool,
) -> list[list[int | None]]:
    """Build the tile grid used to render the maze."""
    cells = maze.get_cells()

    rows = len(cells)
    cols = len(cells[0]) if rows > 0 else 0

    tiles: list[list[int | None]] = [
        [wall_color] * (2 * cols + 1)
        for _ in range(2 * rows + 1)
    ]

    pattern: set[tuple[int, int]] = set()

    for row in range(rows):
        for column in range(cols):
            cell = cells[row][column]

            tile_row = 2 * row + 1
            tile_column = 2 * column + 1

            if _closed_count(cell) == 4:
                pattern.add((row, column))
                tiles[tile_row][tile_column] = PATTERN_COLOR
                continue

            tiles[tile_row][tile_column] = None

            if not cell.get_north():
                tiles[tile_row - 1][tile_column] = None

            if not cell.get_east():
                tiles[tile_row][tile_column + 1] = None

            if not cell.get_south():
                tiles[tile_row + 1][tile_column] = None

            if not cell.get_west():
                tiles[tile_row][tile_column - 1] = None

    # Join neighbouring restricted cells so the 42 pattern looks solid.
    for row, column in pattern:
        if (row, column + 1) in pattern:
            tiles[2 * row + 1][2 * column + 2] = PATTERN_COLOR

        if (row + 1, column) in pattern:
            tiles[2 * row + 2][2 * column + 1] = PATTERN_COLOR

    # Entry and exit are stored as (x, y) = (column, row).
    entry_x, entry_y = maze.get_entry()
    exit_x, exit_y = maze.get_exit()

    if show_path and path:
        row = entry_y
        column = entry_x

        if (
            0 <= row < rows
            and 0 <= column < cols
        ):
            tiles[2 * row + 1][2 * column + 1] = PATH_COLOR

        for letter in path:
            if letter not in STEP:
                break

            dr, dc = STEP[letter]

            next_row = row + dr
            next_column = column + dc

            if not (
                0 <= next_row < rows
                and 0 <= next_column < cols
            ):
                break

            tiles[
                2 * row + 1 + dr
            ][
                2 * column + 1 + dc
            ] = PATH_COLOR

            row = next_row
            column = next_column

            tiles[2 * row + 1][2 * column + 1] = PATH_COLOR

    # Draw entry and exit only when their coordinates are valid.
    if (
        0 <= entry_y < rows
        and 0 <= entry_x < cols
    ):
        tiles[2 * entry_y + 1][2 * entry_x + 1] = ENTRY_COLOR

    if (
        0 <= exit_y < rows
        and 0 <= exit_x < cols
    ):
        tiles[2 * exit_y + 1][2 * exit_x + 1] = EXIT_COLOR

    return tiles


def render(
    maze: Maze,
    path: str = "",
    show_path: bool = False,
    color_index: int = 0,
) -> str:
    """Return the whole maze as one printable string."""
    wall_color = WALL_COLORS[color_index % len(WALL_COLORS)]

    tiles = build_tiles(
        maze,
        wall_color,
        path,
        show_path,
    )

    return "\n".join(
        "".join(block(tile) for tile in row)
        for row in tiles
    )
