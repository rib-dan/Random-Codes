# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:54:08 2022

@author: dan_r
"""

import sys

input_string = sys.stdin.read()

tokens = input_string.split()

a = int(tokens[0])
b = int(tokens[1])

print(a+b)
