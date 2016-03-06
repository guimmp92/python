#!/usr/bin/python

"""
https://www.pramp.com/question/pK6A4GA5YES09qKmqG33

Given a root of a binary search tree and a key x, find the largest key in the tree that
is smaller than x.

Example: if an in-order list of all keys in the tree is {2, 3, 4, 7, 17, 19, 21, 35, 89}
and x is 19, the biggest key that is smaller than x is 17.
"""


def solution(root, x):
    cur = root
    while cur:
        if cur.key < x:
            if not cur.right:
                return cur.key
            cur = cur.right
        else:
            cur = cur.left


if __name__ == "__main__":
    import doctest
    doctest.testmod()
