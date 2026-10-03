"""Terminal renderer: draws the maze with coloured blocks (ANSI colours)."""

from entities.cell import Cell
from entities.maze import Maze

RESET = "\033[0m"  # "stop colouring" code

# Colour numbers of the 256-colour palette. Change them freely.
WALL_COLORS = [250, 214, 46, 51, 201, 33]  # menu option 3 cycles these
ENTRY_COLOR = 13   # pink
EXIT_COLOR = 196   # red
PATH_COLOR = 45    # cyan
PATTERN_COLOR = 244  # grey, used for the "42"

# letter -> (row change, column change)
STEP = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

MENU = (
    "=== A-Maze-ing ===\n"
    "1. Re-generate a new maze\n"
    "2. Show / Hide the shortest path\n"
    "3. Rotate the wall colours\n"
    "4. Quit\n"
    "Choice? (1-4): "
)


def block(color: int | None) -> str:
    """Return one square block (2 characters wide).

    A colour number gives a coloured block, None gives an empty corridor.
    """
    if color is None:
        return "  "
    return f"\033[48;5;{color}m  {RESET}"


def _closed_count(cell: Cell) -> int:
    """Count how many walls of a cell are closed."""
    return (cell.get_north() + cell.get_east()
            + cell.get_south() + cell.get_west())


def build_tiles(
    maze: Maze, wall_color: int, path: str, show_path: bool
) -> list[list[int | None]]:
    """Build the drawing grid of (2*rows+1) x (2*columns+1) tiles.

    Cell (r, c) sits at tile (2r+1, 2c+1); the tiles between two cells are
    the walls. Every tile holds a colour number, or None for a free corridor.
    """
    rows, cols = maze.get_row(), maze.get_column()
    cells = maze.get_cells()
    # start with everything as wall, then open what is open
    tiles: list[list[int | None]] = [
        [wall_color] * (2 * cols + 1) for _ in range(2 * rows + 1)
    ]
    pattern: set[tuple[int, int]] = set()

    for r in range(rows):
        for c in range(cols):
            cell = cells[r][c]
            tr, tc = 2 * r + 1, 2 * c + 1
            if _closed_count(cell) == 4:  # fully closed cell = the "42"
                pattern.add((r, c))
                tiles[tr][tc] = PATTERN_COLOR
                continue
            tiles[tr][tc] = None
            if not cell.get_north():
                tiles[tr - 1][tc] = None
            if not cell.get_east():
                tiles[tr][tc + 1] = None
            if not cell.get_south():
                tiles[tr + 1][tc] = None
            if not cell.get_west():
                tiles[tr][tc - 1] = None

    # join neighbouring "42" cells so the digits look solid
    for r, c in pattern:
        if (r, c + 1) in pattern:
            tiles[2 * r + 1][2 * c + 2] = PATTERN_COLOR
        if (r + 1, c) in pattern:
            tiles[2 * r + 2][2 * c + 1] = PATTERN_COLOR

    # entry / exit are (x, y) = (column, row)
    entry_x, entry_y = maze.get_entry()
    exit_x, exit_y = maze.get_exit()

    if show_path and path:
        r, c = entry_y, entry_x
        tiles[2 * r + 1][2 * c + 1] = PATH_COLOR
        for letter in path:
            if letter not in STEP:
                break
            dr, dc = STEP[letter]
            tiles[2 * r + 1 + dr][2 * c + 1 + dc] = PATH_COLOR
            r, c = r + dr, c + dc
            tiles[2 * r + 1][2 * c + 1] = PATH_COLOR

    tiles[2 * entry_y + 1][2 * entry_x + 1] = ENTRY_COLOR
    tiles[2 * exit_y + 1][2 * exit_x + 1] = EXIT_COLOR
    return tiles


def render(
    maze: Maze, path: str = "", show_path: bool = False, color_index: int = 0
) -> str:
    """Return the whole maze as one printable string."""
    wall_color = WALL_COLORS[color_index % len(WALL_COLORS)]
    tiles = build_tiles(maze, wall_color, path, show_path)
    return "\n".join("".join(block(t) for t in row) for row in tiles)