# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:36:42 2022

@author: dan_r
"""

import sys
import math

def isGreaterorEqual(dig, maxDig):
    if dig+maxDig >= maxDig+dig:
        return True
    else:
        return False
    
def greatest_integer(n, i_list):
    maxDig = '0'
    copy_list = i_list.copy()
    result =''
    
    while len(copy_list)>0:
        i=0
        for i in range(0, len(copy_list)):
            if isGreaterorEqual(copy_list[i], maxDig) == True:
                maxDig = copy_list[i]
        result += maxDig
        copy_list.remove(maxDig)
        maxDig='0'
        
    
    return result
    
        


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    i_list = sys.stdin.readline().split()
    result = greatest_integer(n, i_list)
    print(result)