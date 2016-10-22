'''
Created on 13/9/2016

@author: javier_zardain
'''
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from Mundo import *
from Personajes import *

if __name__ == "__main__":
    mundo = Mundo()
    mundo.agregarPersonaje(Mago("Merlin"))
    mundo.agregarPersonaje(Guerrero("Heman"))
    mundo.agregarPersonaje(Mago("Saruman"))
    persona = Persona("Gil trabajador")
    persona.sueldo = 400
    persona.laburo = True
    mundo.agregarPersonaje(persona)
    mundo.moduloPrincipal()
    