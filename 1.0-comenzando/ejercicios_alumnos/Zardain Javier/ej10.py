#!/usr/bin/env python
# -*- coding: iso-8859-14 -*-

# Escribir un piedra, papel o tijera de 1 ronda.

from random import randint

matrizResultados = [[0,-1,1],[1,0,-1],[-1,1,0]]
opciones = {1:"Piedra", 2:"Papel", 3:"Tijera"}
respuestas = {1:"Ganaste esta vez.", -1:"En tu cara, perdiste!", 0:"Empatamos."}

print("1 - Piedra")
print("2 - Papel")
print("3 - Tijera")

opcion = input("Ingrese una opcion: ")
miOpcion = randint(1, 3)
resultado=(matrizResultados[opcion-1][miOpcion-1])

print("Vos: " + opciones[opcion])
print("Yo: " + opciones[miOpcion])
if(miOpcion == 1):
	print("La buena piedra, nada le gana!")

print(respuestas[resultado])
	