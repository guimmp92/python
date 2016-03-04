#!/usr/bin/python

"""
Given a text string t and a pattern string p, does t contain the pattern p
as a substring and if so where?

Example: Is the substring abba in the string aababba?
"""

print "Enter a pattern string:"
p = raw_input()
print "Enter a text string:"
t = raw_input()


def findmatch(pattern, text):
    for i1, c1 in enumerate(text):
        for i2, c2 in enumerate(pattern):
            if t[i1+i2] != c2:
                break
        else:
            return True
    return False

print findmatch(p, t)
