#!/usr/bin/python
# vim: foldlevel=0

"""
Perform a basic string compression using the counts of repeated characters.
"""


def solution(s):
    """
    >>> solution("aabcccccaaa")
    'a2b1c5a3'
    """
    res = []
    i = 0
    for j in range(1, len(s)):
        if s[j] != s[i]:
            res.append(s[i])
            res.append(str(j-i))
            i = j
    res.append(s[i])
    res.append(str(j-i+1))
    return ''.join(res)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
