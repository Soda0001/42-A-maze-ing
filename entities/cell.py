class Cell:
    """Represent an individual cell in the maze."""

    def __init__(self, row: int, column: int) -> None:
        """Initialize a cell with coordinates and default walls/states."""
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
        """Return the row index of the cell."""
        return self._row

    def set_row(self, row: int) -> None:
        """Set the row index of the cell."""
        self._row = row

    def get_column(self) -> int:
        """Return the column index of the cell."""
        return self._column

    def set_column(self, column: int) -> None:
        """Set the column index of the cell."""
        self._column = column

    def get_west(self) -> bool:
        """Return the state of the west wall."""
        return self._west

    def set_west(self, west: bool = False) -> None:
        """Set the state of the west wall."""
        self._west = west

    def get_south(self) -> bool:
        """Return the state of the south wall."""
        return self._south

    def set_south(self, south: bool = False) -> None:
        """Set the state of the south wall."""
        self._south = south

    def get_east(self) -> bool:
        """Return the state of the east wall."""
        return self._east

    def set_east(self, east: bool = False) -> None:
        """Set the state of the east wall."""
        self._east = east

    def get_north(self) -> bool:
        """Return the state of the north wall."""
        return self._north

    def set_north(self, north: bool = False) -> None:
        """Set the state of the north wall."""
        self._north = north

    def is_visited(self) -> bool:
        """Return whether the cell has been visited."""
        return self._is_visited

    def set_is_visited(self, is_visited: bool) -> None:
        """Set the visited status of the cell."""
        self._is_visited = is_visited

    def get_coordinates(self) -> tuple[int, int]:
        """Return the (row, column) coordinates of the cell."""
        return self.get_row(), self.get_column()

    def get_representation(self) -> str:
        """Return the string representation character of the cell."""
        return self._representation

    def set_representation(self, representation: str) -> None:
        """Set the string representation character of the cell."""
        self._representation = representation

    def is_restricted(self) -> bool:
        """Return whether the cell is restricted."""
        return self._is_restricted

    def set_is_restricted(self, restriction: bool = True) -> None:
        """Set the restricted status of the cell."""
        self._is_restricted = restriction

    def get_bits(self) -> tuple[int, int, int, int]:
        """Return integer values of west, south, east, and north walls."""
        west = self.get_west()
        south = self.get_south()
        east = self.get_east()
        north = self.get_north()

        bits = int(west), int(south), int(east), int(north)
        return bits

    def get_open_walls(self) -> list[int]:
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
