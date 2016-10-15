#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ

@summary: Generar una función que dado una medida en segundos imprima por pantalla cuanto tiempo falta 
(actual + segundos) en hs, minutos y segundos para dicha fecha.
A su vez, se deberá escribir un diccionario (que dicha función reciba por parámetro) 
donde se guardaran estos campos como "minutos faltantes, horas faltantes y segundos faltantes".
'''
from datetime import datetime, time

def convertirFecha(duracion):
    seconds = duracion.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    days = hours // 24
    return days, minutes, hours, seconds

def cuantoFalta(fecha,dicTiempo):
    tuplaFecha = convertirFecha(datetime.now() - fecha)
    dicTiempo[fecha] = str(tuplaFecha[0]) + " minutos faltantes," + str(tuplaFecha[1]) + " horas faltantes y " + str(tuplaFecha[2]) + " segundos faltantes"
    print(str(dicTiempo[fecha]))
    
if __name__ == '__main__':
    dia = input("Ingrese el día: ")
    mes = input("Ingrese el mes: ")
    anio = input("Ingrese el anio: ")
    fecha = datetime.strptime(anio + "-" + mes + "-" + dia, "%Y-%m-%d")
    dicTiempo = {}
    cuantoFalta(fecha,dicTiempo)
    
    