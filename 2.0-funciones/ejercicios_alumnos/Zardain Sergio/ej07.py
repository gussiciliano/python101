#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ

@summary: Generar un conversor de centímetros a pulgadas
'''

def centimetroPulgada(centimetros):
    return round(centimetros / 2.54,2) #redondeo en 2 decimales

if __name__ == '__main__':
    centimetros = float(input("Escriba una cantidad de centimetros: "))
    print("Pulgadas: " + str(centimetroPulgada(centimetros)))