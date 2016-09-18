#!/usr/bin/python
# vim: foldlevel=0

"""
Given an array with unique characters arr and a string str, find the smallest
substring of str containing all characters of arr.

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
    def _has_all_chars(arr, tracker):
        return all(tracker[ord(c)] > 0 for c in arr)

    res = text
    lo = 0
    tracker = [0] * 256
    for hi in range(len(text)):
        # Add new character to window
        tracker[ord(text[hi])] += 1

        # Remove trailing characters from window and check if we have a new smallest
        while _has_all_chars(arr, tracker):
            if hi-lo+1 < len(res):
                res = text[lo:hi+1]
            tracker[ord(text[lo])] -= 1
            lo += 1
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
