#!/usr/bin/python

"""
Determine whether a linked list contains a loop as quickly as possible without using
any extra storage. Also, identify the location of the loop.
http://nbl.cewit.stonybrook.edu/algowiki/index.php/Data-structures-TADM2E-2
"""

from linked_list import randlinkedlist

ll = randlinkedlist(size=20)
print str(ll)


def find_cycle(llist):
    slow, fast = llist.head, llist.head
    while fast:
        if fast.next is None:
            break
        if fast.next == slow:
            return True
        slow, fast = slow.next, fast.next.next
    return False

print find_cycle(ll)  # should return False

cur = ll.head
cycle_start = None
for i in range(ll.count-1):
    if i == 4:
        cycle_start = cur
    cur = cur.next
cur.next = cycle_start

print find_cycle(ll)  # should return True
