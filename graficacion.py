import pygame as pg
from pygame import Surface

from ui.circle import Circle

from settings import *

class Generador:

    def __init__(self) -> None:
        
        self.inorde = []
        self.preorden = []

        self.indices = []
        self.puntos = []
        self.index_y = 0

    def __obtener_puntos(self, star, end, n=1):
        if star > end or star == end:
            return -1
        index_x = self.__encontrar_indice(self.preorden[self.index_y])
        self.puntos.append((index_x + 1, n, self.preorden[self.index_y]['valor']))
        self.index_y += 1
        aux = self.index_y
        left = self.__obtener_puntos(star, index_x, n + 1)
        right = self.__obtener_puntos(index_x + 1, end, n + 1)
        self.indices.append([aux, left])
        self.indices.append([aux, right])

        return aux

    def __encontrar_indice(self, data):
        for i, v in enumerate(self.inorde):
            if v['id'] == data['id']:
                return i
        return -1

    def getIndices(self):
        aux = []
        for i in self.indices:
            if i[1] == -1:
                continue
            aux.append(i)
        return aux
    
    def getPuntos(self):
        return self.puntos
    
    def generarDatos(self, inorden, preorden):
        self.inorde = inorden
        self.preorden = preorden
        self.__obtener_puntos(star=0, end=len(self.inorde))

class ArbolGrafico:

    def __init__(self, screen:Surface, width, height, data:Generador) -> None:
        self.screen = screen
        self.width = width
        self.height = height

        self.indices = data.getIndices()
        self.puntos = []
        v_y = [p[1] for p in data.getPuntos()]
        y_m = max(v_y)
        for i in data.getPuntos():
            x = int((i[0]*self.width)/(len(data.getPuntos())+1))
            y = int((i[1])*(self.height/(y_m + 1)))
            a = i[2]
            self.puntos.append((x,y,a))

        self.all_sprites = pg.sprite.Group()
        
    def update(self):
        # Remueve los esprites 
        self.all_sprites.remove(self.all_sprites)
        # Genera los circulos
        for p in self.puntos:
            circle = Circle(p[0], p[1], 30, RED, p[2])
            self.all_sprites.add(circle)
        # actualiza los puntos
        self.all_sprites.update()

    def render(self):
        # lineas
        for indice in self.indices:
            i1, i2 = indice
            p1 = (self.puntos[i1 - 1][0], self.puntos[i1 - 1][1])
            p2 = (self.puntos[i2 - 1][0], self.puntos[i2 - 1][1])
            pg.draw.line(self.screen, WHITE, p1, p2, 8)
        # nodos
        self.all_sprites.draw(self.screen)