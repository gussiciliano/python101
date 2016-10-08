#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import sys
import datetime

try:
    from ctypes import cdll
except ImportError:
    print("ERROR")
    sys.exit(-1)

a = datetime.datetime.now()
cdll.LoadLibrary("./build/helloLib.so").executeWork()
b = datetime.datetime.now()
print(b-a)
