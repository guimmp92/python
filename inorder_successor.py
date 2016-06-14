#!/usr/bin/python

"""
Given a Binary Tree where each node has following structure, write a function to
populate next pointer for all nodes. The next pointer for every node should be set to
point to inorder successor.

struct node
{
  int data;
  struct node* left;
  struct node* right;
  struct node* next;
}

http://www.geeksforgeeks.org/populate-inorder-successor-for-all-nodes/
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


prev = None


def inorder1(node):
    global prev
    if not node:
        return
    inorder1(node.left)
    if prev:
        prev.next = node
    prev = node
    inorder1(node.right)


def inorder2(node, prev):
    if not node:
        return
    inorder2(node.left, prev)
    if prev[0]:
        prev[0].next = node
    prev[0] = node
    inorder2(node.right, prev)


if __name__ == "__main__":
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)
    root.left.right = Node(25)
    root.left.left.left = Node(0)
    root.left.right.left = Node(22)
    root.left.right.left.right = Node(23)
    root.right = Node(40)
    root.right.right = Node(45)
    root.right.left = Node(35)
    #inorder1(root)
    prev = [None]
    inorder2(root, prev)

    res = []
    node = root.left.left.left
    while node:
        res.append(node.value)
        node = node.next
    print ",".join([str(n) for n in res])
