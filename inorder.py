#!/usr/bin/python

"""
Given a binary search tree, print the elements in-order iteratively without using
recursion.

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
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            print cur.key
            cur = cur.right


if __name__ == "__main__":
    t = randbintree()
    print "The binary tree"
    t.print_tree()

    print "In-order traversal"
    inorder_iterative(t.root)
