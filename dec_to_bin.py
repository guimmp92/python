#!/usr/bin/python

"""
Convert an integer number (base 10) into its binary representation.
"""

print "Enter a pattern string:"
num = int(raw_input())

def convert_to_bin(num):
    stack = []
    while num != 0:
        stack.append(num % 2)
        num //= 2

    res = ""
    while stack:
        res += str(stack.pop())

    return res

print convert_to_bin(num)
