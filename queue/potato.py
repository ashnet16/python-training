'''This module plays the hot potato game.'''
from queue import Queue



def hot_potato(name,number):
    '''This method implements a hot potato game.'''
    circle = Queue()
    for item in name:
        circle.enqueue(item)
    while circle.size() > 1:
        for i in range(number):
            circle.enqueue(circle.dequeue())
        print circle.dequeue()
    return circle.dequeue()


print hot_potato(['Bill','David','Susan','Jane','Kent','Brad'],3)


