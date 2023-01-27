# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 18:33:45 2022

@author: dan_r
"""

import sys

def minimum_distance(matrix, first_string, second_string, i, j):
    
    pass


def edit_distance(first_string, second_string):
    aux_string_one =  " " + first_string
    aux_string_two= " " +  second_string
    
    rows, cols = (len(first_string), len(second_string))
    matrix =  [[0 for i in range(cols)] for j in range(rows)]
    #matrix[0][1] = 1
    #matrix[1][0] = 1
    #input(matrix)
    for i in range(1,rows):
        matrix[i][0] = i
        #print(first_string[i])
        #input(matrix)
        #if first_string[i-1] == first_string[i-2]:
        #    matrix[i][0] = matrix[i-1][0]
        #else:
        #    matrix[i][0] = matrix[i-1][0]+1
            
    for j in range(1,cols):
        matrix[0][j] = j
        #print(second_string[j])
        #input(matrix)
        # if second_string[j-1] == second_string[j-2]:
        #     matrix[0][j] = matrix[0][j-1]
        # else:
        #    matrix[0][j] = matrix[0][j-1]+1
    
    
    #print(matrix, rows, cols)
    #input()
    for i in range(1, rows):
        for j in range(1, cols):
            min_dis = 100000000
            #print(aux_string_one[i-1],aux_string_two[j-1], i, j)
            aux = matrix[i-1][j-1]
            if aux_string_one[i] != aux_string_two[j]:
                aux+=1
            if aux < min_dis:
                min_dis = aux
            
            aux = matrix[i-1][j]+1
            #if aux_string_one[i] != aux_string_two[j]:
            #    aux+=1
            if aux < min_dis:
                min_dis = aux
            
            aux = matrix[i][j-1]+1
            #if aux_string_one[i] != aux_string_two[j]:
            #    aux+=1
            if aux < min_dis:
                min_dis = aux
            
            matrix[i][j]=min_dis
    input(matrix)
        
    return matrix[i][j]



if __name__ == '__main__':
    first_string = sys.stdin.readline()
    second_string = sys.stdin.readline()
    

    print(edit_distance(first_string, second_string))
