import pygame.gfxdraw as pgfw
from pygame import Surface

from settings import *

class Circle:

    def __init__(self, screen:Surface, text:str, poss=(0,0)) -> None:
        self.screen = screen
        self.x = poss[0]
        self.y = poss[1]
        self.color = None
        self.text = FONT_1.render(text, True, BLACK)

    def update(self, color=WHITE) -> None:
        self.color = color

    def render(self) -> None:
        pgfw.filled_circle(self.screen, self.x, self.y + 3, 32, GRAY)
        pgfw.aacircle(self.screen, self.x, self.y + 3, 32, GRAY)
        pgfw.filled_circle(self.screen, self.x, self.y, 30, self.color)
        pgfw.aacircle(self.screen, self.x, self.y, 30, self.color)
        self.screen.blit(self.text, (self.x - 10, self.y - 18))
        
