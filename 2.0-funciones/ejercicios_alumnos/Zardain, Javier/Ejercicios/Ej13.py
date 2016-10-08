'''
Created on 7/9/2016

@author: javier_zardain

- Calcular el Nesimo numero de fibbonacci.
'''

numero = input("Ingrese un numero: ")
numero = int(numero)


def calcularNumeroFibbonacci(a,b, lista):
    resultado = b + a
    a = b
    b = resultado
    lista.append(resultado)
    if(len(lista) < numero):
        calcularNumeroFibbonacci(a, b, lista)

a = 0
b = 1
lista = []
lista.append(a)
lista.append(b)
calcularNumeroFibbonacci(a, b, lista)  
print(lista)