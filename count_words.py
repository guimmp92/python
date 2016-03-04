#!/usr/bin/python

"""
Count the number of words in a string.

https://github.com/juchem/prep/blob/master/exercises.md
"""
from collections import Counter


def count_words_pythonic(s):
    """
    >>> count_words_pythonic("Count the number of words in a string.  ")
    8
    """
    count = Counter(s.strip().split(' '))
    return len(count)


def count_words(s):
    """
    >>> count_words("Count the number of words in a string.  ")
    8
    """
    count = 0
    letters = "abcdefghijklmnopqrstuvwxyz."

    on_word = False
    for c in s.strip().lower():
        if c in letters and not on_word:
            on_word = True
            continue
        if c == ' ' and on_word:
            on_word = False
            count += 1
    count += 1  # account for the last word

    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
