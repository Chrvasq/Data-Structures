"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            # list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)

        return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            # list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)

        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.value

        if node is self.head:
            return
        elif node is self.tail:
            self.remove_from_tail()
        else:
            self.delete(node)

        self.add_to_head(value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.value

        if node is self.tail:
            return
        elif node is self.head:
            self.remove_from_head()
        else:
            self.delete(node)

        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            # list is empty
            return
        elif self.head is self.tail:
            # list has one node
            self.head = None
            self.tail = None
            self.length = 0
        elif node is self.head:
            self.head = node.next
            node.delete()
            self.length -= 1
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
            self.length -= 1
        else:
            node.delete()
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.value
        current = self.head

        while current:
            if current.value > max_value:
                max_value = current.value

            current = current.next

        return max_value

    def update_node_value(self, key, value):
        current_node = self.find_node_by_key(key)
        current_node.value[key] = value

    def find_node_by_key(self, key):
        current_node = self.head
        current_node_key = list(current_node.value.keys())[0]

        while current_node_key is not key:
            current_node = current_node.next
            current_node_key = list(current_node.value.keys())[0]

        return current_node
