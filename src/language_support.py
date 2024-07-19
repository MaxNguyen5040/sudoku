import json

class Localization:
    def __init__(self, language='en'):
        self.language = language
        self.load_translations()

    def load_translations(self):
        try:
            with open(f'locales/{self.language}.json', 'r') as file:
                self.translations = json.load(file)
        except FileNotFoundError:
            self.translations = {}

    def translate(self, key):
        return self.translations.get(key, key)

# locales/en.json
{
    "start_game": "Start Game",
    "pause_game": "Pause Game",
    "resume_game": "Resume Game",
    "high_scores": "High Scores",
    "user_profile": "User Profile"
}

# locales/es.json
{
    "start_game": "Iniciar juego",
    "pause_game": "Pausar juego",
    "resume_game": "Reanudar juego",
    "high_scores": "Puntuaciones más altas",
    "user_profile": "Perfil de usuario"
}


localization = Localization(language='es')

def translate(key):
    return localization.translate(key)

print(translate("start_game"))
print(translate("pause_game"))
print(translate("resume_game"))
print(translate("high_scores"))
print(translate("user_profile"))