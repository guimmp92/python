#!/usr/bin/python

"""
Problem 1: Add two numbers represented by two linked lists in reverse order, and return
the sum as a linked list.

Problem 2: Same as above but the input linked lists are in forward order.
"""
from linked_list import Node, randlinkedlist


def add_linked_lists(node1, node2, carry):
    if not node1 and not node2:
        if carry:
            return Node(carry)
        return
    if not node1:
        q, r = divmod(node2.value + carry, 10)
        n1, n2 = node1, node2.next
    elif not node2:
        q, r = divmod(node1.value + carry, 10)
        n1, n2 = node1.next, node2
    else:
        q, r = divmod(node1.value + node2.value + carry, 10)
        n1, n2 = node1.next, node2.next
    node = Node(r)
    node.next = add_linked_lists(n1, n2, q)
    return node


def solution(head1, head2):
    return add_linked_lists(head1, head2, 0)


if __name__ == "__main__":
    def _print(head):
        cur = head
        while cur:
            print cur.value
            cur = cur.next

    ll1 = randlinkedlist(3, max=9)
    ll2 = randlinkedlist(5, max=9)
    print "Linked list 1:"
    _print(ll1.head)
    print "Linked list 2:"
    _print(ll2.head)

    print "Sum of linked lists:"
    _print(solution(ll1.head, ll2.head))
