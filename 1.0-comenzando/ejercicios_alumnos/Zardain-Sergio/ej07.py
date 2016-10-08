# -*- coding: utf-8 -*-
from time import sleep
'''
Dado un numero ingresado por el usuario, dar la posibilidad al mismo de: generar su sumatoria o su factorial.
'''
print("Calculo Factorial: Opcion 1")
print("Calculo Sumatoria: Opcion 2")
sleep(1)
opcion = 0
intentos = 1
while(opcion != 1 and opcion != 2):
    if intentos <= 2:
        opcion = int(input("Señor usuario, que opción prefiere (1 o 2)?: "))
    elif intentos > 2 and intentos < 5:
        opcion = int(input("Vamos...no es dificil Señor usuario, que opción prefiere (1 o 2)?: "))
    else:
        opcion = int(input("...que opción prefiere (1 o 2)?: "))
    intentos += 1
sleep(1)
print(" ")
numero = int(input("Ingrese un número:"))

#instancio las variables
x = 0
y = 0
fac = 0
acumulador = 0

#bifurcación a pedido del usuario...
if opcion == 1:
    # Cálculo de Factorial
    for x in range(numero):
        fac=1
        for y in range(1,x+1):
            #print("numero: " + str(y))
            fac=fac*y
    print("Factorial: " + str(fac))
else:
    # Cálculo de Sumatoria
    for x in range(numero):
        #print("numero: " + str(x))
        acumulador += x
    print("Sumatoria: " + str(acumulador))
