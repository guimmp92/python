#!/usr/bin/python

"""
Write a program to reverse the direction of a given singly-linked list.
In other words, after the reversal all pointers should now point backwards.
Your algorithm should take linear time.
http://nbl.cewit.stonybrook.edu/algowiki/index.php/Data-structures-TADM2E-2
"""

from linked_list import randlinkedlist

ll = randlinkedlist()
print "The linked list: {0}".format(ll)

def reverse_iterative(linked_list):
    prev, cur = None, linked_list.head
    while cur:
        nnext = cur.next
        cur.next = prev
        if nnext is None:
            linked_list.head = cur
        prev, cur = cur, nnext


def _reverse(node, prev):
    if node is None:
        return prev
    nnext = node.next
    node.next = prev
    return _reverse(nnext, node)


def reverse_recursive(linked_list):
    new_head = _reverse(linked_list.head, None)
    linked_list.head = new_head


reverse_iterative(ll)
print "The reversed linked list (iterative): {0}".format(ll)

reverse_recursive(ll)
print "The reversed linked list (recursive): {0}".format(ll)
