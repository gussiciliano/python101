#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
Created on 24 jul. 2016

@author: Lucas
'''

import time
import webbrowser

REPETITION_BREAK_TIME = 10 * 1 * 1
HOW_MANY_TIMES = 3

if __name__ == '__main__':
    '''El objetivo es detectar cuando han pasado X horas desde el inicio de ejecución para tomar un descanzo.'''
    counter = 0
    while counter < HOW_MANY_TIMES:
        counter +=1
        time.sleep(REPETITION_BREAK_TIME)
        webbrowser.open('https://www.youtube.com/watch?v=12vh55_1ul8')
        input("BREAK TIME! press enter")
