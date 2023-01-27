# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 20:00:02 2022

@author: dan_r
"""
import random
import math
import time

class dynamic_connectivity():
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        
    def get_data(self):
        return self.data
    
    def __str__(self):
        return "This dynamic connective class holds {} ".format(self.data)
    
    def find(self,p,q):
        if p>self.size or q>self.size:
            return False
        if self.data[p] == self.data[q]:
            return True
        else:
            return False
        
    def union(self,p,q):
        for i in range(0,self.size):
            #print(self.data[q], self.data[i])
            if self.data[i] == self.data[p]:
                self.data[i] = self.data[q]
    
    def find_root(self,p):
        index = p
        size = 0
        #print(self.data[index],index)
        
        while self.data[index] != index:
            size = size +1
            index = self.data[index]
           # print(self.data[index],index)
        root_p = self.data[index]
        return root_p, size
    
    def lazy_find(self,p,q):
        
        root_p,_ = self.find_root(p)
        root_q,_ = self.find_root(q)
        
        #print("root",self.data, root_p, root_q)
        if root_q == root_p:
            
            return True
        else:
            return False
                
    
    def lazy_union(self, p, q):
        
        
        root_p,size_p = self.find_root(p)
        root_q,size_q = self.find_root(q)
        
        if size_p>=size_q:
                    
            self.data[root_q] = root_p
        else:
            self.data[root_p] = root_q
    
class percolation(dynamic_connectivity):
    def __init__(self, size):
        con_matrix = []
        perc_matrix = []
        closed_matrix = []
        for i in range(0,size*size):
            con_matrix.append(i)
            closed_matrix.append(i)
            perc_matrix.append(0)
            
        self.data = con_matrix
        self.perc_matrix = perc_matrix
        self.size = size
        self.closed_matrix = closed_matrix
        self.n_find = 0
    def open(self,row,col):
        index = self.size*(row-1) + col - 1       

        if self.isOpen(row, col) == False:
            self.perc_matrix[index] = 1
            self.closed_matrix.remove(index)
            
            if row-1>0 and index - self.size>=0:
                if self.isOpen(row-1, col):
                    self.lazy_union(index-self.size, index)

            if row+1 <= self.size and index+self.size <= self.size**2:
                if self.isOpen(row+1, col):
                    self.lazy_union(index+self.size, index)

            if col-1>0 and index-1>=0:
                if self.isOpen(row, col-1):
                    self.lazy_union(index-1, index)


            if col+1<=self.size and index+1 <= self.size**2:
                if self.isOpen(row, col+1):
                    self.lazy_union(index+1, index)
        else:
            self.open(row,col)
        
    
    def isOpen(self,row,col):
        index = self.size*(row-1) + col - 1
        #print(index, row, col)
        if  self.perc_matrix[index] == 1:
            return True
        else:
            return False
        
    def isFull(self,row,col):
        index = self.size*(row-1) + col - 1
        if  self.perc_matrix[index] == 1:
            return False
        else:
            return True
    
    def numberOfOpenSites(self):
        open_sites = 0
        for i in self.perc_matrix:
            if i == 1:
                open_sites = open_sites+1
        return open_sites
       
    def percolates(self):
        if len(self.data) == self.size**2:  
            
            self.data.append(self.size**2)
            for i in range(0, self.size):
                self.lazy_union(self.size**2,i)
        
        
            self.data.append(self.size**2+1)
            for i in range(self.size**2-self.size, self.size**2):
                self.lazy_union(self.size**2+1,i)
        self.n_find = self.n_find+1
        return self.lazy_find(self.size**2, self.size**2+1)
    
class PercolationStats(percolation):
    def PercolationStats(self, trials):
        print(time.time())
        for n in range(0, trials):
            self.__init__(self.size)
            while self.percolates() is False:
                index = random.randint(1,len(self.closed_matrix)-1)
                index = self.closed_matrix[index]
                #print(len(self.closed_matrix)-1,index,self.percolates())
                row_index = math.floor(index/self.size)+1
                col_index = index-(row_index-1)*self.size+1
                self.open(row_index,col_index)
        print(time.time())
   


        
        
   
        
        
    
if __name__ == '__main__':   
    #teste = dynamic_connectivity([25, 25, 25, 25, 25, 5, 5, 6, 25, 8, 11, 6, 6, 5, 5, 6, 15, 5, 5, 6, 26, 26, 26, 26, 26, 25, 6])
    #print(teste.lazy_find(25, 26))
    din= PercolationStats(1024)
    print(din.PercolationStats(1))
    print(din.n_find)


                