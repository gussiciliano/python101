'''
Created on 12/9/2016

@author: javier_zardain
'''
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from Personajes import *
import random
import time

class Mundo:
    
    def __init__(self):
        self.personajes = set()

    def recorrerPersonajes(self, evitar=None):
        x = 1
        for personaje in self.personajes:
            if(personaje != evitar):
                print(str(x) + " - " + personaje.nombre)
            x += 1
    
    def obtenerPersonajePorIndice(self,indice):
        x = 1
        for personaje in self.personajes:
            if(x == indice):
                return personaje
            x += 1
        return None
    
    def agregarPersonaje(self,personaje):
        self.personajes.add(personaje)
    
    def eliminarPersonaje(self):
        self.recorrerPersonajes()
        opcion = int(input("Seleccione el personaje a eliminar: "))
        self.personajes.remove(self.obtenerPersonajePorIndice(opcion))
        
    def listarPersonajes(self):
        for personaje in self.personajes:
            print("--------------")
            print("Nombre: " + personaje.nombre)
            print("Clase: " + personaje.clase)
            print("Atributos: " + str(personaje.atributos))
            print("--------------")
        
    def listarLaburantes(self):
        for personaje in self.personajes:
            if(personaje.clase == "Persona"):
                if(personaje.laburo):
                    print("--------------")
                    print("Nombre: " + personaje.nombre)
                    print("Atributos: " + str(personaje.atributos))
                    print("Sueldo: " + str(personaje.sueldo))
                    print("--------------")
        
        
    def nuevoPersonaje(self):
        nombre = input("Ingrese el nombre del personaje: ")
        print("1 - Guerrero")
        print("2 - Mago")
        print("3 - Persona")
        clase = int(input("Seleccione la clase del personaje: "))
        if(clase == 1):
            personaje = Guerrero(nombre)
        elif(clase == 2):
            personaje = Mago(nombre)
        else:
            personaje = Persona(nombre)
            personaje.inicializar()
        self.agregarPersonaje(personaje)
    
    def entrenarPersonaje(self):
        self.recorrerPersonajes()
        opcion = int(input("Seleccione el personaje para entrenar: "))
        personaje = self.obtenerPersonajePorIndice(opcion)
        personaje.sumarExperiencia(10)
         
    def gestionPersonajes(self):
        opciones = [self.nuevoPersonaje,self.eliminarPersonaje,self.listarPersonajes, self.listarLaburantes]
        print("1 - Agregar Personajes")
        print("2 - Eliminar Personajes")
        print("3 - Listar Personajes")
        print("4 - Listar Laburantes")
        opcion = int(input("Seleccione una opcion: ")) -1
        opciones[opcion]()
    
    def correrCarreraOlimpica(self):
        primerPuesto = 0
        podioPrimero = ""
        segundoPuesto = 0
        podioSegundo = ""
        tercerPuesto = 0
        podioTercero = ""
        for personaje in self.personajes:
            perfomance = personaje.velocidadCorrer * random.randint(1,5)
            if(perfomance > primerPuesto):
                podioPrimero = personaje.nombre
                primerPuesto = perfomance
            elif(perfomance > segundoPuesto):
                podioSegundo = personaje.nombre
                segundoPuesto = perfomance
            elif(perfomance > tercerPuesto):
                podioTercero = personaje.nombre
                tercerPuesto = perfomance
        print("Primer puesto: " + podioPrimero)
        print("Segundo puesto: " + podioSegundo)
        print("Tercer puesto: " + podioTercero)

    def pelear(self):
        self.recorrerPersonajes()
        opcion = int(input("Seleccione el primer personaje para pelear: "))
        personaje1 = self.obtenerPersonajePorIndice(opcion)
        self.recorrerPersonajes(personaje1)
        opcion2 = int(input("Seleccione el segundo personaje para pelear: "))
        personaje2 = self.obtenerPersonajePorIndice(opcion2)
        print("Va a pelear " + personaje1.nombre + " contra " + personaje2.nombre)
        while(True):
            personaje2.recibirDamage(personaje1.atacar())
            if(personaje2.vida <= 0):
                print(personaje2.nombre + " ha muerto!")
                print(personaje1.nombre + " ha ganado la pelea.")
                break;
            personaje1.recibirDamage(personaje2.atacar())
            if(personaje1.vida <= 0):
                print(personaje1.nombre + " ha muerto!")
                print(personaje2.nombre + " ha ganado la pelea.")
                break;
        personaje1.vida = 100
        personaje2.vida = 100
        
    def mandarAlaAfip(self):
        for personaje in self.personajes:
            if(personaje.clase == "Persona"):
                if(personaje.leCaeLaAfip):
                    print("A " + personaje.nombre + " le cayo la AFIP.")
        
    def moduloPrincipal(self):
        while(True):
            opciones = [self.gestionPersonajes,self.entrenarPersonaje,self.pelear,self.correrCarreraOlimpica, self.mandarAlaAfip]
            print("1 - Gestion de personajes")
            print("2 - Entrenar personaje")
            print("3 - Pelear")
            print("4 - Correr carrera olimpica")
            print("5 - Mandar a la AFIP")
            opcion = int(input("Seleccione una opcion: ")) -1
            opciones[opcion]()