#!/usr/bin/python

"""
Write a function to compare whether two binary trees are identical.
http://nbl.cewit.stonybrook.edu/algowiki/index.php/Data-structures-TADM2E-2
"""

import copy

from bintree import randbintree

t1 = randbintree()
print "Tree #1:"
t1.print_tree()

t2 = randbintree()
print "Tree #2:"
t2.print_tree()

t3 = t1.duplicate()
print "Tree #3:"
t3.print_tree()

t4 = copy.deepcopy(t1)
print "Tree #4:"
t4.print_tree()


def compare_bintrees(node1, node2):
    if node1 is None and node2 is None:
        return True

    if node1 is not None and node2 is not None:
        return node1.key == node2.key and \
               compare_bintrees(node1.left, node2.left) and \
               compare_bintrees(node1.right, node2.right)

    return False

print compare_bintrees(t1.root, t2.root)  # should return False
print compare_bintrees(t1.root, t3.root)  # should return True
print compare_bintrees(t1.root, t4.root)  # should return True
print compare_bintrees(t2.root, t2.root)  # should return True
