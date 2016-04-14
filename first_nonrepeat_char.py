#!/usr/bin/python

"""
Given a stream of characters, find the first non-repeating character.
"""
from collections import deque


def first_non_repeat(stream):
    repeated = [0] * 256  # ascii
    non_repeated = deque()
    try:
        while True:
            c = next(stream)
            print "\nNext character: {0}".format(c)
            if not repeated[ord(c)]:
                if c in non_repeated:
                    non_repeated.remove(c)
                    repeated[ord(c)] = 1
                else:
                    non_repeated.appendleft(c)
            print "First non repeated character: {0}".format(non_repeated[-1])
    except StopIteration:
        print "\nEnd of stream"

print "Enter a string a ascii characters"
data = raw_input()  # "abcda1234bc45a1"
stream = (c for c in data)
first_non_repeat(stream)
