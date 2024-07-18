from board import Board
from solver import Solver

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board.grid[i][j])
            else:
                print(str(board.grid[i][j]) + " ", end="")

def main():
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

    while True:
        print_board(board)
        command = input("Enter command (enter 'q' to quit): ")

        if command.lower() == 'q':
            break
        elif command.lower() == 'reset':
            board.reset()
        elif command.lower() == 'clear':
            board.clear()
        elif command.lower() == 'solve':
            if solver.solve():
                print("Sudoku solved!")
            else:
                print("No solution found.")
        elif command.lower() == 'check':
            if solver.is_solved():
                print("Sudoku puzzle is solved correctly!")
            else:
                print("Sudoku puzzle is not solved yet.")
        elif command.lower() == 'exit':
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
