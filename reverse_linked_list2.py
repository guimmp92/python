#!/usr/bin/python
# vim: foldlevel=0

"""
Reverse a linked list in groups of size k.

http://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
"""
from linked_list import randlinkedlist

ll = randlinkedlist()
print "The linked list: {0}".format(ll)


def reverse_linked_list(head, k):
    if not head:
        return
    node = head
    prev, next = None, None
    count = 0
    while node and count < k:
        next = node.next
        node.next = prev
        prev, node = node, next
        count += 1
    head.next = reverse_linked_list(node, k)
    return prev


ll.head = reverse_linked_list(ll.head, 3)
print "The reversed linked list (iterative): {0}".format(ll)
