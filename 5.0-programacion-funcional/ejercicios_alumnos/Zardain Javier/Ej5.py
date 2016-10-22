'''
Created on 21/10/2016

@author: javier_zardain

- Dada una lista de numeros enteros y un numero entero n,revertir la lista n veces y retornar cada elemento multiplicado por n
'''

def revertirYMultiplicar(numero,lista):
    for x in range(0,numero):
        listaRevertida = [lista[x] for x in range(len(lista)-1,-1,-1)]
    return list(map(lambda x: x * numero, listaRevertida))

lista = [1,2,3,4,5,6,7,8,9]
numero = int(input("Introduzca un numero: "))
print(revertirYMultiplicar(numero,lista))
