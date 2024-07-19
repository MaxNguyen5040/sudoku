import json

class SaveLoad:
    def __init__(self, save_file='savegames.json'):
        self.save_file = save_file

    def save_game(self, game_state, slot):
        try:
            with open(self.save_file, 'r') as file:
                saves = json.load(file)
        except FileNotFoundError:
            saves = {}

        saves[slot] = game_state
        with open(self.save_file, 'w') as file:
            json.dump(saves, file)

    def load_game(self, slot):
        try:
            with open(self.save_file, 'r') as file:
                saves = json.load(file)
            return saves.get(slot, None)
        except FileNotFoundError:
            return None

save_load = SaveLoad()

def save_current_game(game_state, slot):
    save_load.save_game(game_state, slot)

def load_saved_game(slot):
    return save_load.load_game(slot)