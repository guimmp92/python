#!/usr/bin/python

"""
Read a string of parentheses from left to right and decide whether the symbols are
balanced.
http://interactivepython.org/runestone/static/pythonds/BasicDS/SimpleBalancedParentheses.html
"""

print "Enter a string of parentheses:"
s = raw_input()

def check_parens(s):
    tracker = 0
    for c in s:
        if c == "(":
            tracker += 1
        elif c == ")":
            tracker -= 1
            if tracker < 0:
                return False
    if tracker == 0:
        return True
    return False

print check_parens(s)
