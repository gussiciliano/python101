# -*- coding: utf-8 -*-
# Dada una cadena de texto de 10 a 20 caracteres ingresada por el usuario quedarse con los primeros 3 y los ultimos 5.

if __name__ == '__main__':
    while(True):
        cadena = raw_input("Ingrese una palabra de 10 a 20 caracteres: ")
        if len(cadena) >= 10 and len(cadena) <= 20:
            break
        else:
            print("Error, reingrese")
            print(" ")

    #muestro los 3 primeros y los 5 ultimos caracteres
    print("3 primeros caracteres: " + cadena[0:3])
    print("5 ultimos caracteres: " + cadena[-5:])
