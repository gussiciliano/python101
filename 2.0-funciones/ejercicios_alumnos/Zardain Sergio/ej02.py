#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ

@summary: Dado una lista de números de 0 a 100 obtener los números que esten por debajo de 50.
'''

if __name__ == "__main__":
    listaNumeros = list(x for x in [x for x in range(101)] if x < 50)
    print(listaNumeros)
