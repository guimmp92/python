#!/usr/bin/python

"""
Check if a string is a palindrome, e.g. radar.
"""

from collections import deque

print "Enter a string:"
text = raw_input()

def is_palindrome(text):
    d = deque()
    for c in text:
        d.appendleft(c)
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True

print is_palindrome(text)
