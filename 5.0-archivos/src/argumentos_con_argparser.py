#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
Created on 24 jul. 2016

@author: Lucas
'''

import os, argparse
defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k:v for k, v in vars(namespace).items() if v}
