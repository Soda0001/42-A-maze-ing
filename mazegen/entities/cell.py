class Cell:
    def __init__(self, row: int, column: int):
        self._row = row
        self._column = column
        self._west = True
        self._south = True
        self._east = True
        self._north = True
        self._is_visited = False

    def get_row(self) -> int:
        return self._row

    def set_row(self, row: int) -> None:
        self._row = row

    def get_column(self) -> int:
        return self._column

    def set_column(self, column: int) -> None:
        self._column = column

    def get_west(self) -> bool:
        return self._west

    def set_west(self, west: bool) -> None:
        self._west = west

    def get_south(self) -> bool:
        return self._south

    def set_south(self, south: bool) -> None:
        self._south = south

    def get_east(self) -> bool:
        return self._east

    def set_east(self, east: bool) -> None:
        self._east = east

    def get_north(self) -> bool:
        return self._north

    def set_north(self, north: bool) -> None:
        self._north = north

    def is_visited(self) -> bool:
        return self._is_visited

    def set_is_visited(self, is_visited: bool) -> None:
        self._is_visited = is_visited

    def get_coordinates(self) -> tuple[int, int]:
        return self.get_row(), self.get_column()
