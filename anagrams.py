#!/usr/bin/python

"""
How to check if a string contains an anagram of another string?

Example: The string "coding interview questions" contains an anagram of the string
"weivretni".

http://blog.gainlo.co/index.php/2016/04/08/if-a-string-contains-an-anagram-of-another-string/
"""
from collections import defaultdict


def solution(a, b):
    """
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


def solution1(a, b):
    """
    >>> solution1("coding interview questions", "weivretni")
    True
    >>> solution1("coding interviw questions", "weivretni")
    False
    >>> solution1("coding interview questions", "abcde")
    False
    """
    target_hash, rolling_hash = 0, 0
    for i in range(len(b)):
        target_hash += ord(b[i]) // 101
        rolling_hash += ord(a[i]) // 101

    i = 0
    for j in range(len(b), len(a)):
        if rolling_hash == target_hash:
            return True
        rolling_hash += ord(a[j]) // 101
        rolling_hash -= ord(a[i]) // 101
        i += 1
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
