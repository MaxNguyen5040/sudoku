class SudokuEditor:
    def __init__(self, size=9):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def set_value(self, row, col, value):
        if 1 <= value <= self.size:
            self.board[row][col] = value
        else:
            return "Invalid value."

    def save_puzzle(self, filename):
        with open(filename, "w") as file:
            for row in self.board:
                file.write(" ".join(map(str, row)) + "\n")

    def load_puzzle(self, filename):
        with open(filename, "r") as file:
            self.board = [list(map(int, line.split())) for line in file]

# Example usage
editor = SudokuEditor()
editor.set_value(0, 0, 5)
editor.set_value(0, 1, 3)
editor.save_puzzle("custom_puzzle.txt")