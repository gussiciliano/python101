'''
Created on 31/8/2016

@author: javier_zardain
- Dada una cadena de texto de 10 a 20 caracteres ingresada por el usuario quedarse con los primeros 3 y los ultimos 5.
'''

if __name__ == "__main__":
    texto = input("Ingrese un texto de 10 a 20 caracteres: ")
    while(len(texto) < 10 or len(texto) > 20):
        texto = input("Ingrese un texto de 10 a 20 caracteres: ")
    print(texto[:3] + texto[len(texto)-5:])