#!/usr/bin/python
# vim: foldlevel=0

"""
Delete a node in the middle of a singly linked list, given only access to that node.
"""
from linked_list import randlinkedlist


def solution(node):
    if not node or not node.next:
        return
    next = node.next
    node.value = next.value
    node.next = next.next


if __name__ == "__main__":
    def _print(head):
        cur = head
        while cur:
            print cur.value
            cur = cur.next

    ll = randlinkedlist()
    print "Original linked list: "
    _print(ll.head)

    node = ll.head
    for i in range(5):
        node = node.next

    solution(node)
    print "New linked list: "
    _print(ll.head)
