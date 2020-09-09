"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

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
        current = self.head

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = current
            current.prev = new_node
            self.head = new_node

        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        current = self.head
        new_head = current.next

        if new_head:
            new_head.prev = None
            self.head = new_head
        else:
            self.head = None
            self.tail = None

        self.length -= 1
        return current.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        current = self.tail
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        current = self.tail
        new_tail = current.prev

        if new_tail:
            new_tail.next = None
            self.tail = new_tail
        else:
            self.head = None
            self.tail = None
        
        self.length -= 1
        return current.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        max_val = self.head.value
        current = self.head

        while current is not None:
            if current.value > max_val:
                max_val = current.value

            current = current.next
        return max_val
