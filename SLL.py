# Markhus Dammar
# 2/25/2020
# Reused 3/10/2020 for Stack and Queue/Paper Company
# Class setup for linked list and operations


class Node:

    def __init__(self, data=None, next=None, tail=None):
        self.data = data
        self.next = next
        self.tail = None

    def __repr__(self):
        return repr(self.data)


class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):                                      # Returns a string representation of the list
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ' , ' .join(nodes) + ']'

    def prepend(self, data):                                 # Adds to beginning of list
        self.head = Node(data=data, next=self.head)

    def append(self, data):                                  # Adds to end of list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node

    def remove_head(self):                                   # Removes from head of list
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def remove_end(self):                                    # Removes from end of list
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data

    def clear(self):                                          # Clears the list
        self.head = None

    def search(self, data):                                   # Searches for a number from the list
        current = self.head
        while current.next:
            if current.data == data:
                return True
            current = current.next
        if current.data == data:
            return True
        else:
            return False

    def remove_distinct(self, data):                          # Removes a specific value from the list
        previous_node = None
        current = self.head
        while current:
            if current.data == data:
                if previous_node:
                    previous_node.next(current.next())
                else:
                    self.head = current.next
                return True
            previous_node = current
            current = current.next
        return False



