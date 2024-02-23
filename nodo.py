class Nodo:
    """
        Clase Nodo
    """
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left:Nodo = left
        self.rigth:Nodo = right

# Preorden VLR
def preorden(root:Nodo=None) -> list:
    """
        Metodo para el recorrido preorden (Prefijo).
        Retorna una lista que contiene el recorrido en preorden(Prefijo).
        VLR
    """
    # Si la raiz no es un nulo
    if root:
        pre = [root.data]           # Agrega el valor del nodo
        pre += preorden(root.left)  # Agrega el resultado del recorrido por el nodo izquierdo
        pre += preorden(root.rigth) # Agrega el resultado del recorrido por el nodo derecho
        return pre
    # De se nulo la raiz, retorna una lista vacia
    return []

# Infijo LVR
def inorden(root:Nodo=None) -> list:
    """
        Metodo para el recorrido en Inorden (Infijo).
        Retorna una lista que contiene el recorrido en Inorden (Inorden).
        VLR
    """
    # Si la raiz no es un nulo
    if root:
        inor = inorden(root.left)   # Agrega el resultado del recorrido por el nodo izquierdo
        inor += [root.data]         # Agrega el valor del nodo
        inor += inorden(root.rigth) # Agrega el resultado del recorrido por el nodo derecho
        return inor
    # De se nulo la raiz, retorna una lista vacia
    return []

# Postfijo LRV
def postorden(root:Nodo=None) -> list:
    """
        Metodo para el recorrido en Postorden (Postfijo).
        Retorna una lista que contiene el recorrido en Postorden (Postfijo).
        LRV
    """
    # Si la raiz no es un nulo
    if root:
        post = postorden(root.left)   # Agrega el resultado del recorrido por el nodo izquierdo
        post += postorden(root.rigth) # Agrega el resultado del recorrido por el nodo derecho
        post += [root.data]           # Agrega el valor del nodo
        return post
    # De se nulo la raiz, retorna una lista vacia
    return []