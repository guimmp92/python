#!/usr/bin/python
# vim: foldlevel=0

"""
Write a program to determine the lowest common ancestor of two nodes in a binary
tree (not necessarily a binary search tree).
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    """
               6
            /     \
           8       2
         /  \    /  \
       13   20  0    4
           /   \
          10    9
    """
    root = Node(6)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(13)
    root.left.right = Node(20)
    root.left.right.left = Node(10)
    root.left.right.right = Node(9)
    root.right.left = Node(0)
    root.right.right = Node(4)
    return root


def find(root, val):
    if not root:
        return False
    if root.value == val:
        return True
    return find(root.left, val) or find(root.right, val)


def lca(node, x, y):
    if not node:
        return
    if node.value == x or node.value == y:
        return node.value
    xleft = find(node.left, x)
    yleft = find(node.left, y)
    if xleft != yleft:
        return node.value
    if xleft and yleft:
        return lca(node.left, x, y)
    else:
        return lca(node.right, x, y)


def solution1(root, x, y):
    ''' Time complexity of O(n) '''
    return lca(root, x, y)


def lca2(node, x, y):
    if not node:
        return
    if node.value == x or node.value == y:
        return node.value
    left = lca2(node.left, x, y)
    if left is not None and left not in (x, y):
        return left
    right = lca2(node.right, x, y)
    if right is not None and right not in (x, y):
        return right
    if left is not None and right is None:
        return left
    if right is not None and left is None:
        return right
    if left is not None and right is not None:
        return node.value


def solution2(root, x, y):
    ''' Time complexity of O(n), but more efficient than solution1 by a constant '''
    return lca2(root, x, y)


if __name__ == "__main__":
    root = build_tree()
    assert solution1(root, 8, 2) == 6
    assert solution1(root, 13, 9) == 8
    assert solution1(root, 13, 20) == 8
    assert solution1(root, 10, 9) == 20
    assert solution1(root, 10, 4) == 6
    assert solution1(root, 0, 4) == 2

    assert solution2(root, 8, 2) == 6
    assert solution2(root, 13, 9) == 8
    assert solution2(root, 13, 20) == 8
    assert solution2(root, 10, 9) == 20
    assert solution2(root, 10, 4) == 6
    assert solution2(root, 0, 4) == 2
