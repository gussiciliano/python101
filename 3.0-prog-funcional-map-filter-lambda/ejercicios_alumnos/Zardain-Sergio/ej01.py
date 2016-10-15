#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ
@summary: Nos piden que la agenda pueda darme un conjunto de contactos que nacieron después de cierta fecha (en años, ej 1993).
'''

from claseAgenda import Agenda
from datetime import datetime, time

if __name__ == "__main__":
    #muestro un menú y cargo la opción
    miagenda = Agenda()
    miagenda.mostrarMenu()
    listaAgenda = miagenda.obtenerContactos()
    #solicito la edad
    print(" ")
    print("CONTACTOS POR EDAD")
    print(" ")
    anio = int(input("Ingrese el año: "))
    edad = datetime.now().year - anio
    listaContactos = [contacto for contacto in listaAgenda if contacto.edad > edad]

    if len(listaContactos) == 0:
        print("No existen contactos mayores a la edad de " + str(edad))
    else:
        for contacto in listaContactos:
            contacto.mostrarDatos()
