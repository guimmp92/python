#!/usr/bin/python

"""
Write a function to determine if a binary tree is a binary search tree.

http://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
"""
import sys

from bintree import Node


def is_bst(node, min, max):
    if not node:
        return True
    if min > node.key or node.key > max:
        return False
    return is_bst(node.left, min, node.key) and is_bst(node.right, node.key, max)


def solution():
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(50)
    assert is_bst(root, -sys.maxint-1, sys.maxint) == False
    root.left.left = Node(10)
    assert is_bst(root, -sys.maxint-1, sys.maxint) == True
    root.right = Node(40)
    root.right.right = Node(0)
    root.left.right = Node(25)
    root.left.left.left = Node(0)
    assert is_bst(root, -sys.maxint-1, sys.maxint) == False
    root.right.right = Node(45)
    root.right.left = Node(35)
    assert is_bst(root, -sys.maxint-1, sys.maxint) == True


def is_bst2(node, prev):
    if not node:
        return True
    if not is_bst2(node.left, prev):
        return False
    if node.key < prev[0]:
        return False
    prev[0] = node.key
    return is_bst2(node.right, prev)


def solution2():
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(50)
    assert is_bst2(root, [-sys.maxint-1]) == False
    root.left.left = Node(10)
    assert is_bst2(root, [-sys.maxint-1]) == True
    root.right = Node(40)
    root.right.right = Node(0)
    root.left.right = Node(25)
    root.left.left.left = Node(0)
    assert is_bst2(root, [-sys.maxint-1]) == False
    root.right.right = Node(45)
    root.right.left = Node(35)
    assert is_bst2(root, [-sys.maxint-1]) == True


if __name__ == "__main__":
    solution()
    solution2()
