#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ

@summary: Dado una lista de números enteros definir una nueva lista que indica la tupla numero-paridad(true/false)
'''

if __name__ == "__main__":
    print([(x, x%2) for x in range(10)] )

