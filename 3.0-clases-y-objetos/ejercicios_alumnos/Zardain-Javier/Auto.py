'''
Created on Sep 10, 2016

@author: python
'''
# -*- coding: utf-8 -*-
class Auto:

    RUEDAS = 4

    def __init__(self, encendido=False, cinturonAbrochado=False):
        '''
        Constructor de Auto - Se ejecuta cuando hacemos Auto()
        Recordar que la instancia de auto la debemos guardar en algún lugar.
        '''
        self.encendido = encendido
        self.cinturonAbrochado = cinturonAbrochado
        self.velocidad = 0
        self.color = None

    def encender(self):
        '''
        Prende el auto
        '''
        self.encendido = True

    def apagar(self):
        '''
        Apaga el auto.
        '''
        self.encendido = False

    def estadoMotor(self):
        '''
        Nos dice cual es el estado actual del motor.
        '''
        print(self.encendido)

    def abrocharCinto(self, estado):
        '''
        Abrocha el cinturon de seguridad, recibe un booleano.
        '''
        self.cinturonAbrochado = estado

    def acelerar(self):
        if self.encendido and self.cinturonAbrochado:
            self.velocidad +=1
        self.velocimetro()

    def frenar(self):
        if not (self.velocidad == 0):
            self.velocidad -=1
        self.velocimetro()

    def pintar(self, color):
        self.color = color

    def velocimetro(self):
        print(self.velocidad)