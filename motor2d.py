import pygame as pg
import pygame_gui as gui
import sys

from settings import *
from ui.circle import Circle
from ui.inputText import inputText
from ui.button import Button
from graficacion import Generador, ArbolGrafico
from nodo import Nodo
from arbol import Arbol

class Motor2D:

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Arbol de Exprecion")
        self.window_surface = pg.display.set_mode(SIZE, pg.RESIZABLE)

        self.screen = pg.Surface((1600,800))
        self.manager = gui.UIManager((2000,400))

        self.clock = pg.time.Clock()
        self.running = True

        # ==================== Componentes UI ========================
        self.btn_ejecutar = gui.elements.UIButton(relative_rect=pg.Rect((10, 10), (150, 50)),
            text='Crear Arbol',
            manager=self.manager)
        self.txt_label = gui.elements.UILabel(relative_rect=pg.Rect((200, 10), (200, 50)),
            text='Ingrese una expresion',
            manager=self.manager)
        self.input_expresion = gui.elements.UITextEntryLine(relative_rect=pg.Rect((400, 10), (1000, 50)),
            manager=self.manager)

        # ============================================================

        self.arbol_g = None

    def event(self):
        event_list =  pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                self.running = False
            
            if event.type == gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.btn_ejecutar:

                    if self.input_expresion.get_text() != '':
                        for c in self.input_expresion.get_text():
                            if not c in 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM()=+-/*':
                                return  
                        print('La cadena no esta vacia: ' + self.input_expresion.get_text())
                        arbol = Arbol()
                        arbol.crearArbol(self.input_expresion.get_text())
                        print('Inorden: ')
                        print(arbol.inorden())
                        print('Preorden: ')
                        print(arbol.preorden())
                        generar_coord = Generador()
                        generar_coord.generarDatos(arbol.inorden(), arbol.preorden())
                        print('Indices: ')
                        print(generar_coord.getIndices())
                        print('Puntos: ')
                        print(generar_coord.getPuntos())
                        self.arbol_g = ArbolGrafico(self.screen, WITH, HEIGHT, generar_coord)

            
            self.manager.process_events(event)
        
    def update(self):
        self.manager.update(self.clock.tick(60)/1000.0)

        if not (self.arbol_g == None):
            self.arbol_g.update()

    def render(self):
        self.screen.fill(BG_COLOR)
        
        if not (self.arbol_g == None):
            self.arbol_g.render()

        self.window_surface.blit(self.screen, (100,100))
        self.manager.draw_ui(self.window_surface)
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
