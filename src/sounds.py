import pygame

class SoundManager:
    def __init__(self, music_file, sound_files):
        pygame.mixer.init()
        self.music_file = music_file
        self.sound_files = sound_files

    def play_music(self):
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_sound(self, sound_name):
        if sound_name in self.sound_files:
            sound = pygame.mixer.Sound(self.sound_files[sound_name])
            sound.play()

sound_files = {
    "correct": "correct_sound.wav",
    "incorrect": "incorrect_sound.wav"
}
sound_manager = SoundManager("background_music.mp3", sound_files)
sound_manager.play_music()
sound_manager.play_sound("correct")