class Tutorial:
    def __init__(self):
        self.steps = [
            "Welcome to Sudoku! Let's start by learning the basics.",
            "Step 1: Each row must contain the numbers 1 to 9 without repetition.",
            "Step 2: Each column must also contain the numbers 1 to 9 without repetition.",
            "Step 3: Each 3x3 subgrid must contain the numbers 1 to 9 without repetition.",
            "Step 4: Click on a cell to select it and enter a number.",
            "That's it! Try solving the puzzle with these rules in mind."
        ]
        self.current_step = 0

    def next_step(self):
        if self.current_step < len(self.steps):
            self.current_step += 1
        return self.steps[self.current_step - 1] if self.current_step <= len(self.steps) else None

tutorial = Tutorial()

def show_next_tutorial_step():
    step = tutorial.next_step()
    if step:
        print(step)