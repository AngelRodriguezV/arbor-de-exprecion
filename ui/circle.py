import pygame as pg
from pygame import Surface

from settings import *

class Circle(pg.sprite.Sprite):

    def __init__(self,  x, y, radius, color, text):
        super().__init__()

        self.image = pg.Surface((2 * radius, 2 * radius), pg.SRCALPHA)

        pg.draw.circle(self.image, color, (radius, radius), radius)

        font = pg.font.Font(None, 24)
        text_surface = font.render(text, True, pg.Color("white"))
        text_rect = text_surface.get_rect(center=(radius, radius))

        self.image.blit(text_surface, text_rect)
        self.rect = self.image.get_rect(center=(x, y))
        
