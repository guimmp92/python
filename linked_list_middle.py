#!/usr/bin/python

"""
Write a function to find the middle node of a singly-linked list.
http://nbl.cewit.stonybrook.edu/algowiki/index.php/Data-structures-TADM2E-2
"""

from linked_list import randlinkedlist

ll = randlinkedlist(size=9)
print "The linked list: {0}".format(ll)

slow, fast = ll.head, ll.head
while fast:
    if fast.next is None:
        break
    slow, fast = slow.next, fast.next.next

print "The middle of the linked list: {0}".format(slow.value)
