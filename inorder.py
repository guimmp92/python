#!/usr/bin/python

"""
Part 1: Given a binary search tree, print the elements in-order iteratively without using
recursion.

Part 2: Same problem but this time w/o using a stack or any additional memory.

http://stackoverflow.com/questions/2116662/help-me-understand-inorder-traversal-without-using-recursion
http://articles.leetcode.com/binary-search-tree-in-order-traversal
"""
from bintree import randbintree


def inorder_recursive(node):
    if not node:
        return
    inorder_recursive(node.left)
    print node.key
    inorder_recursive(node.right)


def inorder_recursive2(node):
    while node:
        inorder_recursive2(node.left)
        print node.key
        node = node.right


def inorder_iterative(root):
    stack = list()
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print node.key
            node = node.right


if __name__ == "__main__":
    t = randbintree()
    print "The binary tree"
    t.print_tree()

    print "In-order traversal"
    inorder_iterative(t.root)
