#!/usr/bin/python

"""
Given a node n in a binary search tree, explain and code the most efficient way to find
the successor of n. Analyze the runtime complexity of your solution.
"""


def solution(root, n):
    successor = None
    node = root
    while node:
        if node.key > n:
            successor = node.key
            node = node.left
        else:
            node = node.right
    return successor


if __name__ == "__main__":
    import doctest
    doctest.testmod()
