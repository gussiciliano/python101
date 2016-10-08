#!/usr/bin/env python
# -*- coding: iso-8859-14 -*-

# Computar el número K ingresado! 4*sumatoria(-1)i+12i . Ayudita: la sumatoria va de 0 a K, en este caso i es el elemento del ciclo.

num1 = input("Ingrese un numero: ")
while(type(num1) is not int):
	print("No te pases de listo, dije que ingreses un NUMERO");
	num1 = input("Ingrese un numero: ")

acumulador = 0
calculo = 0
acumulador = 0
while(num1>0):
	calculo = -1 * num1 + 12*num1
	acumulador = acumulador + calculo
	num1 = num1 - 1
acumulador = 4 * acumulador
print("El resultado es: ")
print(acumulador)