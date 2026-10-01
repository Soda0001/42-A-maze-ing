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
    