#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import listadoFamosos

x = 0
for fam in listadoFamosos.famosos:
	x = x + 1
	print(str(x) + " - " + fam)
