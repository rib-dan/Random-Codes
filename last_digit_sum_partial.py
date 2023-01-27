# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 20:03:18 2022

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

    if n <= 1 and n>0:
        return n
    elif n < 0:
        return 0
    sum_fib = 0
    return fibonnaci_mod(n+2, 10)

    return sum_fib % 10

def fibonacci_partial_sum(n,m):
    if n == m:
        #print(fibonnaci_naive(n))
        return fibonnaci_mod(n,10)+1
    #print(fibonacci_sum_naive(m), fibonacci_sum_naive(n-1))
    return fibonacci_sum_naive(m)-fibonacci_sum_naive(n-1)

if __name__ == '__main__':   
    
    dictionary={}
    n = sys.stdin.readline().split()
    #last_digit_sum(int(n))
    result= fibonacci_partial_sum(int(n[0]), int(n[1]))
    #print(last_digit_sum(int(n[1])), last_digit_sum(int(n[0])))
    print(result%10 )