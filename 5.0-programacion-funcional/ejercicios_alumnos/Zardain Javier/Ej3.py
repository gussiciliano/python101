'''
Created on 21/10/2016

@author: javier_zardain

- Calcular el Nesimo numero de fibbonacci. 
'''
def calcularNumFibonacci(numero):
    faltan = len([x for x in numero if x == None])
    if(faltan == len(numero)):
        numero[0] = 0
        numero[1] = 1
        return calcularNumFibonacci(numero)
    elif(faltan > 0):
        indice = len(numero) - faltan
        numero[indice] = numero[indice - 1] + numero[indice - 2]
        return calcularNumFibonacci(numero)
    else:
        return numero

numero = [None] * int(input("Ingrese el numero para realizar el calculo: "))
print("El numero de fibonacci es: " + str(calcularNumFibonacci(numero)))