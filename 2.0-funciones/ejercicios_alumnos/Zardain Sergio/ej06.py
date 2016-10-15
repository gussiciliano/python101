#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ

@summary: Definir una función que calcúle el área de un cuadrado. ¿Cómo la modificarías para que calcule el área de un rectangulo?
'''

def calculoArea(base, altura):
    if base < 0 or altura < 0:
        return 0
    if altura == 0:
        return base ** 2
    else:
        return base * altura

if __name__ == '__main__':
    base = float(input("ingresar la base: "))
    altura = float(input("ingresar la altura: "))
    
    print("Area Cuadrado: " + str(calculoArea(base,0)))
    print("Area Rectángulo: " + str(calculoArea(base, altura)))