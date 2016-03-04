#!/usr/bin/python

"""
Find all permutations of a string.
"""


def find_permutations(chars, stop_limit, perm):
    if len(perm) == stop_limit:
        print "Found a permutation: {0}".format("".join(perm))
        return
    for c in chars[:]:
        perm.append(c)
        chars.remove(c)
        find_permutations(chars, stop_limit, perm)
        chars.append(c)
        perm.pop()

text = "hat"
find_permutations(list(text), len(text), [])
