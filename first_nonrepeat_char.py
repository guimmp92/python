#!/usr/bin/python

"""
Given a stream of characters, find the first non-repeating character.
"""

from collections import deque

print "Enter a string a ascii characters"
data = raw_input()  # "abcda1234bc45a1"
stream = (c for c in data)

repeating_chars = []
non_repeating_chars = deque()


def first_non_repeat_char():
    next_char = stream.next()

    if next_char not in repeating_chars:
        if next_char in non_repeating_chars:
            non_repeating_chars.remove(next_char)
            repeating_chars.append(next_char)
        else:
            non_repeating_chars.append(next_char)

    return non_repeating_chars[0]

for i in range(len(data)):
    print first_non_repeat_char()
