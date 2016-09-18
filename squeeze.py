#!/usr/bin/python
# vim: foldlevel=0

"""
Write a function that removes characters from a string.
Programming Interviews Exposed p83
"""


def squeeze(text, chars):
    text = list(text)
    i = 0
    for j in range(len(text)):
        if text[j] not in chars:
            text[i], text[j] = text[j], text[i]
            i += 1
    return ''.join(text[:i])


print squeeze('the dog barked at the mailman', 'tim')
