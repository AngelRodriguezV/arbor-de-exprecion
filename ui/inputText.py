import pygame as pg
import pygame.gfxdraw as pgfw
from pygame import Surface

from settings import *

class inputText:

    def __init__(self, screen:Surface, poss, font) -> None:
        self.screen = screen
        self.poss = poss
        self.font = font
        self.active = False
        self.text = ""
        self.t_surf = self.font.render(self.text, True, WHITE)
        self.color = BLACK
        self.rect = pg.Rect(self.poss[0], self.poss[1], 1000, 50)

    def event(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN: 
                if self.rect.collidepoint(event.pos): 
                    self.active = True
                else: 
                    self.active = False
            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def update(self):
        if self.active: 
            self.color =  GRAY
        else: 
            self.color = BLACK
        self.rect.w = max(100, self.t_surf.get_width()+10)

    def render(self):
        pg.draw.rect(self.screen, self.color, self.rect)
        self.t_surf = self.font.render(self.text, True, WHITE)
        self.screen.blit(self.t_surf, (self.rect.x+5, self.rect.y+5))

    def getText(self) -> str:
        return self.text
    
    def setText(self, text:str):
        self.text = text