#!/usr/bin/python
# vim: foldlevel=0

"""
Write a function to determine if a binary tree is balanced.
"""
from bintree import Node


def is_balanced(node):
    if not node:
        return 0
    left_height = is_balanced(node.left)
    if left_height == -1:
        return -1
    right_height = is_balanced(node.right)
    if right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1


def solution():
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)
    assert is_balanced(root) == -1
    root.right = Node(40)
    root.left.right = Node(25)
    root.left.left.left = Node(0)
    assert is_balanced(root) == -1
    root.right.left = Node(35)
    root.right.right = Node(45)
    assert is_balanced(root) == 4


if __name__ == "__main__":
    solution()
