#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
Escribir un listado de famosos en un archivo .py.
Desde otro archivo mostrar por pantalla el listado de famosos numerados.
'''
from ej01_constantes import famosos

if __name__ == "__main__":
    contador = 0
    for x in famosos:
        print(x + " - posicion " + str(contador))
        contador += 1
