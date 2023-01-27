# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:08:31 2022

@author: dan_r
"""

class Node():
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    def __str__(self):
        return "This node holds {} ".format(self.data)
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def set_next_node(self, next_node):
        self.next_node = next_node
    def get_next_node(self):
        return self.next_node
    
    
class linked_list(Node):
    def __init__(self, node = None):
        if node == None:
            self.head = Node(data = 0)
        else:
            self.head.next_node = node
            
    def add_node(self, new_node):
        new_node = Node(new_node)
        if self.head.next_node == None:
            self.head.next_node = new_node
            new_node.next_node = None
            self.head.data = self.head.data + 1
        else:
            n_node = self.head.next_node
            while n_node.next_node != None:
                n_node = n_node.next_node
            n_node.next_node = new_node
            self.head.data = self.head.data + 1
    def add_nodes(self, list_nodes):
        for node in list_nodes:
            self.add_node(node)
            
    def get_head(self):
        return self.head.data
    
    def get_n_node(self, n):
        if n > self.head.data:
            return -1
        
        n_node = self.head.next_node
        i = 0
        
        while n_node.next_node != None and i < n:
            n_node = n_node.next_node
            i= i+1
        return n_node
    def get_all_nodes(self):
        if self.head.next_node == None:
            return []
        
        nodes = []
        n_node = self.head.next_node
        while n_node != None:
            nodes.append(n_node.data)
            n_node = n_node.next_node
        return nodes
    
    def change_order(self,old_position, new_position):
        if old_position == new_position:
            return
        
        node_og=self.get_n_node(old_position)
        self.get_n_node(old_position-1).set_next_node(self.get_n_node(old_position+1))
        self.get_n_node(new_position-1).set_next_node(node_og)
        
        if new_position+1 < self.get_head():
            node_og.set_next_node(self.get_n_node(new_position+1))
        else:
            node_og.set_next_node(None)

    def __str__(self):
        return "This linked list holds {} ".format(self.get_all_nodes())
        
        
            
            
if __name__ == '__main__':   
    
    og_list = linked_list()

    og_list.add_nodes(["ana","carlos","jose","daniel","demetrio","cunha"])
    
    n2=og_list.get_head()

    n = round(n2/2)
    jen_list = linked_list()
    berry_list = linked_list()
    
    for i in range(0,n):
        print(og_list.get_n_node(i),i)
        jen_list.add_node(og_list.get_n_node(i).get_data())
        
    for i in range(n, n2):
        berry_list.add_node(og_list.get_n_node(i).get_data())
        
    print(jen_list, berry_list)