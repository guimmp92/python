#!/usr/bin/python

"""
Find the longest substring with k unique characters.

Example: If the string is "aabbccdd", if K is 1, the longest substring can be "aa".
If K is 2, the longest substring can be "aabb".
If K is 3, the longest substring can be "aabbcc".

http://blog.gainlo.co/index.php/2016/04/12/find-the-longest-substring-with-k-unique-characters/
http://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
"""
from collections import defaultdict


def count_uniques(uniques):
    return len([e for e in uniques if e != 0])


def solution(text, k):
    """
    >>> solution("aabbccdd", 1)
    'aa'
    >>> solution("aabbccdd", 2)
    'aabb'
    >>> solution("aabbccdd", 3)
    'aabbcc'
    >>> solution("abacbebebe", 3)
    'cbebebe'
    >>> solution("abacbbeb", 3)
    'abacbb'
    >>> solution("ababebebe", 4)
    ''
    """
    res = ""
    maxsofar = 0
    i = 0
    uniques = [0] * 256
    for j in range(len(text)):
        uniques[ord(text[j])] += 1
        while count_uniques(uniques) > k:
            uniques[ord(text[i])] -= 1
            i += 1
        if count_uniques(uniques) == k:
            if j-i+1 > maxsofar:
                maxsofar = j-i+1
                res = text[i:j+1]
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
