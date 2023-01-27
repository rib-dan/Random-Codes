# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:50:11 2022

@author: dan_r
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 18:33:45 2022

@author: dan_r
"""

import sys

def minimum_distance(matrix, first_string, second_string, i, j):
    
    pass


def edit_distance(first_string, second_string):
    aux_string_one = first_string.copy()
    aux_string_two=   second_string.copy()
    aux_string_one.insert(0, " ")
    aux_string_two.insert(0, " ")
    
    rows, cols = (len(aux_string_one), len(aux_string_two))
    matrix =  [[0 for i in range(cols)] for j in range(rows)]
    
    #for i in range(1,rows):
    #    matrix[i][0] = i
        #print(first_string[i])
        #input(matrix)
        #if first_string[i-1] == first_string[i-2]:
        #    matrix[i][0] = matrix[i-1][0]
        #else:
        #    matrix[i][0] = matrix[i-1][0]+1
            
   # for j in range(1,cols):
    #    matrix[0][j] = j
        #print(second_string[j])
        #input(matrix)
        # if second_string[j-1] == second_string[j-2]:
        #     matrix[0][j] = matrix[0][j-1]
        # else:
        #    matrix[0][j] = matrix[0][j-1]+1
    

    for i in range(1, rows):
       for j in range(1, cols):
           #print(aux_string_one[i], aux_string_two[j])
           #input(matrix)
           min_dis = 0
           #print(aux_string_one[i-1],aux_string_two[j-1], i, j)
           #aux = matrix[i-1][j-1]
           #if aux_string_one[i] != aux_string_two[j]:
           #    aux+=1
           #if aux < min_dis:
           #    min_dis = aux
           if aux_string_one[i] != aux_string_two[j]:
               aux = matrix[i-1][j]
               if aux > min_dis:
                   min_dis = aux
           
               aux = matrix[i][j-1]

               if aux > min_dis:
                   min_dis = aux
           else:
               min_dis = matrix[i-1][j-1]+1
           matrix[i][j]=min_dis

        
    return matrix[i][j]



if __name__ == '__main__':
    n = sys.stdin.readline()
    first_string = sys.stdin.readline().split()
    m = sys.stdin.readline()
    second_string = sys.stdin.readline().split()
    

    print(edit_distance(first_string, second_string))
