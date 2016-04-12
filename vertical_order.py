#!/usr/bin/python

"""
Vertical ordering of binary tree.
"""
from collections import defaultdict, deque
from bintree import Node


def vertical_order(root):
    queue = deque()
    queue.appendleft((root, 0))
    distances = defaultdict(list)
    while queue:
        node, hd = queue.pop()
        distances[hd].append(node.key)
        if node.left:
            queue.appendleft((node.left, hd-1))
        if node.right:
            queue.appendleft((node.right, hd+1))
    for hd in sorted(distances):
        print ", ".join([str(k) for k in distances[hd]])


if __name__ == "__main__":
    root = Node(12)
    root.left = Node(10)
    root.right = Node(20)
    root.right.left = Node(25)
    root.right.right = Node(40)
    root.right.left.right = Node(3)

    print "Vertical ordering"
    vertical_order(root)
