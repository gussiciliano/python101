'''
Created on 7/9/2016

@author: javier_zardain

- Escribir un programa que dado un diccionario (empleado-salario) indique si este se encuentra por debajo del sueldo minimo ($6000)
En caso de que lo este, agregarlo a una lista para luego ser impresa por pantalla.
'''
import random

nombres = ["Juan", "Martin", "Matias", "Edgardo", "Roberto", "Ivana", "Marina", "Liliana", "Eliana", "Isabel"]

salarioPorEmpleado={}

for nombre in nombres:
    salarioPorEmpleado[nombre]=random.randint(1,9)*1000

print("Los siguientes empleados cobran menos de $6000")
print({x:v for (x,v) in salarioPorEmpleado.items() if int(v) < 6000})
