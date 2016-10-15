# -*- coding: utf-8 -*-
'''
Escribir un programa que reciba un número entero positivo, devolver la sumatoria de dicho número.
'''
i = int(input("Ingrese un número:"))
acumulador = 0
for j in range(i+1):
    print("acumulo: " + str(j))
    acumulador +=  j
print("la sumatoria es: " + str(acumulador))
