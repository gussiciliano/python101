#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
from auto import Auto

class AutoVolador(Auto):
    ALAS = 2
    def __init__(self):
        Auto.__init__(self)
        self.__enVuelo = False
        self.__altitud = 0

    def despegar(self):
        if not self.__enVuelo and self.cinturonAbrochado and self.encendido and self.velocidad > 100:
            self.__enVuelo = True
            self.__altitud = 500
            print("Vuela vuelaaa, no te hace falta equipaje!")
        elif self.__enVuelo:
            print("cómo despego si ya estoy volando?")
        elif not self.cinturonAbrochado:
            print("La seguriad es lo primero 404")
        elif not self.encendido:
            print("Seriusly? esta bien que soy moderno, pero prendeme.")
        elif self.cinturonAbrochado and self.encendido:
            self.acelerar()
            self.despegar()

    def aterrizar(self):
        self.__altitud = 0
        while self.velocidad >0:
            self.frenar()
