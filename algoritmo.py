from nodo import Nodo
from arbol import Arbol

class Algoritmo:

    def __init__(self) -> None:
        pass

def isOperador(caracter):
    return caracter in "+-*/"

def run(cadena):
    arbol = Arbol()
    # Recorre la cadena
    for i in range(0,len(cadena)):
        # Mientras el caracter diferente de nulo
        if cadena[i] != None:
            # Leer caracter
            caracter = cadena[i]
            # Si es parentesis pasar al siguiente caracter
            if caracter == "(" or caracter == ")":
                continue
            # Crear un nodoo nuevo que contenga ese caracter
            nodo = Nodo(data=caracter)

            if isOperador(caracter):
                print(nodo.data + "  Es operador")
            else:
                nodo.type = 'hoja'
                if arbol.isEmpty():
                    arbol.raiz = nodo
                else:
                    pass


run("a+b-(g*r)")