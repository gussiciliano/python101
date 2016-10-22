'''
Created on Sep 10, 2016

@author: python
'''
# -*- coding: utf-8 -*-

from Auto import Auto


if __name__ == "__main__": 
    class MiClase:
        def manejarAuto(self):
            auto = Auto()
            auto.abrocharCinto(True)
            auto.encender()
            while(auto.velocidad != 100):
                auto.acelerar()
            while(auto.velocidad != 0):
                auto.frenar()
            auto.apagar()
            
    clase = MiClase()
    clase.manejarAuto()
# QuA  si lo ponemos  "MiClase" debajo del main e intentamos correr
#¿Cómo podemos resolverlo?