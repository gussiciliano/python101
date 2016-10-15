#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
Created on 9 jul. 2016

@author: Lucas
'''

import pickle

if __name__ == '__main__':
    lista = [1,2,3,4,5]
    diccionario = {'nombre': 'lucas', 'apellido' : 'bais'}

    pickle.dump(lista, open("lista.p", "wb"))
    pickle.dump(diccionario, open("diccionario.p", "wb"))
    #¿Qué no está bueno de abrir así los archivos?
    nuevaLista = pickle.load(open("lista.p", "rb"))
    nuevoDic = pickle.load(open("diccionario.p", "rb"))
    #¿Qué no está bueno de abrir así los archivos?

    print(nuevaLista)
    print(nuevoDic)
