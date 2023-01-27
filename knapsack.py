# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:24:39 2022

@author: dan_r
"""

import sys

def knapsack(weights, capacity):
    value =  [[0 for i in range(capacity+1)] for j in range(len(weights)+1)]
    for i in range(1,len(weights)+1):
        for k in range(1, capacity+1):
            value[i][k] = value[i-1][k]
            if weights[i-1] <= k:
                aux = value[i-1][k-weights[i-1]] + weights[i-1]
                if aux > value[i][k]:
                    value[i][k] = aux
    print(value)
    return value[-1][-1]
               
        
            


if __name__ == '__main__':
    capacity, n = sys.stdin.readline().split()
    capacity, n = int(capacity), int(n)
    weights = sys.stdin.readline().split()
    for i in range(0, len(weights)):
        weights[i] = int(weights[i])
    print(knapsack(weights, capacity))