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

# ARRAY METHOD
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def dequeue(self):
#         if self.size == 0:
#             pass
#         else:
#             self.size -= 1
#             return self.storage.pop(0)

# USING LINKED LIST
# from singly_linked_list import LinkedList
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         return self.storage.add_to_tail(value)

#     def dequeue(self):
#         if self.size == 0:
#             pass
#         else:
#             self.size -= 1
#             return self.storage.remove_head()


# QUEUE USING STACKS
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.append(value)
        

    def pop(self):
        if self.size == 0:
            pass
        else:
            self.size -= 1
            return self.storage.pop(-1)

class Queue:
    def __init__(self):
        self.size = 0
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        while len(self.stack1) != 0:  
            self.stack2.push(self.stack1.pop())  
            
  
        # Push item into self.s1  
        self.stack1.push(value)  
  
        # Push everything back to s1  
        while len(self.stack2) != 0:  
            self.stack1.push(self.stack2.pop())  
             
    

    def dequeue(self):
        if self.size == 0:
            pass
        else:
            self.size -= 1
            return self.stack1.pop()