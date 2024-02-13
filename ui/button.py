import pygame as pg

from settings import *

class Button(pg.sprite.Sprite):
    def __init__(self, poss, callback):
        pg.sprite.Sprite.__init__(self)

        self.BUTTON_UP_IMG = pg.Surface((50, 50), pg.SRCALPHA)
        self.BUTTON_DOWN_IMG = pg.Surface((50, 50), pg.SRCALPHA)

        pg.draw.polygon(self.BUTTON_UP_IMG, GREEN, [(0, 0), (0, 50), (50, 25)])
        pg.draw.polygon(self.BUTTON_DOWN_IMG, WHITE, [(0, 0), (0, 50), (50, 25)])

        self.image = self.BUTTON_UP_IMG
        self.rect = self.image.get_rect(topleft=poss)
        self.callback = callback

    def event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.image = self.BUTTON_DOWN_IMG
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                self.image = self.BUTTON_UP_IMG
                if self.rect.collidepoint(event.pos):
                    # Button pressed, call your callback function
                    pass