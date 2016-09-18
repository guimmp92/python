#!/usr/bin/python
# vim: foldlevel=0

"""
Given an array with unique characters arr and a string str, find the smallest substring
of str containing all characters of arr.

Example:
arr: [x,y,z], str: xyyzyzyx
result: zyx

Implement your solution and analyze the runtime complexity.

https://www.pramp.com/question/wqNo9joKG6IJm67B6z34
"""


def solution(arr, text):
    """
    Time complexity: O(n)
    >>> solution(['x', 'y', 'z'], "xyyzyzyx")
    'zyx'
    >>> solution(['x', 'y', 'z'], "xyyzxyzyx")
    'yzx'
    >>> solution(['x', 'y', 'z'], "xyyyyzyzy")
    'xyyyyz'
    >>> solution(['x', 'y', 'z'], "xxyxyxyxxxyxxxz")
    'yxxxz'
    >>> solution(['t', 'i', 's'], "this is a test string")
    'this'
    """
    minsofar = text
    tracker = dict()
    for i in range(len(text)):
        if text[i] in arr:
            tracker[text[i]] = i
        if len(tracker) == len(arr):
            min_idx = min(tracker.values())
            if i-min_idx+1 < len(minsofar):
                minsofar = text[min_idx:i+1]
    return minsofar


def is_valid(window, arr):
    return all([window[ord(c)] > 0 for c in arr])


def solution2(arr, text):
    """
    Time complexity: O(n)
    >>> solution2(['x', 'y', 'z'], "xyyzyzyx")
    'zyx'
    >>> solution2(['x', 'y', 'z'], "xyyzxyzyx")
    'yzx'
    >>> solution2(['x', 'y', 'z'], "xyyyyzyzy")
    'xyyyyz'
    >>> solution2(['x', 'y', 'z'], "xxyxyxyxxxyxxxz")
    'yxxxz'
    >>> solution2(['t', 'i', 's'], "this is a test string")
    'this'
    """
    res = ""
    minsofar = len(text)
    lo = 0
    window = [0] * 256
    for hi in range(len(text)):
        # Add new character to window
        window[ord(text[hi])] += 1

        # Remove trailing characters from window and check if we have a new smallest
        while is_valid(window, arr):
            if hi-lo+1 < minsofar:
                minsofar = hi-lo+1
                res = text[lo:hi+1]
            window[ord(text[lo])] -= 1
            lo += 1
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
