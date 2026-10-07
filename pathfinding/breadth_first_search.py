from collections import deque

from entities.maze import Maze
from entities.cell import Cell


class BreadthFirstSearch:
    """Find the shortest path in a maze using BFS."""

    def can_move(
            self,
            current_cell: Cell,
            neighbour: Cell
    ) -> bool:
        """Return whether two neighbouring cells are connected."""
        current_row = current_cell.get_row()
        current_column = current_cell.get_column()

        neighbour_row = neighbour.get_row()
        neighbour_column = neighbour.get_column()

        if neighbour_row == current_row - 1:
            return not current_cell.get_north()

        if neighbour_row == current_row + 1:
            return not current_cell.get_south()

        if neighbour_column == current_column - 1:
            return not current_cell.get_west()

        if neighbour_column == current_column + 1:
            return not current_cell.get_east()

        return False

    def path_to_directions(self, path: list[Cell]) -> str:
        """Convert a cell path into movement directions."""
        directions = ""

        for index in range(len(path) - 1):
            current = path[index]
            next_cell = path[index + 1]

            current_row = current.get_row()
            current_column = current.get_column()

            next_row = next_cell.get_row()
            next_column = next_cell.get_column()

            if next_row == current_row - 1:
                directions += "N"
            elif next_column == current_column + 1:
                directions += "E"
            elif next_row == current_row + 1:
                directions += "S"
            elif next_column == current_column - 1:
                directions += "W"

        return directions

    def write_to_file(
            self,
            filename: str,
            path: str = "",
    ) -> None:
        """Write the shortest path to the output file."""
        with open(filename, "a") as file:
            file.write(f"{path}\n")

    def find_shortest_path(
            self,
            maze: Maze
    ) -> list[Cell]:
        """Find and return the shortest path from entry to exit."""
        entry_row, entry_column = maze.get_entry()
        exit_row, exit_column = maze.get_exit()

        start = maze.get_cells()[entry_row][entry_column]
        target = maze.get_cells()[exit_row][exit_column]

        queue = deque([start])
        visited = {start}
        parent: dict[Cell, Cell | None] = {
            start: None
        }

        while queue:
            current = queue.popleft()

            if current == target:
                break

            neighbours = maze.get_all_neighbours(current)

            for neighbour in neighbours:
                if neighbour.is_restricted():
                    continue

                if neighbour in visited:
                    continue

                if not self.can_move(current, neighbour):
                    continue

                visited.add(neighbour)
                parent[neighbour] = current
                queue.append(neighbour)

        if target not in visited:
            return []

        path = []
        current = target

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        return path
