'''This module allows users to create a stack object.'''

class Stack(object):
    '''Creates a stack object. '''
    def __init__(self):
        '''Initializes the class with a list. To be used for a stack object.'''
        self.items = []
    def push(self, item):
        '''Pushes data to the top of the stack.'''
        self.items.append(item)
    def is_empty(self):
        '''Determines if the stack is empty. '''
        return self.items == []
    def pop(self):
        '''Removes item from the top of the stack.'''
        self.items.pop()
    def peek(self):
        '''Review item from the top of the stack. '''
        return self.items[-1]
    def size(self):
        '''Provides the size of the stack.'''
        return len(self.items)
       