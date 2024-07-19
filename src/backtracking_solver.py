class BacktrackingSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        empty = self.find_empty_location()
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def find_empty_location(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def is_safe(self, row, col, num):
        return self.not_in_row(row, num) and \
               self.not_in_col(col, num) and \
               self.not_in_box(row - row % 3, col - col % 3, num)

    def not_in_row(self, row, num):
        return num not in self.board[row]

    def not_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(9)]

    def not_in_box(self, box_start_row, box_start_col, num):
        for i in range(3):
            for j in range(3):
                if self.board[box_start_row + i][box_start_col + j] == num:
                    return False
        return True

def create_and_validate_board(difficulty):
    advanced_board = AdvancedBoard(difficulty)
    advanced_board.fill_board()
    if advanced_board.is_solvable():
        return advanced_board.board
    else:
        return create_and_validate_board(difficulty)

def solve_board(board):
    solver = BacktrackingSolver(board)
    return solver.solve()

# Example usage
solvable_easy_board = create_and_validate_board('easy')
solved = solve_board(solvable_easy_board)
print("Solved board:", solvable_easy_board if solved else "No solution found")