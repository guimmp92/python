#!/usr/bin/python

"""
Level ordering of binary search tree.
"""
from collections import deque
from bintree import randbintree


def level_order_iterative(root):
    queue = deque()
    queue.appendleft(root)
    while queue:
        node = queue.pop()
        print node.key
        if node.left:
            queue.appendleft(node.left)
        if node.right:
            queue.appendleft(node.right)


def height(node):
    if not node:
        return 0
    lheight = height(node.left)
    rheight = height(node.right)
    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1


def print_level(root, level):
    if not root:
        return
    if level == 1:
        print root.key
    else:
        print_level(root.left, level-1)
        print_level(root.right, level-1)


def level_order_recursive(root):
    h = height(root)
    for level in range(1, h+1):
        print_level(root, level)


if __name__ == "__main__":
    t = randbintree()
    print "The binary tree"
    t.print_tree()

    print "Level order traversal"
    level_order_iterative(t.root)
