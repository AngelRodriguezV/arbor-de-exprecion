import sys
sys.path.append("D:\\Usuarios\\veng\\Documentos\\development\\analizador_semantico")
from nodo import Nodo, inorden

root = Nodo('=', 0)

nodo_l1 = Nodo('x', 1)

nodo_root = Nodo('+', 2)

root.left = nodo_l1
root.rigth = nodo_root

nodo_l = Nodo('a', 3)
nodo_r = Nodo('b', 4)
nodo_root.left = nodo_l
nodo_root.rigth = nodo_r

l = inorden(root)

print(l)