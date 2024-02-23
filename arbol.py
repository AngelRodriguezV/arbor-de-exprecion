from nodo import Nodo, inorden, preorden, postorden

operadores = {'*': 2, '/': 2, '-': 1, '+': 1, '=': 0}

class Arbol:

    def __init__(self, raiz:Nodo=None) -> None:
        self.raiz = raiz

        self.index = 0
        self.cadena = ''
        self.parentesis = 0

    def isOperador(self, caracter):
        return caracter in ('+', '-', '*', '/','=')
    
    def crearArbol(self, cadena):
        self.cadena = cadena
        self.raiz = None
        _id = -1
        # Recorre la cadena
        # Mientras el caracter diferente de nulo
        for i, caracter in enumerate(cadena):
            self.index = i
            # Leer caracter
            # Si es parentesis pasar al siguiente caracter
            if caracter == "(":
                self.parentesis += 1
                continue
            if caracter == ")":
                self.parentesis -= 1
                continue
            _id += 1
            # Crear un nodo nuevo que contenga ese caracter
            nodo = Nodo(data=caracter, _id=_id)

            if self.isOperador(caracter):
                self.raiz = self.__insertar_operador(nodo, self.raiz)
            else:
                self.raiz = self.__insertar_operando(nodo, self.raiz)
                

    def __insertar_operando(self, new:Nodo, root:Nodo=None) -> Nodo:
        # Si la raiz es nula
        if root == None:
            # Nuevo nodo se combierte en raiz
            return new
        else:
            aux = root
            # Recorrer el arbol por la derecha hasta llegar a un nodo con hojas
            while aux.rigth:
                aux = aux.rigth
            # Si la hoja izquierda es nula agregar al nodo izquierdo
            if aux.left == None:
                aux.left = new
            # Si no Colocarlo en la hoja derecha.
            else:
                aux.rigth = new
            # Retorna la raiz
            return root
        
    def __insertar_operador(self, new:Nodo, root:Nodo=None) -> Nodo:
        # Si la raíz es un operando
        if not self.isOperador(root.data):
            # Insertar nuevo en ese nodo y convertir el operando en el hijo izquierdo
            new.left = root
            return new
        # Si no 
        else:
            # Si hay un paréntesis abierto
            if self.parentesis > 0:
                # Insertar nuevo en la última hoja derecha
                aux = root
                while aux.rigth:
                    if aux.rigth.rigth != None:
                        aux = aux.rigth
                    break
                rigth = aux.rigth
                aux.rigth = new
                # Y Colocar operando como hijo izquierdo.
                new.left = rigth
                return root
        
        # Si el carácter anterior es paréntesis izquierdo
        if self.cadena[self.index - 1] == ')':
            # Si el siguiente carácter es paréntesis derecho
            if self.cadena[self.index + 1] == '(':
                # Si solo hay un operador en el árbol
                if not self.isOperador(root.left) and not self.isOperador(root.rigth): 
                    # Nuevo se convierte en raíz
                    new.left = root
                    return new
                # Si no 
                else:
                    # Se inserta en el último nodo derecho
                    aux = root
                    while aux.rigth:
                        aux = aux.rigth
                    # y el nodo se convierte en hijo izquierdo.
                    aux.left = new
            else:
                # Nuevo se convierte en raíz
                new.left = root
                return new

        # Si no se cumple ninguna de las condiciones anteriores
        else:
            # Si la raíz es de igual prioridad o menor prioridad 
            if self.__prioridad(root.data, new.data):
                # Convertir la raíz en el hijo izquierdo de nuevo 
                new.left = root
                return new
            # Si no, la prioridad del nodo raíz es mayor al de nuevo
            else: 
                # Insertar nuevo como hijo derecho
                #aux = root.rigth
                #root.rigth = new
                aux = root
                while aux.rigth:
                    if aux.rigth.rigth != None:
                        aux = aux.rigth
                    break
                rigth = aux.rigth
                aux.rigth = new
                # Colocar el nodo reemplazado como hijo izquierdo
                #root.left = aux
                new.left = rigth
                return root

    def __prioridad(self, operador1, operador2):
        return operadores[operador1] >= operadores[operador2]

    def inorden(self):
        return inorden(self.raiz)
    
    def preorden(self):
        return preorden(self.raiz)
    
    def postorden(self):
        return postorden(self.raiz)