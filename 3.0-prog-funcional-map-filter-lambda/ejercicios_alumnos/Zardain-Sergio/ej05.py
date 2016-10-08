#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ
@summary: Calcular para todos los contactos de la agenda que edad tendrán dentro de 10 años.
'''

from claseAgenda import Agenda

if __name__ == "__main__":
    #muestro un menú y cargo la opción
    miagenda = Agenda()
    miagenda.mostrarMenu()
    listaAgenda = miagenda.obtenerContactos()
    listaContactos = [contacto for contacto in listaAgenda]

    if len(listaContactos) == 0:
        print("No existen contactos")
    else:
        for contacto in listaContactos:
            contacto.sumarAnios(10)
            contacto.mostrarDatos()
