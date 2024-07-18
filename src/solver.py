class Solver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        empty_spot = self._find_empty()
        if not empty_spot:
            return True
        row, col = empty_spot

        for num in range(1, 10):
            if self._is_valid(num, row, col):
                self.board.grid[row][col] = num
                if self.solve():
                    return True
                self.board.grid[row][col] = 0

        return False

    def _find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board.grid[i][j] == 0:
                    return (i, j)
        return None

    def _is_valid(self, num, row, col):
        for i in range(9):
            if self.board.grid[row][i] == num or self.board.grid[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board.grid[i][j] == num:
                    return False

        return True
    
    def is_solved(self):
        for row in range(9):
            for col in range(9):
                if self.board.grid[row][col] == 0:
                    return False
                if not self.is_valid(self.board.grid[row][col], (row, col)):
                    return False
        return True
