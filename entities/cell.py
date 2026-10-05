class Cell:
    def __init__(self, row: int, column: int):
        self._row = row
        self._column = column
        self._west = True
        self._south = True
        self._east = True
        self._north = True
        self._is_visited = False
        self._representation = "f"
        self._is_restricted = False

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

    def get_representation(self) -> str:
        return self._representation

    def set_representation(self, representation: str) -> None:
        self._representation = representation

    def is_restricted(self) -> int:
        return self._is_restricted

    def set_is_restricted(self, restriction: bool) -> None:
        self._is_restricted = restriction

    def get_bits(self) -> tuple[int, int, int, int]:
        west = self.get_west()
        south = self.get_south()
        east = self.get_east()
        north = self.get_north()

        bits = int(west), int(south), int(east), int(north)
        return bits

    def get_open_walls(self) -> list:
        open_walls = []

        walls = self.get_bits()
        for wall in walls:
            if wall == 0:
                open_walls.append(wall)

        return open_walls

    def represent(self) -> None:
        """Convert wall states into a hexadecimal character."""

        bits = self.get_bits()

        bits_str = f"{bits[0]}{bits[1]}{bits[2]}{bits[3]}"
        value = int(bits_str, 2)
        character = format(value, "x")

        self.set_representation(character)
