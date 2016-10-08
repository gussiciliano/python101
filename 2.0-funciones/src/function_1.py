#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
Created on Jul 25, 2016

@author: zehemz
'''

'''
¿Podes explicar que sucede con la función armarLista?
'''


def sumarUno(valor):
    valor +=1
    return valor

def agregarPrefijo(valor, text):
    return ( str(valor) + " - " + text )

def saludar():
    print("Hola! soy una función!")

def armarLista(textoBase, cantidadDeElementos):
    lista = []
    for valor in range(cantidadDeElementos):
        texto = agregarPrefijo(sumarUno(valor), textoBase)
        lista.append(texto)

    print(lista)


if __name__ == '__main__':
    saludar()
    armarLista(cantidadDeElementos=100,textoBase="Elemento")
