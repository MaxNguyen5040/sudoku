import time

class GameTimer:
    def __init__(self):
        self.start_time = None
        self.paused_time = 0
        self.running = False

    def start(self):
        self.start_time = time.time()
        self.running = True

    def pause(self):
        if self.running:
            self.paused_time += time.time() - self.start_time
            self.running = False

    def resume(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def get_elapsed_time(self):
        if self.running:
            return time.time() - self.start_time + self.paused_time
        return self.paused_time


game_timer = GameTimer()

def start_game():
    game_timer.start()

def pause_game():
    game_timer.pause()

def resume_game():
    game_timer.resume()

def get_time():
    return game_timer.get_elapsed_time()