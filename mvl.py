# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:32:29 2022

@author: dan_r
"""

import sys

def maximum_value_loot(capacity, value_items, weight_items, weighted_values):
    taken = 0
    copy_values = value_items.copy()
    copy_weight = weight_items.copy()
    copy_weighted = weighted_values.copy()
    taken_weight = 0
    value = 0
    while taken_weight != capacity and len(copy_weight) != 0:
        aux_weight = copy_weight[copy_weighted.index(max(copy_weighted))]
        aux_value = copy_values[copy_weighted.index(max(copy_weighted))]
        #print(copy_weight, copy_weighted, copy_values)
        #print(aux_weight, aux_value, copy_weight, copy_weighted.index(max(copy_weighted)))
        if capacity - taken_weight>= aux_weight:
            value = value + aux_value
            taken_weight = taken_weight + aux_weight
            
            copy_weight.pop(copy_weighted.index(max(copy_weighted)))
            copy_values.pop(copy_weighted.index(max(copy_weighted)))
            copy_weighted.pop(copy_weighted.index(max(copy_weighted)))
        else:        
            if capacity - taken_weight>= aux_weight:
                value = value + aux_value
                taken_weight = taken_weight+ aux_weight 
            else:
                #print(aux_value*(abs(capacity - taken_weight)/float(aux_weight)), aux_weight,aux_value)
                value = value + aux_value*(abs(capacity - taken_weight)/float(aux_weight))
                #print(value)
                taken_weight = capacity
            
        
    return value


if __name__ == '__main__':
    n,capacity = sys.stdin.readline().split()
    value_items = []
    weight_items = []
    weighted_values = []
    for i in range(0,int(n)):
        value, weight = sys.stdin.readline().split()
        value_items.append(int(value))
        weight_items.append(int(weight))
        weighted_values.append(int(value)/float(weight))
    print("%.4f" % maximum_value_loot(int(capacity), value_items, weight_items, weighted_values))