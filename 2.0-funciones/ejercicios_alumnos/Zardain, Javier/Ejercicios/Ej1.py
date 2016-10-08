'''
Created on 5/9/2016

@author: Javier_Zardain

Dado una lista de numeros enteros definir una nueva lista que indica la tupla numero-paridad(true/false)
'''

listaNumeros = [1,2,3,4,5,6,7,8,9]

listaNumerosBoolean=[x%2==0 for x in listaNumeros]

x = 0
lista = []
while x < len(listaNumeros):
    lista.append((listaNumeros[x], listaNumerosBoolean[x]))
    x += 1
print(lista)