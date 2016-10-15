#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ
@summary: La agenda puede buscar contactos por iniciales y devolver los resultados posibles.
'''

from claseAgenda import Agenda

if __name__ == "__main__":
    #muestro un menú y cargo la opción
    miagenda = Agenda()
    miagenda.mostrarMenu()
    listaAgenda = miagenda.obtenerContactos()
    #solicito la inicial
    print(" ")
    print("CONTACTOS POR INICIALES")
    print(" ")
    inicial = str(input("Ingrese la inicial: "))

    listaContactos = [contacto for contacto in listaAgenda if contacto.nombre[0] == inicial]

    if len(listaContactos) == 0:
        print("No existen contactos con inicial " + inicial)
    else:
        for contacto in listaContactos:
            contacto.mostrarDatos()
