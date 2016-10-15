'''
Created on 8/9/2016

@author: javier_zardain

Dada una lista de numeros enteros y un numero entero n,revertir la lista n veces y retornar cada elemento multiplicado por n
'''


def revertirLista(lista, veces, numero):
    if veces > 0:
        largo = len(lista)-1
        mitadLargo = int(largo/2)
        x = 0
        while x < mitadLargo:
            aux = lista[x]
            lista[x] = lista[largo-x]
            lista[largo-x] = aux
            x += 1
        return revertirLista(lista, veces-1, numero)
    else:
        return  [x*numero for x in lista]

lista = [1,2,3,4,5,6,7,8,9]
numero = int(input("Introduzca un numero: "))   
print(revertirLista(lista, numero, numero))