'''
Created on 7/9/2016

@author: javier_zardain

Revertir una lista.
'''


def revertirLista(lista, indice=0):
    largo= len(lista)-1
    limite = int(largo/2)
    if(largo%2 ==0):
        limite +=1
    seguir =indice != limite
    if(seguir):
        aux = lista[indice]
        lista[indice] = lista[largo - indice]
        lista[largo - indice] = aux
        revertirLista(lista, indice+1)

lista = [1,2,3,4,5,6,7,8,9]    
revertirLista(lista)  
print(lista)