'''
Created on 8/9/2016

@author: javier_zardain

Dadas 2 listas con la misma cantidad de elementos intercalarlos.
'''

def cruzarListas(lista1, lista2, nuevaLista, indice=0):
    x = int(len(nuevaLista)/2)
    nuevaLista.append(lista1[indice])
    nuevaLista.append(lista2[indice])
    if x != len(lista1)-1:
        cruzarListas(lista1, lista2, nuevaLista, indice+1)

lista1 = [1,2,3,4]
lista2 = [9,8,7,6]
nuevaLista = []
cruzarListas(lista1, lista2, nuevaLista)
print(nuevaLista)