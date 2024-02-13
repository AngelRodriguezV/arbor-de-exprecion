import pygame.gfxdraw as pgfw
from pygame import Surface

from settings import *

class Circle:

    def __init__(self, screen:Surface, text:str) -> None:
        self.screen = screen
        self.x = 0
        self.y = 0
        self.color = None
        self.text = FONT_1.render(text, True, BLACK)

    def update(self, position, color=WHITE) -> None:
        self.x = position[0]
        self.y = position[1]
        self.color = color

    def render(self) -> None:
        pgfw.filled_circle(self.screen, self.x, self.y + 3, 32, GRAY)
        pgfw.aacircle(self.screen, self.x, self.y + 3, 32, GRAY)
        pgfw.filled_circle(self.screen, self.x, self.y, 30, self.color)
        pgfw.aacircle(self.screen, self.x, self.y, 30, self.color)
        self.screen.blit(self.text, (self.x - 16, self.y - 16))
        
