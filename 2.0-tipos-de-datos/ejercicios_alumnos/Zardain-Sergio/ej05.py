# -*- coding: utf-8 -*-
#Se debera generar un sistema que mantenga en memoria datos de una agenda.
#    - El programa mostrara las opciones> agregar, editar, borrar, mostrar y salir
#    agregar, agenda un contacto (email, telefono, nombre, domicilio, edad y dni)
#    editar, permite modificar cualquiera de los contactos seleccionando su email.
#    borrar, elimina un contacto.

from time import sleep

"""
    muestro el menú de la agenda de contactos con las opciones
"""
def mostrarMenu():
    print("*****************************")
    print("*** Agenda de Contactos *****")
    print("*****************************")
    print(" ")
    print("OPCIONES")
    print("             --> Agregar (1) ")
    print("             --> Editar (2) ")
    print("             --> Borrar (3) ")
    print("             --> Mostrar (4) ")
    print("             --> Salir (5) ")
    print(" ")
    return int(input("Ingrese alguna opción: "))

"""
    retorno un diccionario de persona cargado
"""
def cargarPersona():
    dicPersona = {}
    print(" ")
    dicPersona["email"] = raw_input("Ingrese Email: ")
    dicPersona["telefono"] = raw_input("Ingrese Telefono: ")
    dicPersona["nombre"] = raw_input("Ingrese Nombre: ")
    dicPersona["domicilio"] = raw_input("Ingrese Domicilio: ")
    dicPersona["edad"] = raw_input("Ingrese Edad: ")
    dicPersona["dni"] = raw_input("Ingrese DNI: ")
    return dicPersona

"""
    muestro los contactos contenidos dentro de la lista
"""
def mostrarContactos(listaAgenda):
    print(" ")
    print("Contactos Disponibles " + str(len(listaAgenda)))
    #recorre la lista
    for contacto in listaAgenda:
        print("Nombre: " + contacto["nombre"] + " Email: " + contacto["email"])


if __name__ == "__main__":
    flagSalida = False
    listaAgenda = []
    dicPersona = {}

    while(flagSalida==False):
            opciones = mostrarMenu()
            #agregar
            if opciones == 1:
                dicPersona = cargarPersona()
                listaAgenda.append(dicPersona)
            #editar
            elif opciones == 2:
                mostrarContactos(listaAgenda)
                print(" ")
                email = raw_input("Ingrese un email: ")

                for contactos in listaAgenda:
                    if email in contactos["email"]:
                        contactos = cargarPersona()
                    else:
                        print("No existe el email ingresado.")
            #borrar
            elif opciones == 3:
                mostrarContactos(listaAgenda)
                print(" ")
                email = raw_input("Ingrese un email: ")

                for contactos in listaAgenda:
                    if email in contactos["email"]:
                        listaAgenda.remove(contactos)
                    else:
                        print("No existe el email ingresado.")
            #mostrar
            elif opciones == 4:
                mostrarContactos(listaAgenda)
                sleep(2)
            else:
                flagSalida = True
