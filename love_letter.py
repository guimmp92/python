#!/usr/bin/python

"""
You have written an anonymous love letter and you don't want your handwriting to be
recognized. Since you don't have a printer within reach, you are trying to write this
letter by copying and pasting characters from a newspaper.

Given a string L representing the letter and a string N representing the newspaper,
return true if the L can be written entirely from N and false otherwise. The letter
includes only ascii characters.
"""
from collections import Counter
from operator import add


def solution(L, N):
    """
    >>> solution("the love letter", "this is the newspaper string lol total vote")
    True
    >>> solution("the love letter", "this is the newspaper string")
    False
    """
    letter = Counter(L)
    count = reduce(add, letter.values())
    for c in N:
        if c in letter and letter[c] >= 1:
            letter[c] -= 1
            count -= 1
        if count == 0:
            return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
