#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ

@summary: Escribir un programa que dado un diccionario (empleado-salario) indíque si este se encuentra 
por debajo del sueldo mínimo ($6000)
En caso de que lo esté, agregarlo a una lista para luego ser impresa por pantalla.
'''

if __name__== "__main__":
    dicEmpleado = {"empleado1":6500, "empleado2": 5000, "empleado3": 10000}
    listaSalarioMinimo =  [nombre for nombre,importe in dicEmpleado.items() if importe < 6000]
    print("***** Nomina de empleados debajo del mínimo *****")
    for empleados in listaSalarioMinimo:
        print("Nombre: " + empleados)
    