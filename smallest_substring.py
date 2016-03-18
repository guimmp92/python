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


def solution(arr, str):
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
    min_so_far = len(str)
    start, end = 0, len(str)-1
    tracker = dict()
    min_idx = 0
    for i in range(len(str)):
        tracker[str[i]] = i
        if len(tracker) != len(arr):
            continue
        min_idx = reduce(min, tracker.values())
        min_ending_here = i - min_idx + 1
        if min_ending_here < min_so_far:
            start, end = min_idx, i
            min_so_far = min_ending_here
    return str[start:end+1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
