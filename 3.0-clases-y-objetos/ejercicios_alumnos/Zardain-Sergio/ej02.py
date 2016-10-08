# -*- coding: utf-8 -*-
from auto import Auto

'''
    @note: Con auto.py hacer un programa que haga acelerar el auto a 100 km por hora, luego frenarlo y apagarlo.
'''

if __name__ == "__main__":
    miAuto = Auto(True,True)
    
    for i in range(1,101):
        miAuto.acelerar() 
    
    for i in range(1,101):
        miAuto.frenar()
         
    miAuto.apagar()