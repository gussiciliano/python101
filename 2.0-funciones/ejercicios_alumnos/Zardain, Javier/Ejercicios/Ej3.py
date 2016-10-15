'''
Created on 5/9/2016

@author: Javier_Zardain

Dado una lista de numeros de 0 a 100 obtener los numeros que esten por debajo de 50 tal cual estan y los que no deberan ser multiplicados por 2.
'''

print([x for x in range(100) if x < 50])
print([x*2 for x in range(100) if x > 50])