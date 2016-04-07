#!/usr/bin/python

"""
Remove duplicates from an unsorted linked list.
"""
from linked_list import randlinkedlist


def solution1(head):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    counter = dict()
    back, cur = None, head
    while cur:
        if not counter.get(cur.value):
            counter[cur.value] = 1
            if back:
                back.next = cur
            back = cur
        cur = cur.next
    back.next = None


def solution2(head):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    cur = head
    while cur:
        runner = cur
        while runner.next:
            if runner.next.value == cur.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next


if __name__ == "__main__":
    def _print(head):
        cur = head
        while cur:
            print cur.value
            cur = cur.next

    ll = randlinkedlist(max=10)
    print "Original linked list: "
    _print(ll.head)
    solution1(ll.head)
    print "Cleaned up linked list: "
    _print(ll.head)
