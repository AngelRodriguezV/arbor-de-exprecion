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

    def on_button_click(self):
        ecuacion = self.input.getText()  # Obtener la ecuación del campo de entrada
        postfija_ecuacion = postfija(ecuacion)  # Convertir a postfija
        raiz = arbol(postfija_ecuacion)  # Construir el árbol
        print("In orden =", inorder(raiz))
        print("Pre orden =", preorder(raiz))
        print("Post orden =", postorder(raiz))
        # Ahora, aquí puedes construir o actualizar el árbol gráfico con la nueva expresión

    # Nuevo método para manejar el evento de clic del botón
    def on_button_event(self, event):
        if event == "click":
            self.on_button_click()


    
def postfija(infija):
    pilaOperadores = []
    operadores = "(+-*/)"
    posfija = ""
    i = 0
    while i < len(infija):
        t = infija[i]
        if t == '(':
            pilaOperadores.append(t)
        else:
            if t == ')':
                while pilaOperadores:
                    o = pilaOperadores.pop()
                    if o != '(':
                        posfija += o
            else:
                if t in ['+', '-']:
                    if any(op in ['*', '/', '-', '+'] for op in pilaOperadores):
                        while pilaOperadores:
                            posfija += pilaOperadores.pop()
                    pilaOperadores.append(t)
                else:
                    if t in ['*', '/']:
                        while pilaOperadores and (pilaOperadores[-1] in ['*', '/']):
                            posfija += pilaOperadores.pop()
                        pilaOperadores.append(t)
                    else:
                        posfija += t
        i += 1
    while pilaOperadores:
        posfija += pilaOperadores.pop()
    return posfija

def arbol(posfija):
    pilaNodos = []
    for c in posfija:
        if not esOperador(c):
            nodo = Nodo(c)
            pilaNodos.append(nodo)
        else:
            nodo = Nodo(c)
            nodoDer = pilaNodos.pop()
            nodoIzq = pilaNodos.pop()
            nodo.der = nodoDer
            nodo.izq = nodoIzq
            pilaNodos.append(nodo)
    return pilaNodos.pop()

def esOperador(c):
    return c in ('+', '-', '*', '/')

# Recorridos
inO = ""
postO = ""
preO = ""

def inorder(nodo):
    global inO
    if nodo:
        inorder(nodo.izq)
        inO += nodo.valor
        inorder(nodo.der)
    return inO

def preorder(nodo):
    global preO
    if nodo:
        preO += nodo.valor
        preorder(nodo.izq)
        preorder(nodo.der)
    return preO

def postorder(nodo):
    global postO
    if nodo:
        postorder(nodo.izq)
        postorder(nodo.der)
        postO += nodo.valor
    return postO
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
