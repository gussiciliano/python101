#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from auto import Auto
from auto_volador import AutoVolador
if __name__ == '__main__':
    # Instanciamos e imprimimos el objeto de la clase Auto
    objeto = Auto()
    print(objeto.color)

    print(objeto.encendido)
    # Imprimimos los métodos de la clase Auto
    print(dir(Auto))
    # Vemos cual es su clase padre
    print(Auto.__class__.__base__)
    # Vemos si es un objeto de alguna clase
    print(Auto.__class__)

    autoVolador = AutoVolador()
    print(dir(autoVolador))

    autoVolador.encender()
    autoVolador.abrocharCinto(True)
    autoVolador.acelerar()
    autoVolador.acelerar()

    #
