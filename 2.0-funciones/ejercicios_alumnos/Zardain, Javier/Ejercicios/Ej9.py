'''
Created on 7/9/2016

@author: javier_zardain

Generar una funcion que dado una medida en segundos imprima por pantalla cuanto tiempo falta (actual + segundos) en hs, minutos y segundos para dicha fecha.
A su vez, se debera escribir un diccionario (que dicha funcion reciba por parametro) donde se guardaran estos campos como "minutos faltantes, horas faltantes y segundos faltantes".
'''
import datetime

def quitarDecimales(numero):
    numero = str(numero)
    return int(numero[:numero.index(".")])

def quitarEnteros(numero):
    return numero[numero.index("."):]

def horaResultante(horaActual, horas, minutos, segundos):
        horaActual[2] = int(horaActual[2]) + segundos
        if(horaActual[2] >= 60):
            horaActual[1] = quitarDecimales(horaActual[2]/60) + int(horaActual[1])
            horaActual[2] = horaActual[2] - 60 
        horaActual[1] = int(horaActual[1]) + minutos
        if(horaActual[1] >= 60):
            horaActual[0] = quitarDecimales(horaActual[1]/60) + int(horaActual[0])
            horaActual[1] = horaActual[1] - 60 
        horaActual[0] = int(horaActual[0]) + horas
        while(horaActual[0] > 24):
            horaActual[0] = horaActual[0] - 24
        return horaActual
    
def cuantoFalta(segundos, tiempo):
    horaActual=str(datetime.datetime.now().time()).split(":",2)
    horaActual[2] = quitarDecimales(horaActual[2])
    segundos = int(segundos)
    
    horas = quitarDecimales(segundos/3600)
    segundos = segundos - 3600 * horas
    minutos = quitarDecimales(segundos/60)
    segundos = segundos - 60*minutos
    tiempo = {"horas_faltantes":horas, "minutos_faltantes":minutos, "segundos_faltantes":segundos}
    
    print("Son las " + str(horaActual[0]) + " horas " + str(horaActual[1]) + " minutos " + str(horaActual[2]) + " segundos")
    print("Faltan " + str(horas) + " horas, " + str(minutos) + " minutos, " + str(segundos) + " segundos")
    horaActual = horaResultante(horaActual, horas, minutos, segundos)
    print("Para las " + str(horaActual[0]) + " horas " + str(horaActual[1]) + " minutos " + str(horaActual[2]) + " segundos") 
    print(tiempo)


if __name__ == "__main__":
    segundos = input("Ingrese segundos: ")
    tiempo = {}
    cuantoFalta(segundos, tiempo)