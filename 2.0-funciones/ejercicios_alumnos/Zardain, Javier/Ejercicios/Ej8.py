'''
Created on 7/9/2016

@author: javier_zardain

Generar un conversor de centimetros a pulgadas
'''



medida = input("Ingrese medida en centrimetros: ")
medidaEnPulgadas = lambda x: float(x) * 2.54
print( str(medidaEnPulgadas(medida)) + " pulgadas.")