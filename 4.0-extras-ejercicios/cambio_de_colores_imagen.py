#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

''' python3.5 -m pip install Pillow  biblioteca necesaria para usar PIL Image'''
from PIL import Image

if __name__ == "__main__":
    picture = Image.open("imagen_con_colores_alterados.png")
    pixelPossibleValues = [ (x,y) for x in range(picture.width) for y in range(picture.height)]

    for x,y in pixelPossibleValues:
       r,g,b = picture.getpixel( (x,y) )
       if not(r == 0x00) or not(g == 0x00) or not(b == 0x00):
           picture.putpixel( (x,y), (0xFF, 0xFF, 0xFF))

    picture.show()
