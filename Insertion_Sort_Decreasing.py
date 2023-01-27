#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:42:10 2022

@author: osgiliath
"""

def insertion_sort(input_array):
    
    for i in range(1,len(input_array)):
        key = input_array[i]
        j = i-1
        while j>-1 and input_array[j]<key:
            input_array[j+1]=input_array[j]
            j=j-1            
        input_array[j+1]=key

if __name__ == "__main__":
    input_array = []
    
    input_number = input("Type the next number in the sequence. Type 'end' when you're done.")
    while input_number != 'end':
        input_array.append(int(input_number))
        input_number = input("Type the next number in the sequence. Type 'end' when you're done.")
        
    insertion_sort(input_array)
    
    print("The sorted sequence is: ", input_array)
    pass