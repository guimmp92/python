#!/usr/bin/python
# vim: foldlevel=0

"""
Reverse the words in a sentence, i.e. My name is Chris becomes Chris is name My.
Optimize for time and space.

http://nbl.cewit.stonybrook.edu/algowiki/index.php/Data-structures-TADM2E-2
https://www.pramp.com/question/VKdqbrq6B1S5XAyGAOn4
"""


def reverse(s, i, j):
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


def solution(s):
    """
    >>> solution(['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e'])
    ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't']
    >>> solution(['p', 'e', 'r', 'f', 'e', 'c', 't'])
    ['p', 'e', 'r', 'f', 'e', 'c', 't']
    """
    lo = 0
    for hi in range(len(s)):
        if s[hi] == ' ':
            reverse(s, lo, hi-1)
            lo = hi+1
    reverse(s, lo, hi)
    reverse(s, 0, len(s)-1)
    return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
