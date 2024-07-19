class GameCustomization:
    def __init__(self):
        self.settings = {
            'difficulty': 'medium',
            'timer': True,
            'hints': True
        }

    def set_difficulty(self, difficulty):
        if difficulty in ['easy', 'medium', 'hard']:
            self.settings['difficulty'] = difficulty

    def toggle_timer(self):
        self.settings['timer'] = not self.settings['timer']

    def toggle_hints(self):
        self.settings['hints'] = not self.settings['hints']

customization = GameCustomization()

def set_game_difficulty(difficulty):
    customization.set_difficulty(difficulty)

def toggle_game_timer():
    customization.toggle_timer()

def toggle_game_hints():
    customization.toggle_hints()