import pygame as pg
import pygame.gfxdraw as pgfw
import sys

from settings import *
from ui.circle import Circle
from ui.inputText import inputText
from ui.button import Button
from graficacion import Generador, ArbolGrafico

class Motor2D:

    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption("Arbol")

        self.clock = pg.time.Clock()
        self.running = True

        self.input = inputText(self.screen, (100,20),  pg.font.Font(None, 60))
        self.input.setText("a+b-c")

        self.button = Button((20, 20), callback=self)
        self.all_sprites = pg.sprite.Group(self.button)

        self.g = Generador()
        self.g.generarDatos(
            ["G","D","K","H","L","B","A","E","I","C","F","J","M"],
            ["A","B","D","G","H","K","L","C","E","I","F","J","M"]
        )
        self.arbol_g = ArbolGrafico(self.screen, WITH, HEIGHT, self.g)

    def event(self):
        event_list =  pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                self.running = False
            self.button.event(event)
        self.input.event(event_list)

        
    def update(self):
        self.input.update()
        self.all_sprites.update()

        self.arbol_g.update()

    def render(self):
        self.screen.fill(BG_COLOR)

        self.input.render()
        self.all_sprites.draw(self.screen)

        self.arbol_g.render()
        
        pg.display.flip()

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.render()
            self.clock.tick(60)
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    app = Motor2D()
    app.run()
