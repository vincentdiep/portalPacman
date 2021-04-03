import pygame as pg
import game_functions as gf
from settings import Settings
from maze import Maze
from character import Pacman, Blinky, Inky, Pinky, Clyde

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button, HighScoreMenu
from displayscores import DisplayScores
from sound import Sound

score_path = 'scores/scores.txt'


# ===================================================================================================
# class Game
# ===================================================================================================
class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(size=(self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("PacMan Portal")
        self.font = pg.font.SysFont(None, 48)
        self.points = 0
        self.hs = 0
        self.maze = Maze(game=self)

        self.sound = Sound(bg_music="sounds/pixel_kingdom.mp3")
        self.sound.play()
        self.sound.pause_bg()

        self.pacman = Pacman(game=self, sound=self.sound)
        self.ghosts = [Blinky(game=self), Pinky(game=self), Clyde(game=self), Inky(game=self)]
        for ghost in self.ghosts:
            ghost.set_ghosts(self.ghosts)
        self.finished = False

        self.play_button = self.stats = self.sb = self.score_button = self.score_menu = None
        self.restart()

    def to_grid(self, index):
        row = index // 11
        offset = index % 11
        ss = self.maze.location(row, offset)
        return ss

    # def to_pixel(self, grid): pixels = []

    def restart(self):
        self.play_button = Button(game=self, screen=self.screen, msg="Play Game")
        self.score_button = HighScoreMenu(screen=self.screen, msg="High Scores")
        self.score_menu = DisplayScores(settings=self.settings)
        self.stats = GameStats(settings=self.settings)
        self.sb = Scoreboard(game=self, sound=self.sound)

        self.stats.high_score = self.hs
        self.sb.read_scores(score_path)
        self.sb.prep_high_score()

    def play(self):
        while not self.finished:
            gf.check_events(game=self)
            # self.screen.fill(self.settings.bg_color)
            if self.stats.game_active:
                self.maze.update()
                for ghost in self.ghosts:
                    ghost.update()
                self.pacman.update()
                self.sb.prep_score()
                self.sb.show_score()

            if not self.stats.game_active:
                self.play_button.draw()
                self.score_button.draw()
                self.sound.pause_bg()
                if self.score_menu.show_scores_menu:
                    self.sb.prep_score_display(score_path)

            else:
                if not self.sound.playing_bg:
                    self.sound.unpause_bg()
            pg.display.flip()
        if self.finished:
            self.stats.game_active = False
            self.sound.pause_bg()
            f = open('scores/scores.txt', 'a')
            f.write(str(self.points))
            f.write('\n')
            f.close()


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
