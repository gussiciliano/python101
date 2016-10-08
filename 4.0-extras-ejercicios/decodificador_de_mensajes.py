#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
''' Resolución de ejercicio mensaje codificado'''
import os
import shutil

if __name__ == "__main__":
    #https://docs.python.org/3/library/os.html
    #Directorio en el que estoy parado:
    print("Estoy en: "+ os.getcwd())
    #Me muevo a otro directorio (no es estrictamente necesario)
    os.chdir(os.path.join(os.getcwd(), 'message'))
    #listo los dirs
    print(os.listdir(os.getcwd()))
    #Creamos el dir.
    if not os.path.exists(os.path.join(os.getcwd(), 'result')):
        os.mkdir('result')
    for filename in os.listdir(os.getcwd()):
        if not filename == 'result':
            #Copio los archivos.
            toTranslate = {ord('-') : ""}
            for i in "0123456789":
                toTranslate[ord(i)] = ""
            modifiedName = filename.translate(toTranslate)
            shutil.copy(os.path.join(os.getcwd(),filename), os.path.join(os.getcwd(),'result',modifiedName))
