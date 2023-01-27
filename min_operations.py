# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:33:10 2022

@author: dan_r
"""

import sys

def minimum_op(value):
    operations = {1:0}
    intermediate = []
    min_operations = 100000000000
    aux = 100000000000
    aux2 = 0
    for i in range(2, value+1):
        if i%2 == 0:
            aux = operations[i/2]+1
            if aux<min_operations:
                min_operations = aux
        if i%3 == 0:
            aux = operations[i/3]+1
            if aux<min_operations:
                    min_operations = aux

        if i-1 > 0:
            aux = operations[i-1]+1
            if aux<min_operations:
                min_operations = aux
        operations[i] = min_operations 
        min_operations = 100000000000
        aux = 100000000000

    #input(operations)    
    aux_val = value
    intermediate.append(aux_val)
    aux2 = 10000000000
    aux = 100000000000
    i = 0
    while aux_val != 1:
        #print(aux_val,i)
        #print(aux_val%3)
        #input()
        i+=1
        if aux_val%2 == 0:
            aux = operations[aux_val/2]+1
            if aux<min_operations:
                min_operations = aux
                aux2 = aux_val/2
                #print("here 2", min_operations, aux2,aux_val)
        
        if aux_val%3 == 0:
            aux = operations[aux_val/3]+1
            if aux_val<min_operations:
                min_operations = aux
                aux2 =aux_val/3
                #print("here 3", min_operations, aux2,aux_val)
            
        if aux_val-1 > 0:
            aux = operations[aux_val-1]+1
            if aux<min_operations:
                min_operations = aux
                aux2 = aux_val - 1
                #print("here 1", min_operations, aux2,aux_val)
            
        aux_val=aux2
        intermediate.append(int(aux_val))
        min_operations = 1000000000000
        
    
    return operations[value], intermediate


if __name__ == '__main__':
    value = sys.stdin.readline()
    n, steps = minimum_op(int(value))
    print(n)
    steps.reverse()
    print(*steps)