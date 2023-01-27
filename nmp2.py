# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 11:13:55 2022

@author: dan_r
"""

def nums(n):
    

    numbers = []
    suma = 0
    i=0

    while suma != n:
        i = i+1  
        suma = sum(numbers)
    
        if suma < n:
            numbers.append(i)
            suma = sum(numbers)
       
        if suma > n:
            numbers.remove(numbers[0])
            suma = sum(numbers)
        numbers.sort(reverse = True)
    
    numbers.sort() 
    
    return numbers



if __name__ == '__main__':
    n = int(input())
    numeros = nums(n)
    print(len(numeros))
    for x in numeros:
        print(x, end=' ')