#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
Created on Jul 25, 2016

@author: zehemz
'''


'''
 Analizar el siguiente código:
¿Que hace?
¿Por qué no funciona?
¿Qué diferencia hay entre saludar, sumarUno y agregarPrefijo?
'''

def saludar():
    print("Hola! soy una función!")


if __name__ == '__main__':

    saludar()

    lista = []

    for valor in range(5):
        texto = agregarPrefijo(sumarUno(valor), "Base")
        lista.append(texto)

    print(lista)


def sumarUno(valor):
    valor +=1
    return valor

def agregarPrefijo(valor, text):
    return ( str(valor) + " - " + text )
