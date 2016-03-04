#!/usr/bin/python

"""
Write a function that removes characters from a string.
Programming Interviews Exposed p83
"""


def squeeze(text, chars):
    text = list(text)
    to_copy = 0
    for idx, char in enumerate(text):
        if char not in chars:
            text[to_copy] = text[idx]
            to_copy += 1
    for i in range(len(text)-to_copy):
        text.pop()
    return "".join(text)

print squeeze("Bonjour monsieur le codeur", "jnr")  # Boou mosieu le codeucodeur
