class AdvancedBoard:
    def __init__(self, difficulty='medium'):
        self.difficulty = difficulty
        self.board = self.create_empty_board()

    def create_empty_board(self):
        return [[0 for _ in range(9)] for _ in range(9)]

    def fill_board(self):
        if self.difficulty == 'easy':
            self.board = self.generate_easy_board()
        elif self.difficulty == 'medium':
            self.board = self.generate_medium_board()
        elif self.difficulty == 'hard':
            self.board = self.generate_hard_board()

    def generate_easy_board(self):
        board = self.create_empty_board()
        self.fill_diagonal_boxes(board)
        self.fill_remaining_cells(board)
        self.remove_numbers_from_board(board, 30)  # Remove 30 numbers for easy difficulty
        return board
    
    def generate_medium_board(self):
        board = self.create_empty_board()
        self.fill_diagonal_boxes(board)
        self.fill_remaining_cells(board)
        self.remove_numbers_from_board(board, 40)  # Remove 40 numbers for medium difficulty
        return board
    
    def generate_hard_board(self):
        board = self.create_empty_board()
        self.fill_diagonal_boxes(board)
        self.fill_remaining_cells(board)
        self.remove_numbers_from_board(board, 50)  # Remove 50 numbers for hard difficulty
        return board

    def create_and_validate_board(difficulty):
        board = create_advanced_board(difficulty)
        advanced_board = AdvancedBoard(difficulty)
        advanced_board.fill_board()
        if advanced_board.is_solvable():
            return advanced_board.board
        else:
            return create_and_validate_board(difficulty)

    def is_solvable(self):
        temp_board = [row[:] for row in self.board]
        return self.solve_sudoku(temp_board)
    
    def fill_diagonal_boxes(self, board):
        for i in range(0, 9, 3):
            self.fill_3x3_box(board, i, i)

    def fill_3x3_box(self, board, row, col):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                board[row + i][col + j] = nums.pop()

    def fill_remaining_cells(self, board):
        self.solve_sudoku(board)

    def solve_sudoku(self, board):
        empty = self.find_empty_location(board)
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if self.is_safe(board, row, col, num):
                board[row][col] = num
                if self.solve_sudoku(board):
                    return True
                board[row][col] = 0
        return False

    def find_empty_location(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def is_safe(self, board, row, col, num):
        return self.not_in_row(board, row, num) and \
               self.not_in_col(board, col, num) and \
               self.not_in_box(board, row - row % 3, col - col % 3, num)

    def not_in_row(self, board, row, num):
        return num not in board[row]

    def not_in_col(self, board, col, num):
        return num not in [board[row][col] for row in range(9)]

    def not_in_box(self, board, box_start_row, box_start_col, num):
        for i in range(3):
            for j in range(3):
                if board[box_start_row + i][box_start_col + j] == num:
                    return False
        return True

    def remove_numbers_from_board(self, board, count):
        while count > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while board[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            board[row][col] = 0
            count -= 1

def create_advanced_board(difficulty):
    board = AdvancedBoard(difficulty)
    board.fill_board()
    return board.board

easy_board = create_advanced_board('easy')