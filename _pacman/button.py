import pygame as pg
import pygame.font
from settings import Settings
from timer import Timer, TimerDict


def image_helper(color, direction):
    return [pg.image.load('images/' + color + 'g' + direction + str(x) + '.png') for x in range(3, 5)]


class Button:
    def __init__(self, game, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = game.settings

        self.width, self.height = 200, 50
        self.button_color = (50, 50, 50)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 58)

        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.msg_image = self.msg_image_rect = None
        self.prep_msg(msg)

        self.images_pman = [pg.image.load('images/pmanopen' + str(x) + '.png') for x in range(0, 12)]
        self.timer = Timer(self.images_pman, wait=20, oscillating=True)

        # Blinky images
        imagesrl = image_helper(color='r', direction='l')
        imagesrr = image_helper(color='r', direction='r')
        imagesru = image_helper(color='r', direction='u')
        imagesrd = image_helper(color='r', direction='d')

        self.b_timer = TimerDict(dict_frames={'left': imagesrl, 'right': imagesrr, 'up': imagesru, 'down': imagesrd},
                                 first_key='left')

        # Inky images
        imagesbl = image_helper(color='b', direction='l')
        imagesbr = image_helper(color='b', direction='r')
        imagesbu = image_helper(color='b', direction='u')
        imagesbd = image_helper(color='b', direction='d')

        self.i_timer = TimerDict(dict_frames={'left': imagesbl, 'right': imagesbr, 'up': imagesbu, 'down': imagesbd},
                                 first_key='left')

        # Pinky images
        imagespl = image_helper(color='p', direction='l')
        imagespr = image_helper(color='p', direction='r')
        imagespu = image_helper(color='p', direction='u')
        imagespd = image_helper(color='p', direction='d')

        self.p_timer = TimerDict(dict_frames={'left': imagespl, 'right': imagespr, 'up': imagespu, 'down': imagespd},
                                 first_key='left')

        # Clyde images
        imagesol = image_helper(color='o', direction='l')
        imagesor = image_helper(color='o', direction='r')
        imagesou = image_helper(color='o', direction='u')
        imagesod = image_helper(color='o', direction='d')

        self.c_timer = TimerDict(dict_frames={'left': imagesol, 'right': imagesor, 'up': imagesou, 'down': imagesod},
                                 first_key='left')

    def draw_pman(self):
        image = self.timer.imagerect()
        p_rect = image.get_rect()
        p_rect.centerx, p_rect.centery = self.screen_rect.centerx * 2 / 3, self.screen_rect.centery * 2 / 3
        self.screen.blit(image, p_rect)
        p_man_label = self.font.render("PACMAN", True, (255, 255, 0), self.settings.bg_color)
        p_man_label_rect = p_man_label.get_rect()
        p_man_label_rect.centerx, p_man_label_rect.centery = self.screen_rect.centerx, p_rect.centery
        self.screen.blit(p_man_label, p_man_label_rect)
        portal_label = self.font.render("PORTAL", True, (255, 255, 0), self.settings.bg_color)
        portal_label_rect = portal_label.get_rect()
        portal_label_rect.centerx, portal_label_rect.bottom = self.screen_rect.centerx, p_man_label_rect.top
        self.screen.blit(portal_label, portal_label_rect)

    def draw_blinky(self):
        image = self.b_timer.imagerect()
        b_rect = image.get_rect()
        b_rect.centerx, b_rect.centery = self.screen_rect.centerx * 2 / 3, self.screen_rect.centery * 7 / 5
        self.screen.blit(image, b_rect)
        b_label = self.font.render("BLINKY", True, (255, 0, 0), self.settings.bg_color)
        b_label_rect = b_label.get_rect()
        b_label_rect.centerx, b_label_rect.centery = self.screen_rect.centerx, b_rect.centery
        self.screen.blit(b_label, b_label_rect)

    def draw_pinky(self):
        image = self.p_timer.imagerect()
        p_rect = image.get_rect()
        p_rect.centerx, p_rect.centery = self.screen_rect.centerx * 2 / 3, self.screen_rect.centery * 8 / 5
        self.screen.blit(image, p_rect)
        p_label = self.font.render("PINKY", True, (255, 204, 204), self.settings.bg_color)
        p_label_rect = p_label.get_rect()
        p_label_rect.centerx, p_label_rect.centery = self.screen_rect.centerx, p_rect.centery
        self.screen.blit(p_label, p_label_rect)

    def draw_inky(self):
        image = self.i_timer.imagerect()
        i_rect = image.get_rect()
        i_rect.centerx, i_rect.centery = self.screen_rect.centerx * 2 / 3, self.screen_rect.centery * 6 / 5
        self.screen.blit(image, i_rect)
        i_label = self.font.render("INKY", True, (51, 255, 255), self.settings.bg_color)
        i_label_rect = i_label.get_rect()
        i_label_rect.centerx, i_label_rect.centery = self.screen_rect.centerx, i_rect.centery
        self.screen.blit(i_label, i_label_rect)

    def draw_clyde(self):
        image = self.c_timer.imagerect()
        c_rect = image.get_rect()
        c_rect.centerx, c_rect.centery = self.screen_rect.centerx * 2 / 3, self.screen_rect.centery * 9 / 5
        self.screen.blit(image, c_rect)
        c_label = self.font.render("CLYDE", True, (255, 128, 0), self.settings.bg_color)
        c_label_rect = c_label.get_rect()
        c_label_rect.centerx, c_label_rect.centery = self.screen_rect.centerx, c_rect.centery
        self.screen.blit(c_label, c_label_rect)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.draw_pman()
        self.draw_blinky()
        self.draw_inky()
        self.draw_pinky()
        self.draw_clyde()


class HighScoreMenu:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = Settings()

        self.width, self.height = 200, 50
        self.button_color = (100, 100, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 80)
        self.msg_image = self.msg_image_rect = None

        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.centerx, self.rect.y = self.screen_rect.centerx, 10
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.rect.width, self.rect.height = self.msg_image_rect.width, self.msg_image_rect.height
        self.rect.centerx = self.screen_rect.centerx

    def draw(self):
        self.screen.blit(self.msg_image, self.rect)
