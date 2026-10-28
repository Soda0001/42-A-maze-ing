from .cell import Cell


class Maze:
    """Represent the maze grid containing cells, entry, and exit points."""

    def __init__(
        self,
        row: int,
        column: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
    ) -> None:
        """Initialize the maze with dimensions, entry, exit, and cell grid."""
        self._row = row
        self._column = column
        self._entry = entry
        self._exit = exit
        self._cells: list[list[Cell]] = []

        for row_index in range(row):
            cell_row = []

            for column_index in range(column):
                cell = Cell(row_index, column_index)
                cell_row.append(cell)

            self._cells.append(cell_row)
        self.mark_restricted_cells()

        self.validate_enter()
        self.validate_exit()

    def get_row(self) -> int:
        """Return the number of rows in the maze."""
        return self._row

    def set_row(self, row: int) -> None:
        """Set the number of rows in the maze."""
        self._row = row

    def get_column(self) -> int:
        """Return the number of columns in the maze."""
        return self._column

    def set_column(self, column: int) -> None:
        """Set the number of columns in the maze."""
        self._column = column

    def get_entry(self) -> tuple[int, int]:
        """Return the entry coordinates of the maze."""
        return self._entry

    def set_entry(self, entry: tuple[int, int]) -> None:
        """Set the entry coordinates of the maze."""
        self._entry = entry

    def get_exit(self) -> tuple[int, int]:
        """Return the exit coordinates of the maze."""
        return self._exit

    def set_exit(self, exit: tuple[int, int]) -> None:
        """Set the exit coordinates of the maze."""
        self._exit = exit

    def get_cells(self) -> list[list[Cell]]:
        """Return the 2D grid of cells composing the maze."""
        return self._cells

    def set_cells(self, cells: list[list[Cell]]) -> None:
        """Set the 2D grid of cells for the maze."""
        self._cells = cells

    def get_all_neighbours(self, cell: Cell) -> list[Cell]:
        """Return all adjacent valid neighboring cells."""
        neighbours = []
        row = cell.get_row()
        column = cell.get_column()

        if row > 0:
            neighbours.append(self.get_cells()[row - 1][column])

        if row < self.get_row() - 1:
            neighbours.append(self.get_cells()[row + 1][column])

        if column > 0:
            neighbours.append(self.get_cells()[row][column - 1])

        if column < self.get_column() - 1:
            neighbours.append(self.get_cells()[row][column + 1])

        return neighbours

    def get_unvisited_neighbours(
        self,
        cell: Cell,
    ) -> list[Cell]:
        """Return all unvisited and unrestricted neighboring cells."""
        unvisited_neighbours = []

        neighbours = self.get_all_neighbours(cell)

        for neighbour in neighbours:
            if not neighbour.is_visited() and not neighbour.is_restricted():
                unvisited_neighbours.append(neighbour)

        return unvisited_neighbours

    def get_visited_neighbours(
        self,
        cell: Cell,
    ) -> list[Cell]:
        """Return all visited neighboring cells."""
        visited_neighbours = []

        neighbours = self.get_all_neighbours(cell)

        for neighbour in neighbours:
            if neighbour.is_visited():
                visited_neighbours.append(neighbour)

        return visited_neighbours

    def get_unvisited_cells(self) -> list[Cell]:
        """Return a list of all unvisited and
        unrestricted cells in the maze."""
        unvisited_cells = []

        for row in self.get_cells():
            for cell in row:
                if not cell.is_visited() and not cell.is_restricted():
                    unvisited_cells.append(cell)

        return unvisited_cells

    def get_unvisited_cell_count(self) -> int:
        """Return the number of unvisited cells."""
        count = 0

        for row in self.get_cells():
            for cell in row:
                if not cell.is_visited() and not cell.is_restricted():
                    count += 1

        return count

    def get_representation(self) -> str:
        """Return the maze representation as a string."""
        representation = ""

        for row in self.get_cells():
            for cell in row:
                representation += cell.get_representation()
            representation += "\n"

        return representation

    def write_to_file(self, filename: str) -> None:
        """Write the maze and its entry and exit to a file."""
        with open(filename, "w", encoding="utf-8") as file:
            for row in self.get_cells():
                for cell in row:
                    file.write(cell.get_representation())
                file.write("\n")

            entry_row, entry_column = self.get_entry()
            exit_row, exit_column = self.get_exit()

            file.write(f"\n{entry_column},{entry_row} #entry (x,y)\n")
            file.write(f"{exit_column},{exit_row}  #exit (x,y)\n")

    def is_42pattern_eligible(self) -> bool:
        """Check if maze dimensions are large enough for the '42' pattern."""
        if self.get_row() < 7 or self.get_column() < 9:
            print("\n***** Too small to have '42' pattern *****\n")
            return False
        else:
            return True

    def get_mid_left_corner_coor(self) -> tuple[int, int]:
        """Return the top-left coordinate for the center '42' pattern."""
        pattern_height = 5
        pattern_width = 7

        mid_row = (self.get_row() - pattern_height) // 2
        mid_column = (self.get_column() - pattern_width) // 2

        return mid_row, mid_column

    def mark_restricted_cells(self) -> None:
        """Mark cells belonging to the central '42' pattern as restricted."""
        if not self.is_42pattern_eligible():
            return

        mid_row, mid_column = self.get_mid_left_corner_coor()
        cells = self.get_cells()

        pattern = (
            "1000111",
            "1000001",
            "1110111",
            "0010100",
            "0010111",
        )

        for row_offset, pattern_row in enumerate(pattern):
            for column_offset, marked in enumerate(pattern_row):
                if marked == "1":
                    cells[mid_row + row_offset][
                        mid_column + column_offset
                    ].set_is_restricted()

    def get_restricted_cells(self) -> list[Cell]:
        """Return all restricted cells in the maze."""
        restricted_cells: list[Cell] = []

        for row in self.get_cells():
            for cell in row:
                if cell.is_restricted():
                    restricted_cells.append(cell)

        return restricted_cells

    def validate_enter(self) -> None:
        """Validate entry coordinates are within bounds and not restricted."""
        entry_row_index, entry_column_index = self.get_entry()

        if entry_row_index < 0 or entry_row_index >= self.get_row():
            raise IndexError("Entry must be inside of boundries of the maze")

        if entry_column_index < 0 or entry_column_index >= self.get_column():
            raise IndexError("Entry must be inside of boundries of the maze")

        entry_cell = self.get_cells()[entry_row_index][entry_column_index]

        if entry_cell.is_restricted():
            raise ValueError("Entry must be outside of '42' pattern")

    def validate_exit(self) -> None:
        """Validate exit coordinates are valid, unrestricted, and distinct."""
        exit_row_index, exit_column_index = self.get_exit()

        if exit_row_index < 0 or exit_row_index >= self.get_row():
            raise IndexError("Exit must be inside of boundries of the maze")

        if exit_column_index < 0 or exit_column_index >= self.get_column():
            raise IndexError("Exit must be inside of boundries of the maze")

        if self.get_cells()[exit_row_index][exit_column_index].is_restricted():
            raise ValueError("Exit must be outside of '42' pattern")

        exit_cell = self.get_cells()[exit_row_index][exit_column_index]

        entry_row_index, entry_column_index = self.get_entry()
        entry_cell = self.get_cells()[entry_row_index][entry_column_index]

        if exit_cell == entry_cell:
            raise ValueError("Entry and exit cannot be the same cell")
