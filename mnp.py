# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 14:56:05 2022

@author: dan_r
"""

import sys
import math
import time

def mnp(n):
    solved = []
    sum_n = 0
    n_copy = n
    i = 1
    while n-sum_n != 0:
        solved.append(i)
        
        sum_n = sum_n + i
        print(solved, sum_n)
        if sum_n > n:
            sum_n = sum_n - solved.pop(len(solved)-2)
        i+=1
    solved.reverse()
    
    return solved
    
        


if __name__ == '__main__':
    n = int(sys.stdin.readline())

        
    
    result = mnp(n)
    result.reverse()
    print(len(result))
    print(*result)

