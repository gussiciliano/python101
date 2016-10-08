#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
Created on 9 jul. 2016

@author: Lucas
'''
if __name__ == '__main__':

    name = str(input("ingrese su nombre:\n"))
    print(name)

    #name = str(raw_input("What is your name: "))
    #age = int(raw_input("How old are you: "))
    #year = str((2014 - age)+100)
    #print(name + " will be 100 years old in the year " + year)

    #On Python 2.x you need to be using raw_input() rather than input(). On the older version of Python, input() actually evaluates what you type as a Python expression, which is why you need the quotes (as you would if you were writing the string in a Python program).
    #There are many differences between Python 3.x and Python 2.x; this is just one of them. However, you could work around this specific difference with code like this:
    #try:
    #    input = raw_input
    #except NameError:
    #    pass
    # now input() does the job on either 2.x or 3.


    value = input("ingrese valor\n")
    print(value)

    # Ejercicio enteros
    print("Suma 3 + 2")
    suma = 3+2
    resta = suma - suma
    division = resta / suma
    print(division)
    division = suma / (suma - 1)
    print(division)
    division = float(suma) / (suma - 1)
    print(division)

    multilinea = """este es un ejemplo
    con multiples lines
    lo pueden ver"""
    print(multilinea)
    value = 65
    multilinea = """este es otro ejemplo
    de multilinea con una variable """+str(value)+""" y puedo
    seguir escribiendo!"""
    print(multilinea)
