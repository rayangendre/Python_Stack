class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Linked List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        if capacity == None:
            capacity = 0
            
        self.capacity = capacity
        self.top = None
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''

        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''

        return (self.num_items == self.capacity)

    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''

        if self.num_items == self.capacity:
            raise IndexError('Stack is full')

        self.top = Node(item, self.top)
        self.num_items = self.num_items + 1

    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''

        if self.num_items == 0:
            raise IndexError('Stack is empty')

        tempValue = self.top.data
        self.top = self.top.next

        self.num_items = self.num_items - 1
        return tempValue


    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''

        if self.num_items == 0:
            raise IndexError('Stack is empty')

        tempValue = self.top.data
        
        return tempValue

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        
        return self.num_items

 