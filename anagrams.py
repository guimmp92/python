#!/usr/bin/python

"""
How to check if a string contains an anagram of another string?

Example: The string "coding interview questions" contains an anagram of the string
"weivretni".

ihttp://blog.gainlo.co/index.php/2016/04/08/if-a-string-contains-an-anagram-of-another-string/
"""
from collections import defaultdict


def solution(a, b):
    """
    Time complexity:
    >>> solution("coding interview questions", "weivretni")
    True
    >>> solution("coding interviw questions", "weivretni")
    False
    >>> solution("coding interview questions", "abcde")
    False
    """
    count = defaultdict(int)
    window = defaultdict(int)
    for i in range(len(b)):
        count[b[i]] += 1
        window[a[i]] += 1

    for i in range(len(a)-len(b)):
        if window == count:
            return True
        window[a[i+len(b)]] += 1
        window[a[i]] -= 1
        for j in window.keys():
            if window[j] == 0:
                del window[j]

    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
