# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 08:58:45 2022

@author: dan_r
"""

import sys
import math
import time
import random

def rearrange(vector, old_position, new_position):
        for i in range(old_position, new_position-1,-1):
            vector[i], vector[i-1] = vector[i-1], vector[i]
        

def quick_sort(vector):
    return quick_sort_internal(vector,0, len(vector))

def partition_3(vector, left, right):
    pivot = vector[left]
    j = left
    n_equal = 0
    for i in range(left+1, right):
        if vector[i] < pivot:     
            j += 1 
            vector[i], vector[j] = vector[j], vector[i]

        elif vector[i] == pivot:
            j += 1
            n_equal += 1
            #print(vector[i], vector[j], n_equal+left)
            vector[i], vector[j] = vector[j], vector[i]
            vector[j], vector[n_equal+left] = vector[n_equal+left], vector[j]
        #print(j)
        #input(vector)

    if n_equal == 0:
        vector[left], vector[j] = vector[j], vector[left]
    else:
       for i in range(0, n_equal+1):
           aux = j - i
           if aux> len(vector)-1:
               aux = len(vector)-1
           vector[left+i], vector[aux] = vector[aux], vector[left+i]
       
    return j, n_equal

def partition(vector, left, right):
    pivot = vector[left]
    j = left
    for i in range(left+1, right):
        if vector[i]< pivot:         
            aux = vector[i]
            j = j+1
            vector[i] = vector[j]
            vector[j] = aux
    aux = vector[left]
    vector[left] = vector[j]
    vector[j] = aux
    return j

def quick_sort_internal(vector, left, right):
    #print(vector[left:right], left, right)
    if left >= right:
        return
    k = random.randint(left, right-1)
    k = left
    aux = vector[left]
    vector[left] = vector[k]
    vector[k] = aux
    m, nequal = partition_3(vector, left, right)
    if m-nequal >= 0:
        aux = m-nequal
    quick_sort_internal(vector, left, aux)
    #print(m)
    #input()

    quick_sort_internal(vector, m+1, right)


if __name__ == '__main__':
    n = sys.stdin.readline()
    if n != "teste\n":
        n = int(n)
        vector = sys.stdin.readline().split()
        for i in range(len(vector)):
            vector[i] = int(vector[i])
        quick_sort(vector)
        print(*vector)
    else:
        vector1 = []
        vector2 = []
        n = 0
        while n < 1000000 and vector1 == vector2:
            vector1 = []
            vector2=[]

            for i in range(0,6):
                a = random.randint(1, 9)
                vector1.append(a)
                vector2.append(a)
            print("origi",vector1)
            start = time.time()
            
            quick_sort(vector1)
            end = time.time()
            print("quick",vector1, end-start)
            print("quick terminou")
            vector2.sort()
            #print("Python terminou")
            print("python",vector2)
            if vector1 != vector2:
                input()

            n+=1
    
