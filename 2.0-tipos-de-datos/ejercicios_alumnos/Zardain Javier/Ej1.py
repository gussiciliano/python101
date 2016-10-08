'''
Created on 29/8/2016

@author: javier_zardain

Escribir un listado de famosos en un archivo .py. Desde otro archivo mostrar por pantalla el listado de famosos numerados.
'''


import NombresFamosos

i = 1
for nombre in NombresFamosos.nombres:
    print(str(i) +" - " + nombre)
    i += 1