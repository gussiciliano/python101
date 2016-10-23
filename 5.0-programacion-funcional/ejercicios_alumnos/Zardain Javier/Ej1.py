'''
Created on 20/10/2016

@author: javier_zardain

Revertir una lista
'''

lista = [2,4,6,8,10,12,14,16,18]
listaRevertida = [lista[x] for x in range(len(lista)-1,-1,-1)]

print(listaRevertida)