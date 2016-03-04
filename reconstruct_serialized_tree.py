#!/usr/bin/python

"""
Given a serialized tree, reconstruct the tree in memory and return the root of the tree.
https://www.reddit.com/r/cscareerquestions/comments/111yyj/what_are_some_good_technical_things_to_know_for/c6imw32
"""

from collections import namedtuple

serialized_tree = (('b', 'c'), ('b', 'd'), ('a', 'b'), ('a', 'f'), ('d', 'g'))
tree = {}
node = namedtuple('Node', ('value', 'children'))
root = None

for link in serialized_tree:
    parent, child = link
    if parent not in tree:
        tree.setdefault(parent, node(value=parent, children=[]))
    if child not in tree:
        tree.setdefault(child, node(value=child, children=[]))
    tree[parent].children.append(tree[child])

for key in tree.keys():
    if key not in tree:
        continue  # we've already deleted the key
    for child in tree[key].children:
        del tree[child.value]  # delete the key

print tree.popitem()
