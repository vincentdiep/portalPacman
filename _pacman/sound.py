import pygame as pg


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(0.5)
        chomp_sound = pg.mixer.Sound('sounds/pacman_chomp.wav')
        pg.mixer.Sound.set_volume(chomp_sound, 0.22)
        self.sounds = {'chomp': chomp_sound}
        self.playing_bg = None
        self.play()
        self.pause_bg()

    def pause_bg(self):
        self.playing_bg = False
        pg.mixer.music.pause()

    def unpause_bg(self):
        self.playing_bg = True
        pg.mixer.music.unpause()

    def play(self):
        self.playing_bg = True
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        self.playing_bg = False
        pg.mixer.music.stop()

    def chomper(self): pg.mixer.Sound.play(self.sounds['chomp'])
