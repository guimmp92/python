import random


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, value):
        """ Add new node at the head of the linked list. """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return new_node

    def pop(self, value):
        prev, cur = self.head, self.head
        while cur:
            if cur.value == value:
                prev.next = cur.next
                if cur == self.head:
                    self.head = cur.next
                self.count -= 1
                return cur
            prev, cur = cur, cur.next

    def __str__(self):
        res = ""
        cur = self.head
        while cur:
            res += str(cur.value)
            res += " "
            cur = cur.next
        return res


def randlinkedlist(size=10):
    linkedlist = LinkedList()
    for i in range(size):
        linkedlist.push(random.randint(0, 50))
    return linkedlist
