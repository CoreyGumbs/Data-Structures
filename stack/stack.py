"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        #returns length
        return len(self.storage)

    def push(self, value):
        #appends value to end of list
        return self.storage.append(value)

    def pop(self):
        #check if list empty, return None if true
        if not self.storage:
            return None
        else:
            #pop the last item out of list and return value
            return self.storage.pop()
