# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 18:35:15 2022

@author: dan_r
"""
import sys

def fibonnaci_naive(n):
    fib = [0,1]
    aux = 0
    if n < 1:
        return 0
    i = 2
    while i < n+1:
        aux = fib[1]
        fib[1] = fib[1]+fib[0]
        fib[0]=aux
        i = i + 1
    return(fib[1])

def fibonnaci_mod(i, m):
    period = 60
    new_i = fibonnaci_naive(i%period)-1
    #print("fib_mod",new_i)
    return(new_i%m)


def fibonacci_sum_naive(n):

    if n <= 1:
        return n
    sum_fib = 0
    return fibonnaci_mod(n+2, 10)

    return sum_fib % 10

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_naive(n))
