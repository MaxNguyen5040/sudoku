class Theme:
    def __init__(self, name, background_color, cell_color, text_color):
        self.name = name
        self.background_color = background_color
        self.cell_color = cell_color
        self.text_color = text_color

class ThemeManager:
    def __init__(self):
        self.themes = {
            'light': Theme('Light', 'white', 'lightgray', 'black'),
            'dark': Theme('Dark', 'black', 'gray', 'white')
        }
        self.current_theme = self.themes['light']

    def set_theme(self, theme_name):
        if theme_name in self.themes:
            self.current_theme = self.themes[theme_name]

theme_manager = ThemeManager()

def apply_theme(theme_name):
    theme_manager.set_theme(theme_name)