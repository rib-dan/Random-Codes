# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 12:09:47 2022

@author: dan_r
"""
import sys

def gcd_naive(a,b):
    for i in range(min(a,b),0,-1):
        if a%i == 0 and b%i == 0:
            return i
def gcd(a,b):
    if b == 0:
        return a
    a_prime = a%b
    return gcd(b,a_prime)        

if __name__ == '__main__':
    a = sys.stdin.readline().split()
    b = int(a[1])
    a = int(a[0])
    print(gcd(a,b)) 
