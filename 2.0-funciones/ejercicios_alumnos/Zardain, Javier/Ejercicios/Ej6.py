'''
Created on 5/9/2016

@author: Javier_Zardain

- Dado un numero, generar una funcion que indique si dicho numero es primo o no lo es.
'''

def esPrimo(numero):
    i = 1
    numero = int(numero)
    divididoUnaVez = False
    while i<numero:
        if(numero%i==0):
            if(not divididoUnaVez):
                divididoUnaVez = True
            else:
                return False
        i+=1
    return True

numero = input("Ingrese un numero: ")

if(esPrimo(numero)):
    print("El numero ingresado es primo.")
else:
    print("El numero ingresado no es primo.")