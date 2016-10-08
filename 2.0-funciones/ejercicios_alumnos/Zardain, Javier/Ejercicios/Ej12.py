'''
Created on 7/9/2016

@author: javier_zardain

- Dado una lista de numeros calcular la sumatoria de dicho numero.
'''

lista = [1,2,3,4,5,6,7,8,9]

def calcularSumatoria(lista,indice = 0):
    x = 0
    sumatoria = 0
    while(x < indice):
        sumatoria = sumatoria + lista[x]
        x += 1
    print("La sumatoria de " + str(indice) + " es " + str(sumatoria))
    if(indice < len(lista)):
        calcularSumatoria(lista,indice+1)


calcularSumatoria(lista)
        