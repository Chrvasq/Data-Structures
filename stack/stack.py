import sys
sys.path.append('singly_linked_list/')

from singly_linked_list import LinkedList

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
        self.size = len(self.storage)
        return self.size

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()


# class Stack: #  using linked-list class
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         if self.storage.head == None:
#             return self.size

#         count = 1
#         current_node = self.storage.head

#         while current_node.get_next() != None:
#             count += 1
#             current_node = current_node.get_next()

#         self.size = count

#         return self.size

#     def push(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1

#     def pop(self):
#         if self.size == 0:
#             return None
#         self.size -= 1
#         return self.storage.remove_tail()

'''
Main difference between using an array and a linked list is the use of  the built in array methods for handling things like tracking size of the linked list
'''