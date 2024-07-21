class Sudoku:
    def __init__(self, size=9):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]
        self.subgrid_size = int(size ** 0.5)

    def generate_puzzle(self):
        from random import sample
        base = range(1, self.size + 1)
        rows  = [sample(base, len(base)) for _ in range(self.size)]
        cols  = [sample(base, len(base)) for _ in range(self.size)]
        self.grid = [list(row) for row in zip(*cols)]

    def is_valid(self):
        for i in range(self.size):
            if len(set(self.grid[i])) != self.size:
                return False
            if len(set(row[i] for row in self.grid)) != self.size:
                return False
        for r in range(0, self.size, self.subgrid_size):
            for c in range(0, self.size, self.subgrid_size):
                block = {self.grid[r+i][c+j] for i in range(self.subgrid_size) for j in range(self.subgrid_size)}
                if len(block) != self.subgrid_size ** 2:
                    return False
        return True

    def display(self):
        for row in self.grid:
            print(" ".join(map(str, row)))
        print()