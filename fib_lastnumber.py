# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 17:00:48 2022

@author: dan_r
"""

import sys

def fibonnaci_naive_n(n):
    fib = [0,1]
    i = 2
    while i<n+1:
        fib.append((fib[i-1]+fib[i-2])%10)
        i = i+1
    return(fib[n])

def fibonnaci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonnaci_recursive(n-1)+fibonnaci_recursive(n-2) 

def fibonnaci_recursive_dict(n, dictionary):
    if n <2:
        dictionary[n]=n
        dictionary[n-1]=n-1
        return dictionary[n]
        
    dictionary[n] = fibonnaci_recursive_dict(n-1, dictionary)+dictionary[n-2]
    return dictionary[n]

if __name__ == '__main__':   
    
    dictionary={}
    n = sys.stdin.readline()
    print(fibonnaci_naive_n(int(n)))