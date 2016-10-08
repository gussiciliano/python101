#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
Created on Jul 25, 2016

@author: zehemz
'''

def listarElementos(value = [1,1,1,1,1,1], *arg):
    print("Value:::::"+ str(value))
    for value in arg:
        print(value)

def argumentosLocos(**args):
        print(args)

if __name__ == '__main__':
    listarElementos(2,3,4,5,6, ["susana", "jorge", "ricardo"])
    argumentosLocos(a=1, b=2, c=3)
