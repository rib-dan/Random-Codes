# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:07:31 2022

@author: dan_r
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:15:15 2022

@author: dan_r
"""

import sys
import math
import time
import random

def b_search_rec(vector, left, right, number):
    if number > vector[-1] or number < vector[0]:
        return -1
    
    if number == vector[0]:
        return 0
    if vector[left] == number:
        return left
    if left == right:
        return -1
    mid = (right - left) // 2 + left
    
    if vector[mid] >= number:
        return b_search_rec(vector, left, mid, number)
    else:
        return b_search_rec(vector, mid+1 , right, number)

def b_search_nrec(vector, number):
    end = len(vector)-1
    start = 0
    step = len(vector)//2
    flag = False
    if number > vector[len(vector)-1] or number < vector[0]:
            return -1
    if number == vector[0]:
        return 0
    while flag == False:
        
        if number > vector[step]:
            start = step
            step = math.ceil((end - step)/2)+step
        elif number < vector[step]:
            end = step
            step = (end-start)//2
            #print(start,step,end)
        else:
            step = step -1
            if vector[step] != number:
                step += 1
                flag = True
        
        if end - start == 1 and vector[end] != number and vector[start] != number:
            return -1
        
    return(step)

def b_search(vector, number):
    return b_search_rec(vector, 0, len(vector), number)

def naive_search(vector, number):
    for i in range(0, len(vector)):
        if vector[i] == number:
            return i
    return -1


if __name__ == '__main__':
    result = []
    n = sys.stdin.readline()
    if n != "teste\n":
        n = int(n)
        vector = sys.stdin.readline().split()
        for i in range(0, len(vector)):
            vector[i]= int(vector[i])
    
        k = sys.stdin.readline()
        k = int(k)
        numbers = sys.stdin.readline().split()
        for i in numbers:
            result.append(b_search(vector, int(i)))
        print(*result)
    else:
        while True:
            vector = []
            for i in range(0,10):
                vector.append(random.randint(0, 5))
                result = []
                vector.sort()
            
                
            number = random.randint(0, 5)
            print("Going in", vector, number)
            start = time.time()
            result.append(b_search(vector,number))
            end = time.time()
            print("vector", vector, number)
            print("resultado",*result)
            result2 = naive_search(vector, number)
            print(result2)
            if result[0] != result2:
                input()