"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #creates new node
        new_node = ListNode(value, None, None);
        #add new node to list length
        self.length +=1
        
        #check if there is an element in the list
        #if not create one
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            #change head to new node
            #connect current node to new node's next 
            new_node.next = self.head
            #connect old head previous to new node
            self.head.prev = new_node
            #assign new node as new head
            self.head = new_node
            
            

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #assign current head's value
        value = self.head.value
        #"delete" current head to next node's prev pointer 
        self.delete(self.head)
        #return value
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            #assign new node.prev to current tail
            new_node.prev = self.tail
            #reassign tail.next to new node
            self.tail.next = new_node
            #reassign tail to new node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #check if node is head
        #assign node value
        #if not check if it is tail
        #if not either, delete node, and add it to head 
        if node is self.head:
            return
        
        value = node.value
        
        if node is self.tail:
            #remove as tail and reassign previous node as tail
            self.remove_from_tail()
        else:
            #delete node from current position and reassign pointers to previous/next nodes
            node.delete()
            #remove node from length
            self.length -=1
        #add value as new node to head
        self.add_to_head(value)
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        
        value = node.value
        
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        #check if there is an element
        #do nothing if there isnt an element or list is empty
        if not self.head and not self.tail:
            return 
        #decrement the length
        self.length -= 1
        
        #check if there is only one element (head & tail)
        #change pointers to None to "delete" only Node
        if self.head == self.tail:
            self.head = None
            self.tail = None
        #check if node is the head
        elif self.head == node:
            #reassign head to next node
            self.head = node.next
            node.delete()
        #check if node is tail
        elif self.tail == node:
            #reassign tail to previous node
            self.tail = node.prev
            node.delete()
        else: 
            node.delete()
        
        
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        
        max_val = self.head.value
        current = self.head
        
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
                
        return max_val
