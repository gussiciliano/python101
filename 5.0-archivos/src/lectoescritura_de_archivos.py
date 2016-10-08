#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
Created on 9 jul. 2016

@author: Lucas
'''

if __name__ == '__main__':

    '''Ejemplo write'''
    file = open("write.txt",'w+')
    file.write("texto")
    file.close()
    '''Ejemplo read'''
    file = open("write.txt", "r+")
    textFile = file.read()
    print(textFile)
    file.close()
