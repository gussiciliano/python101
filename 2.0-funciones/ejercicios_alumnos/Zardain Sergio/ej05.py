#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ

@summary: Dado un número, generar una función que indique si dicho número es primo o no lo es.
'''

def esNumeroPrimo(numero):
    if numero < 2:
        return False    
    for x in range(2, numero):
        if numero % x == 0:
            return False
    return True 
            
if __name__ == "__main__":
    numeroN = int(input("ingresar número: "))
    listaNroPrimo = list(x for x in [x for x in range(2,numeroN)] if numeroN % x == 0) 
    if len(listaNroPrimo) == 0:
        print("Primo")
    else:
        print("No primo")
    
    #resolución utilizando funciones
    #if esNumeroPrimo(numeroN):
    #    print("Es un numero primo")
    #else:
    #    print("No es un numero primo")       
            
