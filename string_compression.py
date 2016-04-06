#!/usr/bin/python

"""
Perform a basic string compression using the counts of repeated characters.
"""


def solution(s):
    """
    >>> solution("aabcccccaaa")
    'a2b1c5a3'
    """
    comp_s = list()
    start, count = 0, 1
    for i in range(1, len(s)):
        if s[i] == s[start]:
            count += 1
            continue
        comp_s.append(s[start])
        comp_s.append(str(count))
        start = i
        count = 1
    comp_s.append(s[start])
    comp_s.append(str(count))
    return "".join(comp_s)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
