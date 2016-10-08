#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ

@summary: Dado una lista de numeros calcular la sumatoria de dicho número.
'''
def calcularSumatoria(valor):
    sumatoria = 0
    if type(valor) is list:
        for item in valor:
            sumatoria += calcularSumatoria(item)
        return sumatoria
    else:   
        for i in range(valor):
            sumatoria += i
        return sumatoria    

if __name__== "__main__":
    listaNumeros = [5,4,10,2,3]
    calcular = calcularSumatoria(listaNumeros)
    print(str(calcular))
