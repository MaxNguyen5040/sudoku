class StoryMode:
    def __init__(self, stages):
        self.stages = stages
        self.current_stage = 0

    def next_stage(self):
        if self.current_stage < len(self.stages) - 1:
            self.current_stage += 1
            return self.stages[self.current_stage]
        else:
            return "You've completed the story mode!"

    def get_current_stage(self):
        return self.stages[self.current_stage]

# Example usage
stages = [
    "Welcome to Sudoku Island! Solve the first puzzle to proceed.",
    "Great job! Now solve this harder puzzle.",
    "You're almost there! One last puzzle to win."
]
story = StoryMode(stages)
print(story.get_current_stage())
print(story.next_stage())
print(story.next_stage())
print(story.next_stage())