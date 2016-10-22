'''
Created on 20/10/2016

@author: javier_zardain

Dado una lista de numeros enteros definir una nueva lista que indica la tupla numero-paridad(true/false)
'''

listaNumeros = [1,2,3,4,5,6,7,8,9]

listaNumerosBoolean=[(x,x%2==0) for x in listaNumeros]

print(listaNumerosBoolean)