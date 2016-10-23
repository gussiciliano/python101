'''
Created on 20/10/2016

@author: javier_zardain

Dadas 2 listas con la misma cantidad de elementos intercalarlos.
'''

def cruzarListas(lista1, lista2):
    if(len(lista1) > 1):
        lista = [lista1.pop(),lista2.pop()]
        return (cruzarListas(lista1, lista2)) + lista
    elif(len(lista1) == 1):
        return [lista1.pop(),lista2.pop()]

lista1 = [1,2,3,4]
lista2 = [9,8,7,6]
print(cruzarListas(lista1, lista2))