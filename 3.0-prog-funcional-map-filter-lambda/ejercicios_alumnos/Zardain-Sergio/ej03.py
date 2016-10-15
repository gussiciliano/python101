#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ
@summary: La agenda puede para todos sus contactos enviarles un email y marcarlos como SEND.
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
            contacto.enviarEmail()
