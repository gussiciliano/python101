# -*- coding: utf-8 -*-
'''
SUPER HARD, vale 10 puntos para Griffindor: Escribir un piedra, papel o tijera de 1 ronda.
'''
import random
from time import sleep

print( "***** Piedra, papel o tijera (el mejor de 3 intentos) *****")
print (" ")
sleep(1)

#Funcion que realiza la lógica del juego
constanteIntentos = 3
intentos = 1
opcion = 0
juegosGanados = 0
juegosPerdidos = 0
#	1- Piedra
#	2- Papel
#	3- Tijera

#	0- Perdi con la CPU
#	1- Gané a la CPU
#	2- Empatamos

# [PIEDRA,PAPEL,TIJERA]
matrizJuego = [[2,0,1],[1,2,0],[0,1,2]]
matrizTexto = ["Piedra","Papel","Tijera"]

while intentos < constanteIntentos + 1:
    print("intento n°: " + str(intentos))
    print(" ")
    # Valido que haya ingresado una opcion correcta
    opcion = -1
    while(opcion != 0 and opcion != 1 and opcion != 2):
        opcion = int(input("¿Piedra(0), papel(1) o tijera(2)?: "))
    #PC, opción al azar
    sleep(1)
    azar = int(random.choice([0, 1, 2]))
    print("PC eligio: " + matrizTexto[azar])
    #Muestro el resultado
    if matrizJuego[opcion][azar] == 0:
        print("Resultado parcial: Perdiste.")
        juegosPerdidos += 1
    elif matrizJuego[opcion][azar] == 1:
        print("Resultado parcial: Ganaste.")
        juegosGanados += 1
    else:
        print("Resultado parcial: Empate.")
    #sumo los intentos
    sleep(1)
    print(" ")
    intentos += 1
print("PARTIDA TERMINADA")
print("el resultado es...")
sleep(2)
if juegosGanados > juegosPerdidos:
    print("Le ganaste a la PC por " + str(juegosGanados) + " a " + str(juegosPerdidos) + ", la suerte estuvo de tu lado esta vez")
elif juegosGanados == juegosPerdidos:
#teniendo en cuenta que la cantidad de intentos es una constante que puede variar
    print("Empataron, nadie se sacó ventaja")
elif juegosGanados < juegosPerdidos:
    print("Perdiste por " + str(juegosPerdidos) + " a " + str(juegosGanados) + ", la PC fue siempre superior!")
