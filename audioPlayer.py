import pygame


class AudioPlayer:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        self.start_sound = pygame.mixer.Sound("sounds/start.wav")
        self.stop_sound = pygame.mixer.Sound("sounds/stop.wav")

    def playStartSound(self):
        self.start_sound.play()

    def playStopSound(self):
        self.stop_sound.play()
