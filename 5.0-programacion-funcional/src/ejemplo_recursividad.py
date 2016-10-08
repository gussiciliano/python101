#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
Created on Jul 25, 2016
http://cscircles.cemc.uwaterloo.ca/16-recursion/
@author: zehemz
'''

'''
{-Escribir una funcion doblefact para calcular n!! = n (n − 2)(n − 4) . . . 2. Por ejemplo: doblefact 10 􏰻 10∗8∗6∗4∗2 􏰻 3840.
La funcion se debe indefinir para los numeros impares.-}

{- Escribir una funcion recursiva que no termine si se la ejecuta con numeros
negativos (y en cambio si termine para el resto de los numeros). -}

{- Escribir una funcion que dado n ∈ N sume los numeros impares
positivos cuyo cuadrado sea menor que n.
Por ejemplo: sumaImparesCuyoCuadSeaMenorQue 30 􏰻 1 + 3 + 5 ->9  -}

enBase :: Integer -> Integer -> [Integer]
enBase valor base | valor < base = [valor]
                  | otherwise = enBase (div valor base) base ++ [mod valor base]


deBase :: [Integer] -> Integer -> Integer
deBase lista base | (length lista) == 1 = head lista
                  | otherwise = head lista * base^((length lista)-1) + deBase (tail lista) base

reverso :: [a] -> [a]
reverso lista | length lista == 0 = []
              | otherwise = reverso (tail lista) ++ [head lista]

esCapicua :: [Integer] -> Bool
esCapicua lista = lista == (reverso lista)

'''

def sumatoria(lista):
    if len(lista) == 0:
        return 0
    print(lista)
    return lista.pop() + sumatoria(lista)

def countdown(n):
  print('Entering countdown(',n,')')
  if n == 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n - 1)
  print('Exiting from countdown(',n,')')

'''
Ejemplo max deepth
def countdownBy2(n):
  if n == 0:
    print('Blastoff!')
  else:
    print(n)
    countdownBy2(n - 2)

countdownBy2(5)
'''

if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8]
    sumatoria(lista)
    countdown(5)
