#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ
@summary: Clase Agenda con funcionalidad para agregar contactos
'''
import smtplib
from time import sleep
from datetime import datetime, time

class Contacto:
    email = ""
    telefono = ""
    nombre = ""
    domicilio = ""
    edad = 0
    dni = 0
    emailEnviado = False

    def cargar(self):
        print(" ")
        self.email = str(input("Ingrese Email: "))
        self.telefono = str(input("Ingrese Telefono: "))
        self.nombre = str(input("Ingrese Nombre: "))
        self.domicilio = str(input("Ingrese Domicilio: "))
        self.edad = int(input("Ingrese Edad: "))
        self.dni = int(input("Ingrese DNI: "))

    def mostrarDatos(self):
        print(self.obtenerDatos())
        sleep(2)

    def sumarAnios(self,anios):
        self.edad += anios

    def obtenerDatos(self):
        return "Nombre: " + self.nombre + " Email: " + self.email + " Edad: " + str(self.edad)

    def enviarEmail(self):
        print("..Enviando email a " + str(self.email))
        sleep(2)
        remitente = "Desde pythonTest <pythonTest@utnfra.com.ar>"
        destinatario = str(self.nombre) + " <" + str(self.email) + ">"
        asunto = "Ejercicio 3 - Python101"
        mensaje = "Email automático para: " + self.obtenerDatos()
        email = """From: %s
        To: %s
        MIME-Version: 1.0
        Content-type: text/html
        Subject: %s

        %s
        """ % (remitente, destinatario, asunto, mensaje)
        try:
            smtp = smtplib.SMTP('localhost')
            smtp.sendmail(remitente, destinatario, email)
            print("El email se ha enviado correctamente")
            self.emailEnviado = True
        except:
            print("""Error: el mensaje no pudo enviarse.
            Compruebe que sendmail se encuentra instalado en su sistema""")
            self.emailEnviado = False

class Agenda:
    def __init__(self):
        self.listaContactos = []

    def obtenerContactos(self):
        return self.listaContactos

    def mostrarMenu(self):
        opcion = 0
        while(opcion != 5):
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
            opcion = int(input("Ingrese alguna opción: "))

            if opcion == 1:
                self.cargarContactos()
            elif opcion == 2:
                self.cargarContactos()
            elif opcion == 3:
                self.borrarContactos()
            elif opcion == 4:
                self.mostrarContactos()


    def cargarContactos(self):
        contacto = Contacto()
        #carga datos en el objeto contacto
        contacto.cargar()
        #subo el contacto a la lista
        self.listaContactos.append(contacto)

    def editarContactos(self):
        self.mostrarContactos()
        print(" ")
        email = str(input("Ingrese un email: "))
        #recorro todos los contactos hasta que encuentro el que coincida
        for contacto in self.listaContactos:
            if email in contacto.email:
                contacto.cargar()
            else:
                print("No existe el email ingresado.")

    def borrarContactos(self):
        self.mostrarContactos()
        print(" ")
        email = str(input("Ingrese un email: "))
        #recorro todos los contactos hasta que encuentro el que coincida
        for contacto in self.listaContactos:
            if email in contacto.email:
                listaContactos.remove(contacto)
            else:
                print("No existe el email ingresado.")
    def mostrarContactos(self):
        print(" ")
        print("Contactos Disponibles " + str(len(self.listaContactos)))
        for contacto in self.listaContactos:
            contacto.mostrarDatos()
