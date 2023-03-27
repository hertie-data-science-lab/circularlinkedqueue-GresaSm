# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:48:01 2023

@author: Hannah
"""

from my_cq import CircularQueue

cq = CircularQueue()

print ("Starting size: ", len(cq))
cq.enqueue("A")
cq.enqueue("B")
cq.enqueue("C")
print ("Size after enqueuing 3 items: ", len(cq))
print ("First item: ", cq.first())
cq.rotate()
print ("First item after rotation: ", cq.first())
print ("Does the queue contain E? ", cq.contains("E"))
print ("Does the queue contain A? ", cq.contains("A"))


