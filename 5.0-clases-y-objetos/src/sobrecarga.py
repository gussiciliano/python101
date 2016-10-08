#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
class Vehiculo(object):
    def tipo(self):
        print("Dos ruedas")

class Material(object):
    def tipo(self):
        print("plástico")

class Moto(Vehiculo, Material):
    def modelo(self):
        print("Modelo 1")
        super(Moto, self).tipo()
        super().tipo()
        Material.tipo(self)
        Vehiculo.tipo(self)

class Bicicleta(Material, Vehiculo):
    def modelo(self):
        print("Modelo 2")
        super(Bicicleta, self).tipo()
        super().tipo()
        Material.tipo(self)
        Vehiculo.tipo(self)



print("---------- Prioridad Clases ------------")
print(Moto.__mro__)
print(Bicicleta.__mro__)
print("---------- para objeto 1 ------------")
objeto1 = Moto()
objeto1.modelo()
objeto1.tipo()
print("---------- para objeto 2 ------------")
objeto2 = Bicicleta()
objeto2.modelo()

'''
Nota: En python 3, la sintaxis se simplifica de super(ClaseHija,self).__init__() a
super().__init().
Nota: En python 3 podemos llamar al método de la case padre desde dentro de la clase
hija, directamente indicando el nombre de la clase padre de la cual queremos heredar, y
con notación de punto el nombre del método a utilizar:
Ejemplo: Vehiculo.tipo(self)
Mezclar ambos tipos de llamadas dentro de un código puede traer errores serios, sobre
todo al trabajar con __init__, por lo que NO se debe mezclar las dos variantes dentro de
un código.
'''

''' Ejemplo de mal uso: '''
# class Vehiculo(object):
#     def __init__(self):
#         print("Dos ruedas")
#         super(Vehiculo,self).__init__()
# class Material(object):
#     def __init__(self):
#         print("plástico")
#         super(Material,self).__init__()
# class Moto(Vehiculo, Material):
#     def __init__(self):
#         print("Modelo 1")
#         Vehiculo.__init__(self)
#         Material.__init__(self)
#
# objeto1 = Moto()

'''
Se corrige llamando un unico constructor padre de moto.
super().__init__()
'''
