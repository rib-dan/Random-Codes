# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:36:23 2022

@author: dan_r
"""

import sys
import math
import time
import random

def count(vector, left, right, majority):
    count = 0
    for i in range(left, right):
        if vector[i] == majority:
            count += 1
    return count

def majority(vector):
    res,_ = majority_internal(vector, 0, len(vector))
    count = 0

    for i in vector:
        if i == res:
            count +=1
    if count > len(vector)/2:
        return 1
    else:
        return 0

def majority_internal(vector, left, right):
    if left+1 == right:
        return vector[left], 1
    
    mid = left + math.floor((right - left)/2)
    maj1, count1 = majority_internal(vector, left, mid)
    maj2, count2 = majority_internal(vector, mid, right)
    if maj1 == maj2:
        return maj1, count1+count2
    
    if count1 > count2:
        return maj1, count1
    else:
        return maj2, count2
    
    return result

def majority_naive(vector):
    max_ap = 0
    
    for i in range(0, len(vector)):
        sum_ap = 0
        for k in range(0,len(vector)):
            if vector[k] == vector[i]:
                sum_ap += 1
            
        if sum_ap > max_ap:
            max_ap = sum_ap
    
    if max_ap > len(vector)/2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    result = []
    n = sys.stdin.readline()
    n = int(n)
    vector = sys.stdin.readline().split()
    k=0 
    vec1 = majority(vector)
    print(vec1)

