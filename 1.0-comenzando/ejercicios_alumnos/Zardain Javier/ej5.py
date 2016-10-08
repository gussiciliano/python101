#!/usr/bin/env python
# -*- coding: iso-8859-14 -*-

# Escribir un programa que reciba un numero entero positivo, devolver la sumatoria de dicho numero.

num1 = input("Ingrese un numero entero positivo: ")
while(type(num1) is not int or num1 < 0):
	print("No te pases de listo, dije que ingreses un NUMERO ENTERO POSITIVO")
	num1 = input("Ingrese un numero entero positivo: ")

acumulador = 0
while(num1>0):
		acumulador = acumulador + num1
		num1 = num1 - 1
print("El resultado es: ")
print(acumulador)
