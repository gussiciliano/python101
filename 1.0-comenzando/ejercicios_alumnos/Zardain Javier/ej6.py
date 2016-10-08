#!/usr/bin/env python
# -*- coding: iso-8859-14 -*-

# Modificar el ejercicio anterior generando que únicamente sume números que sean múltiplos de 3, 5 o 7 hasta el número ingresado.

num1 = input("Ingrese un numero que sea multiplo de 3, 5 o 7: ")
while(type(num1) is not int):
	print("No te pases de listo, dije que ingreses un NUMERO");
	num1 = input("Ingrese un numero: ")
while(num1%3 != 0 and num1%5 != 0 and num1%7 !=0):
	print("El numero debe ser multiplo de 3, 5 o 7");
	num1 = input("Ingrese un numero multiplo de 3, 5 o 7: ")

acumulador = 0
while(num1>0):
		acumulador = acumulador + num1
		num1 = num1 - 1
print("El resultado es: ")
print(acumulador)