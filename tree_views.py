#!/usr/bin/python

"""
Print left, right, top and bottom view of binary tree.
"""
from collections import deque
from bintree import Node


def visit_left_view(node, prev_level, cur_level):
    if not node:
        return
    if cur_level > prev_level[0]:
        print node.key
        prev_level[0] = cur_level
    visit_left_view(node.left, prev_level, cur_level+1)
    visit_left_view(node.right, prev_level, cur_level+1)


def left_view_recursive(root):
    prev_level = [0]
    visit_left_view(root, prev_level, 1)


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


def visit_right_view(node, prev_level, cur_level):
    if not node:
        return
    if cur_level > prev_level[0]:
        print node.key
        prev_level[0] = cur_level
    visit_right_view(node.right, prev_level, cur_level+1)
    visit_right_view(node.left, prev_level, cur_level+1)


def right_view_recursive(root):
    prev_level = [0]
    visit_right_view(root, prev_level, 1)


def top_view_iterative(root):
    queue = deque()
    queue.appendleft((root, 0))
    view = dict()
    while queue:
        node, idx = queue.pop()
        if not view.get(idx):
            view[idx] = node.key
        if node.left:
            queue.appendleft((node.left, idx-1))
        if node.right:
            queue.appendleft((node.right, idx+1))
    for i in sorted(view):
        print view[i]


def bottom_view_iterative(root):
    queue = deque()
    distances = dict()
    queue.append((root, 0))  # node and its horizontal distance
    while queue:
        node, hd = queue.pop()
        distances[hd] = node.key
        if node.left:
            queue.appendleft((node.left, hd-1))
        if node.right:
            queue.appendleft((node.right, hd+1))
    for hd in sorted(distances):
        print distances[hd]


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

    print "Right view (recursive)"
    right_view_recursive(root)

    print "Top view (iterative)"
    top_view_iterative(root)

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)

    print "Top view (iterative)"
    top_view_iterative(root)

    print "Bottom view (iterative)"
    bottom_view_iterative(root)
