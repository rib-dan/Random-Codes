# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 20:06:00 2022

@author: dan_r
"""

import sys

def fibonnaci_naive(n):
    fib = [0,1]
    aux = 0
    if n < 1:
        return 0, 0
    i = 2
    #print(n)
    while i < n+1:
        aux = fib[1]
        fib[1] = fib[1]+fib[0]
        fib[0]=aux
        i = i + 1
    return(fib[0], fib[1])

def fibonnaci_mod(i, m):
    period = 60
    new_i_minus, new_i = fibonnaci_naive(i%period)
    new_i = new_i 
    new_i_minus = new_i_minus
    #print("fib_mod",new_i)
    return(new_i_minus%m,new_i%m)


def last_digit_sum_square(k):
    if k == 0:
        return 0
    
    fib_minus,fib = fibonnaci_mod(k,10)
    #print(fib_minus, fib)
    return(fib*(fib+fib_minus)%10)
    

if __name__ == '__main__':   

    n = sys.stdin.readline()
    #last_digit_sum(int(n))
    print(last_digit_sum_square(int(n)))