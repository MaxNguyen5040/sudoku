import datetime
import random

class DailyChallenge:
    def __init__(self):
        self.daily_puzzles = {}

    def generate_daily_puzzle(self, difficulty):
        date_key = datetime.date.today().isoformat()
        if date_key not in self.daily_puzzles:
            board = self.create_and_validate_board(difficulty)
            self.daily_puzzles[date_key] = board
        return self.daily_puzzles[date_key]

    def create_and_validate_board(self, difficulty):
        advanced_board = AdvancedBoard(difficulty)
        advanced_board.fill_board()
        if advanced_board.is_solvable():
            return advanced_board.board
        else:
            return self.create_and_validate_board(difficulty)

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

daily_challenge = DailyChallenge()
puzzle = daily_challenge.generate_daily_puzzle('medium')
print("Today's Daily Challenge Puzzle:", puzzle)
