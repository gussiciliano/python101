'''
Created on 20/10/2016

@author: javier_zardain

- Dado una lista de numeros calcular la sumatoria de dicho numero.
'''
lista = [1,2,3,4,5,6,7,8,9]

def calcularSumatoria(lista):
    if(len(lista) > 1):
        return lista.pop()+calcularSumatoria(lista)
    elif(len(lista) == 1):
        return lista.pop()

print("La sumatoria de " + str(lista) + " es: " + str(calcularSumatoria(lista)))