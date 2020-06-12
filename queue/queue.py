"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
""" 

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage);
    
#     def enqueue(self, value):
#         return self.storage.insert(0, value);
    
#     def dequeue(self):
#         if not self.storage:
#             return None
#         else:
#             return self.storage.pop();
        
        
class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node =  next_node
        
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
        
    def set_next_node(self, new_node):
        self.next_node = new_node
        

class Queue:
    def __init__(self):
        self.head = None
        
    def len(self):
        count = 0
        current_head = self.head
        while(current_head):
            count +=1
            current_head = current_head.next_node 
        return count
    
    def enqueue(self, value):
        new_node = Node(value, None);
        
        if not self.head:
            self.head = new_node;
        else:
            current_node = self.head
            while(current_node.next_node is not None):
                current_node = current_node.next_node
            current_node.next_node = new_node
    
    def dequeue(self):
        if not self.head:
            return None
        else: 
            value = self.head.value
            self.head = self.head.next_node
            return value
                
    def __str__(self):
        return f"{self.head.value}"
            


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()



print(q.len())
