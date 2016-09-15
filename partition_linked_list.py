#!/usr/bin/python
# vim: foldlevel=0

"""
Write code to partition a linked list around a value x, such that all nodes less
than x come before all nodes greater than or equal to x.

CTCI p188
"""


def solution(head):
    before_head, before_tail = None, None
    after_head, after_tail = None, None
    node = head
    while node:
        if node.key < x:
            if not before_head:
                before_head, before_tail = node, node
            else:
                before_tail.next, before_tail = node, node
        else:
            if not after_head:
                after_head, after_tail = node, node
            else:
                after_tail.next, after_tail = node, node
        node = node.next

    after_tail = None
    if before_head:
        tail.next = after_head
        return before_head
    else:
        return after_head
