# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:42:53 2023


@author: Hannah
"""

class Empty(Exception):
    pass

class CircularQueue:
    """Queue implementation using a circularly linked list for storage."""
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    """returns the number of elements in the queue"""
    def __len__(self):
        return self.size
    """returns True if the queue is empty"""
    def is_empty(self):
        return self.size == 0
    """returns the first element in the queue without removing it"""
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.data
    """removes and returns the first element in the queue"""
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.head.data
        self.size -= 1
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return data
    """adds an element to the back of the queue"""
    def enqueue(self, data):
        new_node = self.Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head
        self.size += 1
    """rotates the front element to the back of the queue"""
    def rotate(self):
        if self.is_empty():
            return
        self.tail = self.head
        self.head = self.head.next
    """returns True if the queue contains the element, False otherwise"""
    """contains method was added to help the user determine if the queue contains a specific element"""
    def contains(self, data):
        if self.is_empty():
            return False
        current = self.head
        for i in range(self.size):
            if current.data == data:
                return True
            current = current.next
        return False
 



    


