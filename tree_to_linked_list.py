#!/usr/bin/python

"""
Write a program to convert a binary search tree into a linked list.
http://nbl.cewit.stonybrook.edu/algowiki/index.php/Data-structures-TADM2E-2
"""

from collections import deque

from bintree import randbintree
from linked_list import LinkedList

t = randbintree()
print "The binary tree"
t.print_tree()

queue = deque()


def process_tree_node(tnode):
    if tnode is None:
        return
    # In-order traversal
    process_tree_node(tnode.left)
    queue.appendleft(tnode.key)
    process_tree_node(tnode.right)


def convert_into_linked_list(t):
    process_tree_node(t.root)
    ll = LinkedList()
    while queue:
        ll.push(queue.pop())
    return ll


print "The linked list"
print convert_into_linked_list(t)
