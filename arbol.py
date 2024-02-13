from nodo import Nodo, OPERADOR, OPERANDO

class Arbol:

    def __init__(self, raiz:Nodo=None) -> None:
        self.raiz = raiz

    def isEmpty(self):
        return self.raiz == None

    def agregar(self, nodo:Nodo):
        aux = self.raiz
        while aux.type!= 'raiz':
            aux = aux.rigth
        if aux.left == None:
            aux.left = nodo
        else:
            aux.rigth = nodo
    
    def agregarOperador(self, nodo:Nodo):
        if self.raiz.type == OPERANDO:
            aux = self.raiz
            self.raiz = nodo
            self.raiz.left = aux