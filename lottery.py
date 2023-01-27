# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 21:42:50 2022

@author: dan_r
"""
import sys
import math
import random

def merge(first_half, second_half):
    i = 0
    j = 0
    result = []
    
    
    while len(result) < len(first_half)+len(second_half):
        if j<len(second_half) and i< len(first_half):
            #print(first_half[i], second_half)
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
            

def merge_sort(vector):
    if len(vector) == 1:
        return vector
    middle = math.floor(len(vector)/2)
    first_half = merge_sort(vector[0:middle])
    second_half = merge_sort(vector[middle:len(vector)])
    
    result = merge(first_half, second_half)
    
    return result
    

def b_search(vector, number):
    end = len(vector)-1
    start = 0
    step = math.floor(len(vector)/2)
    if number < vector[0]:
            return -1
    if number >= vector[len(vector)-1]:
        return len(vector)-1
    while vector[step] !=number:
        
        if number > vector[step]:
            start = step
            step = math.ceil((end - step)/2)+step
        else:
            end = step
            step = math.floor((step-start)/2)
        
        if end - start == 1 and vector[end] != number and vector[start] != number:
            return start
    return(step)

def find_point(vector_ini, vector_end, point):
    #vector_ini = merge_sort(vector_ini)
    #vector_end = merge_sort(vector_end)
    start = b_search(vector_ini, point)
    if start == -1:
        return 0
    seg_sum = 0
    aux = start
    end = vector_end[start]
    while point <= end and start >-1:
        seg_sum+=1
        start-=1
        end = vector_end[start]

    return seg_sum
    
def find_point_naive(vector_ini, vector_end, point):
    vector_ini = merge_sort(vector_ini)
    vector_end = merge_sort(vector_end)
    if point > vector_end[len(vector_end)-1]:
        return 0
    if point < vector_ini[0]:
        return 0
    i = len(vector_ini)-1
    while vector_ini[i]>point:
        i-=1
    if point<= vector_end[i]:
        return 1
    else:
        return 0
        

if __name__ == '__main__':
    s,p = sys.stdin.readline().split()
    #print(s)

    segments_ini = []
    segments_end = []
    result1 = []
    result2 = []
    if s != "teste":
        
        for i in range(int(s)):
            aux = sys.stdin.readline().split()
            segments_ini.append(int(aux[0]))
            segments_end.append(int(aux[1]))

        points = sys.stdin.readline().split()
        for i in range(int(p)):
            result1.append(find_point(segments_ini, segments_end, int(points[i])))
            #result2.append(find_point_naive(segments_ini, segments_end, int(points[i])))
        print(*result1)
        #print('Second',*result2)
    else:
        s = random.randint(5, 5)
        p = random.randint(10, 20)
        for i in range(s):
            aux = random.randint(0, 10)
            segments_ini.append(aux)
            segments_end.append(random.randint(aux, aux+5))
        for i in range(int(p)):
            aux = random.randint(0, 10)
            result1.append(find_point(segments_ini, segments_end, aux))
            result2.append(find_point_naive(segments_ini, segments_end, aux))
        print(merge_sort(segments_ini), merge_sort(segments_end))
        print('First',*result1)
        print('Second',*result2)

    
