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

    def isOperador(caracter):
        return caracter in "+-*/"

    def crearArbol(self, cadena):
        # Recorre la cadena
        for i in range(0,len(cadena)):
            # Mientras el caracter diferente de nulo
            if cadena[i] != None:
                # Leer caracter
                caracter = cadena[i]
                # Si es parentesis pasar al siguiente caracter
                if caracter == "(" or caracter == ")":
                    self.numero_parentesis += 1
                    continue
                # Crear un nodoo nuevo que contenga ese caracter
                nodo = Nodo(data=caracter)

                if self.isOperador(caracter):
                    print(nodo.data + "  Es operador")
                else:
                    nodo.type = 'hoja'
                    if self.arbol.isEmpty():
                        self.arbol.raiz = nodo
                    else:
                        pass