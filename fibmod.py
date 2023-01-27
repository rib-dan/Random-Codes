# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:19:07 2022

@author: dan_r
"""
import sys
import time
def fibonnaci_mod(i, m):
    cycle = [0]
    sequence = [0]
    aux = []
    period = 1
    flag = False
    k = 1
    j=0
    while flag == False:
        sequence.append(fibonnaci_naive(k)%m)
        if fibonnaci_naive(k)%m != cycle[0]:
            cycle.append(fibonnaci_naive(k)%m)
        else:
            for j in range(0, len(cycle)):
                if fibonnaci_naive(k+j)%m == cycle[j]:
                    aux.append(fibonnaci_naive(k+j)%m)
            if aux == cycle:
                period = len(cycle)
                flag = True
            else:
                cycle.append(fibonnaci_naive(k)%m)
                aux = []
        k=k+1
    new_i = fibonnaci_naive(i%period)
    return(new_i%m)


def fibonnaci_naive(n):
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return(fib[n])


if __name__ == '__main__':   
    
    dictionary={}
    n = sys.stdin.readline().split()
    print(fibonnaci_mod(int(n[0]), int(n[1])))
