
OPERANDO = 1
OPERADOR = 0

class Nodo:


    def __init__(self, data, left=None, right=None, type=0) -> None:
        self.data = data
        self.left:Nodo = left
        self.rigth:Nodo = right
        self.type = type