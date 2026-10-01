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

    def get_neighbours(self, cell: Cell) -> list:
        neighbours = []

        if cell.get_y() > 0:
            neighbours.append((cell.get_x(), cell.get_y() + 1))

        if cell.get_y() < self.get_row() - 1:
            neighbours.append((cell.get_x(), cell.get_y() - 1))

        if cell.get_x() > 0:
                    neighbours.append((cell.get_x() - 1, cell.get_y()))
        
        if cell.get_x() < self.get_row() - 1:
            neighbours.append((cell.get_x() + 1, cell.get_y()))