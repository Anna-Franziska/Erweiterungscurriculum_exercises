from collections import deque



#class for holding the data, defaults to empty node if no data is given
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None #pointer to the next node

# Class for managing the list and nodes
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1 #always update the size to prevent costly iterations to get the size

    #defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size


    def iterate_modification(self):
        current = self.head
        while current:
            val = current
            current = current.next
            yield val



    def clear(self):

        allNodes = [node for node in self.iterate_modification()]
        for node in allNodes:
            node.next = None
        self.head = None
        self.size = 0
        return

    def get_data(self, data):

        allNodes = [node for node in self.iterate_modification()]
        for node in allNodes:
            if node.data == data:
                return data
        return False


    def delete(self, data):

        allNodes = [node for node in self.iterate_modification()]
        for node in allNodes:
            if node.next.data == data:
                node.next = node.next.next
                self.size -= 1
                return


class NodeDLL:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None



class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node

        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current

        self.size += 1  # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size


    def iterate_modification(self):
        current = self.head
        while current:
            val = current
            current = current.next
            yield val



    def clear(self):


        allNodes = [node for node in self.iterate_modification()]
        for node in allNodes:
            node.next = None
        self.head = None
        self.size = 0
        return

    def get_data(self, data):


        allNodes = [node for node in self.iterate_modification()]
        for node in allNodes:
            if node.data == data:
                return data
        return False


    def delete(self, data):


        allNodes = [node for node in self.iterate_modification()]
        for node in allNodes:
            if node.next.data == data:
                node.next = node.next.next
                node.next.next.prev = node
                self.size -= 1
                return





class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, element):
        self.stack.append(element)
        return

    def pop(self):
        return self.stack.pop(0)

    def top(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)




class MyQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, element):
        self.queue.append(element)
        return

    def pop(self):
        return self.queue.pop(0)

    def show_left(self):
        return self.queue[0]

    def show_right(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)











