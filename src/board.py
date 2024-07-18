class Board:
    def __init__(self, grid):
        self.grid = grid

    def display(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else "." for num in row))

    def is_valid(self):
        return self._rows_valid() and self._cols_valid() and self._squares_valid()

    def _rows_valid(self):
        for row in self.grid:
            if not self._units_valid(row):
                return False
        return True

    def _cols_valid(self):
        for col in zip(*self.grid):
            if not self._units_valid(col):
                return False
        return True

    def _squares_valid(self):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [self.grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self._units_valid(square):
                    return False
        return True

    def _units_valid(self, unit):
        unit = [num for num in unit if num != 0]
        return len(unit) == len(set(unit))
