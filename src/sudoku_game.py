class SudokuGame:
    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.subgrid_size = int(self.size ** 0.5)

    def provide_hint(self, row, col):
        if self.board[row][col] != 0:
            return "Cell already filled."
        possible_values = self.get_possible_values(row, col)
        if possible_values:
            return f"Try one of these values: {possible_values}"
        return "No possible values found."

    def get_possible_values(self, row, col):
        used_values = set()
        used_values.update(self.board[row])
        used_values.update(self.board[i][col] for i in range(self.size))
        subgrid_row_start = (row // self.subgrid_size) * self.subgrid_size
        subgrid_col_start = (col // self.subgrid_size) * self.subgrid_size
        for r in range(subgrid_row_start, subgrid_row_start + self.subgrid_size):
            for c in range(subgrid_col_start, subgrid_col_start + self.subgrid_size):
                used_values.add(self.board[r][c])
        return [value for value in range(1, self.size + 1) if value not in used_values]
