#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ

@summary: Revertir una lista.
'''

def invertir(lista):
    listaInvertida = []
    for i in range(len(lista) - 1,-1,-1):
        if type(lista[i]) is list:
            listaInvertida.append(invertir(lista[i]))
        else:
            listaInvertida.append(lista[i])
    return listaInvertida

if __name__ == "__main__":
    lista = [1,2,[0,3,4,5],[5,55]]
    lista = invertir(lista)
    print(lista)  
        