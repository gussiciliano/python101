# -*- coding: utf-8 -*-
# Computar el número K ingresado! 4⋅∑(−1)i+12i . Ayudita: la sumatoria va de 0 a K, en este caso i es el elemento del ciclo.
i = int(input("Ingrese un número:"))
acumulador = 0
aux = 0
for j in range(i-1,-1,-1):
    aux = -1 * i + 12 * i
    acumulador += aux
print("el resultado es: " + str(acumulador))


