import sys
sys.path.append("D:\\Usuarios\\veng\\Documentos\\development\\analizador_semantico")
from nodo import Nodo, preorden

root = Nodo('=')

nodo_l1 = Nodo('x')

nodo_root = Nodo('+')

root.left = nodo_l1
root.rigth = nodo_root

nodo_l = Nodo('a')
nodo_r = Nodo('b')
nodo_root.left = nodo_l
nodo_root.rigth = nodo_r

l = preorden(root)

print(l)