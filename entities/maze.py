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

        for y in range(row):
            cell_row = []

            for x in range(column):
                cell = Cell(y, x)
                cell_row.append(cell)

            self._cells.append(cell_row)

    def get_row(self):
        return self._row

    def get_all_neighbours(self, cell: Cell) -> list[Cell]:
        neighbours = []
        row = cell.get_row()
        column = cell.get_column()

        if row > 0:
            neighbours.append(self._cells[row - 1][column])

        if row < self._row - 1:
            neighbours.append(self._cells[row + 1][column])

        if column > 0:
            neighbours.append(self._cells[row][column - 1])

        if column < self._column - 1:
            neighbours.append(self._cells[row][column + 1])

        return neighbours

    def get_unvisited_neighbours(self, all_neighbours: list) -> list[Cell]:
        unvisited_neighbours = []

        for neighbour in all_neighbours:
            if not neighbour.is_visited:
                unvisited_neighbours.append(neighbour)

        return unvisited_neighbours
