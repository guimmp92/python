#!/usr/bin/python

"""
Print left view of binary tree.
"""
from collections import deque
from bintree import Node


def visit(node, prev_level, cur_level):
    if not node:
        return
    if cur_level > prev_level[0]:
        print node.key
        prev_level[0] = cur_level
    visit(node.left, prev_level, cur_level+1)
    visit(node.right, prev_level, cur_level+1)


def left_view_recursive(root):
    prev_level = [0]
    visit(root, prev_level, 1)


def left_view_iterative(root):
    queue = deque()
    queue.appendleft((root, 1))
    prev_level = 0
    while queue:
        node, level = queue.pop()
        if level > prev_level:
            print node.key
            prev_level = level
        if node.left:
            queue.appendleft((node.left, level+1))
        if node.right:
            queue.appendleft((node.right, level+1))


if __name__ == "__main__":
    root = Node(12)
    root.left = Node(10)
    root.right = Node(20)
    root.right.left = Node(25)
    root.right.right = Node(40)
    root.right.left.right = Node(3)

    print "Left view (recursive)"
    left_view_recursive(root)

    print "Left view (iterative)"
    left_view_iterative(root)
