#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ
@summary: La agenda puede integrar las funcionalidades y permitir: mandar mail a todas las personas que nacieron despues de 1993.
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
            contacto.enviarEmail()
