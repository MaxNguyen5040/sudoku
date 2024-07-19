import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            'place_number': pygame.mixer.Sound('sounds/place_number.wav'),
            'game_complete': pygame.mixer.Sound('sounds/game_complete.wav'),
            'error': pygame.mixer.Sound('sounds/error.wav')
        }
        self.background_music = 'sounds/background_music.mp3'

    def play_sound(self, sound):
        if sound in self.sounds:
            self.sounds[sound].play()

    def play_background_music(self):
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)  # Loop the music

    def stop_background_music(self):
        pygame.mixer.music.stop()

sound_manager = SoundManager()
sound_manager.play_background_music()

def place_number():
    sound_manager.play_sound('place_number')

def complete_game():
    sound_manager.play_sound('game_complete')

def handle_error():
    sound_manager.play_sound('error')