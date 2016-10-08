'''
Created on 5/9/2016

@author: Javier_Zardain

Definir una funcion que calcule el area de un cuadrado. Como la modificarias para que calcule el area de un rectangulo?
'''

def areaCuadrado():
    lado = int(input("Ingrese la medida del lado: "))
    return lado*lado

def areaRectangulo():
    base = int(input("Ingrese la medida de la base: "))
    altura = int(input("Ingrese la medida de la altura: "))
    return base * altura


print("1 - Area de un cuadrado")
print("2 - Area de un rectangulo")
opcion = int(input("Ingrese una opcion: "))
if(opcion == 1):
    print("El area es: " + str(areaCuadrado()))
elif(opcion==2):
    print("El area es: " + str(areaRectangulo()))