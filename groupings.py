# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:11:39 2022

@author: dan_r
"""

import sys

def souvenirs(weights, capacity):
    #weights.sort()
  
    flag = False
    if capacity %3 != 0:
        return 0
    capacity = capacity // 3
    value =  [[0 for i in range(capacity+1)] for j in range(len(weights)+1)]
    while len(value) > 0 and flag == False:
        print("a")
        j=0
        i = 1
        k = 1

        while i < len(value) and value[i-1][k-1] != capacity:
            k=1
            while k < capacity+1 and value[i][k-1] != capacity:
                
                value[i][k] = value[i-1][k]
                
                flag = False
                if weights[i-1] <= k:
                    aux = value[i-1][k-weights[i-1]] + weights[i-1]
                    if aux > value[i][k]:
                        value[i][k] = aux
                k+=1
            i+= 1
        i = i-1
        k = k-1
        numbers = [i]
        k = k-weights[i-1]
        i = i-1
        aux = value[i][k]
        while aux != 0:
            
            if i -1 >= 0:
                if aux == value[i-1][k]:
                    i = i-1
                else:
                    numbers.append(i)
                    i = i-1
                    k = k-weights[i-1]
            aux = value[i][k]
        sum_n = 0
        for i in numbers:
            copy_weights = weights.copy()
            value.pop(i)
            input(value)
            sum_n += copy_weights[i-1]
            weights.pop(i-1)
            print("in",weights[i-1], numbers)
        j+=1
        print(j, sum_n, capacity)
        if sum_n != capacity or j > 3:
            print("here2")
            flag = True
        print(flag, len(value))
        
            
                
        
            
    if flag == False:
        return 1
    else:
        return 0
               
        
            


if __name__ == '__main__':
    capacity = sys.stdin.readline().split()
    capacity = int(capacity[0])
    weights = sys.stdin.readline().split()
    sum_weights = 0
    for i in range(0, len(weights)):
        weights[i] = int(weights[i])
        sum_weights += int(weights[i])
        
    print(souvenirs(weights, sum_weights))