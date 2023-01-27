# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:23:08 2022

@author: dan_r
"""
import sys

def dp_money_change(value, coins):
    changes = {0:0}
    
    min_changes = 100000000000
    aux = 100000000000
    for i in range(1, value+1):
        for coin in coins:
            if i - coin >= 0:
                aux = changes[i-coin]+1
            if aux<min_changes:
                min_changes = aux
        changes[i] = min_changes 
        min_changes = 100000000000
        aux = 100000000000
        
        #print(changes)
            
    return changes[value]




if __name__ == '__main__':
    coins = [1,3,4]
    value = sys.stdin.readline()
    print(dp_money_change(int(value), coins))