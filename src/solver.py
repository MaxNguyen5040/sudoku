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

    def is_valid(self, num, pos):
        for col in range(9):
            if self.board.grid[pos[0]][col] == num and pos[1] != col:
                return False

        for row in range(9):
            if self.board.grid[row][pos[1]] == num and pos[0] != row:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board.grid[i][j] == num and (i, j) != pos:
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
