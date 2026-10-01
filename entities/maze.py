from cell import Cell


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
            neighbours.append(self._cells[row - 1][column])

        if row < self.get_row() - 1:
            neighbours.append(self._cells[row + 1][column])

        if column > 0:
            neighbours.append(self._cells[row][column - 1])

        if column < self.get_column() - 1:
            neighbours.append(self._cells[row][column + 1])

        return neighbours

    def get_unvisited_neighbours(
            self,
            all_neighbours: list[Cell]
    ) -> list[Cell]:
        unvisited_neighbours = []

        for neighbour in all_neighbours:
            if not neighbour.is_visited():
                unvisited_neighbours.append(neighbour)

        return unvisited_neighbours