class Node:
    def __init__(self, value=None, next_node=None):
        self.value =  value;
        self.next_node = next_node;
        
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node;
    
    def set_next_node(self, new_next):
        self.next_node = new_next
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value, None);
        
        if not self.head:
            self.head = new_node;
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node
            
            
    def remove_tail(self):
        pass
    
    def contains(self, value):
        if not self.head:
            return False
        
        current =  self.head
        while current:
            if current.get_value() == value:
                return True
            current =  current.get_next()
        return False
    
    def get_max(self):
        pass