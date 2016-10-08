# -*- coding: utf-8 -*-
'''
Escribir un programa que reciba texto, si es una fruta y es una banana o manzana indica "yummi", si no lo es dice "puajjj"
'''
fruta = str(input("Ingrese el nombre de una fruta:")).strip().lower()
#if fruta.find('banana') == 0 or fruta.find('manzana') == 0:
if "banana" in fruta or "manzana" in fruta:
    print("yummi")
else:
    print("puajjj")
