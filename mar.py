# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 09:41:08 2022

@author: dan_r
"""

import sys

def mar2(n, profit_list, clicks_list):
    copy_profit = profit_list.copy()
    copy_clicks = clicks_list.copy()
    copy_profit = sorted(copy_profit)
    copy_clicks = sorted(copy_clicks)
    sum_profit = 0
    max_product = -10000000000000000000000
    max_profit = -1000000000000000000000
    max_clicks = -1000000000000000000000
    while len(copy_profit) > 0:    
        for i in range(0, len(copy_profit)):
            for k in range(0, len(copy_clicks)):
                if int(copy_profit[i])*int(copy_clicks[k]) >= max_product:
                    max_product = int(copy_profit[i])*int(copy_clicks[k])
                    max_profit=copy_profit[i]
                    max_clicks=copy_clicks[k]

        copy_profit.remove(max_profit)
        copy_clicks.remove(max_clicks)
        sum_profit+=max_product
        max_profit = -1000000000000000000000
        max_clicks = -1000000000000000000000
        max_product = -10000000000000000000000
        
        

    return(sum_profit)

def mar(n, profit_list, clicks_list):
    copy_profit = profit_list.copy()
    copy_clicks = clicks_list.copy()
    copy_profit = sorted(copy_profit)
    copy_clicks = sorted(copy_clicks)
    sum_profit = 0
    while len(copy_profit)>0:
        #print(copy_profit, copy_clicks)
        #print(int(max(copy_profit)),int(max(copy_clicks)))
        sum_profit+=int(max(copy_profit))*int(max(copy_clicks))
        copy_profit.remove(max(copy_profit))
        copy_clicks.remove(max(copy_clicks))
    return(sum_profit)
    

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    profit_list = sys.stdin.readline().split()
    clicks_list = sys.stdin.readline().split()
    for i in range(0, len(profit_list)):
        profit_list[i] = int(profit_list[i])
        clicks_list[i] = int(clicks_list[i])
    print(mar(n, profit_list, clicks_list))
    
