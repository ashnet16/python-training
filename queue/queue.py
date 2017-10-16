''' This module contains a queue class.'''

class Queue(object):
   '''This class creates a queue object.'''
   def __init__(self):
       '''This constructor uses a python list to implement a queue.'''
       self.items = []
   def is_empty(self):
       '''This method returns True or False.'''
       return self.items == []
   def enqueue(self,item):
       '''This method will add an item to the end of the queue.'''
       self.items.insert(0,item)
   def dequeue(self):
       ''' This method will remove item from the end of the list.'''
       return self.items.pop()
   def size(self):
       return len(self.items)
       
       