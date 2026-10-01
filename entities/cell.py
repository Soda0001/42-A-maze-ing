class Cell:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._w = True
        self._s = True
        self._e = True
        self._n = True
        self._is_visited = False

    def get_x(self) -> int:
        return self._x

    def set_x(self, x: int) -> None:
        self._x = x

    def get_y(self) -> int:
        return self._y

    def set_y(self, y: int) -> None:
        self._y = y

    def get_w(self) -> bool:
        return self._w

    def set_w(self, w: bool) -> None:
        self._w = w

    def get_s(self) -> bool:
        return self._s

    def set_s(self, s: bool) -> None:
        self._s = s

    def get_e(self) -> bool:
        return self._e

    def set_e(self, e: bool) -> None:
        self._e = e

    def get_n(self) -> bool:
        return self._n

    def set_n(self, n: bool) -> None:
        self._n = n

    def is_visited(self) -> bool:
        return self._is_visited

    def set_is_visited(self, is_visited: bool) -> None:
        self._is_visited = is_visited
