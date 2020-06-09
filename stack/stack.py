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
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         #returns length
#         return len(self.storage)

#     def push(self, value):
#         #appends value to end of list
#         return self.storage.append(value)

#     def pop(self):
#         #check if list empty, return None if true
#         if not self.storage:
#             return None
#         else:
#             #pop the last item out of list and return value
#             return self.storage.pop()


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value;
        self.next_node = next_node

class Stack:
    def __init__(self):
        self.head = None
        self. tail = None
    
    def __len__(self):
        count = 0
        current_head = self.head
        while(current_head):
            count +=1
            current_head = current_head.next_node 
        return count
        
    def push(self, value):
        new_node = Node(value, None);
        #check if head is empty
        if not self.head:
            self.head = new_node;
        else:
            head = self.head;
            new_node.next_node = self.head
            self.head = new_node
            
    def __str__(self):
        return f"{self.head} {self.head.next_node}"
    
test_node =  Node(1, None);



new_stack = Stack();

new_stack.push(1);
print(new_stack);
new_stack.push(2)
print(new_stack)
new_stack.push(3)
print(new_stack)
print(new_stack.__len__())