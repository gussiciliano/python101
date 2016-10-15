# -*- coding: utf-8 -*-
'''
Modificar el ejercicio anterior generando que únicamente sume números que sean múltiplos de 3, 5 o 7 hasta el número ingresado.
'''
acumulador = 0
i = int(input("Ingrese un número:"))
for j in range(i+1):
    if j % 3 == 0 or j % 5 == 0 or j % 7 == 0:
        print("acumulo: " + str(j))
        acumulador += j
print("la sumatoria es: " + str(acumulador))
