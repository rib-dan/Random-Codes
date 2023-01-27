# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:17:10 2022

@author: dan_r
"""
import sys

def money_change(money):
    aux = money
    coin = [10,5,1]
    i = 0
    coins = 0
    while aux > 0:
        if aux < coin[i]:
            i += 1
        if aux >= coin[i]:
            aux = aux - coin[i]
            coins += 1

    return coins


if __name__ == '__main__':
    n = sys.stdin.readline()
    #last_digit_sum(int(n))
    print(money_change(int(n)))