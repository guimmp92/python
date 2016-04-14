#!/usr/bin/python

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
    >>> solution(['x', 'y', 'z'], "xyyzyzyx")
    'zyx'
    >>> solution(['x', 'y', 'z'], "xyyzxyzyx")
    'yzx'
    >>> solution(['x', 'y', 'z'], "xyyyyzyzy")
    'xyyyyz'
    >>> solution(['x', 'y', 'z'], "xxyxyxyxxxyxxxz")
    'yxxxz'
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
