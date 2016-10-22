'''
Created on Sep 10, 2016

@author: python

- Nos piden que la agenda pueda darme un conjunto de contactos que nacieron despues de cierta fecha (ej 1993).
- La agenda puede buscar contactos por iniciales y devolver los resultados posibles.
'''
# -*- coding: utf-8 -*-

import sys
from AgendaContactosModulo import AgendaContactos

class MiClase:
    if __name__ == "__main__":
        agenda = AgendaContactos()
        
        while(True):
            print("1-Agregar Contacto")
            print("2-Editar Contacto")
            print("3-Borrar Contacto")
            print("4-Mostrar Contactos")
            print("5-Mostrar Contacto despues de:")
            print("6-Buscar por iniciales")
            print("7-Enviar mail")
            print("8-Enviar mail despues de 1993")
            print("9-Edad de los contactos despues de 10 years")
            print("10-Cargar contactos de archivo txt")
            print("11-Salir")
            opcion =int(input("Ingrese una opcion: "))
            if(opcion == 1):
                agenda.agregarContacto()
            elif(opcion == 2):
                agenda.editarContacto()
            elif(opcion == 3):
                agenda.borrarContacto()
            elif(opcion == 4):
                agenda.mostrarContactos()
            elif(opcion == 5):
                agenda.mostrarContactosDespuesDe()
            elif(opcion == 6):
                agenda.buscarPorIniciales()  
            elif(opcion == 7):
                agenda.enviarMail()
            elif(opcion == 8):
                agenda.enviarMailsDespuesDe()
            elif(opcion == 9):
                agenda.edadDespuesDe10()
            elif(opcion == 10):
                agenda.cargarDeArchivoTxt()
            elif(opcion == 11):
                sys.exit()
# QuA  si lo ponemos  "MiClase" debajo del main e intentamos correr
#¿Cómo podemos resolverlo?