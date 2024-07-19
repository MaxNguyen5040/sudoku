def save_game(self):
        game_state = {
            "grid": self.board.grid,
            "time": time.time() - self.start_time,
            "moves": self.move_count
        }
        with open("sudoku_save.json", "w") as save_file:
            json.dump(game_state, save_file)

def load_game(self):
        try:
            with open("sudoku_save.json", "r") as save_file:
                game_state = json.load(save_file)
            self.board.grid = game_state["grid"]
            self.start_time = time.time() - game_state["time"]
            self.move_count = game_state["moves"]
            self.create_board()
            self.update_move_counter()
        except FileNotFoundError:
            self.display_message("No saved game found.")