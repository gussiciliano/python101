#!/usr/bin/env python
# -*- coding: iso-8859-14 -*-

# Dado un numero ingresado por el usuario, dar la posibilidad al mismo de: generar su sumatoria o su factorial.

num1 = input("Ingrese un numero: ")
while(type(num1) is not int):
	print("No te pases de listo, dije que ingreses un NUMERO");
	num1 = input("Ingrese un numero: ")
acumulador = 0
print("Opciones:")
print("1 - Sumatoria")
print("2 - Factorial")

opcion = input("Ingrese una opcion: ")
while(opcion != 1 and opcion != 2):
	opcion = input("Ingrese una opcion: ")
	
if(opcion == 1):
	while(num1>0):
		acumulador = acumulador + num1
		num1 = num1 - 1
elif(opcion == 2):
	acumulador = num1
	num1 = num1 -1
	while(num1>0):
		acumulador = acumulador * num1
		num1 = num1 - 1
print("El resultado es: ")
print(acumulador)