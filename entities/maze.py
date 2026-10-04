from .cell import Cell


class Maze:
    def __init__(
            self,
            row: int,
            column: int,
            entry: tuple[int, int],
            exit: tuple[int, int],
    ):
        self._row = row
        self._column = column
        self._entry = entry
        self._exit = exit
        self._cells = []

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
        return self._row

    def set_row(self, row: int) -> None:
        self._row = row

    def get_column(self) -> int:
        return self._column

    def set_column(self, column: int) -> None:
        self._column = column

    def get_entry(self) -> tuple[int, int]:
        return self._entry

    def set_entry(self, entry: tuple[int, int]) -> None:
        self._entry = entry

    def get_exit(self) -> tuple[int, int]:
        return self._exit

    def set_exit(self, exit: tuple[int, int]) -> None:
        self._exit = exit

    def get_cells(self) -> list[list[Cell]]:
        return self._cells

    def set_cells(self, cells: list[list[Cell]]) -> None:
        self._cells = cells

    def get_all_neighbours(self, cell: Cell) -> list[Cell]:
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
            all_neighbours: list[Cell]
    ) -> list[Cell]:

        unvisited_neighbours = []
        for neighbour in all_neighbours:
            if not neighbour.is_visited() and not neighbour.is_restricted():
                unvisited_neighbours.append(neighbour)

        return unvisited_neighbours

    def get_unvisited_cell_count(self) -> int:
        """Return the number of unvisited cells."""
        count = 0

        for row in self.get_cells():
            for cell in row:
                if not cell.is_visited():
                    count += 1

        return count

    def get_visited_neighbours(
            self,
            all_neighbours: list[Cell]
    ) -> list[Cell]:

        visited_neighbours = []
        for neighbour in all_neighbours:
            if neighbour.is_visited() and not neighbour.is_restricted():
                visited_neighbours.append(neighbour)

        return visited_neighbours

    def get_representation(self) -> str:
        """Return the maze representation as a string."""
        representation = ""

        for row in self._cells:
            for cell in row:
                representation += cell.get_representation()
            representation += "\n"

        return representation

    def write_to_file(self, filename: str) -> None:
        """Write the maze and its entry and exit to a file."""
        with open(filename, "w") as file:
            for row in self.get_cells():
                for cell in row:
                    file.write(cell.get_representation())
                file.write("\n")

            entry_row, entry_column = self.get_entry()
            exit_row, exit_column = self.get_exit()

            file.write(f"\n{entry_row},{entry_column}\n")
            file.write(f"{exit_row},{exit_column}\n")

    def is_42pattern_eligible(self) -> bool:

        if self.get_row() < 5 or self.get_column() < 7:
            print("Too small to have '42' pattern")
            return False
        else:
            return True

    def get_mid_left_corner_coor(self) -> tuple[int, int]:
        pattern_height = 5
        pattern_width = 7

        mid_row = (self.get_row() - pattern_height) // 2
        mid_column = (self.get_column() - pattern_width) // 2

        return mid_row, mid_column

    def mark_restricted_cells(self) -> None:
        if not self.is_42pattern_eligible():
            return

        mid_row, mid_column = self.get_mid_left_corner_coor()
        cells = self.get_cells()

        cells[mid_row][mid_column].set_is_restricted(True)
        cells[mid_row + 1][mid_column].set_is_restricted(True)
        cells[mid_row + 2][mid_column].set_is_restricted(True)
        cells[mid_row + 2][mid_column + 1].set_is_restricted(True)
        cells[mid_row + 2][mid_column + 2].set_is_restricted(True)
        cells[mid_row + 3][mid_column + 2].set_is_restricted(True)
        cells[mid_row + 4][mid_column + 2].set_is_restricted(True)

        cells[mid_row][mid_column + 4].set_is_restricted(True)
        cells[mid_row][mid_column + 5].set_is_restricted(True)
        cells[mid_row][mid_column + 6].set_is_restricted(True)
        cells[mid_row + 1][mid_column + 6].set_is_restricted(True)
        cells[mid_row + 2][mid_column + 4].set_is_restricted(True)
        cells[mid_row + 2][mid_column + 5].set_is_restricted(True)
        cells[mid_row + 2][mid_column + 6].set_is_restricted(True)
        cells[mid_row + 3][mid_column + 4].set_is_restricted(True)
        cells[mid_row + 4][mid_column + 4].set_is_restricted(True)
        cells[mid_row + 4][mid_column + 5].set_is_restricted(True)
        cells[mid_row + 4][mid_column + 6].set_is_restricted(True)

    def get_restricted_cells(self) -> list[Cell]:
        """Return all restricted cells in the maze."""
        restricted_cells: list[Cell] = []

        for row in self.get_cells():
            for cell in row:
                if cell.is_restricted():
                    restricted_cells.append(cell)

        return restricted_cells

    def validate_enter(self) -> None:
        entry_row_index, entry_column_index = self.get_entry()

        if entry_row_index < 0 or entry_row_index >= self.get_row():
            raise IndexError("Entry must be inside of boundries of the maze")

        if entry_column_index < 0 or entry_column_index >= self.get_column():
            raise IndexError("Entry must be inside of boundries of the maze")

        entry_cell = self.get_cells()[entry_row_index][entry_column_index]

        if entry_cell.is_restricted():
            raise ValueError("Entry must be outside of '42' pattern")

    def validate_exit(self) -> None:
        exit_row_index, exit_column_index = self.get_exit()

        if exit_row_index < 0 or exit_row_index >= self.get_row():
            raise IndexError("Exit must be inside of boundries of the maze")

        if exit_column_index < 0 or exit_column_index >= self.get_column():
            raise IndexError("Exit must be inside of boundries of the maze")

        if self.get_cells()[exit_row_index][exit_column_index].is_restricted():
            raise ValueError("Exit must be outside of '42' pattern")
