# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 20:28:01 2022

@author: dan_r
"""

import sys
import time
import random


n = sys.stdin.readline()

sequence = sys.stdin.readline().split()

if int(n) > len(sequence):
    n = len(sequence)

first_number = 0
second_number = 0
#print(len(sequence))
for i in range(0,len(sequence)):
    #print(i)
    k = int(sequence[i])
    if k > first_number:
        first_number = k
#print(first_number, sequence)
sequence.remove(str(first_number))

for i in range(0,int(n)-1):
    k = int(sequence[i])
    if k > second_number:
        second_number = k

    
print(first_number*second_number)
        



