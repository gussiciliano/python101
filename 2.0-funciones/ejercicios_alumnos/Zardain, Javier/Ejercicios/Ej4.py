'''
Created on 5/9/2016

@author: Javier_Zardain

Dado un numero N entero entregar un generador que recorra todos los numeros pares <= a N.
'''

def generadorPares(n):
    num = 0
    while True:
        if(num%2 == 0 and num<=n):
            yield num
        num += 1

numero = input("Introduzca un numero: ")

for x in generadorPares(int(numero)):
    print(x)