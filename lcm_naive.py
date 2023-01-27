# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 17:07:01 2022

@author: dan_r
"""

import sys

def lcm(a,b):
    gcd_ab = gcd(a,b)
    return (a*b/gcd_ab)

def gcd(a,b):
    if b == 0:
        return a
    a_prime = a%b
    return gcd(b,a_prime)        

if __name__ == '__main__':
    a = sys.stdin.readline().split()
    b = int(a[1])
    a = int(a[0])
    print(int(lcm(a,b))) 
