import tkinter as tk
from board import Board
from solver import Solver

class SudokuGUI:
    def __init__(self, root, board, solver):
        self.root = root
        self.board = board
        self.solver = solver
        self.root.title("Sudoku")
        self.cells = {}
        self.create_board()

    def create_board(self):
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(self.root, width=5, font=("Arial", 18), justify="center")
                cell.grid(row=row, column=col, padx=1, pady=1, ipadx=5, ipady=5)
                if self.board.grid[row][col] != 0:
                    cell.insert(0, self.board.grid[row][col])
                    cell.config(state="readonly", disabledbackground="light grey")
                self.cells[(row, col)] = cell

    def highlight_cells(self):
        for row in range(9):
            for col in range(9):
                self.cells[(row, col)].config(bg="white")
        selected = self.root.focus_get()
        for pos, cell in self.cells.items():
            if cell == selected:
                for col in range(9):
                    self.cells[(pos[0], col)].config(bg="light yellow")
                for row in range(9):
                    self.cells[(row, pos[1])].config(bg="light yellow")
                box_x = pos[1] // 3
                box_y = pos[0] // 3
                for i in range(box_y * 3, box_y * 3 + 3):
                    for j in range(box_x * 3, box_x * 3 + 3):
                        self.cells[(i, j)].config(bg="light yellow")
                break

    def create_board(self):
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(self.root, width=5, font=("Arial", 18), justify="center")
                cell.grid(row=row, column=col, padx=1, pady=1, ipadx=5, ipady=5)
                cell.bind("<FocusIn>", lambda e: self.highlight_cells())
                if self.board.grid[row][col] != 0:
                    cell.insert(0, self.board.grid[row][col])
                    cell.config(state="readonly", disabledbackground="light grey")
                self.cells[(row, col)] = cell

    def update_board(self):
        for row in range(9):
            for col in range(9):
                value = self.cells[(row, col)].get()
                self.board.grid[row][col] = int(value) if value.isdigit() else 0

    def solve_board(self):
        self.update_board()
        if self.solver.solve():
            self.display_message("Sudoku solved!")
            for row in range(9):
                for col in range(9):
                    self.cells[(row, col)].delete(0, tk.END)
                    self.cells[(row, col)].insert(0, self.board.grid[row][col])
        else:
            self.display_message("No solution found.")

    def clear_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[(row, col)].delete(0, tk.END)

    def reset_board(self):
        self.board.reset()
        self.create_board()

    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_board)
        solve_button.grid(row=10, column=0, columnspan=3)

        reset_button = tk.Button(self.root, text="Reset", command=self.reset_board)
        reset_button.grid(row=10, column=3, columnspan=3)

        clear_button = tk.Button(self.root, text="Clear", command=self.clear_board)
        clear_button.grid(row=10, column=6, columnspan=3)

def main():
    root = tk.Tk()
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    board = Board(grid)
    solver = Solver(board)
    gui = SudokuGUI(root, board, solver)
    gui.create_buttons()
    root.mainloop()

if __name__ == "__main__":
    main()
