# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:12:46 2022

@author: dan_r
"""
import sys
import math
import random
import time

def inversions(first_half, second_half, size):
    i = 0
    j = 0
    result = []
    #print("start", first_half, second_half, size)
    
    while len(result) < len(first_half)+len(second_half):
        #print("1",size, first_half, second_half, result, i, j)
        
        if j<len(second_half) and i< len(first_half):
            #print(first_half[i],second_half[j])
            
            if first_half[i]>second_half[j]:
                #print(first_half[i], second_half[j])
                size+=len(first_half) - i
        
            if first_half[i] <= second_half[j]:
                result.append(first_half[i])
                
                i+=1    
            else:
                result.append(second_half[j])
                j+=1
                
        else:
            if j<len(second_half):
                result.append(second_half[j])
                
                if j < len(second_half):
                    j+=1
            if i<len(first_half):
                result.append(first_half[i])
                #size+=1
                if i < len(first_half):
                    i+=1
        #print("2",size, first_half, second_half, result)

    return result,size

def merge(first_half, second_half):
    i = 0
    j = 0
    result = []
    
    
    while len(result) < len(first_half)+len(second_half):
        if j<len(second_half) and i< len(first_half):
        
            if first_half[i] < second_half[j]:
                result.append(first_half[i])
                i+=1       
            else:
                result.append(second_half[j])
                j+=1
        else:
            if j<len(second_half):
                result.append(second_half[j])
                if j < len(second_half):
                    j+=1
            if i<len(first_half):
                result.append(first_half[i])
                if i < len(first_half):
                    i+=1

    return result
            

def merge_sort(vector,size):
    if len(vector) == 1:
        return vector,0
    middle = math.floor(len(vector)/2)
    first_half,size_first = merge_sort(vector[0:middle], size)
    second_half, size_second = merge_sort(vector[middle:len(vector)], size)
    
    result,size = inversions(first_half, second_half, size_first+size_second)
    
    return result, size
if __name__ == '__main__':
    n = sys.stdin.readline()
    if n != "teste\n":
        n = int(n)
    
        vector = sys.stdin.readline().split()
        for i in range(len(vector)):
            vector[i] = int(vector[i])
        _,size = merge_sort(vector, 0)
    
        print(size)
    else:
        vector1 = []
        vector2 = []
        n = 0
        while n < 1000000 and vector1 == vector2:
            vector1 = []
            vector2=[]

            for i in range(0,50):
                a = random.randint(1, 9)
                vector1.append(a)
                vector2.append(a)
            print("origi",vector1)
    
            vector1, size = merge_sort(vector1,0)
            print("quick",vector1, size)
            vector2.sort()
            print("python",vector2, vector1==vector2)
            time.sleep(1)

            n+=1
