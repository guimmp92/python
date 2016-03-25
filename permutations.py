#!/usr/bin/python

"""
Find all permutations of a string.
"""


def find_permutations(chars, cur):
    if len(cur) == len(chars):
        print "Found a permutation: {0}".format("".join(cur))
        return
    for c in set(chars)-set(cur):
        cur.append(c)
        find_permutations(chars, cur)
        cur.pop()

text = "hat"
find_permutations(list(text), [])
