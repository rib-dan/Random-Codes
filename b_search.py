# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:15:15 2022

@author: dan_r
"""

import sys
import math
import time
def b_search(vector, number):
    end = len(vector)-1
    start = 0
    step = math.floor(len(vector)/2)
    if number > vector[len(vector)-1] or number < vector[0]:
            return -1
    while vector[step] !=number:
        
        if number > vector[step]:
            start = step
            step = math.ceil((end - step)/2)+step
        else:
            end = step
            step = math.floor((step-start)/2)
        
        if end - start == 1 and vector[end] != number and vector[start] != number:
            return -1
    return(step)


if __name__ == '__main__':
    result = []
    n = sys.stdin.readline()
    n = int(n)
    vector = sys.stdin.readline().split()
    for i in range(0, len(vector)):
        vector[i]= int(vector[i])
    
    k = sys.stdin.readline()
    k = int(k)
    numbers = sys.stdin.readline().split()
    for i in numbers:
        result.append(b_search(vector, int(i)))
    print(*result)