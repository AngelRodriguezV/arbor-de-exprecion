import pygame as pg
from pygame import Surface
from settings import *

class ArbolLinea:

    def __init__(self, index, screen:Surface) -> None:
        self.screen = screen
        self.index = index

    def update(self):
        pass

    def render(self):
        for i in self.index:
            p1, p2 = i
            pg.draw.line(self.screen, WHITE, )
