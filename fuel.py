# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:18:18 2022

@author: dan_r
"""


import sys
import time

def fuel(d, m, n, list_fuel):
    position = 0
    i = 0
    stops = 0
    list_fuel.sort()
    #print(list_fuel)
    n = len(list_fuel)
    if m-d>=0:
        return 0
    if n < len(list_fuel):
        return -1

    if int(list_fuel[n-1])+m < d:
        
        return -1
    while position < d:
        while m+position>=int(list_fuel[i]) and i < len(list_fuel)-1:
            i += 1
        stops += 1  
        if position != int(list_fuel[i-1]):
            position = int(list_fuel[i-1])
        else:
            position = int(list_fuel[i])
        if position + m < int(list_fuel[i]):
            return -1
            
        if position + m >= d:
            position = d
                 
        
    return stops
 


if __name__ == '__main__':
    d = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    list_fuel1 = sys.stdin.readline().split()
    while len(list_fuel1) != n:
        list_fuel1 = list_fuel1 + sys.stdin.readline().split()
    #print(list_fuel1)
    list_fuel = [0]
    for i in range(0, len(list_fuel1)):
        list_fuel.append(int(list_fuel1[i]))
    list_fuel.append(d)
    
    print(fuel(d, m, n, list_fuel))