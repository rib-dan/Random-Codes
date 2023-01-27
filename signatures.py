# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:44:33 2022

@author: dan_r
"""


import sys

def signatures(n, xcoordinates, ycoordinates):
    i = 0
    solved = []
    copy_xcoordinates = xcoordinates.copy()
    copy_ycoordinates = ycoordinates.copy()
    
    while len(copy_xcoordinates) !=0:
       trace = min(copy_ycoordinates)
       while i < len(xcoordinates):
           if trace >= xcoordinates[i] and trace <=ycoordinates[i]:
               if xcoordinates[i] in copy_xcoordinates:
                   copy_xcoordinates.remove(xcoordinates[i])
                   copy_ycoordinates.remove(ycoordinates[i])
               if trace not in solved:
                   solved.append(trace)   
           i += 1
       i=0
 

    
    return len(solved), solved
    
        


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    xcoordinates = []
    ycoordinates=[]
    for i in range(0,n):
        aux = sys.stdin.readline().split()
        xcoordinates.append(int(aux[0]))
        ycoordinates.append(int(aux[1]))
        
    
    n, coordinates = signatures(n, xcoordinates, ycoordinates)
    
    
    message = ""
    
    for i in range(0,n):
        message = message + str(coordinates[i]) + " "
    print(n)
    print(message)
