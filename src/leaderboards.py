class Leaderboard:
    def __init__(self):
        self.entries = []

    def add_entry(self, username, puzzles_solved, time_spent):
        self.entries.append({
            'username': username,
            'puzzles_solved': puzzles_solved,
            'time_spent': time_spent
        })
        self.entries = sorted(self.entries, key=lambda x: (-x['puzzles_solved'], x['time_spent']))

    def get_top_entries(self, top_n=10):
        return self.entries[:top_n]

from advanced_board import AdvancedBoard
from backtracking_solver import BacktrackingSolver
from user_profile import UserProfile
from leaderboard import Leaderboard

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