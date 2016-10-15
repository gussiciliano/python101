#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
Created on 9 jul. 2016

lectura de argumentos
@author: Lucas
'''
import sys
import getopt

def parseArgs(arguments):
    if len(arguments) > 1:
        print(arguments)
        return True

    return False

def argumentOpt(arguments):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(arguments,"hi:o:",["ifile=","ofile="])
        print(opts, args)
    except getopt.GetoptError:
        print('argumentos.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('argumentos.py -i <inputfile> -o <outputfile>')
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg
        print('Input file is ', inputfile)
        print('Output file is ', outputfile)

if __name__ == '__main__':

    habiaArgumentos = parseArgs(sys.argv)

    if habiaArgumentos: #esto entra si no es None
        print("se leyeron argumentos correctamente")
        argumentOpt(sys.argv)
    else:
        print("No habia argumentos")
